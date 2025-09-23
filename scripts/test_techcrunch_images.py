#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import feedparser
from bs4 import BeautifulSoup
import time
import logging

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_rss_images():
    """Test získání obrázků z TechCrunch RSS"""
    logger.info("🔍 Testování TechCrunch RSS pro obrázky...")

    rss_url = "https://techcrunch.com/feed/"
    feed = feedparser.parse(rss_url)

    if not feed.entries:
        logger.error("❌ Žádné články v RSS")
        return

    logger.info(f"📰 Nalezeno {len(feed.entries)} článků")

    for i, entry in enumerate(feed.entries[:3], 1):
        logger.info(f"\n📋 Článek {i}: {entry.title[:50]}...")
        logger.info(f"🔗 URL: {entry.link}")

        # Test různých RSS image metod
        image_found = False

        # 1. Media thumbnail
        if hasattr(entry, 'media_thumbnail') and entry.media_thumbnail:
            logger.info(f"🖼️ Media thumbnail: {entry.media_thumbnail[0].get('url')}")
            image_found = True

        # 2. Media content
        if hasattr(entry, 'media_content') and entry.media_content:
            for media in entry.media_content:
                if media.get('type', '').startswith('image'):
                    logger.info(f"🖼️ Media content: {media.get('url')}")
                    image_found = True

        # 3. Enclosures
        if hasattr(entry, 'enclosures') and entry.enclosures:
            for enc in entry.enclosures:
                if enc.get('type', '').startswith('image'):
                    logger.info(f"🖼️ Enclosure: {enc.get('href')}")
                    image_found = True

        # 4. Content parsing
        content = ''
        if hasattr(entry, 'content') and entry.content:
            content = entry.content[0].get('value', '')
        elif hasattr(entry, 'summary'):
            content = entry.summary

        if content:
            soup = BeautifulSoup(content, 'html.parser')
            img = soup.find('img')
            if img and img.get('src'):
                logger.info(f"🖼️ Content image: {img.get('src')}")
                image_found = True

        if not image_found:
            logger.warning("❌ Žádný obrázek nenalezen v RSS")

        logger.info("-" * 60)

