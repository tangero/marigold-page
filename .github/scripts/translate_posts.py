import os
import requests
import frontmatter
import yaml
import hashlib
from datetime import datetime

DEEPL_API_KEY = os.environ['DEEPL_API_KEY']
DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'

def translate_text(text, target_lang='EN-US'):
    response = requests.post(DEEPL_API_URL, data={
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'target_lang': target_lang
    })
    return response.json()['translations'][0]['text']

def get_content_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

def get_latest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')]
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def process_file(file_path):
    post = frontmatter.load(file_path)
    
    # Generate new filename and path
    base_name = os.path.basename(file_path)
    new_file_name = os.path.splitext(base_name)[0] + '.md'
    new_file_path = os.path.join('_posts', 'en', new_file_name)
    
    # Create '_posts/en' directory if it doesn't exist
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    
    # Skip if English version already exists and has the same content hash
    if os.path.exists(new_file_path):
        existing_post = frontmatter.load(new_file_path)
        if 'content_hash' in existing_post and existing_post['content_hash'] == get_content_hash(post.content):
            print(f"Skipping unchanged file: {file_path}")
            return
    
    # Translate title
    post['title'] = translate_text(post['title'])
    
    # Translate content
    content = post.content
    translated_content = translate_text(content)
    post.content = translated_content
    
    # Add metadata
    post['translated'] = True
    post['original_lang'] = 'cs'
    post['content_hash'] = get_content_hash(content)
    
    # Adjust the URL
    if 'permalink' in post:
        post['permalink'] = '/en' + post['permalink']
    else:
        # If no permalink is set, we'll create one based on the filename
        permalink = '/en/item/' + os.path.splitext(new_file_name)[0] + '/'
        post['permalink'] = permalink
    
    # Save translated file
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    print(f"Translated and saved: {new_file_path}")

def main():
    latest_file = get_latest_file('_posts')
    if latest_file:
        process_file(latest_file)
    else:
        print("No files to process.")

if __name__ == '__main__':
    main()
