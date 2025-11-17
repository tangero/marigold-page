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
Microsoft vydal naléhavé bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti v jádru operačního systému Windows (CVE-2025-62215). Tato chyba umožňuje útočníkům získat nejvyšší systémová oprávnění a je již využívána v reálných útocích. Uživatelé systémů Windows 10, 11 i Windows Server jsou vyzváni k okamžité aktualizaci.

## Klíčové body
- Zranitelnost CVE-2025-62215 je umístěna v jádru Windows a umožňuje eskalaci oprávnění.
- Microsoft potvrdil aktivní zneužívání této chyby v reálném prostředí („in the wild“).
- Útočníci pravděpodobně využívají tuto zranitelnost až po počátečním průniku do systému (např. phishingem).
- Aktualizace je k dispozici prostřednictvím standardního mechanismu Windows Update.
- Současně s tímto upozorněním Microsoft opravil celkem 63 dalších zranitelností.

## Podrobnosti
Zranitelnost CVE-2025-62215 je typu „race condition“ v jádru Windows, což znamená, že útočník musí využít přesně načasovanou sekvenci operací, aby získal kontrolu nad systémem. I přes tuto technickou náročnost již byly zaznamenány skutečné útoky, které tuto chybu využívají. Podle Satnama Naranga, senior staff research engineer ve společnosti Tenable (bezpečnostní firma specializující se na správu rizik a zranitelností), se jedná o klasický případ post-explotační aktivity — útočník nejprve získá základní přístup do systému (například prostřednictvím phishingové kampaně) a následně využije tuto zranitelnost k eskalaci na úroveň SYSTEM, což mu umožní plnou kontrolu nad počítačem.

Microsoft zveřejnil opravu v rámci mimořádného bezpečnostního updatu mimo standardní cyklus Patch Tuesday, což podtrhuje závažnost hrozby. Uživatelé by měli co nejdříve nainstalovat nejnovější aktualizace prostřednictvím Windows Update nebo pomocí nástrojů pro správu podnikových sítí (např. WSUS nebo Intune).

## Proč je to důležité
Tato zranitelnost představuje vážné riziko pro miliony uživatelů i podnikové infrastruktury po celém světě. Jádro operačního systému je nejcitlivější částí systému — kompromitace této vrstvy umožňuje obejít všechny ostatní bezpečnostní mechanismy, včetně izolace procesů a ochrany paměti. Vzhledem k tomu, že útočníci již tuto chybu aktivně využívají, jde o bezpečnostní krizi vyžadující okamžitou reakci. Podobné události v minulosti (např. EternalBlue) ukázaly, jak rychle se mohou šířit útoky využívající zranitelnosti jádra, zejména v prostředí, kde nejsou systémy pravidelně aktualizovány.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
