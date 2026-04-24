#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
REPOS = [
    {"repo": "appointment", "product": "Thunderbird Appointment"},
    {"repo": "mailstrom", "product": "Thunderbird Pro's mail server deployment"},
    {"repo": "services-ui", "product": "Services UI"},
    {"repo": "tbpro-add-on", "product": "Thunderbird Send and Pro Add-on"},
    {"repo": "thunderbird-accounts", "product": "Thunderbird Accounts"},
    {"repo": "pro", "product": "Thunderbird Pro"},
]

SOURCE_OWNER = "thunderbird"
FORK_OWNER = "kewisch"
FORK_REMOTE = "pkewisch"
BRANCH_NAME = "templates"
BASE_BRANCH = "main"
COMMIT_MESSAGE_TEMPLATE = "Update GitHub templates for $repo"
PR_TITLE_TEMPLATE = "Update GitHub templates"
PR_BODY = "Auto-generated PR for updating repository metadata to the latest templates from thunderbird/notion-scripts."


def run(
    args: list[str],
    *,
    cwd: Path | None = None,
    capture_output: bool = False,
    check: bool = True,
) -> str:
    """Run a subprocess command and optionally return captured stdout."""
    proc = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        check=check,
        text=True,
        capture_output=capture_output,
    )
    return proc.stdout if capture_output else ""


def try_run(args: list[str], *, cwd: Path | None = None) -> bool:
    """Run a command and return whether it succeeded."""
    try:
        run(args, cwd=cwd)
    except subprocess.CalledProcessError:
        return False
    return True


def is_repo_dirty(repo_dir: Path) -> bool:
    """Return whether a git repository has tracked or untracked changes."""
    status = run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True)
    return bool(status.strip())


def reset_templates_branch_to_origin_main(repo_dir: Path, *, clean_untracked: bool) -> None:
    """Move to templates branch and reset it to origin/main."""
    run(["git", "fetch", "origin"], cwd=repo_dir)
    run(["git", "checkout", "-B", BRANCH_NAME], cwd=repo_dir)
    run(["git", "reset", "--hard", f"origin/{BASE_BRANCH}"], cwd=repo_dir)
    if clean_untracked:
        run(["git", "clean", "-fd"], cwd=repo_dir)


def ensure_remote(repo_dir: Path, remote: str, url: str) -> None:
    """Ensure a git remote exists and points to the expected URL."""
    remotes = run(["git", "remote"], cwd=repo_dir, capture_output=True).split()
    if remote in remotes:
        run(["git", "remote", "set-url", remote, url], cwd=repo_dir)
    else:
        run(["git", "remote", "add", remote, url], cwd=repo_dir)


def branch_matches_head(repo_dir: Path, remote: str, branch: str) -> bool:
    """Return whether remote/branch points to the same commit as local HEAD."""
    run(
        ["git", "fetch", remote, f"+refs/heads/{branch}:refs/remotes/{remote}/{branch}"],
        cwd=repo_dir,
        check=False,
    )
    local_head = run(["git", "rev-parse", "HEAD"], cwd=repo_dir, capture_output=True).strip()
    try:
        remote_head = run(["git", "rev-parse", f"{remote}/{branch}"], cwd=repo_dir, capture_output=True).strip()
    except subprocess.CalledProcessError:
        return False
    return local_head == remote_head


def staged_matches_remote_branch(repo_dir: Path, remote: str, branch: str) -> bool:
    """Return whether staged local changes match the remote branch exactly."""
    fetch = subprocess.run(
        ["git", "fetch", remote, f"+refs/heads/{branch}:refs/remotes/{remote}/{branch}"],
        cwd=str(repo_dir),
        check=False,
        text=True,
        capture_output=True,
    )
    if fetch.returncode != 0:
        return False

    proc = subprocess.run(
        ["git", "diff", "--cached", "--quiet", f"{remote}/{branch}", "--"],
        cwd=str(repo_dir),
        check=False,
        text=True,
        capture_output=True,
    )
    return proc.returncode == 0


def expand_template(template: str, repo: str) -> str:
    """Expand $repo placeholders in configured message templates."""
    return template.replace("$repo", repo)


