#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dashboard Data Generator pro Tech News
=======================================
Generuje agregovaná data z processing logů pro dashboard zobrazení
"""

import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DashboardDataGenerator:
    """Generuje dashboard data z processing logů"""

    def __init__(self, db_path: str = '_data/tech_news_metrics.db'):
        self.db_path = Path(db_path)
        if not self.db_path.exists():
            logger.warning(f"⚠️ Databáze neexistuje: {db_path}")
            self.conn = None
        else:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row

    def generate_dashboard_data(self, days: int = 30) -> Dict:
        """Generuje kompletní dashboard data za posledních N dní"""

        if not self.conn:
            logger.error("❌ Databáze není dostupná")
            return self._empty_dashboard()

        logger.info(f"📊 Generuji dashboard data za posledních {days} dní...")

        # Získat data
        daily_stats = self._get_daily_statistics(days)
        current_status = self._get_current_status()
        aggregates = self._calculate_aggregates(daily_stats)
        performance = self._get_performance_metrics(days)

        dashboard = {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'period_days': days,
            'current_status': current_status,
            'daily_series': daily_stats,
            'aggregates': aggregates,
            'performance_metrics': performance
        }

        logger.info("✅ Dashboard data vygenerována")
        return dashboard

    def _get_daily_statistics(self, days: int) -> List[Dict]:
        """Získá denní statistiky za posledních N dní"""

        cursor = self.conn.cursor()

        # Získat data ze sessions
        cursor.execute('''
            SELECT
                DATE(timestamp) as date,
                COUNT(*) as sessions_count,
                SUM(articles_fetched) as total_fetched,
                SUM(articles_processed) as total_processed,
                SUM(articles_saved) as total_saved,
                SUM(articles_skipped) as total_skipped,
                SUM(total_llm_cost_usd) as total_cost,
                AVG(total_duration_seconds) as avg_duration,
                CAST(SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) as success_rate
            FROM processing_sessions
            WHERE timestamp >= datetime('now', '-' || ? || ' days')
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
        ''', (days,))

        rows = cursor.fetchall()

        daily_stats = []
        for row in rows:
            # Parse skip reasons from individual sessions
            skip_reasons = self._get_skip_reasons_for_day(row['date'])

            daily_stats.append({
                'date': row['date'],
                'sessions_count': row['sessions_count'],
                'articles_fetched': row['total_fetched'] or 0,
                'articles_processed': row['total_processed'] or 0,
                'articles_saved': row['total_saved'] or 0,
                'articles_skipped': row['total_skipped'] or 0,
                'skip_reasons': skip_reasons,
                'llm_cost': round(row['total_cost'] or 0.0, 4),
                'avg_duration': round(row['avg_duration'] or 0.0, 2),
                'success_rate': round(row['success_rate'] or 0.0, 2)
            })

        return daily_stats

    def _get_skip_reasons_for_day(self, date: str) -> Dict[str, int]:
        """Získá důvody přeskočení pro daný den"""

        cursor = self.conn.cursor()

        cursor.execute('''
            SELECT skip_reasons_json
            FROM processing_sessions
            WHERE DATE(timestamp) = ?
            AND skip_reasons_json IS NOT NULL
        ''', (date,))

        rows = cursor.fetchall()

        # Agreguj důvody
        reasons_total = defaultdict(int)
        for row in rows:
            try:
                reasons = json.loads(row['skip_reasons_json'])
                for reason, count in reasons.items():
                    if reason.startswith('skipped_'):
                        reason_name = reason.replace('skipped_', '')
                        reasons_total[reason_name] += count
            except json.JSONDecodeError:
                continue

        return dict(reasons_total)

    def _get_current_status(self) -> Dict:
        """Získá aktuální status z posledního runu"""

        cursor = self.conn.cursor()

        # Poslední session
        cursor.execute('''
            SELECT *
            FROM processing_sessions
            ORDER BY timestamp DESC
            LIMIT 1
        ''')

        row = cursor.fetchone()

        if not row:
            return {
                'health': 'UNKNOWN',
                'last_run': None,
                'last_run_status': 'unknown',
                'articles_today': 0,
                'active_alerts': []
            }

        # Spočítat články dnes
        cursor.execute('''
            SELECT SUM(articles_saved) as total
            FROM processing_sessions
            WHERE DATE(timestamp) = DATE('now')
        ''')

        today_row = cursor.fetchone()
        articles_today = today_row['total'] or 0

        # Určit health status
        health = 'OK'
        alerts = []

        if row['status'] != 'success':
            health = 'WARNING'
            alerts.append('Poslední run selhal')

        if articles_today < 10:
            health = 'WARNING' if health == 'OK' else 'CRITICAL'
            alerts.append(f'Málo článků dnes: {articles_today}')

        return {
            'health': health,
            'last_run': row['timestamp'],
            'last_run_status': row['status'],
            'articles_today': articles_today,
            'active_alerts': alerts
        }

    def _calculate_aggregates(self, daily_stats: List[Dict]) -> Dict:
        """Vypočítá agregované metriky"""

        if not daily_stats:
            return {
                'total_articles': 0,
                'total_cost': 0.0,
                'avg_daily_articles': 0,
                'most_common_skip_reason': None
            }

        total_articles = sum(day['articles_saved'] for day in daily_stats)
        total_cost = sum(day['llm_cost'] for day in daily_stats)
        avg_daily = total_articles / len(daily_stats) if daily_stats else 0

        # Nejčastější důvod skip
        all_skip_reasons = defaultdict(int)
        for day in daily_stats:
            for reason, count in day['skip_reasons'].items():
                all_skip_reasons[reason] += count

        most_common = None
        if all_skip_reasons:
            most_common = max(all_skip_reasons.items(), key=lambda x: x[1])
            most_common = {'reason': most_common[0], 'count': most_common[1]}

        return {
            'total_articles': total_articles,
            'total_cost': round(total_cost, 2),
            'avg_daily_articles': round(avg_daily, 1),
            'most_common_skip_reason': most_common,
            'total_sessions': sum(day['sessions_count'] for day in daily_stats),
            'total_fetched': sum(day['articles_fetched'] for day in daily_stats),
            'total_skipped': sum(day['articles_skipped'] for day in daily_stats)
        }

    def _get_performance_metrics(self, days: int) -> Dict:
        """Získá performance metriky"""

        cursor = self.conn.cursor()

        cursor.execute('''
            SELECT
                AVG(total_duration_seconds) as avg_duration,
                AVG(api_response_time_ms) as avg_api_response,
                AVG(CAST(total_llm_tokens AS FLOAT) / NULLIF(articles_llm_processed, 0)) as avg_tokens_per_article,
                CAST(SUM(error_count) AS FLOAT) / SUM(articles_processed) as error_rate
            FROM processing_sessions
            WHERE timestamp >= datetime('now', '-' || ? || ' days')
            AND articles_processed > 0
        ''', (days,))

        row = cursor.fetchone()

        if not row:
            return {}

        return {
            'avg_session_duration': round(row['avg_duration'] or 0.0, 2),
            'avg_api_response_time': round(row['avg_api_response'] or 0.0, 0),
            'avg_tokens_per_article': round(row['avg_tokens_per_article'] or 0.0, 0),
            'error_rate': round(row['error_rate'] or 0.0, 4)
        }

    def _empty_dashboard(self) -> Dict:
        """Vrátí prázdný dashboard"""
        return {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'period_days': 30,
            'current_status': {
                'health': 'UNKNOWN',
                'last_run': None,
                'last_run_status': 'unknown',
                'articles_today': 0,
                'active_alerts': ['Databáze není dostupná']
            },
            'daily_series': [],
            'aggregates': {},
            'performance_metrics': {}
        }

    def save_dashboard_data(self, output_path: str = '_data/tech_news_dashboard.json'):
        """Uloží dashboard data do JSON souboru"""

        dashboard = self.generate_dashboard_data()

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with output_file.open('w', encoding='utf-8') as f:
            json.dump(dashboard, f, ensure_ascii=False, indent=2)

        logger.info(f"💾 Dashboard data uložena do: {output_file}")

        return dashboard

    def close(self):
        """Zavře databázové spojení"""
        if self.conn:
            self.conn.close()


def main():
    """Hlavní funkce"""
    import argparse

    parser = argparse.ArgumentParser(description='Dashboard Data Generator')
    parser.add_argument(
        '--days',
        type=int,
        default=30,
        help='Počet dní historie (default: 30)'
    )
    parser.add_argument(
        '--output',
        default='_data/tech_news_dashboard.json',
        help='Výstupní JSON soubor'
    )
    parser.add_argument(
        '--db-path',
        default='_data/tech_news_metrics.db',
        help='Cesta k SQLite databázi'
    )

    args = parser.parse_args()

    generator = DashboardDataGenerator(args.db_path)
    dashboard = generator.save_dashboard_data(args.output)
    generator.close()

    # Výpis summary
    print("\n" + "="*60)
    print("📊 DASHBOARD DATA GENERATED")
    print("="*60)
    print(f"\nPeriod: {dashboard['period_days']} days")
    print(f"Status: {dashboard['current_status']['health']}")
    print(f"Total articles: {dashboard['aggregates'].get('total_articles', 0)}")
    print(f"Total cost: ${dashboard['aggregates'].get('total_cost', 0):.2f}")
    print(f"Daily average: {dashboard['aggregates'].get('avg_daily_articles', 0)} articles")
    print(f"\nSaved to: {args.output}\n")


if __name__ == '__main__':
    main()
