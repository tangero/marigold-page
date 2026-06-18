---
slug: "v2v"
url: "/mobilnisite/slovnik/v2v/"
type: "slovnik"
title: "V2V – Vehicle-to-Vehicle"
date: 2025-01-01
abbr: "V2V"
fullName: "Vehicle-to-Vehicle"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/v2v/"
summary: "Přímá komunikační služba mezi vozidly, která jim umožňuje vyměňovat si bezpečnostní a provozní informace, jako je rychlost, poloha a stav brzdění. Jedná se o základní technologii pro kooperativní inte"
---

V2V je přímá komunikační služba mezi vozidly, která umožňuje výměnu bezpečnostních a provozních informací a tvoří základ pro kooperativní inteligentní dopravní systémy.

## Popis

Komunikace vozidlo-vozidlo (V2V) je typ komunikace mezi vozidly definovaný v rámci širšího rámce Cellular Vehicle-to-Everything (C-V2X), standardizovaného organizací 3GPP. Umožňuje vozidlům přímo si vyměňovat informace s jinými vozidly ve svém okolí, typicky v dosahu několika set metrů. Tato přímá komunikace probíhá buď prostřednictvím sidelink rozhraní (PC5), což je komunikační kanál zařízení-zařízení, nebo může být usnadněna prostřednictvím mobilní sítě (rozhraní Uu). Primárním režimem pro bezpečnostní zprávy s nízkou latencí a vysokou spolehlivostí je sidelink PC5, pracující v pásmu 5,9 GHz pro [ITS](/mobilnisite/slovnik/its/).

Technické fungování zahrnuje vysílání základních bezpečnostních zpráv ([BSM](/mobilnisite/slovnik/bsm/)) nebo zpráv o kooperativním povědomí ([CAM](/mobilnisite/slovnik/cam/)) vysokou frekvencí (např. 10 Hz). Tyto zprávy obsahují dynamické stavové údaje, jako je [GPS](/mobilnisite/slovnik/gps/) poloha vozidla, rychlost, zrychlení, směr a stav vozidla (např. aktivace brzd). Blízká vozidla tyto zprávy přijímají a jejich palubní jednotky informace zpracovávají. Na základě těchto dat mohou aplikace provádět analýzu hrozeb, jako je výpočet času do kolize, a poskytovat varování řidiči nebo zahajovat automatizované akce, jako je nouzové brzdění. Komunikační režim definovaný pro tento účel je LTE-V2X Mode 4 nebo NR-V2X Mode 2, které používají mechanismus autonomního výběru zdrojů založený na snímání (sensing-based semi-persistent scheduling - [SPS](/mobilnisite/slovnik/sps/)) bez síťového plánování, což zajišťuje provoz i mimo pokrytí mobilní sítí.

V rámci architektury 3GPP jsou služby V2V podporovány jak základnovou sítí, tak rádiovou přístupovou sítí. Základnová síť prostřednictvím funkcí, jako je [V2X](/mobilnisite/slovnik/v2x/) Application Server a V2X Control Function, může poskytovat autorizaci, poskytování parametrů (jako je konfigurace PC5) a podporu pro síťově asistované plánování (Mode 3). Radiové specifikace (např. 36.785, 38.785) definují fyzickou vrstvu, protokoly přidělování zdrojů a struktury zpráv pro rozhraní PC5. Vývoj od V2V založeného na LTE (v Rel-14/15) k V2V založenému na NR (od Rel-16) přinesl vylepšené schopnosti, jako je podpora vyšších frekvencí (mmWave), ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a přesné sidelink určování polohy, které jsou klíčové pro pokročilé automatizované manévry a jízdu v koloně.

## K čemu slouží

Komunikace V2V byla vyvinuta za účelem řešení kritických omezení palubních senzorů vozidel (jako je radar, lidar a kamery). Zatímco tyto senzory poskytují 'pohled' na bezprostřední okolí, jsou omezeny přímou viditelností a mohou být ovlivněny počasím, překážkami nebo jinými vozidly. V2V vytváří kooperativní povědomí, které umožňuje vozidlům 'vidět' za rohy a přes překážky díky elektronickému sdílení dat odvozených ze senzorů. To je zásadní pro prevenci nehod, zejména ve scénářích, jako jsou srážky na křižovatkách, náhlé brzdění předního vozidla mimo přímý výhled nebo kooperativní zařazování do provozu.

Standardizace v rámci 3GPP, začínající ve verzi 14, byla motivována potřebou globálně harmonizovaného řešení založeného na mobilních sítích, které by mohlo využít stávající i budoucí infrastrukturu mobilních sítí. Před C-V2X byla hlavní navrhovanou technologií komunikace s krátkým dosahem (DSRC) založená na [IEEE](/mobilnisite/slovnik/ieee/) 802.11p. C-V2X od 3GPP, včetně V2V, nabídlo vývojově příznivější cestu s lepším výkonem, delším dosahem a nativní integrací s celulárními sítěmi široké oblasti pro rozšířené služby. Cílem je vytvořit komunikační páteř pro kooperativní inteligentní dopravní systémy (C-ITS), která umožní nejen bezpečnost, ale také optimalizaci dopravního proudu a konečné uskutečnění vysoce automatizované a autonomní jízdy.

## Klíčové vlastnosti

- Přímá komunikace mezi vozidly využívající sidelink rozhraní PC5 v pásmu 5,9 GHz
- Vysílání základních bezpečnostních zpráv (BSM/CAM) obsahujících dynamické stavové údaje vozidla
- Autonomní výběr zdrojů (Mode 4/Mode 2) pro provoz mimo pokrytí mobilní sítí
- Podpora jak LTE-V2X (od Rel-14), tak vylepšené NR-V2X (od Rel-16) rádiové technologie
- Umožňuje bezpečnostní aplikace jako varování před čelní srážkou, asistence pohybu na křižovatce a nouzové elektronické brzdové světlo
- Může být síťově asistovaná (Mode 3/Mode 1) pro lepší efektivitu a správu zdrojů

## Definující specifikace

- **TS 22.886** (Rel-16) — eV2X Use Cases and Requirements
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TR 37.885** (Rel-15) — Study on V2X Evaluation Methodology for LTE/NR
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TR 38.868** (Rel-17) — Optimizations of pi/2 BPSK uplink power in NR
- **TR 38.886** (Rel-16) — NR V2X UE Radio Transmission & Reception

---

📖 **Anglický originál a plná specifikace:** [V2V na 3GPP Explorer](https://3gpp-explorer.com/glossary/v2v/)
