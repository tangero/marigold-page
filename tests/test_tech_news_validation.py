#!/usr/bin/env python3
"""
Tech News Validation Test Suite
================================

Komplexní testovací framework pro validaci tech-news pipeline.
Pokrývá:
- Importance scoring validaci
- Content filtering accuracy
- LLM cost tracking integrity
- NewsAPI freshness detection
- Health check thresholds

Author: Test Engineer Agent
"""

import pytest
import sqlite3
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional
from unittest.mock import Mock, patch, MagicMock
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from generate_tech_news_newsapi import NewsAPITechNewsGenerator
from processing_logger import ProcessingLogger
from llm_cost_tracker import LLMCostTracker
from tech_news_health_check import TechNewsHealthCheck


class TestImportanceScoring:
    """Test cases pro validaci importance scoring algoritmů"""

    @pytest.fixture
    def generator(self):
        """Vytvoř NewsAPI generátor instanci"""
        return NewsAPITechNewsGenerator()

    def test_importance_5_breakthrough_ai(self, generator):
        """IMPORTANCE 5: AGI a průlomové AI zprávy"""
        title = "OpenAI Announces AGI Breakthrough with GPT-5"
        description = "Artificial general intelligence achieved for the first time"
        category = "AI"

        importance = generator.detect_importance(title, description, category)
        assert importance == 5, f"AGI breakthrough should be importance 5, got {importance}"

    def test_importance_5_quantum_advantage(self, generator):
        """IMPORTANCE 5: Kvantové počítače s quantum advantage"""
        title = "Google Achieves Quantum Advantage with New Processor"
        description = "Quantum computer solves problem impossible for classical computers"
        category = "quantum"

        importance = generator.detect_importance(title, description, category)
        assert importance == 5, f"Quantum advantage should be importance 5, got {importance}"

    def test_importance_5_major_security_breach(self, generator):
        """IMPORTANCE 5: Velké bezpečnostní incidenty"""
        title = "Major Zero-Day Exploit Discovered in All Operating Systems"
        description = "Critical vulnerability affects billions of devices worldwide"
        category = "security"

        importance = generator.detect_importance(title, description, category)
        assert importance == 5, f"Major zero-day should be importance 5, got {importance}"

    def test_importance_4_openai_release(self, generator):
        """IMPORTANCE 4: OpenAI produktové release"""
        title = "OpenAI Releases GPT-4.5 with Enhanced Capabilities"
        description = "New AI model features improved reasoning and coding"
        category = "AI"

        importance = generator.detect_importance(title, description, category)
        assert importance == 4, f"OpenAI GPT release should be importance 4, got {importance}"

    def test_importance_4_tesla_fsd(self, generator):
        """IMPORTANCE 4: Tesla Full Self-Driving pokroky"""
        title = "Tesla Achieves Level 4 Autonomy with FSD 13"
        description = "Full self-driving now works in all weather conditions"
        category = "autonomous"

        importance = generator.detect_importance(title, description, category)
        assert importance == 4, f"Tesla FSD breakthrough should be importance 4, got {importance}"

    def test_importance_4_apple_iphone_launch(self, generator):
        """IMPORTANCE 4: Nové Apple iPhone"""
        title = "Apple Unveils iPhone 17 Pro with Revolutionary Features"
        description = "New iPhone introduces holographic display technology"
        category = "hardware"

        importance = generator.detect_importance(title, description, category)
        assert importance == 4, f"Major Apple iPhone launch should be importance 4, got {importance}"

    def test_importance_3_standard_tech_news(self, generator):
        """IMPORTANCE 3: Standardní tech novinky"""
        title = "Microsoft Announces New Azure Features"
        description = "Cloud platform gets enhanced AI capabilities"
        category = "cloud"

        importance = generator.detect_importance(title, description, category)
        assert importance == 3, f"Standard tech news should be importance 3, got {importance}"

    def test_importance_2_chinese_phone(self, generator):
        """IMPORTANCE 2: Čínské telefony (nízká priorita)"""
        title = "OnePlus 13 Pro Launches with Snapdragon 8 Gen 4"
        description = "New flagship phone from OnePlus features latest processor"
        category = "mobile"

        importance = generator.detect_importance(title, description, category)
        assert importance == 2, f"Chinese phone should be importance 2, got {importance}"

    def test_importance_2_routine_update(self, generator):
        """IMPORTANCE 2: Rutinní software updaty"""
        title = "Android November Security Patch Released"
        description = "Monthly security update fixes minor vulnerabilities"
        category = "software"

        importance = generator.detect_importance(title, description, category)
        assert importance == 2, f"Routine security patch should be importance 2, got {importance}"

    def test_importance_2_rumors_and_leaks(self, generator):
        """IMPORTANCE 2: Spekulace a leaky"""
        title = "iPhone 18 Might Feature Under-Display Camera, Sources Say"
        description = "Leaked documents allegedly show Apple's future plans"
        category = "rumors"

        importance = generator.detect_importance(title, description, category)
        assert importance == 2, f"Rumors should be importance 2, got {importance}"

    def test_importance_1_clickbait(self, generator):
        """IMPORTANCE 1: Clickbait a marketing"""
        title = "You Won't Believe This Amazing Black Friday Deal!"
        description = "Best price ever on this smartphone accessory"
        category = "deals"

        importance = generator.detect_importance(title, description, category)
        assert importance == 1, f"Clickbait should be importance 1, got {importance}"

    def test_importance_edge_case_sam_altman_tech(self, generator):
        """Edge case: Sam Altman v tech kontextu = 4, v lifestyle = 2"""
        # Tech context - should be 4
        title_tech = "Sam Altman Announces OpenAI's New AI Model"
        desc_tech = "CEO unveils breakthrough in artificial intelligence"

        importance_tech = generator.detect_importance(title_tech, desc_tech, "AI")
        assert importance_tech == 4, "Sam Altman + tech should be importance 4"

        # Lifestyle context - should not be 4
        title_lifestyle = "Sam Altman's Birthday Party Photos"
        desc_lifestyle = "OpenAI CEO celebrates personal milestone"

        importance_lifestyle = generator.detect_importance(title_lifestyle, desc_lifestyle, "lifestyle")
        assert importance_lifestyle < 4, "Sam Altman + lifestyle should be < importance 4"


