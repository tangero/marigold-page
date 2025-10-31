# Tech-News: Analýza problému a návrh řešení

## 🔴 Zjištěné problémy

### 1. Obrovská velikost stránky
```
Soubor: _site/tech-news/index.html
Velikost: 6.4 MB
Řádky: 163,250
```
**Důsledky:**
- Pomalé načítání stránky
- Vysoká spotřeba dat
- Problémy s výkonem prohlížeče
- Špatné SEO

### 2. Nadměrný počet článků v kolekci
```
Celkem článků v _tech_news/: 2,478
Nejstarší článek: 23. září 2025
Nejnovější článek: 29. října 2025
Rozsah: více než měsíc
```

**Rozdělení podle období:**
- Dnes (30.10.): 0 článků
- Včera (29.10.): 1 článek
- Poslední týden (23-29.10.): 263 článků
- Celkem: 2,478 článků

### 3. Chybějící filtrace podle data

**Layout `tech_news_index.html` (řádky 26-29):**
```liquid
{% assign all_dates = site.tech_news | map: 'date' | uniq | sort | reverse %}
{% assign sorted_articles = site.tech_news | sort: 'publishedAt' | reverse %}
{% assign recent_articles = sorted_articles | limit: 18 %}
```

**Problém:**
- ❌ Načítá **VŠECH 2,478 článků** z kolekce
- ❌ Žádná filtrace podle data (24 hodin)
- ❌ Jen limit 18 článků, ale po načtení všech
- ❌ Jekyll musí při každém buildu zpracovat všechny články

### 4. Neefektivní build proces

**Současný stav:**
1. Jekyll načte všech 2,478 článků do paměti
2. Seřadí je podle publishedAt
3. Vezme prvních 18
4. Vygeneruje 6.4 MB HTML soubor

**Výsledek:**
- Dlouhý build čas
- Vysoká spotřeba paměti
- Neefektivní využití zdrojů

## 💡 Navrhovaná řešení

### Řešení A: Cleanup + Filtrace (DOPORUČENO)

#### 1. Automatický cleanup starých článků

**Vytvořit skript `.github/scripts/cleanup_old_tech_news.py`:**
```python
#!/usr/bin/env python3
"""
Cleanup starých tech-news článků
Ponechá pouze články za posledních 7 dní
"""

from pathlib import Path
from datetime import datetime, timedelta, timezone
import re

def cleanup_old_articles(days_to_keep=7):
    tech_news_dir = Path('_tech_news')
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_to_keep)

    removed_count = 0
    kept_count = 0

    for article_file in tech_news_dir.glob('*.md'):
        if article_file.name == 'index.md':
            continue

        # Extrahovat datum z názvu souboru (YYYY-MM-DD)
        match = re.match(r'(\d{4}-\d{2}-\d{2})-', article_file.name)
        if not match:
            continue

        article_date = datetime.fromisoformat(match.group(1)).replace(tzinfo=timezone.utc)

        if article_date < cutoff_date:
            article_file.unlink()
            removed_count += 1
        else:
            kept_count += 1

    print(f"✅ Cleanup dokončen")
    print(f"   Smazáno: {removed_count} článků")
    print(f"   Ponecháno: {kept_count} článků")

    return removed_count, kept_count

if __name__ == "__main__":
    cleanup_old_articles(days_to_keep=7)
```

#### 2. Přidat cleanup do GitHub Actions workflow

**`.github/workflows/tech-news.yml` - přidat před build:**
```yaml
- name: Cleanup old tech-news articles
  run: python .github/scripts/cleanup_old_tech_news.py
```

#### 3. Filtrovat v layoutu podle data

**Aktualizovat `_layouts/tech_news_index.html` (řádky 26-34):**
```liquid
{% comment %} Získat články za posledních 24-48 hodin {% endcomment %}
{% if site.tech_news %}
  {% comment %} Vypočítat cutoff timestamp (48 hodin zpět) {% endcomment %}
  {% assign now_timestamp = 'now' | date: '%s' | to_integer %}
  {% assign cutoff_timestamp = now_timestamp | minus: 172800 %} {% comment %} 48 hodin = 172800 sekund {% endcomment %}

  {% comment %} Filtrovat články podle publishedAt {% endcomment %}
  {% assign recent_articles = "" | split: "," %}
  {% for article in site.tech_news %}
    {% assign article_timestamp = article.publishedAt | date: '%s' | to_integer %}
    {% if article_timestamp >= cutoff_timestamp %}
      {% assign recent_articles = recent_articles | push: article %}
    {% endif %}
  {% endfor %}

  {% comment %} Seřadit podle důležitosti a času {% endcomment %}
  {% assign recent_articles = recent_articles | sort: 'importance' | reverse %}
  {% assign recent_articles = recent_articles | limit: 18 %}
{% else %}
  {% assign recent_articles = "" | split: "," %}
{% endif %}
```

**Výhody:**
- ✅ Zobrazí jen relevantní články (24-48 hodin)
- ✅ Automatický cleanup snižuje velikost kolekce
- ✅ Zachovává historii v denních stránkách
- ✅ Snížení velikosti HTML na ~100-200 KB

---

### Řešení B: Redirect na denní stránku

**Změnit `/tech-news/` na redirect:**

**`_pages/tech-news.md`:**
```yaml
---
layout: tech_news_redirect
title: Technologické zprávy
permalink: /tech-news/
---
```

