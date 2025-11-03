#!/usr/bin/env python3
"""
LLM Cost Tracker - Monitoring nákladů za OpenRouter API volání

Tento modul sleduje a zaznamenává náklady za volání LLM API přes OpenRouter.
Ukládá data do SQLite databáze a poskytuje statistiky o využití.
"""

import os
import sqlite3
import logging
from datetime import datetime, date
from typing import Dict, Any, Optional, Tuple
import json
import requests

# Nastavení logování
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Ceny pro různé modely (USD za 1M tokenů)
MODEL_PRICING = {
    "anthropic/claude-sonnet-4.5": {
        "input": 3.0,   # $3 per 1M input tokens
        "output": 15.0  # $15 per 1M output tokens
    },
    "anthropic/claude-3.5-sonnet": {
        "input": 3.0,
        "output": 15.0
    },
    "anthropic/claude-3-opus": {
        "input": 15.0,
        "output": 75.0
    },
    # Přidat další modely podle potřeby
}


class LLMCostTracker:
    """
    Třída pro sledování nákladů na LLM API volání.

    Attributes:
        db_path: Cesta k SQLite databázi
        conn: SQLite connection objekt
    """

    def __init__(self, db_path: str = "_data/llm_costs.db"):
        """
        Inicializuje cost tracker a vytvoří databázové tabulky.

        Args:
            db_path: Cesta k SQLite databázi (default: _data/llm_costs.db)
        """
        self.db_path = db_path

        # Vytvoř _data adresář pokud neexistuje
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Připoj se k databázi
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

        # Vytvoř tabulky
        self._init_database()

        logger.info(f"LLM Cost Tracker inicializován s databází: {db_path}")

    def _init_database(self):
        """Vytvoří databázové tabulky pokud neexistují."""
        cursor = self.conn.cursor()

        # Tabulka pro jednotlivá API volání
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_calls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME NOT NULL,
                model TEXT NOT NULL,
                operation TEXT NOT NULL,
                prompt_tokens INTEGER,
                completion_tokens INTEGER,
                total_tokens INTEGER,
                estimated_cost_usd REAL,
                article_slug TEXT,
                article_title TEXT,
                status TEXT NOT NULL,
                error_message TEXT,
                response_time_ms INTEGER
            )
        """)

        # Tabulka pro denní souhrny
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_summary (
                date DATE PRIMARY KEY,
                total_calls INTEGER NOT NULL,
                successful_calls INTEGER NOT NULL,
                failed_calls INTEGER NOT NULL,
                total_tokens INTEGER NOT NULL,
                total_prompt_tokens INTEGER NOT NULL,
                total_completion_tokens INTEGER NOT NULL,
                total_cost_usd REAL NOT NULL,
                operations_breakdown TEXT,
                last_updated DATETIME NOT NULL
            )
        """)

        # Indexy pro rychlejší dotazy
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_api_calls_timestamp
            ON api_calls(timestamp)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_api_calls_date
            ON api_calls(date(timestamp))
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_api_calls_operation
            ON api_calls(operation)
        """)

        self.conn.commit()
        logger.debug("Databázové tabulky inicializovány")

    def calculate_cost(
        self,
        model: str,
        prompt_tokens: int,
        completion_tokens: int
    ) -> float:
        """
        Vypočítá náklady na API volání.

        Args:
            model: Název modelu (např. "anthropic/claude-sonnet-4.5")
            prompt_tokens: Počet input tokenů
            completion_tokens: Počet output tokenů

        Returns:
            Odhadované náklady v USD
        """
        if model not in MODEL_PRICING:
            logger.warning(f"Neznámý model {model}, používám výchozí ceny")
            pricing = MODEL_PRICING.get("anthropic/claude-sonnet-4.5")
        else:
            pricing = MODEL_PRICING[model]

        input_cost = (prompt_tokens / 1_000_000) * pricing["input"]
        output_cost = (completion_tokens / 1_000_000) * pricing["output"]

        return input_cost + output_cost

    def log_call(
        self,
        model: str,
        operation: str,
        status: str,
        prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        article_slug: Optional[str] = None,
        article_title: Optional[str] = None,
        error_message: Optional[str] = None,
        response_time_ms: Optional[int] = None
    ) -> int:
        """
        Zaloguje API volání do databáze.

        Args:
            model: Název modelu
            operation: Typ operace (translate, categorize, summarize, atd.)
            status: Status volání ('success' nebo 'error')
            prompt_tokens: Počet input tokenů
            completion_tokens: Počet output tokenů
            article_slug: Slug článku (pokud relevantní)
            article_title: Název článku (pokud relevantní)
            error_message: Chybová zpráva (pokud status='error')
            response_time_ms: Doba odpovědi v milisekundách

        Returns:
            ID nového záznamu v databázi
        """
        cursor = self.conn.cursor()

        total_tokens = None
        estimated_cost = None

        if prompt_tokens is not None and completion_tokens is not None:
            total_tokens = prompt_tokens + completion_tokens
            estimated_cost = self.calculate_cost(model, prompt_tokens, completion_tokens)

        cursor.execute("""
            INSERT INTO api_calls (
                timestamp, model, operation, prompt_tokens, completion_tokens,
                total_tokens, estimated_cost_usd, article_slug, article_title,
                status, error_message, response_time_ms
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            model,
            operation,
            prompt_tokens,
            completion_tokens,
            total_tokens,
            estimated_cost,
            article_slug,
            article_title,
            status,
            error_message,
            response_time_ms
        ))

        self.conn.commit()
        call_id = cursor.lastrowid

        if status == 'success' and estimated_cost:
            logger.info(
                f"API call logged: {operation} | {total_tokens} tokens | "
                f"${estimated_cost:.6f} | Article: {article_slug or 'N/A'}"
            )

        return call_id

    def update_daily_summary(self, target_date: Optional[date] = None):
        """
        Aktualizuje denní souhrn pro dané datum.

        Args:
            target_date: Datum pro souhrn (default: dnes)
        """
        if target_date is None:
            target_date = date.today()

        cursor = self.conn.cursor()

        # Agreguj data pro dané datum
        cursor.execute("""
            SELECT
                COUNT(*) as total_calls,
                SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful_calls,
                SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) as failed_calls,
                COALESCE(SUM(total_tokens), 0) as total_tokens,
                COALESCE(SUM(prompt_tokens), 0) as total_prompt_tokens,
                COALESCE(SUM(completion_tokens), 0) as total_completion_tokens,
                COALESCE(SUM(estimated_cost_usd), 0) as total_cost_usd
            FROM api_calls
            WHERE date(timestamp) = ?
        """, (target_date.isoformat(),))

        row = cursor.fetchone()

        # Získej breakdown podle operací
        cursor.execute("""
            SELECT
                operation,
                COUNT(*) as count,
                COALESCE(SUM(estimated_cost_usd), 0) as cost
            FROM api_calls
            WHERE date(timestamp) = ?
            GROUP BY operation
        """, (target_date.isoformat(),))

        operations = {}
        for op_row in cursor.fetchall():
            operations[op_row['operation']] = {
                'count': op_row['count'],
                'cost': op_row['cost']
            }

        # Ulož nebo updatuj souhrn
        cursor.execute("""
            INSERT OR REPLACE INTO daily_summary (
                date, total_calls, successful_calls, failed_calls,
                total_tokens, total_prompt_tokens, total_completion_tokens,
                total_cost_usd, operations_breakdown, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            target_date.isoformat(),
            row['total_calls'],
            row['successful_calls'],
            row['failed_calls'],
            row['total_tokens'],
            row['total_prompt_tokens'],
            row['total_completion_tokens'],
            row['total_cost_usd'],
            json.dumps(operations),
            datetime.now().isoformat()
        ))

        self.conn.commit()
        logger.info(
            f"Daily summary updated for {target_date}: "
            f"{row['total_calls']} calls, ${row['total_cost_usd']:.4f}"
        )

    def get_stats(
        self,
        days: int = 7
    ) -> Dict[str, Any]:
        """
        Vrátí statistiky za poslední N dní.

        Args:
            days: Počet dní zpětně (default: 7)

        Returns:
            Dictionary se statistikami
        """
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) as total_calls,
                SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as successful_calls,
                SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) as failed_calls,
                COALESCE(SUM(total_tokens), 0) as total_tokens,
                COALESCE(SUM(estimated_cost_usd), 0) as total_cost
            FROM api_calls
            WHERE timestamp >= datetime('now', '-' || ? || ' days')
        """, (days,))

        row = cursor.fetchone()

        return {
            'period_days': days,
            'total_calls': row['total_calls'],
            'successful_calls': row['successful_calls'],
            'failed_calls': row['failed_calls'],
            'total_tokens': row['total_tokens'],
            'total_cost_usd': round(row['total_cost'], 4),
            'avg_cost_per_call': round(row['total_cost'] / row['total_calls'], 6) if row['total_calls'] > 0 else 0,
            'avg_tokens_per_call': round(row['total_tokens'] / row['total_calls'], 0) if row['total_calls'] > 0 else 0
        }

    def close(self):
        """Zavře databázové připojení."""
        if self.conn:
            self.conn.close()
            logger.debug("Database connection closed")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


