---
slug: "pcch"
url: "/mobilnisite/slovnik/pcch/"
type: "slovnik"
title: "PCCH – Paging Control Channel"
date: 2025-01-01
abbr: "PCCH"
fullName: "Paging Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pcch/"
summary: "Downlinkový logický transportní kanál v UMTS a LTE, který síť využívá k vyvolání nečinných nebo neaktivních uživatelských zařízení (UE). Doručuje vyvolávací zprávy, aby upozornila UE na příchozí hovor"
---

PCCH je downlinkový logický transportní kanál v UMTS a LTE, který slouží k vyvolání nečinných nebo neaktivních uživatelských zařízení (User Equipment) zprávami o příchozích hovorech, datech nebo změnách systému.

## Popis

Paging Control Channel (PCCH) je logický transportní kanál definovaný v architekturách UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) i LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)). Funguje výhradně ve směru downlink, tedy ze sítě k uživatelskému zařízení (UE). Jeho hlavní funkcí je přenášet transportní bloky Paging Channel ([PCH](/mobilnisite/slovnik/pch-text-pch/)), které obsahují vyvolávací zprávy. Tyto zprávy slouží k upozornění UE v nečinném režimu ([RRC](/mobilnisite/slovnik/rrc/)_IDLE v LTE, stavy Idle/Cell_PCH/[URA](/mobilnisite/slovnik/ura/)_PCH v UMTS) nebo v některých případech v neaktivním režimu na síťové události vyžadující jejich pozornost.

V protokolové architektuře je PCCH logickým kanálem na vrstvě Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Je namapován na transportní kanál Paging Channel ([PCH](/mobilnisite/slovnik/pch/)), který je následně namapován na fyzický kanál. V UMTS je PCH namapován na Secondary Common Control Physical Channel (S-CCPCH). V LTE je PCH namapován na Physical Downlink Shared Channel (PDSCH), přičemž plánovací informace pro vyvolávací zprávu jsou poskytovány prostřednictvím Physical Downlink Control Channel (PDCCH) pomocí specifického P-RNTI (Paging Radio Network Temporary Identifier). Toto mapování umožňuje efektivní sdílení fyzických zdrojů.

Provoz PCCH je úzce spojen s cyklem nespojitého příjmu (DRX) UE. Aby se šetřila energie baterie, UE nepřetržitě nesleduje vyvolávací kanál. Místo toho se probouzejí v konkrétních, předem definovaných intervalech (paging occasions) v rámci svého DRX cyklu, aby zkontrolovala vyvolávací zprávy na PCCH. Síť zná DRX cyklus UE a vypočítává správný okamžik pro vyvolání. Vyvolávací zpráva může označovat příchozí hlasový hovor (CS fallback), mobilně ukončenou datovou relaci, upozornění systému pro varování před zemětřesením a tsunami (ETWS), oznámení Commercial Mobile Alert System (CMAS) nebo změnu systémových informací vyžadující, aby UE znovu získala vysílací kanál. PCCH tedy umožňuje síti udržovat dosažitelnost milionů nečinných UE a zároveň těmto UE umožňuje dosáhnout významné úspory energie.

## K čemu slouží

PCCH existuje, aby vyřešil základní problém síťově iniciovaného kontaktu s mobilním zařízením, které není aktivně v hovoru nebo datové relaci. V každém buněčném systému musí být síť schopna lokalizovat a upozornit konkrétní UE na příchozí komunikaci nebo kritické oznámení. Před vyhrazenými vyvolávacími kanály používaly rané systémy neefektivní metody, které spotřebovávaly nadměrnou energii baterie UE a rádiové zdroje.

V UMTS (od Release 99) byl PCCH definován jako součást strukturované architektury logických a transportních kanálů, aby poskytoval spolehlivý a efektivní vyvolávací mechanismus. Oddělil vyvolávací provoz od ostatních řídicích a uživatelských dat, což umožnilo optimalizované plánování a přenos. Jeho návrh zahrnoval podporu různých stavů UE (jako Cell_PCH a URA_PCH v UMTS) pro vyvážení zatížení vyvolávací signalizace a režie správy mobility UE.

S příchodem LTE zůstal účel PCCH ústřední, ale jeho implementace se vyvinula, aby využila all-IP a sdílenou povahu kanálů v systému. Přechod k mapování PCCH na sdílený PDSCH, spíše než na vyhrazený fyzický kanál jako v UMTS, zvýšil spektrální účinnost. Role PCCH se rozšířila za tradiční vyvolávání, aby podporovala pokročilé funkce, jako je ETWS a CMAS pro veřejnou bezpečnost, a usnadňovala energeticky efektivní provoz prostřednictvím sofistikovaných mechanismů DRX, které jsou klíčové pro paradigmata neustálého připojení moderních smartphonů a IoT zařízení.

## Klíčové vlastnosti

- Logický kanál pouze pro downlink určený k doručování vyvolávacích zpráv
- Podporuje úsporu energie UE prostřednictvím nespojitého příjmu (DRX)
- Přenáší oznámení pro mobilně ukončené hovory, relace a změny systémových informací
- Umožňuje efektivní lokalizaci nečinných UE napříč oblastmi sledování (tracking areas) nebo směrovacími oblastmi (routing areas)
- Podporuje systémy veřejného varování (ETWS, CMAS)
- Namapován na sdílené fyzické zdroje (PDSCH v LTE) pro spektrální účinnost

## Související pojmy

- [PCH – Paging Channel](/mobilnisite/slovnik/pch/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.314** (Rel-19) — E-UTRA Radio Measurements Specification
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcch/)
