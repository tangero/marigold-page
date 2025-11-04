---
author: Marisa Aigen
category: kybernetická bezpečn
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

Microsoft vydal mimořádnou bezpečnostní aktualizaci KB5070881, která opravuje kritickou zranitelnost CVE-2025-59287 ve Windows Server Update Service (WSUS) aktivně zneužívanou útočníky. Aktualizace však způsobila nečekaný vedlejší efekt – vyřadila funkci hotpatching na části serverů s Windows Server 2025, což znamená, že tyto systémy budou muset být v listopadu a prosinci restartovány pro instalaci bezpečnostních aktualizací.

## Klíčové body

- Mimořádná aktualizace KB5070881 opravuje zranitelnost CVE-2025-59287 umožňující vzdálené spuštění kódu (RCE) ve službě WSUS
- Zranitelnost je aktivně zneužívána útočníky a existuje veřejně dostupný proof-of-concept exploit
- Aktualizace způsobila ztrátu registrace k hotpatchingu u omezeného počtu serverů Windows Server 2025
- Americká agentura CISA přidala zranitelnost do katalogu aktivně zneužívaných bezpečnostních chyb a nařídila vládním agenturám okamžité zabezpečení
- Organizace Shadowserver sleduje přes 2 600 WSUS instancí vystavených na internetu přes výchozí porty 8530/8531

## Podrobnosti

Zranitelnost CVE-2025-59287 představuje vážné bezpečnostní riziko pro organizace využívající Windows Server Update Service – centralizovanou službu pro správu a distribuci aktualizací Windows v podnikových sítích. Několik bezpečnostních společností potvrdilo aktivní zneužívání této chyby v reálných útocích, což Microsoftu nenechalo jinou možnost než vydat mimořádnou aktualizaci mimo standardní měsíční cyklus Patch Tuesday.

Hotpatching je relativně nová funkce Windows Server 2025, která umožňuje instalaci bezpečnostních aktualizací bez nutnosti restartování serveru. Tato schopnost je zásadní pro kritické systémy, které musí běžet nepřetržitě. Bohužel aktualizace KB5070881 způsobila, že některé servery ztratily registraci k této službě.

Microsoft problém identifikoval a zastavil distribuci aktualizace KB5070881 na servery s aktivním hotpatchingem. Společnost uvádí, že problém postihl pouze velmi omezený počet zařízení, která aktualizaci stihla obdržet před opravou distribučního mechanismu. Postižené servery budou v listopadu a prosinci dostávat standardní měsíční bezpečnostní aktualizace vyžadující restart místo hotpatch aktualizací.

Nizozemské národní centrum kybernetické bezpečnosti (NCSC-NL) varuje správce IT infrastruktury před zvýšeným rizikem, zejména vzhledem k dostupnosti veřejného exploitu. Situaci komplikuje fakt, že tisíce WSUS instancí jsou vystaveny přímo na internetu, což je z bezpečnostního hlediska nevhodná konfigurace.

## Proč je to důležité

Tato situace ilustruje klasický bezpečnostní dilema – nutnost rychle opravit kritickou zranitelnost versus riziko narušení funkčnosti systémů. Microsoft musel volit mezi ponecháním serverů zranitelných vůči aktivním útokům a dočasným vyřazením pokročilé funkce hotpatching.

Pro organizace využívající Windows Server 2025 s hotpatchingem to znamená komplikaci v plánování údržbových oken. Servery, které aktualizaci obdržely, budou muset být v následujících měsících restartovány, což může ovlivnit dostupnost služeb. Na druhou stranu neinstalování aktualizace představuje mnohem větší riziko vzhledem k aktivnímu zneužívání zranitelnosti.

Případ také zdůrazňuje důležitost správné konfigurace WSUS serverů – tyto systémy by neměly být vystaveny přímo na internet, ale měly by být přístupné pouze z interní sítě. Více než 2 600 veřejně dostupných instancí představuje značný útočný povrch pro kybernetické útoky.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/)

**Zdroj:** 📰 BleepingComputer
