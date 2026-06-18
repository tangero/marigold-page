---
slug: "en-dc"
url: "/mobilnisite/slovnik/en-dc/"
type: "slovnik"
title: "EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR"
date: 2026-01-01
abbr: "EN-DC"
fullName: "E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/en-dc/"
summary: "Architektura 5G Non-Standalone (NSA), kde je zařízení současně připojeno k hlavnímu uzlu 4G LTE (eNodeB) a sekundárnímu uzlu 5G NR (gNB). LTE kotva poskytuje připojení řídicí roviny a pokrytí, zatímco"
---

EN-DC je architektura 5G Non-Standalone (nesamostatná), kde zařízení využívá 4G LTE jako hlavní (master) uzel pro řídicí rovinu a pokrytí a zároveň současně využívá připojení 5G NR jako sekundární pro vysokorychlostní přenos dat.

## Popis

[E-UTRA](/mobilnisite/slovnik/e-utra/) NR Dual Connectivity (EN-DC) je specifická konfigurace duální konektivity definovaná standardem 3GPP, kde uživatelské zařízení (UE) je současně připojeno ke dvěma různým technologiím rádiového přístupu: LTE (E-UTRA) a 5G New Radio (NR). V této architektuře základnová stanice LTE (eNodeB) funguje jako hlavní uzel ([MN](/mobilnisite/slovnik/mn/)) a tvoří hlavní skupinu buněk ([MCG](/mobilnisite/slovnik/mcg/)). Základnová stanice 5G NR (gNB) funguje jako sekundární uzel ([SN](/mobilnisite/slovnik/sn/)) a tvoří sekundární skupinu buněk ([SCG](/mobilnisite/slovnik/scg/)). UE udržuje jediné připojení řídicí roviny k hlavnímu uzlu LTE prostřednictvím MCG. Připojení k jádru sítě je ukotveno v Evolved Packet Core (EPC), nikoli v 5G Core (5GC), což klasifikuje EN-DC jako nesamostatný ([NSA](/mobilnisite/slovnik/nsa/)) režim nasazení 5G.

Jak to funguje, zahrnuje koordinovaný provoz mezi eNodeB (MN) a gNB (SN). LTE eNodeB je kotvou řídicí roviny, zpracovává veškerou signalizaci Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), správu mobility a připojení k EPC (konkrétně k [MME](/mobilnisite/slovnik/mme/) a S-GW). NR gNB je primárně zodpovědný za poskytování dodatečné kapacity uživatelské roviny. Data mohou být rozdělena na vrstvě PDCP (umístěné v MN) nebo v jádru sítě (S-GW). Vrstva PDCP v MN může směrovat datové pakety do své vlastní vrstvy RLC (pro přenos přes LTE) nebo do vrstvy RLC SN (pro přenos přes NR) prostřednictvím rozhraní X2 (rozšířeného na X2-C a X2-U). To vyžaduje těsnou synchronizaci a koordinaci mezi oběma uzly.

Klíčové komponenty zahrnují UE podporující jak LTE, tak NR rádiové rozhraní, LTE eNodeB (hlavní eNB neboli MeNB), NR gNB (sekundární gNB neboli SgNB) a EPC. Kritickými rozhraními jsou rozhraní LTE-Uu mezi UE a eNodeB, rozhraní NR-Uu mezi UE a gNB a rozhraní X2 mezi eNodeB a gNB pro koordinaci řídicí (X2-C) a uživatelské roviny (X2-U). Úloha EN-DC v síti spočívala v tom, že sloužila jako primární cesta pro časné nasazení 5G, což operátorům umožnilo využít jejich hustou infrastrukturu LTE k poskytnutí rozsáhlého pokrytí 5G a vysokých přenosových rychlostí bez nutnosti okamžité investice do plnohodnotné sítě 5G Core, čímž se urychlilo uvedení 5G služeb na trh.

## K čemu slouží

EN-DC bylo vytvořeno, aby vyřešilo problém, jak rychle a nákladově efektivně zavést a nasadit technologii 5G New Radio ještě předtím, než byla plně standardizována a nasazena síť 5G Core. Hlavní motivací bylo umožnit operátorům nabízet rozšířené služby mobilního širokopásmového přístupu (eMBB) s velmi vysokými datovými rychlostmi s využitím spektra 5G NR, přičemž se mohli spolehnout na zralou, všudypřítomnou a stabilní síť LTE pro funkce řídicí roviny a kotvení pokrytí.

Historicky řešilo omezení čistě „greenfieldového“ nasazení samostatné 5G (SA), které by vyžadovalo současné zavedení nového rádiového rozhraní i nového jádra sítě, což je masivní a pomalá kapitálová investice. EN-DC jako nesamostatná architektura umožnila postupný přístup. Využilo stávající infrastrukturu LTE jako spolehlivou vrstvu řídicí roviny a pokrytí a překrylo ji kapacitou 5G NR pouze v cílových oblastech (např. husté městské hotspoty, stadiony), kde byla vysoká propustnost nejvíce potřeba.

Řešilo klíčové technické a obchodní výzvy: Poskytlo jasnou migrační cestu, snížilo počáteční riziko a náklady nasazení a umožnilo časný vývoj ekosystému zařízení zaměřený na datově orientované případy užití. Ukotvením v EPC také zajistilo zpětnou kompatibilitu a kontinuitu služeb pro hlas (VoLTE) a další služby LTE. EN-DC bylo základním kamenem první vlny komerčních nasazení 5G po celém světě a vytvořilo most mezi 4G a plnohodnotnými samostatnými systémy 5G.

## Klíčové vlastnosti

- Nesamostatná (NSA) architektura 5G ukotvená v LTE EPC
- LTE eNodeB jako hlavní uzel (Master Node) pro řídicí rovinu (RRC) a pokrytí
- NR gNB jako sekundární uzel (Secondary Node) pro zvýšení kapacity uživatelské roviny
- Rozdělení/agregace dat na vrstvě PDCP hlavního uzlu nebo v S-GW
- Využívá rozšířené rozhraní X2 (Xn pro NR se nepoužívá) pro koordinaci mezi uzly
- Umožňuje časné nasazení 5G bez sítě 5G Core

## Související pojmy

- [E-UTRA – Enhanced Universal Terrestrial Radio Access](/mobilnisite/slovnik/e-utra/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)
- [MCG – Master Cell Group](/mobilnisite/slovnik/mcg/)
- [SCG – Secondary Cell Group](/mobilnisite/slovnik/scg/)

## Definující specifikace

- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 28.554** (Rel-20) — 5G Network & Slice KPI Specification
- **TS 28.558** (Rel-19) — UE Level Measurements for 5G System
- **TS 28.657** (Rel-19) — E-UTRAN NRM IRP Requirements
- **TS 28.707** (Rel-19) — EPC NRM IRP Requirements
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.424** (Rel-19) — X2 Interface User Plane Transport Protocols
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [EN-DC na 3GPP Explorer](https://3gpp-explorer.com/glossary/en-dc/)
