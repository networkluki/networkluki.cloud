#!/usr/bin/env python3
"""Build the static site into the public directory."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
PUBLIC = ROOT / "public"


def copy_text_file(source: Path, destination: Path) -> None:
    """Copy a UTF-8 text file, creating the destination directory if needed."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    copy_text_file(SRC / "index.template.html", PUBLIC / "index.html")

    cname = ROOT / "CNAME"
    if cname.exists():
        copy_text_file(cname, PUBLIC / "CNAME")


if __name__ == "__main__":
    main()
