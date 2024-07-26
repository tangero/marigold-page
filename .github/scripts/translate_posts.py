import os
import requests
import frontmatter
import yaml
import hashlib
import sys

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

def get_latest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')]
    if not files:
        return None
    return max(files, key=os.path.getmtime)

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
    
    log("Translating content")
    content = post.content
    translated_content = translate_text(content)
    post.content = translated_content
    
    post['translated'] = True
    post['original_lang'] = 'cs'
    post['content_hash'] = get_content_hash(content)
    
    if 'permalink' in post:
        post['permalink'] = '/en' + post['permalink']
    else:
        permalink = '/en/item/' + os.path.splitext(new_file_name)[0] + '/'
        post['permalink'] = permalink
    
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
