import os
import requests
import frontmatter
import yaml
import hashlib

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

def process_file(file_path):
    post = frontmatter.load(file_path)
    
    # Skip if already translated
    if 'translated' in post and post['translated'] == True:
        print(f"Skipping already translated file: {file_path}")
        return
    
    # Generate new filename
    base_name = os.path.basename(file_path)
    new_file_name = os.path.splitext(base_name)[0] + '-en.md'
    new_file_path = os.path.join('_posts', new_file_name)
    
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
        post['permalink'] = post['permalink'].replace('/item/', '/en/item/')
    else:
        # If no permalink is set, we'll create one based on the filename
        permalink = '/en/item/' + os.path.splitext(new_file_name)[0] + '/'
        post['permalink'] = permalink
    
    # Save translated file
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    print(f"Translated and saved: {new_file_path}")

def main():
    for file in os.listdir('_posts'):
        if file.endswith('.md') and not file.endswith('-en.md'):
            file_path = os.path.join('_posts', file)
            process_file(file_path)

if __name__ == '__main__':
    main()
