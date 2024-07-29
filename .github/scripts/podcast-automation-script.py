import os
import requests
from xml.etree.ElementTree import Element, SubElement, tostring, parse
from github import Github
import re
import yaml

# Nastavení proměnných prostředí
API_KEY = os.getenv('ELEVENLABS_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "tangero/marigold-page"
VOICE_ID = "NHv5TpkohJlOhwlTCzJk"  # Změňte toto ID na požadované ID hlasu
CHUNK_SIZE = 1024  # Velikost chunku pro čtení/zápis
AUDIO_DIR = "audio"  # Adresář pro ukládání audio souborů
BASE_URL = "http://www.marigold.cz"  # Základní URL pro audio soubory
RSS_FEED_PATH = "rss_feed.xml"  # Cesta k RSS feed souboru

def debug_print(message):
    print(f"[DEBUG] {message}")

def text_to_speech(text, api_key, voice_id, output_path):
    debug_print("Starting text-to-speech conversion")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    debug_print(f"Request URL: {url}")
    debug_print(f"Request headers: {headers}")
    debug_print(f"Request body: {data}")

    response = requests.post(url, headers=headers, json=data, stream=True)
    if response.ok:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        debug_print(f"Audio stream saved successfully to {output_path}")
        return output_path
    else:
        debug_print(f"Error in text-to-speech API: {response.status_code}, {response.text}")
        return None

def load_existing_rss_feed():
    if os.path.exists(RSS_FEED_PATH):
        return parse(RSS_FEED_PATH).getroot()
    else:
        rss = Element('rss', version='2.0')
        channel = SubElement(rss, 'channel')
        title = SubElement(channel, 'title')
        title.text = "Marigold Podcast"
        link = SubElement(channel, 'link')
        link.text = "http://www.marigold.cz/podcast"
        description = SubElement(channel, 'description')
        description.text = "Automaticky generované podcasty z článků na Marigold.cz"
        language = SubElement(channel, 'language')
        language.text = "cs"  # Změňte podle jazyka podcastu
        return rss

def add_item_to_rss_feed(rss, audio_file):
    channel = rss.find('channel')
    item = SubElement(channel, 'item')
    title = SubElement(item, 'title')
    title.text = audio_file['title']
    description = SubElement(item, 'description')
    description.text = audio_file['excerpt']
    enclosure = SubElement(item, 'enclosure', url=audio_file['url'], type="audio/mpeg")
    guid = SubElement(item, 'guid')
    guid.text = audio_file['url']
    pubDate = SubElement(item, 'pubDate')
    pubDate.text = audio_file['pubDate']

def save_rss_feed(rss):
    rss_feed = tostring(rss)
    with open(RSS_FEED_PATH, "wb") as f:
        f.write(rss_feed)
    debug_print(f"RSS feed saved as {RSS_FEED_PATH}")

def get_latest_article(repo):
    commits = repo.get_commits(path="_posts/")
    latest_commit = commits[0]
    files = latest_commit.files
    for file in files:
        if file.filename.startswith("_posts/") and file.filename.endswith(".md") and not file.filename.startswith("_posts/en/"):
            debug_print(f"Latest article found: {file.filename}")
            file_content = repo.get_contents(file.filename, ref=latest_commit.sha)
            return file.filename, file_content.decoded_content.decode('utf-8')
    return None, None

def extract_front_matter(article_content):
    front_matter_match = re.match(r'---\n(.*?)\n---\n', article_content, re.DOTALL)
    if front_matter_match:
        return yaml.safe_load(front_matter_match.group(1)), article_content[front_matter_match.end():]
    return {}, article_content

def update_front_matter(front_matter, audio_url):
    front_matter['audio_url'] = audio_url
    return front_matter

def reassemble_article(front_matter, content):
    front_matter_str = yaml.dump(front_matter, default_flow_style=False)
    return f"---\n{front_matter_str}---\n{content}"

def extract_title(article_content):
    lines = article_content.split('\n')
    for line in lines:
        if line.startswith('title:'):
            return line.replace('title:', '').strip()
    return "Untitled"

def extract_date(article_content):
    lines = article_content.split('\n')
    for line in lines:
        if line.startswith('date:'):
            return line.replace('date:', '').strip()
    return "No date"

def extract_excerpt(article_content):
    lines = article_content.split('\n')
    for line in lines:
        if line.startswith('excerpt:'):
            return line.replace('excerpt:', '').strip()
    return ""

def extract_clean_text(article_content):
    # Odstraní hlavičku článku
    clean_text = re.sub(r'---[\s\S]*?---', '', article_content)
    # Odstraní Markdown formátování
    clean_text = re.sub(r'!\[.*?\]\(.*?\)', '', clean_text)  # Odstraní obrázky
    clean_text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', clean_text)  # Odstraní odkazy, ponechá text odkazu
    clean_text = re.sub(r'[#*`>]', '', clean_text)  # Odstraní speciální znaky
    clean_text = re.sub(r'\n+', '\n', clean_text)  # Odstraní nadbytečné nové řádky
    return clean_text.strip()

def commit_and_push(repo, file_paths, commit_message):
    for file_path in file_paths:
        with open(file_path, "rb") as file:
            content = file.read()
        try:
            contents = repo.get_contents(file_path)
            repo.update_file(contents.path, commit_message, content, contents.sha)
        except:
            repo.create_file(file_path, commit_message, content)
    debug_print(f"Committed and pushed files: {file_paths}")

def main():
    debug_print("Script started")
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    article_filename, article_content = get_latest_article(repo)
    if article_content:
        # Vytvoření adresáře audio pokud neexistuje
        if not os.path.exists(AUDIO_DIR):
            os.makedirs(AUDIO_DIR)
        
        # Vytvoření cesty k výstupnímu souboru
        audio_filename = os.path.splitext(os.path.basename(article_filename))[0] + ".mp3"
        audio_path = os.path.join(AUDIO_DIR, audio_filename)
        audio_url = f"{BASE_URL}/{audio_path}"

        # Zkontrolujte, zda již audio soubor existuje
        if os.path.exists(audio_path):
            debug_print(f"Audio file already exists: {audio_path}")
        else:
            article_title = extract_title(article_content)
            article_date = extract_date(article_content)
            article_excerpt = extract_excerpt(article_content)
            article_text = extract_clean_text(article_content)
            text_to_convert = f"Nadpis: {article_title}\nVydáno: {article_date}\n{article_text}"

            audio_file_path = text_to_speech(text_to_convert, API_KEY, VOICE_ID, audio_path)
            if audio_file_path:
                rss = load_existing_rss_feed()
                audio_files = [{"title": article_title, "url": audio_url, "excerpt": article_excerpt, "pubDate": article_date}]
                for audio_file in audio_files:
                    add_item_to_rss_feed(rss, audio_file)
                save_rss_feed(rss)
                front_matter, content = extract_front_matter(article_content)
                updated_front_matter = update_front_matter(front_matter, audio_url)
                updated_article = reassemble_article(updated_front_matter, content)
                with open(article_filename, "w") as file:
                    file.write(updated_article)
                commit_and_push(repo, [audio_path, RSS_FEED_PATH, article_filename], f"Add audio for {article_filename}")
    else:
        debug_print("No new article found")
        debug_print("Script finished")

if __name__ == "__main__":
    main()