**`_layouts/tech_news_redirect.html`:**
```html
---
layout: default
---

<script>
// Přesměrovat na nejnovější denní stránku
const today = new Date();
const yyyy = today.getFullYear();
const mm = String(today.getMonth() + 1).padStart(2, '0');
const dd = String(today.getDate()).padStart(2, '0');
const dateStr = `${yyyy}-${mm}-${dd}`;

window.location.href = `/tech-news/${dateStr}/`;
</script>

<div style="text-align: center; padding: 3rem;">
  <p>Přesměrovávám na dnešní zprávy...</p>
  <p><a href="/tech-news/{{ 'now' | date: '%Y-%m-%d' }}/">Pokračovat ručně</a></p>
</div>
```

**Výhody:**
- ✅ Nejjednodušší řešení
- ✅ Žádné načítání velkých kolekcí
- ✅ Denní stránky už existují
- ✅ Okamžité zobrazení

**Nevýhody:**
- ⚠️ Žádný přehled napříč dny
- ⚠️ Nutný JavaScript

---

### Řešení C: Kombinované (NEJVÍCE ROBUSTNÍ)

Kombinace řešení A + B:

1. **Cleanup starých článků** (7 dní)
2. **Hlavní stránka zobrazuje 18 nejnovějších** (48 hodin)
3. **Fallback redirect** pokud nejsou žádné články za 48 hodin
4. **Link na archiv** pro přístup k denním stránkám

**Implementace:**

**1. Cleanup script** (stejný jako Řešení A)

**2. Aktualizovaný layout `tech_news_index.html`:**
```liquid
{% comment %} Filtrovat články za posledních 48 hodin {% endcomment %}
{% assign now_timestamp = 'now' | date: '%s' | to_integer %}
{% assign cutoff_timestamp = now_timestamp | minus: 172800 %}

{% assign recent_articles = "" | split: "," %}
{% for article in site.tech_news %}
  {% assign article_timestamp = article.publishedAt | date: '%s' | to_integer %}
  {% if article_timestamp >= cutoff_timestamp %}
    {% assign recent_articles = recent_articles | push: article %}
  {% endif %}
{% endfor %}

{% if recent_articles.size == 0 %}
  {% comment %} Fallback - přesměrovat na nejnovější denní stránku {% endcomment %}
  <script>
    window.location.href = '/tech-news/{{ site.tech_news[0].publishedAt | date: '%Y-%m-%d' }}/';
  </script>
{% else %}
  {% comment %} Zobrazit články {% endcomment %}
  {% assign recent_articles = recent_articles | sort: 'importance' | reverse | limit: 18 %}

  <!-- Navigace -->
  <div class="tech-news-navigation">
    <a href="/tech-news/archive/">📚 Archiv</a>
  </div>

  <!-- Články... -->
{% endif %}
```

**3. Stránka archivu** `/tech-news/archive/`:
- Seznam denních stránek
- Kalendářové zobrazení
- Filtr podle měsíce

---

## 📊 Srovnání řešení

| Kritérium | Řešení A | Řešení B | Řešení C |
|-----------|----------|----------|----------|
| **Velikost HTML** | ~100-200 KB | ~10 KB (redirect) | ~100-200 KB |
| **Build čas** | Střední | Rychlý | Střední |
| **Funkčnost** | ✅ Plná | ⚠️ Omezená | ✅ Plná |
| **Uživatelský zážitek** | ✅ Dobrý | ⚠️ Redirect delay | ✅ Výborný |
| **Údržba** | Střední | Nízká | Vyšší |
| **Implementace** | ⚙️ Jednoduchá | 🚀 Velmi jednoduchá | ⚙️ Složitější |

## 🎯 Doporučení

**Pro okamžité řešení:** **Řešení A** (Cleanup + Filtrace)
- ✅ Řeší hlavní problémy
- ✅ Rychlá implementace
- ✅ Zachovává funkcionalitu
- ✅ Automatický maintenance

**Pro dlouhodobé řešení:** **Řešení C** (Kombinované)
- ✅ Nejrobustnější
- ✅ Nejlepší UX
- ✅ Archiv pro historii
- ✅ Fallback mechanismy

## 📋 Implementační kroky

### Krok 1: Cleanup script
1. Vytvořit `.github/scripts/cleanup_old_tech_news.py`
2. Otestovat lokálně
3. Přidat do workflow

### Krok 2: Aktualizovat layout
1. Upravit `_layouts/tech_news_index.html`
2. Přidat filtraci podle data
3. Otestovat s malým počtem článků

### Krok 3: Deploy
1. Commitnout změny
2. Pushnout do GitHubu
3. Ověřit workflow

### Krok 4: Monitoring
1. Zkontrolovat velikost HTML
2. Měřit build čas
3. Sledovat počet článků v kolekci

## 🔧 Technické detaily

### Jekyll Collection Limits
- Jekyll nemá vestavěný limit pro kolekce
- Všechny dokumenty se načítají do paměti
- Filtrace Liquid je pomalá pro velké kolekce

### Liquid Date Filtering
```liquid
{% assign now_timestamp = 'now' | date: '%s' | to_integer %}
{% assign article_timestamp = article.publishedAt | date: '%s' | to_integer %}
{% if article_timestamp >= cutoff_timestamp %}
  <!-- Článek je dostatečně nový -->
{% endif %}
```

### Cleanup Considerations
- **7 dní:** Optimální pro archiv + aktuální zobrazení
- **Denní stránky:** Zachovávají historii
- **Build čas:** ~50% redukce při cleanup

## 📈 Očekávané výsledky

**Po implementaci Řešení A:**
- Velikost HTML: **6.4 MB → ~150 KB** (-98%)
- Počet článků: **2,478 → ~100-200** (-92%)
- Build čas: **~3-5 min → ~1-2 min** (-50%)
- Načítání stránky: **~5-10s → <1s** (-90%)

**Po implementaci Řešení C:**
- Stejné výsledky jako A
- Plus: Archiv, lepší navigace, fallback
