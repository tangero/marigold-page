---
slug: "iam"
url: "/mobilnisite/slovnik/iam/"
type: "slovnik"
title: "IAM – Initial Address Message"
date: 2025-01-01
abbr: "IAM"
fullName: "Initial Address Message"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iam/"
summary: "Signalizační zpráva protokolu ISUP (ISDN User Part) používaná v telefonních sítích s přepojováním okruhů k zahájení hovoru. Přenáší klíčové informace pro zřízení hovoru, jako je číslo volaného účastní"
---

IAM je signalizační zpráva protokolu ISUP používaná v mobilních sítích s přepojováním okruhů k zahájení hovoru přenosem nezbytných informací pro jeho zřízení, jako jsou čísla volaného a volajícího účastníka.

## Popis

Zpráva Initial Address Message (IAM) je klíčová signalizační zpráva v rámci protokolu [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)), který je součástí signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)) používaného pro řízení hovorů v telefonních sítích s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Je to první zpráva odeslaná ve směru dopředného přenosu k zahájení ustavení hovoru. IAM obsahuje všechny nezbytné informace potřebné pro směrování hovoru sítí a rezervaci požadovaných prostředků. Mezi klíčové informační prvky v IAM patří Číslo volaného účastníka (CdPN), Číslo volajícího účastníka (CgPN), indikátory povahy spojení ([NCI](/mobilnisite/slovnik/nci/)), indikátory dopředného hovoru a požadovaná přenosová kapacita (např. řeč, 3,1 kHz audio). Zpráva prochází přes více signalizačních přenosových bodů ([STP](/mobilnisite/slovnik/stp/)) a ústředen (např. [MSC](/mobilnisite/slovnik/msc/), [GMSC](/mobilnisite/slovnik/gmsc/)) na základě vytočeného čísla a vytváří okruhovou cestu segment po segmentu.

Po přijetí IAM ústředna analyzuje Číslo volaného účastníka, aby určila směrování. Pokud ústředna není konečným cílem, může provést analýzu čísla a přeposlat novou IAM do dalšího uzlu na cestě, a současně rezervovat spojovací okruh mezi příchozí a odchozí stranou. Tento proces pokračuje, dokud IAM nedosáhne cílové ústředny obsluhující volaného účastníka. Cílová ústředna pak typicky odešle zpět směrem k původci zprávu Address Complete Message (ACM), která signalizuje, že adresní informace byly přijaty a volaný účastník je vyzván.

Role IAM je ústřední pro fázi zřizování hovoru. Její efektivní zpracování přímo ovlivňuje prodlevu po vytočení a úspěšnost dokončení hovoru. Ve specifikacích 3GPP se IAM používá v jádru sítě pro hovory mezi MSC, hovory do PSTN a další interakce v CS doméně. S vývojem směrem k plně IP sítím (IMS) byla role ISUP a IAM doplněna a nakonec nahrazena protokoly založenými na SIP, jako je SIP-INVITE, ale IAM zůstává klíčová pro vzájemné propojení legacy CS sítí a moderních IP systémů.

## K čemu slouží

IAM existuje jako spolehlivá a standardizovaná metoda pro zahájení telefonních hovorů v sítích s přepojováním okruhů. Před digitálními signalizačními systémy, jako je SS7, se zřizování hovorů spoléhalo na signalizaci v pásmu (např. vícefrekvenční tóny), která byla pomalá, nejistá a měla omezenou podporu služeb. Vytvoření SS7 a protokolu ISUP s IAM jako klíčovou zprávou pro zřízení hovoru tyto problémy vyřešilo zavedením signalizace mimo pásmo na samostatné, vysokorychlostní síti s přepojováním paketů. Toto oddělení umožnilo rychlejší zřizování hovorů, efektivnější využití hlasových okruhů a umožnilo pokročilé telefonní služby, jako je zobrazení čísla volajícího, přesměrování hovoru a bezplatná čísla, díky přenosu bohatých signalizačních informací.

Historický kontext je zakořeněn v digitalizaci telefonních sítí. IAM umožnila globální propojení národních telefonních sítí (PSTN) a raných mobilních sítí (GSM, UMTS CS doména). Poskytla společný jazyk pro komunikaci ústředen od různých dodavatelů. Její návrh řešil omezení předchozí kanálově asociované signalizace tím, že byl vysoce efektivní a nabízel bohaté možnosti, čímž vytvořil páteř mezinárodní a národní telefonie na desetiletí. Motivací pro její konkrétní strukturu bylo zapouzdření všech nezbytných informací pro směrování hovoru a služeb do jediné, úvodní zprávy, aby se minimalizovalo signalizační zpoždění.

## Klíčové vlastnosti

- Přenáší klíčové informace pro směrování hovoru (Čísla volaného a volajícího účastníka)
- Specifikuje požadovanou přenosovou kapacitu pro hovor (např. řeč, data)
- Obsahuje indikátory dopředného hovoru s instrukcemi pro zpracování sítí
- Přenáší dodatečné informace pro doplňkové služby
- Zahajuje proces rezervace okruhu v síti
- Tvoří základ pro následující zprávy ISUP (ACM, ANM, REL)

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 33.831** (Rel-12) — Study on Spoofed Call Detection & Prevention

---

📖 **Anglický originál a plná specifikace:** [IAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/iam/)
