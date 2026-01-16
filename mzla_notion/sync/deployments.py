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
        """Synchronize the configured repo deployments to the notion blocks/page."""
        op = Operation(schema.Query)

        if not len(self.blocks):
            logger.error("No blocks to synchronize")
            return

        for orgrepo in self.blocks.keys():
            org, repo = orgrepo.split("/")
            alias = f"deployment_{org}_{repo.replace('-', '_')}"

            repository = op.repository(owner=org, name=repo, __alias__=alias)

            deploy = repository.deployments(first=50, order_by={"field": "CREATED_AT", "direction": "DESC"})

            deploy.nodes.environment()
            deploy.nodes.state()
            status = deploy.nodes.latest_status()
            status.state()
            status.created_at()

        data = await self.endpoint(op)
        datares = op + data

        async with asyncio.TaskGroup() as tg:
            for orgrepo, block_id in self.blocks.items():
                org, repo = orgrepo.split("/")
                alias = f"deployment_{org}_{repo.replace('-', '_')}"
                res = getattr(datares, alias)

                stage_date = ""
                prod_date = ""

                for node in res.deployments.nodes:
                    env = node.environment
                    if node.latest_status.state != "SUCCESS":
                        continue

                    timestamp = node.latest_status.created_at or node.created_at
                    formatted_timestamp = timestamp.strftime(self.DATE_FORMAT) if timestamp else ""

                    # Not a typo, catches "staging" as well
                    if "stag" in env and stage_date == "":
                        stage_date = formatted_timestamp

                    elif "prod" in env and prod_date == "":
                        prod_date = formatted_timestamp

                    if stage_date and prod_date:
                        break

                tg.create_task(self._update_block(orgrepo, block_id, stage_date, prod_date))

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
