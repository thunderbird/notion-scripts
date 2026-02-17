import logging
import asyncio
import notion_client

from sgqlc.endpoint.httpx import HTTPXEndpoint

from ..github_schema import schema
from sgqlc.operation import Operation

from ..util import AsyncRetryingClient

logger = logging.getLogger("gh_deployments")


class DeploymentsSync:
    """Deployment synchronizer.

    This is a hack to get the latest deployment dates and nicely place them on a page in notion.
    Configure the block mappings with the id of the block that should be updated and the repository.
    """

    DATE_FORMAT = "%B %d, %Y %H:%M:%S"

    def __init__(
        self,
        project_key,
        blocks,
        notion_token,
        github_token,
        expected_columns,
        stage_column,
        prod_column,
        dry=True,
    ):
        """Initialize deployment sync."""
        self.notion = notion_client.AsyncClient(auth=notion_token, client=AsyncRetryingClient(http2=True))
        self.blocks = blocks
        self.expected_columns = expected_columns
        self.stage_column = stage_column
        self.prod_column = prod_column
        self.dry = dry

        self.endpoint = HTTPXEndpoint(
            url="https://api.github.com/graphql",
            base_headers={"Authorization": f"Bearer {github_token}"},
            timeout=120.0,
            client=AsyncRetryingClient(http2=True),
        )

    def _richtext_field(self, text):
        return [{"type": "text", "text": {"content": text}}]

    async def synchronize(self):
        """Synchronize the configured repo deployment dates to the notion blocks/page."""
        op = Operation(schema.Query)

        if not len(self.blocks):
            logger.error("No blocks to synchronize")
            return

        for blockinfo in self.blocks:
            org, repo = blockinfo["repo"].split("/")
            alias = f"deployment_{org}_{repo.replace('-', '_')}"
            method = blockinfo.get("method", "releases")

            repository = op.repository(owner=org, name=repo, __alias__=alias)

            if method == "deployments":
                environments = [blockinfo.get("stage_env", "staging"), blockinfo.get("prod_env", "production")]
                deploy = repository.deployments(
                    first=50,
                    order_by={"field": "CREATED_AT", "direction": "DESC"},
                    environments=[env for env in environments if env is not None],
                )
                deploy.nodes.environment()
                deploy.nodes.state()
                deploy.nodes.commit_oid()
                deploy.nodes.created_at()
                status = deploy.nodes.latest_status()
                status.state()
                status.created_at()
            elif method == "releases":
                releases = repository.releases(first=100, order_by={"field": "CREATED_AT", "direction": "DESC"})

                releases.nodes.is_draft()
                releases.nodes.is_latest()
                releases.nodes.created_at()
                releases.nodes.published_at()
                releases.nodes.name()

        data = await self.endpoint(op)
        datares = op + data

        async with asyncio.TaskGroup() as tg:
            for blockinfo in self.blocks:
                org, repo = blockinfo["repo"].split("/")
                method = blockinfo.get("method", "releases")

                alias = f"deployment_{org}_{repo.replace('-', '_')}"
                res = getattr(datares, alias)

                stage_date = ""
                prod_date = ""

                if method == "deployments":
                    stage_date, prod_date = self.get_deployments_dates(blockinfo, res.deployments.nodes)
                elif method == "releases":
                    if not getattr(res, "releases", None):
                        logger.warning(f"Repository {blockinfo['repo']} has no releases")
                        continue
                    stage_date, prod_date = self.get_releases_dates(blockinfo, res.releases.nodes)
                else:
                    raise Exception("Unknown sync method " + method)

                tg.create_task(self._update_block(blockinfo["repo"], blockinfo["block_id"], stage_date, prod_date))

    def get_deployments_dates(self, blockinfo, deployments):
        """Gets the stage/prod dates via deployments."""
        stage_env_name = blockinfo.get("stage_env", "staging")
        prod_env_name = blockinfo.get("prod_env", "production")

        stage_date = ""
        prod_date = ""

        for node in deployments:
            env = node.environment
            if node.state != "ACTIVE":
                continue

            if node.latest_status.state != "SUCCESS":
                continue

            timestamp = node.created_at.strftime(self.DATE_FORMAT) if node.created_at else ""

            if env == stage_env_name and stage_date == "":
                stage_date = timestamp
                logger.debug(f"Using stage deployment for {blockinfo['repo']}: {str(node)}")

            elif env == prod_env_name and prod_date == "":
                prod_date = timestamp
                logger.debug(f"Using prod deployment for {blockinfo['repo']}: {str(node)}")

            if (stage_date or not stage_env_name) and (prod_date or not prod_env_name):
                break

        return stage_date, prod_date

    def get_releases_dates(self, blockinfo, releases):
        """Gets the stage/prod dates via releases."""
        stage_date = ""
        prod_date = ""

        for node in releases:
            if not stage_date and node.is_draft:
                logger.debug(f"Using stage release for {blockinfo['repo']}: {str(node)}")
                stage_date = node.created_at.strftime(self.DATE_FORMAT) if node.created_at else ""
            elif not prod_date and node.is_latest:
                logger.debug(f"Using prod release for {blockinfo['repo']}: {str(node)}")
                prod_date = node.published_at.strftime(self.DATE_FORMAT) if node.published_at else ""
            else:
                logger.debug(f"This release is not it for {blockinfo['repo']}: {str(node)}")

            if stage_date and prod_date:
                break

        return stage_date, prod_date

    async def _update_block(self, orgrepo, block_id, stage_date, prod_date):
        """Updates a block with the given stage and prod date."""
        row = await self.notion.blocks.retrieve(block_id)
        cells = row["table_row"]["cells"]

        if len(cells) != self.expected_columns:
            raise Exception("Table length changed, check columns!")

        cells[self.stage_column - 1] = self._richtext_field(stage_date)
        cells[self.prod_column - 1] = self._richtext_field(prod_date)

        logger.info(f"Updating block {block_id} for {orgrepo} to use stage: {stage_date} and prod: {prod_date}")

        if not self.dry:
            await self.notion.blocks.update(block_id, table_row=row["table_row"])

    async def get_page_contents(self, orgrepo, page_id):
        """Debug method to get page contents and children."""
        from pprint import pprint

        row = await self.notion.blocks.retrieve(page_id)
        pprint(row)

        row = await self.notion.blocks.children.list(page_id)
        pprint(row)


async def synchronize(**kwargs):  # pragma: no cover
    """Exported method to begin synchronization."""
    await DeploymentsSync(**kwargs).synchronize()