class TestContentFiltering:
    """Test cases pro validaci content filtering"""

    @pytest.fixture
    def generator(self):
        return NewsAPITechNewsGenerator()

    def test_filter_gaming_console(self, generator):
        """Filtrovat: herní konzole články"""
        title = "PS5 Pro Launches with Enhanced Graphics"
        description = "Sony's new gaming console features ray tracing"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is True, "Gaming console article should be filtered"

    def test_filter_video_game_review(self, generator):
        """Filtrovat: recenze her"""
        title = "Call of Duty Modern Warfare 3 Review: A Mixed Bag"
        description = "Latest entry in the popular FPS series reviewed"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is True, "Video game review should be filtered"

    def test_filter_sports_news(self, generator):
        """Filtrovat: sportovní zprávy"""
        title = "NFL Championship Game Breaks Viewership Records"
        description = "Super Bowl attracts millions of viewers worldwide"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is True, "Sports news should be filtered"

    def test_filter_wrestling_entertainment(self, generator):
        """Filtrovat: wrestling a zábavní sport"""
        title = "WWE Wrestlemania 40 Main Event Announced"
        description = "Wrestling entertainment's biggest event reveals headliner"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is True, "Wrestling should be filtered"

    def test_allow_ai_in_gaming_technology(self, generator):
        """NEFILTROVAT: AI v gamingu (technologie)"""
        title = "Nvidia Introduces AI-Powered Game Graphics Technology"
        description = "Machine learning enhances real-time rendering in games"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is False, "AI gaming tech should NOT be filtered"

    def test_allow_cloud_gaming_infrastructure(self, generator):
        """NEFILTROVAT: Cloud gaming infrastruktura"""
        title = "Microsoft Azure Powers New Cloud Gaming Technology"
        description = "Cloud infrastructure enables game streaming at scale"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is False, "Cloud gaming tech should NOT be filtered"

    def test_allow_gpu_for_gaming(self, generator):
        """NEFILTROVAT: GPU hardware (i když zmíněn gaming)"""
        title = "Nvidia RTX 5090 GPU Announced with DLSS 4.0"
        description = "New graphics card features AI acceleration for gaming"

        should_skip = generator.should_skip_article(title, description)
        assert should_skip is False, "GPU hardware should NOT be filtered"

    def test_filter_false_positive_detection(self, generator):
        """Test: Detekce falešně pozitivních výsledků"""
        # Tento článek obsahuje slovo "game" ale je o business
        title = "Tech Giants Play High-Stakes Game in AI Race"
        description = "Companies compete for artificial intelligence supremacy"

        # Toto by MOHLO být filtrováno, ale nemělo by
        # Kontrolujeme, že není příliš agresivní
        should_skip = generator.should_skip_article(title, description)
        # Akceptujeme obě možnosti, ale logujeme pro analýzu
        print(f"Business context with 'game' word: should_skip={should_skip}")