def track_llm_call(
    url: str,
    headers: Dict[str, str],
    data: Dict[str, Any],
    operation: str,
    article_slug: Optional[str] = None,
    article_title: Optional[str] = None,
    timeout: int = 60,
    tracker: Optional[LLMCostTracker] = None
) -> Tuple[Optional[requests.Response], Optional[Dict[str, Any]]]:
    """
    Wrapper funkce pro OpenRouter API volání s automatickým cost trackingem.

    Args:
        url: OpenRouter API URL
        headers: HTTP headers
        data: Request payload (JSON)
        operation: Název operace (translate, categorize, atd.)
        article_slug: Slug článku
        article_title: Název článku
        timeout: Timeout v sekundách
        tracker: LLMCostTracker instance (pokud None, vytvoří se nová)

    Returns:
        Tuple (response, usage_dict) nebo (None, None) při chybě
    """
    close_tracker = False
    if tracker is None:
        tracker = LLMCostTracker()
        close_tracker = True

    model = data.get('model', 'unknown')
    start_time = datetime.now()

    try:
        # Proveď API volání
        response = requests.post(url, headers=headers, json=data, timeout=timeout)
        response.raise_for_status()

        response_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)

        # Extrahuj usage data z response
        response_json = response.json()
        usage = response_json.get('usage', {})

        prompt_tokens = usage.get('prompt_tokens')
        completion_tokens = usage.get('completion_tokens')

        # Zaloguj úspěšné volání
        tracker.log_call(
            model=model,
            operation=operation,
            status='success',
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            article_slug=article_slug,
            article_title=article_title,
            response_time_ms=response_time_ms
        )

        # Aktualizuj denní souhrn
        tracker.update_daily_summary()

        return response, usage

    except requests.exceptions.RequestException as e:
        # Zaloguj chybu
        response_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)

        tracker.log_call(
            model=model,
            operation=operation,
            status='error',
            article_slug=article_slug,
            article_title=article_title,
            error_message=str(e),
            response_time_ms=response_time_ms
        )

        logger.error(f"API call failed for {operation}: {str(e)}")
        return None, None

    finally:
        if close_tracker:
            tracker.close()


if __name__ == "__main__":
    # Test cost trackeru
    with LLMCostTracker() as tracker:
        # Test výpočtu nákladů
        cost = tracker.calculate_cost(
            "anthropic/claude-sonnet-4.5",
            prompt_tokens=1000,
            completion_tokens=500
        )
        print(f"Test cost calculation: ${cost:.6f}")

        # Test logu
        tracker.log_call(
            model="anthropic/claude-sonnet-4.5",
            operation="test",
            status="success",
            prompt_tokens=1000,
            completion_tokens=500,
            article_slug="test-article"
        )

        # Získej statistiky
        stats = tracker.get_stats(days=7)
        print("\nStats for last 7 days:")
        print(json.dumps(stats, indent=2))
