#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inicializace SQLite databáze pro Tech News metriky
===================================================
Vytváří schéma pro sledování processing pipeline
"""

import sqlite3
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_database(db_path: str = '_data/tech_news_metrics.db'):
    """Inicializuje SQLite databázi s tabulkami pro metriky"""

    db_file = Path(db_path)
    db_file.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"📊 Inicializuji databázi: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Povolit WAL mode pro lepší concurrent access
    cursor.execute('PRAGMA journal_mode=WAL')

    # 1. Processing sessions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS processing_sessions (
            session_id TEXT PRIMARY KEY,
            timestamp DATETIME NOT NULL,
            status TEXT NOT NULL,

            -- API metrics
            articles_fetched INTEGER DEFAULT 0,
            api_response_time_ms INTEGER DEFAULT 0,

            -- Processing metrics
            articles_processed INTEGER DEFAULT 0,
            articles_llm_processed INTEGER DEFAULT 0,
            total_llm_tokens INTEGER DEFAULT 0,
            total_llm_cost_usd REAL DEFAULT 0.0,

            -- Save metrics
            articles_saved INTEGER DEFAULT 0,
            articles_skipped INTEGER DEFAULT 0,
            skip_reasons_json TEXT,

            -- Performance
            total_duration_seconds REAL DEFAULT 0.0,
            error_count INTEGER DEFAULT 0,
            error_messages_json TEXT
        )
    ''')

    # 2. Hourly aggregates
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hourly_metrics (
            hour_timestamp DATETIME PRIMARY KEY,
            sessions_count INTEGER DEFAULT 0,

            -- Aggregated metrics
            total_fetched INTEGER DEFAULT 0,
            total_processed INTEGER DEFAULT 0,
            total_saved INTEGER DEFAULT 0,
            total_skipped INTEGER DEFAULT 0,

            -- Quality metrics
            avg_importance REAL DEFAULT 0.0,
            czech_ratio REAL DEFAULT 0.0,
            enhanced_content_ratio REAL DEFAULT 0.0,

            -- Performance
            avg_session_duration_seconds REAL DEFAULT 0.0,
            total_llm_cost_usd REAL DEFAULT 0.0,
            error_rate REAL DEFAULT 0.0
        )
    ''')

    # 3. Daily rollups
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_rollups (
            date DATE PRIMARY KEY,
            sessions_count INTEGER DEFAULT 0,
            total_articles_saved INTEGER DEFAULT 0,
            unique_sources INTEGER DEFAULT 0,

            -- Distribution
            importance_distribution_json TEXT,
            category_distribution_json TEXT,
            source_distribution_json TEXT,

            -- Quality
            avg_content_length INTEGER DEFAULT 0,
            czech_ratio REAL DEFAULT 0.0,

            -- Cost & Performance
            total_llm_cost_usd REAL DEFAULT 0.0,
            avg_processing_time_seconds REAL DEFAULT 0.0,
            success_rate REAL DEFAULT 1.0
        )
    ''')

    # Create indexes
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_sessions_timestamp ON processing_sessions(timestamp)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_sessions_status ON processing_sessions(status)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_hourly_timestamp ON hourly_metrics(hour_timestamp)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_daily_date ON daily_rollups(date)')

    conn.commit()

    # Verify tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    logger.info(f"✅ Databáze inicializována s {len(tables)} tabulkami:")
    for table in tables:
        logger.info(f"   - {table[0]}")

    conn.close()

    return db_path


def verify_database(db_path: str = '_data/tech_news_metrics.db'):
    """Ověří integritu databáze"""

    logger.info(f"🔍 Ověřuji databázi: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Zkontrolovat tabulky
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]

    expected_tables = ['processing_sessions', 'hourly_metrics', 'daily_rollups']
    missing = [t for t in expected_tables if t not in tables]

    if missing:
        logger.error(f"❌ Chybějící tabulky: {missing}")
        return False

    # Zkontrolovat počty záznamů
    for table in expected_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        logger.info(f"   {table}: {count} záznamů")

    conn.close()

    logger.info("✅ Databáze je v pořádku")
    return True


def clear_old_data(db_path: str = '_data/tech_news_metrics.db', days: int = 90):
    """Smaže data starší než N dní"""

    logger.info(f"🧹 Čištění dat starších než {days} dní...")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Smazat staré sessions
    cursor.execute('''
        DELETE FROM processing_sessions
        WHERE timestamp < datetime('now', '-' || ? || ' days')
    ''', (days,))

    deleted_sessions = cursor.rowcount
    logger.info(f"   Smazáno {deleted_sessions} starých sessions")

    # Smazat staré hourly metrics
    cursor.execute('''
        DELETE FROM hourly_metrics
        WHERE hour_timestamp < datetime('now', '-' || ? || ' days')
    ''', (days,))

    deleted_hourly = cursor.rowcount
    logger.info(f"   Smazáno {deleted_hourly} hodinových metrik")

    # Daily rollups nechat déle (365 dní)
    cursor.execute('''
        DELETE FROM daily_rollups
        WHERE date < date('now', '-365 days')
    ''')

    deleted_daily = cursor.rowcount
    logger.info(f"   Smazáno {deleted_daily} denních agregací")

    conn.commit()

    # Vacuum pro optimalizaci
    logger.info("⚙️ Optimalizuji databázi (VACUUM)...")
    cursor.execute('VACUUM')

    conn.close()

    logger.info("✅ Čištění dokončeno")


def main():
    """Hlavní funkce"""
    import argparse

    parser = argparse.ArgumentParser(description='Inicializace metrics databáze')
    parser.add_argument(
        '--db-path',
        default='_data/tech_news_metrics.db',
        help='Cesta k SQLite databázi'
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Pouze ověřit databázi'
    )
    parser.add_argument(
        '--clean',
        type=int,
        metavar='DAYS',
        help='Smazat data starší než N dní'
    )

    args = parser.parse_args()

    if args.verify:
        verify_database(args.db_path)
    elif args.clean:
        clear_old_data(args.db_path, args.clean)
    else:
        init_database(args.db_path)
        verify_database(args.db_path)


if __name__ == '__main__':
    main()
