---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-11-14 14:58:04'
description: Microsoft potvrdil aktivně zneužívanou zero-day zranitelnost v jádru
  Windows, která umožňuje útočníkům získat systémová oprávnění. Uživatelé musí co
  nejdříve nainstalovat bezpečnostní záplatu.
importance: 5
layout: tech_news_article
original_title: Critical Microsoft Alert — Update Windows 10, 11 And Server Right
  Now - Forbes
publishedAt: '2025-11-14T14:58:04+00:00'
slug: critical-microsoft-alert-update-windows-10-11-and-
source:
  emoji: 💼
  id: null
  name: Forbes
title: Kritické varování od Microsoftu — okamžitě aktualizujte Windows 10, 11 a Server
url: https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn
Microsoft vydal naléhavé bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti v jádru operačního systému Windows. Tato chyba, označená jako CVE-2025-62215, umožňuje útočníkům eskalovat svá oprávnění na úroveň systému. Odborníci doporučují okamžitou aktualizaci všech systémů Windows 10, 11 i Windows Server.

## Klíčové body
- Zranitelnost CVE-2025-62215 je aktivně zneužívána v reálném prostředí.
- Jedná se o chybu v jádru Windows (Windows Kernel) umožňující eskalaci oprávnění.
- Microsoft vydal opravu v rámci mimořádného bezpečnostního updatu mimo standardní cyklus Patch Tuesday.
- Útočníci pravděpodobně využívají tuto zranitelnost až po získání počátečního přístupu například prostřednictvím phishingu.
- Současně byla zveřejněna řada dalších 62 zranitelností, z nichž některé mají také vysokou závažnost.

## Podrobnosti
Zranitelnost CVE-2025-62215 byla identifikována jako tzv. race condition v jádru Windows, což znamená, že útočník může při určitém časovém sledu operací obejít bezpečnostní mechanismy a získat plná systémová oprávnění. Podle Satnama Naranga, senior staff research engineeru z firmy Tenable (specializující se na správu bezpečnostních rizik), je tato chyba pravděpodobně využívána v rámci tzv. post-exploitation fáze — tedy poté, co útočník získá počáteční přístup do systému jiným způsobem, například prostřednictvím phishingové kampaně nebo jiné zranitelnosti. Microsoft potvrdil, že existují důkazy o aktivním zneužívání této chyby v terénu. Aktualizace byla vydána mimořádně, což podtrhuje její naléhavost, a doporučuje se co nejdříve ji nasadit na všechny systémy, včetně firemních serverů.

## Proč je to důležité
Zero-day zranitelnosti v jádru operačního systému patří mezi nejzávažnější bezpečnostní hrozby, protože umožňují úplnou kontrolu nad zařízením. Vzhledem k tomu, že Windows dominuje na trhu desktopových i serverových systémů, má tato chyba potenciál ovlivnit miliony uživatelů a organizací po celém světě. Rychlá reakce Microsoftu a výzva k okamžité aktualizaci ukazují na vážnost situace. Pro firmy i běžné uživatele je klíčové neodkládat instalaci bezpečnostních záplat, protože zpoždění může vést ke kompromitaci dat, šíření malware nebo dokonce k úplné ztrátě kontroly nad systémem.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