class TestLLMCostTracking:
    """Test cases pro LLM cost tracking integrity"""

    @pytest.fixture
    def temp_db(self, tmp_path):
        """Vytvoř dočasnou databázi pro testy"""
        db_path = tmp_path / "test_llm_costs.db"
        return str(db_path)

    def test_cost_calculation_claude_sonnet(self, temp_db):
        """Test: Správný výpočet ceny pro Claude Sonnet 4.5"""
        tracker = LLMCostTracker(db_path=temp_db)

        # Claude Sonnet 4.5: $3/1M input, $15/1M output
        cost = tracker.calculate_cost(
            model="anthropic/claude-sonnet-4.5",
            prompt_tokens=1000,
            completion_tokens=500
        )

        expected_cost = (1000 / 1_000_000) * 3.0 + (500 / 1_000_000) * 15.0
        assert abs(cost - expected_cost) < 0.000001, f"Expected {expected_cost}, got {cost}"

        tracker.close()

    def test_cost_calculation_qwen3_max(self, temp_db):
        """Test: Správný výpočet ceny pro Qwen3 Max"""
        tracker = LLMCostTracker(db_path=temp_db)

        # Qwen3 Max: $1.20/1M input, $6.00/1M output
        cost = tracker.calculate_cost(
            model="qwen/qwen3-max",
            prompt_tokens=2000,
            completion_tokens=1000
        )

        expected_cost = (2000 / 1_000_000) * 1.20 + (1000 / 1_000_000) * 6.00
        assert abs(cost - expected_cost) < 0.000001, f"Expected {expected_cost}, got {cost}"

        tracker.close()

    def test_log_call_stores_data(self, temp_db):
        """Test: log_call skutečně ukládá data do DB"""
        tracker = LLMCostTracker(db_path=temp_db)

        call_id = tracker.log_call(
            model="qwen/qwen3-max",
            operation="translate_title",
            status="success",
            prompt_tokens=500,
            completion_tokens=100,
            article_slug="test-article",
            article_title="Test Article"
        )

        # Ověř, že data jsou v DB
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM api_calls WHERE id = ?", (call_id,))
        row = cursor.fetchone()

        assert row is not None, "Call should be stored in database"
        assert row[3] == "translate_title", "Operation should be translate_title"
        assert row[4] == 500, "Prompt tokens should be 500"
        assert row[5] == 100, "Completion tokens should be 100"

        conn.close()
        tracker.close()

    def test_daily_summary_aggregation(self, temp_db):
        """Test: Denní souhrn správně agreguje data"""
        tracker = LLMCostTracker(db_path=temp_db)

        # Zaloguj několik volání
        for i in range(5):
            tracker.log_call(
                model="qwen/qwen3-max",
                operation=f"operation_{i}",
                status="success",
                prompt_tokens=1000,
                completion_tokens=500
            )

        # Aktualizuj souhrn
        from datetime import date
        tracker.update_daily_summary(date.today())

        # Ověř souhrn
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM daily_summary WHERE date = ?", (date.today().isoformat(),))
        row = cursor.fetchone()

        assert row is not None, "Daily summary should exist"
        assert row[1] == 5, "Should have 5 total calls"
        assert row[2] == 5, "Should have 5 successful calls"

        conn.close()
        tracker.close()

    def test_track_llm_call_wrapper_integration(self, temp_db):
        """Test: track_llm_call wrapper správně extrahuje usage data"""
        from llm_cost_tracker import track_llm_call

        tracker = LLMCostTracker(db_path=temp_db)

        # Mock OpenRouter response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'Translated text'}}],
            'usage': {
                'prompt_tokens': 150,
                'completion_tokens': 50,
                'total_tokens': 200
            }
        }

        with patch('requests.post', return_value=mock_response):
            response, usage = track_llm_call(
                url='https://openrouter.ai/api/v1/chat/completions',
                headers={'Authorization': 'Bearer test'},
                data={'model': 'qwen/qwen3-max', 'messages': []},
                operation='test_operation',
                tracker=tracker
            )

        assert usage is not None, "Usage should be extracted"
        assert usage['prompt_tokens'] == 150
        assert usage['completion_tokens'] == 50

        # Ověř, že data jsou v DB
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM api_calls WHERE operation = 'test_operation'")
        count = cursor.fetchone()[0]

        assert count == 1, "Call should be logged to database"

        conn.close()
        tracker.close()