def confirm_changes(repo: str) -> bool:
    """Ask for per-repo confirmation before commit/push workflow continues."""
    while True:
        answer = input(f"Apply and publish these changes for {repo}? [y/N]: ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"", "n", "no"}:
            return False
        print("Please answer y or n (or Ctrl+C to abort).")


def build_template_context(repo_config: dict[str, object]) -> dict[str, object]:
    """Build Jinja2 context from a repo configuration dictionary."""
    context = dict(repo_config)
    repo = context.get("repo")
    if not isinstance(repo, str) or not repo:
        raise ValueError("Each REPOS entry must include non-empty string key 'repo'.")
    return context


def rendered_output_path(relative_path: Path) -> Path:
    """Map a template source path to output path by stripping a .j2 suffix."""
    if relative_path.suffix == ".j2":
        return relative_path.with_suffix("")
    return relative_path


def sync_templates(templates_src: Path, repo_dir: Path, context: dict[str, object]) -> None:
    """Copy static files and render .j2 templates into the destination repo."""
    env = Environment(
        loader=FileSystemLoader(str(templates_src)),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        variable_start_string="[[",
        variable_end_string="]]",
        block_start_string="[%",
        block_end_string="%]",
        comment_start_string="[#",
        comment_end_string="#]",
    )

    for src in sorted(templates_src.rglob("*")):
        if src.is_dir():
            continue

        relative_path = src.relative_to(templates_src)
        destination = repo_dir / rendered_output_path(relative_path)
        destination.parent.mkdir(parents=True, exist_ok=True)

        if src.suffix == ".j2":
            try:
                template = env.get_template(relative_path.as_posix())
                rendered = template.render(**context)
            except Exception as exc:
                line_number = getattr(exc, "lineno", None)
                if line_number is None:
                    for frame in traceback.extract_tb(exc.__traceback__):
                        if frame.filename == "<template>":
                            line_number = frame.lineno
                            break

                if line_number is not None:
                    raise RuntimeError(
                        f"Failed rendering template {relative_path.as_posix()}:{line_number}: {exc}"
                    ) from exc
                raise RuntimeError(f"Failed rendering template {relative_path.as_posix()}: {exc}") from exc
            if not rendered.strip():
                continue
            destination.write_text(rendered, encoding="utf-8")
        else:
            shutil.copy2(src, destination)


def main() -> int:
    """Execute repository template propagation and optional PR creation flow."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Commit locally but skip push and PR creation.")
    parser.add_argument("--no-pr", action="store_true", help="Update and push branch, but skip PR creation.")
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="If a repo is dirty, discard local changes and continue.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    templates_src = script_dir / "src"
    repos_dir = script_dir / "repos"

    if not templates_src.is_dir():
        print(f"Template source directory missing: {templates_src}", file=sys.stderr)
        return 1

    repos_dir.mkdir(parents=True, exist_ok=True)

    if shutil.which("git") is None:
        print("git is required but not installed.", file=sys.stderr)
        return 1
    if shutil.which("gh") is None:
        print("gh is required but not installed.", file=sys.stderr)
        return 1

    for repo_config in REPOS:
        try:
            context = build_template_context(repo_config)
        except ValueError as exc:
            print(f"Invalid repository config: {exc}", file=sys.stderr)
            return 1

        repo = context["repo"]
        if not isinstance(repo, str):
            print("Invalid repository config: key 'repo' must be a string.", file=sys.stderr)
            return 1

        print()
        print("================================================================")
        print(f"Repository: {repo}")
        print("================================================================")

        repo_dir = repos_dir / repo
        source_url = f"git@github.com:{SOURCE_OWNER}/{repo}.git"
        fork_url = f"git@github.com:{FORK_OWNER}/{repo}.git"
        if not (repo_dir / ".git").is_dir():
            print(f"Cloning {source_url} into {repo_dir}")
            run(["git", "clone", source_url, str(repo_dir)])

        ensure_remote(repo_dir, "origin", source_url)
        ensure_remote(repo_dir, FORK_REMOTE, fork_url)

        dirty = is_repo_dirty(repo_dir)
        if dirty and not args.force:
            print(
                f"Repository {repo} is dirty before applying templates. "
                "Run with -f/--force to discard local changes and continue.",
                file=sys.stderr,
            )
            return 1

        print(f"Preparing {repo_dir}: {BRANCH_NAME} -> origin/{BASE_BRANCH}")
        reset_templates_branch_to_origin_main(repo_dir, clean_untracked=args.force)

        try:
            sync_templates(templates_src, repo_dir, context)
        except Exception as exc:
            print(f"Template rendering failed for {repo}: {exc}", file=sys.stderr)
            return 1

        if not is_repo_dirty(repo_dir):
            if branch_matches_head(repo_dir, FORK_REMOTE, BRANCH_NAME):
                print(f"No updates needed for {repo}. {FORK_REMOTE}/{BRANCH_NAME} already matches local {BRANCH_NAME}.")
            else:
                print(
                    f"No updates needed for {repo}. "
                    f"{FORK_REMOTE}/{BRANCH_NAME} does not match local {BRANCH_NAME}, skipping push/PR."
                )
            continue

        run(["git", "add", "-A"], cwd=repo_dir)
        if staged_matches_remote_branch(repo_dir, FORK_REMOTE, BRANCH_NAME):
            print(f"No updates needed for {repo}. Template output already matches {FORK_REMOTE}/{BRANCH_NAME}.")
            run(["git", "reset", "--hard", f"{FORK_REMOTE}/{BRANCH_NAME}"], cwd=repo_dir)
            continue

        print(f"\nStaged diff for {repo}:")
        run(["git", "diff", "--cached"], cwd=repo_dir)

        if not confirm_changes(repo):
            print(f"Skipping {repo}.")
            continue

        commit_message = expand_template(COMMIT_MESSAGE_TEMPLATE, f"{SOURCE_OWNER}/{repo}")
        pr_title = expand_template(PR_TITLE_TEMPLATE, repo)

        run(["git", "commit", "-m", commit_message], cwd=repo_dir)

        if args.dry_run:
            print(f"Dry run for {repo}: committed locally on {BRANCH_NAME}, skipping push and PR creation.")
            continue

        run(["git", "push", "-u", FORK_REMOTE, BRANCH_NAME, "-f"], cwd=repo_dir)
        if args.no_pr:
            print(f"Updated {FORK_REMOTE}/{BRANCH_NAME} for {repo}; skipping PR creation (--no-pr).")
            continue

        run(
            [
                "gh",
                "-R",
                f"{SOURCE_OWNER}/{repo}",
                "pr",
                "create",
                "--base",
                BASE_BRANCH,
                "--head",
                f"{FORK_OWNER}:{BRANCH_NAME}",
                "--title",
                pr_title,
                "--body",
                PR_BODY,
            ],
            cwd=repo_dir,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
