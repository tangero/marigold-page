import os
import requests
import frontmatter
import hashlib
import sys
import subprocess

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

def get_latest_file(directory='_posts'):
    try:
        # Použijeme git ls-tree pro získání seznamu souborů v _posts adresáři
        result = subprocess.run(
            ['git', 'ls-tree', '-r', '--name-only', 'HEAD', directory],
            capture_output=True, text=True, check=True
        )
        files = result.stdout.strip().split('\n')
        md_files = [f for f in files if f.endswith('.md') and f.startswith(directory)]
        
        if not md_files:
            log("No .md files found in the _posts directory")
            return None
        
        # Získáme poslední commit pro každý soubor
        latest_file = None
        latest_commit_date = None
        for file in md_files:
            date_result = subprocess.run(
                ['git', 'log', '-1', '--format=%ct', file],
                capture_output=True, text=True, check=True
            )
            commit_date = int(date_result.stdout.strip())
            if latest_commit_date is None or commit_date > latest_commit_date:
                latest_file = file
                latest_commit_date = commit_date
        
        log(f"Latest file: {latest_file}")
        return latest_file
    except subprocess.CalledProcessError as e:
        log(f"Error running git command: {e}")
        return None

def process_file(file_path):
    log(f"Processing file: {file_path}")
    post = frontmatter.load(file_path)
    
    base_name = os.path.basename(file_path)
    new_file_name = os.path.splitext(base_name)[0] + '.md'
    new_file_path = os.path.join('_posts', 'en', new_file_name)
    
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    
    if os.path.exists(new_file_path):
        existing_post = frontmatter.load(new_file_path)
        if 'content_hash' in existing_post and existing_post['content_hash'] == get_content_hash(post.content):
            log(f"Skipping unchanged file: {file_path}")
            return
    
    log("Translating title")
    post['title'] = translate_text(post['title'])
    
    if 'post_excerpt' in post:
        log("Translating post_excerpt")
        post['post_excerpt'] = translate_text(post['post_excerpt'])
    
    log("Translating content")
    content = post.content
    translated_content = translate_text(content)
    post.content = translated_content
    
    post['translated'] = True
    post['original_lang'] = 'cs'
    post['lang'] = 'en'
    post['content_hash'] = get_content_hash(content)
    
    # Vytvoření správné struktury URL bez data
    post['lang'] = 'en'
    slug = '-'.join(new_file_name.split('-')[3:]).replace('.md', '')
    post['permalink'] = f"/en/item/{slug}/"
    
    log(f"Saving translated file: {new_file_path}")
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    log("File saved successfully")

def main():
    log("Starting translation process")
    latest_file = get_latest_file('_posts')
    if latest_file:
        try:
            process_file(latest_file)
            log("Translation completed successfully")
        except Exception as e:
            log(f"Error processing file: {str(e)}")
            sys.exit(1)
    else:
        log("No files to process")

if __name__ == '__main__':
    main()
