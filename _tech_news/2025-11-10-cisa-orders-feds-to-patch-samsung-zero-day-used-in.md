---
author: Marisa Aigen
category: kybernetika
companies:
- CISA
- Samsung
- WhatsApp
date: '2025-11-10 20:00:34'
description: Americká CISA nařídila federálním úřadům okamžitě opravit kritickou zranitelnost
  v telefonech Samsung, která byla aktivně zneužívána ke skrytému nasazení spyware
  LandFall přes WhatsApp. Útok umožňuje vzdálené spuštění kódu a rozsáhlé sledování
  uživatelů včetně přístupu k hovorům, zprávám, poloze a souborům.
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
title: CISA nařizuje povinnou záplatu kritické Samsung zero-day zneužívané spywarem
  LandFall
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
---

## Souhrn
Americká vládní agentura CISA zařadila zranitelnost CVE-2025-21042 v zařízeních Samsung mezi aktivně zneužívané chyby a nařídila federálním úřadům její povinné záplatování. Zneužití chyby umožňuje nasazení spyware LandFall přes škodlivé DNG obrázky zaslané ve WhatsApp a poskytuje útočníkům rozsáhlý přístup k citlivým datům uživatelů.

## Klíčové body
- Kritická zranitelnost CVE-2025-21042 v knihovně libimagecodec.quram.so umožňuje vzdálené spuštění kódu na telefonech Samsung (Android 13 a vyšší).
- Zranitelnost je aktivně zneužívána spywarem LandFall doručovaným přes upravené DNG obrázky ve WhatsApp.
- LandFall získává přístup k historii prohlížení, hovorům, mikrofonu, poloze, fotkám, kontaktům, SMS, logům hovorů i souborům.
- CISA zařadila chybu do katalogu Known Exploited Vulnerabilities a federálním úřadům nařídila urychlenou instalaci záplat.
- Indikátory útoků a infrastruktura naznačují souvislost s profesionálním komerčním spywarem, ale bez jednoznačného přiřazení ke konkrétnímu dodavateli či státnímu aktérovi.

## Podrobnosti
Zranitelnost CVE-2025-21042 je chyba typu out-of-bounds write v knihovně libimagecodec.quram.so používané v telefonech Samsung s Androidem 13 a novějším. Tento typ chyby umožňuje útočníkovi zapisovat data mimo vyhrazenou paměť a tím dosáhnout vzdáleného spuštění vlastního kódu. Prakticky to znamená, že postačí doručit speciálně upravený soubor, který spustí škodlivý kód na cílovém zařízení bez vědomí uživatele.

Podle analýzy bezpečnostního týmu Unit 42 společnosti Palo Alto Networks (firma specializující se na síťovou a cloudovou bezpečnost) byla tato zranitelnost zneužívána nejméně od července 2024. Vektorem útoku jsou škodlivé DNG obrázky zaslané přes komunikátor WhatsApp. Jakmile je obrázek zpracován zranitelnou knihovnou, útočník získá kontrolu nad zařízením a dojde k instalaci spyware LandFall.

Spyware LandFall je pokročilý nástroj pro sledování, který umožňuje:
- přístup k historii prohlížení a aktivitám v internetových prohlížečích,
- odposlech a záznam hovorů a okolního zvuku,
- sledování polohy zařízení v reálném čase,
- čtení SMS, přístup ke kontaktům, logům hovorů a multimediálním souborům,
- vytažení dokumentů a dalších lokálně uložených dat.

Zasaženy jsou především vlajkové modely Samsung, včetně řad Galaxy S22, S23, S24 a skládacích modelů Z Fold 4 a Z Flip 4. Analýza vzorků z VirusTotal naznačuje cílení zejména na uživatele v Iráku, Íránu, Turecku a Maroku. Infrastruktura velících (C2) serverů, registrační vzorce domén a použití názvu „Bridge Head“ pro loader připomínají praxi známých dodavatelů komerčního spyware, jako jsou NSO Group, Variston, Cytrox či Quadream, nicméně LandFall nelze jednoznačně přiřadit k žádné z těchto skupin.

Samsung vydal opravu již v dubnu 2025 po upozornění od týmů Meta a WhatsApp Security, avšak aktivní zneužívání před zveřejněním záplaty potvrzuje kvalitně organizovanou zero-day kampaň.

## Proč je to důležité
Tento případ potvrzuje několik dlouhodobých trendů v oblasti kybernetické bezpečnosti:

Za prvé, komunikační platformy typu WhatsApp se stávají klíčovým vektorem pro cílené útoky, protože kombinují masivní uživatelskou základnu a bohaté multimediální funkce. Útok přes DNG obrázek ukazuje, že útočníci preferují formáty, které běžným uživatelům nepřijdou podezřelé.

Za druhé, mobilní zařízení – zejména vlajkové modely – jsou primárním cílem pro sledovací operace s politickým, zpravodajským nebo průmyslovým motivem. Rozsah přístupných dat z telefonu (komunikace, poloha, sociální graf, dvoufaktorové kódy) z něj dělá klíčový zdroj informací. Úspěšné zero-day kampaně proti Android zařízením potvrzují, že mobilní ekosystém je pro profesionální útočníky stejně atraktivní jako tradiční servery či pracovní stanice.

Za třetí, reakce CISA – povinné záplatování a zařazení do Known Exploited Vulnerabilities – signalizuje, že jde o reálnou a probíhající hrozbu, nikoliv teoretickou slabinu. Pro státní instituce a velké organizace je to jasný signál k revizi mobilní bezpečnostní politiky, inventarizaci zařízení Samsung, ověření úrovně záplat a nasazení detekčních mechanismů pro špehovací software.

Pro běžné uživatele a firmy je praktický závěr jednoznačný: aktualizace systému a bezpečnostních záplat u mobilních telefonů musí být brána stejně vážně jako u serverů, zejména u zařízení používaných k práci, přístupu do interních systémů a správě citlivých účtů.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/)

**Zdroj:** 📰 BleepingComputer
