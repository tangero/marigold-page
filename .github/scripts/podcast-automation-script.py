import os
import requests
from xml.etree.ElementTree import Element, SubElement, tostring
from github import Github

# Nastavení proměnných prostředí
API_KEY = os.getenv('ELEVENLABS_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "tangero/marigold-page"
VOICE_ID = "NHv5TpkohJlOhwlTCzJk"  # Změňte toto ID na požadované ID hlasu
CHUNK_SIZE = 1024  # Velikost chunku pro čtení/zápis

def debug_print(message):
    print(f"[DEBUG] {message}")

def text_to_speech(text, api_key, voice_id):
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
        output_path = "output.mp3"
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        debug_print(f"Audio stream saved successfully to {output_path}")
        return output_path
    else:
        debug_print(f"Error in text-to-speech API: {response.status_code}, {response.text}")
        return None

def generate_rss_feed(audio_files):
    debug_print("Generating RSS feed")
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')
    title = SubElement(channel, 'title')
    title.text = "Marigold Podcast"
    link = SubElement(channel, 'link')
    link.text = "http://www.marigold.cz/podcast"
    description = SubElement(channel, 'description')
    description.text = "Automaticky generované podcasty z článků na Marigold.cz"

    for audio_file in audio_files:
        item = SubElement(channel, 'item')
        title = SubElement(item, 'title')
        title.text = audio_file['title']
        enclosure = SubElement(item, 'enclosure', url=audio_file['url'], type="audio/mpeg")
        guid = SubElement(item, 'guid')
        guid.text = audio_file['url']

    rss_feed = tostring(rss)
    with open("rss_feed.xml", "wb") as f:
        f.write(rss_feed)
    debug_print("RSS feed generated and saved as rss_feed.xml")

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

def main():
    debug_print("Script started")
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    article_filename, article_content = get_latest_article(repo)
    if article_content:
        audio_path = text_to_speech(article_content, API_KEY, VOICE_ID)
        if audio_path:
            audio_files = [{"title": article_filename, "url": audio_path}]
            generate_rss_feed(audio_files)
    else:
        debug_print("No new article found")
    debug_print("Script finished")

if __name__ == "__main__":
    main()
