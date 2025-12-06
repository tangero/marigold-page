---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Netskope
date: '2025-12-01 23:15:07'
description: Společnost Netskope oznámila nové bezpečnostní funkce pro Model Context
  Protocol v platformě Netskope One. Tyto nástroje umožňují organizacím objevovat
  MCP servery, hodnotit rizika a řídit přístup AI agentů k podnikovým zdrojům bezpečně.
importance: 3
layout: tech_news_article
original_title: Netskope adds MCP security controls to protect enterprise AI agents
publishedAt: '2025-12-01T23:15:07+00:00'
slug: netskope-adds-mcp-security-controls-to-protect-ent
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Netskope přidává bezpečnostní kontroly pro MCP k ochraně podnikových AI agentů
url: https://siliconangle.com/2025/12/01/netskope-adds-mcp-security-controls-protect-enterprise-ai-agents/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/netskope.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/netskope.png
---

## Souhrn
Společnost Netskope, která se specializuje na bezpečnost cloudových služeb, představila nové bezpečnostní mechanismy pro Model Context Protocol (MCP) v rámci své platformy Netskope One. MCP je vycházející standard, který umožňuje AI agentům přímé připojení k podnikovým datům, nástrojům a pracovním postupům, což přináší nová bezpečnostní rizika, zejména kvůli tisícům veřejně dostupných MCP serverů. Novinky pomáhají organizacím přecházet od experimentálních nasazení AI agentů k produkčnímu využití s lepší viditelností a kontrolou.

## Klíčové body
- Automatické objevování a identifikace MCP serverů i klientů v podnikových sítích s podrobnými metadaty (hostitel, identita, verze).
- Hodnocení rizik pomocí Cloud Confidence Index pro posouzení bezpečnostní úrovně MCP nástrojů.
- Granularní zásadní kontroly pro MCP provoz, včetně blokování neautorizovaného přístupu k podnikovým zdrojům.
- Real-time inspekce MCP relací, detekce provozu typického pro AI agenty a úplné logování událostí pro audit.
- Vestavěná prevence úniku dat (DLP) pro detekci citlivých informací.

## Podrobnosti
Model Context Protocol (MCP) slouží k tomu, aby AI agenti – autonomní systémy schopné vykonávat úkoly za uživatele – mohli bezpečně interagovat s podnikovými systémy. Například agent může přistupovat k databázím pro analýzu dat, spouštět workflow v CRM systémech nebo integrovat externí nástroje jako Slack či GitHub. Problém nastává s rychlým růstem tohoto standardu: existují tisíce veřejných MCP serverů, což zvyšuje riziko nechtěného přístupu k citlivým datům nebo zneužití agentů.

Platforma Netskope One, která monitoruje cloudový provoz a sítě, nyní automaticky detekuje tyto komponenty v podnikovém prostředí. Poskytuje metadata jako IP adresy hostitelů, atributy identit uživatelů a verze protokolu, což umožňuje bezpečnostním týmům přesně lokalizovat aktivity AI agentů. Dále přichází risk scoring založený na Cloud Confidence Indexu – indexu, který Netskope používá k hodnocení důvěryhodnosti cloudových služeb na základě historických dat o bezpečnosti, konfiguracích a známých zranitelnostech. Tím organizace rychle identifikují rizikové MCP integrace.

Klíčovou novinkou jsou granularní policy controls: týmy definují pravidla typu „povolit agent X přístup k databázi Y pouze v pracovní době“ nebo „blokovat všechny neznámé MCP klienty“. Platforma provádí real-time inspekci relací, rozpoznává netypické provozové vzorce (např. vysokou frekvenci dotazů typickou pro AI) a loguje vše pro forenzní analýzy. DLP funkce navíc skenuje obsah a blokuje úniky citlivých dat, jako jsou osobní údaje nebo obchodní tajemství. Tyto nástroje jsou integrovány do existující Netskope infrastruktury, což usnadňuje nasazení bez nutnosti nového hardware.

## Proč je to důležité
V éře agentického AI, kde agenti přecházejí z prototypů do produkce, MCP urychluje adopci, ale zároveň exponuje podniky novým hrozbám – od neautorizovaného přístupu po supply-chain útoky přes veřejné servery. Netskope řeší mezeru v tradiční bezpečnosti, která se zaměřuje na lidi, ne na autonomní agenty. Pro průmysl to znamená lepší governance AI nasazení, snížení rizik compliance (GDPR, HIPAA) a podporu skalování bezpečně. Kriticky řečeno, není to univerzální řešení – závisí na kvalitě Netskope sítě a neřeší rizika uvnitř samotných AI modelů –, ale posiluje perimetrální ochranu v rostoucím ekosystému MCP.

---

[Číst původní článek](https://siliconangle.com/2025/12/01/netskope-adds-mcp-security-controls-protect-enterprise-ai-agents/)

**Zdroj:** 📰 SiliconANGLE News
