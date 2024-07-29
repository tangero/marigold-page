import os
import requests
import yaml
import feedgenerator
from datetime import datetime
from github import Github
from elevenlabs import voices, generate, save, set_api_key

# Nastavení
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
ELEVENLABS_API_KEY = os.environ['ELEVENLABS_API_KEY']
REPO_NAME = 'tangero/marigold-page'
POSTS_DIR = '_posts'
RSS_FILE = 'podcast_feed.xml'
AUDIO_DIR = 'audio'
VOICE_ID = "NHv5TpkohJlOhwlTCzJk"

# Inicializace GitHub klienta
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Nastavení API klíče pro Elevenlabs
set_api_key(ELEVENLABS_API_KEY)

def get_latest_post():
    contents = repo.get_contents(POSTS_DIR)
    posts = [content for content in contents if content.name.endswith('.md')]
    latest_post = max(posts, key=lambda x: x.commit.commit.author.date)
    return latest_post

def parse_frontmatter(content):
    _, frontmatter, body = content.split('---', 2)
    metadata = yaml.safe_load(frontmatter)
    return metadata, body.strip()

def text_to_speech(text, filename):
    try:
        # Získání objektu hlasu podle ID
        voice = next((v for v in voices() if v.voice_id == VOICE_ID), None)
        if not voice:
            raise ValueError(f"Hlas s ID {VOICE_ID} nebyl nalezen.")

        # Generování audia
        audio = generate(
            text=text,
            voice=voice,
            model="eleven_multilingual_v2"
        )
        save(audio, filename)
        print(f"Audio úspěšně vygenerováno a uloženo jako {filename}")
    except Exception as e:
        print(f"Chyba při generování audia: {str(e)}")

def create_rss_feed(items):
    feed = feedgenerator.Rss201rev2Feed(
        title="Marigold Podcast",
        link="https://www.marigold.cz/",
        description="Podcast version of Marigold blog",
        language="cs",
    )
    
    for item in items:
        feed.add_item(
            title=item['title'],
            link=item['link'],
            description=item['description'],
            pubdate=item['pubdate'],
            enclosure=feedgenerator.Enclosure(
                url=item['audio_url'],
                length=str(item['audio_size']),
                mime_type='audio/mpeg'
            )
        )
    
    with open(RSS_FILE, 'w') as f:
        feed.write(f, 'utf-8')

def main():
    latest_post = get_latest_post()
    metadata, content = parse_frontmatter(latest_post.decoded_content.decode())
    
    audio_filename = f"{AUDIO_DIR}/{latest_post.name.replace('.md', '.mp3')}"
    text_to_speech(content, audio_filename)
    
    audio_size = os.path.getsize(audio_filename)
    audio_url = f"https://raw.githubusercontent.com/{REPO_NAME}/main/{audio_filename}"
    
    items = [{
        'title': metadata['title'],
        'link': f"https://www.marigold.cz/{latest_post.name.replace('.md', '')}",
        'description': metadata.get('description', ''),
        'pubdate': datetime.strptime(metadata['date'], '%Y-%m-%d'),
        'audio_url': audio_url,
        'audio_size': audio_size
    }]
    
    create_rss_feed(items)

if __name__ == "__main__":
    main()