def test_og_image_extraction(url):
    """Test získání OG image z konkrétního URL"""
    logger.info(f"🔍 Testování OG image extraction z: {url[:50]}...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Marigold.cz Tech News Bot)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        logger.info(f"📡 HTTP Status: {response.status_code}")
        logger.info(f"📝 Content-Type: {response.headers.get('content-type', 'Unknown')}")

        if not response.ok:
            logger.error(f"❌ HTTP chyba: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        # Test různých meta tagů
        images_found = []

        # 1. Open Graph image
        og_image = soup.find('meta', property='og:image')
        if og_image:
            og_url = og_image.get('content')
            logger.info(f"✅ OG Image: {og_url}")
            images_found.append(('og:image', og_url))

            # Další OG image properties
            og_width = soup.find('meta', property='og:image:width')
            og_height = soup.find('meta', property='og:image:height')
            if og_width and og_height:
                logger.info(f"📐 OG Dimensions: {og_width.get('content')}x{og_height.get('content')}")

        # 2. Twitter Card image
        twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
        if twitter_image:
            twitter_url = twitter_image.get('content')
            logger.info(f"✅ Twitter Image: {twitter_url}")
            images_found.append(('twitter:image', twitter_url))

        # 3. Schema.org image
        schema_image = soup.find('meta', attrs={'itemprop': 'image'})
        if schema_image:
            schema_url = schema_image.get('content')
            logger.info(f"✅ Schema.org Image: {schema_url}")
            images_found.append(('schema:image', schema_url))

        # 4. Article image
        article_image = soup.find('meta', attrs={'name': 'twitter:image:src'})
        if article_image:
            article_url = article_image.get('content')
            logger.info(f"✅ Article Image: {article_url}")
            images_found.append(('article:image', article_url))

        # 5. Featured image v HTML
        featured_selectors = [
            'img.wp-post-image',
            'img.featured-image',
            'img.post-featured-image',
            '.post-featured img',
            '.featured-image img',
            'article img:first-of-type'
        ]

        for selector in featured_selectors:
            featured_img = soup.select_one(selector)
            if featured_img and featured_img.get('src'):
                featured_url = featured_img.get('src')
                logger.info(f"✅ Featured Image ({selector}): {featured_url}")
                images_found.append(('featured', featured_url))
                break

        # 6. První obrázek v článku
        article_selectors = [
            'article img',
            '.post-content img',
            '.entry-content img',
            '.content img'
        ]

        for selector in article_selectors:
            first_img = soup.select_one(selector)
            if first_img and first_img.get('src'):
                first_url = first_img.get('src')
                # Přeskočit malé obrázky (ikony, logá)
                src = first_img.get('src', '')
                if not any(skip in src.lower() for skip in ['icon', 'logo', 'avatar', 'favicon']):
                    logger.info(f"✅ First Article Image ({selector}): {first_url}")
                    images_found.append(('first_article', first_url))
                    break

        if not images_found:
            logger.warning("❌ Žádné obrázky nenalezeny")

        return images_found

    except requests.RequestException as e:
        logger.error(f"❌ Request chyba: {e}")
        return None
    except Exception as e:
        logger.error(f"❌ Parsing chyba: {e}")
        return None

def test_multiple_techcrunch_articles():
    """Test na více TechCrunch článcích"""
    logger.info("🔍 Testování více TechCrunch článků...")

    # Získat články z RSS
    feed = feedparser.parse("https://techcrunch.com/feed/")

    if not feed.entries:
        logger.error("❌ Nelze načíst RSS")
        return

    success_count = 0
    total_tested = min(5, len(feed.entries))

    for i, entry in enumerate(feed.entries[:total_tested], 1):
        logger.info(f"\n{'='*60}")
        logger.info(f"ČLÁNEK {i}/{total_tested}: {entry.title[:60]}...")
        logger.info(f"URL: {entry.link}")
        logger.info('='*60)

        images = test_og_image_extraction(entry.link)
        if images:
            success_count += 1
            logger.info(f"✅ Úspěch: {len(images)} obrázků nalezeno")
        else:
            logger.warning("❌ Neúspěch: žádné obrázky")

        # Rate limiting
        time.sleep(2)

    logger.info(f"\n📊 SHRNUTÍ: {success_count}/{total_tested} článků s obrázky ({success_count/total_tested*100:.1f}%)")

def test_different_user_agents():
    """Test různých User-Agent stringů"""
    test_url = "https://techcrunch.com/2025/09/23/strictlyvc-at-disrupt-2025-the-full-lp-track-agenda-revealed/"

    user_agents = [
        'Mozilla/5.0 (Marigold.cz Tech News Bot)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Googlebot/2.1 (+http://www.google.com/bot.html)',
        'facebookexternalhit/1.1'
    ]

    for i, ua in enumerate(user_agents, 1):
        logger.info(f"\n🤖 Test {i}: {ua[:50]}...")

        headers = {'User-Agent': ua}
        try:
            response = requests.get(test_url, headers=headers, timeout=10)
            logger.info(f"📡 Status: {response.status_code}")

            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                og_image = soup.find('meta', property='og:image')
                if og_image:
                    logger.info(f"✅ OG Image nalezen: {og_image.get('content')[:50]}...")
                else:
                    logger.warning("❌ OG Image nenalezen")

        except Exception as e:
            logger.error(f"❌ Chyba: {e}")

        time.sleep(1)

def main():
    """Hlavní test funkce"""
    logger.info("🚀 Spouštím diagnostiku TechCrunch obrázků")

    print("\n" + "="*80)
    print("1. TEST RSS FEED OBRÁZKŮ")
    print("="*80)
    test_rss_images()

    print("\n" + "="*80)
    print("2. TEST OG IMAGE EXTRACTION")
    print("="*80)
    test_url = "https://techcrunch.com/2025/09/23/strictlyvc-at-disrupt-2025-the-full-lp-track-agenda-revealed/"
    test_og_image_extraction(test_url)

    print("\n" + "="*80)
    print("3. TEST VÍCE ČLÁNKŮ")
    print("="*80)
    test_multiple_techcrunch_articles()

    print("\n" + "="*80)
    print("4. TEST RŮZNÝCH USER AGENTS")
    print("="*80)
    test_different_user_agents()

if __name__ == "__main__":
    main()