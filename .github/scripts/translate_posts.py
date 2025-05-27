import os
import requests
import frontmatter
import hashlib
import sys
import re
from datetime import datetime

DEEPL_API_KEY = os.environ.get('DEEPL_API_KEY')
DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'

def log(message):
    print(message, flush=True)
    sys.stdout.flush()

def translate_text(text, target_lang='EN-US'):
    if not DEEPL_API_KEY:
        log("Error: DEEPL_API_KEY is not set")
        sys.exit(1)
    try:
        response = requests.post(DEEPL_API_URL, data={
            'auth_key': DEEPL_API_KEY,
            'text': text,
            'target_lang': target_lang
        })
        response.raise_for_status()
        return response.json()['translations'][0]['text']
    except requests.RequestException as e:
        log(f"Error during translation: {str(e)}")
        sys.exit(1)

def get_content_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

# Load environment variables
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# Optional cutoff_date for processing only newer posts
cutoff_str = os.getenv("CUTOFF_DATE")
cutoff_date = None
if cutoff_str:
    try:
        cutoff_date = datetime.strptime(cutoff_str, "%Y-%m-%d")
    except ValueError:
        log(f"Warning: ignored invalid CUTOFF_DATE: {cutoff_str}")

def get_post_date_from_filename(filename):
    match = re.match(r'^(\d{4}-\d{2}-\d{2})', filename)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        except ValueError:
            return None
    return None

def main():
    log("Starting translation process")
    posts_dir = Path('_posts')
    output_dir = posts_dir / 'en'
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in posts_dir.rglob('*.md'):
        if cutoff_date:
            date = get_post_date_from_filename(file_path.name)
            if not date or date <= cutoff_date:
                continue
        if 'en' in file_path.parts:
            continue
        post = frontmatter.load(file_path)
        if not post.metadata.get('translate', False):
            continue

        base_name = file_path.name
        new_file_path = output_dir / base_name
        if new_file_path.exists():
            existing_post = frontmatter.load(new_file_path)
            if existing_post.get('content_hash') == get_content_hash(post.content):
                log(f"Skipping unchanged file: {file_path}")
                continue

        log(f"Translating file: {file_path}")
        # Title
        post['title'] = translate_text(post.get('title', ''))
        # Excerpt
        if 'post_excerpt' in post.metadata:
            post['post_excerpt'] = translate_text(post.metadata['post_excerpt'])
        # Content
        original_content = post.content
        post.content = translate_text(original_content)

        post['translated'] = True
        post['original_lang'] = post.metadata.get('lang', 'cs')
        post['lang'] = 'en'
        post['content_hash'] = get_content_hash(original_content)

        slug = '-'.join(base_name.split('-')[3:]).replace('.md', '')
        post['permalink'] = f"/en/item/{slug}/"

        log(f"Saving translated file: {new_file_path}")
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))

    log("Translation completed")

if __name__ == '__main__':
    main()
