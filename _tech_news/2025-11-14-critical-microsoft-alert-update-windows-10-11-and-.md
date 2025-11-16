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
title: Kritické varování od Microsoftu – okamžitě aktualizujte Windows 10, 11 a Server
url: https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn
Microsoft vydal naléhavé bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti v jádru operačního systému Windows. Chyba označená jako CVE-2025-62215 umožňuje útočníkům eskalovat oprávnění a získat plnou kontrolu nad systémem. Odborníci doporučují okamžitou aktualizaci všech zařízení s Windows 10, 11 i Windows Server.

## Klíčové body
- Zranitelnost CVE-2025-62215 je zero-day v jádru Windows a je již aktivně zneužívána v reálných útocích.
- Útočníci pravděpodobně využívají tuto chybu až po počátečním průniku do systému (např. phishingem).
- Microsoft vydal opravu v rámci mimořádného bezpečnostního updatu mimo standardní cyklus Patch Tuesday.
- Zranitelnost vyžaduje splnění tzv. race condition, což komplikuje, ale neznemožňuje zneužití.
- Současně s tímto upozorněním Microsoft opravil dalších 62 zranitelností, z nichž některé jsou také kritické.

## Podrobnosti
Zranitelnost CVE-2025-62215 se nachází v jádru (kernel) operačního systému Windows a jedná se o chybu typu privilege escalation – tedy zvýšení oprávnění. Podle Satnama Naranga, senior staff research engineer ve společnosti Tenable (bezpečnostní firma specializující se na správu rizik a zranitelností), byla tato chyba potvrzena jako aktivně zneužívaná „in the wild“, tedy v reálných kybernetických útocích. I když její zneužití vyžaduje splnění race condition – situace, kdy více procesů soupeří o přístup ke sdílenému prostředku – útočníci ji pravděpodobně využívají až po získání počátečního přístupu do systému prostřednictvím phishingových e-mailů nebo jiných vektorů.

Microsoft reagoval vydáním mimořádného bezpečnostního updatu, který doplňuje běžný měsíční cyklus oprav známý jako Patch Tuesday. Uživatelé systémů Windows 10, 11 i serverových verzí by měli co nejdříve nainstalovat nejnovější aktualizace prostřednictvím Nastavení → Aktualizace a zabezpečení. Selhání v aktualizaci může vést k plné kompromitaci systému, včetně možnosti instalace škodlivého softwaru, krádeže dat nebo vytvoření botnetu.

## Proč je to důležité
Tato událost patří mezi nejzávažnější bezpečnostní incidenty v ekosystému Windows v posledních letech. Zero-day zranitelnosti v jádru operačního systému jsou extrémně nebezpečné, protože umožňují obejít většinu běžných bezpečnostních mechanismů. Skutečnost, že je chyba již aktivně zneužívána, zvyšuje naléhavost reakce. Pro podniky i běžné uživatele to znamená bezprostřední riziko kompromitace zařízení. V širším kontextu ukazuje tato událost na rostoucí sofistikaci útočníků i na zranitelnost základních komponent moderních operačních systémů, což má dopad na celkovou důvěru v digitální infrastrukturu.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
