#!/usr/bin/env python3
"""
Podcast Automation Script pro Marigold.cz
Generuje audio verze článků pomocí ElevenLabs API
"""

import os
import sys
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
import re
import yaml
import requests
from xml.etree.ElementTree import Element, SubElement, tostring, parse, ElementTree
from github import Github

# Konfigurace
API_KEY = os.getenv('ELEVENLABS_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "tangero/marigold-page"
VOICE_ID = "NHv5TpkohJlOhwlTCzJk"  # ID hlasu v ElevenLabs
CHUNK_SIZE = 1024
AUDIO_DIR = "audio"
BASE_URL = "https://www.marigold.cz"  # HTTPS!
RSS_FEED_PATH = "podcast-feed.xml"

def debug_print(message):
    """Výpis debug informací"""
    print(f"[DEBUG] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")

def error_print(message):
    """Výpis chybových hlášení"""
    print(f"[ERROR] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}", file=sys.stderr)

def text_to_speech(text, api_key, voice_id, output_path):
    """
    Převede text na řeč pomocí ElevenLabs API
    """
    if not api_key:
        error_print("ElevenLabs API key is not set!")
        return None
        
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
    
    try:
        response = requests.post(url, headers=headers, json=data, stream=True, timeout=60)
        response.raise_for_status()
        
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        
        debug_print(f"Audio saved successfully to {output_path}")
        return output_path
    except requests.exceptions.RequestException as e:
        error_print(f"Error in text-to-speech API: {e}")
        return None

def parse_front_matter(content):
    """
    Správně parsuje YAML front matter z markdown souboru
    """
    if not content.startswith('---'):
        return {}, content
    
    try:
        # Najde konec front matter
        end_match = re.search(r'\n---\s*\n', content[3:])
        if not end_match:
            return {}, content
        
        front_matter_text = content[3:end_match.start()+3]
        article_content = content[end_match.end()+3:]
        
        # Parse YAML
        front_matter = yaml.safe_load(front_matter_text)
        if front_matter is None:
            front_matter = {}
            
        return front_matter, article_content
    except yaml.YAMLError as e:
        error_print(f"Error parsing YAML front matter: {e}")
        return {}, content

def update_article_with_audio(repo, article_path, audio_url):
    """
    Aktualizuje článek v repository s audio URL
    """
    try:
        # Získat obsah souboru z repository
        file_content = repo.get_contents(article_path)
        content = file_content.decoded_content.decode('utf-8')
        
        # Parse front matter
        front_matter, article_body = parse_front_matter(content)
        
        # Přidat audio_url do front matter
        front_matter['audio_url'] = audio_url
        front_matter['audio_generated'] = datetime.now().isoformat()
        
        # Znovu sestavit článek
        updated_content = f"---\n{yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)}---\n{article_body}"
        
        # Aktualizovat soubor v repository
        repo.update_file(
            article_path,
            f"Add audio for {Path(article_path).name}",
            updated_content,
            file_content.sha
        )
        debug_print(f"Updated article with audio URL: {article_path}")
        return True
    except Exception as e:
        error_print(f"Failed to update article: {e}")
        return False

def extract_clean_text(content):
    """
    Extrahuje čistý text z markdown obsahu pro TTS
    """
    # Odstraní Markdown formátování
    text = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Odstraní obrázky
    text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', text)  # Odstraní odkazy, ponechá text
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)  # Odstraní nadpisy
    text = re.sub(r'[*_`]', '', text)  # Odstraní formátování
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)  # Odstraní citace
    text = re.sub(r'<[^>]+>', '', text)  # Odstraní HTML tagy
    text = re.sub(r'\n{3,}', '\n\n', text)  # Normalizuje nové řádky
    
    return text.strip()

def add_to_rss_feed(repo, audio_file_info):
    """
    Přidá položku do RSS feedu
    """
    try:
        # Zkusit získat existující feed
        try:
            feed_content = repo.get_contents(RSS_FEED_PATH)
            rss = parse(feed_content.decoded_content.decode('utf-8'))
            feed_exists = True
        except:
            # Vytvořit nový feed
            rss = Element('rss', version='2.0', attrib={
                '{http://www.w3.org/2000/xmlns/}itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'
            })
            channel = SubElement(rss, 'channel')
            SubElement(channel, 'title').text = "Marigold Podcast"
            SubElement(channel, 'link').text = f"{BASE_URL}/podcast"
            SubElement(channel, 'description').text = "Automaticky generované podcasty z článků na Marigold.cz"
            SubElement(channel, 'language').text = "cs"
            feed_exists = False
        
        # Přidat novou položku
        channel = rss.find('channel')
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = audio_file_info['title']
        SubElement(item, 'description').text = audio_file_info['description']
        SubElement(item, 'enclosure', url=audio_file_info['url'], type="audio/mpeg")
        SubElement(item, 'guid').text = audio_file_info['url']
        SubElement(item, 'pubDate').text = audio_file_info['pubDate']
        SubElement(item, 'link').text = audio_file_info['article_url']
        
        # Uložit feed
        tree = ElementTree(rss)
        feed_content_str = tostring(rss, encoding='unicode')
        
        if feed_exists:
            repo.update_file(
                RSS_FEED_PATH,
                f"Update RSS feed with {audio_file_info['title']}",
                feed_content_str,
                feed_content.sha
            )
        else:
            repo.create_file(
                RSS_FEED_PATH,
                f"Create RSS feed with {audio_file_info['title']}",
                feed_content_str
            )
        
        debug_print("RSS feed updated successfully")
        return True
    except Exception as e:
        error_print(f"Failed to update RSS feed: {e}")
        return False

