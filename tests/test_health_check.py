#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test suite pro Tech News Health Check systém

Testuje všechny aspekty health check funkcionality včetně:
- Detekce jazyka (čeština vs angličtina)
- Parsování článků a front matter
- Výpočet metrik
- Alert generování
- Edge cases a failure scenarios
"""

import unittest
import tempfile
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
import sys

# Přidat parent directory do path pro import
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from tech_news_health_check import TechNewsHealthCheck


class TestLanguageDetection(unittest.TestCase):
    """Testy pro detekci jazyka"""

    def setUp(self):
        self.checker = TechNewsHealthCheck()

    def test_detect_czech_text(self):
        """Test detekce českého textu"""
        czech_text = "Společnost Google představila novou funkci, která umožňuje lepší práci s daty."
        score = self.checker._detect_language(czech_text)
        self.assertGreater(score, 0.5, "České znaky a slova by měly dát skóre > 0.5")

    def test_detect_english_text(self):
        """Test detekce anglického textu"""
        english_text = "Google announces new feature that allows better data management."
        score = self.checker._detect_language(english_text)
        self.assertLess(score, 0.5, "Anglický text by měl dát skóre < 0.5")

    def test_detect_mixed_text(self):
        """Test detekce smíšeného textu"""
        mixed_text = "Google představuje new feature"
        score = self.checker._detect_language(mixed_text)
        # Smíšený text by měl být někde uprostřed
        self.assertGreater(score, 0.3)
        self.assertLess(score, 0.7)

    def test_detect_empty_text(self):
        """Test prázdného textu"""
        score = self.checker._detect_language("")
        self.assertEqual(score, 0.5, "Prázdný text by měl vrátit neutrální skóre 0.5")

    def test_detect_numbers_only(self):
        """Test textu obsahujícího pouze čísla"""
        numbers = "123 456 789 2025"
        score = self.checker._detect_language(numbers)
        # Mělo by vrátit nízké skóre (žádné české znaky/slova)
        self.assertLessEqual(score, 0.5)


class TestArticleParsing(unittest.TestCase):
    """Testy pro parsování článků"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.checker = TechNewsHealthCheck(tech_news_dir=self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_parse_valid_article(self):
        """Test parsování validního článku"""
        article_content = """---
title: Testovací článek
description: Popis článku
category: technologie
publishedAt: 2025-11-14T10:00:00+00:00
url: https://example.com
layout: tech_news_article
---

Toto je obsah článku v češtině.
"""
        article_file = Path(self.temp_dir) / "test-article.md"
        article_file.write_text(article_content, encoding='utf-8')

        article = self.checker._parse_article(article_file)

        self.assertIsNotNone(article)
        self.assertEqual(article['title'], 'Testovací článek')
        self.assertEqual(article['description'], 'Popis článku')
        self.assertIn('Toto je obsah článku', article['content'])

    def test_parse_article_missing_front_matter(self):
        """Test parsování článku bez front matter"""
        article_content = "Toto je článek bez front matter"

        article_file = Path(self.temp_dir) / "invalid-article.md"
        article_file.write_text(article_content, encoding='utf-8')

        article = self.checker._parse_article(article_file)

        self.assertIsNone(article, "Článek bez front matter by měl vrátit None")

    def test_parse_article_invalid_yaml(self):
        """Test parsování článku s neplatným YAML"""
        article_content = """---
title: Test
invalid: yaml: syntax: error
---

Content
"""
        article_file = Path(self.temp_dir) / "invalid-yaml.md"
        article_file.write_text(article_content, encoding='utf-8')

        article = self.checker._parse_article(article_file)

        self.assertIsNone(article, "Článek s neplatným YAML by měl vrátit None")

    def test_parse_date_formats(self):
        """Test parsování různých formátů data"""
        test_cases = [
            ("2025-11-14T10:00:00+00:00", True),  # ISO format s timezone
            ("2025-11-14", True),                 # Date only
            ("invalid-date", False),              # Neplatný formát
            (None, False),                        # None
        ]

        for date_str, should_parse in test_cases:
            dt = self.checker._parse_date(date_str)
            if should_parse:
                self.assertNotEqual(dt, datetime.min.replace(tzinfo=timezone.utc))
            else:
                self.assertEqual(dt, datetime.min.replace(tzinfo=timezone.utc))


