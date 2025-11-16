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
Microsoft vydal naléhavé bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti v jádru operačního systému Windows (CVE-2025-62215). Tato chyba umožňuje útočníkům získat nejvyšší systémová oprávnění a je již využívána v reálných kybernetických útocích. Uživatelé systémů Windows 10, 11 i Windows Server jsou vyzváni k okamžité aktualizaci.

## Klíčové body
- Zranitelnost CVE-2025-62215 je zero-day v jádru Windows a je již aktivně zneužívána.
- Útočníci pravděpodobně využívají tuto chybu pro eskalaci oprávnění po počátečním průniku do systému (např. přes phishing).
- Microsoft vydal opravu v rámci mimořádného bezpečnostního updatu mimo standardní cyklus Patch Tuesday.
- Odborníci z Tenable upozorňují, že zneužití vyžaduje výhru v tzv. race condition, což neznamená, že by hrozba byla méně vážná.
- Současně s tímto upozorněním Microsoft řeší dalších 62 zranitelností, z nichž některé jsou také kritické.

## Podrobnosti
Zranitelnost CVE-2025-62215 se nachází přímo v jádru (kernel) operačního systému Windows, což z ní činí zvláště nebezpečnou – úspěšný útok umožňuje útočníkovi získat plnou kontrolu nad systémem. Podle Satnama Naranga, senior staff research engineer ve společnosti Tenable (bezpečnostní firma specializující se na správu zranitelností), byla tato chyba potvrzena jako aktivně zneužívaná v reálném prostředí. Narang dále uvedl, že se pravděpodobně jedná o součást tzv. post-exploitation aktivity – tedy že útočníci nejprve získají omezený přístup (například přes phishingový e-mail nebo jinou zranitelnost) a následně využijí CVE-2025-62215 k eskalaci na úroveň systémového administrátora.

I když zneužití této chyby vyžaduje splnění specifických podmínek (tzv. race condition – situace, kdy útočník musí „předběhnout“ systém v časovém okně), skutečnost, že je již v terénu aktivně využívána, zvyšuje její rizikový profil. Microsoft proto vydal mimořádnou opravu mimo svůj běžný měsíční cyklus záplat (Patch Tuesday). Uživatelé by měli co nejdříve nainstalovat nejnovější bezpečnostní aktualizace prostřednictvím Windows Update nebo centrální správy v podnicích.

## Proč je to důležité
Tato zranitelnost představuje vážnou hrozbu pro miliony uživatelů po celém světě, včetně firem a kritické infrastruktury. Jádro operačního systému je nejcitlivější částí softwarového stacku – jakákoli chyba zde může vést k úplné kompromitaci zařízení. Skutečnost, že jde o zero-day (chyba neznámá vývojáři před jejím zneužitím) a že je již aktivně využívána, zvyšuje naléhavost reakce. Tento případ také ilustruje rostoucí agresivitu státních i kriminálních aktérů, kteří cíleně využívají nejnovější zranitelnosti dříve, než jsou opraveny. Pro organizace i běžné uživatele je klíčové mít zapnuté automatické aktualizace a pravidelně kontrolovat bezpečnostní stav svých systémů.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
