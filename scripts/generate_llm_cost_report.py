#!/usr/bin/env python3
"""
LLM Cost Report Generator - Generování přehledů nákladů za LLM API

Tento skript generuje denní, týdenní a měsíční reporty nákladů
za OpenRouter API volání z SQLite databáze.
"""

import os
import sys
import sqlite3
import json
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import Dict, List, Any
import argparse

# Přidat parent directory do path pro import llm_cost_tracker
sys.path.insert(0, str(Path(__file__).parent))

from llm_cost_tracker import LLMCostTracker


class LLMCostReportGenerator:
    """
    Generátor reportů nákladů za LLM API.

    Attributes:
        tracker: LLMCostTracker instance
        output_dir: Adresář pro výstupní reporty
    """

    def __init__(self, db_path: str = "_data/llm_costs.db", output_dir: str = "_data"):
        """
        Inicializuje report generator.

        Args:
            db_path: Cesta k SQLite databázi
            output_dir: Adresář pro výstupní reporty
        """
        self.tracker = LLMCostTracker(db_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def get_daily_stats(self, target_date: date) -> Dict[str, Any]:
        """
        Získá statistiky pro konkrétní den.

        Args:
            target_date: Datum pro statistiky

        Returns:
            Dictionary se statistikami
        """
        cursor = self.tracker.conn.cursor()

        # Celkové statistiky
        cursor.execute("""
            SELECT
                COUNT(*) as total_calls,
                SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful_calls,
                SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) as failed_calls,
                COALESCE(SUM(total_tokens), 0) as total_tokens,
                COALESCE(SUM(prompt_tokens), 0) as prompt_tokens,
                COALESCE(SUM(completion_tokens), 0) as completion_tokens,
                COALESCE(SUM(estimated_cost_usd), 0) as total_cost,
                COALESCE(AVG(response_time_ms), 0) as avg_response_time
            FROM api_calls
            WHERE date(timestamp) = ?
        """, (target_date.isoformat(),))

        row = cursor.fetchone()

        # Breakdown podle operací
        cursor.execute("""
            SELECT
                operation,
                COUNT(*) as count,
                COALESCE(SUM(total_tokens), 0) as tokens,
                COALESCE(SUM(estimated_cost_usd), 0) as cost,
                COALESCE(AVG(response_time_ms), 0) as avg_response_time
            FROM api_calls
            WHERE date(timestamp) = ?
            GROUP BY operation
            ORDER BY cost DESC
        """, (target_date.isoformat(),))

        operations = []
        for op_row in cursor.fetchall():
            operations.append({
                'operation': op_row['operation'],
                'count': op_row['count'],
                'tokens': op_row['tokens'],
                'cost': op_row['cost'],
                'avg_response_time': op_row['avg_response_time']
            })

        # Top 5 nejdražších článků
        cursor.execute("""
            SELECT
                article_title,
                COUNT(*) as call_count,
                COALESCE(SUM(estimated_cost_usd), 0) as total_cost,
                COALESCE(SUM(total_tokens), 0) as total_tokens
            FROM api_calls
            WHERE date(timestamp) = ? AND article_title IS NOT NULL
            GROUP BY article_title
            ORDER BY total_cost DESC
            LIMIT 5
        """, (target_date.isoformat(),))

        top_articles = []
        for article_row in cursor.fetchall():
            top_articles.append({
                'title': article_row['article_title'],
                'call_count': article_row['call_count'],
                'cost': article_row['total_cost'],
                'tokens': article_row['total_tokens']
            })

        return {
            'date': target_date.isoformat(),
            'total_calls': row['total_calls'],
            'successful_calls': row['successful_calls'],
            'failed_calls': row['failed_calls'],
            'total_tokens': row['total_tokens'],
            'prompt_tokens': row['prompt_tokens'],
            'completion_tokens': row['completion_tokens'],
            'total_cost': round(row['total_cost'], 4),
            'avg_response_time': round(row['avg_response_time'], 0),
            'operations': operations,
            'top_articles': top_articles
        }

    def get_period_stats(self, days: int = 7) -> Dict[str, Any]:
        """
        Získá statistiky za poslední N dní.

        Args:
            days: Počet dní zpětně

        Returns:
            Dictionary se statistikami
        """
        cursor = self.tracker.conn.cursor()

        start_date = date.today() - timedelta(days=days-1)
        end_date = date.today()

        # Celkové statistiky
        cursor.execute("""
            SELECT
                COUNT(*) as total_calls,
                SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful_calls,
                SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) as failed_calls,
                COALESCE(SUM(total_tokens), 0) as total_tokens,
                COALESCE(SUM(estimated_cost_usd), 0) as total_cost
            FROM api_calls
            WHERE date(timestamp) >= ? AND date(timestamp) <= ?
        """, (start_date.isoformat(), end_date.isoformat()))

        row = cursor.fetchone()

        # Denní breakdown
        cursor.execute("""
            SELECT
                date(timestamp) as date,
                COUNT(*) as calls,
                COALESCE(SUM(estimated_cost_usd), 0) as cost
            FROM api_calls
            WHERE date(timestamp) >= ? AND date(timestamp) <= ?
            GROUP BY date(timestamp)
            ORDER BY date(timestamp) DESC
        """, (start_date.isoformat(), end_date.isoformat()))

        daily_breakdown = []
        for day_row in cursor.fetchall():
            daily_breakdown.append({
                'date': day_row['date'],
                'calls': day_row['calls'],
                'cost': day_row['cost']
            })

        # Operations breakdown
        cursor.execute("""
            SELECT
                operation,
                COUNT(*) as count,
                COALESCE(SUM(estimated_cost_usd), 0) as cost
            FROM api_calls
            WHERE date(timestamp) >= ? AND date(timestamp) <= ?
            GROUP BY operation
            ORDER BY cost DESC
        """, (start_date.isoformat(), end_date.isoformat()))

        operations = []
        for op_row in cursor.fetchall():
            operations.append({
                'operation': op_row['operation'],
                'count': op_row['count'],
                'cost': op_row['cost']
            })

        return {
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat(),
            'days': days,
            'total_calls': row['total_calls'],
            'successful_calls': row['successful_calls'],
            'failed_calls': row['failed_calls'],
            'total_tokens': row['total_tokens'],
            'total_cost': round(row['total_cost'], 4),
            'avg_cost_per_day': round(row['total_cost'] / days, 4) if days > 0 else 0,
            'daily_breakdown': daily_breakdown,
            'operations': operations
        }

    def generate_markdown_report(self, output_file: str = "llm_costs_report.md"):
        """
        Generuje Markdown report s přehledem nákladů.

        Args:
            output_file: Název výstupního souboru
        """
        output_path = self.output_dir / output_file

        # Získat statistiky
        today_stats = self.get_daily_stats(date.today())
        weekly_stats = self.get_period_stats(days=7)
        monthly_stats = self.get_period_stats(days=30)

        # Sestavit Markdown report
        report = f"""---
title: LLM Cost Report
generated: {datetime.now().isoformat()}
---

# LLM Cost Report

Přehled nákladů za OpenRouter API volání pro generování tech-news.

*Vygenerováno: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

---

## 📊 Dnes ({today_stats['date']})

### Celkové statistiky
- **Celkem volání:** {today_stats['total_calls']} (úspěšných: {today_stats['successful_calls']}, chyb: {today_stats['failed_calls']})
- **Celkem tokenů:** {today_stats['total_tokens']:,} ({today_stats['prompt_tokens']:,} input + {today_stats['completion_tokens']:,} output)
- **Celková cena:** ${today_stats['total_cost']:.4f}
- **Průměrná doba odpovědi:** {today_stats['avg_response_time']:.0f} ms

### Breakdown podle operací
"""

        if today_stats['operations']:
            report += "\n| Operace | Počet | Tokeny | Cena | Avg. čas (ms) |\n"
            report += "|---------|-------|--------|------|---------------|\n"
            for op in today_stats['operations']:
                report += f"| {op['operation']} | {op['count']} | {op['tokens']:,} | ${op['cost']:.4f} | {op['avg_response_time']:.0f} |\n"
        else:
            report += "\n*Žádná data pro dnešek.*\n"

        if today_stats['top_articles']:
            report += "\n### 🏆 Top 5 nejdražších článků (dnes)\n\n"
            for i, article in enumerate(today_stats['top_articles'], 1):
                report += f"{i}. **{article['title'][:80]}**\n"
                report += f"   - Volání: {article['call_count']}, Tokeny: {article['tokens']:,}, Cena: ${article['cost']:.4f}\n\n"

        report += f"""
---

## 📅 Poslední týden ({weekly_stats['start_date']} až {weekly_stats['end_date']})

### Celkové statistiky
- **Celkem volání:** {weekly_stats['total_calls']} (úspěšných: {weekly_stats['successful_calls']}, chyb: {weekly_stats['failed_calls']})
- **Celkem tokenů:** {weekly_stats['total_tokens']:,}
- **Celková cena:** ${weekly_stats['total_cost']:.4f}
- **Průměrná cena za den:** ${weekly_stats['avg_cost_per_day']:.4f}

### Denní breakdown
"""

        if weekly_stats['daily_breakdown']:
            report += "\n| Datum | Volání | Cena |\n"
            report += "|-------|--------|------|\n"
            for day in weekly_stats['daily_breakdown']:
                report += f"| {day['date']} | {day['calls']} | ${day['cost']:.4f} |\n"
        else:
            report += "\n*Žádná data pro poslední týden.*\n"

        report += "\n### Operations breakdown\n"
        if weekly_stats['operations']:
            report += "\n| Operace | Počet | Cena |\n"
            report += "|---------|-------|------|\n"
            for op in weekly_stats['operations']:
                report += f"| {op['operation']} | {op['count']} | ${op['cost']:.4f} |\n"

        report += f"""
---

## 📆 Poslední měsíc ({monthly_stats['start_date']} až {monthly_stats['end_date']})

### Celkové statistiky
- **Celkem volání:** {monthly_stats['total_calls']} (úspěšných: {monthly_stats['successful_calls']}, chyb: {monthly_stats['failed_calls']})
- **Celkem tokenů:** {monthly_stats['total_tokens']:,}
- **Celková cena:** ${monthly_stats['total_cost']:.4f}
- **Průměrná cena za den:** ${monthly_stats['avg_cost_per_day']:.4f}
- **Odhadovaná měsíční cena:** ${monthly_stats['avg_cost_per_day'] * 30:.2f}

### Operations breakdown
"""

        if monthly_stats['operations']:
            report += "\n| Operace | Počet | Cena | % z celku |\n"
            report += "|---------|-------|------|----------|\n"
            total_cost = monthly_stats['total_cost']
            for op in monthly_stats['operations']:
                percentage = (op['cost'] / total_cost * 100) if total_cost > 0 else 0
                report += f"| {op['operation']} | {op['count']} | ${op['cost']:.4f} | {percentage:.1f}% |\n"
        else:
            report += "\n*Žádná data pro poslední měsíc.*\n"

        report += """
---

## 📝 Poznámky

- Ceny jsou odhadované na základě token usage a aktuálních cen modelů
- Claude Sonnet 4.5: $3/M input tokens, $15/M output tokens
- Workflow běží každé 4 hodiny (6x denně)
- Každý článek vyžaduje typicky 4-5 API volání
"""

        # Uložit report
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"✅ Report vygenerován: {output_path}")
        return output_path

    def print_summary(self):
        """Vypíše stručný přehled do konzole."""
        today_stats = self.get_daily_stats(date.today())
        weekly_stats = self.get_period_stats(days=7)
        monthly_stats = self.get_period_stats(days=30)

        print("\n" + "="*60)
        print("📊 LLM COST SUMMARY")
        print("="*60)

        print(f"\n🔹 Today ({today_stats['date']}):")
        print(f"   Calls: {today_stats['total_calls']} | Cost: ${today_stats['total_cost']:.4f}")

        print(f"\n🔹 Last 7 days:")
        print(f"   Calls: {weekly_stats['total_calls']} | Cost: ${weekly_stats['total_cost']:.4f}")
        print(f"   Avg per day: ${weekly_stats['avg_cost_per_day']:.4f}")

        print(f"\n🔹 Last 30 days:")
        print(f"   Calls: {monthly_stats['total_calls']} | Cost: ${monthly_stats['total_cost']:.4f}")
        print(f"   Estimated monthly: ${monthly_stats['avg_cost_per_day'] * 30:.2f}")

        print("\n" + "="*60 + "\n")

    def close(self):
        """Zavře databázové připojení."""
        self.tracker.close()


def main():
    """Hlavní funkce"""
    parser = argparse.ArgumentParser(description="Generate LLM cost reports")
    parser.add_argument(
        '--output',
        default='llm_costs_report.md',
        help='Output markdown file name (default: llm_costs_report.md)'
    )
    parser.add_argument(
        '--summary-only',
        action='store_true',
        help='Print summary to console only, without generating report'
    )
    parser.add_argument(
        '--db',
        default='_data/llm_costs.db',
        help='Path to SQLite database (default: _data/llm_costs.db)'
    )

    args = parser.parse_args()

    # Zkontrolovat existenci databáze
    if not Path(args.db).exists():
        print(f"❌ Databáze nenalezena: {args.db}")
        print("   Spusťte nejdřív generate_tech_news_newsapi.py pro vytvoření dat.")
        return 1

    generator = LLMCostReportGenerator(db_path=args.db)

    try:
        if args.summary_only:
            # Jen vypsat summary
            generator.print_summary()
        else:
            # Vygenerovat plný report
            generator.print_summary()
            generator.generate_markdown_report(output_file=args.output)

    finally:
        generator.close()

    return 0


if __name__ == "__main__":
    exit(main())
