---
author: Marisa Aigen
category: bezpečnostní aktuali
companies:
- Microsoft
date: '2025-11-03 15:22:12'
description: Mimořádná bezpečnostní aktualizace KB5070881, která opravuje aktivně
  zneužívanou zranitelnost ve Windows Server Update Service, způsobila výpadek funkce
  hotpatching na některých serverech s Windows Server 2025.
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
title: 'Microsoft: Záplata pro kritickou chybu WSUS vyřadila hotpatching na Windows
  Server 2025'
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/05/16/Windows-Server.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/05/16/Windows-Server.jpg
---

## Souhrn

Microsoft vydal mimořádnou bezpečnostní aktualizaci KB5070881, která opravuje kritickou zranitelnost CVE-2025-59287 ve Windows Server Update Service (WSUS) aktivně zneužívanou útočníky. Záplata však způsobila nečekaný vedlejší efekt – vyřadila funkci hotpatching na části serverů s Windows Server 2025, což znamená, že tyto systémy budou muset být pro instalaci bezpečnostních aktualizací restartovány.

## Klíčové body

- Mimořádná aktualizace KB5070881 opravuje kritickou zranitelnost CVE-2025-59287 umožňující vzdálené spuštění kódu (RCE) ve WSUS
- Zranitelnost je aktivně zneužívána útočníky a existuje veřejně dostupný proof-of-concept exploit
- Aktualizace způsobila ztrátu registrace hotpatchingu na omezeném počtu Windows Server 2025 systémů
- Americká agentura CISA přidala zranitelnost do katalogu aktivně zneužívaných bezpečnostních chyb a nařídila federálním agenturám okamžité záplatování
- Organizace Shadowserver sleduje přes 2 600 WSUS instancí vystavených na internetu na výchozích portech 8530/8531

## Podrobnosti

Zranitelnost CVE-2025-59287 představuje vážné bezpečnostní riziko pro organizace využívající Windows Server Update Service, centralizovaný systém pro správu a distribuci aktualizací Windows v podnikových sítích. Několik bezpečnostních společností potvrdilo, že chyba je aktivně zneužívána v reálných útocích, což vedlo k vydání mimořádné záplaty mimo standardní měsíční cyklus aktualizací.

Nizozemské národní centrum kybernetické bezpečnosti (NCSC-NL) varovalo správce IT infrastruktury před zvýšeným rizikem, zejména kvůli dostupnosti funkčního exploitu. Situaci dále vyostřila americká agentura CISA, která zranitelnost zařadila do svého katalogu známých zneužívaných zranitelností a nařídila vládním agenturám okamžité záplatování.

Problem s aktualizací KB5070881 se týká funkce hotpatching – technologie umožňující instalaci bezpečnostních aktualizací bez nutnosti restartu serveru. Tato funkce je klíčová pro prostředí vyžadující nepřetržitý provoz. Microsoft v aktualizované dokumentaci přiznává, že omezený počet serverů Windows Server 2025 registrovaných pro hotpatching ztratil po instalaci záplaty svůj registrační status.

Společnost reagovala zastavením distribuce aktualizace KB5070881 na servery s aktivním hotpatchingem. Systémy, které již záplatu obdržely, nebudou v listopadu a prosinci dostávat hotpatch aktualizace a místo toho jim budou nabídnuty standardní měsíční bezpečnostní aktualizace vyžadující restart.

## Proč je to důležité

Situace ilustruje složitý balanc mezi rychlou reakcí na aktivně zneužívané zranitelnosti a zajištěním stability systémů. Organizace čelí dilema – buď okamžitě záplatovat kritickou bezpečnostní chybu s rizikem výpadku hotpatchingu, nebo odložit aktualizaci a riskovat kompromitaci systému. Pro podniky s tisíci servery představuje ztráta možnosti aktualizovat bez restartu významný provozní problém, zejména v prostředích s vysokými požadavky na dostupnost služeb. Incident také ukazuje rostoucí tlak na výrobce software rychle reagovat na bezpečnostní hrozby, což může vést k nedostatečnému testování aktualizací.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/)

**Zdroj:** 📰 BleepingComputer
