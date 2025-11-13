---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
- BleepingComputer
date: '2025-11-11 18:45:29'
description: Microsoft v rámci listopadového Patch Tuesday 2025 vydal bezpečnostní
  aktualizace řešící 63 zranitelností, včetně jedné aktivně zneužívané zero-day chyby
  v jádře Windows, a upozorňuje na nutnost řešit podporu a zabezpečení Windows 10.
importance: 3
layout: tech_news_article
original_title: Microsoft November 2025 Patch Tuesday fixes 1 zero-day, 63 flaws -
  BleepingComputer
publishedAt: '2025-11-11T18:45:29+00:00'
slug: microsoft-november-2025-patch-tuesday-fixes-1-zero
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Listopadové záplaty Microsoftu opravují 63 zranitelností a jednu aktivně zneužívanou
  zero-day chybu
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
---

## Souhrn
Microsoft v listopadovém Patch Tuesday 2025 zveřejnil aktualizace opravující 63 zranitelností v produktech Windows, z toho jednu aktivně zneužívanou zero-day chybu v jádře systému. Součástí balíku jsou také čtyři kritické zranitelnosti a první vlna rozšířené bezpečnostní podpory (ESU) pro Windows 10.

## Klíčové body
- Opraveno 63 zranitelností, včetně jedné aktivně zneužívané zero-day v jádře Windows.
- Čtyři kritické chyby: dvě umožňují vzdálené spuštění kódu (RCE), jedna eskalaci oprávnění a jedna únik informací.
- Dominují zranitelnosti typu elevation of privilege a remote code execution, které útočníkům běžně slouží ke kompletnímu převzetí systému.
- Zahájení Extended Security Updates (ESU) pro Windows 10, nutnost přechodu na Windows 11 nebo zapojení do ESU programu.
- Microsoft vydal mimořádnou aktualizaci kvůli chybě, která bránila registraci do ESU.

## Podrobnosti
Listopadové záplaty se zaměřují na široké spektrum slabin v ekosystému Windows. Z celkových 63 zranitelností je 29 typu elevation of privilege, které umožňují útočníkovi získat vyšší oprávnění v systému, typicky přechod z běžného uživatele na správce. Tato kategorie je kritická zejména v prostředích, kde útočník již získal počáteční přístup (například pomocí phishingu) a potřebuje rozšířit kontrolu nad systémem či sítí.

Dále bylo opraveno 16 zranitelností vedoucích k remote code execution (RCE), tedy vzdálenému spuštění škodlivého kódu bez nutnosti fyzického přístupu. Tyto chyby patří k nejvyužívanějším v reálných útocích, protože umožňují kompromitovat servery, pracovní stanice nebo aplikační služby typicky prostřednictvím škodlivých dokumentů, síťových požadavků či služeb naslouchajících na otevřených portech. Opraveno bylo také 11 slabin typu information disclosure, 3 denial of service a 2 spoofing, které mohou podpořit průzkum infrastruktury, obcházení autentizace nebo znepřístupnění služeb.

Zásadní je jedna aktivně zneužívaná zero-day zranitelnost v jádře Windows. Jádro je nejprivilegovanější vrstva systému; zneužití chyby v této úrovni typicky umožní obejít bezpečnostní mechanismy, skrýt aktivitu útočníka a udržet trvalý přístup. Proto je instalace aktuálních záplat okamžitě po jejich dostupnosti nutností, zejména v podnikových prostředích.

Pro Windows 10 Microsoft spustil program Extended Security Updates (ESU), který poskytuje placené bezpečnostní aktualizace pro organizace, jež stále provozují nepodporovanou verzi systému. Současně byla vydána mimořádná aktualizace řešící chybu bránící některým zákazníkům v registraci do ESU. Microsoft tím nepřímo tlačí na migraci na Windows 11, případně na formální zapojení do ESU, protože ponechání Windows 10 bez podpory otevírá prostor pro masové kompromitace.

## Proč je to důležité
Tato vlna záplat má přímý dopad na bezpečnost firemních infrastruktur i domácích uživatelů. Aktivně zneužívaná zero-day v jádře Windows znamená, že existují reálné útoky, které tyto slabiny využívají dříve, než jsou plně nasazeny opravy. Organizace, které odkládají aktualizace, tím poskytují útočníkům časové okno k útoku.

Struktura zranitelností – převaha elevation of privilege a RCE – potvrzuje dlouhodobý trend: útoční řetězce kombinují počáteční průnik (např. phishing, zneužití aplikace) s následnou eskalací oprávnění a laterálním pohybem v síti. V prostředí, kde se masivně používají AI nástroje, cloudové služby a automatizované nasazování, jakékoli neaktualizované Windows uzly zůstávají nejslabším článkem. Pro správce IT je proto klíčové: mít automatizovaný patch management, validovat aplikaci těchto záplat ve výrobních systémech a aktivně řešit odchod z Windows 10 mimo ESU, aby se minimalizovalo riziko dlouhodobě zranitelných stanic a serverů.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/)

**Zdroj:** 📰 BleepingComputer
