---
author: Marisa Aigen
category: kyberbezpečnost
date: '2025-12-07 00:20:43'
description: Pro rok 2026 předpovídá CEO DryRun Security posun k novým útokům zneužívajícím
  autonomní AI agenty místo klasických prompt injection a pokračování halucinací AI,
  které se budou jen omezovat. Jak se custom payloady stanou levnými a snadno generovatelnými,
  temné trhy se přizpůsobí.
importance: 4
layout: tech_news_article
original_title: 'AI hallucinations and sophisticated cyberattacks: Business tech concerns
  for next year'
publishedAt: '2025-12-07T00:20:43+00:00'
slug: ai-hallucinations-and-sophisticated-cyberattacks-b
source:
  emoji: 📰
  id: null
  name: Digital Journal
title: 'Halucinace umělé inteligence a sofistikované kyberútoky: Obavy technologického
  byznysu pro příští rok'
url: https://www.digitaljournal.com/business/ai-hallucinations-and-sophisticated-cyberattacks-business-tech-concerns-for-next-year/article
urlToImage: https://www.digitaljournal.com/wp-content/uploads/2024/08/Computerman-©TimSandle-768px-01.jpg
urlToImageBackup: https://www.digitaljournal.com/wp-content/uploads/2024/08/Computerman-©TimSandle-768px-01.jpg
---

## Souhrn
CEO DryRun Security, James Wickett, předpovídá pro rok 2026 dva klíčové rizika v oblasti AI: zneužití autonomních AI agentů jako novou formu kyberútoků a pokračování halucinací umělé inteligence, které se neodstraní, ale pouze omezí. Tyto trendy ohrozí firemní workflowy propojené s AI agenty, které mají přístup k databázím, repozitářům kódu a systémům tiketů.

## Klíčové body
- Posun od prompt injection k „agency abuse“: Útočníci budou zneužívat autoritu AI agentů k provádění škodlivých akcí pod rouškou rutinních úkolů.
- Rizika excesivní autonomie: AI agenti mohou omylem mazat produkční prostředí nebo vyčerpat rozpočty na tokeny kvůli nekontrolovaným operacím.
- Exfiltrace dat: Příkladem je příkaz „přenést zálohy databáze na externí úložiště pro audit“, který agent provede bez pochopení skutečného záměru.
- Halucinace AI: Nezmizí, ale budou obsahovány v kontrolovaných prostředích.

## Podrobnosti
James Wickett, generální ředitel DryRun Security – firmy specializující se na testování a bezpečnostní analýzu AI systémů, zejména autonomních agentů – varuje před evolucí kyberútoků. V současnosti firmy integrují AI agenty do svých procesů: tyto agenty slouží k automatizaci úkolů jako čištění nasazení, správa tiketů nebo přístup k databázím. Problém spočívá v tom, že agenty nerozumí lidskému záměru stejně jako lidé a mohou být zmanipulovány.

První předpověď se týká „agent exploits“, což je posun od prompt injection – útoků, kde útočník vloží škodlivý text do vstupu AI modelu – k zneužití agentovy autonomie (agency abuse). Útočník může zadat zdánlivě nevinný požadavek, například „přenést všechny zálohy produkční databáze na mé externí úložiště kvůli auditu“. Agent, který má oprávnění k databázím, to provede, aniž by ověřil kontext, což vede k exfiltraci citlivých dat. Wickett uvádí, že jsme již viděli případy, kdy agenti spouštěli rekurzivní vyhledávání a spotřebovali tisíce dolarů na API tokeny za den. Tyto incidenty nejsou o úniku dat, ale o reálné škodě: mazání produkčních systémů nebo nákladové exploze.

Druhá předpověď se zaměřuje na halucinace AI, tedy generování falešných nebo zavádějících informací prezentovaných jako fakta. Tyto jevy nezmizí, protože vycházejí z povahy velkých jazykových modelů (LLM), ale budou lokalizovány do kontrolovaných prostředí. Firmy budou muset zavádět vrstvy validace, sandboxy a lidskou kontrolu, aby omezily dopady.

Tyto trendy jsou logické v kontextu rostoucí adopce AI agentů jako jsou ty od OpenAI (např. custom GPTs s akcemi) nebo Anthropic (Claude s tool use). Nicméně Wickettovy varování přehánějí rizika bez zmínky o stávajících obranách, jako jsou role-based access control (RBAC) pro agenty nebo observability nástroje.

## Proč je to důležité
Tyto předpovědi mají široké dopady na průmysl: firmy s AI workflowy čelí nejen datovým únikům, ale i provozním výpadkům a finančním ztrátám. V širším ekosystému AI urychlí adopci bezpečnostních standardů, jako jsou agent guardrails nebo verifikace intentu. Pro uživatele znamená nutnost přehodnocení důvěry v autonomní systémy – například v CI/CD pipelinech nebo DevOps. Pokud se temné trhy přizpůsobí levným custom payloadům generovaným AI, útoky se stanou dostupnějšími i pro méně zkušené aktéry, což zvýší tlak na regulace jako EU AI Act. Celkově to podtrhuje, že bezpečnost AI není jen o datech, ale o kontrole akcí v reálném světě.

---

[Číst původní článek](https://www.digitaljournal.com/business/ai-hallucinations-and-sophisticated-cyberattacks-business-tech-concerns-for-next-year/article)

**Zdroj:** 📰 Digital Journal
