---
author: Marisa Aigen
category: kybernetika
companies:
- CISA
- Samsung
- WhatsApp
- Google
- Apple
date: '2025-11-10 20:00:34'
description: Americká agentura CISA zařadila kritickou zranitelnost v telefonech Samsung
  (CVE-2025-21042) mezi aktivně zneužívané chyby a nařídila federálním úřadům urychlenou
  instalaci opravy poté, co byla využita ke špehování přes WhatsApp pomocí spywaru
  LandFall.
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
title: CISA nařizuje federálním úřadům okamžitě opravit zero-day zranitelnost Samsung
  využívanou spywarem LandFall
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
---

## Souhrn
Americká agentura CISA (Cybersecurity and Infrastructure Security Agency) nařídila federálním civilním úřadům neodkladně opravit kritickou zero-day zranitelnost v telefonech Samsung, označenou jako CVE-2025-21042. Tato chyba byla aktivně zneužívána ke vzdálené instalaci spywaru LandFall přes škodlivé DNG obrázky ve WhatsApp a umožňovala útočníkům plný přístup k datům uživatele.

## Klíčové body
- Kritická zranitelnost CVE-2025-21042 v knihovně libimagecodec.quram.so umožňuje vzdálené spuštění kódu na zařízeních se systémem Android 13 a novějším.
- Chyba byla využívána minimálně od července 2024 ke špehovacím kampaním prostřednictvím spywaru LandFall doručovaného přes WhatsApp.
- Cílila na vybrané modely Samsung Galaxy S22, S23, S24, Z Fold 4 a Z Flip 4, především v regionech Blízkého východu a severní Afriky.
- CISA zařadila CVE-2025-21042 na seznam Known Exploited Vulnerabilities a nařídila federálním úřadům povinnou aktualizaci.
- Analýza naznačuje podobnosti s komerčním špehovacím ekosystémem (NSO Group, Variston, Cytrox, Quadream), ale LandFall zatím nelze spolehlivě přiřadit konkrétnímu aktérovi.

## Podrobnosti
Podstatou incidentu je chyba typu out-of-bounds write v knihovně libimagecodec.quram.so, kterou Samsung používá pro zpracování obrázků. Útočník ji mohl zneužít k vzdálenému spuštění škodlivého kódu na zranitelných telefonech s Androidem 13 a vyšším. Praktická exploatace probíhala přes WhatsApp: oběť obdržela speciálně upravený DNG obrázek, jehož zpracování spustilo řetězec útoku vedoucí k instalaci spywaru LandFall bez nutnosti zásahu uživatele.

LandFall je sofistikovaný špehovací software, který po úspěšné instalaci umožňuje přístup k historii prohlížení, fotkám, kontaktům, SMS, seznamu hovorů, souborům a geolokačním datům. Umí také nahrávat hovory a okolní zvuk, což z něj dělá nástroj pro dlouhodobé sledování konkrétních cílů. Analýza bezpečnostního týmu Unit 42 společnosti Palo Alto Networks (specializuje se na síťovou bezpečnost, detekci hrozeb a analýzu malwaru) ukazuje, že kampaně mířily zejména na uživatele v Iráku, Íránu, Turecku a Maroku.

Infrastruktura řídicích serverů LandFall (C2 domény, registrační vzorce) sdílí znaky známé z operací Stealth Falcon, dříve spojovaných se Spojenými arabskými emiráty. Zároveň pojmenování komponent, jako "Bridge Head" pro načítací modul, odpovídá zvyklostem komerčních poskytovatelů spywaru typu NSO Group či Cytrox. Vyšetřovatelé však zatím nemají dostatek důkazů pro jednoznačné přiřazení.

Samsung vydal opravu již v dubnu 2025 na základě hlášení bezpečnostních týmů Meta a WhatsApp. Skutečnost, že zranitelnost byla v praxi aktivně zneužívána s výrazným časovým předstihem, vedla CISA k zařazení CVE-2025-21042 do katalogu Known Exploited Vulnerabilities. Pro federální agentury tak vzniká povinnost chybu v definovaném termínu odstranit, jinak riskují regulatorní i bezpečnostní dopady.

## Proč je to důležité
Incident potvrzuje několik dlouhodobých trendů.

Za prvé, komunikační platformy jako WhatsApp zůstávají atraktivním vektorem útoků, a to i přes šifrování obsahu. Útočníci se soustředí na zneužití implementačních chyb v mobilních zařízeních a multimediálních knihovnách, kde stačí zpracování škodlivého souboru. To je relevantní nejen pro státní správu USA, ale i pro evropské instituce a kritickou infrastrukturu, které běžně používají zařízení Samsung.

Za druhé, charakteristika LandFall naznačuje, že jsme stále v prostředí, kde se komerční spyware a státem podporované operace prolínají. Útočné nástroje se profesionalizují, ale zůstávají pod radarem, dokud nejsou odhaleny dlouhodobou technickou analýzou. Pro organizace to znamená nutnost důsledného patch managementu, kontroly dodavatelského řetězce mobilních zařízení a využívání nástrojů pro detekci anomálního chování na úrovni koncových bodů.

Za třetí, zásah CISA ukazuje, že zranitelnosti v běžně používaných telefonech velkých značek mají přímý dopad na národní bezpečnost. Evropské státy by měly podobně systematicky sledovat katalogy aktivně zneužívaných zranitelností a zavádět povinné lhůty pro aktualizace u státních institucí i provozovatelů kritických služeb. Pro běžné uživatele je tento případ dalším potvrzením, že odkládání aktualizací u mobilních zařízení vytváří prostor pro vysoce cílené špehovací kampaně.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/)

**Zdroj:** 📰 BleepingComputer
