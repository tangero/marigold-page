#!/usr/bin/env python3
"""
Sanitize filenames to contain only URL-safe characters.
Remove accents and special characters from filenames.
"""
import os
import re
import unicodedata
from pathlib import Path


def remove_accents(text):
    """Remove accents from unicode string."""
    # Normalize unicode characters
    nfd = unicodedata.normalize('NFD', text)
    # Filter out combining characters (accents)
    return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')


def sanitize_filename(filename):
    """Convert filename to URL-safe format."""
    # Get the base name without extension
    name, ext = os.path.splitext(filename)

    # Remove accents
    name = remove_accents(name)

    # Convert to lowercase
    name = name.lower()

    # Replace spaces and special characters with hyphens
    name = re.sub(r'[^a-z0-9-]', '-', name)

    # Remove multiple consecutive hyphens
    name = re.sub(r'-+', '-', name)

    # Remove leading/trailing hyphens
    name = name.strip('-')

    return name + ext


def update_frontmatter_url(content, old_filename, new_filename):
    """Update urlobrazu in frontmatter if it references the old filename."""
    # Extract the image filename from the old path
    old_image_name = os.path.splitext(old_filename)[0] + '.jpg'
    new_image_name = os.path.splitext(new_filename)[0] + '.jpg'

    # Replace in urlobrazu field
    content = re.sub(
        r'urlobrazu:\s*["\']?/assets/obrazy/' + re.escape(old_image_name) + r'["\']?',
        f'urlobrazu: /assets/obrazy/{new_image_name}',
        content
    )

    return content


def fix_image_urls_in_articles(directory):
    """Fix image URLs in all markdown files to match sanitized filenames."""
    files = list(Path(directory).glob('*.md'))
    fixed_count = 0

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Find all image URLs in the content
        # Pattern: /assets/obrazy/filename.jpg
        def sanitize_url_match(match):
            full_url = match.group(0)
            path_part = match.group(1)
            # Sanitize just the filename part
            parts = path_part.split('/')
            filename = parts[-1]
            sanitized = sanitize_filename(filename)
            parts[-1] = sanitized
            new_path = '/'.join(parts)
            return f'"/assets/obrazy/{sanitized}"'

        # Replace URLs with accents
        content = re.sub(
            r'["\']?/assets/obrazy/([^"\']+\.(jpg|jpeg|png))["\']?',
            lambda m: f'"/assets/obrazy/{sanitize_filename(m.group(1))}"',
            content
        )

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ✅ Fixed URLs in {filepath.name}")
            fixed_count += 1

    return fixed_count


def sanitize_directory(directory, dry_run=False):
    """Sanitize all markdown filenames in directory."""
    files = list(Path(directory).glob('*.md'))

    renamed_count = 0
    skipped_count = 0

    for filepath in files:
        old_filename = filepath.name
        new_filename = sanitize_filename(old_filename)

        if old_filename == new_filename:
            skipped_count += 1
            continue

        new_filepath = filepath.parent / new_filename

        print(f"📝 Renaming:")
        print(f"   Old: {old_filename}")
        print(f"   New: {new_filename}")

        if not dry_run:
            # Update content to fix image URLs
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            content = update_frontmatter_url(content, old_filename, new_filename)

            # Write to new file
            with open(new_filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            # Remove old file
            filepath.unlink()

            print(f"   ✅ Renamed successfully\n")
            renamed_count += 1
        else:
            print(f"   [DRY RUN - would rename]\n")
            renamed_count += 1

    return renamed_count, skipped_count


def sanitize_images_directory(directory, dry_run=False):
    """Sanitize all image filenames in directory."""
    files = list(Path(directory).glob('*.jpg')) + list(Path(directory).glob('*.jpeg')) + list(Path(directory).glob('*.png'))

    renamed_count = 0
    skipped_count = 0

    for filepath in files:
        old_filename = filepath.name
        new_filename = sanitize_filename(old_filename)

        if old_filename == new_filename:
            skipped_count += 1
            continue

        new_filepath = filepath.parent / new_filename

        print(f"🖼️  Renaming image:")
        print(f"   Old: {old_filename}")
        print(f"   New: {new_filename}")

        if not dry_run:
            filepath.rename(new_filepath)
            print(f"   ✅ Renamed successfully\n")
            renamed_count += 1
        else:
            print(f"   [DRY RUN - would rename]\n")
            renamed_count += 1

    return renamed_count, skipped_count


if __name__ == '__main__':
    obrazy_dir = '/Users/imac/Github/zastupitelstvo/_obrazy'
    assets_dir = '/Users/imac/Github/zastupitelstvo/assets/obrazy'

    print("="*60)
    print("SANITIZING FILENAMES - REMOVING ACCENTS AND SPECIAL CHARS")
    print("="*60)
    print()

    # First, do a dry run to show what will be changed
    print("🔍 DRY RUN - Checking what needs to be sanitized...\n")

    print("📁 Checking markdown files in _obrazy/...")
    md_renamed, md_skipped = sanitize_directory(obrazy_dir, dry_run=True)

    print("\n📁 Checking image files in assets/obrazy/...")
    img_renamed, img_skipped = sanitize_images_directory(assets_dir, dry_run=True)

    print("\n" + "="*60)
    print(f"DRY RUN SUMMARY:")
    print(f"  Markdown files to rename: {md_renamed}")
    print(f"  Markdown files OK: {md_skipped}")
    print(f"  Image files to rename: {img_renamed}")
    print(f"  Image files OK: {img_skipped}")
    print("="*60)

    if md_renamed > 0 or img_renamed > 0:
        print("\n⚠️  Files with accents/special characters found!")
        print("\n🔧 Proceeding with automatic renaming...")

        print("\n" + "="*60)
        print("PROCEEDING WITH ACTUAL RENAMING...")
        print("="*60 + "\n")

        print("📁 Sanitizing markdown files...")
        md_renamed, md_skipped = sanitize_directory(obrazy_dir, dry_run=False)

        print("\n📁 Sanitizing image files...")
        img_renamed, img_skipped = sanitize_images_directory(assets_dir, dry_run=False)

        print("\n📁 Fixing image URLs in articles...")
        url_fixed = fix_image_urls_in_articles(obrazy_dir)

        print("\n" + "="*60)
        print(f"✅ COMPLETED!")
        print(f"  Markdown files renamed: {md_renamed}")
        print(f"  Image files renamed: {img_renamed}")
        print(f"  URLs fixed in articles: {url_fixed}")
        print("="*60)
    else:
        print("\n✅ All filenames are already sanitized!")