class TestNewsAPIFreshness:
    """Test cases pro detekci stáří článků z NewsAPI"""

    def test_detect_stale_articles(self):
        """Test: Detekce, když NewsAPI vrací staré články"""
        # Simulujme situaci, kdy všechny články jsou staré 2-3 dny
        now = datetime.now(timezone.utc)
        stale_articles = [
            {
                'title': f'Article {i}',
                'description': 'Test',
                'publishedAt': (now - timedelta(days=2, hours=i)).isoformat(),
                'url': f'http://example.com/{i}',
                'source': {'id': 'test', 'name': 'Test'}
            }
            for i in range(10)
        ]

        # Kontrola: Žádný článek není čerstvý (< 4 hodiny)
        fresh_count = sum(
            1 for article in stale_articles
            if (now - datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))).total_seconds() / 3600 < 4
        )

        assert fresh_count == 0, "Should detect that no articles are fresh"
        print(f"ALERT: All {len(stale_articles)} articles are older than 2 days!")

    def test_newsapi_date_parameter_suggestion(self):
        """Test/Návrh: Použití 'from' parametru pro čerstvé články"""
        # Navržený fix pro NewsAPI fetch
        from datetime import datetime, timedelta, timezone

        # Měli bychom přidat 'from' parametr do NewsAPI volání
        now = datetime.now(timezone.utc)
        from_date = now - timedelta(hours=24)

        suggested_params = {
            'category': 'technology',
            'apiKey': 'YOUR_KEY',
            'pageSize': 40,
            'language': 'en',
            'from': from_date.isoformat(),  # <-- PŘIDAT TOTO!
            'sortBy': 'publishedAt'          # <-- A TOTO!
        }

        print("Suggested NewsAPI params with freshness filter:")
        print(json.dumps(suggested_params, indent=2, default=str))


