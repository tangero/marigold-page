#!/usr/bin/env python3
"""
Optimize and download tech news images locally.

Downloads images from tech news articles and stores them in:
/assets/tech-news/YYYY/MM/slug.jpg (or .webp)

Converts images to WebP format for better compression.
Resizes large images to max 1200px width.
Updates article front matter with local image path.
"""

import os
import sys
import re
import glob
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import requests
import logging

try:
    from PIL import Image
    from io import BytesIO
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
TECH_NEWS_DIR = Path("_tech_news")
ASSETS_BASE_DIR = Path("assets/tech-news")
MAX_IMAGE_WIDTH = 1200
MIN_IMAGE_SIZE = 10000  # 10KB minimum
TIMEOUT = 10  # seconds
JPEG_QUALITY = 85
WEBP_QUALITY = 85


def create_asset_path(article_date: str, slug: str) -> tuple:
    """
    Create asset path from article date.

    Example: "2025-10-15-my-article.md" -> "assets/tech-news/2025/10/"
    Returns: (directory_path, filename_base)
    """
    try:
        match = re.match(r'(\d{4})-(\d{2})-\d{2}', article_date)
        if not match:
            logger.warning(f"Invalid date format in {article_date}")
            return None, None

        year, month = match.groups()
        asset_dir = ASSETS_BASE_DIR / year / month
        return asset_dir, slug
    except Exception as e:
        logger.error(f"Error parsing date from {article_date}: {e}")
        return None, None


def download_image(url: str) -> bytes:
    """Download image from URL with error handling."""
    try:
        logger.info(f"Downloading image from: {url}")
        response = requests.get(
            url,
            timeout=TIMEOUT,
            headers={
                'User-Agent': 'Mozilla/5.0 (compatible; ImageDownloader/1.0)'
            },
            verify=True
        )
        response.raise_for_status()

        # Check if content is actually an image
        if not response.headers.get('content-type', '').startswith('image/'):
            logger.warning(f"Content-Type is not image: {response.headers.get('content-type')}")
            return None

        # Check minimum size
        if len(response.content) < MIN_IMAGE_SIZE:
            logger.warning(f"Image too small ({len(response.content)} bytes)")
            return None

        return response.content
    except requests.Timeout:
        logger.error(f"Timeout downloading image: {url}")
        return None
    except requests.RequestException as e:
        logger.error(f"Error downloading image: {e}")
        return None


def optimize_image(image_data: bytes) -> tuple:
    """
    Optimize image and return JPG and WebP versions.

    Returns: (jpg_bytes, webp_bytes) or (None, None) on error
    """
    try:
        # Open image
        img = Image.open(BytesIO(image_data))

        # Convert RGBA to RGB if necessary (for JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background

        # Resize if needed
        if img.width > MAX_IMAGE_WIDTH:
            ratio = MAX_IMAGE_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_IMAGE_WIDTH, new_height), Image.Resampling.LANCZOS)
            logger.info(f"Resized image to {img.width}x{img.height}")

        # Save as JPEG
        jpg_buffer = BytesIO()
        img.save(jpg_buffer, format='JPEG', quality=JPEG_QUALITY, optimize=True)
        jpg_bytes = jpg_buffer.getvalue()

        # Save as WebP
        webp_buffer = BytesIO()
        img.save(webp_buffer, format='WEBP', quality=WEBP_QUALITY)
        webp_bytes = webp_buffer.getvalue()

        logger.info(f"Optimized: JPEG {len(jpg_bytes)/1024:.1f}KB, WebP {len(webp_bytes)/1024:.1f}KB")
        return jpg_bytes, webp_bytes

    except Exception as e:
        logger.error(f"Error optimizing image: {e}")
        return None, None


def extract_slug_from_filename(filename: str) -> str:
    """Extract slug from filename (remove date prefix)."""
    # Format: YYYY-MM-DD-slug.md -> slug
    match = re.match(r'\d{4}-\d{2}-\d{2}-(.+)\.md$', filename)
    if match:
        return match.group(1)
    return filename.replace('.md', '')


