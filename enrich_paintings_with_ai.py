#!/usr/bin/env python3
"""
Enrich painting articles with detailed information using AI.
"""
import os
import re
import json
import subprocess
from pathlib import Path

def get_painting_files(directory):
    """Get all markdown files from directory."""
    files = []
    for file in Path(directory).glob('*.md'):
        # Skip the example file
        if 'bar-ve-folies' not in file.name:
            files.append(str(file))
    return sorted(files)


def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)

        # Parse frontmatter
        fm_dict = {}
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm_dict[key.strip()] = value.strip().strip('"')

        return fm_dict, body
    return {}, content


def generate_ai_content(artist, artwork):
    """Generate detailed content using AI (DeepSeek API)."""

    prompt = f"""Vytvoř detailní článek v českém jazyce o slavném uměleckém díle "{artwork}" od {artist}.

FORMÁT ODPOVĚDI - vrať pouze JSON bez dalšího textu:
{{
  "rok": "rok vytvoření díla (např. 1503-1506, nebo 1889)",
  "styl": "umělecký styl (např. renesance, impresionismus, barok)",
  "uvod": "2-3 věty úvodního odstavce o autorovi a díle, popisující jeho význam a jedinečnost",
  "kde_videt": "kde je dílo vystaveno (muzeum, město, země)",
  "autor_narozen": "rok narození - úmrtí",
  "autor_fakta": ["fakt 1", "fakt 2", "fakt 3", "fakt 4"],
  "o_obraze": ["detail 1", "detail 2", "detail 3", "detail 4"],
  "detaily": {{
    "styl_popis": "podrobný popis stylu",
    "perspektiva": "popis perspektivy a kompozice",
    "inspirace": "zdroje inspirace",
    "nalada": "nálada a atmosféra díla"
  }},
  "historicky_kontext": "2-3 věty o historickém kontextu vzniku díla",
  "srovnani": ["🖌️emoji Umělec - stručný popis podobnosti", "další umělci..."]
}}

Pokud je {artist} "Unknown", zaměř se hlavně na dílo samotné a historický kontext."""

    try:
        # Use DeepSeek API via environment variable
        api_key = os.environ.get('DEEPSEEK_API_KEY')
        if not api_key:
            print("Warning: DEEPSEEK_API_KEY not set, using placeholder data")
            return None

        import urllib.request
        import json

        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "Jsi expert na dějiny umění. Odpovídáš pouze validním JSON bez dalšího textu."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        req = urllib.request.Request(
            'https://api.deepseek.com/v1/chat/completions',
            data=json.dumps(data).encode('utf-8'),
            headers=headers
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            content = result['choices'][0]['message']['content']

            # Try to extract JSON from response
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))
            else:
                return json.loads(content)

    except Exception as e:
        print(f"Error calling AI: {e}")
        return None


def create_enriched_article(filepath, ai_data):
    """Create enriched markdown article."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = extract_frontmatter(content)

    if not ai_data:
        print(f"Skipping {filepath} - no AI data")
        return

    # Update frontmatter
    fm['namalovano'] = ai_data.get('rok', 'neznámo')
    fm['styl'] = ai_data.get('styl', '')

    # Create new content
    new_body = f"""

{ai_data.get('uvod', f"{fm['autor']} je {fm['obraz']}.")}

## 🖼️ Kde dílo vidět
{ai_data.get('kde_videt', 'Informace o umístění díla.')}

## {fm['autor']}
- 🗓️ **Narozen/a:** {ai_data.get('autor_narozen', '')}
"""

    for fact in ai_data.get('autor_fakta', []):
        new_body += f"- {fact}\n"

    new_body += f"""
![{fm['obraz']}]({fm['urlobrazu']})

## 🎨 O obraze {fm['obraz']}

"""

    for detail in ai_data.get('o_obraze', []):
        new_body += f"- {detail}\n"

    detaily = ai_data.get('detaily', {})
    new_body += f"""
## Pár detailů k obrazu

- 🖋️ **Styl:** {detaily.get('styl_popis', '')}
- 🪞 **Perspektiva:** {detaily.get('perspektiva', '')}
- 🎭 **Inspirace:** {detaily.get('inspirace', '')}
- 🌃 **Nálada:** {detaily.get('nalada', '')}

## Historický kontext

{ai_data.get('historicky_kontext', '')}

## Srovnání s dalšími umělci

"""

    for comparison in ai_data.get('srovnani', []):
        new_body += f"- {comparison}\n"

    # Reconstruct file
    new_content = "---\n"
    for key, value in fm.items():
        if value:
            new_content += f'{key}: "{value}"\n' if ' ' in str(value) or ':' in str(value) else f'{key}: {value}\n'
        else:
            new_content += f'{key}:\n'
    new_content += "---\n"
    new_content += new_body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Enriched {os.path.basename(filepath)}")


if __name__ == '__main__':
    directory = '/Users/imac/Github/zastupitelstvo/_obrazy'
    files = get_painting_files(directory)

    print(f"Found {len(files)} paintings to enrich")

    # Filter out the new ones only (the ones we just created)
    recent_files = [f for f in files if any(x in f for x in [
        'venus-de-milo', 'nike-of', 'arnolfini', 'garden-of-earthly',
        'birth-of-venus', 'last-supper', 'michelangelo-david',
        'mona-lisa', 'sistine-chapel', 'school-of-athens',
        'night-watch', 'las-meninas', 'girl-with-a-pearl',
        'the-swing', 'great-wave', 'liberty-leading',
        'impression-sunrise', 'bal-du-moulin', 'starry-night',
        'edvard-munch-the-scream', 'auguste-rodin-the-thinker',
        'water-lilies', 'gustav-klimt-the-kiss', 'marcel-duchamp-fountain',
        'american-gothic', 'composition-ii', 'persistence-of-memory',
        'guernica', 'nighthawks'
    ])]

    print(f"Processing {len(recent_files)} recently created paintings")

    for filepath in recent_files[:5]:  # Start with first 5 as a test
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm, _ = extract_frontmatter(content)
        artist = fm.get('autor', '')
        artwork = fm.get('obraz', '')

        print(f"\nProcessing: {artwork} by {artist}")

        ai_data = generate_ai_content(artist, artwork)
        if ai_data:
            create_enriched_article(filepath, ai_data)
        else:
            print(f"  Skipping (no AI data)")

    print("\n✅ Done! You can now run this script again to process more paintings.")
