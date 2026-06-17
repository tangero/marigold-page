---
slug: "hips"
url: "/mobilnisite/slovnik/hips/"
type: "slovnik"
title: "HIPS – HAPS as IMT Base Stations"
date: 2025-01-01
abbr: "HIPS"
fullName: "HAPS as IMT Base Stations"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hips/"
summary: "HIPS označuje využití stanic na vysokých výškách (HAPS) jako základnových stanic pro IMT (International Mobile Telecommunications). Umožňuje pokrytí neterestrickou sítí (NTN) ze stratosféry a poskytuj"
---

HIPS je využití stanic na vysokých výškách (High Altitude Platform Stations) ve stratosféře jako základnových stanic pro IMT, poskytující rozsáhlé pokrytí neterestrickou sítí pro odlehlé a nedostatečně pokryté regiony.

## Popis

HIPS ([HAPS](/mobilnisite/slovnik/haps/) as [IMT](/mobilnisite/slovnik/imt/) Base Stations) je koncept 3GPP, který definuje integraci stanic na vysokých výškách (HAPS) do architektury pozemní mobilní sítě jako vzdušných základnových stanic. HAPS jsou kvazistacionární platformy, jako například solární bezpilotní letouny nebo vzducholodě, operující ve stratosféře v typických výškách mezi 17–22 km. V rámci HIPS jsou tyto platformy vybaveny funkcemi základnové stanice definovanými 3GPP (gNB pro 5G NR) a účinně fungují jako létající vysílače. Připojují se k páteřní síti přes satelitní nebo pozemní backhaulové spoje a poskytují rádiový přístup uživatelským zařízením (UE) na zemi, čímž vytvářejí vrstvu neterestrické sítě (NTN).

Architektura zahrnuje platformu HAPS hostující rádiovou jednotku (RU), distribuovanou jednotku ([DU](/mobilnisite/slovnik/du/)) a potenciálně část centralizované jednotky ([CU](/mobilnisite/slovnik/cu/)) podle rozdělení NG-RAN dle 3GPP. Komunikuje s UE pomocí rozhraní 3GPP NR, ale se specifickými úpravami pro dlouhé zpoždění šíření a jedinečné podmínky kanálu stratosférických spojů. Systém HIPS musí zvládat výzvy jako významné zpoždění zpáteční cesty (řádově desítky milisekund), Dopplerovy posuny způsobené pohybem platformy a široké oblasti pokrytí paprskem. Mezi klíčové technické aspekty patří synchronizace, mechanismy časového předstihu a upravené procedury náhodného přístupu, které zohledňují geometrii vysoké nadmořské výšky.

HIPS funguje jako součást integrované vzdušno-pozemní sítě, kde může poskytovat plynulou kontinuitu služeb s pozemními sítěmi. Podporuje jak transparentní (bent-pipe), tak regenerativní režim užitečného zatížení (s on-board zpracováním základnové stanice). Systém je navržen pro poskytování rozšířeného mobilního širokopásmového připojení (eMBB) a služeb masivního IoT přes velké geografické oblasti a doplňuje tak pozemní infrastrukturu. Jeho role je klíčová pro dosažení všudypřítomného pokrytí 5G, obnovu po katastrofách a kapacitu pro dočasné události, což je v souladu s vizí 3GPP pro komplexní integraci NTN ve verzi Release 17 a dalších.

## K čemu slouží

HIPS byl zaveden, aby řešil výzvu poskytování nákladově efektivního, rozsáhlého mobilního širokopásmového pokrytí v regionech, kde je nasazení pozemní infrastruktury ekonomicky nebo geograficky neproveditelné, jako jsou odlehlé venkovské oblasti, oceány a zóny postižené katastrofami. Tradiční pozemní sítě vyžadují husté nasazení základnových stanic, což je v oblastech s nízkou hustotou obyvatelstva neúměrně drahé. [HAPS](/mobilnisite/slovnik/haps/) nabízí střední cestu mezi pozemními věžemi a satelity, s nižší latencí než geostacionární satelity a širším pokrytím než pozemní buňky.

Motivace vychází z potřeby globální konektivity jako součásti vývoje 5G a vize IMT-2020 [ITU](/mobilnisite/slovnik/itu/). Před HIPS se úsilí o NTN v 3GPP zaměřovalo hlavně na satelitní přístup; HIPS to rozšiřuje o stratosférické platformy, které lze nasadit a rekonfigurovat rychleji než satelity. Řeší omezení předchozích izolovaných vzdušných řešení standardizací integrace HAPS v rámci ekosystému 3GPP, což zajišťuje interoperabilitu, efektivní využití spektra a plynulé předávání mezi pozemními sítěmi. Tato standardizace ve verzi Release 17 umožňuje komerční životaschopnost a škálovatelné nasazení HAPS pro mobilní operátory.

## Klíčové vlastnosti

- Provoz ve stratosféře ve výšce 17–22 km pro rozsáhlé pokrytí
- Podpora rozhraní 3GPP NR s úpravami pro NTN
- Transparentní a regenerativní režimy užitečného zatížení
- Integrace s páteřní sítí 5G přes satelitní nebo pozemní backhaul
- Podpora správy mobility a předávání s pozemními sítěmi
- Rozšířené pokrytí pro venkovské, námořní a letecké uživatele

## Související pojmy

- [HAPS – High Altitude Platform Station](/mobilnisite/slovnik/haps/)
- [GPS – Global Positioning System](/mobilnisite/slovnik/gps/)

## Definující specifikace

- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [HIPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hips/)
