#!/usr/bin/env python3
"""
NewsAPI Freshness Fix
=====================

Tento skript obsahuje navrhované úpravy pro řešení problému se starými články z NewsAPI.

PROBLÉM:
- NewsAPI /v2/top-headlines vrací články staré 2-3 dny
- Žádné čerstvé články (< 4 hodiny)
- Filename se generuje podle publishedAt, ne aktuálního data

ŘEŠENÍ:
1. Použít /v2/everything místo /v2/top-headlines
2. Přidat parametr 'from' pro poslední 24h
3. Přidat 'sortBy=publishedAt' pro seřazení od nejnovějšího
4. Možnost filtrovat podle domén (quality sources)

POUŽITÍ:
- Tento soubor obsahuje novou implementaci fetch_newsapi_articles()
- Zkopírovat do generate_tech_news_newsapi.py

Author: Test Engineer Agent
"""

import requests
import logging
from datetime import datetime, timedelta, timezone
from typing import List, Dict

logger = logging.getLogger(__name__)


class NewsAPIFreshnessFix:
    """Fixed version of NewsAPI fetching with freshness guarantee"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        # Quality tech news sources
        self.trusted_domains = [
            'techcrunch.com',
            'theverge.com',
            'arstechnica.com',
            'wired.com',
            'technologyreview.com',
            'axios.com',
            'bloomberg.com',
            'reuters.com',
            'apnews.com',
            'bbc.com',
            'cnn.com',
            'theguardian.com',
            'wsj.com',
            'nytimes.com',
            'ft.com',
            'zdnet.com',
            'cnet.com',
            'engadget.com',
            'mashable.com',
            'venturebeat.com'
        ]

    def fetch_newsapi_articles_v2_everything(
        self,
        hours_back: int = 24,
        max_results: int = 100,
        use_domain_filter: bool = True
    ) -> List[Dict]:
        """
        Stáhne články z NewsAPI /v2/everything s garantovanou čerstvostí

        Args:
            hours_back: Kolik hodin zpětně načítat (default: 24)
            max_results: Maximum článků (default: 100)
            use_domain_filter: Použít filtr domén (default: True)

        Returns:
            List článků s garantovaným publishedAt v rozsahu
        """
        if not self.api_key:
            logger.error("NewsAPI key not provided")
            return []

        # Calculate time range
        now = datetime.now(timezone.utc)
        from_time = now - timedelta(hours=hours_back)

        # Build query
        # Focus on major tech topics
        query_keywords = [
            'AI OR "artificial intelligence"',
            'OpenAI OR Anthropic OR "Google AI"',
            'Tesla OR SpaceX OR Neuralink',
            'Apple OR Microsoft OR Google OR Meta OR Amazon',
            'quantum computing',
            'robotics',
            '"self-driving" OR autonomous',
            'cryptocurrency OR blockchain',
            'cybersecurity',
            'breakthrough OR innovation'
        ]

        query = f'({" OR ".join(query_keywords)})'

        # Build request params
        params = {
            'q': query,
            'from': from_time.isoformat(),
            'to': now.isoformat(),
            'language': 'en',
            'sortBy': 'publishedAt',  # Sort by newest first
            'pageSize': min(max_results, 100),  # NewsAPI max is 100
            'apiKey': self.api_key
        }

        # Add domain filter if enabled
        if use_domain_filter:
            params['domains'] = ','.join(self.trusted_domains[:20])  # Max 20 domains

        url = 'https://newsapi.org/v2/everything'

        try:
            logger.info(f"Fetching articles from NewsAPI /v2/everything (last {hours_back}h)...")
            logger.debug(f"Query: {query[:100]}...")

            response = requests.get(url, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()

                if data['status'] == 'ok':
                    articles = data.get('articles', [])
                    logger.info(f"Fetched {len(articles)} articles from NewsAPI")

                    # Validate freshness
                    fresh_articles = self._validate_freshness(articles, hours_back)
                    logger.info(f"After freshness validation: {len(fresh_articles)} articles")

                    return fresh_articles
                else:
                    logger.error(f"NewsAPI error: {data.get('message', 'Unknown')}")
            else:
                logger.error(f"HTTP {response.status_code}: {response.text[:200]}")

        except Exception as e:
            logger.error(f"Error fetching from NewsAPI: {e}")

        return []

    def _validate_freshness(self, articles: List[Dict], max_age_hours: int) -> List[Dict]:
        """
        Validuje, že články jsou čerstvé podle publishedAt

        Args:
            articles: List článků z NewsAPI
            max_age_hours: Maximální stáří článku v hodinách

        Returns:
            Filtrovaný list pouze čerstvých článků
        """
        now = datetime.now(timezone.utc)
        fresh_articles = []
        stale_count = 0

        for article in articles:
            # Skip removed articles
            if not article.get('title') or article['title'] == '[Removed]':
                continue
            if not article.get('url'):
                continue

            # Parse published date
            pub_date_str = article.get('publishedAt')
            if not pub_date_str:
                continue

            try:
                if pub_date_str.endswith('Z'):
                    pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
                else:
                    pub_date = datetime.fromisoformat(pub_date_str)

                # Ensure UTC
                if pub_date.tzinfo is None:
                    pub_date = pub_date.replace(tzinfo=timezone.utc)
                else:
                    pub_date = pub_date.astimezone(timezone.utc)

                # Check age
                age_hours = (now - pub_date).total_seconds() / 3600

                if age_hours <= max_age_hours:
                    fresh_articles.append(article)
                else:
                    stale_count += 1
                    logger.debug(f"Filtered stale article ({age_hours:.1f}h old): {article['title'][:50]}...")

            except Exception as e:
                logger.warning(f"Could not parse date for article: {e}")
                continue

        if stale_count > 0:
            logger.warning(f"Filtered {stale_count} stale articles (older than {max_age_hours}h)")

        return fresh_articles

    def fetch_newsapi_articles_hybrid(
        self,
        try_top_headlines: bool = True,
        fallback_to_everything: bool = True
    ) -> List[Dict]:
        """
        Hybridní přístup: Zkusit top-headlines, pokud jsou staré, použít everything

        Args:
            try_top_headlines: Nejdřív zkusit /v2/top-headlines
            fallback_to_everything: Pokud top-headlines jsou staré, použít /v2/everything

        Returns:
            List čerstvých článků
        """
        articles = []

        if try_top_headlines:
            # Try top-headlines first
            articles = self._fetch_top_headlines()

            # Check freshness
            if articles:
                now = datetime.now(timezone.utc)
                newest_age = None

                for article in articles[:10]:  # Check first 10
                    pub_date_str = article.get('publishedAt')
                    if pub_date_str:
                        try:
                            pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
                            age_hours = (now - pub_date).total_seconds() / 3600

                            if newest_age is None or age_hours < newest_age:
                                newest_age = age_hours
                        except:
                            pass

                # If newest article is > 6h old, top-headlines are stale
                if newest_age and newest_age > 6:
                    logger.warning(f"Top-headlines are stale (newest: {newest_age:.1f}h), falling back to /everything")
                    articles = []

        if not articles and fallback_to_everything:
            # Fallback to /v2/everything
            logger.info("Using /v2/everything as fallback...")
            articles = self.fetch_newsapi_articles_v2_everything(hours_back=24)

        return articles

    def _fetch_top_headlines(self) -> List[Dict]:
        """Original top-headlines fetch"""
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            'category': 'technology',
            'apiKey': self.api_key,
            'pageSize': 40,
            'language': 'en'
        }

        try:
            response = requests.get(url, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'ok':
                    return data.get('articles', [])

        except Exception as e:
            logger.error(f"Error fetching top-headlines: {e}")

        return []


# Example usage and migration guide
"""
MIGRATION GUIDE
===============

