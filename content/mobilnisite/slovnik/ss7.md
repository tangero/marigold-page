---
slug: "ss7"
url: "/mobilnisite/slovnik/ss7/"
type: "slovnik"
title: "SS7 – Signalling System Number 7"
date: 2025-01-01
abbr: "SS7"
fullName: "Signalling System Number 7"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ss7/"
summary: "SS7 je soubor protokolů pro telefonní signalizaci používaný k navazování a ukončování telefonních hovorů, poskytování služeb jako identifikace volajícího a umožnění roamingu. Jde o základní mimopásmov"
---

SS7 (Signalizační systém číslo 7) je základní soubor protokolů pro mimopásmovou telefonní signalizaci používaný v sítích s přepojováním okruhů pro navazování a ukončování hovorů a pro umožnění služeb, jako je identifikace volajícího a roaming.

## Popis

Signalling System Number 7 (SS7) je soubor protokolů pro telefonní signalizaci vyvinutý [ITU-T](/mobilnisite/slovnik/itu-t/), přijatý a profilovaný 3GPP pro použití v jádrech mobilních sítí, zejména v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Funguje na mimopásmové signalizační síti oddělené od kanálů pro přenos hlasového provozu, přičemž využívá vyhrazené signalizační spoje. Architektura je založena na síti signalizačních přenosových bodů ([STP](/mobilnisite/slovnik/stp/)), bodů řízení služeb ([SCP](/mobilnisite/slovnik/scp/)) a bodů přepínání služeb ([SSP](/mobilnisite/slovnik/ssp/)), které jsou implementovány v síťových prvcích, jako jsou mobilní ústředny ([MSC](/mobilnisite/slovnik/msc/)) a domácí registrační místa ([HLR](/mobilnisite/slovnik/hlr/)). Mezi klíčové protokoly v rámci SS7 patří část pro přenos zpráv ([MTP](/mobilnisite/slovnik/mtp/)) pro spolehlivé směrování a doručování, část pro řízení signalizačního spojení (SCCP) pro rozšířenou adresaci a část pro aplikační transakční schopnosti (TCAP) pro podporu databázových dotazů a pokročilých služeb.

V kontextu 3GPP je SS7 klíčové pro doménu CS sítí 2G (GSM) a 3G (UMTS). Umožňuje základní postupy správy mobility a řízení hovorů. Například když mobilní uživatel zahájí hovor, MSC použije signalizaci SS7 ke komunikaci s HLR za účelem autentizace účastníka a získání směrovacích informací. Komunikuje také s návštěvnickým registračním místem (VLR) a dalšími MSC za účelem vytvoření cesty hovoru. Protokol ISDN User Part (ISUP) v rámci SS7 je zodpovědný za navazování, správu a uvolňování hlasových okruhů mezi ústřednami.

Role SS7 přesahuje základní řízení hovorů a umožňuje širokou škálu služeb inteligentní sítě (IN). Patří mezi ně vlastní hovorové funkce, jako je přesměrování hovoru, čekání na hovor a identifikace volajícího, stejně jako prémiové služby, jako jsou bezplatná čísla (např. 800 čísla) a předplacené účtování. Bezpečnost v tradiční SS7 síti byla založena na uzavřené, důvěryhodné povaze sítí operátorů, přičemž fyzická bezpečnost signalizačních spojů byla primárním kontrolním mechanismem. S vývojem sítí a jejich globálním propojováním se však tento model důvěry ukázal jako zranitelný, což vedlo k vývoji bezpečnostních bran v pozdějších vydáních.

## K čemu slouží

SS7 bylo vytvořeno, aby nahradilo dřívější systémy vnitropásmové signalizace (jako SS5), které pro řízení používaly tóny uvnitř hlasového kanálu. To bylo neefektivní a náchylné k podvodům (např. 'phreaking'). Účelem SS7 bylo poskytnout robustní, vysoce výkonnou mimopásmovou signalizační síť, která by zvládla rostoucí složitost a objem telefonního provozu, podporovala nové služby a umožnila automatizaci navazování a ukončování hovorů. Jeho oddělení řídicí a přenosové roviny umožnilo rychlejší časy navazování hovorů, efektivnější využití spojovacích linek a položilo základ pro služby inteligentní sítě.

V kontextu 3GPP, počínaje Release 99, bylo SS7 přijato jako základní signalizační protokol pro doménu s přepojováním okruhů sítí GSM a UMTS. Vyřešilo problém umožnění bezproblémové mobility a roamingu napříč rozsáhlými, geograficky rozptýlenými sítěmi tím, že poskytlo standardizovanou metodu pro výměnu informací o účastnících a směrování hovorů mezi MSC, HLR a VLR. Bylo to pojivo, které drželo pohromadě globální systém mobilní telefonie před úplným přechodem na signalizaci založenou na IP. Mezi omezení, která řešilo, patřily ruční ústředny a omezené funkční sady elektromechanických a raných elektronických přepínacích systémů, což umožnilo automatizované mobilní sítě s bohatými funkcemi v érách 2G a 3G.

## Klíčové vlastnosti

- Mimopásmová signalizace oddělující řídicí a přenosové cesty
- Vysoce spolehlivý přenos zpráv prostřednictvím části pro přenos zpráv (MTP)
- Globální adresování a směrování síťových prvků prostřednictvím signalizačních kódů bodů
- Podpora transakčně orientovaných služeb prostřednictvím části pro aplikační transakční schopnosti (TCAP)
- Řízení hovorů a správa okruhů prostřednictvím protokolu ISDN User Part (ISUP)
- Základ pro služby inteligentní sítě (IN) a vlastní hovorové služby

## Související pojmy

- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [SS7 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss7/)
