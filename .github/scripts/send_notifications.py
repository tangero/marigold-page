#!/usr/bin/env python3
"""
Universal OneSignal notification sender for both marigold.cz and vibecoding.cz
Runs on every commit and checks which articles were added/modified
"""

import os
import subprocess
import json
import requests
import sys
from pathlib import Path
import yaml
from datetime import datetime


def run_git_command(cmd):
    """Run git command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ Git command failed: {e}")
        return ""


def get_changed_files():
    """Get list of changed files in last commit."""
    # Get files changed between HEAD~1 and HEAD
    output = run_git_command("git diff --name-only HEAD~1 HEAD 2>/dev/null")
    if not output:
        # Fallback for first commit or detached head
        output = run_git_command("git diff --name-only --staged 2>/dev/null")

    changed_files = output.split('\n') if output else []
    return [f for f in changed_files if f.strip()]


def get_article_metadata(file_path):
    """Extract title and summary from article frontmatter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse front matter
        if not content.startswith('---'):
            return None

        parts = content.split('---', 2)
        if len(parts) < 3:
            return None

        # Parse YAML
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            return None

        if not frontmatter:
            return None

        title = frontmatter.get('title', 'Bez názvu')
        summary = frontmatter.get('summary', frontmatter.get('post_excerpt', frontmatter.get('excerpt', title)))

        if not summary or summary == title:
            summary = title

        return {
            'title': title,
            'summary': summary
        }
    except Exception as e:
        print(f"⚠️ Error parsing {file_path}: {e}")
        return None


def is_new_article(file_path):
    """Check if article is new (first commit) or edit (multiple commits)."""
    try:
        # Count commits for this file (follow renames)
        output = run_git_command(f'git log --oneline --follow "{file_path}" 2>/dev/null | wc -l')
        count = int(output) if output.isdigit() else 0
        return count <= 1  # New if 1 or fewer commits
    except:
        return True  # Fallback: assume new


def send_notification(title, message, app_id, website_name):
    """Send notification via OneSignal API."""
    api_key = os.getenv('ONESIGNAL_REST_API_KEY')

    if not api_key or not app_id:
        print(f"❌ Missing credentials for {website_name}")
        return False

    url = "https://onesignal.com/api/v1/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    payload = {
        "app_id": app_id,
        "included_segments": ["Total Subscriptions"],
        "headings": {"en": title, "cs": title},
        "contents": {"en": message, "cs": message},
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code in [200, 201]:
            result = response.json()
            notification_id = result.get('id', 'unknown')
            recipients = result.get('recipients', 0)
            print(f"✅ {website_name}: Notifikace poslána! ID: {notification_id}, Příjemci: {recipients}")
            return True
        else:
            print(f"❌ {website_name}: Chyba {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ {website_name}: Chyba při odesílání: {e}")
        return False


def main():
    """Main function."""
    print("🔔 OneSignal Notification Sender (Universal)")
    print(f"⏰ Čas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    # Get changed files
    changed_files = get_changed_files()

    if not changed_files:
        print("⚠️ Žádné změny detekovány")
        return 0

    print(f"📝 Změněné soubory: {len(changed_files)}")
    for f in changed_files[:5]:  # Show first 5
        print(f"   - {f}")

    # Separate articles by location
    marigold_articles = []
    vibecoding_articles = []

    for file_path in changed_files:
        if file_path.startswith('_posts/') and file_path.endswith('.md'):
            marigold_articles.append(file_path)
        elif file_path.startswith('_vibecoding/') and file_path.endswith('.md'):
            vibecoding_articles.append(file_path)

    # Process Marigold articles
    if marigold_articles:
        print("\n🌐 Marigold.cz články:")
        for article_path in marigold_articles:
            print(f"  📄 {article_path}")

            # Check if new
            if not is_new_article(article_path):
                print(f"     ✏️ Úprava (přeskočeno)")
                continue

            # Get metadata
            metadata = get_article_metadata(article_path)
            if not metadata:
                print(f"     ❌ Nelze načíst metadata")
                continue

            print(f"     📰 {metadata['title']}")

            # Send notification
            send_notification(
                title=f"🆕 Nový článek: {metadata['title']}",
                message=metadata['summary'],
                app_id=os.getenv('ONESIGNAL_MARIGOLD_APP_ID'),
                website_name="Marigold"
            )

    # Process Vibecoding articles
    if vibecoding_articles:
        print("\n🌐 Vibecoding.cz články:")
        for article_path in vibecoding_articles:
            print(f"  📄 {article_path}")

            # Check if new
            if not is_new_article(article_path):
                print(f"     ✏️ Úprava (přeskočeno)")
                continue

            # Get metadata
            metadata = get_article_metadata(article_path)
            if not metadata:
                print(f"     ❌ Nelze načíst metadata")
                continue

            print(f"     📰 {metadata['title']}")

            # Send notification
            send_notification(
                title=f"🆕 Nový článek: {metadata['title']}",
                message=metadata['summary'],
                app_id=os.getenv('ONESIGNAL_VIBECODING_APP_ID'),
                website_name="Vibecoding"
            )

    print("\n" + "-" * 60)
    print("✅ Proces dokončen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
