#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Processing Logger pro Tech News Pipeline
=========================================
Sleduje celý processing pipeline: API fetch → LLM processing → Storage
"""

import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)


class ProcessingLogger:
    """Centralizovaný logger pro celý processing pipeline"""

    def __init__(self, db_path: str = '_data/tech_news_metrics.db'):
        self.session_id = self._generate_session_id()
        self.start_time = time.time()
        self.timestamp = datetime.now(timezone.utc)

        # Metriky
        self.metrics = {
            'api': defaultdict(int),
            'processing': defaultdict(int),
            'filtering': defaultdict(int),
            'save': defaultdict(int),
            'performance': defaultdict(float)
        }

        self.errors = []
        self.skip_reasons = []

        # SQLite connection
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None

        # JSON Lines log path
        log_dir = Path('_data/processing_logs')
        log_dir.mkdir(parents=True, exist_ok=True)
        self.jsonl_path = log_dir / f"{self.timestamp.strftime('%Y-%m-%d')}.jsonl"

        logger.info(f"📊 Processing Logger inicializován: {self.session_id}")

    def _generate_session_id(self) -> str:
        """Generuje unikátní session ID"""
        now = datetime.now(timezone.utc)
        return f"gen_{now.strftime('%Y%m%d_%H%M%S')}_{id(self) % 10000:04d}"

    def log_phase_start(self, phase: str):
        """Log začátku fáze (fetch/process/save)"""
        logger.info(f"🔄 Fáze: {phase}")
        self.metrics['performance'][f'{phase}_start'] = time.time()

    def log_phase_end(self, phase: str):
        """Log konce fáze"""
        start_key = f'{phase}_start'
        if start_key in self.metrics['performance']:
            duration = time.time() - self.metrics['performance'][start_key]
            self.metrics['performance'][f'{phase}_duration_seconds'] = duration
            logger.info(f"✅ Fáze {phase} dokončena za {duration:.2f}s")

    def log_api_fetch(self, articles_count: int, response_time_ms: int, status_code: int = 200, error: Optional[str] = None):
        """Log API fetch metriky"""
        self.metrics['api']['total_fetched'] = articles_count
        self.metrics['api']['api_response_time_ms'] = response_time_ms
        self.metrics['api']['api_status_code'] = status_code

        if error:
            self.metrics['api']['api_error'] = error
            self.errors.append({'phase': 'api_fetch', 'error': error})

        logger.info(f"📥 API fetch: {articles_count} článků za {response_time_ms}ms")

    def log_article_processing(self, article_slug: str, result: Dict):
        """Log zpracování jednotlivého článku"""
        self.metrics['processing']['total_processed'] += 1

        if result.get('llm_used'):
            self.metrics['processing']['llm_processed'] += 1

            # LLM metriky
            if 'tokens' in result:
                self.metrics['processing']['total_llm_tokens'] = \
                    self.metrics['processing'].get('total_llm_tokens', 0) + result['tokens']

            if 'cost' in result:
                self.metrics['processing']['total_llm_cost_usd'] = \
                    self.metrics['processing'].get('total_llm_cost_usd', 0.0) + result['cost']

            if 'response_time_ms' in result:
                # Průměrný response time
                current_avg = self.metrics['processing'].get('avg_llm_response_time_ms', 0)
                count = self.metrics['processing']['llm_processed']
                new_avg = ((current_avg * (count - 1)) + result['response_time_ms']) / count
                self.metrics['processing']['avg_llm_response_time_ms'] = new_avg

        logger.debug(f"⚙️ Zpracován: {article_slug}")

    def log_article_skip(self, reason: str, article_title: str, details: Optional[Dict] = None):
        """Log přeskočení článku s důvodem"""
        # Kategorizace důvodů
        reason_key = f'skipped_{reason}'
        self.metrics['filtering'][reason_key] = self.metrics['filtering'].get(reason_key, 0) + 1
        self.metrics['filtering']['total_skipped'] = self.metrics['filtering'].get('total_skipped', 0) + 1

        self.skip_reasons.append({
            'reason': reason,
            'title': article_title[:100],
            'details': details
        })

        logger.debug(f"⏭️ Přeskočeno ({reason}): {article_title[:50]}")

    def log_article_save(self, article_data: Dict):
        """Log uložení článku"""
        self.metrics['save']['total_saved'] += 1

        # Importance distribuce
        importance = article_data.get('importance', 3)
        importance_key = f'importance_{importance}'
        self.metrics['save'][importance_key] = self.metrics['save'].get(importance_key, 0) + 1

        # Jazyková kvalita
        if article_data.get('has_czech'):
            self.metrics['save']['czech_articles'] = self.metrics['save'].get('czech_articles', 0) + 1
        else:
            self.metrics['save']['english_articles'] = self.metrics['save'].get('english_articles', 0) + 1

        # Další metriky
        if article_data.get('has_image'):
            self.metrics['save']['articles_with_images'] = self.metrics['save'].get('articles_with_images', 0) + 1

        if article_data.get('enhanced_content'):
            self.metrics['save']['articles_with_enhanced_content'] = \
                self.metrics['save'].get('articles_with_enhanced_content', 0) + 1

        logger.debug(f"💾 Uloženo: {article_data.get('title', 'unknown')[:50]} (importance: {importance})")

    def log_error(self, phase: str, error: str, details: Optional[Dict] = None):
        """Log chyby"""
        self.errors.append({
            'phase': phase,
            'error': error,
            'details': details,
            'timestamp': datetime.now(timezone.utc).isoformat()
        })
        logger.error(f"❌ Chyba v {phase}: {error}")

    def finalize_and_save(self):
        """Finalizuj session a ulož všechny metriky"""
        # Vypočti celkový čas
        total_duration = time.time() - self.start_time
        self.metrics['performance']['total_duration_seconds'] = total_duration

        # Sestav kompletní log záznam
        log_record = {
            'version': '1.0',
            'timestamp': self.timestamp.isoformat(),
            'session_id': self.session_id,
            'status': 'success' if len(self.errors) == 0 else 'error',

            'api_metrics': dict(self.metrics['api']),
            'processing_metrics': dict(self.metrics['processing']),
            'filtering_metrics': dict(self.metrics['filtering']),
            'save_metrics': dict(self.metrics['save']),
            'performance': dict(self.metrics['performance']),

            'error_count': len(self.errors),
            'error_details': self.errors[:10],  # Max 10 chyb
            'skip_count': len(self.skip_reasons),
            'skip_sample': self.skip_reasons[:20]  # Max 20 samples
        }

        # Ulož do JSON Lines
        try:
            with self.jsonl_path.open('a', encoding='utf-8') as f:
                f.write(json.dumps(log_record, ensure_ascii=False) + '\n')
            logger.info(f"💾 JSON log uložen: {self.jsonl_path}")
        except Exception as e:
            logger.error(f"❌ Nelze uložit JSON log: {e}")

        # Ulož do SQLite
        try:
            self._save_to_database(log_record)
            logger.info(f"💾 Metriky uloženy do databáze: {self.db_path}")
        except Exception as e:
            logger.error(f"❌ Nelze uložit do databáze: {e}")

        # Výpis summary
        self._print_summary()

    def _save_to_database(self, log_record: Dict):
        """Uloží metriky do SQLite databáze"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Vložit do processing_sessions
        cursor.execute('''
            INSERT INTO processing_sessions (
                session_id, timestamp, status,
                articles_fetched, api_response_time_ms,
                articles_processed, articles_llm_processed,
                total_llm_tokens, total_llm_cost_usd,
                articles_saved, articles_skipped,
                skip_reasons_json,
                total_duration_seconds,
                error_count, error_messages_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            log_record['session_id'],
            log_record['timestamp'],
            log_record['status'],
            log_record['api_metrics'].get('total_fetched', 0),
            log_record['api_metrics'].get('api_response_time_ms', 0),
            log_record['processing_metrics'].get('total_processed', 0),
            log_record['processing_metrics'].get('llm_processed', 0),
            log_record['processing_metrics'].get('total_llm_tokens', 0),
            log_record['processing_metrics'].get('total_llm_cost_usd', 0.0),
            log_record['save_metrics'].get('total_saved', 0),
            log_record['filtering_metrics'].get('total_skipped', 0),
            json.dumps(log_record['filtering_metrics']),
            log_record['performance'].get('total_duration_seconds', 0),
            log_record['error_count'],
            json.dumps(log_record['error_details'])
        ))

        conn.commit()
        conn.close()

    def _print_summary(self):
        """Vytiskne summary do konzole"""
        api = self.metrics['api']
        proc = self.metrics['processing']
        filt = self.metrics['filtering']
        save = self.metrics['save']
        perf = self.metrics['performance']

        print("\n" + "="*60)
        print(f"📊 PROCESSING SESSION SUMMARY: {self.session_id}")
        print("="*60)

        print(f"\n📥 API FETCH:")
        print(f"  Articles fetched: {api.get('total_fetched', 0)}")
        print(f"  Response time: {api.get('api_response_time_ms', 0)}ms")

        print(f"\n⚙️ PROCESSING:")
        print(f"  Total processed: {proc.get('total_processed', 0)}")
        print(f"  LLM processed: {proc.get('llm_processed', 0)}")
        print(f"  LLM tokens: {proc.get('total_llm_tokens', 0):,}")
        print(f"  LLM cost: ${proc.get('total_llm_cost_usd', 0.0):.4f}")

        print(f"\n⏭️ FILTERING:")
        print(f"  Total skipped: {filt.get('total_skipped', 0)}")
        for reason, count in sorted(filt.items()):
            if reason.startswith('skipped_') and count > 0:
                print(f"    {reason.replace('skipped_', '')}: {count}")

        print(f"\n💾 SAVED:")
        print(f"  Total saved: {save.get('total_saved', 0)}")
        for i in range(5, 0, -1):
            count = save.get(f'importance_{i}', 0)
            if count > 0:
                print(f"    Importance {i}: {count}")
        print(f"  Czech articles: {save.get('czech_articles', 0)}")
        print(f"  With images: {save.get('articles_with_images', 0)}")

        print(f"\n⏱️ PERFORMANCE:")
        print(f"  Total duration: {perf.get('total_duration_seconds', 0):.2f}s")

        if self.errors:
            print(f"\n❌ ERRORS: {len(self.errors)}")
            for err in self.errors[:5]:
                print(f"    [{err['phase']}] {err['error']}")

        print("\n" + "="*60 + "\n")
