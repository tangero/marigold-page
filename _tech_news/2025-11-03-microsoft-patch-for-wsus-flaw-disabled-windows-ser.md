---
author: Marisa Aigen
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-11-03 15:22:12'
description: Mimořádná bezpečnostní aktualizace KB5070881, která opravuje aktivně
  zneužívanou zranitelnost ve Windows Server Update Service, způsobila výpadek funkce
  hotpatching na některých serverech Windows Server 2025.
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

Microsoft vydal mimořádnou bezpečnostní aktualizaci KB5070881, která opravuje kritickou zranitelnost CVE-2025-59287 ve Windows Server Update Service (WSUS) aktivně zneužívanou útočníky. Záplata však způsobila nečekaný problém – vyřadila funkci hotpatching na části serverů Windows Server 2025, které byly do tohoto programu zapojeny.

## Klíčové body

- Aktualizace KB5070881 opravuje kritickou zranitelnost CVE-2025-59287 umožňující vzdálené spuštění kódu (RCE) ve službě WSUS
- Zranitelnost je aktivně zneužívána útočníky a existuje veřejně dostupný proof-of-concept exploit
- Záplata způsobila ztrátu hotpatch enrollmentu na omezeném počtu Windows Server 2025 systémů
- Microsoft zastavil distribuci aktualizace na servery s aktivním hotpatchingem
- Organizace Shadowserver sleduje přes 2 600 WSUS instancí vystavených na internetu s výchozími porty 8530/8531

## Podrobnosti

Zranitelnost CVE-2025-59287 představuje vážné bezpečnostní riziko pro organizace využívající Windows Server Update Service – centralizovanou službu pro správu a distribuci aktualizací Windows v podnikových sítích. Několik bezpečnostních společností potvrdilo aktivní zneužívání této chyby v reálných útocích, což vedlo k vydání mimořádné záplaty mimo standardní měsíční cyklus aktualizací.

Nizozemské národní centrum kybernetické bezpečnosti (NCSC-NL) varovalo správce IT infrastruktury před zvýšeným rizikem, zejména kvůli dostupnosti veřejného exploitu. Americká agentura CISA (Cybersecurity and Infrastructure Security Agency) následně přidala zranitelnost do svého katalogu bezpečnostních chyb zneužívaných v útocích a nařídila federálním agenturám okamžité zabezpečení systémů.

Hotpatching je funkce Windows Server 2025 umožňující instalaci bezpečnostních aktualizací bez nutnosti restartování serveru, což je zásadní pro provoz kritických služeb vyžadujících nepřetržitou dostupnost. Microsoft v aktualizované dokumentaci k KB5070881 přiznává, že omezený počet serverů zapojených do programu hotpatching ztratil po instalaci záplaty svůj enrollment status.

Postižené servery nebudou v listopadu a prosinci 2025 dostávat hotpatch aktualizace a místo toho jim budou nabídnuty standardní měsíční bezpečnostní aktualizace vyžadující restart. Microsoft již zastavil distribuci KB5070881 na servery s aktivním hotpatchingem, problém však postihl systémy, které aktualizaci obdržely před identifikací chyby.

## Proč je to důležité

Tato situace ilustruje složitý kompromis mezi rychlou reakcí na aktivně zneužívané zranitelnosti a stabilitou pokročilých funkcí operačního systému. Organizace čelí dilema – buď okamžitě nainstalovat kritickou bezpečnostní záplatu a riskovat ztrátu hotpatchingu, nebo odložit aktualizaci a vystavit se riziku kompromitace přes WSUS.

Pro podniky využívající Windows Server 2025 s hotpatchingem jde o významný problém, protože tato funkce byla jedním z hlavních prodejních argumentů nové verze serveru. Nutnost restartů po instalaci bezpečnostních aktualizací znamená plánované výpadky služeb, což může mít dopad na dostupnost kritických aplikací a služeb.

Vysoký počet WSUS instancí vystavených na internetu (přes 2 600) ukazuje na rozsah potenciálního útočného prostoru. WSUS je klíčová infrastruktura pro správu aktualizací v podnikových sítích, a její kompromitace může útočníkům poskytnout možnost distribuovat škodlivý software do celé organizace pod záminkou legitimních aktualizací.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-patch-for-wsus-flaw-disabled-windows-server-hotpatching/)

**Zdroj:** 📰 BleepingComputer
