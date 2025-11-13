---
author: Marisa Aigen
category: kybernetika
companies:
- CISA
- Samsung
- WhatsApp
date: '2025-11-10 20:00:34'
description: Americká CISA nařídila federálním úřadům okamžitě opravit kritickou zranitelnost
  v zařízeních Samsung, která byla zneužívána jako zero-day k instalaci spyware LandFall
  přes WhatsApp. Útok cílil na moderní modely Galaxy a umožňoval rozsáhlé sledování
  uživatelů.
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
title: CISA nařizuje urgentní záplatu kritické zranitelnosti Samsungu zneužívané spywarem
  LandFall
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/13/CISA--headpic.jpg
---

## Souhrn
Americká agentura CISA zařadila zranitelnost CVE-2025-21042 v zařízeních Samsung mezi známé aktivně zneužívané chyby a nařídila federálním institucím její okamžité odstranění. Chyba byla využívána jako zero-day k doručení spyware LandFall přes škodlivé DNG obrázky posílané přes WhatsApp na novější modely telefonů Samsung.

## Klíčové body
- Kritická zranitelnost CVE-2025-21042 v knihovně libimagecodec.quram.so umožňuje vzdálené spuštění kódu na zařízeních Samsung (Android 13 a vyšší).
- Zneužívána minimálně od července 2024 k nasazení spyware LandFall, a to přes škodlivé obrázky ve formátu DNG posílané přes WhatsApp.
- LandFall umožňuje přístup k historii prohlížení, hovorům, mikrofonu, poloze, fotografiím, kontaktům, SMS, logům hovorů a souborům.
- Cílí na vlajkové modely Samsung (Galaxy S22/S23/S24, Z Fold 4, Z Flip 4) a pravděpodobně na uživatele v Iráku, Iránu, Turecku a Maroku.
- Infrastruktura útoku nese podobnosti s operacemi komerčních špionážních platforem, ale bez jednoznačného přiřazení ke konkrétnímu výrobci nebo státnímu aktérovi.

## Podrobnosti
Zranitelnost CVE-2025-21042 je chyba typu out-of-bounds write v knihovně libimagecodec.quram.so používané v telefonech Samsung. Tento typ chyby umožňuje útočníkovi zapisovat data mimo vyhrazenou paměť, což lze zneužít k obejití ochranných mechanismů systému a spuštění libovolného kódu. V praxi to znamená, že stačí doručit speciálně upravený obsah, který zpracuje zranitelná knihovna – v tomto případě obrázky ve formátu DNG.

Podle analýzy bezpečnostního týmu Unit 42 společnosti Palo Alto Networks (firma zaměřená na síťovou a cloudovou kybernetickou bezpečnost) byla zranitelnost využívána nejméně od července 2024. Útočníci posílali obětem škodlivé DNG soubory přes WhatsApp. Jakmile systém tento soubor zpracoval, došlo ke spuštění kódu vedoucího k instalaci spyware LandFall bez nutnosti zásahu uživatele. Meta a bezpečnostní tým WhatsApp zranitelnost nahlásili Samsungu, který vydal záplatu v dubnu 2025, ale aktivní zneužívání ukazuje, že řada zařízení zůstává neaktualizovaná.

Spyware LandFall je koncipován jako komplexní sledovací nástroj. Po úspěšné instalaci umožňuje dlouhodobé skryté monitorování: přístup k historii prohlížení, záznamu hovorů, odposlechu mikrofonu, geolokačním datům, fotografiím, kontaktům, SMS, logům hovorů a souborům. Tím se funkčně řadí k profesionálním komerčním špionážním řešením typu Pegasus a dalším nástrojům používaným zejména v cílených útocích proti novinářům, aktivistům nebo politickým oponentům.

Unit 42 identifikovala potenciální cíle v Iráku, Iránu, Turecku a Maroku na základě vzorků ve službě VirusTotal. Analýza infrastruktury C2 serverů a pojmenování komponent (například loader označený jako „Bridge Head“) vykazuje podobnosti s postupy známých komerčních spyware výrobců (NSO Group, Variston, Cytrox, Quadream) a operací Stealth Falcon spojených s oblastí Spojených arabských emirátů. Přesto nebylo možné LandFall přesvědčivě přiřadit konkrétní firmě nebo státnímu aktérovi.

Zařazení CVE-2025-21042 do katalogu Known Exploited Vulnerabilities znamená pro americké federální úřady povinné a časově vázané nasazení záplat. Prakticky to potvrzuje, že nejde o hypotetickou zranitelnost, ale o reálně probíhající a cíleně vedené útoky na vysoce hodnotné cíle.

## Proč je to důležité
Tato událost potvrzuje několik trendů, které jsou relevantní pro státní instituce, podniky i jednotlivé uživatele:

Za prvé, mobilní zařízení – zejména vlajkové modely hlavních výrobců – jsou prioritním cílem sofistikovaných aktérů. Vektor přes multimediální knihovny a zprávové aplikace ukazuje, že uživatel nemusí „udělat chybu“, aby byl kompromitován. Stačí pasivní příjem a automatické zpracování obsahu.

Za druhé, komerční spyware se dále profesionalizuje a přibližuje schopnostem státních zpravodajských služeb. LandFall funkčně zapadá do ekosystému nástrojů umožňujících dlouhodobé skryté sledování, bez jasné transparentnosti kdo je provozuje, s potenciálem zneužití proti civilním cílům.

Za třetí, reakce CISA podtrhuje, že rychlá aplikace bezpečnostních aktualizací není formální doporučení, ale kritická bezpečnostní povinnost. Organizace, které provozují zařízení Samsung na Androidu 13 a vyšším, musí ověřit aplikaci dubnových a novějších záplat, provést revizi mobilní bezpečnostní politiky, omezit rizikové kanály příjmu souborů a sledovat indikátory kompromitace spojené s LandFall a související infrastrukturou.

Pro koncové uživatele je hlavní závěr jednoduchý: aktualizace systému a aplikací nejsou kosmetika, ale jediná účinná obrana proti profesionálním zero-day útokům, které dokážou obejít běžné návyky bezpečného chování.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-samsung-zero-day-used-in-spyware-attacks/)

**Zdroj:** 📰 BleepingComputer