class TestHealthChecks(unittest.TestCase):
    """Testy pro jednotlivé health checks"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.checker = TechNewsHealthCheck(tech_news_dir=self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def _create_test_article(self, filename, title, content, hours_ago=0, language='czech'):
        """Helper pro vytvoření testovacího článku"""
        if language == 'czech':
            content = f"Společnost Google představila {content}"
        else:
            content = f"Google announces {content}"

        publish_time = datetime.now(timezone.utc) - timedelta(hours=hours_ago)

        article_content = f"""---
title: {title}
description: Test description
category: technologie
publishedAt: {publish_time.isoformat()}
url: https://example.com/{filename}
layout: tech_news_article
---

{content}
"""
        article_file = Path(self.temp_dir) / filename
        article_file.write_text(article_content, encoding='utf-8')

    def test_freshness_check_ok(self):
        """Test freshness check s dostatečným počtem článků"""
        # Vytvořit 12 článků za posledních 24h
        for i in range(12):
            self._create_test_article(
                f"article-{i}.md",
                f"Článek {i}",
                "test content",
                hours_ago=i * 2
            )

        articles = self.checker._load_all_articles()
        self.checker._check_article_freshness(articles)

        self.assertEqual(self.checker.results['checks']['freshness']['status'], 'OK')
        self.assertGreaterEqual(self.checker.results['metrics']['articles_24h'], 10)

    def test_freshness_check_warning_old_articles(self):
        """Test freshness check s příliš starými články"""
        # Vytvořit články starší než threshold
        self._create_test_article(
            "old-article.md",
            "Starý článek",
            "test content",
            hours_ago=10  # Starší než default threshold 6h
        )

        articles = self.checker._load_all_articles()
        self.checker._check_article_freshness(articles)

        self.assertEqual(self.checker.results['checks']['freshness']['status'], 'WARNING')

    def test_language_check_all_czech(self):
        """Test language check s 100% českými články"""
        for i in range(10):
            self._create_test_article(
                f"czech-{i}.md",
                f"Český článek {i}",
                "novou funkci která pomáhá",
                language='czech'
            )

        articles = self.checker._load_all_articles()
        self.checker._check_language_quality(articles)

        self.assertEqual(self.checker.results['checks']['language']['status'], 'OK')
        self.assertGreaterEqual(self.checker.results['metrics']['czech_ratio'], 0.85)

    def test_language_check_too_much_english(self):
        """Test language check s příliš mnoha anglickými články"""
        # 7 anglických, 3 české = 30% češtiny
        for i in range(7):
            self._create_test_article(
                f"english-{i}.md",
                f"English article {i}",
                "new feature that helps",
                language='english'
            )

        for i in range(3):
            self._create_test_article(
                f"czech-{i}.md",
                f"Český článek {i}",
                "novou funkci která pomáhá",
                language='czech'
            )

        articles = self.checker._load_all_articles()
        self.checker._check_language_quality(articles)

        self.assertEqual(self.checker.results['checks']['language']['status'], 'CRITICAL')
        self.assertLess(self.checker.results['metrics']['czech_ratio'], 0.85)

    def test_content_quality_check(self):
        """Test content quality check"""
        # Vytvořit články s různou délkou obsahu
        self._create_test_article(
            "short.md",
            "Krátký článek",
            "x" * 200,  # 200 znaků
            language='czech'
        )
        self._create_test_article(
            "long.md",
            "Dlouhý článek",
            "x" * 1000,  # 1000 znaků
            language='czech'
        )

        articles = self.checker._load_all_articles()
        self.checker._check_content_quality(articles)

        self.assertIn('avg_content_length', self.checker.results['metrics'])
        self.assertGreater(self.checker.results['metrics']['avg_content_length'], 0)

    def test_front_matter_validity(self):
        """Test front matter validity check"""
        # Vytvořit článek s chybějícími povinnými poli
        article_content = """---
