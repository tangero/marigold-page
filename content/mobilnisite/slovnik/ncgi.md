---
slug: "ncgi"
url: "/mobilnisite/slovnik/ncgi/"
type: "slovnik"
title: "NCGI – NR Cell Global Identifier"
date: 2026-01-01
abbr: "NCGI"
fullName: "NR Cell Global Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ncgi/"
summary: "Globálně jednoznačný identifikátor buňky 5G NR, který kombinuje PLMN ID a NR Cell Identity (NCI). Umožňuje jednoznačnou identifikaci buňky napříč sítěmi pro správu mobility, lokalizační služby a síťov"
---

NCGI je globálně jednoznačný identifikátor buňky 5G NR, vytvořený kombinací PLMN ID a NR Cell Identity, který umožňuje jednoznačnou identifikaci buňky napříč sítěmi.

## Popis

NR Cell Global Identifier (NCGI) je klíčový identifikátor v sítích 5G New Radio (NR), standardizovaný organizací 3GPP. Slouží jako globálně jednoznačný štítek pro konkrétní NR buňku, který je nezbytný pro řadu síťových funkcí. NCGI je vytvořen spojením dvou základních složek: Public Land Mobile Network (PLMN) Identifier a NR Cell Identity ([NCI](/mobilnisite/slovnik/nci/)). PLMN ID jednoznačně identifikuje zemi a kód sítě mobilního operátora, čímž zajišťuje globální platnost identifikátoru. NCI je řetězec bitů, který jednoznačně identifikuje buňku v rámci daného PLMN. Délka a struktura NCI jsou definovány ve specifikacích a umožňují obrovské množství jedinečných identit buněk v síti jednoho operátora.

Z architektonického pohledu se NCGI používá napříč více síťovými entitami a rozhraními. V rádiové přístupové síti (RAN) gNB (5G základnová stanice) spravuje a vysílá NCGI pro své buňky. Tyto informace jsou předávány uživatelskému zařízení (UE) během procesů objevování buněk a měření. Jádro sítě (CN), konkrétně funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), využívá NCGI pro sledování polohy UE, správu předávání hovorů (mobilitu) a propojování servisních požadavků s konkrétními rádiovými prostředky. Systémy pro správu sítě a analytické platformy také používají záznamy s NCGI pro monitorování výkonu, lokalizaci chyb a analýzu provozu.

Jeho role v síti je mnohostranná. Především je základním kamenem pro správu mobility. Běhu procedur předání hovoru mezi NR buňkami, ať už intra-gNB nebo inter-gNB, jsou zdrojová a cílová buňka identifikovány svými NCGI. To síti umožňuje plynule přenést kontext UE a zachovat kontinuitu relace. Pro lokalizační služby a regulatorní požadavky, jako je zákonné odposlouchávání, poskytuje NCGI přesný identifikátor polohy na úrovni sítě. Dále ve scénářích zahrnujících sdílení sítě nebo víceoperátorová jádra sítě ([MOCN](/mobilnisite/slovnik/mocn/)) NCGI díky vloženému PLMN ID objasňuje, které prostředky kterého operátora jsou používány, což napomáhá účtování a arbitráži prostředků.

Generování a přidělování NCGI typicky spravují plánovací a konfigurační systémy síťového operátora. Část NCI musí být přidělena jednoznačně v rámci PLMN, aby se předešlo konfliktům. Při nasazení je NCGI vysíláno buňkou v blocích systémových informací (SIB) a je hlášeno UE v měřicích hlášeních a registračních zprávách. Jeho standardizovaný formát zajišťuje interoperabilitu mezi zařízeními od různých výrobců a napříč různými síťovými operátory, což je klíčové pro globální ekosystém 5G.

## K čemu slouží

NCGI bylo vytvořeno, aby uspokojilo potřebu standardizovaného, globálně jednoznačného identifikátoru buňky v systému 5G NR. Předchozí generace, jako 4G LTE, používaly [E-UTRAN](/mobilnisite/slovnik/e-utran/) Cell Global Identifier ([ECGI](/mobilnisite/slovnik/ecgi/)), které kombinovalo PLMN ID a Cell Identity ([CI](/mobilnisite/slovnik/ci/)). Se zavedením nové rádiové technologie (NR) a složitějších síťových architektur v 5G byl nezbytný nový, technologií specifický identifikátor. NCGI zajišťuje jasné odlišení od LTE buněk a zohledňuje strukturální specifika nasazení NR.

Motivace pro jeho vytvoření vychází z několika klíčových požadavků v 5G. Za prvé pokročilé scénáře mobility, včetně ultra-spolehlivé komunikace s nízkou latencí (URLLC) a plynulých předání hovorů ve vysokofrekvenčních pásmech, vyžadují přesnou a jednoznačnou identifikaci buňky. Za druhé rozšíření síťového segmentování (network slicing), kde logické sítě sdílejí fyzické rádiové prostředky, vyžaduje identifikátory, které lze asociovat s konkrétními segmenty na úrovni jednotlivých buněk. NCGI poskytuje kotvu pro takové asociace. Za třetí pro mezisíťové operace, jako je roaming a předávání hovorů mezi různými 5G sítěmi operátorů, globálně jednoznačný identifikátor zabraňuje záměnám a zajišťuje správné směrování a aplikaci politik.

Řeší problém nejednoznačného odkazování na buňky v heterogenním a globálním síťovém prostředí. Bez globálně jednoznačného identifikátoru by správa předávání hovorů mezi buňkami vlastněnými různými operátory, nebo dokonce v rámci složité sítě makro, mikro a piko buněk jednoho operátora, vedla k chybám a přerušením služby. NCGI díky vloženému PLMN ID tento problém rozsahu vnitřně řeší. Také poskytuje základ pro pokročilejší funkce, jako je hlášení polohy pro tísňové služby a síťové analytické nástroje, které sledují výkonnostní metriky na úrovni buňky v celé síti.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor kombinující PLMN ID a NR Cell Identity (NCI)
- Zásadní pro identifikaci buněk 5G NR v procedurách mobility a správy
- Vysíláno v systémových informacích pro objevování a výběr buňky UE
- Používáno funkcemi jádra sítě (AMF) pro sledování polohy UE a řízení předání hovoru
- Podporuje scénáře sdílení sítě a víceoperátorového jádra sítě (MOCN)
- Základ pro analytiku na úrovni buňky, monitorování výkonu a účtování

## Související pojmy

- [NCI – Native Code Identifier](/mobilnisite/slovnik/nci/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.008** (Rel-19) — Organization of Subscriber Data
- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.274** (Rel-19) — SMS Charging Management Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [NCGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncgi/)
