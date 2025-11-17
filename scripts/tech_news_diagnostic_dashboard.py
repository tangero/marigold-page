#!/usr/bin/env python3
"""
Tech News Diagnostic Dashboard
===============================

Komplexní monitoring dashboard pro tech-news pipeline.
Zobrazuje:
- Důvody zamítnutí článků (breakdown)
- Sample zamítnutých článků s jejich skóre
- LLM cost metriky (daily/weekly)
- Freshness alerts
- Success rate trendy

Generuje HTML/JSON report pro zobrazení v health-status.
"""

import json
import sqlite3
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict
import statistics
import re


class TechNewsDiagnosticDashboard:
    """Generátor diagnostického dashboardu pro tech-news"""

    def __init__(
        self,
        metrics_db: str = '_data/tech_news_metrics.db',
        llm_costs_db: str = '_data/llm_costs.db',
        processing_logs_dir: str = '_data/processing_logs'
    ):
        self.metrics_db = Path(metrics_db)
        self.llm_costs_db = Path(llm_costs_db)
        self.processing_logs_dir = Path(processing_logs_dir)
        self.now = datetime.now(timezone.utc)

    def generate_full_report(self) -> Dict:
        """Vygeneruje kompletní diagnostický report"""
        report = {
            'timestamp': self.now.isoformat(),
            'version': '1.0',
            'sections': {
                'rejection_analysis': self._analyze_rejections(),
                'llm_costs': self._analyze_llm_costs(),
                'freshness_check': self._check_freshness(),
                'success_rate_trend': self._analyze_success_rate_trend(),
                'importance_distribution': self._analyze_importance_distribution(),
                'recommendations': []
            }
        }

        # Generuj doporučení na základě analýzy
        report['sections']['recommendations'] = self._generate_recommendations(report)

        return report

    def _analyze_rejections(self) -> Dict:
        """
        Analyzuje důvody zamítnutí článků za poslední 24h/7d

        Returns:
            {
                'last_24h': {
                    'total_rejected': int,
                    'breakdown': {'content_filter': X, 'low_importance': Y},
                    'samples': [...]
                },
                'last_7d': {...}
            }
        """
        analysis = {
            'last_24h': self._get_rejection_stats(hours=24),
            'last_7d': self._get_rejection_stats(days=7),
        }

        return analysis

    def _get_rejection_stats(self, hours: int = None, days: int = None) -> Dict:
        """Získá statistiky zamítnutí pro dané období"""
        stats = {
            'total_rejected': 0,
            'breakdown': defaultdict(int),
            'samples': []
        }

        # Načíst z processing logs
        cutoff_time = self.now
        if hours:
            cutoff_time = self.now - timedelta(hours=hours)
        elif days:
            cutoff_time = self.now - timedelta(days=days)

        # Projít processing logs
        for log_file in sorted(self.processing_logs_dir.glob('*.jsonl'), reverse=True):
            # Parse date from filename
            try:
                log_date = datetime.strptime(log_file.stem, '%Y-%m-%d').replace(tzinfo=timezone.utc)
                if log_date < cutoff_time.replace(hour=0, minute=0, second=0):
                    break
            except ValueError:
                continue

            # Read JSONL
            with log_file.open('r', encoding='utf-8') as f:
                for line in f:
                    try:
                        record = json.loads(line)

                        # Filter by timestamp
                        record_time = datetime.fromisoformat(record['timestamp'])
                        if record_time < cutoff_time:
                            continue

                        # Aggregate rejection data
                        filtering = record.get('filtering_metrics', {})
                        total_skipped = filtering.get('total_skipped', 0)
                        stats['total_rejected'] += total_skipped

                        # Breakdown by reason
                        for key, value in filtering.items():
                            if key.startswith('skipped_'):
                                reason = key.replace('skipped_', '')
                                stats['breakdown'][reason] += value

                        # Collect samples
                        skip_samples = record.get('skip_sample', [])
                        stats['samples'].extend(skip_samples[:5])

                    except (json.JSONDecodeError, KeyError) as e:
                        continue

        # Trim samples to max 20
        stats['samples'] = stats['samples'][:20]

        return stats

    def _analyze_llm_costs(self) -> Dict:
        """
        Analyzuje LLM náklady za různá období

        Returns:
            {
                'today': {'calls': X, 'tokens': Y, 'cost_usd': Z},
                'yesterday': {...},
                'last_7d': {...},
                'last_30d': {...},
                'by_operation': {...}
            }
        """
        if not self.llm_costs_db.exists():
            return {'error': 'LLM costs database not found'}

        conn = sqlite3.connect(self.llm_costs_db)
        conn.row_factory = sqlite3.Row

        analysis = {
            'today': self._get_llm_stats(conn, days=0),
            'yesterday': self._get_llm_stats(conn, days=1, single_day=True),
            'last_7d': self._get_llm_stats(conn, days=7),
            'last_30d': self._get_llm_stats(conn, days=30),
            'by_operation': self._get_llm_by_operation(conn, days=7)
        }

        conn.close()
        return analysis

    def _get_llm_stats(
        self,
        conn: sqlite3.Connection,
        days: int,
        single_day: bool = False
    ) -> Dict:
        """Získá LLM statistiky pro dané období"""
        cursor = conn.cursor()

        if single_day:
            # Specific day
            target_date = (datetime.now(timezone.utc) - timedelta(days=days)).date()
            cursor.execute("""
                SELECT
                    COUNT(*) as total_calls,
                    COALESCE(SUM(total_tokens), 0) as total_tokens,
                    COALESCE(SUM(estimated_cost_usd), 0) as total_cost_usd
                FROM api_calls
                WHERE date(timestamp) = ?
                AND status = 'success'
            """, (target_date.isoformat(),))
        else:
            # Range
            cursor.execute("""
                SELECT
                    COUNT(*) as total_calls,
                    COALESCE(SUM(total_tokens), 0) as total_tokens,
                    COALESCE(SUM(estimated_cost_usd), 0) as total_cost_usd
                FROM api_calls
                WHERE timestamp >= datetime('now', '-' || ? || ' days')
                AND status = 'success'
            """, (days,))

        row = cursor.fetchone()

        return {
            'total_calls': row['total_calls'],
            'total_tokens': row['total_tokens'],
            'total_cost_usd': round(row['total_cost_usd'], 4),
            'avg_cost_per_call': round(row['total_cost_usd'] / row['total_calls'], 6) if row['total_calls'] > 0 else 0
        }

    def _get_llm_by_operation(self, conn: sqlite3.Connection, days: int) -> Dict:
        """Získá breakdown LLM nákladů podle operace"""
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                operation,
                COUNT(*) as calls,
                COALESCE(SUM(total_tokens), 0) as tokens,
                COALESCE(SUM(estimated_cost_usd), 0) as cost_usd
            FROM api_calls
            WHERE timestamp >= datetime('now', '-' || ? || ' days')
            AND status = 'success'
            GROUP BY operation
            ORDER BY cost_usd DESC
        """, (days,))

        breakdown = {}
        for row in cursor.fetchall():
            breakdown[row['operation']] = {
                'calls': row['calls'],
                'tokens': row['tokens'],
                'cost_usd': round(row['cost_usd'], 4)
            }

        return breakdown

    def _check_freshness(self) -> Dict:
        """
        Kontroluje čerstvost článků z NewsAPI

        Returns:
            {
                'status': 'OK' | 'WARNING' | 'CRITICAL',
                'latest_article_age_hours': float,
                'articles_in_last_4h': int,
                'alert': str (if applicable)
            }
        """
        # Read from processing logs to see article ages
        freshness = {
            'status': 'OK',
            'latest_article_age_hours': None,
            'articles_in_last_4h': 0,
            'alert': None
        }

        # Check latest processing session
        latest_log = self._get_latest_processing_log()
        if not latest_log:
            freshness['status'] = 'CRITICAL'
            freshness['alert'] = 'No processing logs found'
            return freshness

        # Analyze article freshness from _tech_news directory
        tech_news_dir = Path('_tech_news')

        if not tech_news_dir.exists():
            freshness['status'] = 'CRITICAL'
            freshness['alert'] = 'Tech news directory not found'
            return freshness

        # Find newest article by file modification time (simpler than parsing YAML)
        newest_age = None
        articles_4h = 0

        for md_file in tech_news_dir.glob('*.md'):
            try:
                # Extract date from filename (format: YYYY-MM-DD-slug.md)
                filename = md_file.stem
                date_match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', filename)

                if date_match:
                    year, month, day = map(int, date_match.groups())
                    file_date = datetime(year, month, day, tzinfo=timezone.utc)
                    age_hours = (self.now - file_date).total_seconds() / 3600

                    if newest_age is None or age_hours < newest_age:
                        newest_age = age_hours

                    if age_hours <= 4:
                        articles_4h += 1

            except Exception as e:
                continue

        freshness['latest_article_age_hours'] = round(newest_age, 2) if newest_age else None
        freshness['articles_in_last_4h'] = articles_4h

        # Determine status
        if newest_age is None:
            freshness['status'] = 'CRITICAL'
            freshness['alert'] = 'No articles with valid publishedAt found'
        elif newest_age > 24:
            freshness['status'] = 'CRITICAL'
            freshness['alert'] = f'Latest article is {newest_age:.1f}h old (>24h)'
        elif newest_age > 6:
            freshness['status'] = 'WARNING'
            freshness['alert'] = f'Latest article is {newest_age:.1f}h old (>6h)'

        if articles_4h == 0:
            freshness['status'] = 'WARNING'
            if freshness['alert']:
                freshness['alert'] += '; No articles in last 4h'
            else:
                freshness['alert'] = 'No articles in last 4h'

        return freshness

    def _analyze_success_rate_trend(self) -> Dict:
        """
        Analyzuje trend úspěšnosti (saved/fetched ratio) v čase

        Returns:
            {
                'current_rate': float,
                'trend': 'improving' | 'stable' | 'declining',
                'history': [...]
            }
        """
        if not self.metrics_db.exists():
            return {'error': 'Metrics database not found'}

        conn = sqlite3.connect(self.metrics_db)
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                date(timestamp) as day,
                SUM(articles_fetched) as fetched,
                SUM(articles_saved) as saved
            FROM processing_sessions
            WHERE timestamp >= datetime('now', '-7 days')
            GROUP BY day
            ORDER BY day ASC
        """)

        history = []
        rates = []

        for row in cursor.fetchall():
            fetched = row['fetched']
            saved = row['saved']
            rate = (saved / fetched * 100) if fetched > 0 else 0

            history.append({
                'day': row['day'],
                'fetched': fetched,
                'saved': saved,
                'success_rate_pct': round(rate, 1)
            })
            rates.append(rate)

        conn.close()

        # Determine trend
        trend = 'stable'
        if len(rates) >= 3:
            recent_avg = statistics.mean(rates[-3:])
            older_avg = statistics.mean(rates[:3]) if len(rates) >= 6 else rates[0]

            if recent_avg > older_avg + 5:
                trend = 'improving'
            elif recent_avg < older_avg - 5:
                trend = 'declining'

        return {
            'current_rate': rates[-1] if rates else 0,
            'trend': trend,
            'history': history
        }

    def _analyze_importance_distribution(self) -> Dict:
        """
        Analyzuje distribuci importance skóre za poslední týden

        Returns:
            {
                'distribution': {1: X, 2: Y, 3: Z, 4: A, 5: B},
                'avg_importance': float,
                'most_common': int
            }
        """
        # Read from processing logs
        distribution = defaultdict(int)
        total = 0

        cutoff = self.now - timedelta(days=7)

        for log_file in sorted(self.processing_logs_dir.glob('*.jsonl'), reverse=True):
            try:
                log_date = datetime.strptime(log_file.stem, '%Y-%m-%d').replace(tzinfo=timezone.utc)
                if log_date < cutoff.replace(hour=0, minute=0, second=0):
                    break
            except ValueError:
                continue

            with log_file.open('r', encoding='utf-8') as f:
                for line in f:
                    try:
                        record = json.loads(line)
                        save_metrics = record.get('save_metrics', {})

                        for i in range(1, 6):
                            count = save_metrics.get(f'importance_{i}', 0)
                            distribution[i] += count
                            total += count

                    except (json.JSONDecodeError, KeyError):
                        continue

        # Calculate stats
        if total > 0:
            weighted_sum = sum(imp * count for imp, count in distribution.items())
            avg_importance = weighted_sum / total
            most_common = max(distribution.items(), key=lambda x: x[1])[0]
        else:
            avg_importance = 0
            most_common = None

        return {
            'distribution': dict(distribution),
            'total_articles': total,
            'avg_importance': round(avg_importance, 2),
            'most_common': most_common
        }

    def _get_latest_processing_log(self) -> Optional[Dict]:
        """Získá nejnovější processing log záznam"""
        latest_file = None
        latest_date = None

        for log_file in self.processing_logs_dir.glob('*.jsonl'):
            try:
                log_date = datetime.strptime(log_file.stem, '%Y-%m-%d').replace(tzinfo=timezone.utc)
                if latest_date is None or log_date > latest_date:
                    latest_date = log_date
                    latest_file = log_file
            except ValueError:
                continue

        if not latest_file:
            return None

        # Read last line (latest record)
        with latest_file.open('r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                try:
                    return json.loads(lines[-1])
                except json.JSONDecodeError:
                    return None

        return None

    def _generate_recommendations(self, report: Dict) -> List[Dict]:
        """Generuje doporučení na základě analýzy"""
        recommendations = []

        # Check success rate
        success_rate = report['sections']['success_rate_trend'].get('current_rate', 0)
        if success_rate < 20:
            recommendations.append({
                'severity': 'high',
                'category': 'filtering',
                'issue': f'Velmi nízká úspěšnost: {success_rate:.1f}%',
                'recommendation': 'Přehodnotit importance threshold (< 3) nebo content filters. '
                                 'Možná jsou příliš agresivní.',
                'action': 'Review filters in generate_tech_news_newsapi.py'
            })

        # Check freshness
        freshness = report['sections']['freshness_check']
        if freshness['status'] == 'CRITICAL':
            recommendations.append({
                'severity': 'critical',
                'category': 'freshness',
                'issue': freshness.get('alert', 'Articles not fresh'),
                'recommendation': 'Použít NewsAPI /v2/everything s parametrem "from" pro poslední 24h. '
                                 'Přidat "sortBy=publishedAt".',
                'action': 'Update fetch_newsapi_articles() to use /v2/everything with from parameter'
            })

        # Check LLM costs
        llm_costs = report['sections']['llm_costs']
        today_cost = llm_costs.get('today', {}).get('total_cost_usd', 0)
        if today_cost == 0 and llm_costs.get('today', {}).get('total_calls', 0) > 0:
            recommendations.append({
                'severity': 'high',
                'category': 'monitoring',
                'issue': 'LLM cost tracking nefunguje - $0 náklady při aktivních voláních',
                'recommendation': 'Ověřit, že track_llm_call() wrapper správně extrahuje usage data '
                                 'z OpenRouter response.',
                'action': 'Debug llm_cost_tracker.py and track_llm_call() function'
            })

        # Check rejection breakdown
        rejections_24h = report['sections']['rejection_analysis']['last_24h']
        total_rejected = rejections_24h.get('total_rejected', 0)
        content_filter = rejections_24h.get('breakdown', {}).get('content_filter', 0)

        if total_rejected > 0:
            content_filter_pct = (content_filter / total_rejected) * 100
            if content_filter_pct > 70:
                recommendations.append({
                    'severity': 'medium',
                    'category': 'filtering',
                    'issue': f'{content_filter_pct:.0f}% článků filtrováno jako hry/sport/zábava',
                    'recommendation': 'Zvážit použití jiného NewsAPI query (místo category=technology) '
                                     'nebo přidat více zdrojů.',
                    'action': 'Review NewsAPI sources or use /v2/everything with custom query'
                })

        return recommendations

    def save_report_json(self, output_path: str = '_data/tech_news_diagnostic.json'):
        """Uloží report jako JSON"""
        report = self.generate_full_report()

        output_file = Path(output_path)
        output_file.parent.mkdir(exist_ok=True)

        with output_file.open('w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        print(f"Diagnostic report saved to: {output_file}")

    def print_summary(self):
        """Vytiskne summary do konzole"""
        report = self.generate_full_report()

        print("\n" + "="*70)
        print("TECH NEWS DIAGNOSTIC DASHBOARD")
        print("="*70)

        # Freshness
        freshness = report['sections']['freshness_check']
        print(f"\n🕐 FRESHNESS: {freshness['status']}")
        print(f"  Latest article age: {freshness['latest_article_age_hours']}h")
        print(f"  Articles in last 4h: {freshness['articles_in_last_4h']}")
        if freshness['alert']:
            print(f"  ⚠️ Alert: {freshness['alert']}")

        # Success Rate
        success = report['sections']['success_rate_trend']
        print(f"\n📊 SUCCESS RATE: {success['current_rate']:.1f}% (trend: {success['trend']})")

        # Rejections
        rejections = report['sections']['rejection_analysis']['last_24h']
        print(f"\n⏭️ REJECTIONS (24h): {rejections['total_rejected']} total")
        for reason, count in rejections['breakdown'].items():
            pct = (count / rejections['total_rejected'] * 100) if rejections['total_rejected'] > 0 else 0
            print(f"  {reason}: {count} ({pct:.1f}%)")

        # Sample rejected
        if rejections['samples']:
            print(f"\n  Sample rejected articles:")
            for sample in rejections['samples'][:5]:
                print(f"    [{sample['reason']}] {sample['title'][:60]}...")

        # LLM Costs
        llm = report['sections']['llm_costs']
        print(f"\n💰 LLM COSTS:")
        print(f"  Today: ${llm['today']['total_cost_usd']:.4f} ({llm['today']['total_calls']} calls, {llm['today']['total_tokens']:,} tokens)")
        print(f"  Last 7d: ${llm['last_7d']['total_cost_usd']:.4f} ({llm['last_7d']['total_calls']} calls)")

        if llm.get('by_operation'):
            print(f"\n  By operation (7d):")
            for op, stats in sorted(llm['by_operation'].items(), key=lambda x: x[1]['cost_usd'], reverse=True):
                print(f"    {op}: ${stats['cost_usd']:.4f} ({stats['calls']} calls)")

        # Importance Distribution
        importance = report['sections']['importance_distribution']
        print(f"\n⭐ IMPORTANCE DISTRIBUTION (7d):")
        for i in range(5, 0, -1):
            count = importance['distribution'].get(i, 0)
            pct = (count / importance['total_articles'] * 100) if importance['total_articles'] > 0 else 0
            print(f"  {i}: {count} ({pct:.1f}%)")
        print(f"  Average: {importance['avg_importance']}")

        # Recommendations
        recs = report['sections']['recommendations']
        if recs:
            print(f"\n🔧 RECOMMENDATIONS: {len(recs)}")
            for rec in recs:
                print(f"\n  [{rec['severity'].upper()}] {rec['category']}")
                print(f"    Issue: {rec['issue']}")
                print(f"    Fix: {rec['recommendation']}")

        print("\n" + "="*70 + "\n")


def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description='Tech News Diagnostic Dashboard')
    parser.add_argument('--output', default='_data/tech_news_diagnostic.json',
                       help='Output JSON file')
    parser.add_argument('--summary-only', action='store_true',
                       help='Print summary to console only')

    args = parser.parse_args()

    dashboard = TechNewsDiagnosticDashboard()

    if args.summary_only:
        dashboard.print_summary()
    else:
        dashboard.save_report_json(args.output)
        dashboard.print_summary()


if __name__ == '__main__':
    main()
