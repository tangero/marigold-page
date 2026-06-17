---
slug: "ipepc"
url: "/mobilnisite/slovnik/ipepc/"
type: "slovnik"
title: "IPEPC – In-Progress Emergency Private Call"
date: 2025-01-01
abbr: "IPEPC"
fullName: "In-Progress Emergency Private Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ipepc/"
summary: "Kritická služba v MCPTT (Mission Critical Push To Talk) pro zpracování nouzových privátních hovorů, které již probíhají. Zajišťuje, že komunikační sezení nouzového charakteru jsou v síti správně prior"
---

IPEPC je kritická služba MCPTT pro správu a zvýšení priority nouzového privátního hovoru, který již probíhá, za účelem zachování jeho kontinuity a řízení.

## Popis

In-Progress Emergency Private Call (IPEPC) je specifický funkční stav a služba v architektuře služeb pro mise kritické z hlediska bezpečnosti (Mission Critical Services – [MCS](/mobilnisite/slovnik/mcs/)) definované 3GPP, konkrétně pro Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Odkazuje na probíhající, bod-bod nouzový privátní hovor mezi dvěma uživateli MCPTT. Označení 'In-Progress' je klíčové pro logiku sítě a klienta, neboť signalizuje, že nouzové sezení bylo úspěšně navázáno a je aktivní, a odlišuje jej tak od požadovaného nebo čekajícího nouzového hovoru. Architektura zahrnuje MCPTT klienta na uživatelském zařízení (UE), MCPTT aplikační server a podkladovou síť jádra 3GPP (EPC nebo 5GC). MCPTT server je zodpovědný za rozpoznání nouzové povahy hovoru, aplikaci specifických autorizačních politik a správu životního cyklu sezení. Mezi klíčové komponenty patří autorizační funkce služby MCPTT, protokoly pro správu sezení a mechanismy QoS, které tento provoz zvýhodňují v rádiové síti a síti jádra. Jejím účelem je poskytnout garantovaný, řízený a prioritizovaný komunikační kanál pro nouzové situace mezi dvěma konkrétními osobami, například záchranářem a dispečerem, a zajistit nízkou latenci a vysokou spolehlivost i v podmínkách vytížené sítě. Zpracování IPEPC zahrnuje specifické procedury pro přednostní přerušení jiných hovorů (pre-emption), prioritní zacházení a případné hlášení polohy, které se odlišují od běžných privátních hovorů. Tento stav je udržován jak na straně klienta, tak serveru za účelem koordinace akcí, jako je ukončení nouzového sezení, které může vyžadovat specifické autorizované příkazy.

## K čemu slouží

IPEPC bylo vytvořeno za účelem splnění přísných požadavků na komunikaci v oblasti veřejné bezpečnosti a pro mise kritické z hlediska bezpečnosti přes sítě 3GPP. Tradiční komerční hlasové služby postrádaly potřebnou míru kontroly, priority a funkcí pro správu vyžadovaných pro scénáře kritické z hlediska života. Tento koncept řeší problém správy aktivního nouzového hovorového sezení a zajišťuje, že nemůže být neúmyslně ukončeno nebo jeho priorita snížena jiným síťovým provozem. Poskytuje standardizovaný mechanismus, pomocí kterého síť tyto specifické hovory identifikuje, chrání a řídí. Historicky měly profesionální mobilní radiové systémy (PMR), jako je TETRA, proprietární mechanismy pro nouzové hovory, ale přechod na širokopásmové sítě LTE a 5G vyžadoval, aby 3GPP tyto schopnosti standardizovalo a zajistilo tak interoperabilitu mezi dodavateli a přes hranice států. IPEPC jako součást širší sady [MCPTT](/mobilnisite/slovnik/mcptt/) od 3GPP Release 13 a novějších řeší omezení předchozích buněčných systémů, které zacházely se všemi hlasovými hovory s relativně stejnou prioritou, což je činilo nevhodnými pro komunikaci první zasahující složky, kde musí být aktivní nouzový kanál zachován za každou cenu.

## Klíčové vlastnosti

- Označuje aktivní, navázané bod-bod nouzové hovorové sezení v rámci MCPTT.
- Spouští síťově vynucované mechanismy priority a přednostního přerušení (eMPS, QoS).
- Umožňuje specifická autorizovaná řízení hovoru (např. autorizované ukončení).
- Vyžaduje odlišnou správu stavu sezení jak na straně klienta, tak serveru.
- Často je asociováno s hlášením polohy a dalšími doplňkovými službami souvisejícími s nouzovým stavem.
- Funguje v rámci standardizované servisní architektury MCPTT pro zajištění interoperability.

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [IPEPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipepc/)
