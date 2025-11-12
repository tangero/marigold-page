---
author: Marisa Aigen
category: kybernetika
companies:
- CISA
- Samsung
- WhatsApp
date: '2025-11-10 20:00:34'
description: Americká CISA zařadila kritickou zranitelnost CVE-2025-21042 v zařízeních
  Samsung mezi aktivně zneužívané chyby a nařídila federálním úřadům okamžitě instalovat
  aktualizace, protože exploit umožňuje vzdálené nasazení špionážního spyware LandFall
  přes WhatsApp.
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
title: CISA nařizuje urychlené záplatování kritické zero-day zranitelnosti Samsungu
  zneužívané špionážním spywarem
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
---

## Souhrn
Americká agentura CISA nařídila federálním institucím bezodkladně opravit kritickou zero-day zranitelnost CVE-2025-21042 v telefonech Samsung, která byla využívána k nasazení spyware LandFall přes škodlivé DNG obrázky zasílané přes WhatsApp. Útok umožňoval vzdálené spuštění kódu, skryté sledování uživatele a získání rozsáhlého množství citlivých dat z kompromitovaných zařízení.

## Klíčové body
- Kritická zranitelnost CVE-2025-21042 v knihovně libimagecodec.quram.so umožňuje vzdálené spuštění kódu na zařízeních Samsung s Androidem 13 a novějšími.
- Chyba byla zneužívána minimálně od července 2024 k doručování spyware LandFall přes škodlivé DNG obrázky v aplikaci WhatsApp.
- LandFall umožňuje přístup k historii prohlížení, fotografiím, kontaktům, SMS, hovorům, souborům, poloze a nahrávání zvuku.
- CISA zařadila CVE-2025-21042 na seznam Known Exploited Vulnerabilities a nařídila federálním úřadům rychlou aplikaci záplat.
- Indikace naznačují možnou vazbu na státem sponzorované nebo komerční špionážní aktéry, ale bez jednoznačného přiřazení.

## Podrobnosti
Zranitelnost CVE-2025-21042 je out-of-bounds write chyba v knihovně libimagecodec.quram.so, kterou Samsung používá pro zpracování obrázků ve svých telefonech. Tento typ chyby umožňuje útočníkovi zapisovat data mimo vyhrazenou paměť a tím získat možnost spustit vlastní kód na cílovém zařízení. V praxi to znamená, že útočník může připravit speciálně upravený obrázek, jehož pouhé zpracování systémem vede ke kompromitaci zařízení.

Podle analýzy bezpečnostního týmu Unit 42 (Palo Alto Networks, společnost specializující se na síťovou a cloudovou bezpečnost) byla zranitelnost aktivně využívána nejpozději od července 2024. Útočníci doručovali škodlivé DNG obrázky přes WhatsApp, který sloužil jako vektor pro vzdálené spuštění kódu bez nutnosti komplexní interakce ze strany uživatele. Po úspěšném zneužití byl instalován dosud neznámý spyware LandFall.

Spyware LandFall je navržen pro systematické sledování uživatele. Umožňuje přístup k historii prohlížení, fotografiím, kontaktům, SMS zprávám, záznamům hovorů, uloženým souborům a k přesné poloze zařízení. Dokáže také nahrávat hovory a okolní zvuk, což z něj dělá plnohodnotný nástroj pro politickou, průmyslovou i osobní špionáž. Unit 42 identifikoval cíle zejména v Iráku, Íránu, Turecku a Maroku.

Infrastruktura řídicích serverů (C2) a způsob registrace domén mají podobnosti s dřívějšími operacemi Stealth Falcon, kampaně spojované s aktéry ze Spojených arabských emirátů. Zároveň použití názvu "Bridge Head" pro komponentu loaderu kopíruje pojmenování běžné u komerčních spyware platforem jako NSO Group, Variston, Cytrox a Quadream. Přesto analytici zatím LandFall jednoznačně nepřiřadili ke konkrétní firmě či státnímu aktérovi.

Samsung zranitelnost opravil již v dubnu po upozornění od bezpečnostních týmů Meta a WhatsApp. Problém je, že velká část uživatelů a institucí aktualizace neaplikovala nebo používá zařízení s opožděnou distribucí bezpečnostních záplat. Zařazení CVE-2025-21042 do katalogu Known Exploited Vulnerabilities ze strany CISA znamená, že federální úřady mají povinnost chybu v definovaném termínu odstranit a potvrdit shodu.

## Proč je to důležité
Tento případ ukazuje několik zásadních trendů v bezpečnosti mobilních zařízení. Za prvé, útočníci nadále úspěšně zneužívají chyby v multimediálním zpracování, kde i běžný obsah, jako je obrázek, může sloužit jako nosič pro vzdálené spuštění kódu. Za druhé, WhatsApp a další komunikační aplikace jsou zneužívány jako důvěryhodné kanály pro doručení exploitů, což snižuje šanci na podezření ze strany uživatelů.

Pro státní instituce a podniky to potvrzuje, že mobilní zařízení je nutné považovat za plnohodnotný kritický endpoint, nikoli jen doplněk k počítačům. V praxi to znamená důsledně prosazovat pravidelnou instalaci bezpečnostních aktualizací, používat MDM systémy pro řízení verzí firmware, omezovat instalaci neověřených aplikací a monitorovat indikátory kompromitace i na mobilní platformě.

Pro běžné uživatele zařízení Samsung je klíčové zkontrolovat, zda mají nainstalované bezpečnostní aktualizace z dubna 2025 nebo novější, a neignorovat aktualizace systému. Incident také znovu otevírá otázku regulace a kontroly komerčních spyware nástrojů a státem podporovaných špionážních operací, které zneužívají slabiny v masově rozšířených zařízeních a aplikacích.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/)

**Zdroj:** 📰 BleepingComputer
