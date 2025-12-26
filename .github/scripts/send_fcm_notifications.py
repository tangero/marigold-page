#!/usr/bin/env python3
"""
Firebase Cloud Messaging notification sender for marigold.cz and vibecoding.cz
Runs on every commit and checks which articles were added/modified
Replaces the previous OneSignal implementation
"""

import os
import subprocess
import json
import requests
import sys
from pathlib import Path
import yaml
from datetime import datetime

# Google Auth imports
try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
except ImportError:
    print("Installing google-auth...")
    subprocess.run([sys.executable, "-m", "pip", "install", "google-auth", "-q"])
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request


def get_access_token():
    """Get OAuth 2.0 access token from service account."""
    service_account_json = os.getenv('FIREBASE_SERVICE_ACCOUNT')

    if not service_account_json:
        print("FIREBASE_SERVICE_ACCOUNT environment variable not set")
        return None

    try:
        service_account_info = json.loads(service_account_json)
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info,
            scopes=['https://www.googleapis.com/auth/firebase.messaging']
        )
        credentials.refresh(Request())
        return credentials.token
    except Exception as e:
        print(f"Failed to get access token: {e}")
        return None


def run_git_command(cmd):
    """Run git command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip()
    except Exception as e:
        print(f"Git command failed: {e}")
        return ""


def get_changed_files():
    """Get list of changed files in last commit."""
    output = run_git_command("git diff --name-only HEAD~1 HEAD 2>/dev/null")
    if not output:
        output = run_git_command("git diff --name-only --staged 2>/dev/null")

    changed_files = output.split('\n') if output else []
    return [f for f in changed_files if f.strip()]


def get_article_metadata(file_path):
    """Extract title and summary from article frontmatter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            return None

        parts = content.split('---', 2)
        if len(parts) < 3:
            return None

        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            return None

        if not frontmatter:
            return None

        title = frontmatter.get('title', 'Bez názvu')
        summary = frontmatter.get('summary', frontmatter.get('post_excerpt', frontmatter.get('excerpt', title)))

        # Get permalink/slug for URL
        slug = frontmatter.get('slug', '')
        date = frontmatter.get('date', '')

        return {
            'title': title,
            'summary': summary if summary and summary != title else title,
            'slug': slug,
            'date': str(date) if date else ''
        }
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None


def is_new_article(file_path):
    """Check if article is new (first commit) or edit (multiple commits)."""
    try:
        output = run_git_command(f'git log --oneline --follow "{file_path}" 2>/dev/null | wc -l')
        count = int(output) if output.strip().isdigit() else 0
        return count <= 1
    except:
        return True


def get_article_url(file_path, metadata, site_base):
    """Generate article URL from file path and metadata."""
    # Extract date and slug from filename
    filename = Path(file_path).stem  # e.g., "2025-12-26-article-name"
    parts = filename.split('-', 3)

    if len(parts) >= 4:
        year, month, day = parts[0], parts[1], parts[2]
        slug = parts[3] if not metadata.get('slug') else metadata.get('slug')
        return f"{site_base}/item/{slug}/"

    return site_base


def send_fcm_notification(topic, title, body, url, site_name):
    """Send notification via Firebase Cloud Messaging."""
    project_id = os.getenv('FIREBASE_PROJECT_ID')

    if not project_id:
        print(f"{site_name}: FIREBASE_PROJECT_ID not set")
        return False

    access_token = get_access_token()
    if not access_token:
        print(f"{site_name}: Failed to get access token")
        return False

    fcm_url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Use data message for more control over notification display
    payload = {
        "message": {
            "topic": topic,
            "data": {
                "title": title,
                "body": body,
                "url": url,
                "icon": f"https://www.{'marigold' if 'marigold' in topic else 'vibecoding'}.cz/assets/images/logo-192.png"
            },
            "webpush": {
                "fcm_options": {
                    "link": url
                }
            }
        }
    }

    try:
        response = requests.post(fcm_url, json=payload, headers=headers, timeout=10)

        if response.status_code == 200:
            result = response.json()
            message_id = result.get('name', 'unknown')
            print(f"{site_name}: Notifikace odeslána! Message ID: {message_id}")
            return True
        else:
            print(f"{site_name}: Chyba {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"{site_name}: Chyba při odesílání: {e}")
        return False


def main():
    """Main function."""
    print("Firebase Cloud Messaging Notification Sender")
    print(f"Cas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    # Check required environment variables
    if not os.getenv('FIREBASE_SERVICE_ACCOUNT'):
        print("FIREBASE_SERVICE_ACCOUNT is not set!")
        print("Please add the service account JSON as a GitHub Secret.")
        return 1

    if not os.getenv('FIREBASE_PROJECT_ID'):
        print("FIREBASE_PROJECT_ID is not set!")
        return 1

    # Get changed files
    changed_files = get_changed_files()

    if not changed_files:
        print("Zadne zmeny detekovany")
        return 0

    print(f"Zmenene soubory: {len(changed_files)}")
    for f in changed_files[:5]:
        print(f"   - {f}")

    # Separate articles by location
    marigold_articles = []
    vibecoding_articles = []

    for file_path in changed_files:
        if file_path.startswith('_posts/') and file_path.endswith('.md'):
            marigold_articles.append(file_path)
        elif file_path.startswith('_vibecoding/') and file_path.endswith('.md'):
            vibecoding_articles.append(file_path)

    notifications_sent = 0

    # Process Marigold articles
    if marigold_articles:
        print("\nMarigold.cz clanky:")
        for article_path in marigold_articles:
            print(f"  {article_path}")

            if not is_new_article(article_path):
                print(f"     Uprava (preskoceno)")
                continue

            metadata = get_article_metadata(article_path)
            if not metadata:
                print(f"     Nelze nacist metadata")
                continue

            print(f"     {metadata['title']}")

            url = get_article_url(article_path, metadata, "https://www.marigold.cz")

            success = send_fcm_notification(
                topic="marigold-news",
                title=f"Novy clanek: {metadata['title']}",
                body=metadata['summary'][:200],
                url=url,
                site_name="Marigold"
            )

            if success:
                notifications_sent += 1

    # Process Vibecoding articles
    if vibecoding_articles:
        print("\nVibecoding.cz clanky:")
        for article_path in vibecoding_articles:
            print(f"  {article_path}")

            if not is_new_article(article_path):
                print(f"     Uprava (preskoceno)")
                continue

            metadata = get_article_metadata(article_path)
            if not metadata:
                print(f"     Nelze nacist metadata")
                continue

            print(f"     {metadata['title']}")

            # Vibecoding URL structure
            url = get_article_url(article_path, metadata, "https://www.vibecoding.cz")

            success = send_fcm_notification(
                topic="vibecoding-news",
                title=f"Novy clanek: {metadata['title']}",
                body=metadata['summary'][:200],
                url=url,
                site_name="Vibecoding"
            )

            if success:
                notifications_sent += 1

    print("\n" + "-" * 60)
    print(f"Proces dokoncen. Odeslano notifikaci: {notifications_sent}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
