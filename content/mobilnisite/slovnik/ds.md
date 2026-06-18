---
slug: "ds"
url: "/mobilnisite/slovnik/ds/"
type: "slovnik"
title: "DS – Discovery Service"
date: 2026-01-01
abbr: "DS"
fullName: "Discovery Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ds/"
summary: "Služba definovaná v rámci architektury služeb polohování (LCS), která umožňuje autorizovanému klientovi (LCS Client) zjistit, které lokální servery (např. GMLC, LMF) jsou dostupné v síti nebo napříč s"
---

DS je služba v architektuře služeb polohování (Location Services), která umožňuje autorizovaným klientům objevit dostupné lokální servery (Location Servers) a získat jejich adresování a informace o schopnostech.

## Popis

Discovery Service (DS) je funkční prvek a související procedury v architektuře služeb polohování ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP. Jejím hlavním úkolem je fungovat jako adresář nebo registr, který poskytuje informace pro objevování klientům LCS. LCS Client je aplikace nebo síťová entita, která žádá o polohu cílového UE. Než může podat žádost o polohu, potřebuje klient vědět, *který* síťový uzel (lokální server, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) v jádru sítě nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5GC) je za cílové UE odpovědný nebo mu může poskytnout službu. DS tyto informace o směrování a schopnostech poskytuje.

Architektonicky může být DS implementována jako samostatný síťový uzel nebo integrována do existujícího uzlu, jako je GMLC. Spravuje databázi nebo má přístup k provozním datům, která mapují klíčové identifikátory (jako je číslo [MSISDN](/mobilnisite/slovnik/msisdn/), identita [IMSI](/mobilnisite/slovnik/imsi/) cílového UE nebo identita Serving Network) na adresu (např. IP adresu, Diameter hostname) příslušného lokálního serveru. Procedura typicky zahrnuje odeslání zprávy Discovery Request ze strany LCS Client na známý vstupní bod DS. Tato žádost obsahuje identifikátor cíle. DS tuto žádost zpracuje, provede potřebné vyhledávání nebo mezisíťové rozlišení směrování (např. použitím LCS Roaming Exchange (LRX) pro případy mezi [PLMN](/mobilnisite/slovnik/plmn/)) a vrátí Discovery Response s adresou příslušného lokálního serveru a případně s jeho podporovanými schopnostmi (např. metody určování polohy, protokoly pro ochranu soukromí).

DS je klíčová pro škálovatelná a interoperabilní nasazení LCS, zejména v prostředích s více dodavateli, v roamingových scénářích a v sítích s více geograficky distribuovanými lokálními servery. Odděluje servisní logiku LCS Client od podkladové síťové topologie. Bez DS by musel být každý LCS Client staticky nakonfigurován adresami všech možných lokálních serverů, což je nepraktický přístup pro velké, vyvíjející se nebo propojené sítě. Služba je definována napříč více specifikacemi 3GPP pokrývajícími architekturu, protokoly (jako je Diameter-based LCS Application Protocol) a vzájemné propojení, což zajišťuje, že jak klienti v síti, tak externí aplikační klienti mohou spolehlivě objevovat koncové body polohových služeb.

## K čemu slouží

Discovery Service byla vytvořena k řešení základního bootstrap problému při poskytování polohových služeb: 'Jak klient najde správný server?' V raných implementacích [LCS](/mobilnisite/slovnik/lcs/) klienti často používali předem nakonfigurované nebo pevně zakódované adresy pro [GMLC](/mobilnisite/slovnik/gmlc/). Tento přístup byl nepružný, obtížně spravovatelný ve velkých sítích a zcela selhával v roamingových scénářích, kdy klient v domovské síti potřeboval najít GMLC v navštívené síti. DS poskytuje dynamický, standardizovaný mechanismus vyhledávání, který byl nezbytný pro komerční rozvoj interoperabilních služeb založených na poloze napříč sítěmi více operátorů.

K jejímu vytvoření vedly potřeby škálovatelnosti a automatizace v LCS. S rostoucím počtem LCS Client (např. pro nouzové služby, zákonný odposlech, správu vozového parku a spotřebitelské aplikace) se ruční konfigurace stala hlavní provozní zátěží a zdrojem chyb. DS abstrahuje síťovou složitost, umožňuje přidávání nových lokálních serverů nebo vyřazování starých bez nutnosti aktualizace každého klienta. Dále umožňuje pokročilé funkce, jako je vyrovnávání zátěže mezi servery a objevování na základě vlastní identity klienta nebo požadované úrovně služby. Poskytnutím centralizovaného bodu pro objevování usnadňuje polohové služby mezi PLMN, které jsou klíčové pro směrování nouzových hovorů (E911, eCall) a mezinárodní roamingové služby, a zajišťuje, že žádost o polohu může být správně směrována do sítě, která cílového účastníka aktuálně obsluhuje.

## Klíčové vlastnosti

- Poskytuje adresní informace (např. hostname, IP) příslušného lokálního serveru (GMLC/LMF) pro cílové UE.
- Podporuje objevování na základě různých cílových identifikátorů včetně MSISDN, IMSI a IP adresy.
- Umožňuje objevování mezi PLMN prostřednictvím interakce s LCS Roaming Exchange (LRX) nebo H-GMLC.
- Může vracet schopnosti serveru, jako jsou podporované metody určování polohy a protokoly LCS.
- Odděluje LCS Client od fyzické síťové topologie lokálních serverů.
- Používá standardizované protokoly, primárně založené na Diameter pro LCS Application Protocol (LCS-AP).

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.220** (Rel-19) — Contact Manager for UICC Applications
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [DS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ds/)