def process_article(repo, article_path, article_content):
    """
    Zpracuje jeden článek - vygeneruje audio a aktualizuje repository
    """
    debug_print(f"Processing article: {article_path}")
    
    # Parse front matter
    front_matter, article_body = parse_front_matter(article_content)
    
    # Kontrola, zda má článek generovat audio
    if not front_matter.get('audio', False):
        debug_print(f"Article {article_path} does not have audio: true, skipping")
        return False
    
    # Kontrola, zda už nemá audio
    if 'audio_url' in front_matter:
        debug_print(f"Article {article_path} already has audio_url, skipping")
        return False
    
    # Extrakce metadat
    title = front_matter.get('title', 'Bez názvu')
    date = front_matter.get('date', datetime.now())
    if isinstance(date, datetime):
        date_str = date.strftime('%a, %d %b %Y %H:%M:%S +0000')
    else:
        date_str = str(date)
    
    # Příprava textu pro TTS
    clean_text = extract_clean_text(article_body)
    text_for_tts = f"{title}.\n\n{clean_text}"
    
    # Omezení délky textu (ElevenLabs má limit)
    max_chars = 5000  # Upravte podle vašeho plánu ElevenLabs
    if len(text_for_tts) > max_chars:
        text_for_tts = text_for_tts[:max_chars] + "... Text byl zkrácen."
        debug_print(f"Text truncated to {max_chars} characters")
    
    # Vytvoření názvu audio souboru
    audio_filename = Path(article_path).stem + ".mp3"
    audio_path = f"{AUDIO_DIR}/{audio_filename}"
    audio_url = f"{BASE_URL}/{audio_path}"
    
    # Dočasný soubor pro audio
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_audio:
        tmp_audio_path = tmp_audio.name
    
    try:
        # Generování audio
        if not text_to_speech(text_for_tts, API_KEY, VOICE_ID, tmp_audio_path):
            error_print("Failed to generate audio")
            return False
        
        # Upload audio do repository
        with open(tmp_audio_path, 'rb') as f:
            audio_content = f.read()
        
        try:
            # Zkusit získat existující soubor
            existing_file = repo.get_contents(audio_path)
            repo.update_file(
                audio_path,
                f"Update audio for {Path(article_path).name}",
                audio_content,
                existing_file.sha
            )
        except:
            # Vytvořit nový soubor
            repo.create_file(
                audio_path,
                f"Add audio for {Path(article_path).name}",
                audio_content
            )
        
        debug_print(f"Audio uploaded to {audio_path}")
        
        # Aktualizovat článek s audio URL
        if not update_article_with_audio(repo, article_path, audio_url):
            error_print("Failed to update article with audio URL")
            return False
        
        # Přidat do RSS feedu
        article_url = f"{BASE_URL}/item/{Path(article_path).stem}/"
        rss_info = {
            'title': title,
            'description': front_matter.get('excerpt', '')[:500],
            'url': audio_url,
            'pubDate': date_str,
            'article_url': article_url
        }
        add_to_rss_feed(repo, rss_info)
        
        return True
        
    finally:
        # Cleanup
        if os.path.exists(tmp_audio_path):
            os.remove(tmp_audio_path)

def get_recent_articles(repo, limit=10):
    """
    Získá nedávné články z repository
    """
    articles = []
    
    # Získat všechny markdown soubory z _posts
    contents = repo.get_contents("_posts")
    
    def process_contents(contents_list):
        for content in contents_list:
            if content.type == "dir":
                # Rekurzivně zpracovat podadresáře
                sub_contents = repo.get_contents(content.path)
                process_contents(sub_contents)
            elif content.name.endswith('.md') and not content.path.startswith('_posts/en/'):
                articles.append({
                    'path': content.path,
                    'name': content.name
                })
    
    process_contents(contents)
    
    # Seřadit podle data v názvu souboru (novější první)
    articles.sort(key=lambda x: x['name'], reverse=True)
    
    return articles[:limit]

def main():
    """
    Hlavní funkce scriptu
    """
    debug_print("Script started")
    
    # Kontrola proměnných prostředí
    if not API_KEY:
        error_print("ELEVENLABS_API_KEY is not set!")
        sys.exit(1)
    
    if not GITHUB_TOKEN:
        error_print("GITHUB_TOKEN is not set!")
        sys.exit(1)
    
    try:
        # Připojení k GitHub repository
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        debug_print(f"Connected to repository: {REPO_NAME}")
        
        # Získat nedávné články
        recent_articles = get_recent_articles(repo, limit=5)
        debug_print(f"Found {len(recent_articles)} recent articles")
        
        processed_count = 0
        for article_info in recent_articles:
            try:
                # Získat obsah článku
                file_content = repo.get_contents(article_info['path'])
                article_content = file_content.decoded_content.decode('utf-8')
                
                # Zpracovat článek
                if process_article(repo, article_info['path'], article_content):
                    processed_count += 1
                    debug_print(f"Successfully processed: {article_info['name']}")
                    # Zpracovat pouze jeden článek za běh (kvůli API limitům)
                    break
                    
            except Exception as e:
                error_print(f"Error processing {article_info['name']}: {e}")
                continue
        
        debug_print(f"Processed {processed_count} articles")
        
    except Exception as e:
        error_print(f"Fatal error: {e}")
        sys.exit(1)
    
    debug_print("Script finished")

if __name__ == "__main__":
    main()