#!/usr/bin/env python3
"""Create a Claude-compatible ZIP; only the public skill directory is included."""
from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
folder = root / "aveva-system-platform"
if not (folder / "SKILL.md").is_file():
    raise SystemExit("SKILL.md missing; validate repository before packaging")
out_dir = root / "dist"
out_dir.mkdir(exist_ok=True)
zip_path = out_dir / "aveva-system-platform.zip"
with ZipFile(zip_path, "w", ZIP_DEFLATED) as archive:
    for path in sorted(folder.rglob("*")):
        if path.is_file() and not path.is_symlink() and "__pycache__" not in path.parts:
            archive.write(path, path.relative_to(root).as_posix())
print(f"Created {zip_path}")
print("ZIP root: aveva-system-platform/SKILL.md")
