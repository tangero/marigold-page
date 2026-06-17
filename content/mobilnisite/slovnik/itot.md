---
slug: "itot"
url: "/mobilnisite/slovnik/itot/"
type: "slovnik"
title: "ITOT – ISO Transport Service on top of TCP"
date: 2025-01-01
abbr: "ITOT"
fullName: "ISO Transport Service on top of TCP"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/itot/"
summary: "Standardizovaná metoda pro zabezpečený přenos aplikačních protokolových datových jednotek (APDU) založených na ISO, jako jsou ty používané v PKI a správě certifikátů, přes síť TCP/IP. Poskytuje spoleh"
---

ITOT je standardizovaná metoda pro zabezpečený přenos aplikačních protokolových datových jednotek (APDU) založených na ISO přes síť TCP/IP, která poskytuje spolehlivou transportní vrstvu pro bezpečnostní komunikaci.

## Popis

[ISO](/mobilnisite/slovnik/iso/) Transport Service on top of TCP (ITOT) je specifikace transportního protokolu definovaná 3GPP pro přenos aplikačních protokolů [OSI](/mobilnisite/slovnik/osi/) (Open Systems Interconnection) přes sítě TCP/IP. Je formálně specifikována v [IETF](/mobilnisite/slovnik/ietf/) RFC 1006 a přijata 3GPP pro specifická bezpečnostní rozhraní. Hlavní funkcí ITOT je poskytnout službu ISO Transport Service (TS), jak je definována v ISO/[IEC](/mobilnisite/slovnik/iec/) 8073, ale s využitím TCP (Transmission Control Protocol) jako podkladové síťové služby namísto nativních síťových protokolů vrstvy OSI. To umožňuje aplikacím navrženým pro zásobník OSI bezproblémově fungovat nad všudypřítomnou infrastrukturou TCP/IP.

Architektonicky ITOT funguje jako adaptační vrstva. Leží mezi vrstvou TCP a aplikační vrstvou OSI, jako jsou protokoly používané pro operace Public Key Infrastructure (PKI). Když má aplikace OSI data k odeslání (aplikační protokolovou datovou jednotku neboli [APDU](/mobilnisite/slovnik/apdu/)), předá je prezentační a relační vrstvě (pokud jsou použity) a poté vrstvě ITOT. Entita ITOR zapouzdří tato data do hlavičky TPKT (TCP Packet) dle RFC 1006 a přenese je přes standardní TCP spojení k protistraně ITOT. Přijímající entita ITOT odstraní hlavičku TPKT a doručí APDU svým vyšším vrstvám OSI. Toto zapouzdření zajišťuje potřebné rámování dat OSI přes TCP spojení orientované na proud bajtů.

V ekosystému 3GPP je ITOT specifikováno pro použití v bezpečnostních protokolech, zejména pro přenos certifikátů a zpráv souvisejících s PKI. Například může být použito na rozhraní mezi entitou Network Domain Security ([NDS](/mobilnisite/slovnik/nds/)) a certifikační autoritou ([CA](/mobilnisite/slovnik/ca/)). Jeho úlohou je zajistit spolehlivé, v pořádku doručené a kontrolované doručování bezpečnostně citlivých APDU. Díky využití TCP přebírá vlastnosti jako řízení toku dat, řízení zahlcení a garantované doručení, které jsou klíčové pro integritu bezpečnostních transakcí. Specifikace v dokumentech 3GPP, jako je TS 33.108, zajišťuje interoperabilitu mezi zařízeními různých výrobců při provádění bezpečnostních operací spoléhajících na standardizované aplikační protokoly OSI, čímž poskytuje robustní transportní základ pro bezpečnostní architekturu sítě.

## K čemu slouží

ITOT bylo přijato k vyřešení problému interoperability pro bezpečnostní a managementové protokoly původně navržené pro sadu protokolů [OSI](/mobilnisite/slovnik/osi/) ve světě, který se z velké části standardizoval na TCP/IP. Mnoho telekomunikačních standardů, včetně raných specifikací 3GPP pro bezpečnostní funkce jako správa certifikátů, bylo založeno na normách ISO (např. certifikáty X.509 používají ASN.1 a jsou často přenášeny aplikačními protokoly OSI). Nasazení těchto protokolů v nativní podobě vyžadovalo celý zásobník OSI, což bylo složité a v IP sítích operátorů nebylo široce rozšířeno.

Motivací pro specifikaci ITOT v 3GPP, zejména od Release 15 pro bezpečnost 5G, bylo poskytnout pragmatický a standardizovaný most. Umožňuje znovu využít bohatou, dobře definovanou sémantiku aplikačních protokolů OSI pro PKI bez nutnosti zavádět celou síťovou infrastrukturu OSI. Specifikací způsobu provozu těchto protokolů přes TCP/IP umožnilo 3GPP výrobcům implementovat bezpečnostní funkce pomocí osvědčených standardů aplikační vrstvy ISO při využití všudypřítomné, spolehlivé a spravovatelné transportní vrstvy TCP/IP. Tím se vyřešila omezení předchozích ad-hoc metod nebo režie spojené s implementací celých zásobníků OSI, a bylo zajištěno zabezpečené, spolehlivé a interoperabilní transportní médium pro kritická bezpečnostní data, jako jsou žádosti o certifikáty a zprávy o odvolání, mezi síťovými funkcemi a externími entitami PKI v sítích 5G.

## Klíčové vlastnosti

- Poskytuje službu ISO Transport Service (TS) přes sítě TCP/IP dle IETF RFC 1006
- Používá hlavičku TPKT pro rámování APDU OSI přes TCP proud bajtů
- Umožňuje bezpečnostním aplikacím založeným na OSI (např. PKI) fungovat přes IP sítě
- Zajišťuje spolehlivé doručování jednotek bezpečnostního protokolového datu ve správném pořadí
- Specifikováno pro použití na bezpečnostních rozhraních 3GPP, jako je správa certifikátů
- Usnadňuje interoperabilitu výrobců pro bezpečnostní komunikaci

## Související pojmy

- [NDS – Network Domain Security](/mobilnisite/slovnik/nds/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [ITOT na 3GPP Explorer](https://3gpp-explorer.com/glossary/itot/)