def parse_front_matter(content: str) -> tuple:
    """Parse YAML front matter and body."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content


def update_front_matter(front_matter: str, local_image_path: str, backup_url: str) -> str:
    """
    Update front matter with image paths.

    Replaces:
    - urlToImage: with local path
    - Adds: urlToImageBackup: for fallback
    """
    # Remove old urlToImage if exists
    front_matter = re.sub(r'urlToImage:.*\n', '', front_matter)

    # Add new image paths (at the end, before final newline)
    lines = front_matter.rstrip().split('\n')
    lines.append(f'urlToImage: "{local_image_path}"')
    lines.append(f'urlToImageBackup: "{backup_url}"')

    return '\n'.join(lines) + '\n'


def process_article(article_path: Path) -> bool:
    """
    Process single article: download and optimize image if needed.
    """
    try:
        logger.info(f"Processing: {article_path.name}")

        # Read article
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse front matter
        front_matter, body = parse_front_matter(content)
        if not front_matter:
            logger.warning(f"No front matter found in {article_path.name}")
            return False

        # Extract current image URL
        url_match = re.search(r'urlToImage:\s*"?([^"\n]+)"?', front_matter)
        if not url_match:
            logger.info(f"No urlToImage found in {article_path.name}")
            return False

        image_url = url_match.group(1).strip()
        backup_url = image_url  # Save original as backup

        # Check if already has local path
        if image_url.startswith('/assets/tech-news/'):
            logger.info(f"Already has local image: {image_url}")
            return True

        # Create asset directory
        slug = extract_slug_from_filename(article_path.name)
        asset_dir, _ = create_asset_path(article_path.name, slug)

        if not asset_dir:
            logger.error(f"Could not create asset path for {article_path.name}")
            return False

        asset_dir.mkdir(parents=True, exist_ok=True)

        # Download image
        image_data = download_image(image_url)
        if not image_data:
            logger.warning(f"Failed to download image for {article_path.name}")
            return False

        # Optimize image
        jpg_bytes, webp_bytes = optimize_image(image_data)
        if not jpg_bytes:
            logger.error(f"Failed to optimize image for {article_path.name}")
            return False

        # Save images
        jpg_path = asset_dir / f"{slug}.jpg"
        webp_path = asset_dir / f"{slug}.webp"

        with open(jpg_path, 'wb') as f:
            f.write(jpg_bytes)
        logger.info(f"Saved: {jpg_path}")

        with open(webp_path, 'wb') as f:
            f.write(webp_bytes)
        logger.info(f"Saved: {webp_path}")

        # Update front matter with local path
        # Use JPG as primary (better browser support)
        local_image_path = f"/assets/tech-news/{asset_dir.name.split('/')[-2]}/{asset_dir.name.split('/')[-1]}/{slug}.jpg"
        front_matter = update_front_matter(front_matter, local_image_path, backup_url)

        # Write back to file
        new_content = f"---\n{front_matter}---\n{body}"
        with open(article_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        logger.info(f"Updated front matter for {article_path.name}")
        return True

    except Exception as e:
        logger.error(f"Error processing {article_path.name}: {e}")
        return False


def main():
    """Main function."""
    logger.info("Starting tech news image optimization")

    # Find all tech news articles
    article_files = sorted(TECH_NEWS_DIR.glob("*.md"), reverse=True)
    logger.info(f"Found {len(article_files)} articles")

    if not article_files:
        logger.warning("No articles found in _tech_news/")
        return 0

    success_count = 0
    fail_count = 0

    # Process articles (limit to recent ones to avoid too many downloads)
    for i, article_path in enumerate(article_files[:50]):  # Process last 50 articles
        if process_article(article_path):
            success_count += 1
        else:
            fail_count += 1

    logger.info(f"Completed: {success_count} success, {fail_count} failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
