import os
import sys
import requests
import yaml
import feedgenerator
from datetime import datetime
from github import Github
import elevenlabs

print(f"Python version: {sys.version}")
print(f"Elevenlabs version: {elevenlabs.__version__}")

# Nastavení
PAT_TOKEN = os.environ['PAT_TOKEN']
ELEVENLABS_API_KEY = os.environ['ELEVENLABS_API_KEY']
REPO_NAME = 'tangero/marigold-page'
POSTS_DIR = '_posts'
RSS_FILE = 'podcast_feed.xml'
AUDIO_DIR = 'audio'
VOICE_ID = "NHv5TpkohJlOhwlTCzJk"

print(f"PAT_TOKEN set: {'PAT_TOKEN' in os.environ}")
print(f"ELEVENLABS_API_KEY set: {'ELEVENLABS_API_KEY' in os.environ}")

# Inicializace GitHub klienta
g = Github(PAT_TOKEN)
repo = g.get_repo(REPO_NAME)

# Nastavení API klíče pro ElevenLabs
elevenlabs.set_api_key(ELEVENLABS_API_KEY)

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
        print("Začínám generovat audio...")
        voice = elevenlabs.Voice(voice_id=VOICE_ID)
        print(f"Hlas nastaven: {voice}")
        
        audio = elevenlabs.generate(
            text=text,
            voice=voice,
            model="eleven_multilingual_v2"
        )
        print("Audio vygenerováno")
        
        elevenlabs.save(audio, filename)
        print(f"Audio úspěšně uloženo jako {filename}")
    except Exception as e:
        print(f"Chyba při generování audia: {str(e)}")
        raise

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
    try:
        print("Začínám zpracování...")
        latest_post = get_latest_post()
        print(f"Nejnovější příspěvek: {latest_post.name}")
        
        metadata, content = parse_frontmatter(latest_post.decoded_content.decode())
        print(f"Metadata: {metadata}")
        print(f"Délka obsahu: {len(content)} znaků")
        
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
        print("RSS feed vytvořen")
    except Exception as e:
        print(f"Chyba v hlavní funkci: {str(e)}")
        raise

if __name__ == "__main__":
    main()
