#!/usr/bin/env python3
"""
Aktualizuje overall_score a overall_tier ve všech LLM markdown souborech
podle nových dat z benchmark cache.
"""

import os
import json
import re
from pathlib import Path


def main():
    # Načíst cache
    cache_path = Path(__file__).parent.parent / "_data" / "llm_benchmarks_cache.json"
    with open(cache_path) as f:
        cache = json.load(f)

    llm_dir = Path(__file__).parent.parent / "_llm"
    updated = 0

    for md_file in llm_dir.glob('*.md'):
        content = md_file.read_text(encoding='utf-8')

        # Najít model_id z front matter
        model_match = re.search(r'^model_id:\s*(.+)$', content, re.MULTILINE)
        if not model_match:
            continue

        model_id = model_match.group(1).strip()

        # Najít v cache
        if model_id not in cache.get('models', {}):
            continue

        model_data = cache['models'][model_id]
        summary = model_data.get('summary', {})
        new_score = summary.get('overall_score')
        new_tier = summary.get('overall_tier')

        if new_score is None:
            continue

        # Aktualizovat overall_score
        old_score_match = re.search(r'^overall_score:\s*([\d.]+)', content, re.MULTILINE)
        if old_score_match:
            old_score_val = float(old_score_match.group(1))
            if abs(old_score_val - new_score) > 0.01:
                # Nahradit score
                content = re.sub(
                    r'^overall_score:\s*[\d.]+',
                    f'overall_score: {new_score}',
                    content,
                    flags=re.MULTILINE
                )
                # Nahradit tier
                content = re.sub(
                    r'^overall_tier:\s*.+$',
                    f'overall_tier: {new_tier}',
                    content,
                    flags=re.MULTILINE
                )
                md_file.write_text(content, encoding='utf-8')
                print(f'Updated {md_file.name}: {old_score_val} -> {new_score} ({new_tier})')
                updated += 1

    print(f'\nTotal updated: {updated} files')


if __name__ == "__main__":
    main()
