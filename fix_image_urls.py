#!/usr/bin/env python3
"""
Fix image URLs in markdown files to remove accents.
"""
import os
import re
import unicodedata
from pathlib import Path


def remove_accents(text):
    """Remove accents from unicode string."""
    nfd = unicodedata.normalize('NFD', text)
    return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')


def sanitize_filename(filename):
    """Convert filename to URL-safe format."""
    name, ext = os.path.splitext(filename)
    name = remove_accents(name)
    name = name.lower()
    name = re.sub(r'[^a-z0-9-]', '-', name)
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')
    return name + ext


def fix_image_urls_in_articles(directory):
    """Fix image URLs in all markdown files."""
    files = list(Path(directory).glob('*.md'))
    fixed_count = 0

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace URLs with accents in urlobrazu field
        content = re.sub(
            r'(urlobrazu:\s*["\']?)/assets/obrazy/([^"\'>\n]+\.(jpg|jpeg|png))(["\']?)',
            lambda m: f'{m.group(1)}/assets/obrazy/{sanitize_filename(m.group(2))}{m.group(4)}',
            content
        )

        # Replace URLs in markdown image tags
        content = re.sub(
            r'!\[([^\]]*)\]\((/assets/obrazy/[^)]+\.(jpg|jpeg|png))\)',
            lambda m: f'![{m.group(1)}](/assets/obrazy/{sanitize_filename(os.path.basename(m.group(2)))})',
            content
        )

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed URLs in {filepath.name}")
            fixed_count += 1

    return fixed_count


if __name__ == '__main__':
    directory = '/Users/imac/Github/zastupitelstvo/_obrazy'

    print("="*60)
    print("FIXING IMAGE URLs IN MARKDOWN FILES")
    print("="*60)
    print()

    fixed_count = fix_image_urls_in_articles(directory)

    print()
    print("="*60)
    print(f"✅ Done! Fixed URLs in {fixed_count} files")
    print("="*60)
