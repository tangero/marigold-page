#!/usr/bin/env python3
"""
Automatické prolinkování klíčových pojmů v Markdown článcích.
Nahradí první výskyt každého klíčového slova či jeho variace odkazem dle nastavení v _data/pojmy.json.
"""
import os
import json
import re
from datetime import datetime
from pathlib import Path

# Optional cutoff_date for processing only newer posts
cutoff_str = os.getenv("CUTOFF_DATE")
cutoff_date = None
if cutoff_str:
    try:
        cutoff_date = datetime.strptime(cutoff_str, "%Y-%m-%d")
    except ValueError:
        print(f"Warning: ignored invalid CUTOFF_DATE: {cutoff_str}")

def get_post_date_from_filename(filename):
    match = re.match(r'^(\d{4}-\d{2}-\d{2})', filename)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        except ValueError:
            return None
    return None

markdown_link_pattern = re.compile(r'\[[^\]]+\]\([^\)]+\)')
html_link_pattern = re.compile(r'<a\b[^>]*>.*?</a>', flags=re.IGNORECASE|re.DOTALL)

def get_protected_spans(text: str):
    spans = []
    for m in markdown_link_pattern.finditer(text):
        spans.append(m.span())
    for m in html_link_pattern.finditer(text):
        spans.append(m.span())
    return spans

def load_keywords(data_file: str = '_data/pojmy.json'):
    data = json.loads(Path(data_file).read_text(encoding='utf-8'))
    entries = []
    for item in data.get('keywords', []):
        keyword = item.get('keyword')
        link = item.get('link')
        if not keyword or not link:
            continue
        entries.append((keyword, link))
        for var in item.get('variations', []):
            entries.append((var, link))
    return entries

def add_links(posts_dir: str = '_posts'):
    posts_path = Path(posts_dir)
    for file_path in posts_path.rglob('*.md'):
        if cutoff_date:
            date = get_post_date_from_filename(file_path.name)
            if not date or date <= cutoff_date:
                continue
        if 'en' in file_path.parts:
            continue
        text = file_path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if len(parts) < 3:
            continue
        front_matter, body = parts[1], parts[2]
        new_body = body
        for keyword, link in load_keywords():
            pattern = re.compile(rf"\b{re.escape(keyword)}\b")
            protected_spans = get_protected_spans(new_body)
            for match in pattern.finditer(new_body):
                start, end = match.span()
                if any(ps[0] <= start < ps[1] for ps in protected_spans):
                    continue
                new_body = new_body[:start] + f'[{match.group(0)}]({link})' + new_body[end:]
                break
        new_text = f"---{front_matter}---{new_body}"
        if new_text != text:
            file_path.write_text(new_text, encoding='utf-8')
            print(f"✓ Prolinkováno '{file_path}'")
    print('✅ Prolinkování klíčových pojmů dokončeno.')

if __name__ == '__main__':
    add_links()