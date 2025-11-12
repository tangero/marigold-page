---
author: Marisa Aigen
category: kybernetika
companies:
- CISA
- Samsung
- WhatsApp
date: '2025-11-10 20:00:34'
description: Americká CISA přikázala federálním agenturám okamžitě aktualizovat zařízení
  Samsung kvůli kritické zranitelnosti CVE-2025-21042, kterou útočníci využívají k
  nasazení spywaru LandFall přes škodlivé obrázky ve WhatsApp. Útok umožňuje vzdálené
  spuštění kódu a rozsáhlé sledování uživatelů bez jejich interakce.
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
title: CISA nařídila federálním úřadům opravit zranitelnost Samsungu zneužívanou spywarem
  LandFall
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
---

## Souhrn
Americká agentura CISA zařadila zranitelnost CVE-2025-21042 v zařízeních Samsung mezi aktivně zneužívané chyby a nařídila federálním civilním úřadům její neodkladné záplatování. Chyba umožňuje vzdálené spuštění kódu v knihovně libimagecodec.quram.so a byla využívána k nasazení spywaru LandFall prostřednictvím škodlivých DNG obrázků posílaných přes WhatsApp.

## Klíčové body
- Kritická zranitelnost CVE-2025-21042 v knihovně libimagecodec.quram.so umožňuje vzdálené spuštění kódu na zařízeních Samsung s Androidem 13 a vyšším.
- Zneužití probíhá přes speciálně upravené DNG obrázky zaslané ve WhatsApp, bez nutnosti výrazné interakce uživatele.
- Spyware LandFall získává přístup k historii prohlížení, hovorům, mikrofonu, poloze, fotografiím, kontaktům, SMS, logům hovorů a souborům.
- CISA zařadila chybu do katalogu Known Exploited Vulnerabilities a nařídila federálním agenturám rychlou aktualizaci.
- Indikace ukazují na cílení na Blízkém východě a v severní Africe, s možnými vazbami na komerční spyware ekosystém, ale bez potvrzeného pachatele.

## Podrobnosti
Zranitelnost CVE-2025-21042 je out-of-bounds write chyba v knihovně libimagecodec.quram.so, která se používá pro zpracování obrázků na vybraných zařízeních Samsung s Androidem 13 a novějšími verzemi. Útočník může vytvořit speciálně upravený DNG obrázek (digitální negativ), který při zpracování knihovnou vyvolá chybu a umožní spuštění libovolného kódu s oprávněními procesu, typicky bez nutnosti zásadní interakce uživatele. To je klasický scénář pro tzv. zero-click nebo low-click exploity, které jsou oblíbené u komerčních špionážních nástrojů.

Podle analýzy bezpečnostního týmu Unit 42 společnosti Palo Alto Networks byl exploit aktivně využíván minimálně od července 2024 k nasazování nového spywaru označeného jako LandFall. Palo Alto Networks je bezpečnostní firma zaměřená na firewally, cloudovou bezpečnost a hrozbovou analytiku; Unit 42 je její výzkumný tým specializovaný na analýzu malwaru a sofistikovaných kampaní. LandFall po úspěšné infiltraci umožňuje útočníkovi:

- monitorovat historii prohlížení a online aktivitu,
- zaznamenávat hovory a okolní zvuk,
- sledovat geolokaci zařízení,
- přistupovat k fotografiím, kontaktům, SMS, historii hovorů a uloženým souborům.

Cílem jsou především vlajkové modely Samsung Galaxy S22, S23 a S24, stejně jako skládací zařízení Z Fold 4 a Z Flip 4. Analýza vzorků z VirusTotal naznačuje cíle v Iráku, Íránu, Turecku a Maroku. Infrastruktura řídicích serverů (C2), vzory registrace domén a pojmenování komponent (např. „Bridge Head“) připomínají praktiky známé z oblasti komerčního spywaru, jako jsou NSO Group, Variston, Cytrox či Quadream. Výzkumníkům se však nepodařilo LandFall jednoznačně přiřadit ke konkrétní firmě nebo státnímu aktérovi.

Samsung vydal opravu již v dubnu 2025 po upozornění od bezpečnostních týmů Meta a WhatsApp. Skutečnost, že exploit byl v provozu dlouhé měsíce před zveřejněním, potvrzuje, že jde o skutečný zero-day využívaný proti vybraným cílům. CISA nyní zařazením do Known Exploited Vulnerabilities ukládá federálním civilním agenturám povinnost chybu v definovaném termínu odstranit, což je signál, že zranitelnost představuje reálné riziko i pro vládní infrastrukturu.

## Proč je to důležité
Tento případ potvrzuje několik trendů, které jsou z hlediska kybernetické bezpečnosti zásadní:

Za prvé, mobilní zařízení jsou primárním cílem pro špionážní operace. Kombinace WhatsApp (široce používaný komunikační nástroj) a zranitelnosti v proprietárních knihovnách výrobce umožňuje nenápadné, vysoce cílené útoky bez viditelných známek kompromitace. To je relevantní nejen pro státní správu USA, ale i pro evropské instituce, kritickou infrastrukturu, novináře, právníky a všechny vysoce exponované profese.

Za druhé, LandFall zapadá do stále rostoucího ekosystému komerčního spywaru, kde dodavatelé vyvíjejí a prodávají exploity a sledovací nástroje státním i nestátním aktérům. Opakované používání podobných naming konvencí a infrastruktury ukazuje na profesionalizaci trhu a recyklaci technik mezi různými kampaněmi.

Za třetí, přímý zásah CISA je signál pro celý průmysl: zpoždění při instalaci bezpečnostních aktualizací na mobilních zařízeních je neakceptovatelným rizikem. Organizace by měly:
- zavést povinné aktualizace pro firemní a vládní telefony,
- omezit používání nezaopatřených zařízení Samsung ve vysoce citlivých prostředích,
- systematicky monitorovat indikátory kompromitace (C2 domény, podezřelé DNG přílohy, anomální přístup k mikrofonu a poloze).

Pro běžné uživatele je praktickým dopadem nutnost okamžitě aktualizovat Samsung zařízení, zejména vlajkové modely, a předpokládat, že i zdánlivě bezpečné kanály, jako je komunikace přes WhatsApp, mohou být zneužity k sofistikovanému sledování, pokud není systém průběžně záplatován.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/)

**Zdroj:** 📰 BleepingComputer
