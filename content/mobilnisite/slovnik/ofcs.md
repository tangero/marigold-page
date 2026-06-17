---
slug: "ofcs"
url: "/mobilnisite/slovnik/ofcs/"
type: "slovnik"
title: "OFCS – Offline Charging System"
date: 2025-01-01
abbr: "OFCS"
fullName: "Offline Charging System"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ofcs/"
summary: "Offline Charging System (OFCS) je funkce základní síťové infrastruktury, která shromažďuje a zpracovává záznamy o účtování (CDR) pro účely vyúčtování po ukončení služebního spojení. Umožňuje operátorů"
---

OFCS je funkce základní síťové infrastruktury, která shromažďuje a zpracovává záznamy o účtování po ukončení služebního spojení pro účely vyúčtování, umožňuje vyúčtování na základě fakturace po použití bez nutnosti řízení kreditů v reálném čas.

## Popis

Offline Charging System (OFCS) je základní součást architektury účtování 3GPP, speciálně navržená pro scénáře fakturace mimo reálný čas. Funguje na principu shromažďování podrobných informací o využití z různých síťových elementů po poskytnutí služby. Primární datovou jednotkou je Charging Data Record ([CDR](/mobilnisite/slovnik/cdr/)), který je generován Charging Trigger Functions ([CTF](/mobilnisite/slovnik/ctf/)) integrovanými v síťových uzlech jako SGSN, GGSN, [P-GW](/mobilnisite/slovnik/p-gw/) nebo S-CSCF. Tyto CTF detekují účtovatelné události – jako začátek, změna nebo ukončení datového spojení, hovoru nebo SMS – a shromažďují relevantní informace do CDR. Tento záznam obsahuje pole jako identita účastníka (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), podrobnosti spojení (čas začátku/konce, délka), identifikátory služby a objem dat.

Architektura OFCS je definována Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) a Charging Gateway Function ([CGF](/mobilnisite/slovnik/cgf/)). CDF přijímá účtovatelné události od CTF přes referenční bod Rf, který používá základní protokol Diameter s Diameter Credit Control Application ([DCCA](/mobilnisite/slovnik/dcca/)). CDF validuje, formátuje a sestavuje tyto události do kompletních, konzistentních CDR. Tyto CDR jsou pak přeneseny na CGF přes referenční bod Ga, typicky pomocí protokolů jako FTP nebo FTPS. CGF funguje jako brána, provádí funkce jako buffering CDR, konsolidace, korelace (např. spojení dílčích záznamů z různých uzlů pro jedno spojení) a zpracování chyb před předáním finalizovaných CDR do Billing Domain (BD) operátora pro dlouhodobé uložení a generování faktur.

OFCS podporuje více servisních domén, zahrnující Circuit Switched (CS) telefony, Packet Switched (PS) data a IP Multimedia Subsystem (IMS) služby, umožňující konvergované účtování. Jeho role je striktně offline; neinteraguje s online stavem účtu nebo neprovádí autorizaci kreditů v reálném čas. Toto oddělení od Online Charging System (OCS) umožňuje flexibilní modely účtování jako měsíční subskripce, tarify na základě objemu a podrobné účtování jednotlivých položek. Design systému zajišťuje spolehlivost a nezpochybnitelnost účtovatelných dat, což je kritické pro zajištění příjmů operátora a regulatorní compliance.

## K čemu slouží

OFCS byl vytvořen k řešení základní businessové potřebě pro přesné, spolehlivé a podrobné účtování telekomunikačních služeb v modelu fakturace po použití. Před standardizovaným offline účtováním operátory závisely na proprietárních systémech, které komplikovaly interoperabilitu a multi-vendor síťové deploymenty. Standardizace OFCS v 3GPP, začínající v Release 6, poskytla unified framework pro shromažďování dat o využití ze všech síťových domén, umožňující operátorům účtovat pro široký array služeb – hlas, data, messaging a multimedia – z jedné, konzistentní platformy.

Jeho vytvoření bylo motivované limity reálného časového účtování pro všechny služby. While online účtování je nezbytné pro prepaid služby, zavádí latenci a komplexnost pro služby, kde immediate řízení kreditů není required. OFCS řeší toto oddělením procesu účtování od cesty poskytnutí služby. Toto umožňuje síti poskytovat služby bez pause pro kontrolu kreditů, zlepšující user experience a síťovou efektivitu pro post-paid customers. Také umožňuje generování podrobných, auditovatelných záznamů nezbytných pro customer invoices, business intelligence, detekci fraud a regulatorní reporting. Evoluce systému byla driven potřebou podporovat nové služby, vyšší objemy dat a více komplexní účtovatelné scénáře introduced v later 3GPP releases.

## Klíčové vlastnosti

- Generování standardizovaných Charging Data Records (CDR) pro všechny servisní domény
- Architektura na základě Charging Data Function (CDF) a Charging Gateway Function (CGF)
- Využívá protokol Diameter přes referenční bod Rf pro sběr událostí
- Podporuje korelaci a konsolidaci CDR pro spojení přesahující více síťových uzlů
- Umožňuje flexibilní, mimo reálný čas modely účtování jako subskripce a tiered data plány
- Poskytuje spolehlivý transfer billing záznamů do Billing Domain operátora

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [CTF – Charging Trigger Function](/mobilnisite/slovnik/ctf/)
- [CDF – Cumulative Distribution Function](/mobilnisite/slovnik/cdf/)
- [CGF – Charging Gateway Functionality](/mobilnisite/slovnik/cgf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 32.820** (Rel-8) — Charging Architecture Study for Evolved 3GPP
- **TS 32.869** (Rel-15) — Diameter Overload Control for Charging Interfaces

---

📖 **Anglický originál a plná specifikace:** [OFCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ofcs/)
