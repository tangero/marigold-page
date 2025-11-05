---
author: Marisa Aigen
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-11-03 15:22:12'
description: Mimořádná bezpečnostní aktualizace KB5070881, která opravuje aktivně
  zneužívanou zranitelnost ve Windows Server Update Service, zablokovala funkci hotpatchingu
  na některých serverech s Windows Server 2025.
importance: 4
layout: tech_news_article
original_title: 'Microsoft: Patch for WSUS flaw disabled Windows Server hotpatching
  - BleepingComputer'
publishedAt: '2025-11-03T15:22:12+00:00'
slug: microsoft-patch-for-wsus-flaw-disabled-windows-ser
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: 'Microsoft: Záplata kritické chyby WSUS vyřadila hotpatching na Windows Server
  2025'
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/05/16/Windows-Server.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/05/16/Windows-Server.jpg
---

## Souhrn

Microsoft vydal mimořádnou bezpečnostní aktualizaci KB5070881, která opravuje kritickou zranitelnost CVE-2025-59287 ve Windows Server Update Service (WSUS) aktivně zneužívanou útočníky. Záplata však způsobila nečekaný problém – vyřadila funkci hotpatchingu na části serverů s Windows Server 2025, což znamená, že tyto systémy budou muset být pro instalaci bezpečnostních aktualizací restartovány.

## Klíčové body

- Mimořádná aktualizace KB5070881 opravuje kritickou zranitelnost CVE-2025-59287 umožňující vzdálené spuštění kódu (RCE) ve WSUS
- Zranitelnost je aktivně zneužívána útočníky a existuje veřejně dostupný proof-of-concept exploit
- Aktualizace vyřadila funkci hotpatchingu na omezeném počtu Windows Server 2025 systémů
- Americká agentura CISA nařídila vládním institucím okamžité záplatování systémů
- Watchdog skupina Shadowserver sleduje přes 2 600 WSUS instancí vystavených na internetu

## Podrobnosti

Zranitelnost CVE-2025-59287 představuje vážné bezpečnostní riziko pro organizace využívající Windows Server Update Service – centralizovanou službu pro správu a distribuci aktualizací Windows v podnikových sítích. Několik bezpečnostních firem potvrdilo aktivní zneužívání této chyby v reálných útocích, což vedlo k vydání mimořádné záplaty mimo běžný měsíční cyklus aktualizací.

Nizozemské národní centrum kybernetické bezpečnosti (NCSC-NL) varovalo správce IT infrastruktury před zvýšeným rizikem, zejména kvůli dostupnosti veřejného proof-of-concept exploitu. Americká agentura CISA (Cybersecurity and Infrastructure Security Agency) následně přidala zranitelnost do svého katalogu bezpečnostních chyb zneužívaných v útocích a nařídila federálním institucím okamžité záplatování.

Problem s aktualizací KB5070881 se projevil na Windows Server 2025 systémech zapojených do programu hotpatchingu. Hotpatching je pokročilá funkce umožňující instalaci bezpečnostních aktualizací bez nutnosti restartu serveru, což je kritické pro systémy vyžadující nepřetržitý provoz. Microsoft v aktualizované dokumentaci přiznává, že omezený počet serverů s aktivním hotpatchingem ztratil po instalaci záplaty svůj enrollment status.

Společnost již zastavila distribuci aktualizace KB5070881 na servery s aktivním hotpatchingem. Systémy, které aktualizaci již obdržely, nebudou v listopadu a prosinci dostávat hotpatch aktualizace a místo toho jim budou nabídnuty standardní měsíční bezpečnostní záplaty vyžadující restart. Microsoft pracuje na řešení problému, zatím však neuvedl konkrétní termín opravy.

## Proč je to důležité

Tato situace ilustruje složitý kompromis mezi rychlou reakcí na aktivně zneužívané zranitelnosti a stabilitou pokročilých funkcí operačního systému. Pro organizace provozující kritickou infrastrukturu na Windows Server 2025 s hotpatchingem to znamená dilema – buď okamžitě záplatovat a přijít o možnost aktualizací bez restartu, nebo riskovat zneužití kritické bezpečnostní chyby.

Počet přes 2 600 WSUS instancí vystavených na internetu podle Shadowserver ukazuje na rozsah potenciálního útočného povrchu. WSUS je klíčová komponenta pro správu aktualizací v podnikových prostředích, a jeho kompromitace může útočníkům umožnit distribuci škodlivého softwaru maskovaného jako legitimní aktualizace Microsoft napříč celou firemní sítí. Incident také zdůrazňuje rostoucí komplexitu moderních serverových systémů, kde i bezpečnostní záplaty mohou mít nečekané vedlejší efekty na pokročilé funkce.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/)

**Zdroj:** 📰 BleepingComputer
