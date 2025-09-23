#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import yaml
from pathlib import Path
import logging
from datetime import datetime
from analyze_tech_news_clicky import ClickyTechNewsAnalyzer

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TechNewsOptimizer:
    """Optimalizuje tech-news algoritmus na základě Clicky analytics"""

    def __init__(self):
        self.analyzer = ClickyTechNewsAnalyzer()
        self.config_file = Path('_data/tech_news_sources.yaml')
        self.optimization_history = Path('_data/tech_news_analytics/optimization_history.json')

    def load_current_config(self):
        """Načte současnou konfiguraci tech-news"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"❌ Chyba při načítání konfigurace: {e}")
            return None

    def save_config(self, config):
        """Uloží aktualizovanou konfiguraci"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(config, f, default_flow_style=False, allow_unicode=True, indent=2)
            logger.info("✅ Konfigurace uložena")
            return True
        except Exception as e:
            logger.error(f"❌ Chyba při ukládání konfigurace: {e}")
            return False

    def optimize_source_priorities(self, analytics_report, config):
        """Optimalizuje priority zdrojů na základě engagement"""
        if not analytics_report or 'top_articles' not in analytics_report:
            return config

        # Analyzovat výkonnost podle zdrojů
        source_performance = {}
        for article in analytics_report['top_articles']:
            title = article['title']
            clicks = article['clicks']

            # Extrahovat zdroj z titulku (formát: "Source: Title")
            if ':' in title:
                source = title.split(':')[0].strip()
                if source not in source_performance:
                    source_performance[source] = {'total_clicks': 0, 'article_count': 0}
                source_performance[source]['total_clicks'] += clicks
                source_performance[source]['article_count'] += 1

        # Vypočítat průměrné kliknutí na zdroj
        for source, stats in source_performance.items():
            if stats['article_count'] > 0:
                stats['avg_clicks'] = stats['total_clicks'] / stats['article_count']

        # Upravit priority v konfiguraci
        if source_performance and 'sources' in config:
            logger.info("🔧 Optimalizuji priority zdrojů...")

            best_sources = sorted(source_performance.items(),
                                key=lambda x: x[1]['avg_clicks'], reverse=True)

            for source_name, stats in best_sources[:3]:  # Top 3 zdroje
                # Najít odpovídající zdroj v konfiguraci
                for source_id, source_config in config['sources'].items():
                    if source_config['name'] == source_name:
                        old_priority = source_config.get('priority', 3)
                        new_priority = min(5, old_priority + 1)  # Zvýšit o 1, max 5
                        source_config['priority'] = new_priority
                        logger.info(f"  ⬆️ {source_name}: {old_priority} → {new_priority}")

        return config

    def optimize_category_focus(self, analytics_report, config):
        """Optimalizuje zaměření kategorií podle engagement"""
        if not analytics_report or 'category_performance' not in analytics_report:
            return config

        category_perf = analytics_report['category_performance']
        if not category_perf:
            return config

        logger.info("🎯 Optimalizuji zaměření kategorií...")

        # Najít nejlepší kategorie
        best_categories = sorted(category_perf.items(),
                               key=lambda x: x[1]['avg_clicks_per_article'], reverse=True)

        # Upravit max_articles pro nejlepší kategorie
        top_categories = [cat[0] for cat in best_categories[:3]]

        if 'sources' in config:
            for source_id, source_config in config['sources'].items():
                category_focus = source_config.get('category_focus', [])

                # Zvýšit max_articles pro zdroje s populárními kategoriemi
                if any(cat in top_categories for cat in category_focus):
                    old_max = source_config.get('max_articles', 5)
                    new_max = min(7, old_max + 1)  # Zvýšit o 1, max 7
                    source_config['max_articles'] = new_max
                    logger.info(f"  📈 {source_config['name']}: max_articles {old_max} → {new_max}")

        return config

    def optimize_filters(self, analytics_report, config):
        """Optimalizuje filtry na základě dat"""
        if not analytics_report:
            return config

        recommendations = analytics_report.get('recommendations', [])

        # Aplikovat doporučení na filtry
        if 'settings' not in config:
            config['settings'] = {}
        if 'filters' not in config['settings']:
            config['settings']['filters'] = {}

        for rec in recommendations:
            if rec['type'] == 'importance_calibration':
                # Upravit filtry pro lepší kalibraci důležitosti
                old_min_title = config['settings']['filters'].get('min_title_length', 10)
                new_min_title = max(15, old_min_title + 2)  # Zvýšit minimální délku
                config['settings']['filters']['min_title_length'] = new_min_title
                logger.info(f"  📝 min_title_length: {old_min_title} → {new_min_title}")

        return config

    def create_optimization_summary(self, old_config, new_config, analytics_report):
        """Vytvoří shrnutí provedených optimalizací"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'analytics_period': analytics_report.get('period_days', 7),
            'total_clicks_analyzed': analytics_report.get('summary', {}).get('total_clicks', 0),
            'changes_made': [],
            'recommendations_applied': []
        }

        # Porovnat konfigurace a najít změny
        if 'sources' in old_config and 'sources' in new_config:
            for source_id, old_source in old_config['sources'].items():
                new_source = new_config['sources'].get(source_id, {})

                # Priority změny
                old_priority = old_source.get('priority', 3)
                new_priority = new_source.get('priority', 3)
                if old_priority != new_priority:
                    summary['changes_made'].append({
                        'type': 'priority_change',
                        'source': old_source.get('name', source_id),
                        'old_value': old_priority,
                        'new_value': new_priority
                    })

                # Max articles změny
                old_max = old_source.get('max_articles', 5)
                new_max = new_source.get('max_articles', 5)
                if old_max != new_max:
                    summary['changes_made'].append({
                        'type': 'max_articles_change',
                        'source': old_source.get('name', source_id),
                        'old_value': old_max,
                        'new_value': new_max
                    })

        return summary

    def save_optimization_history(self, summary):
        """Uloží historii optimalizací"""
        history = []

        # Načíst existující historii
        if self.optimization_history.exists():
            try:
                with open(self.optimization_history, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            except Exception as e:
                logger.warning(f"⚠️ Nelze načíst historii optimalizací: {e}")

        # Přidat novou optimalizaci
        history.append(summary)

        # Omezit historii na posledních 50 záznamů
        history = history[-50:]

        # Uložit
        self.optimization_history.parent.mkdir(exist_ok=True)
        try:
            with open(self.optimization_history, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
            logger.info(f"📝 Historie optimalizací uložena: {len(history)} záznamů")
        except Exception as e:
            logger.error(f"❌ Chyba při ukládání historie: {e}")

    def run_optimization(self, days=7, dry_run=False):
        """Spustí kompletní optimalizaci"""
        logger.info("🚀 Spouští se automatická optimalizace tech-news")

        # Získat analytics report
        analytics_report = self.analyzer.generate_optimization_report(days)
        if not analytics_report:
            logger.error("❌ Nelze získat analytics data")
            return False

        # Načíst současnou konfiguraci
        config = self.load_current_config()
        if not config:
            logger.error("❌ Nelze načíst konfiguraci")
            return False

        old_config = config.copy()

        # Aplikovat optimalizace
        config = self.optimize_source_priorities(analytics_report, config)
        config = self.optimize_category_focus(analytics_report, config)
        config = self.optimize_filters(analytics_report, config)

        # Vytvořit shrnutí změn
        summary = self.create_optimization_summary(old_config, config, analytics_report)

        if not summary['changes_made']:
            logger.info("✅ Žádné změny nejsou potřeba")
            return True

        logger.info(f"📊 Navrženo {len(summary['changes_made'])} změn")

        if dry_run:
            logger.info("🔍 DRY RUN - změny se neuloží")
            for change in summary['changes_made']:
                logger.info(f"  • {change['type']}: {change.get('source', 'N/A')} "
                          f"{change['old_value']} → {change['new_value']}")
            return True

        # Uložit optimalizovanou konfiguraci
        if self.save_config(config):
            self.save_optimization_history(summary)
            logger.info("✅ Optimalizace dokončena")
            return True
        else:
            logger.error("❌ Optimalizace selhala")
            return False

def main():
    """Hlavní funkce"""
    import argparse

    parser = argparse.ArgumentParser(description='Optimalizace tech-news na základě Clicky analytics')
    parser.add_argument('--days', type=int, default=7, help='Počet dní pro analýzu (default: 7)')
    parser.add_argument('--dry-run', action='store_true', help='Pouze simulace bez uložení změn')

    args = parser.parse_args()

    optimizer = TechNewsOptimizer()
    success = optimizer.run_optimization(days=args.days, dry_run=args.dry_run)

    if success:
        logger.info("🎉 Optimalizace úspěšně dokončena")
    else:
        logger.error("💥 Optimalizace selhala")
        exit(1)

if __name__ == "__main__":
    main()