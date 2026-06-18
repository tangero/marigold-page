---
slug: "clnp"
url: "/mobilnisite/slovnik/clnp/"
type: "slovnik"
title: "CLNP – Connectionless Network Protocol"
date: 2025-01-01
abbr: "CLNP"
fullName: "Connectionless Network Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/clnp/"
summary: "CLNP je síťový protokol vrstvy síťové v modelu OSI standardizovaný 3GPP pro přenos dat bez vytvoření spojení v raných sítích GPRS. Poskytuje datagramové služby, umožňuje směrování paketů bez nutnosti"
---

CLNP je síťový protokol vrstvy síťové v modelu OSI standardizovaný 3GPP pro přenos dat bez vytvoření spojení v raných sítích GPRS, který poskytoval datagramové služby pro mobilní paketová data, než byl nahrazen protokolem IP.

## Popis

Connectionless Network Protocol (CLNP) je síťový protokol vrstvy síťové v modelu [OSI](/mobilnisite/slovnik/osi/) (Open Systems Interconnection), standardizovaný jako [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 8473-1, který byl přijat ve specifikacích 3GPP pro rané sítě General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)). Jako protokol bez vytvoření spojení CLNP funguje tak, že přenáší data v nezávislých paketech neboli datagramech, z nichž každý obsahuje úplné adresování a řídicí informace. To umožňuje, aby byl každý paket směrován sítí nezávisle na základě své cílové adresy, aniž by vyžadoval předchozí fázi navázání spojení mezi koncovými body. V kontextu 3GPP byl CLNP využíván jako síťový protokol uvnitř páteřní sítě GPRS, konkrétně mezi uzly GPRS Support Nodes (GSNs), pro přenos uživatelských dat a signalizačních zpráv. Fungoval společně s protokolem Connectionless Network Protocol (CLNP) a Subnetwork Dependent Convergence Protocol ([SNDCP](/mobilnisite/slovnik/sndcp/)) na síťové vrstvě, což umožňovalo paketově orientovanou komunikaci přes GSM rádiový přístup.

Architektonicky byla role CLNP nedílnou součástí jádrové sítě GPRS, známé jako páteřní síť GPRS. Tato páteř propojovala Serving GPRS Support Nodes ([SGSN](/mobilnisite/slovnik/sgsn/)) a Gateway GPRS Support Nodes (GGSN). Pakety CLNP, zapouzdřující uživatelská data z mobilních stanic, byly směrovány mezi těmito uzly na základě adres Network Service Access Point ([NSAP](/mobilnisite/slovnik/nsap/)), což jsou hierarchické adresy definované v modelu OSI. Protokol poskytoval základní služby, jako je segmentace a opětovné složení velkých paketů, detekce chyb pomocí kontrolních součtů a mechanismus time-to-live (TTL) pro zabránění nekonečnému obíhání paketů sítí. Operoval nad různými technologiemi linkové vrstvy, včetně Frame Relay a Ethernetu, které byly běžné v raných mobilních jádrových sítích. Použití CLNP umožnilo GPRS nabízet skutečnou paketově orientovanou službu, což byl rozdíl oproti spojově orientované povaze tradičních GSM hovorů.

Během provozu, když mobilní stanice zahájila paketovou datovou relaci, SGSN zapouzdřil datové jednotky do paketů CLNP. Tyto pakety byly pak přeposílány přes páteřní síť GPRS, případně přes několik mezilehlých uzlů, až k GGSN, který sloužil jako brána k externím paketovým datovým sítím ([PDN](/mobilnisite/slovnik/pdn/)). Bezspojová povaha CLNP znamenala, že trasa každého paketu mohla být dynamicky určována mezilehlými směrovači na základě směrovacích tabulek a stavu sítě, což nabízelo robustnost a flexibilitu. CLNP však negarantoval doručení, pořadí ani bezchybný přenos; tyto funkce byly ponechány protokolům vyšších vrstev, jako je Transport Protocol Class 4 (TP4) ve stacku OSI nebo adaptacím v architektuře 3GPP. Postupem času, jak se internetový protokol (IP) stal všudypřítomným, 3GPP vyvinulo směrem k přijetí IP (nejprve IPv4, později IPv6) jako standardního síťového protokolu, a CLNP byl vyřazen kvůli globální dominanci IP a zjednodušené integraci s internetem.

## K čemu slouží

CLNP byl zaveden ve verzi 3GPP Release 4, aby poskytl standardizovaný síťový protokol bez vytvoření spojení pro paketově orientovanou jádrovou síť GPRS. Jeho vytvoření bylo motivováno potřebou umožnit služby mobilních paketových dat v sítích GSM, které byly původně navrženy pouze pro spojově orientovaný hlas. Před GPRS datové služby v GSM spoléhaly na spojově orientovaná datová připojení, která byla neefektivní pro trhavý, přerušovaný datový provoz, protože vyčleňovala rádiové zdroje na celou dobu trvání relace, což vedlo ke špatnému využití zdrojů a vyšším nákladům. CLNP tento problém řešil nabídkou paketově orientovaného přístupu, který umožňoval statistické multiplexování dat od více uživatelů přes sdílené síťové zdroje, čímž zlepšil efektivitu a umožnil nové služby, jako je mobilní přístup k internetu.

Přijetí CLNP bylo poháněno jeho souladem s referenčním modelem OSI, který byl vlivný v telekomunikační standardizaci během 90. let. Poskytoval dobře definovaný mezinárodní standard pro síťování bez vytvoření spojení, což zajišťovalo interoperabilitu mezi zařízeními od různých výrobců v páteřní síti GPRS. CLNP řešil problém přenosu paketizovaných dat přes jádrovou síť mezi GSNs bez nutnosti složitých procedur navazování spojení, což bylo vhodné pro dynamickou a mobilní povahu uživatelských relací. Jeho účel byl však nakonec přechodný; jak internet a sada protokolů IP získaly ohromnou převahu, staly se zjevnými omezení udržování samostatného protokolového stacku založeného na OSI, včetně zvýšené složitosti a nedostatku bezproblémové integrace s IP externími sítěmi. To vedlo 3GPP k přechodu na IP jako sjednocující síťový protokol v pozdějších verzích.

## Klíčové vlastnosti

- Datagramová služba bez vytvoření spojení pro nezávislé směrování paketů
- Použití adres NSAP pro hierarchické síťové adresování
- Segmentace a opětovné složení velkých jednotek protokolových dat
- Detekce chyb pomocí kontrolního součtu hlavičky pro integritu dat
- Pole time-to-live pro zabránění oběhu paketů v síti
- Provoz nad různými linkovými vrstvami, jako je Frame Relay

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [SNDCP – Sub-Network Dependent Convergence Protocol](/mobilnisite/slovnik/sndcp/)
- [IP – IP Packet eXchange](/mobilnisite/slovnik/ip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [CLNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/clnp/)
