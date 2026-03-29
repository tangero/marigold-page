#!/usr/bin/env python3
"""
Hugo front matter migration script for Marigold.cz Jekyll-to-Hugo migration.

Processes all markdown files in a given directory:
- Removes Jekyll-specific keys (layout, ID, oldlink, post_date, post_excerpt)
- Extracts slug from filename and adds to front matter if missing
- Preserves all other front matter and content exactly as-is

Uses only Python stdlib (no external dependencies).

Usage:
    python3 scripts/hugo_migrate_frontmatter.py content/posts
    python3 scripts/hugo_migrate_frontmatter.py content/en/posts
"""

import sys
import re
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

# Keys to remove from front matter (Jekyll-specific)
JEKYLL_KEYS_TO_REMOVE = {"layout", "ID", "oldlink", "post_date", "post_excerpt"}

# Pattern: YYYY-MM-DD-slug-here.md -> slug-here
FILENAME_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)\.md$")


def extract_slug_from_filename(filename: str) -> str | None:
    """Extract slug from Jekyll-style filename YYYY-MM-DD-slug.md."""
    match = FILENAME_DATE_PATTERN.match(filename)
    if match:
        return match.group(1)
    return None


def split_front_matter(content: str) -> tuple[str | None, str, str]:
    """
    Split markdown content into:
    - The raw YAML front matter string (between the --- delimiters)
    - The body after front matter
    - The original front matter block for fallback

    Returns (yaml_str, body, original_block) or (None, full_content, '') if no FM.
    """
    if not content.startswith("---"):
        return None, content, ""

    rest = content[3:]
    # Match closing --- on its own line (with possible trailing spaces)
    end_match = re.search(r"\n---[ \t]*\n", rest)
    if end_match:
        yaml_str = rest[: end_match.start()]
        body = rest[end_match.end():]
        original_block = "---" + rest[: end_match.end() + 3]
        return yaml_str, body, original_block

    # Try closing --- at end of file
    end_match = re.search(r"\n---[ \t]*$", rest)
    if end_match:
        yaml_str = rest[: end_match.start()]
        body = rest[end_match.end():]
        original_block = "---" + rest[: end_match.end()]
        return yaml_str, body, original_block

    return None, content, ""


def remove_key_from_yaml_text(yaml_text: str, key: str) -> str:
    """
    Remove a top-level YAML key and its value from raw YAML text.

    Handles:
    - Simple scalar values: key: value
    - Quoted values: key: "value with spaces"
    - Block scalars / multi-line (indented continuation lines)
    - List values starting with -

    Strategy: find the line starting with 'key:' and remove it plus any
    continuation lines (indented or starting with -)
    """
    lines = yaml_text.split("\n")
    result = []
    skip_until_next_key = False

    for line in lines:
        if skip_until_next_key:
            # Continuation: indented line or list item means it belongs to prev key
            if line and (line[0] == " " or line[0] == "\t" or line.startswith("-")):
                continue  # skip continuation
            else:
                skip_until_next_key = False

        # Check if this line is the key we want to remove
        # Match: optional spaces at start (but top-level key has no indent),
        # then key:, then either space/newline or end
        key_pattern = re.compile(r"^" + re.escape(key) + r"\s*:")
        if key_pattern.match(line.lstrip()) and not line.startswith(" ") and not line.startswith("\t"):
            # This is a top-level key to remove
            skip_until_next_key = True
            continue

        result.append(line)

    return "\n".join(result)


def has_key_in_yaml_text(yaml_text: str, key: str) -> bool:
    """Check if a top-level YAML key exists in raw YAML text."""
    pattern = re.compile(r"^" + re.escape(key) + r"\s*:", re.MULTILINE)
    return bool(pattern.search(yaml_text))


def add_slug_to_yaml_text(yaml_text: str, slug: str) -> str:
    """Add slug key at the beginning of YAML text."""
    # Escape single quotes in slug
    slug_escaped = slug.replace("'", "''")
    slug_line = f"slug: '{slug_escaped}'\n"
    return slug_line + yaml_text


def process_file(file_path: Path) -> bool:
    """
    Process a single markdown file: update front matter for Hugo compatibility.

    Returns True on success, False on skip/error.
    """
    filename = file_path.name
    slug_from_filename = extract_slug_from_filename(filename)

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.warning(f"Cannot read {file_path}: {e}")
        return False

    yaml_str, body, _ = split_front_matter(content)

    if yaml_str is None:
        # No front matter - skip silently
        return True

    modified_yaml = yaml_str

    # Remove Jekyll-specific keys
    for key in JEKYLL_KEYS_TO_REMOVE:
        if has_key_in_yaml_text(modified_yaml, key):
            modified_yaml = remove_key_from_yaml_text(modified_yaml, key)

    # Add slug if not already present
    if slug_from_filename and not has_key_in_yaml_text(modified_yaml, "slug"):
        modified_yaml = add_slug_to_yaml_text(modified_yaml, slug_from_filename)

    # Ensure YAML ends with a newline before closing ---
    if not modified_yaml.endswith("\n"):
        modified_yaml += "\n"

    new_content = f"---\n{modified_yaml}---\n{body}"

    try:
        file_path.write_text(new_content, encoding="utf-8")
    except Exception as e:
        logger.error(f"Cannot write {file_path}: {e}")
        return False

    return True


def process_directory(directory: Path) -> None:
    """Process all .md files in a directory recursively."""
    md_files = list(directory.rglob("*.md"))

    if not md_files:
        logger.warning(f"No .md files found in {directory}")
        return

    logger.info(f"Processing {len(md_files)} markdown files in {directory}")

    processed = 0
    skipped = 0
    errors = 0

    for file_path in md_files:
        # Skip _index.md files (Hugo section files, not posts)
        if file_path.name == "_index.md":
            skipped += 1
            continue

        success = process_file(file_path)
        if success:
            processed += 1
        else:
            errors += 1

    logger.info(
        f"Done: {processed} processed, {skipped} skipped, {errors} errors"
    )


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>", file=sys.stderr)
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        logger.error(f"Directory does not exist: {directory}")
        sys.exit(1)

    if not directory.is_dir():
        logger.error(f"Not a directory: {directory}")
        sys.exit(1)

    process_directory(directory)


if __name__ == "__main__":
    main()
