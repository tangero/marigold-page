#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import logging
from dotenv import load_dotenv
import yaml

# Načíst .env soubor
load_dotenv()

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ClickyTechNewsAnalyzer:
    """Analyzátor Clicky dat pro tech-news optimalizaci"""

    def __init__(self):
        """Inicializace s Clicky credentials"""
        self.site_id = os.environ.get('CLICKY_SITE_ID', '101451859')  # Z analytics.html
        self.sitekey = os.environ.get('CLICKY_SITEKEY')

        if not self.sitekey:
            logger.warning("⚠️ CLICKY_SITEKEY není nastaven v .env")

        self.reports_dir = Path('_data/tech_news_analytics')
        self.reports_dir.mkdir(exist_ok=True)

    def get_clicky_data(self, data_type='actions', date_range='last-7-days', limit=100):
        """Získá data z Clicky Analytics API"""
        if not self.sitekey:
            logger.error("❌ Chybí CLICKY_SITEKEY pro API přístup")
            return None

        url = "https://api.clicky.com/api/stats/4"
        params = {
            'site_id': self.site_id,
            'sitekey': self.sitekey,
            'type': data_type,
            'date': date_range,
            'limit': limit,
            'output': 'json'
        }

        try:
            logger.info(f"🔄 Stahuji {data_type} data z Clicky API...")
            response = requests.get(url, params=params, timeout=30)

            if not response.ok:
                logger.error(f"❌ Clicky API chyba {response.status_code}: {response.text}")
                return None

            data = response.json()
            logger.info(f"✅ Staženo {len(data[0]['dates'][0]['items'])} záznamů")
            return data

        except Exception as e:
            logger.error(f"❌ Chyba při stahování z Clicky API: {e}")
            return None

    def analyze_tech_news_clicks(self, days=7):
        """Analyzuje kliknutí na tech-news články"""
        logger.info(f"📊 Analyzuji tech-news kliknutí za posledních {days} dní")

        # Získat actions data
        actions_data = self.get_clicky_data('actions', f'last-{days}-days')
        if not actions_data:
            return None

        tech_news_actions = []

        # Filtrovat pouze tech-news akce
        for item in actions_data[0]['dates'][0]['items']:
            action_url = item.get('value', '')
            action_title = item.get('title', '')

            if '#tech-news' in action_url:
                tech_news_actions.append({
                    'url': action_url,
                    'title': action_title,
                    'clicks': int(item.get('value_percent', 0)),
                    'unique_clicks': int(item.get('value_percent', 0)),  # Clicky aggreguje
                    'category': self.extract_category(action_url),
                    'importance': self.extract_importance(action_url),
                    'position': self.extract_position(action_url),
                    'action_type': self.extract_action_type(action_url)
                })

        # Seřadit podle kliknutí
        tech_news_actions.sort(key=lambda x: x['clicks'], reverse=True)

        logger.info(f"📈 Nalezeno {len(tech_news_actions)} tech-news akcí")
        return tech_news_actions

    def extract_category(self, action_url):
        """Extrahuje kategorii z action URL"""
        if '#tech-news-click/' in action_url:
            parts = action_url.split('#tech-news-click/')[1].split('/')
            return parts[0] if parts else 'unknown'
        elif '#tech-news-detail/' in action_url:
            parts = action_url.split('#tech-news-detail/')[1].split('/')
            return parts[0] if parts else 'unknown'
        return 'unknown'

    def extract_importance(self, action_url):
        """Extrahuje důležitost z action URL"""
        if '#tech-news-click/' in action_url:
            parts = action_url.split('#tech-news-click/')[1].split('/')
            return int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
        elif '#tech-news-detail/' in action_url:
            parts = action_url.split('#tech-news-detail/')[1].split('/')
            return int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
        return 0

    def extract_position(self, action_url):
        """Extrahuje pozici článku z action URL"""
        if '#tech-news-detail/' in action_url:
            parts = action_url.split('#tech-news-detail/')[1].split('/')
            return int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
        return 0

    def extract_action_type(self, action_url):
        """Určí typ akce"""
        if '#tech-news-click/' in action_url:
            return 'article_click'
        elif '#tech-news-detail/' in action_url:
            return 'detailed_click'
        elif '#tech-news-filter/' in action_url:
            return 'filter_use'
        return 'other'

    def analyze_category_performance(self, actions):
        """Analyzuje výkonnost jednotlivých kategorií"""
        category_stats = {}

        for action in actions:
            if action['action_type'] == 'article_click':
                category = action['category']
                if category not in category_stats:
                    category_stats[category] = {
                        'total_clicks': 0,
                        'articles_count': 0,
                        'avg_importance': 0,
                        'importance_sum': 0
                    }

                category_stats[category]['total_clicks'] += action['clicks']
                category_stats[category]['articles_count'] += 1
                category_stats[category]['importance_sum'] += action['importance']

        # Vypočítat průměry
        for category, stats in category_stats.items():
            if stats['articles_count'] > 0:
                stats['avg_clicks_per_article'] = stats['total_clicks'] / stats['articles_count']
                stats['avg_importance'] = stats['importance_sum'] / stats['articles_count']
            else:
                stats['avg_clicks_per_article'] = 0
                stats['avg_importance'] = 0

        return category_stats

    def analyze_importance_correlation(self, actions):
        """Analyzuje korelaci mezi AI důležitostí a skutečnými kliknutími"""
        importance_stats = {}

        for action in actions:
            if action['action_type'] == 'article_click':
                importance = action['importance']
                if importance not in importance_stats:
                    importance_stats[importance] = {
                        'total_clicks': 0,
                        'articles_count': 0
                    }

                importance_stats[importance]['total_clicks'] += action['clicks']
                importance_stats[importance]['articles_count'] += 1

        # Vypočítat průměry
        for importance, stats in importance_stats.items():
            if stats['articles_count'] > 0:
                stats['avg_clicks_per_article'] = stats['total_clicks'] / stats['articles_count']

        return importance_stats

    def analyze_position_effect(self, actions):
        """Analyzuje vliv pozice článku na kliknutí"""
        position_stats = {}

        for action in actions:
            if action['action_type'] == 'detailed_click' and action['position'] > 0:
                position = action['position']
                if position not in position_stats:
                    position_stats[position] = {
                        'total_clicks': 0,
                        'articles_count': 0
                    }

                position_stats[position]['total_clicks'] += action['clicks']
                position_stats[position]['articles_count'] += 1

        return position_stats

    def get_goals_data(self, days=7):
        """Získá data o dosažených goals"""
        goals_data = self.get_clicky_data('goals', f'last-{days}-days')
        if not goals_data:
            return {}

        goals_stats = {}
        for item in goals_data[0]['dates'][0]['items']:
            goal_name = item.get('title', '')
            goals_stats[goal_name] = {
                'conversions': int(item.get('value_percent', 0)),
                'unique_conversions': int(item.get('value_percent', 0))
            }

        return goals_stats

    def generate_optimization_report(self, days=7):
        """Vygeneruje kompletní optimalizační report"""
        logger.info(f"📋 Generuji optimalizační report za {days} dní")

        # Získat všechna data
        actions = self.analyze_tech_news_clicks(days)
        if not actions:
            logger.error("❌ Nelze získat data pro report")
            return None

        category_performance = self.analyze_category_performance(actions)
        importance_correlation = self.analyze_importance_correlation(actions)
        position_effect = self.analyze_position_effect(actions)
        goals_data = self.get_goals_data(days)

        # Sestavit report
        report = {
            'generated_at': datetime.now().isoformat(),
            'period_days': days,
            'summary': {
                'total_tech_news_actions': len(actions),
                'total_clicks': sum(action['clicks'] for action in actions),
                'unique_articles_clicked': len(set(action['url'] for action in actions))
            },
            'top_articles': actions[:10],
            'category_performance': category_performance,
            'importance_correlation': importance_correlation,
            'position_effect': position_effect,
            'goals_achieved': goals_data,
            'recommendations': self.generate_recommendations(
                category_performance, importance_correlation, position_effect
            )
        }

        # Uložit report
        report_file = self.reports_dir / f"tech_news_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        logger.info(f"✅ Report uložen: {report_file}")
        return report

    def generate_recommendations(self, category_perf, importance_corr, position_effect):
        """Generuje doporučení pro optimalizaci"""
        recommendations = []

        # Kategorie doporučení
        if category_perf:
            best_category = max(category_perf.items(),
                              key=lambda x: x[1]['avg_clicks_per_article'])
            worst_category = min(category_perf.items(),
                               key=lambda x: x[1]['avg_clicks_per_article'])

            recommendations.append({
                'type': 'category_optimization',
                'message': f"Kategorie '{best_category[0]}' má nejvyšší CTR ({best_category[1]['avg_clicks_per_article']:.1f}). Zvažte více článků z této kategorie.",
                'priority': 'high'
            })

            if worst_category[1]['avg_clicks_per_article'] < 1.0:
                recommendations.append({
                    'type': 'category_optimization',
                    'message': f"Kategorie '{worst_category[0]}' má nízký CTR ({worst_category[1]['avg_clicks_per_article']:.1f}). Zvažte úpravu algoritmu důležitosti.",
                    'priority': 'medium'
                })

        # Důležitost doporučení
        if importance_corr:
            for importance, stats in importance_corr.items():
                if importance >= 4 and stats['avg_clicks_per_article'] < 2.0:
                    recommendations.append({
                        'type': 'importance_calibration',
                        'message': f"Články s důležitostí {importance} mají nižší CTR než očekáváno. Algoritmus možná předhodnocuje.",
                        'priority': 'medium'
                    })

        return recommendations

    def print_summary(self, report):
        """Vytiskne přehled reportu"""
        if not report:
            return

        print("\n" + "="*60)
        print("📊 TECH-NEWS ANALYTICS REPORT")
        print("="*60)
        print(f"📅 Období: {report['period_days']} dní")
        print(f"🔢 Celkem akcí: {report['summary']['total_tech_news_actions']}")
        print(f"👆 Celkem kliknutí: {report['summary']['total_clicks']}")
        print(f"📰 Unikátních článků: {report['summary']['unique_articles_clicked']}")

        print("\n🏆 TOP 5 ČLÁNKŮ:")
        for i, article in enumerate(report['top_articles'][:5], 1):
            print(f"{i}. {article['title'][:50]}... ({article['clicks']} kliknutí)")

        print("\n📊 KATEGORIE PERFORMANCE:")
        for category, stats in report['category_performance'].items():
            print(f"• {category}: {stats['avg_clicks_per_article']:.1f} avg clicks/článek")

        if report['recommendations']:
            print("\n💡 DOPORUČENÍ:")
            for rec in report['recommendations']:
                print(f"• {rec['message']}")

def main():
    """Hlavní funkce"""
    analyzer = ClickyTechNewsAnalyzer()

    # Vygenerovat týdenní report
    report = analyzer.generate_optimization_report(days=7)

    if report:
        analyzer.print_summary(report)
    else:
        logger.error("❌ Nepodařilo se vygenerovat report")

if __name__ == "__main__":
    main()