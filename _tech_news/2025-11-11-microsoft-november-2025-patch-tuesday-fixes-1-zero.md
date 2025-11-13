---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
- BleepingComputer
date: '2025-11-11 18:45:29'
description: Listopadový Patch Tuesday od Microsoftu přináší opravy 63 zranitelností
  včetně jedné aktivně zneužívané zero-day chyby v jádře Windows a čtyř kritických
  problémů. Firmy i jednotlivci musí záplaty nasadit rychle, zejména na stále používaných
  instalacích Windows 10.
importance: 3
layout: tech_news_article
original_title: Microsoft November 2025 Patch Tuesday fixes 1 zero-day, 63 flaws -
  BleepingComputer
publishedAt: '2025-11-11T18:45:29+00:00'
slug: microsoft-november-2025-patch-tuesday-fixes-1-zero
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Microsoft v listopadu 2025 opravuje 63 zranitelností včetně aktivně zneužívané
  zero-day chyby
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
---

## Souhrn
Microsoft v rámci listopadového Patch Tuesday 2025 vydal bezpečnostní aktualizace, které řeší 63 zranitelností v produktech Windows, včetně jedné aktivně zneužívané zero-day chyby v jádře systému. Součástí balíčku jsou i čtyři kritické zranitelnosti, včetně vzdáleného spuštění kódu a zvýšení oprávnění.

## Klíčové body
- Celkem opraveno 63 zranitelností, z toho 1 aktivně zneužívaná zero-day v jádře Windows.
- Čtyři zranitelnosti označeny jako kritické, včetně vzdáleného spuštění kódu (RCE) a zvýšení oprávnění.
- Výrazný podíl tvoří chyby umožňující zvýšení oprávnění (29) a vzdálené spuštění kódu (16).
- Zahájení programu Extended Security Updates (ESU) pro Windows 10, důležité pro organizace stále běžící na nepodporované verzi.
- Doporučeno urychlené nasazení záplat a revize procesů správy aktualizací.

## Podrobnosti
Listopadový balíček aktualizací Microsoftu se zaměřuje na rozsáhlé spektrum zranitelností v operačních systémech Windows a souvisejících komponentách. Klíčovým prvkem je oprava aktivně zneužívané zero-day chyby v jádře Windows. Tato zranitelnost umožňuje útočníkovi, který již získal omezený přístup k systému, zvýšit svá oprávnění na úroveň systému, obejít bezpečnostní politiky a nasadit škodlivý kód, často bez detekce tradičními antiviry. Pro útočníky jde o zásadní nástroj pro post-exploitation fázi útoku.

Struktura opravených chyb ukazuje typický profil současných útoků na podnikové prostředí: 29 zranitelností typu elevation of privilege, které umožňují převzetí kontroly nad systémem po úvodním průniku; 16 chyb remote code execution (RCE), jež mohou být zneužity k útoku na dálku přes síť nebo škodlivé dokumenty; 11 zranitelností typu information disclosure umožňujících únik interních dat či systémových informací; dále 3 denial of service a 2 spoofing chyby. Kritické zranitelnosti typu RCE představují přímé riziko pro servery, pracovní stanice i vzdálené uživatele a měly by být prioritizovány při nasazování záplat.

Důležitým prvkem tohoto cyklu je také spuštění programu Extended Security Updates (ESU) pro Windows 10. Organizace, které stále provozují Windows 10 po ukončení standardní podpory, musí buď migrovat na Windows 11, nebo se přihlásit do ESU programu, aby nadále dostávaly bezpečnostní aktualizace. Microsoft současně vydal mimořádnou aktualizaci pro odstranění chyby, která bránila některým systémům do ESU vstoupit. To ukazuje, že firma očekává významný počet zákazníků, kteří Windows 10 nadále používají v produkčních prostředích.

Pro administrátory je klíčové aktualizace co nejrychleji otestovat a nasadit, zejména na systémech vystavených do internetu, serverech poskytujících vzdálený přístup a koncových bodech s vysokou mírou privilegovaných účtů. Zanedbání těchto záplat vytváří přímý prostor pro ransomware skupiny a cílené útoky na infrastrukturu.

## Proč je to důležité
Tento Patch Tuesday je významný z hlediska kontinuity bezpečnosti ve firemním i státním sektoru. Aktivně zneužívaná zero-day chyba v jádře Windows ukazuje, že útočníci mají funkční exploit dříve, než jsou systémy plošně záplatovány. Organizace, které nemají robustní proces řízení záplat (centralizované patch management nástroje, automatizované nasazování, testovací prostředí), zůstávají reálně zranitelné i týdny po vydání oprav.

Zahájení ESU pro Windows 10 potvrzuje, že mnoho provozů stále běží na nepodporované nebo přechodné infrastruktuře. To je problém zejména v sektorech kritické infrastruktury, zdravotnictví, výroby a veřejné správy, kde se modernizace často zpožďuje. Tento update cyklus je vhodným okamžikem pro audit: inventarizaci verzí OS, ověření, které stroje jsou bez podpory, a nastavení jasné politiky přechodu na Windows 11 nebo izolace a zajištění starších systémů. V prostředí, kde se útoky stále více automatizují a kombinují zneužití RCE a elevation of privilege chyb, se rychlé a disciplinované patchování stává základním bezpečnostním standardem, nikoli volitelným doporučením.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/)

**Zdroj:** 📰 BleepingComputer