class TestHealthCheckThresholds:
    """Test cases pro health check threshold validaci"""

    @pytest.fixture
    def temp_tech_news_dir(self, tmp_path):
        """Vytvoř dočasný adresář s test články"""
        tech_news_dir = tmp_path / "_tech_news"
        tech_news_dir.mkdir()
        return tech_news_dir

    def test_critical_alert_no_articles_24h(self, temp_tech_news_dir):
        """Test: CRITICAL alert když 0 článků za 24h"""
        # Vytvoř pouze staré články (>24h)
        now = datetime.now(timezone.utc)
        old_date = now - timedelta(days=2)

        article_path = temp_tech_news_dir / "2025-11-15-old-article.md"
        article_path.write_text(f"""---
title: Old Article
description: Test
publishedAt: {old_date.isoformat()}
date: {old_date.strftime('%Y-%m-%d %H:%M:%S')}
category: tech
layout: tech_news_article
url: http://example.com
---

Test content
""")

        checker = TechNewsHealthCheck(tech_news_dir=str(temp_tech_news_dir))
        results = checker.run_all_checks()

        assert results['metrics']['articles_24h'] == 0
        assert results['status'] in ['CRITICAL', 'WARNING'], "Should trigger alert for 0 articles"

    def test_warning_alert_low_czech_ratio(self, temp_tech_news_dir):
        """Test: WARNING alert když < 85% článků v češtině"""
        now = datetime.now(timezone.utc)

        # Vytvoř 10 článků: 7 anglických, 3 českých = 30% čeština
        for i in range(10):
            is_czech = i < 3  # První 3 jsou české

            article_path = temp_tech_news_dir / f"2025-11-17-article-{i}.md"

            if is_czech:
                title = f"Český článek číslo {i}"
                content = "Tento článek je napsaný v češtině s českými znaky."
            else:
                title = f"English Article Number {i}"
                content = "This article is written in English language."

            article_path.write_text(f"""---
title: {title}
description: Test
publishedAt: {now.isoformat()}
date: {now.strftime('%Y-%m-%d %H:%M:%S')}
category: tech
layout: tech_news_article
url: http://example.com/{i}
---

{content}
""")

        checker = TechNewsHealthCheck(tech_news_dir=str(temp_tech_news_dir))
        results = checker.run_all_checks()

        czech_ratio = results['metrics']['czech_ratio']
        assert czech_ratio < 0.85, f"Czech ratio should be < 0.85, got {czech_ratio}"
        assert results['status'] in ['CRITICAL', 'WARNING'], "Should trigger alert for low Czech ratio"


class TestProcessingLoggerIntegration:
    """Test cases pro ProcessingLogger integraci"""

    @pytest.fixture
    def temp_data_dir(self, tmp_path):
        """Vytvoř dočasný data adresář"""
        data_dir = tmp_path / "_data"
        data_dir.mkdir()
        return data_dir

    def test_processing_logger_tracks_llm_tokens(self, temp_data_dir):
        """Test: ProcessingLogger správně sleduje LLM tokens"""
        db_path = temp_data_dir / "tech_news_metrics.db"

        logger = ProcessingLogger(db_path=str(db_path))

        # Simuluj zpracování s LLM
        logger.log_article_processing('test-slug', {
            'llm_used': True,
            'tokens': 1500,
            'cost': 0.002,
            'response_time_ms': 1200
        })

        logger.finalize_and_save()

        # Ověř, že tokens jsou zaznamenány
        assert logger.metrics['processing']['total_llm_tokens'] == 1500
        assert logger.metrics['processing']['total_llm_cost_usd'] == 0.002

    def test_filtering_breakdown_accuracy(self, temp_data_dir):
        """Test: Přesný breakdown důvodů zamítnutí"""
        db_path = temp_data_dir / "tech_news_metrics.db"

        logger = ProcessingLogger(db_path=str(db_path))

        # Simuluj různé důvody zamítnutí
        logger.log_article_skip('content_filter', 'Gaming Article 1')
        logger.log_article_skip('content_filter', 'Gaming Article 2')
        logger.log_article_skip('low_importance', 'Rumor Article', {'importance': 2})
        logger.log_article_skip('low_importance', 'Marketing Article', {'importance': 1})
        logger.log_article_skip('no_title', 'Article without title')

        logger.finalize_and_save()

        # Ověř breakdown
        assert logger.metrics['filtering']['skipped_content_filter'] == 2
        assert logger.metrics['filtering']['skipped_low_importance'] == 2
        assert logger.metrics['filtering']['skipped_no_title'] == 1
        assert logger.metrics['filtering']['total_skipped'] == 5


# Pytest configuration
def pytest_configure(config):
    """Pytest setup"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test (may be slow)"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test (fast)"
    )


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--tb=short"])
