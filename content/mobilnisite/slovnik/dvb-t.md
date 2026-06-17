---
slug: "dvb-t"
url: "/mobilnisite/slovnik/dvb-t/"
type: "slovnik"
title: "DVB-T – Digital Video Broadcasting - Terrestrial"
date: 2025-01-01
abbr: "DVB-T"
fullName: "Digital Video Broadcasting - Terrestrial"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dvb-t/"
summary: "Standard DVB pro pozemní digitální televizní vysílání využívající OFDM modulaci. Poskytuje robustní, kvalitní video a datové služby přes vzdušné rozhraní pro pevné a přenosné přijímače. V rámci 3GPP j"
---

DVB-T je standard DVB pro pozemní digitální televizní vysílání využívající OFDM modulaci, který je v rámci 3GPP zvažován pro doplňkový downlink a vysílací odlehčení v 5G sítích.

## Popis

Digital Video Broadcasting - Terrestrial (DVB-T) je standard [DVB](/mobilnisite/slovnik/dvb/) specifikující fyzickou vrstvu přenosového systému pro pozemní digitální televizi. Používá modulaci Coded Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) (COFDM) pro potlačení vícecestného šíření a zajištění robustního příjmu v náročných podmínkách. V rámci 3GPP je DVB-T zmiňován v kontextu poskytování vysílacích služeb, zejména pro [MBMS](/mobilnisite/slovnik/mbms/)/eMBMS přes pozemní vysílací sítě nebo jako doplňková downlinková technologie pro mobilní sítě.

Technologie funguje tak, že rozdělí digitální datový proud na tisíce pomalejších podproudů, z nichž každý je modulován na samostatnou subnosnou v rámci [OFDM](/mobilnisite/slovnik/ofdm/) symbolu. To poskytuje odolnost vůči frekvenčně selektivnímu útlumu a umožňuje vytváření sítí s jedním kmitočtem (SFN), kde více vysílačů vysílá stejný signál na stejné frekvenci, čímž se zlepšuje pokrytí a efektivita využití spektra. Mezi klíčové komponenty patří kanálové kódování (konvoluční a Reed-Solomon), prokládání a OFDM modulátor s konfigurovatelnými parametry, jako je 2k nebo 8k režim, ochranný interval a modulační schémata (QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)).

Ve scénáři integrovaném s 3GPP lze DVB-T použít jako vysílací přenosovou vrstvu pro doručování multimediálního obsahu zařízením 3GPP vybaveným DVB-T přijímači. To umožňuje hybridní vysílací-broadbandové služby, kde vysílací síť doručuje obsah s vysokou šířkou pásma (jako živé TV) a mobilní síť poskytuje interaktivitu a personalizaci. Pro 5G je DVB-T studován pro doplňkový downlink ke zvýšení downlinkové kapacity v hustě osídlených městských oblastech nebo pro pevný bezdrátový přístup s využitím stávající vysílací infrastruktury.

## K čemu slouží

DVB-T byl vyvinut pro umožnění digitálního přechodu od analogové pozemní televize (PAL, SECAM) v Evropě a dalších regionech. Řešil problém neefektivního využití spektra a špatné obrazové kvality analogové TV a zároveň poskytl odolnost vůči duchům a interferencím. Motivací bylo uvolnění spektra (tzv. digitální dividenda) pro jiné služby, jako je mobilní broadband, a zároveň nabídnutí divákům více kanálů a funkcí, jako jsou elektronické programové průvodce.

Z pohledu 3GPP je účelem odkazování na DVB-T prozkoumat využití vysílacího spektra a infrastruktury pro odlehčení downlinkového provozu s vysokou poptávkou, zejména pro populární živý video obsah. Tím se řeší omezení spočívající v nedostatku mobilního spektra během hromadných akcí. Potenciálním využitím DVB-T jako doplňkového downlinku v 5G sítích mohou operátoři zvýšit kapacitu a uživatelský komfort bez nasazování dalších mobilních stanic, a to s využitím širokého pokrytí vysílacích věží.

## Klíčové vlastnosti

- COFDM modulace s režimy 2k/8k pro flexibilitu
- Podpora sítí s jedním kmitočtem (SFN) pro efektivní využití spektra
- Hierarchická modulace umožňující dva nezávislé datové toky (HP/LP)
- Robustní kanálové kódování (konvoluční + Reed-Solomon)
- Konfigurovatelné ochranné intervaly pro potlačení dlouhých ozvěn
- Podpora video kódování MPEG-2 a později H.264/AVC a HEVC

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TR 36.792** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [DVB-T na 3GPP Explorer](https://3gpp-explorer.com/glossary/dvb-t/)
