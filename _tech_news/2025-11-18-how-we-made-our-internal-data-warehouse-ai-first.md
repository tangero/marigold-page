---
author: Marisa Aigen
category: ai analýza
date: '2025-11-18 05:47:01'
description: Tým ClickHouse popisuje přechod svého interního datového skladu o velikosti
  2,1 PB z tradičního BI přístupu na platformu řízenou umělou inteligencí, která nyní
  pokrývá 70 % interních analytických požadavků.
importance: 3
layout: tech_news_article
original_title: How we made our internal data warehouse AI-first
publishedAt: '2025-11-18T05:47:01+00:00'
slug: how-we-made-our-internal-data-warehouse-ai-first
source:
  emoji: 📰
  id: null
  name: Clickhouse.com
title: Jak jsme přeměnili interní datový sklad na AI-first platformu
url: https://clickhouse.com/blog/ai-first-data-warehouse
urlToImage: https://clickhouse.com/_next/image?url=%2Fuploads%2FBlog_Banner_AI_first_Click_House_d082488b3c.jpg&w=1200&h=630&q=80
urlToImageBackup: https://clickhouse.com/_next/image?url=%2Fuploads%2FBlog_Banner_AI_first_Click_House_d082488b3c.jpg&w=1200&h=630&q=80
---

## Souhrn
Společnost ClickHouse převedla svůj interní datový sklad založený na tradičním business intelligence (BI) přístupu na architekturu řízenou umělou inteligencí (AI-first). Nová platforma umožňuje uživatelům získávat analytické poznatky bez nutnosti psát SQL dotazy a pokrývá již 70 % interních analytických úloh.

## Klíčové body
- Interní datový sklad obsahuje 2,1 PB komprimovaných dat a slouží více než 300 uživatelům.
- Původní BI workflow vyžadovalo ruční psaní komplexních SQL dotazů napříč více zdroji dat.
- Nová AI-first architektura umožňuje přirozený jazyk pro dotazování dat.
- Autor článku, dřívější skeptik AI, uznává výrazné zlepšení spolehlivosti a kontextového porozumění moderních LLM.
- Platforma využívá ClickHouse Cloud a vizualizační nástroj Superset.

## Podrobnosti
Původní přístup k analýze dat v ClickHouse byl typický pro tradiční datové sklady: inženýři museli ručně psát SQL dotazy, které spojovaly data z různých systémů – například metadata služeb z Control Plane, metriky výkonu z Data Plane, logy autoskalování a záznamy z CRM systému Salesforce. Tento proces byl časově náročný a vyžadoval hlubokou znalost schémat a obchodní logiky. Nová AI-first architektura umožňuje uživatelům klást otázky v přirozeném jazyce, přičemž systém automaticky generuje a spouští odpovídající SQL dotazy. Klíčovým posunem je schopnost modelu porozumět kontextu dotazu, správně interpretovat obchodní metriky a minimalizovat tzv. halucinace – falešné nebo nesmyslné odpovědi, které dřívější LLM často generovaly. Platforma stále využívá ClickHouse jako výkonný analytický databázový engine a Superset pro vizualizaci, ale mezi uživatele a tyto nástroje byla vložena AI vrstva, která zprostředkovává interakci.

## Proč je to důležité
Tento případ ukazuje, že AI-first přístup už není jen experimentem, ale praktickým řešením pro zrychlení datové analýzy v podnicích. Zatímco dřívější pokusy s LLM a daty selhávaly kvůli nespolehlivosti, moderní systémy s lepším kontextovým porozuměním a integrací s existující infrastrukturou začínají přinášet reálné výhody. Pro průmysl to znamená možnost demokratizovat přístup k datům – nejen analytici, ale i produktoví manažeři nebo inženýři mohou rychle získávat odpovědi bez specializovaných dovedností. Zároveň to však klade vysoké nároky na kvalitu metadat, správu datových zdrojů a bezpečnostní opatření proti neoprávněnému přístupu k citlivým informacím.

---

[Číst původní článek](https://clickhouse.com/blog/ai-first-data-warehouse)

**Zdroj:** 📰 Clickhouse.com