title: Test
# chybí description, category, atd.
---

Content
"""
        article_file = Path(self.temp_dir) / "incomplete.md"
        article_file.write_text(article_content, encoding='utf-8')

        articles = self.checker._load_all_articles()
        self.checker._check_front_matter_validity(articles)

        self.assertGreater(self.checker.results['metrics']['front_matter_error_rate'], 0)


class TestOverallStatus(unittest.TestCase):
    """Testy pro výpočet celkového statusu"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.checker = TechNewsHealthCheck(tech_news_dir=self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_status_ok_when_all_checks_pass(self):
        """Test že status je OK když všechny checks projdou"""
        self.checker.results['checks'] = {
            'freshness': {'status': 'OK'},
            'language': {'status': 'OK'},
            'content_quality': {'status': 'OK'},
        }

        self.checker._calculate_overall_status()

        self.assertEqual(self.checker.results['status'], 'OK')

    def test_status_warning_when_one_warning(self):
        """Test že status je WARNING když je jeden WARNING"""
        self.checker.results['checks'] = {
            'freshness': {'status': 'OK'},
            'language': {'status': 'WARNING'},
            'content_quality': {'status': 'OK'},
        }

        self.checker._calculate_overall_status()

        self.assertEqual(self.checker.results['status'], 'WARNING')

    def test_status_critical_overrides_warning(self):
        """Test že CRITICAL má přednost před WARNING"""
        self.checker.results['checks'] = {
            'freshness': {'status': 'WARNING'},
            'language': {'status': 'CRITICAL'},
            'content_quality': {'status': 'OK'},
        }

        self.checker._calculate_overall_status()

        self.assertEqual(self.checker.results['status'], 'CRITICAL')


