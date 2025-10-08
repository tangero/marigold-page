#!/usr/bin/env python3
"""
Add Czech translations to painting titles and update articles.
"""
import os
import re
from pathlib import Path

# Dictionary of Czech translations for famous artworks
CZECH_TRANSLATIONS = {
    "Venus de Milo": "Venuše Milská",
    "Nike of Samothrace": "Niké ze Samothráky",
    "Arnolfini Portrait": "Arnolfiniho portrét",
    "Garden of Earthly Delights": "Zahrada pozemských rozkoší",
    "The Birth of Venus": "Zrození Venuše",
    "The Last Supper": "Poslední večeře",
    "David": "David",
    "Mona Lisa": "Mona Lisa",
    "Sistine Chapel Ceiling": "Strop Sixtinské kaple",
    "School of Athens": "Athénská škola",
    "The Night Watch": "Noční hlídka",
    "Las Meninas": "Las Meninas",
    "Girl with a Pearl Earring": "Dívka s perlou",
    "The Swing": "Houpačka",
    "The Great Wave off Kanagawa": "Velká vlna u Kanagawy",
    "Liberty Leading the People": "Svoboda vede lid",
    "Impression, Sunrise": "Imprese, východ slunce",
    "Bal du moulin de la Galette": "Ples v Moulin de la Galette",
    "Starry Night": "Hvězdná noc",
    "The Scream": "Výkřik",
    "The Thinker": "Myslitel",
    "Water Lilies": "Lekníny",
    "The Kiss": "Polibek",
    "Fountain": "Fontána",
    "American Gothic": "Americká gotika",
    "Composition II in Red, Yellow, and Blue": "Kompozice II v červené, žluté a modré",
    "The Persistence of Memory": "Stálost paměti",
    "Guernica": "Guernica",
    "Nighthawks": "Noční ptáci",
    "The Netherlandish Proverbs": "Nizozemská přísloví"
}


def get_painting_files(directory):
    """Get all markdown files from directory."""
    files = []
    for file in Path(directory).glob('*.md'):
        if 'bar-ve-folies' not in file.name:
            files.append(str(file))
    return sorted(files)


def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        fm_dict = {}
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm_dict[key.strip()] = value.strip().strip('"')
        return fm_dict, body
    return {}, content


def update_article_with_czech(filepath):
    """Update article with Czech translation."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = extract_frontmatter(content)

    obraz = fm.get('obraz', '').strip('"')
    autor = fm.get('autor', '').strip('"')

    # Check if we have Czech translation
    if obraz not in CZECH_TRANSLATIONS:
        return False

    czech_name = CZECH_TRANSLATIONS[obraz]

    # Skip if already has Czech translation in title
    if czech_name in fm.get('title', ''):
        print(f"⏭️  Already has Czech: {os.path.basename(filepath)}")
        return False

    # Update frontmatter
    fm['title'] = f"{autor} - {czech_name} / {obraz}"
    fm['obraz'] = czech_name

    # Update body - replace section headers
    body = re.sub(
        r'## 🎨 O obraze ' + re.escape(obraz),
        f'## 🎨 O obraze {czech_name} - {obraz}',
        body
    )

    # Replace image alt text if needed
    body = re.sub(
        r'\!\[' + re.escape(obraz) + r'\]',
        f'![{czech_name}]',
        body
    )

    # Reconstruct file
    new_content = "---\n"
    for key, value in fm.items():
        if value:
            if ' ' in str(value) or ':' in str(value) or ',' in str(value) or '/' in str(value):
                new_content += f'{key}: "{value}"\n'
            else:
                new_content += f'{key}: {value}\n'
        else:
            new_content += f'{key}:\n'
    new_content += "---"
    new_content += body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


if __name__ == '__main__':
    directory = '/Users/imac/Github/zastupitelstvo/_obrazy'
    files = get_painting_files(directory)

    print(f"Found {len(files)} painting files\n")

    # Filter recent files
    recent_files = [f for f in files if any(x in f for x in [
        'unknown-venus-de-milo', 'unknown-nike-of', 'arnolfini', 'garden-of-earthly',
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

    print(f"Processing {len(recent_files)} paintings\n")

    updated_count = 0

    for filepath in recent_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm, _ = extract_frontmatter(content)
        obraz = fm.get('obraz', '').strip('"')

        if update_article_with_czech(filepath):
            print(f"✅ Updated with Czech: {obraz} → {CZECH_TRANSLATIONS.get(obraz)}")
            updated_count += 1

    print(f"\n{'='*60}")
    print(f"✅ Done! Updated {updated_count} articles with Czech translations")
    print(f"{'='*60}")
