#!/usr/bin/env python3
"""
Create Jekyll articles for paintings extracted from HTML file.
Downloads images and creates markdown files.
"""
import re
import json
import urllib.request
import os
import html
from datetime import datetime, timedelta

def extract_paintings(html_file):
    """Extract painting information from HTML file using regex."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    paintings = []

    # Pattern to find h3 with title
    h3_pattern = r'<h3[^>]*><span[^>]*>(?:<a[^>]*>)?<strong>(?:<em>)?([^<]+?)(?:</em>)?(?:\s+by\s+([^<]+?))?</strong>(?:</a>)?</span></h3>'
    h3_matches = re.finditer(h3_pattern, content)

    for h3_match in h3_matches:
        title_text = h3_match.group(1).strip()
        artist_from_title = h3_match.group(2)

        # Try to extract artist if not captured
        if not artist_from_title and ' by ' in title_text:
            match = re.search(r'^(.+?)\s+by\s+(.+?)$', title_text)
            if match:
                artwork = match.group(1).strip()
                artist = match.group(2).strip()
            else:
                continue
        elif artist_from_title:
            artwork = title_text
            artist = artist_from_title.strip()
        else:
            # No "by" found, might be a sculpture or artwork without artist in title
            artwork = title_text
            artist = ""

        # Find image after this h3
        start_pos = h3_match.end()
        search_range = content[start_pos:start_pos+3000]

        img_pattern = r'data-src="([^"]+\.jpg[^"]*)"[^>]+alt="([^"]*)"'
        img_match = re.search(img_pattern, search_range)

        if img_match:
            img_url = img_match.group(1)
            alt_text = img_match.group(2)

            # Decode HTML entities
            artist_clean = html.unescape(artist) if artist else 'Unknown'
            artwork_clean = html.unescape(artwork)

            paintings.append({
                'title': artwork_clean + (f' by {artist_clean}' if artist_clean != 'Unknown' else ''),
                'artwork': artwork_clean,
                'artist': artist_clean,
                'image_url': img_url,
                'alt_text': html.unescape(alt_text)
            })

    return paintings


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = html.unescape(text.lower())
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def download_image(url, filepath):
    """Download image from URL to filepath."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


def create_markdown_article(painting, index, output_dir, assets_dir):
    """Create markdown article for a painting."""
    # Create filename
    date = datetime.now() - timedelta(days=len(paintings) - index)
    date_str = date.strftime('%Y-%m-%d')
    slug = slugify(f"{painting['artist']}-{painting['artwork']}")
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(output_dir, filename)

    # Download image
    image_filename = f"{slug}.jpg"
    image_path = os.path.join(assets_dir, image_filename)
    image_url_local = f"/assets/obrazy/{image_filename}"

    if not os.path.exists(image_path):
        print(f"Downloading image for {painting['artwork']}...")
        download_image(painting['image_url'], image_path)

    # Estimate year (this would need manual correction or AI)
    year = "neznámo"

    # Create markdown content
    content = f"""---
layout: post
title: "{painting['artist']} - {painting['artwork']}"
date: {date_str}
order:
namalovano: {year}
autor: {painting['artist']}
obraz: {painting['artwork']}
styl:
urlobrazu: {image_url_local}
---


{painting['artist']} je {painting['artwork']}.

## 🖼️ Kde dílo vidět


## {painting['artist']}
- 🗓️ **Narozen/a:**
- 🏫
- 🎭
- 👥

![{painting['artwork']}]({image_url_local})

## 🎨 O obraze {painting['artwork']}

-
-
-

## Pár detailů k obrazu

- 🖋️ **Styl:**
- 🪞 **Perspektiva:**
- 🎭 **Inspirace:**
- 🌃 **Nálada:**
- ✨

## Historický kontext

## Srovnání s dalšími umělci

"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created {filename}")
    return filepath


if __name__ == '__main__':
    # Configuration
    html_file = '/Users/imac/Github/zastupitelstvo/obrazy.html'
    output_dir = '/Users/imac/Github/zastupitelstvo/_obrazy'
    assets_dir = '/Users/imac/Github/zastupitelstvo/assets/obrazy'

    # Create directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)

    # Extract paintings
    paintings = extract_paintings(html_file)
    print(f"Found {len(paintings)} paintings")

    # Create articles for each painting
    for idx, painting in enumerate(paintings):
        create_markdown_article(painting, idx, output_dir, assets_dir)

    print(f"\nDone! Created {len(paintings)} articles in {output_dir}")
