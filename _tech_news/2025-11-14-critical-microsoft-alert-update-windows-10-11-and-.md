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
Microsoft vydal naléhavé bezpečnostní upozornění kvůli kritické zero-day zranitelnosti CVE-2025-62215 v jádru operačního systému Windows. Tato chyba je již aktivně zneužívána útočníky k eskalaci oprávnění na úroveň systému. Aktualizace jsou k dispozici pro Windows 10, 11 i Windows Server a je nutné je nainstalovat co nejdříve.

## Klíčové body
- Zranitelnost CVE-2025-62215 se nachází v jádru Windows a umožňuje eskalaci oprávnění.
- Microsoft potvrdil aktivní zneužívání této chyby v reálném prostředí („in the wild“).
- Útočníci pravděpodobně využívají tuto zranitelnost až po počátečním průniku do systému (např. phishingem).
- Aktualizace jsou součástí nejnovějších bezpečnostních záplat vydaných v rámci Patch Tuesday.
- Tenable a další bezpečnostní analytici varují před vysokým rizikem pro neaktualizované systémy.

## Podrobnosti
Zranitelnost CVE-2025-62215 je chybou typu „race condition“ v jádru Windows, která umožňuje útočníkovi získat oprávnění na úrovni systému (SYSTEM). Podle Satnama Naranga, senior staff research engineer ve společnosti Tenable (bezpečnostní firma specializující se na detekci hrozeb a správu zranitelností), je tato chyba pravděpodobně využívána v rámci tzv. post-exploitation – tedy po tom, co útočník již získal počáteční přístup do systému, například prostřednictvím phishingové kampaně nebo jiné zranitelnosti. I když využití chyby vyžaduje splnění specifických podmínek (vyhrát „závod“ mezi procesy), skutečnost, že je již aktivně zneužívána, zvyšuje její nebezpečí na maximum. Microsoft vydal opravu v rámci nejnovější sady bezpečnostních aktualizací, které řeší celkem 63 zranitelností, z nichž tato je nejkritičtější.

## Proč je to důležité
Jádro operačního systému (kernel) je nejcitlivější částí Windows – kompromitace jádra znamená plnou kontrolu nad celým zařízením. Zero-day zranitelnosti v jádru jsou extrémně vzácné a zároveň nebezpečné, protože neexistuje žádná ochrana před jejich zneužitím, dokud není vydána záplata. Tato situace je typickým příkladem „bezpečnostní krize“ podle kritérií důležitosti – jde o aktivně zneužívanou chybu v kritické infrastruktuře, která ohrožuje miliony uživatelů i podnikové systémy. Pro organizace i běžné uživatele je nezbytné okamžitě nainstalovat aktualizace, protože zpoždění může vést ke kompromitaci dat, šíření malware nebo trvalému přístupu útočníků do sítě.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
