#!/usr/bin/env python3
"""
Enrich painting articles with detailed information using OpenRouter API.
"""
import os
import re
import json
import urllib.request
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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


def is_article_enriched(content):
    """Check if article is already enriched (has real content)."""
    # Check if it has placeholder text
    if 'neznámo' in content and len(content) < 500:
        return False
    # Check if it has substantial content
    if '## Historický kontext' in content:
        lines_after = content.split('## Historický kontext')[1].split('\n')
        # If there's content after "Historický kontext", it's enriched
        for line in lines_after[:5]:
            if line.strip() and not line.startswith('#'):
                return True
    return False


def generate_ai_content(artist, artwork):
    """Generate detailed content using OpenRouter API."""

    prompt = f"""Vytvoř detailní článek v českém jazyce o slavném uměleckém díle "{artwork}" od {artist}.

FORMÁT ODPOVĚDI - vrať pouze JSON bez dalšího textu:
{{
  "rok": "rok vytvoření díla (např. 1503-1506, nebo 1889)",
  "styl": "umělecký styl (např. renesance, impresionismus, barok)",
  "uvod": "2-3 věty úvodního odstavce o autorovi a díle, popisující jeho význam a jedinečnost",
  "kde_videt": "kde je dílo vystaveno (muzeum, město, země)",
  "autor_narozen": "rok narození - úmrtí",
  "autor_fakta": ["fakt 1 s emoji", "fakt 2 s emoji", "fakt 3 s emoji", "fakt 4 s emoji"],
  "o_obraze": ["detail 1 o díle", "detail 2 o díle", "detail 3 o díle", "detail 4 o díle"],
  "detaily": {{
    "styl_popis": "podrobný popis stylu a techniky",
    "perspektiva": "popis perspektivy a kompozice",
    "inspirace": "zdroje inspirace",
    "nalada": "nálada a atmosféra díla"
  }},
  "historicky_kontext": "2-3 věty o historickém kontextu vzniku díla",
  "srovnani": ["🖌️ **Umělec** - stručný popis podobnosti", "🎨 **Další umělec** - popis"]
}}

Pokud je {artist} "Unknown", zaměř se hlavně na dílo samotné a historický kontext."""

    try:
        api_key = os.environ.get('OPENROUTER_API_KEY')
        if not api_key:
            print("Error: OPENROUTER_API_KEY not set in .env file")
            return None

        data = {
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [
                {
                    "role": "system",
                    "content": "Jsi expert na dějiny umění. Odpovídáš pouze validním JSON bez dalšího textu nebo markdown formátování."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
            'HTTP-Referer': 'https://github.com',
            'X-Title': 'Painting Articles Generator'
        }

        req = urllib.request.Request(
            'https://openrouter.ai/api/v1/chat/completions',
            data=json.dumps(data).encode('utf-8'),
            headers=headers
        )

        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            content = result['choices'][0]['message']['content']

            # Try to extract JSON from response (in case it's wrapped in markdown)
            content = content.strip()
            if content.startswith('```json'):
                content = content.split('```json')[1].split('```')[0].strip()
            elif content.startswith('```'):
                content = content.split('```')[1].split('```')[0].strip()

            # Try to find JSON object
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))
            else:
                return json.loads(content)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"HTTP Error calling OpenRouter API: {e.code} - {error_body}")
        return None
    except Exception as e:
        print(f"Error calling OpenRouter API: {type(e).__name__}: {e}")
        return None


def create_enriched_article(filepath, ai_data):
    """Create enriched markdown article."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = extract_frontmatter(content)

    if not ai_data:
        print(f"Skipping {filepath} - no AI data")
        return False

    # Update frontmatter
    fm['namalovano'] = ai_data.get('rok', 'neznámo')
    fm['styl'] = ai_data.get('styl', '')

    # Create new content
    new_body = f"\n\n{ai_data.get('uvod', f"{fm['autor']} je {fm['obraz']}.")}\n\n"
    new_body += f"## 🖼️ Kde dílo vidět\n{ai_data.get('kde_videt', 'Informace o umístění díla.')}\n\n"
    new_body += f"## {fm['autor']}\n"
    new_body += f"- 🗓️ **Narozen/a:** {ai_data.get('autor_narozen', '')}\n"

    for fact in ai_data.get('autor_fakta', []):
        new_body += f"- {fact}\n"

    new_body += f"\n![{fm['obraz']}]({fm['urlobrazu']})\n\n"
    new_body += f"## 🎨 O obraze {fm['obraz']}\n\n"

    for detail in ai_data.get('o_obraze', []):
        new_body += f"- {detail}\n"

    detaily = ai_data.get('detaily', {})
    new_body += "\n## Pár detailů k obrazu\n\n"
    new_body += f"- 🖋️ **Styl:** {detaily.get('styl_popis', '')}\n"
    new_body += f"- 🪞 **Perspektiva:** {detaily.get('perspektiva', '')}\n"
    new_body += f"- 🎭 **Inspirace:** {detaily.get('inspirace', '')}\n"
    new_body += f"- 🌃 **Nálada:** {detaily.get('nalada', '')}\n\n"
    new_body += f"## Historický kontext\n\n{ai_data.get('historicky_kontext', '')}\n\n"
    new_body += "## Srovnání s dalšími umělci\n\n"

    for comparison in ai_data.get('srovnani', []):
        new_body += f"- {comparison}\n"

    # Reconstruct file
    new_content = "---\n"
    for key, value in fm.items():
        if value:
            # Quote values that contain special characters
            if ' ' in str(value) or ':' in str(value) or ',' in str(value):
                new_content += f'{key}: "{value}"\n'
            else:
                new_content += f'{key}: {value}\n'
        else:
            new_content += f'{key}:\n'
    new_content += "---"
    new_content += new_body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


if __name__ == '__main__':
    directory = '/Users/imac/Github/zastupitelstvo/_obrazy'
    files = get_painting_files(directory)

    print(f"Found {len(files)} painting files")

    # Filter out only the new paintings (recently created)
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
        'guernica', 'nighthawks', 'netherlandish-proverbs'
    ])]

    print(f"Processing {len(recent_files)} recently created paintings\n")

    enriched_count = 0
    skipped_count = 0
    error_count = 0

    for filepath in recent_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already enriched
        if is_article_enriched(content):
            print(f"⏭️  Already enriched: {os.path.basename(filepath)}")
            skipped_count += 1
            continue

        fm, _ = extract_frontmatter(content)
        artist = fm.get('autor', '')
        artwork = fm.get('obraz', '')

        print(f"🎨 Processing: {artwork} by {artist}")

        ai_data = generate_ai_content(artist, artwork)
        if ai_data:
            if create_enriched_article(filepath, ai_data):
                print(f"✅ Enriched {os.path.basename(filepath)}\n")
                enriched_count += 1
            else:
                print(f"❌ Failed to enrich {os.path.basename(filepath)}\n")
                error_count += 1
        else:
            print(f"❌ No AI data for {os.path.basename(filepath)}\n")
            error_count += 1

    print(f"\n{'='*60}")
    print(f"✅ Done! Enriched: {enriched_count} | Skipped: {skipped_count} | Errors: {error_count}")
    print(f"{'='*60}")
