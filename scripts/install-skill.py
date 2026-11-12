#!/usr/bin/env python3
"""Install a public AVEVA skill into Codex, Claude Code or GitHub Copilot.

No networking, no privileged writes and no overwriting existing installs.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description="Install AVEVA System Platform Agent Skill")
parser.add_argument("--agent", choices=("codex", "claude", "copilot"), required=True)
parser.add_argument("--scope", choices=("user", "project"), default="user")
parser.add_argument("--project-dir", type=Path, default=Path.cwd(),
                    help="Target workspace root for --scope project")
args = parser.parse_args()

repo = Path(__file__).resolve().parents[1]
src = repo / "aveva-system-platform"
if not (src / "SKILL.md").is_file():
    raise SystemExit(f"Missing skill source: {src}")
relative = {
    "codex": { "project": ".agents/skills", "user": ".agents/skills" },
    "claude": { "project": ".claude/skills", "user": ".claude/skills" },
    "copilot": { "project": ".github/skills", "user": ".copilot/skills" },
}
root = Path.home() if args.scope == "user" else args.project_dir.expanduser().resolve()
if args.scope == "project" and not root.is_dir():
    raise SystemExit(f"Target project directory not found: {root}")

dest = root / relative[args.agent][args.scope] / src.name
if dest.exists():
    raise SystemExit(f"Already installed at {dest}. Back up/remove it manually before reinstalling.")
dest.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(src, dest)
print(f"Installed to: {dest}")
print("Open a new agent session and ask to use the 'aveva-system-platform' skill.")
