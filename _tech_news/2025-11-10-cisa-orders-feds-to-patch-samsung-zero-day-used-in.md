---
author: Marisa Aigen
category: kybernetika
companies:
- CISA
- Samsung
- WhatsApp
- Google
- Microsoft
date: '2025-11-10 20:00:34'
description: Americká agentura CISA zařadila kritickou zranitelnost v telefonech Samsung
  (CVE-2025-21042) mezi aktivně zneužívané chyby a nařídila federálním úřadům okamžitou
  aktualizaci, protože slouží k tichému nasazení spywaru LandFall přes WhatsApp.
importance: 4
layout: tech_news_article
original_title: CISA orders feds to patch Samsung zero-day used in spyware attacks
  - BleepingComputer
publishedAt: '2025-11-10T20:00:34+00:00'
slug: cisa-orders-feds-to-patch-samsung-zero-day-used-in
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: CISA nařizuje americkým úřadům záplatovat zranitelnost Samsungu zneužívanou
  spywarovým útokem LandFall
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
---

## Souhrn
Americká Agentura pro kybernetickou bezpečnost a infrastrukturu (CISA) nařídila federálním civilním úřadům neodkladně aktualizovat zařízení Samsung kvůli kritické zranitelnosti CVE-2025-21042, která je aktivně zneužívána k nasazení spywaru LandFall. Útok využívá upravené obrazové soubory zasílané přes WhatsApp a umožňuje vzdálené spuštění kódu a hluboké sledování uživatele bez jeho vědomí.

## Klíčové body
- Kritická chyba CVE-2025-21042 v knihovně libimagecodec.quram.so umožňuje vzdálené spuštění kódu na zařízeních Samsung s Androidem 13 a novějším.
- Zranitelnost je zneužívána nejméně od července 2024 k doručování spywaru LandFall přes škodlivé DNG obrázky posílané ve WhatsApp.
- LandFall získává přístup k historii prohlížeče, hovorům, mikrofonu, poloze, fotografiím, SMS, kontaktům a souborům.
- CISA zařadila chybu do katalogu „Known Exploited Vulnerabilities“ a vyžaduje povinné záplatování u federálních úřadů.
- Analýza naznačuje vazby na profesionální spyware ekosystém, ale bez jednoznačného přiřazení ke konkrétnímu vendorovi či státnímu aktérovi.

## Podrobnosti
CVE-2025-21042 je out-of-bounds write zranitelnost v obrazové knihovně libimagecodec.quram.so používané v zařízeních Samsung s Androidem 13 a vyšším. Chyba umožňuje útočníkovi po zpracování speciálně upraveného obrazového souboru spustit libovolný kód v kontextu napadené komponenty. Tento typ chyby je obzvláště závažný, protože napadá nízkoúrovňovou knihovnu, která standardně zpracovává multimediální obsah a má přístup k široké sadě systémových oprávnění.

Meta a bezpečnostní tým WhatsApp chybu nahlásily Samsungu, který vydal opravu v dubnu 2025. Následná analýza výzkumného týmu Unit 42 společnosti Palo Alto Networks (bezpečnostní firma zaměřená na síťovou, cloudovou a endpoint ochranu) však ukázala, že zranitelnost byla zneužívána již minimálně od července 2024. Útočníci doručovali upravené DNG obrazové soubory přes WhatsApp, přičemž samotné zobrazení nebo zpracování snímku na zařízení Samsung stačilo k aktivaci exploitu bez výrazné interakce uživatele.

Nasazený spyware, označený jako LandFall, je plnohodnotný sledovací nástroj. Umožňuje exfiltraci prohlížečové historie, odposlech a nahrávání hovorů a okolního zvuku, sledování polohy, přístup k adresáři, SMS, historii hovorů, fotografiím a souborům. Podle Unit 42 byly cílem zejména telefony řady Galaxy S22, S23, S24 a skládací modely Z Fold 4 a Z Flip 4.

Data z VirusTotal naznačují, že útoky byly zaměřeny na uživatele v Iráku, Íránu, Turecku a Maroku. Infrastruktura řídicích serverů (C2) a vzorce registrace domén připomínají dřívější operace Stealth Falcon, spojované s aktéry z oblasti Spojených arabských emirátů. Zároveň jsou vidět podobnosti v pojmenování komponent (např. „Bridge Head“) s komerčními spywarovými projekty typu NSO Group, Variston, Cytrox či Quadream. Autoři LandFall ale nemohou být na základě dostupných dat spolehlivě přiřazeni k žádnému známému dodavateli.

Zařazení CVE-2025-21042 do katalogu Known Exploited Vulnerabilities znamená, že federální úřady USA mají povinnost chybu záplatovat v daném termínu. V praxi to potvrzuje, že nejde o teoretické riziko, ale o probíhající cílené operace proti vybraným zařízením.

## Proč je to důležité
Tento případ ukazuje několik trendů, které jsou zásadní pro bezpečnost mobilního ekosystému:

Zaprvé, exploity přes multimediální obsah v běžně používaných komunikátorech (WhatsApp) zůstávají preferovaným vektorem pro sofistikované útočníky, protože umožňují tiché napadení uživatele bez viditelného podezřelého chování. Uživatel nemusí otevírat přílohu vědomě, stačí automatické zpracování.

Zadruhé, cílení na špičkové modely Samsungu potvrzuje orientaci útočníků na politicky, ekonomicky či bezpečnostně významné osoby. To staví výrobce zařízení i provozovatele komunikačních platforem pod tlak na rychlé zveřejňování záplat a transparentní komunikaci o útocích.

Zatřetí, podobnosti s komerčním spywarem a stopami dříve spojovanými s aktéry z Blízkého východu ukazují, že trh se sledovacím softwarem se dále profesionalizuje a fragmentuje. Organizace a státní správy by měly počítat s tím, že mobilní zařízení jsou primárním cílem a vyžadují stejnou úroveň řízení zranitelností jako servery a pracovní stanice.

Pro běžné uživatele a firmy je praktický závěr jednoznačný: udržovat systém a bezpečnostní záplaty aktuální, minimalizovat počet instalovaných aplikací, omezit udělená oprávnění a předpokládat, že i běžné komunikační kanály mohou být zneužity k cílenému sledování.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/)

**Zdroj:** 📰 BleepingComputer
