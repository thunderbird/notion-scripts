# Template Propagation

This directory is a standalone `uv` project for propagating shared repository files from `templates/src/` into multiple GitHub repos.

It is heavily purpose-built, and should be replaced by a real tool that synchronizes files between repositories.

## What it does

- Clones or reuses repos under `templates/repos/`
- Renders `*.j2` files with Jinja and copies non-template files as-is
- Creates/updates a local `templates` branch from `origin/main`
- Stages, shows diff, asks for confirmation, commits, and pushes
- Optionally creates a PR

## Run

From this directory:

```bash
uv run propagate --dry-run
```

Or via wrapper:

```bash
./propagate.sh --dry-run
```

## Important flags

- `--dry-run`: commit locally, skip push and PR creation
- `--no-pr`: push branch updates, skip `gh pr create`
- `-f`, `--force`: if repo is dirty, discard local changes and continue

## Repo configuration

Edit `REPOS` in `propagate.py`. Each entry is a dict; the full dict is available to Jinja templates.

Example:

```python
{"repo": "appointment", "product": "Thunderbird Appointment"}
```

Template variables commonly used:

- `repo`
- `product`
- any additional keys from the repo dict

## Template rules

- Template files must end with `.j2`
- Rendered output drops the `.j2` suffix
- If rendered content is empty after `strip()`, the file is not written
- Missing variables fail fast (`StrictUndefined`)

Custom Jinja delimiters (to avoid conflict with GitHub `${{ ... }}`):

- variables: `[[ ... ]]`
- blocks: `[% ... %]`
- comments: `[# ... #]`
