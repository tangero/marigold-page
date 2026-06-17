---
slug: "csi-rs"
url: "/mobilnisite/slovnik/csi-rs/"
type: "slovnik"
title: "CSI-RS – Channel State Information Reference Signal"
date: 2025-01-01
abbr: "CSI-RS"
fullName: "Channel State Information Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csi-rs/"
summary: "CSI-RS je referenční signál v downlinku vysílaný gNB/eNB, který umožňuje UE odhadnout rádiový kanál. UE měří CSI-RS pro hlášení informací o stavu kanálu (CSI), včetně kvality kanálu, hodnosti (rank) a"
---

CSI-RS je referenční signál v downlinku vysílaný základnovou stanicí, který umožňuje uživatelskému terminálu (UE) odhadnout rádiový kanál a hlásit informace o stavu kanálu (CSI) pro adaptaci spojení, beamforming a optimalizaci MIMO.

## Popis

Channel State Information Reference Signal (CSI-RS) je signál fyzické vrstvy definovaný ve specifikacích 3GPP pro LTE (od Release 10) a NR. Jeho primární funkcí je poskytnout známou referenci pro uživatelský terminál (UE), aby mohl provést odhad downlinkového kanálu. Na rozdíl od buněčně specifických referenčních signálů ([CRS](/mobilnisite/slovnik/crs/)) používaných pro demodulaci je CSI-RS speciálně navržen pro získávání informací o stavu kanálu a lze jej konfigurovat s mnohem větší flexibilitou z hlediska hustoty, periodicity a mapování portů. gNB (v 5G NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) vysílá tyto signály na specifických zdrojových elementech v časově-frekvenční mřížce podle nakonfigurovaného vzoru. UE po přijetí CSI-RS měří vlastnosti jako frekvenční odezvu kanálu, interferenci a úroveň šumu.

Architektura CSI-RS zahrnuje konfiguraci prostřednictvím signalizace vyšší vrstvy [RRC](/mobilnisite/slovnik/rrc/). Mezi klíčové parametry patří počet anténních portů (který může být v NR od 1 do 32, čímž podporuje massive [MIMO](/mobilnisite/slovnik/mimo/)), vzor mapování zdrojů (hustota a umístění v resource blocku) a periodicita vysílání a offset subrámce. UE používá přijatý CSI-RS k výpočtu různých hlášení [CSI](/mobilnisite/slovnik/csi/). Tato hlášení typicky zahrnují indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), který doporučuje modulaci a kódovací schéma; indikátor předkódovací matice (PMI), který navrhuje předkódovací matici pro beamforming; a indikátor hodnosti (RI), který udává počet užitečných přenosových vrstev. Tyto informace jsou síti hlášeny zpět prostřednictvím Physical Uplink Control Channel (PUCCH) nebo Physical Uplink Shared Channel (PUSCH).

V provozu sítě gNB/eNB využívá hlášení CSI pro kritické funkce správy rádiových zdrojů. Na základě CQI provádí adaptaci spojení, volí vhodnou modulaci (např. QPSK, 256QAM) a kódovací poměr pro downlinkové přenosy k UE. PMI a RI se používají ke konfiguraci předkodéru pro víceanténní přenosy, což umožňuje zisky prostorového multiplexování (MIMO) a beamformingu. Tento uzavřený smyčkový mechanismus zpětné vazby umožňuje síti dynamicky se přizpůsobovat měnícím se rádiovým podmínkám a optimalizovat propustnost a spolehlivost. V 5G NR byla funkčnost CSI-RS významně rozšířena pro podporu nových případů užití, jako je správa beamů pro mmWave, kde může být CSI-RS vysílán v různých beamech, aby jej UE mohlo změřit a nahlásit nejlepší beam pro komunikaci.

