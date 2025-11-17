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
Microsoft vydal naléhavé bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti CVE-2025-62215 v jádru operačního systému Windows. Tato chyba umožňuje útočníkům eskalovat oprávnění a získat plnou kontrolu nad systémem. Odborníci doporučují okamžitou aktualizaci všech zařízení s Windows 10, 11 a Windows Server.

## Klíčové body
- Zranitelnost CVE-2025-62215 je zero-day chyba v jádru Windows (Windows Kernel) s potvrzeným zneužitím v reálném prostředí.
- Útočníci pravděpodobně využívají tuto chybu po počátečním průniku do systému, například prostřednictvím phishingu.
- Microsoft vydal opravu v rámci mimořádného bezpečnostního updatu mimo standardní cyklus Patch Tuesday.
- Zranitelnost vyžaduje splnění podmínky tzv. race condition, ale i přesto je považována za kritickou.
- Současně s tímto upozorněním Google vydal nouzovou opravu pro prohlížeč Chrome kvůli jiné závažné chybě.

## Podrobnosti
Zranitelnost CVE-2025-62215 byla identifikována jako chyba typu privilege escalation v jádru Windows. Podle Satnama Naranga, senior staff research engineer ve společnosti Tenable (bezpečnostní firma specializující se na správu rizik a zranitelností), útočníci ji využívají v rámci tzv. post-exploitation aktivity – tedy po získání počátečního přístupu do systému jinými prostředky, jako je phishing nebo jiná zranitelnost. I když využití chyby vyžaduje splnění race condition (soupeření vláken o zdroje v čase), což komplikuje útok, Microsoft potvrdil její aktivní zneužívání v terénu. Tento případ je mimořádný, protože jde o zero-day – tedy chybu, o které výrobce nevěděl před jejím zneužitím – a navíc se nachází v jádru operačního systému, což je nejcitlivější část softwaru. Microsoft reagoval vydáním mimořádného bezpečnostního updatu, který doporučuje nainstalovat všem uživatelům bez odkladu.

## Proč je to důležité
Tato událost podtrhuje zvýšenou hrozbu cílených útoků na infrastrukturu firem i domácích uživatelů. Jádro operačního systému je klíčovou součástí bezpečnosti celého systému – jeho kompromitace umožňuje obejít všechny další ochranné mechanismy. Skutečnost, že se jedná o zero-day s potvrzeným zneužitím, zvyšuje riziko rychlého šíření útoků, zejména v prostředí firemních sítí. Současné paralelní nouzové aktualizace od Microsoftu i Google ukazují na intenzivní bezpečnostní tlak, kterému čelí hlavní technologické platformy. Pro uživatele to znamená nutnost prioritního nasazení aktualizací a zvýšené ostražitosti vůči phishingovým pokusům, které mohou být bránou k využití této zranitelnosti.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
