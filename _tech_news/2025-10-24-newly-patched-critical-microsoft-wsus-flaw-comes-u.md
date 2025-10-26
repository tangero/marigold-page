---
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-10-24 16:30:00'
description: Microsoft vydal nouzovou opravu pro kritickou zranitelnost CVE-2025-59287
  ve službě WSUS, která je již aktivně zneužívána útočníky v reálných útocích.
importance: 4
layout: tech_news_article
original_title: Newly Patched Critical Microsoft WSUS Flaw Comes Under Active Exploitation
  - The Hacker News
publishedAt: '2025-10-24T16:30:00+00:00'
slug: newly-patched-critical-microsoft-wsus-flaw-comes-u
source:
  emoji: 📰
  id: null
  name: Internet
title: Microsoft záplatuje kritickou chybu ve WSUS, která je aktivně zneužívána
url: https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiboN42WiQTI7VcMEGEDyMaY3ZP7VsruF2cHNgK4XQ2SxW0adaaMaJYfa_3B5Og4rvc1KF9HS1L7IxA-jSa_ZWMOz5kAKexTlsbZHomhllf8esxYBqcv3-pL7GY5CCb7qZaSxFaM2s3sbLR6cw-KlYMQ0ZnyWbYpjxHph9tMZxDxGdsf6jQ8kdBWYsMdvol/s790-rw-e365/windows-update.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiboN42WiQTI7VcMEGEDyMaY3ZP7VsruF2cHNgK4XQ2SxW0adaaMaJYfa_3B5Og4rvc1KF9HS1L7IxA-jSa_ZWMOz5kAKexTlsbZHomhllf8esxYBqcv3-pL7GY5CCb7qZaSxFaM2s3sbLR6cw-KlYMQ0ZnyWbYpjxHph9tMZxDxGdsf6jQ8kdBWYsMdvol/s790-rw-e365/windows-update.jpg
---

## Souhrn

Microsoft vydal kritickou bezpečnostní záplatu pro zranitelnost CVE-2025-59287 ve službě Windows Server Update Services (WSUS), která je již aktivně zneužívána útočníky. Jedná se o vážnou chybu umožňující vzdálené spuštění kódu, která vyžaduje okamžitou pozornost správců IT infrastruktury.

## Klíčové body

- Zranitelnost CVE-2025-59287 ve WSUS je aktivně zneužívána v reálných útocích
- Microsoft vydal mimořádnou bezpečnostní opravu mimo standardní update cyklus
- Chyba umožňuje vzdálené spuštění kódu (Remote Code Execution) na postižených systémech
- Útočníci mohou získat plnou kontrolu nad servery spravujícími aktualizace Windows
- Doporučuje se okamžitá instalace záplaty na všech WSUS serverech

## Podrobnosti

Windows Server Update Services (WSUS) je klíčová služba pro správu a distribuci aktualizací Windows v podnikových sítích. Umožňuje IT administrátorům centralizovaně řídit, které aktualizace se nasadí na klientské stanice a servery v organizaci. Právě tato centrální role činí z WSUS atraktivní cíl pro útočníky.

Zranitelnost CVE-2025-59287 představuje kritické bezpečnostní riziko, protože útočník, který ji úspěšně zneužije, může získat možnost vzdáleně spustit libovolný kód na WSUS serveru. To v praxi znamená, že může převzít plnou kontrolu nad serverem a potenciálně distribuovat škodlivé aktualizace do celé firemní sítě maskované jako legitimní záplaty od Microsoftu.

Skutečnost, že zranitelnost je již aktivně zneužívána, značí, že útočníci mají funkční exploit a cílí na nezáplatované systémy. Microsoft proto vydal opravu mimo svůj standardní měsíční update cyklus (Patch Tuesday), což signalizuje mimořádnou závažnost situace.

Správci IT infrastruktury by měli bezpečnostní záplatu nasadit s nejvyšší prioritou. Kromě instalace aktualizace je vhodné zkontrolovat logy WSUS serverů na známky kompromitace a ověřit integritu distribuovaných aktualizací. Organizace využívající WSUS by měly také zvážit implementaci dodatečných bezpečnostních opatření, jako je segmentace sítě a monitoring síťového provozu směřujícího k WSUS serverům.

## Proč je to důležité

Tato zranitelnost představuje významné riziko pro podnikovou bezpečnost, protože WSUS servery jsou kritickou součástí IT infrastruktury většiny středních a velkých organizací používajících Windows. Kompromitace WSUS serveru může útočníkům poskytnout přístup k tisícům koncových zařízení a umožnit jim distribuci malwaru maskovaného jako legitimní aktualizace. Aktivní zneužívání zranitelnosti znamená, že hrozba není teoretická, ale reálná a aktuální. Rychlá reakce Microsoftu mimo standardní update cyklus ukazuje na závažnost situace a nutnost okamžité akce ze strany administrátorů.

---

[Číst původní článek](https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html)

**Zdroj:** 📰 Internet
