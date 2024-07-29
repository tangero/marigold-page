import os
import requests
from xml.etree.ElementTree import Element, SubElement, tostring
from github import Github

# Nastavení proměnných prostředí
API_KEY = os.getenv('ELEVENLABS_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "tangero/marigold-page"

def debug_print(message):
    print(f"[DEBUG] {message}")

def text_to_speech(text, api_key):
    debug_print("Starting text-to-speech conversion")
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice": "en_us_male"  # Změňte hlas dle potřeby
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        audio_url = response.json().get("audio_url")
        debug_print(f"Audio URL received: {audio_url}")
        return audio_url
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
        if file.filename.endswith(".md"):
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
        audio_url = text_to_speech(article_content, API_KEY)
        if audio_url:
            audio_files = [{"title": article_filename, "url": audio_url}]
            generate_rss_feed(audio_files)
    else:
        debug_print("No new article found")
    debug_print("Script finished")

if __name__ == "__main__":
    main()