Klíčové komponenty v rámci CSI-RS zahrnují CSI-RS zdroj (resource), který definuje časově-frekvenční umístění signálu a konfiguraci anténních portů; sadu CSI-RS zdrojů (resource set), která seskupuje více zdrojů pro měření, jako je měření interference; a konfiguraci hlášení CSI, která určuje, co má UE měřit a hlásit (např. CQI/PMI/RI pro konkrétní sadu zdrojů). Pro pokročilé funkce, jako je měření interference CSI ([CSI-IM](/mobilnisite/slovnik/csi-im/)), síť konfiguruje zdroje CSI-RS s nulovým výkonem (zero-power), kde gNB nevysílá, což umožňuje UE měřit interferenci ze sousedních buněk. Tento komplexní systém umožňuje sofistikované plánování víceuživatelského MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)), kde síť může obsluhovat více UE současně na stejných časově-frekvenčních zdrojích využitím přesných prostorových informací o kanálu odvozených z měření CSI-RS.

## K čemu slouží

CSI-RS byl zaveden v LTE Release 10, aby řešil omezení stávajícího buněčně specifického referenčního signálu (CRS) pro zpětnou vazbu informací o stavu kanálu v pokročilých anténních systémech. Před Release 10 byl CRS používán jak pro demodulaci, tak pro odhad stavu kanálu. CRS však byl vysílán nepřetržitě ze všech anténních portů, což způsobovalo vysokou režii, zejména s rostoucím počtem anténních portů pro MIMO. Byl také buněčně specifický, nikoli UE-specifický, což omezovalo přesnost odhadu kanálu pro funkce jako koordinovaný multipoint (CoMP) a beamforming. CSI-RS byl vytvořen, aby poskytl flexibilnější, nízkorežiový a UE-specifický referenční signál určený výhradně pro sondování kanálu, což umožnilo efektivní podporu MIMO vyššího řádu (až 8 vrstev v LTE) a technik síťové koordinace.

Motivace pro CSI-RS vycházela z úsilí průmyslu o vyšší spektrální účinnost a kapacitu. Jak sítě začaly používat více anténních prvků (což vedlo k Massive MIMO), potřeba přesné a detailní znalosti kanálu se stala prvořadou. CSI-RS umožňuje síti konfigurovat referenční signály šité na míru konkrétním UE nebo skupinám UE, což ve srovnání s neustále vysílaným CRS snižuje interferenci a režii. To umožňuje pokročilé funkce, jako je dynamický výběr bodu a společný přenos v CoMP, kde více přenosových bodů spolupracuje na základě přesného CSI. V 5G NR se účel dále rozšířil na podporu nových frekvenčních rozsahů, včetně milimetrových vln (mmWave), kde je provoz založený na beamech zásadní. CSI-RS v NR je základem pro procedury správy beamů, které umožňují gNB vysílat referenční signály v různých beamech, aby UE mohlo identifikovat nejlepší beam pro komunikaci, což je kritický požadavek pro překonání vysokých ztrát na mmWave frekvencích.

CSI-RS dále řeší problém škálovatelného návrhu referenčního signálu pro různé anténní konfigurace. Jeho konfigurovatelná povaha znamená, že režie se škáluje s počtem aktivních anténních portů používaných pro odhad kanálu, namísto aby byla pevná. To je ekonomicky i spektrálně efektivní. Také usnadňuje pokročilé implementace přijímače v UE, jako je potlačení interference, tím, že poskytuje vyhrazené zdroje pro měření jak požadovaného signálu, tak interference. Celkově je CSI-RS klíčovou technologií, která umožňuje vysokovýkonnou, adaptivní fyzickou vrstvu v moderních sítích 4G a 5G, a přímo přispívá k dosažení vysokých přenosových rychlostí, nízké latence a spolehlivého připojení, které tyto standardy slibují.

## Klíčové vlastnosti

- Umožňuje odhad downlinkového kanálu pro zpětnou vazbu CSI (CQI, PMI, RI)
- Konfigurovatelné anténní porty (1–32 v NR) podporující massive MIMO
- Flexibilní časově-frekvenční hustota a periodicita pro minimalizaci režie
- Podporuje CSI-RS s nulovým výkonem pro měření interference (CSI-IM)
- Základní prvek pro správu a měření beamů v 5G NR
- Umožňuje pokročilé víceuživatelské MIMO (MU-MIMO) a operace CoMP

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [CRS – Cell-specific Reference Signals](/mobilnisite/slovnik/crs/)
- [CSI-IM – CSI-Interference Measurement](/mobilnisite/slovnik/csi-im/)

## Definující specifikace

- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSI-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/csi-rs/)
