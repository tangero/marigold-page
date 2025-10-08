#!/usr/bin/env python3
"""
Extract paintings from HTML file and prepare data for Jekyll articles.
"""
import re
import json
from html.parser import HTMLParser

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

        # Skip if it doesn't contain "by" and artist_from_title is None
        # Check in full match if "by" exists
        full_match_text = h3_match.group(0)

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

            paintings.append({
                'title': title_text + (f' by {artist}' if artist and artist not in title_text else ''),
                'artwork': artwork,
                'artist': artist if artist else 'Unknown',
                'image_url': img_url,
                'alt_text': alt_text
            })

    return paintings

if __name__ == '__main__':
    paintings = extract_paintings('/Users/imac/Github/zastupitelstvo/obrazy.html')

    print(f"Found {len(paintings)} paintings:")
    print(json.dumps(paintings, indent=2, ensure_ascii=False))
