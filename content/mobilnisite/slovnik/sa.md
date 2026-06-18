---
slug: "sa"
url: "/mobilnisite/slovnik/sa/"
type: "slovnik"
title: "SA – File Service Announcement File"
date: 2026-01-01
abbr: "SA"
fullName: "File Service Announcement File"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sa/"
summary: "Soubor oznámení služby (Service Announcement File, SA) je strukturovaný datový soubor používaný v 3GPP službě Multimedia Broadcast/Multicast Service (MBMS) a její pokročilé verzi (eMBMS). Obsahuje met"
---

SA je strukturovaný datový soubor používaný v 3GPP MBMS a eMBMS, který obsahuje metadata popisující nabídku vysílacích služeb a umožňuje uživatelským zařízením objevovat a připojovat se k vysílacím relacím.

## Popis

Soubor oznámení služby (Service Announcement, SA) je klíčovou součástí servisní vrstvy služby 3GPP Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její pokročilé verze (eMBMS). Nejde o mediální soubor, ale o kontejner metadat, který poskytuje uživatelskému zařízení (UE) veškeré potřebné informace k objevení, výběru a přístupu k dostupným vysílacím/multicastovým službám. Soubor SA je obvykle doručován do UE prostřednictvím přenosové cesty s nízkou přenosovou rychlostí, například protokolem File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)), nebo může být poskytnut jinými prostředky, jako je [HTTP](/mobilnisite/slovnik/http/).

Soubor je strukturován podle specifických specifikací 3GPP (často za použití [XML](/mobilnisite/slovnik/xml/) schémat definovaných v TS 26.346 pro MBMS). Jeho obsah zahrnuje seznam dostupných vysílacích služeb, z nichž každá má atributy jako čitelný název služby, jedinečný identifikátor služby a podrobný popis služby. Zásadně obsahuje technické parametry potřebné k připojení k relaci doručování médií. To zahrnuje IP multicastovou adresu a číslo portu pro relaci, přidružený dočasný skupinový identifikátor mobilní sítě ([TMGI](/mobilnisite/slovnik/tmgi/)), který identifikuje vysílací přenosovou cestu na rádiové úrovni, a informace protokolu popisu relace (např. [SDP](/mobilnisite/slovnik/sdp/)) detailující kodeky a formáty médií. Může také zahrnovat plánovací informace (čas začátku, doba trvání) a metadata pro elektronické průvodce službami ([ESG](/mobilnisite/slovnik/esg/)).

Z architektonické perspektivy je soubor SA generován a spravován centrem vysílacích/multicastových služeb ([BM-SC](/mobilnisite/slovnik/bm-sc/)) v síti. BM-SC je zodpovědné za poskytování oznámení služeb, plánování relací a přenosů a zabezpečení (správu klíčů). MBMS klientská aplikace v UE přijímá a parsuje soubor SA. S využitím informací v něm obsažených může UE následně instruovat své nižší vrstvy k aktivaci příslušné MBMS přenosové cesty, připojení se k určené IP multicastové skupině a zahájení příjmu vysílacích mediálních proudů. Tím je odděleno objevování služeb od doručování médií, což umožňuje efektivní dynamické aktualizace služeb.

## K čemu slouží

Soubor oznámení služby byl vytvořen k řešení zásadní výzvy objevování služeb v celulárním vysílacím systému. V tradiční jednosměrové síti uživatel vyžádá konkrétní službu a je navázáno spojení typu point-to-point. Při vysílání síť přenáší obsah do široké oblasti a potenciálně miliony zařízení potřebují vědět, co se vysílá a jak se naladit.

Soubor SA poskytuje standardizovaný, efektivní mechanismus pro propagaci vysílacích služeb. Před jeho definicí neexistoval jednotný způsob, jak síť informuje zařízení o dostupných multicastových relacích, jejich časových plánech a technických parametrech potřebných pro příjem. Jeho vytvoření bylo motivováno zavedením MBMS, které umožňuje služby jako mobilní TV, streamování živých událostí a distribuci softwaru/aktualizací přes celulární sítě. Umožňuje operátorům dynamicky spravovat katalog služeb a poskytuje uživatelům interaktivního průvodce pro výběr obsahu, čímž činí vysílací služby uživatelsky přívětivými a spravovatelnými.

## Klíčové vlastnosti

- Obsahuje metadata pro objevování služeb MBMS/eMBMS
- Zahrnuje technické přístupové parametry (IP multicastová adresa, port, TMGI)
- Může poskytovat časové plány služeb a data pro elektronický průvodce službami (ESG)
- Obvykle doručován prostřednictvím FLUTE nebo HTTP poskytování
- Strukturován podle XML schémat 3GPP
- Generován a spravován centrem BM-SC v síti

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.419** (Rel-19) — Service Area Broadcast Protocol (SABP)
- **TS 25.703** (Rel-12) — HNB Emergency Warning Area Study for UTRA
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [SA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sa/)
