---
slug: "ecsd"
url: "/mobilnisite/slovnik/ecsd/"
type: "slovnik"
title: "ECSD – Enhanced Circuit Switched Data"
date: 2025-01-01
abbr: "ECSD"
fullName: "Enhanced Circuit Switched Data"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ecsd/"
summary: "Evoluční technologie GSM, která zvýšila přenosové rychlosti oproti tradičním okruhově přepínaným spojením. Vylepšila původní službu Circuit Switched Data (CSD) využitím více časových slotů a pokročilý"
---

ECSD je evoluční technologie GSM, která zvýšila přenosové rychlosti oproti tradičním okruhově přepínaným spojením využitím více časových slotů a pokročilých kódovacích schémat.

## Popis

Enhanced Circuit Switched Data (ECSD) je datová služba založená na GSM, která představuje vývoj základní schopnosti Circuit Switched Data ([CSD](/mobilnisite/slovnik/csd/)). Zatímco standardní CSD poskytovala jediný, pevný datový kanál 9,6 kbps nebo 14,4 kbps vyčleněním jednoho plnorychlostního kanálu pro přenos (TCH/F) pro datové volání, ECSD zavedla mechanismy pro zvýšení dosažitelné přenosové rychlosti v rámci okruhově přepínané domény. Funguje tak, že agreguje více časových slotů přenosového kanálu pro jediné datové spojení, což je koncept známý jako více-slotový provoz. Dále využívala efektivnější schémata kódování kanálu spolu s modulací vyšší úrovně ve svých pozdějších vývojových stupních spojených s [EDGE](/mobilnisite/slovnik/edge/).

Architektonicky ECSD využívá stávající okruhově přepínanou síť jádra GSM, zahrnující Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Interworking Function ([IWF](/mobilnisite/slovnik/iwf/)) pro připojení k externím datovým sítím, jako je PSTN nebo [ISDN](/mobilnisite/slovnik/isdn/). Klíčové vylepšení probíhá v rádiové přístupové síti a v mobilní stanici. Rádiový subsystém musí podporovat přidělení více časových slotů v rámci TDMA rámce jednomu uživateli. Mobilní stanice a systém základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) vyjednávají během sestavování hovoru o podporovaných schopnostech, aby určily maximální počet časových slotů (více-slotová třída) a podporovaná schémata modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)). Datový proud je segmentován a přenášen paralelně přes přidělené časové sloty.

ECSD definovala několik typů kanálů pro datový provoz: TCH/F (plná rychlost, hrubá rychlost 22,8 kbps) a TCH/H (poloviční rychlost, hrubá rychlost 11,4 kbps). Použitím různých schémat kódování kanálu (např. kódovací schémata ECS-1 až ECS-4 pro ECSD založené na EDGE) se mohla uživatelská datová rychlost na jeden časový slot lišit. Například použití nejodolnějšího kódování (ECS-1) na kanálu TCH/F může poskytnout ~8,8 kbps na slot, zatímco méně chráněné schéma (ECS-4) může dosáhnout ~17,6 kbps na slot. Když jsou kombinovány více sloty, lze teoreticky dosáhnout maximální uživatelské datové rychlosti až 64 kbps, což odpovídá kanálu B ISDN, například použitím čtyř časových slotů s vysokorychlostním kódovacím schématem.

Jeho provoz je přísně řízen sítí. Přidělování prostředků je statické po dobu trvání hovoru, což odpovídá okruhově přepínanému paradigmatu. To zaručuje konstantní přenosovou rychlost a nízké, konzistentní zpoždění, ale je neefektivní pro trhaný datový provoz. Správa více-slotových konfigurací zahrnuje složitou signalizaci pro přiřazování kanálů a předávání hovoru. Význam ECSD spočívá v jeho roli přechodové technologie, která demonstrovala potenciál pro vysokorychlostní mobilní data v rámci stávající infrastruktury GSM před rozšířeným zavedením inherentně efektivnějších paketově přepínaných technologií [GPRS](/mobilnisite/slovnik/gprs/) a EDGE.

## K čemu slouží

ECSD byl vyvinut, aby řešil kritické omezení raných datových služeb GSM: velmi nízké přenosové rychlosti. Původní služba CSD, omezená na 14,4 kbps, byla nedostatečná pro vznikající aplikace, jako je rychlejší prohlížení internetu, videokonference a přístup k podnikovým sítím, které vyžadovaly rychlosti blízké pevným modemům (28,8/56k) nebo ISDN (64 kbps). ECSD si kladl za cíl tuto mezeru překlenout využitím stávající, široce nasazené architektury okruhově přepínané sítě a poskytnout operátorům přímočarou cestu upgradu.

Motivace byla primárně hnána tržní poptávkou po vyšších rychlostech mobilních dat na konci 90. let a začátkem 2000. let, předtím než bylo GPRS plně zralé a nasazené. Řešil problém přírůstkového vylepšení. Namísto vyžadování zcela nové paketové sítě jádra umožnilo ECSD operátorům nabízet datové služby střední rychlosti upgradem základnových stanic a koncových zařízení na podporu více-slotového provozu a nových kódovacích schémat. To bylo zvláště atraktivní pro podporu aplikací v reálném čase s konstantní přenosovou rychlostí, jako je videotelefonie, kde garantovaná šířka pásma okruhově přepínaného spojení byla výhodná ve srovnání s proměnlivým zpožděním raných paketových sítí.

Dále ECSD, zejména ve své formě vylepšené EDGE (někdy nazývané ECSCD), sloužilo jako proof-of-concept pro vysokorychlostní rádiové techniky později používané v EDGE pro paketová data. Ověřilo použití 8-PSK modulace a pokročilého přizpůsobování spojení v živé síti. Jeho základní omezení však zůstávalo neefektivita vyčleňování okruhově přepínaných prostředků pro datový provoz. Tento inherentní nedostatek, spolu s rychlým úspěchem a lepší spektrální účinností paketově přepínaných služeb GPRS/EDGE, nakonec omezil rozšířené komerční nasazení ECSD a omezil jej na okrajovou roli ve vývojové cestě.

## Klíčové vlastnosti

- Více-slotový provoz agregující až 8 časových slotů pro jediné datové spojení
- Podpora jak Gaussian Minimum Shift Keying (GMSK), tak 8-PSK modulace (s EDGE)
- Více kódovacích schémat kanálu (ECS-1 až ECS-4) pro kompromisy mezi datovou rychlostí a odolností
- Využívá stávající okruhově přepínanou síť jádra GSM (MSC, IWF)
- Poskytuje garantovanou, konstantní přenosovou rychlost a nízké zpoždění po dobu trvání hovoru
- Definuje specifické typy kanálů pro přenos (TCH/F, TCH/H) a s nimi spojené datové rychlosti

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [ECSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecsd/)