V generate_tech_news_newsapi.py:

1. Import fix:
   from fix_newsapi_freshness import NewsAPIFreshnessFix

2. V __init__ přidat:
   self.freshness_fix = NewsAPIFreshnessFix(self.news_api_key)

3. Nahradit fetch_newsapi_articles():

   def fetch_newsapi_articles(self):
       # NOVÝ KÓD - použít hybrid approach
       articles = self.freshness_fix.fetch_newsapi_articles_hybrid(
           try_top_headlines=True,
           fallback_to_everything=True
       )

       # Process articles (stejný kód jako před tím)
       processed_articles = []
       for article in articles:
           # ... stejný processing ...
           pass

       return processed_articles

NEBO přímo integrovat do třídy:

   def fetch_newsapi_articles(self):
       # Direct integration
       now = datetime.now(timezone.utc)
       from_time = now - timedelta(hours=24)

       url = "https://newsapi.org/v2/everything"
       params = {
           'q': '(AI OR OpenAI OR Tesla OR Apple OR Google) AND technology',
           'from': from_time.isoformat(),
           'to': now.isoformat(),
           'language': 'en',
           'sortBy': 'publishedAt',
           'pageSize': 100,
           'apiKey': self.news_api_key
       }

       # ... rest of the code ...
"""


if __name__ == '__main__':
    # Test script
    import os
    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        print("ERROR: NEWS_API_KEY not set!")
        exit(1)

    fix = NewsAPIFreshnessFix(api_key)

    print("\n" + "="*70)
    print("TESTING NEWSAPI FRESHNESS FIX")
    print("="*70)

    # Test 1: /v2/everything
    print("\nTest 1: Fetching from /v2/everything (last 24h)...")
    articles = fix.fetch_newsapi_articles_v2_everything(hours_back=24, max_results=50)

    print(f"\nFetched {len(articles)} articles")

    if articles:
        # Analyze freshness
        now = datetime.now(timezone.utc)
        ages = []

        for article in articles[:10]:
            pub_date_str = article.get('publishedAt')
            if pub_date_str:
                try:
                    pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
                    age_hours = (now - pub_date).total_seconds() / 3600
                    ages.append(age_hours)

                    print(f"  [{age_hours:5.1f}h old] {article['title'][:60]}...")
                except:
                    pass

        if ages:
            print(f"\nFreshness stats:")
            print(f"  Newest: {min(ages):.1f}h")
            print(f"  Oldest: {max(ages):.1f}h")
            print(f"  Average: {sum(ages)/len(ages):.1f}h")

    # Test 2: Hybrid approach
    print("\n" + "-"*70)
    print("\nTest 2: Hybrid approach (top-headlines with fallback)...")
    articles = fix.fetch_newsapi_articles_hybrid()

    print(f"\nFinal article count: {len(articles)}")

    print("\n" + "="*70 + "\n")
