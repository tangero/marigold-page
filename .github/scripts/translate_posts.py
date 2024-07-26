import os
import requests
import frontmatter
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

def get_latest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')]
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def main():
    log("Starting translation process")
    latest_file = get_latest_file('_posts')
    if latest_file:
        log(f"Latest file: {latest_file}")
        # Zde by byl kód pro zpracování a překlad souboru
    else:
        log("No files to process")

if __name__ == '__main__':
    main()
