---
layout: post
title: "Cursor vylepšuje Codebase Indexing - rychlejší pochopení projektu"
date: 2025-01-19
thumbnail: "https://www.marigold.cz/assets/cursor-indexing.jpg"
hide: true
---

Nejnovější aktualizace Cursor přináší výrazně vylepšený systém indexování kódu, který umožňuje AI rychleji a přesněji rozumět struktuře a kontextu celého projektu.

## Co je Codebase Indexing?

Codebase Indexing je pokročilý systém, který:
- **Analyzuje celý projekt** - mapuje všechny soubory, závislosti a vztahy
- **Vytváří semantic embeddings** - porozumí významu kódu, nejen syntaxi
- **Cachuje znalosti** - rychlejší responses díky pre-processed informacím
- **Real-time updates** - automaticky aktualizuje index při změnách

## Nové funkce v indexování:

### Intelligent Parsing
- **Multi-language support** - jednotný přístup pro všechny jazyky
- **Framework detection** - automaticky rozpozná React, Vue, Angular atd.
- **Architecture mapping** - identifikuje design patterns a struktury
- **Dependency graph** - mapuje všechny závislosti a importy

### Semantic Understanding
```javascript
// AI nyní rozumí nejen syntaxi, ale i významu:
function calculateUserMetrics(user) {
  // AI ví, že toto je business logic
  // souvisí s user management
  // a pravděpodobně ovlivňuje analytics
}
```

### Advanced Search Capabilities
- **Semantic search** - "najdi všechny funkce pro user authentication"
- **Intent-based queries** - "kde se handleuje error při platbě?"
- **Cross-file relationships** - "které komponenty používají tuto utility?"
- **Impact analysis** - "co ovlivní změna této funkce?"

## Performance vylepšení:

### Rychlost indexování:
- **50% rychlejší** - optimalizované algoritmy
- **Parallel processing** - využití všech CPU cores
- **Incremental updates** - pouze změněné části
- **Smart caching** - inteligentní cache management

### Memory optimalizace:
- **Reduced RAM usage** - efektivnější data structures
- **Compression** - komprimované indexy
- **Selective loading** - načítá jen potřebné části
- **Garbage collection** - automatické čištění nepotřebných dat

## Praktické výhody:

### Pro malé projekty (< 100 souborů):
- ⚡ **Instant responses** - okamžité AI odpovědi
- 🎯 **Perfect context** - AI rozumí 100% kódu
- 🔍 **Deep insights** - detailní analýza architektury

### Pro střední projekty (100-1000 souborů):
- ⚡ **Sub-second responses** - odpovědi pod 1 sekunda
- 🎯 **Selective context** - relevantní části pro daný dotaz
- 🔍 **Pattern recognition** - identifikace common patterns

### Pro velké projekty (1000+ souborů):
- ⚡ **Fast responses** - odpovědi do 3 sekund
- 🎯 **Smart filtering** - pouze relevantní kód
- 🔍 **Module isolation** - práce s jednotlivými moduly

## Nové AI capabilities díky indexingu:

### Code Navigation
```
"Vysvětli mi flow dat v této e-commerce aplikaci"
```
AI dokáže:
- Projít celý data flow od API po UI
- Identifikovat všechny transformace
- Najít potenciální bottlenecky
- Navrhnout optimalizace

### Architecture Analysis
```
"Je tato aplikace připravená na škálování?"
```
AI analyzuje:
- Coupling mezi moduly
- Single points of failure
- Performance bottlenecks
- Scalability patterns

### Security Audit
```
"Najdi potenciální security vulnerabilities"
```
AI kontroluje:
- Input validation
- Authentication flows
- Authorization checks
- Data exposure risks

## Konfigurace a customizace:

### .cursor/settings.json
```json
{
  "codebaseIndexing": {
    "enabled": true,
    "indexingDepth": "full",
    "excludePatterns": [
      "node_modules/**",
      "*.test.*",
      "coverage/**"
    ],
    "includeComments": true,
    "semanticAnalysis": true
  }
}
```

### Indexing priorities:
1. **Core business logic** - nejvyšší priorita
2. **API endpoints** - střední priorita  
3. **UI components** - střední priorita
4. **Tests & configs** - nízká priorita
5. **Generated code** - minimální priorita

## Troubleshooting:

### Pomalé indexování:
- **Exclude large files** - node_modules, build folders
- **Use .cursorignore** - podobně jako .gitignore
- **Restart indexing** - Cmd/Ctrl + Shift + P > "Reindex Codebase"

### Neprésní AI responses:
- **Update index** - ujistěte se, že je aktuální
- **Check file inclusion** - možná jsou některé soubory vyloučené
- **Provide more context** - přidejte specifické informace k dotazu

## Měření výkonu:

### Indexing metrics:
- **Index size**: Zobrazuje velikost indexu
- **Last updated**: Kdy byla poslední aktualizace
- **Coverage**: Procento indexovaného kódu
- **Performance**: Rychlost AI responses

```bash
# Cursor Developer Tools
Cmd/Ctrl + Shift + I > Console
> cursor.showIndexStats()
```

Toto vylepšení činí Cursor ještě mocnějším nástrojem pro práci s velkými a komplexními projekty, kde rychlé pochopení kontextu je klíčové. 