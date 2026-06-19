#!/usr/bin/env python3
"""Tiny static site generator for the public directory."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
PUBLIC = ROOT / "public"

SITE = {
    "title": "Network Luki Cloud",
}


def render_template(source: Path, context: dict[str, str]) -> str:
    """Render a tiny HTML template with escaped {placeholders}."""
    template = source.read_text(encoding="utf-8")
    safe_context = {key: escape(value, quote=True) for key, value in context.items()}

    try:
        return template.format_map(safe_context)
    except KeyError as error:
        missing_key = error.args[0]
        raise SystemExit(
            f"Missing template value '{missing_key}' while rendering {source}"
        ) from error


def write_text_file(destination: Path, content: str) -> None:
    """Write a UTF-8 text file, creating the destination directory if needed."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def copy_text_file(source: Path, destination: Path) -> None:
    """Copy a UTF-8 text file, creating the destination directory if needed."""
    write_text_file(destination, source.read_text(encoding="utf-8"))


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    index_html = render_template(SRC / "index.template.html", SITE)
    write_text_file(PUBLIC / "index.html", index_html)

    cname = ROOT / "CNAME"
    if cname.exists():
        copy_text_file(cname, PUBLIC / "CNAME")


if __name__ == "__main__":
    main()
