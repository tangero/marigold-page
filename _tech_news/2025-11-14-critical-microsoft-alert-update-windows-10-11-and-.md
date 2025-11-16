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
title: Kritické varování od Microsoftu – okamžitě aktualizujte Windows 10, 11 i Server
url: https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn
Microsoft vydal naléhavé bezpečnostní upozornění kvůli kritické zero-day zranitelnosti CVE-2025-62215 v jádru operačního systému Windows. Tato chyba je již aktivně zneužívána útočníky k eskalaci oprávnění na úroveň systému. Aktualizace je nutná pro všechny uživatele Windows 10, 11 i Windows Server.

## Klíčové body
- Zranitelnost CVE-2025-62215 se nachází v jádru Windows a umožňuje získání systémových oprávnění.
- Microsoft potvrdil aktivní zneužívání této chyby v reálném prostředí („in the wild“).
- Útočníci pravděpodobně tuto zranitelnost využívají až po počátečním průniku do systému, například prostřednictvím phishingu.
- Aktualizace byla vydána mimo standardní cyklus Patch Tuesday kvůli naléhavosti hrozby.
- Současně s tímto upozorněním Microsoft řeší dalších 62 zranitelností, z nichž některé jsou také kritické.

## Podrobnosti
Zranitelnost CVE-2025-62215 je chybou typu „race condition“ v jádru Windows, což znamená, že útočník musí správně načasovat své akce, aby úspěšně zneužil chování systému. I přes tuto technickou náročnost již byly zaznamenány reálné útoky. Podle Satnama Naranga, senior staff research engineer z Tenable (bezpečnostní společnosti specializující se na správu rizik a zranitelností), se jedná o typický příklad post-exploitační aktivity – tedy krok, který útočník provádí po získání počátečního přístupu do systému (např. prostřednictvím škodlivého e-mailu nebo jiné zranitelnosti). Tímto způsobem si zajistí plnou kontrolu nad počítačem. Microsoft vydal opravu mimo svůj běžný měsíční cyklus zabezpečovacích aktualizací, což podtrhuje závažnost situace. Uživatelé by měli co nejdříve nainstalovat nejnovější aktualizace prostřednictvím Windows Update nebo pomocí nástrojů pro správu podnikových systémů.

## Proč je to důležité
Tato zranitelnost představuje vážné riziko pro miliony zařízení po celém světě, včetně firemních serverů a kritické infrastruktury. Jádro operačního systému je nejcitlivější vrstvou – jakákoli chyba zde může vést k úplné kompromitaci systému. Skutečnost, že je chyba již aktivně zneužívána, zvyšuje naléhavost reakce. V kontextu širšího bezpečnostního prostředí se jedná o další příklad rostoucího tlaku na dodavatele softwaru, aby reagovali rychleji na hrozby mimo plánované cykly. Pro uživatele i organizace je klíčové mít zapnuté automatické aktualizace a pravidelně kontrolovat stav zabezpečení svých systémů.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
