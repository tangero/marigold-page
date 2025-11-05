---
author: Marisa Aigen
category: bezpečnostní aktuali
companies:
- Microsoft
date: '2025-11-03 15:22:12'
description: Mimořádná bezpečnostní aktualizace KB5070881, která opravuje aktivně
  zneužívanou kritickou zranitelnost ve Windows Server Update Service, způsobila výpadek
  funkce hotpatching na některých serverech s Windows Server 2025.
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
title: 'Microsoft: Záplata kritické zranitelnosti WSUS vyřadila hotpatching na Windows
  Server 2025'
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/05/16/Windows-Server.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/05/16/Windows-Server.jpg
---

## Souhrn

Microsoft vydal mimořádnou bezpečnostní aktualizaci KB5070881, která opravuje kritickou zranitelnost CVE-2025-59287 ve Windows Server Update Service (WSUS) aktivně zneužívanou útočníky. Aktualizace však způsobila nečekaný problém – vyřadila funkci hotpatching na části serverů s Windows Server 2025, což znamená, že tyto systémy budou muset být pro instalaci bezpečnostních aktualizací restartovány.

## Klíčové body

- Mimořádná aktualizace KB5070881 opravuje zranitelnost CVE-2025-59287 umožňující vzdálené spuštění kódu (RCE) ve službě WSUS
- Zranitelnost je aktivně zneužívána útočníky a existuje veřejně dostupný proof-of-concept exploit
- Aktualizace způsobila ztrátu registrace k hotpatchingu u omezeného počtu Windows Server 2025 systémů
- Americká agentura CISA přidala zranitelnost do katalogu aktivně zneužívaných bezpečnostních chyb a nařídila vládním agenturám okamžité zabezpečení
- Sledovací skupina Shadowserver identifikovala přes 2 600 WSUS instancí vystavených na internetu s výchozími porty 8530/8531

## Podrobnosti

Zranitelnost CVE-2025-59287 představuje vážné bezpečnostní riziko pro Windows Server Update Service, který slouží k centralizované správě a distribuci aktualizací Windows v podnikových sítích. Několik bezpečnostních společností potvrdilo aktivní zneužívání této chyby v reálných útocích, což vedlo Microsoft k vydání mimořádné aktualizace ještě před pravidelným měsíčním cyklem záplat.

Nizozemské národní centrum kybernetické bezpečnosti (NCSC-NL) varovalo administrátory IT před zvýšeným rizikem, zejména kvůli dostupnosti veřejného proof-of-concept exploitu. Americká agentura CISA následně zařadila zranitelnost do svého katalogu známých zneužívaných bezpečnostních chyb a nařídila federálním agenturám okamžité nasazení záplaty.

Nečekaným vedlejším efektem aktualizace KB5070881 je však narušení funkce hotpatching na Windows Server 2025. Hotpatching umožňuje instalaci bezpečnostních aktualizací bez nutnosti restartu serveru, což je klíčová funkce pro kritické systémy vyžadující nepřetržitý provoz. Microsoft potvrdil, že omezený počet serverů registrovaných k hotpatchingu ztratil po instalaci aktualizace svůj registrační status.

Společnost problém rychle identifikovala a upravila distribuci aktualizace tak, aby se již nenabízela systémům s aktivním hotpatchingem. Postižené servery však nebudou v listopadu a prosinci dostávat hotpatch aktualizace a místo toho obdrží standardní měsíční bezpečnostní záplaty vyžadující restart.

## Proč je to důležité

Tato situace ilustruje složitý kompromis mezi bezpečností a dostupností systémů. Microsoft čelil dilema – buď okamžitě opravit aktivně zneužívanou kritickou zranitelnost s rizikem vedlejších efektů, nebo počkat na důkladnější testování a ponechat systémy zranitelné. Společnost zvolila bezpečnost, což je v kontextu aktivních útoků správné rozhodnutí.

Pro administrátory Windows Server 2025 s hotpatchingem to znamená nutnost plánovat restarty serverů pro instalaci bezpečnostních aktualizací v následujících dvou měsících. Zároveň je kritické okamžitě nainstalovat KB5070881 na všechny WSUS servery, protože riziko aktivního zneužití zranitelnosti výrazně převyšuje dočasnou ztrátu funkce hotpatching. Přítomnost přes 2 600 potenciálně zranitelných WSUS instancí vystavených na internetu ukazuje na rozsah problému a naléhavost nasazení záplaty.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/)

**Zdroj:** 📰 BleepingComputer
