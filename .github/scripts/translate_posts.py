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

# ... (rest of the functions remain the same)

def main():
    log("Starting translation process")
    latest_file = get_latest_file('_posts')
    if latest_file:
        log(f"Processing file: {latest_file}")
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
