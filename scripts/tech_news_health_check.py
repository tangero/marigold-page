#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tech News Health Check System
==============================
Komplexní health monitoring pro tech-news generování na Marigold.cz

Kontroluje:
- Dostupnost a čerstvost článků
- Jazykovou kvalitu (detekce češtiny vs angličtiny)
- Front matter validitu
- Content quality metrics
- Generování trendy

Vytváří JSON report pro uptimerobot.com monitoring.
"""

import json
import yaml
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging
from collections import defaultdict
import statistics

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TechNewsHealthCheck:
    """Healthcheck systém pro tech-news monitoring"""

    # Jazykové znaky pro detekci češtiny
    CZECH_CHARS = set('áčďéěíňóřšťúůýž')
    CZECH_WORDS = {
        # Zájmena a spojky
        'který', 'která', 'které', 'když', 'kde', 'kam', 'odkud', 'jak', 'proč',
        'kdo', 'co', 'jaký', 'jaká', 'jakým', 'jež', 'jenž', 'což',

        # Časté příslovce a částice
        'také', 'více', 'pouze', 'především', 'totiž', 'však', 'přesto',
        'zatím', 'nyní', 'již', 'ještě', 'stále', 'ani', 'nebo', 'ale', 'proto',

        # Předložky
        'podle', 'během', 'pomocí', 'prostřednictvím', 'díky', 'oproti', 'místo',
        'kromě', 'kolem', 'okolo', 'mezi', 'přes', 'před', 'vedle', 'uvnitř',

        # Slovesa
        'může', 'měl', 'měla', 'mělo', 'byla', 'byly', 'byl', 'budou', 'bude',
        'jsou', 'jsem', 'mají', 'máme', 'mít', 'umožňuje', 'nabízí', 'představuje',

        # Přídavná jména
        'možné', 'další', 'nový', 'nová', 'nové', 'nových', 'hlavní', 'první',
        'druhý', 'třetí', 'velký', 'velká', 'malý', 'dobrý', 'špatný', 'lepší',

        # Podstatná jména
        'společnost', 'firma', 'uživatel', 'systém', 'funkce', 'aplikace',
        'služba', 'technologie', 'zařízení', 'produkt', 'článek', 'informace',

        # Příklady a vysvětlení
        'například', 'tedy', 'tzn', 'resp', 'apod', 'atd', 'mimo', 'včetně',

        # České tech termíny
        'počítač', 'software', 'databáze', 'síť', 'internet', 'webová', 'mobilní'
    }

    # Povinná pole ve front matter
    REQUIRED_FRONT_MATTER_FIELDS = [
        'title', 'description', 'category', 'publishedAt', 'url', 'layout'
    ]

    # Threshold hodnoty pro alerts
    THRESHOLDS = {
        'min_articles_24h': 10,  # Minimální počet článků za 24h
        'min_articles_1h': 1,    # Minimální počet článků za poslední hodinu
        'max_age_hours': 6,      # Maximální stáří nejnovějšího článku (hodiny)
        'min_czech_ratio': 0.85,  # Minimální poměr českých článků (85%)
        'min_avg_content_length': 300,  # Minimální průměrná délka obsahu
        'max_error_rate': 0.10,  # Maximální chybovost článků (10%)
    }

    def __init__(self, tech_news_dir: str = '_tech_news'):
        self.tech_news_dir = Path(tech_news_dir)
        self.now = datetime.now(timezone.utc)

        self.results = {
            'status': 'UNKNOWN',
            'timestamp': self.now.isoformat(),
            'checks': {},
            'metrics': {},
            'alerts': [],
            'summary': ''
        }

    def run_all_checks(self) -> Dict:
        """Spustí všechny health checks a vrátí kompletní report"""
        logger.info("🏥 Spouštím Tech News Health Check...")

        try:
            # Načíst všechny články
            articles = self._load_all_articles()

            if not articles:
                self._add_critical_alert("Nenalezeny žádné tech-news články!")
                self.results['status'] = 'CRITICAL'
                return self.results

            logger.info(f"📊 Načteno {len(articles)} článků")

            # Spustit jednotlivé kontroly
            self._check_article_freshness(articles)
            self._check_language_quality(articles)
            self._check_content_quality(articles)
            self._check_generation_trend(articles)
            self._check_front_matter_validity(articles)

            # Vypočítat celkový status
            self._calculate_overall_status()

            # Vygenerovat summary
            self._generate_summary()

            logger.info(f"✅ Health check dokončen: {self.results['status']}")

        except Exception as e:
            logger.error(f"❌ Chyba při health check: {e}")
            self._add_critical_alert(f"Systémová chyba: {str(e)}")
            self.results['status'] = 'CRITICAL'

        return self.results

    def _load_all_articles(self) -> List[Dict]:
        """Načte všechny tech-news články z filesystému"""
        articles = []

        if not self.tech_news_dir.exists():
            logger.error(f"❌ Adresář {self.tech_news_dir} neexistuje!")
            return articles

        for md_file in self.tech_news_dir.glob('*.md'):
            try:
                article_data = self._parse_article(md_file)
                if article_data:
                    articles.append(article_data)
            except Exception as e:
                logger.warning(f"⚠️ Chyba při parsování {md_file.name}: {e}")

        return sorted(articles, key=lambda x: x.get('published_dt', datetime.min), reverse=True)

    def _parse_article(self, file_path: Path) -> Optional[Dict]:
        """Parsuje jeden markdown článek včetně front matter"""
        content = file_path.read_text(encoding='utf-8')

        # Rozdělit front matter a obsah
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)

        if len(parts) < 3:
            logger.warning(f"⚠️ Neplatný formát: {file_path.name}")
            return None

        # Parsovat YAML front matter
        try:
            front_matter = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            logger.warning(f"⚠️ Chyba YAML v {file_path.name}: {e}")
            return None

        # Obsah článku (bez front matter)
        article_content = parts[2].strip()

        # Parsovat datum
        published_dt = self._parse_date(
            front_matter.get('publishedAt') or front_matter.get('date')
        )

        return {
            'file_name': file_path.name,
            'file_path': str(file_path),
            'front_matter': front_matter,
            'content': article_content,
            'published_dt': published_dt,
            'title': front_matter.get('title', ''),
            'description': front_matter.get('description', ''),
        }

    def _parse_date(self, date_str: Optional[str]) -> datetime:
        """Parsuje datum z různých formátů"""
        if not date_str:
            return datetime.min.replace(tzinfo=timezone.utc)

        try:
            # Zkusit ISO format
            if 'T' in str(date_str):
                dt = datetime.fromisoformat(str(date_str).replace('Z', '+00:00'))
            else:
                # Zkusit date-only format
                dt = datetime.strptime(str(date_str)[:10], '%Y-%m-%d')
                dt = dt.replace(tzinfo=timezone.utc)

            return dt
        except Exception as e:
            logger.debug(f"⚠️ Nelze parsovat datum '{date_str}': {e}")
            return datetime.min.replace(tzinfo=timezone.utc)

    def _check_article_freshness(self, articles: List[Dict]):
        """Kontrola čerstvosti článků"""
        logger.info("🕐 Kontroluji čerstvost článků...")

        # Nejnovější článek
        newest = articles[0] if articles else None
        newest_age_hours = None

        if newest and newest['published_dt'] != datetime.min.replace(tzinfo=timezone.utc):
            age = self.now - newest['published_dt']
            newest_age_hours = age.total_seconds() / 3600

        # Počet článků za poslední období
        articles_24h = sum(
            1 for a in articles
            if a['published_dt'] != datetime.min.replace(tzinfo=timezone.utc)
            and (self.now - a['published_dt']).total_seconds() / 3600 <= 24
        )

        articles_1h = sum(
            1 for a in articles
            if a['published_dt'] != datetime.min.replace(tzinfo=timezone.utc)
            and (self.now - a['published_dt']).total_seconds() / 3600 <= 1
        )

        # Metrics
        self.results['metrics']['total_articles'] = len(articles)
        self.results['metrics']['articles_24h'] = articles_24h
        self.results['metrics']['articles_1h'] = articles_1h
        self.results['metrics']['newest_article_age_hours'] = round(newest_age_hours, 2) if newest_age_hours else None

        # Checks
        self.results['checks']['freshness'] = {
            'status': 'OK',
            'newest_age_hours': round(newest_age_hours, 2) if newest_age_hours else None,
            'articles_24h': articles_24h,
            'articles_1h': articles_1h,
        }

        # Alerts
        if newest_age_hours and newest_age_hours > self.THRESHOLDS['max_age_hours']:
            self._add_warning_alert(
                f"Nejnovější článek je starý {newest_age_hours:.1f}h "
                f"(threshold: {self.THRESHOLDS['max_age_hours']}h)"
            )
            self.results['checks']['freshness']['status'] = 'WARNING'

        if articles_24h < self.THRESHOLDS['min_articles_24h']:
            self._add_warning_alert(
                f"Pouze {articles_24h} článků za 24h "
                f"(minimum: {self.THRESHOLDS['min_articles_24h']})"
            )
            self.results['checks']['freshness']['status'] = 'WARNING'

        if articles_1h < self.THRESHOLDS['min_articles_1h']:
            self._add_info_alert(f"Pouze {articles_1h} článků za poslední hodinu")

    def _check_language_quality(self, articles: List[Dict]):
        """Kontrola jazykové kvality - detekce češtiny vs angličtiny"""
        logger.info("🇨🇿 Kontroluji jazykovou kvalitu...")

        czech_count = 0
        english_count = 0
        english_articles = []

        for article in articles[:100]:  # Kontrolovat max 100 nejnovějších
            lang_score = self._detect_language(
                article['title'] + ' ' + article['description'] + ' ' + article['content'][:500]
            )

            if lang_score > 0.5:  # > 0.5 = čeština
                czech_count += 1
            else:
                english_count += 1
                english_articles.append({
                    'file': article['file_name'],
                    'title': article['title'][:50],
                    'score': round(lang_score, 2)
                })

        total = czech_count + english_count
        czech_ratio = czech_count / total if total > 0 else 0

        # Metrics
        self.results['metrics']['czech_articles'] = czech_count
        self.results['metrics']['english_articles'] = english_count
        self.results['metrics']['czech_ratio'] = round(czech_ratio, 3)

        # Checks
        self.results['checks']['language'] = {
            'status': 'OK',
            'czech_ratio': round(czech_ratio, 3),
            'sample_size': total,
            'english_articles_sample': english_articles[:5]  # Top 5 anglických
        }

        # Alerts
        if czech_ratio < self.THRESHOLDS['min_czech_ratio']:
            self._add_critical_alert(
                f"Pouze {czech_ratio*100:.1f}% článků v češtině! "
                f"(minimum: {self.THRESHOLDS['min_czech_ratio']*100}%)"
            )
            self.results['checks']['language']['status'] = 'CRITICAL'
        elif czech_ratio < 0.95:
            self._add_warning_alert(
                f"Nižší poměr českých článků: {czech_ratio*100:.1f}%"
            )
            self.results['checks']['language']['status'] = 'WARNING'

    def _detect_language(self, text: str) -> float:
        """
        Detekuje jazyk textu a vrátí skóre 0-1
        0 = angličtina, 1 = čeština, 0.5 = nelze rozhodnout

        ZLEPŠENÝ algoritmus: snížené thresholdy pro spolehlivější detekci
        """
        if not text:
            return 0.5

        text_lower = text.lower()

        # Počítat české znaky (háčky a čárky)
        czech_char_count = sum(1 for char in text_lower if char in self.CZECH_CHARS)

        # Pokud je hodně českých znaků, je to určitě čeština
        if czech_char_count >= 20:  # 20+ českých znaků = téměř jistě čeština
            return 1.0

        # Počítat české slova
        words = re.findall(r'\b\w+\b', text_lower)
        czech_word_count = sum(1 for word in words if word in self.CZECH_WORDS)

        # Pokud je hodně českých slov, je to čeština
        if czech_word_count >= 8:  # 8+ českých slov = téměř jistě čeština
            return 1.0

        # Kombinované skóre s nižšími thresholdy
        char_score = min(czech_char_count / 5, 1.0)  # SNÍŽENO: 5+ českých znaků = plný bod (dříve 10)
        word_score = min(czech_word_count / 3, 1.0)  # SNÍŽENO: 3+ českých slov = plný bod (dříve 5)

        # Vážený průměr (slova mají větší váhu, ale znaky také důležité)
        final_score = (char_score * 0.4 + word_score * 0.6)

        return final_score

    def _check_content_quality(self, articles: List[Dict]):
        """Kontrola kvality obsahu článků"""
        logger.info("📝 Kontroluji kvalitu obsahu...")

        content_lengths = []
        articles_with_images = 0
        articles_with_category = 0

        for article in articles[:100]:
            content_len = len(article['content'])
            content_lengths.append(content_len)

            if article['front_matter'].get('urlToImage'):
                articles_with_images += 1

            if article['front_matter'].get('category'):
                articles_with_category += 1

        avg_content_length = statistics.mean(content_lengths) if content_lengths else 0
        median_content_length = statistics.median(content_lengths) if content_lengths else 0

        # Metrics
        self.results['metrics']['avg_content_length'] = round(avg_content_length, 0)
        self.results['metrics']['median_content_length'] = round(median_content_length, 0)
        self.results['metrics']['articles_with_images_pct'] = round(
            (articles_with_images / len(articles[:100])) * 100, 1
        )
        self.results['metrics']['articles_with_category_pct'] = round(
            (articles_with_category / len(articles[:100])) * 100, 1
        )

        # Checks
        self.results['checks']['content_quality'] = {
            'status': 'OK',
            'avg_length': round(avg_content_length, 0),
            'median_length': round(median_content_length, 0),
        }

        # Alerts
        if avg_content_length < self.THRESHOLDS['min_avg_content_length']:
            self._add_warning_alert(
                f"Nízká průměrná délka obsahu: {avg_content_length:.0f} znaků "
                f"(minimum: {self.THRESHOLDS['min_avg_content_length']})"
            )
            self.results['checks']['content_quality']['status'] = 'WARNING'

    def _check_generation_trend(self, articles: List[Dict]):
        """Kontrola trendu generování článků v čase"""
        logger.info("📈 Analyzuji trend generování...")

        # Seskupit články po hodinách za poslední 24h
        hourly_counts = defaultdict(int)

        for article in articles:
            if article['published_dt'] == datetime.min.replace(tzinfo=timezone.utc):
                continue

            age_hours = (self.now - article['published_dt']).total_seconds() / 3600

            if age_hours <= 24:
                hour_bucket = int(age_hours)
                hourly_counts[hour_bucket] += 1

        # Vypočítat trend (simple linear regression)
        if len(hourly_counts) >= 3:
            hours = sorted(hourly_counts.keys())
            counts = [hourly_counts[h] for h in hours]

            # Trend: stoupající nebo klesající?
            recent_avg = statistics.mean(counts[:3]) if len(counts) >= 3 else 0
            older_avg = statistics.mean(counts[-3:]) if len(counts) >= 3 else 0

            trend = "stoupající" if recent_avg > older_avg else "klesající"
        else:
            trend = "nedostatek dat"

        self.results['checks']['generation_trend'] = {
            'status': 'OK',
            'trend': trend,
            'hourly_distribution': dict(sorted(hourly_counts.items())[:12])  # Posledních 12h
        }

    def _check_front_matter_validity(self, articles: List[Dict]):
        """Kontrola validity front matter ve všech článcích"""
        logger.info("🔍 Kontroluji validitu front matter...")

        invalid_count = 0
        missing_fields = defaultdict(int)
        invalid_articles = []

        for article in articles[:100]:
            fm = article['front_matter']
            article_errors = []

            for field in self.REQUIRED_FRONT_MATTER_FIELDS:
                if not fm.get(field):
                    missing_fields[field] += 1
                    article_errors.append(f"chybí {field}")

            if article_errors:
                invalid_count += 1
                invalid_articles.append({
                    'file': article['file_name'],
                    'errors': article_errors
                })

        total = min(len(articles), 100)
        error_rate = invalid_count / total if total > 0 else 0

        # Metrics
        self.results['metrics']['front_matter_error_rate'] = round(error_rate, 3)

        # Checks
        self.results['checks']['front_matter'] = {
            'status': 'OK',
            'error_rate': round(error_rate, 3),
            'invalid_count': invalid_count,
            'most_common_missing_fields': dict(
                sorted(missing_fields.items(), key=lambda x: x[1], reverse=True)[:5]
            ),
            'sample_invalid_articles': invalid_articles[:3]
        }

        # Alerts
        if error_rate > self.THRESHOLDS['max_error_rate']:
            self._add_warning_alert(
                f"Vysoká chybovost front matter: {error_rate*100:.1f}% "
                f"(maximum: {self.THRESHOLDS['max_error_rate']*100}%)"
            )
            self.results['checks']['front_matter']['status'] = 'WARNING'

    def _calculate_overall_status(self):
        """Vypočítá celkový health status na základě všech checks"""
        statuses = [check.get('status', 'OK') for check in self.results['checks'].values()]

        if 'CRITICAL' in statuses:
            self.results['status'] = 'CRITICAL'
        elif 'WARNING' in statuses:
            self.results['status'] = 'WARNING'
        else:
            self.results['status'] = 'OK'

    def _generate_summary(self):
        """Vygeneruje textový summary pro uptimerobot"""
        status = self.results['status']
        metrics = self.results['metrics']

        summary_parts = [
            f"Status: {status}",
            f"Články 24h: {metrics.get('articles_24h', 0)}",
            f"Čeština: {metrics.get('czech_ratio', 0)*100:.1f}%",
        ]

        if self.results['alerts']:
            summary_parts.append(f"Alerty: {len(self.results['alerts'])}")

        self.results['summary'] = " | ".join(summary_parts)

    def _add_critical_alert(self, message: str):
        """Přidá kritický alert"""
        self.results['alerts'].append({'level': 'CRITICAL', 'message': message})
        logger.error(f"🚨 CRITICAL: {message}")

    def _add_warning_alert(self, message: str):
        """Přidá varovný alert"""
        self.results['alerts'].append({'level': 'WARNING', 'message': message})
        logger.warning(f"⚠️ WARNING: {message}")

    def _add_info_alert(self, message: str):
        """Přidá informační alert"""
        self.results['alerts'].append({'level': 'INFO', 'message': message})
        logger.info(f"ℹ️ INFO: {message}")

    def save_results_to_json(self, output_path: str = '_data/tech_news_health.json'):
        """Uloží výsledky do JSON souboru"""
        output_file = Path(output_path)
        output_file.parent.mkdir(exist_ok=True)

        with output_file.open('w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)

        logger.info(f"💾 Health check report uložen do: {output_file}")


def main():
    """Hlavní funkce"""
    import argparse

    parser = argparse.ArgumentParser(description='Tech News Health Check')
    parser.add_argument(
        '--output',
        default='_data/tech_news_health.json',
        help='Výstupní JSON soubor (default: _data/tech_news_health.json)'
    )
    parser.add_argument(
        '--tech-news-dir',
        default='_tech_news',
        help='Adresář s tech-news články (default: _tech_news)'
    )

    args = parser.parse_args()

    # Spustit health check
    checker = TechNewsHealthCheck(tech_news_dir=args.tech_news_dir)
    results = checker.run_all_checks()

    # Uložit výsledky
    checker.save_results_to_json(args.output)

    # Vypsat summary do konzole
    print("\n" + "="*60)
    print(f"TECH NEWS HEALTH CHECK: {results['status']}")
    print("="*60)
    print(f"\n{results['summary']}\n")

    if results['alerts']:
        print("ALERTY:")
        for alert in results['alerts']:
            print(f"  [{alert['level']}] {alert['message']}")
        print()

    # Exit code podle statusu
    if results['status'] == 'CRITICAL':
        exit(2)
    elif results['status'] == 'WARNING':
        exit(1)
    else:
        exit(0)


if __name__ == '__main__':
    main()
