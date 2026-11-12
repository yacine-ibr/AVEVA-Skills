#!/usr/bin/env python3
"""Validate structure and relative links for the public AVEVA Agent Skill."""
from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "aveva-system-platform"
MAIN = SKILL / "SKILL.md"
REQUIRED = [
    MAIN,
    SKILL / "references" / "official-sources.md",
    SKILL / "references" / "review-checklist.md",
    SKILL / "examples" / "README.md",
    SKILL / "examples" / "motor-start-stop.qsnet",
    SKILL / "examples" / "alarm-evaluation.qsnet",
    SKILL / "examples" / "state-derivation.qsnet",
]
errors = []
for file in REQUIRED:
    if not file.is_file():
        errors.append(f"Missing: {file.relative_to(ROOT)}")

if MAIN.is_file():
    text = MAIN.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        errors.append("SKILL.md must start with YAML frontmatter delimited by ---")
    else:
        fields = {}
        for line in parts[1].splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip().strip('"').strip("'")
        if fields.get("name") != "aveva-system-platform":
            errors.append("frontmatter name must equal avea-system-platform skill directory")
        if not fields.get("description"):
            errors.append("frontmatter description is required")
        if len(fields.get("description", "")) > 200:
            errors.append("frontmatter description is over 200 characters")
    links = re.findall(r"\]\(([^)]+)\)", text)
    for href in links:
        if href.startswith(("https://", "http://", "#", "mailto:")):
            continue
        target = (SKILL / href.split("#", 1)[0]).resolve()
        if not target.is_file() or not target.is_relative_to(SKILL.resolve()):
            errors.append(f"Missing or unsafe relative link in SKILL.md: {href}")

if errors:
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)
print("OK: skill frontmatter, required files and relative links")