class TestAlertGeneration(unittest.TestCase):
    """Testy pro generování alertů"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.checker = TechNewsHealthCheck(tech_news_dir=self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_add_critical_alert(self):
        """Test přidání kritického alertu"""
        self.checker._add_critical_alert("Test critical alert")

        self.assertEqual(len(self.checker.results['alerts']), 1)
        self.assertEqual(self.checker.results['alerts'][0]['level'], 'CRITICAL')
        self.assertEqual(self.checker.results['alerts'][0]['message'], 'Test critical alert')

    def test_add_multiple_alerts(self):
        """Test přidání více alertů"""
        self.checker._add_critical_alert("Critical 1")
        self.checker._add_warning_alert("Warning 1")
        self.checker._add_info_alert("Info 1")

        self.assertEqual(len(self.checker.results['alerts']), 3)

    def test_summary_generation(self):
        """Test generování summary"""
        self.checker.results['status'] = 'WARNING'
        self.checker.results['metrics'] = {
            'articles_24h': 15,
            'czech_ratio': 0.92,
        }
        self.checker.results['alerts'] = [
            {'level': 'WARNING', 'message': 'Test'}
        ]

        self.checker._generate_summary()

        self.assertIn('WARNING', self.checker.results['summary'])
        self.assertIn('15', self.checker.results['summary'])
        self.assertIn('92', self.checker.results['summary'])


class TestIntegration(unittest.TestCase):
    """Integration testy pro celý health check systém"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.checker = TechNewsHealthCheck(tech_news_dir=self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def _create_realistic_article(self, filename, hours_ago=0):
        """Vytvoří realistický článek podobný těm na produkci"""
        publish_time = datetime.now(timezone.utc) - timedelta(hours=hours_ago)

        article_content = f"""---
category: mobilní telefony
companies:
- Samsung
date: '{publish_time.isoformat()}'
description: Samsung plánuje prodat 36 milionů kusů řady Galaxy S26, což by představovalo
  nárůst oproti 22 milionům prodaných S25 v první polovině roku 2025.
importance: 2
layout: tech_news_article
original_title: Samsung expects the Galaxy S26 series to sell 35 million units
publishedAt: '{publish_time.isoformat()}'
slug: samsung-galaxy-s26-sales
source:
  emoji: 📰
  id: null
  name: 9to5google.com
title: Samsung očekává prodej 35 milionů kusů řady Galaxy S26 díky AI
url: http://9to5google.com/2025/11/04/samsung-galaxy-s26/
urlToImage: https://example.com/image.jpg
---

Samsung zveřejnil ambiciózní plány pro svou mobilní divizi na rok 2026, kde očekává prodej 36 milionů kusů nadcházející řady Galaxy S26. Celkově by společnost chtěla prodat 240 milionů smartphonů globálně.

V první polovině roku 2025 se Samsungu podařilo prodat 22 milionů kusů řady Galaxy S25, což firma považuje za překvapivě úspěšný výsledek. Pro řadu S26 tedy počítá s nárůstem o minimálně 2 miliony kusů.

Společnost úspěch přisuzuje zaměření na mobilní AI funkce, ačkoli skutečné důvody mohou být prozaičtější - probíhající upgrade cyklus starších zařízení.
"""
        article_file = Path(self.temp_dir) / filename
        article_file.write_text(article_content, encoding='utf-8')

    def test_full_health_check_healthy_system(self):
        """Test kompletního health check na zdravém systému"""
        # Vytvořit 15 realistických článků za posledních 24h
        for i in range(15):
            self._create_realistic_article(
                f"2025-11-14-article-{i}.md",
                hours_ago=i * 1.5
            )

        results = self.checker.run_all_checks()

        self.assertEqual(results['status'], 'OK')
        self.assertGreaterEqual(results['metrics']['articles_24h'], 10)
        self.assertGreaterEqual(results['metrics']['czech_ratio'], 0.85)
        self.assertLessEqual(results['metrics']['newest_article_age_hours'], 6)

    def test_save_results_to_json(self):
        """Test uložení výsledků do JSON"""
        self._create_realistic_article("test.md", hours_ago=1)
        self.checker.run_all_checks()

        output_file = Path(self.temp_dir) / "health.json"
        self.checker.save_results_to_json(str(output_file))

        self.assertTrue(output_file.exists())

        # Načíst a validovat JSON
        with output_file.open('r') as f:
            data = json.load(f)

        self.assertIn('status', data)
        self.assertIn('metrics', data)
        self.assertIn('checks', data)
        self.assertIn('alerts', data)


class TestEdgeCases(unittest.TestCase):
    """Testy pro edge cases a boundary conditions"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.checker = TechNewsHealthCheck(tech_news_dir=self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_empty_tech_news_directory(self):
        """Test s prázdným adresářem tech-news"""
        results = self.checker.run_all_checks()

        self.assertEqual(results['status'], 'CRITICAL')
        self.assertGreater(len(results['alerts']), 0)

    def test_nonexistent_directory(self):
        """Test s neexistujícím adresářem"""
        checker = TechNewsHealthCheck(tech_news_dir='/nonexistent/path')
        results = checker.run_all_checks()

        self.assertEqual(results['status'], 'CRITICAL')

    def test_very_large_content(self):
        """Test s velmi dlouhým obsahem článku"""
        article_content = f"""---
title: Test
description: Test desc
category: tech
publishedAt: 2025-11-14T10:00:00+00:00
url: https://example.com
layout: tech_news_article
---

{'x' * 100000}  # 100k znaků
"""
        article_file = Path(self.temp_dir) / "large.md"
        article_file.write_text(article_content, encoding='utf-8')

        articles = self.checker._load_all_articles()
        self.checker._check_content_quality(articles)

        # Mělo by projít bez chyby
        self.assertIn('avg_content_length', self.checker.results['metrics'])


def run_tests():
    """Spustí všechny testy"""
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_tests()
