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
    """Find the most recently modified post in _posts directory (recursive)."""
    posts_dir = Path("_posts")

    if not posts_dir.exists():
        print("❌ _posts directory not found")
        return None

    # Get all markdown files recursively (including subdirectories)
    posts = sorted(posts_dir.glob("**/*.md"), key=lambda p: p.stat().st_mtime, reverse=True)

    if not posts:
        print("❌ No posts found in _posts")
        return None

    latest_post = posts[0]
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


def send_onesignal_notification(title, message):
    """Send notification via OneSignal REST API."""
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')
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
    """Check if changes are from _posts directory."""
    try:
        # Get the last commit's changed files
        result = os.popen('git diff --name-only HEAD~1 HEAD 2>/dev/null || git diff --name-only --cached 2>/dev/null').read()
        changed_files = result.strip().split('\n') if result.strip() else []

        # Filter for _posts files
        posts_changes = [f for f in changed_files if f.startswith('_posts/')]

        if not posts_changes:
            print("⚠️  No changes in _posts/ directory detected")
            return False

        return True
    except Exception as e:
        print(f"⚠️  Could not check git changes: {e}")
        # Fallback - allow notification if we can't check
        return True


def main():
    """Main function."""
    print("🔔 OneSignal Notification Sender")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    # Check if this is from _posts directory
    if not check_git_changes():
        print("⚠️  Skipping notification - not a post change")
        return 0

    # Get latest post
    latest_post = get_latest_post()
    if not latest_post:
        print("⚠️  No posts to notify about. Exiting.")
        return 0

    print(f"📝 Latest post: {latest_post.name}")

    # Extract metadata
    metadata = extract_post_metadata(latest_post)
    if not metadata:
        print("❌ Failed to extract post metadata")
        return 1

    print(f"📰 Title: {metadata['title']}")
    print(f"📄 Summary: {metadata['summary']}")
    print("-" * 50)

    # Send notification
    success = send_onesignal_notification(
        title=f"Nový článek: {metadata['title']}",
        message=metadata['summary']
    )

    if success:
        print("✅ Process completed successfully")
        return 0
    else:
        print("❌ Process failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
