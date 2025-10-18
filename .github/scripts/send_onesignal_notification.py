#!/usr/bin/env python3
"""
Send push notification via OneSignal API when a new post is published.
"""

import os
import json
import requests
import sys
from datetime import datetime
from pathlib import Path
import yaml


def get_latest_post():
    """Find the most recently modified post in _posts or _vibecoding directory (recursive)."""
    posts_locations = [Path("_posts"), Path("_vibecoding")]
    all_posts = []

    for posts_dir in posts_locations:
        if posts_dir.exists():
            # Get all markdown files recursively (including subdirectories)
            posts = list(posts_dir.glob("**/*.md"))
            all_posts.extend(posts)

    if not all_posts:
        print("❌ No posts found in _posts or _vibecoding")
        return None

    # Sort by modification time (most recent first)
    latest_post = sorted(all_posts, key=lambda p: p.stat().st_mtime, reverse=True)[0]
    return latest_post


def extract_post_metadata(post_path):
    """Extract title and summary from post frontmatter using YAML parser."""
    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse front matter
        if not content.startswith('---'):
            print(f"❌ Invalid post format in {post_path}")
            return None

        # Split by --- to get frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"❌ Could not parse frontmatter in {post_path}")
            return None

        # Parse YAML front matter
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            print(f"❌ Error parsing YAML: {e}")
            return None

        if not frontmatter:
            print(f"❌ Empty frontmatter in {post_path}")
            return None

        # Extract title and summary
        title = frontmatter.get('title', 'Bez názvu')
        summary = frontmatter.get('summary', frontmatter.get('excerpt', title))

        # If summary is still just the title, use it
        if not summary or summary == title:
            summary = title

        return {
            'title': title,
            'summary': summary,
            'filename': post_path.name
        }
    except Exception as e:
        print(f"❌ Error parsing post: {e}")
        return None


def detect_website_and_get_app_id(file_path):
    """Detect which website the article is for and return corresponding App ID."""
    file_path_str = str(file_path)

    # Vibecoding App ID (from _vibecoding directory)
    ONESIGNAL_VIBECODING_APP_ID = "0c413930-f7f6-4d73-9438-36ec057acb7d"

    # Check if article is from _vibecoding
    if "_vibecoding" in file_path_str:
        print(f"🌐 Detekován vibecoding.cz článek")
        return ONESIGNAL_VIBECODING_APP_ID, "vibecoding"

    # Default to marigold (from _posts)
    print(f"🌐 Detekován marigold.cz článek")
    return os.getenv('ONESIGNAL_APP_ID'), "marigold"


def send_onesignal_notification(title, message, app_id=None):
    """Send notification via OneSignal REST API."""
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')

    if not app_id:
        app_id = os.getenv('ONESIGNAL_APP_ID')

    if not api_key or not app_id:
        print("❌ Missing ONESIGNAL_REST_API_KEY or ONESIGNAL_APP_ID environment variables")
        return False

    # OneSignal API endpoint
    url = "https://onesignal.com/api/v1/notifications"

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    # Notification payload
    payload = {
        "app_id": app_id,
        "included_segments": ["All"],  # Send to all subscribed users
        "headings": {"en": title},
        "contents": {"en": message},
        "big_picture": "",  # You can add featured image URL here
        "chrome_web_icon": "",  # You can add icon URL here
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code in [200, 201]:
            result = response.json()
            notification_id = result.get('body', {}).get('id', 'unknown')
            print(f"✅ Notification sent successfully! ID: {notification_id}")
            return True
        else:
            print(f"❌ Failed to send notification. Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except requests.exceptions.Timeout:
        print("❌ Request timeout while sending notification")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
        return False
    except json.JSONDecodeError:
        print("❌ Invalid JSON response from OneSignal API")
        return False


def check_git_changes():
    """Check if changes are from _posts or _vibecoding directory."""
    try:
        # Get the last commit's changed files
        result = os.popen('git diff --name-only HEAD~1 HEAD 2>/dev/null || git diff --name-only --cached 2>/dev/null').read()
        changed_files = result.strip().split('\n') if result.strip() else []

        # Filter for _posts or _vibecoding files
        posts_changes = [f for f in changed_files if f.startswith('_posts/') or f.startswith('_vibecoding/')]

        if not posts_changes:
            print("⚠️ Žádné změny v _posts/ nebo _vibecoding/ adresáři detekovány")
            return False

        return True
    except Exception as e:
        print(f"⚠️ Nepodařilo se zkontrolovat git změny: {e}")
        # Fallback - allow notification if we can't check
        return True


def is_new_article(file_path):
    """Check if the article is new (first commit) or an edit (multiple commits)."""
    try:
        # Počet commitů pro tento soubor (včetně renames s --follow)
        result = os.popen(f'git log --oneline --follow "{file_path}" 2>/dev/null | wc -l').read().strip()
        commit_count = int(result) if result.isdigit() else 0

        if commit_count <= 1:
            print(f"✨ Nový článek detekován (prvn commit): {file_path}")
            return True
        else:
            print(f"✏️ Oprava detekována ({commit_count} commitů): {file_path}")
            return False

    except Exception as e:
        print(f"⚠️ Chyba při kontrole git historie: {e}")
        # Fallback - assume it's new if we can't determine
        return True


def main():
    """Main function."""
    print("🔔 OneSignal Notification Sender")
    print(f"⏰ Čas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    # Check if this is from _posts directory
    if not check_git_changes():
        print("⚠️ Přeskakuji notifikaci - není změna v _posts/")
        return 0

    # Get latest post
    latest_post = get_latest_post()
    if not latest_post:
        print("⚠️ Žádné články k upozornění. Ukončuji.")
        return 0

    print(f"📝 Nejnovější článek: {latest_post.name}")

    # Detect which website this article is for
    app_id, website = detect_website_and_get_app_id(latest_post)

    # Check if it's a new article or just an edit
    if not is_new_article(str(latest_post)):
        print("✏️ Skipping notification - article was edited, not new")
        return 0

    # Extract metadata
    metadata = extract_post_metadata(latest_post)
    if not metadata:
        print("❌ Selhalo extrahování metadat")
        return 1

    print(f"📰 Titulek: {metadata['title']}")
    print(f"📄 Shrnutí: {metadata['summary']}")
    print("-" * 50)

    # Send notification
    success = send_onesignal_notification(
        title=f"🆕 Nový článek: {metadata['title']}",
        message=metadata['summary'],
        app_id=app_id
    )

    if success:
        print("✅ Proces úspěšně dokončen")
        return 0
    else:
        print("❌ Proces selhal")
        return 1


if __name__ == "__main__":
    sys.exit(main())
