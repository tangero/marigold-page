---
slug: "emm"
url: "/mobilnisite/slovnik/emm/"
type: "slovnik"
title: "EMM – Evolved Mobility Management"
date: 2025-01-01
abbr: "EMM"
fullName: "Evolved Mobility Management"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/emm/"
summary: "EMM je protokol a stavový automat v systémech EPS a 5GS, který spravuje mobilitu a bezpečnostní kontext uživatelského zařízení (UE). Zpracovává procedury jako připojení (attach), odpojení (detach), ak"
---

EMM je protokol a stavový automat v systémech EPS a 5GS, který spravuje mobilitu, bezpečnostní kontext a dosažitelnost uživatelského zařízení (UE) prostřednictvím procedur, jako je připojení (attach), odpojení (detach) a autentizace.

## Popis

Evolved Mobility Management (EMM) je základní protokol a entita pro správu stavu definovaná pro Evolved Packet System (EPS) a zachovaná v systému 5G (5GS). Působí v řídicí rovině mezi uživatelským zařízením (UE) a entitou Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v jádru sítě 4G nebo funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. EMM je zodpovědné za vytváření, udržování a uvolňování kontextu správy mobility uživatelského zařízení (UE), což je nezbytné pro to, aby síť znala polohu UE (na úrovni sledovací/směrovací oblasti) a jeho stav připojení (EMM-REGISTERED nebo EMM-DEREGISTERED). Tento kontext je klíčový pro umožnění sítě stránkovat UE pro příchozí relace a autentizovat zařízení pro přístup k síti.

Protokol definuje specifické EMM procedury, které jsou iniciovány sítí nebo uživatelským zařízením. Klíčové procedury iniciované UE zahrnují počáteční připojení (Attach), které registruje UE v síti a vytváří výchozí přenosový kanál (bearer), a aktualizaci sledovací oblasti (Tracking Area Update – TAU), která informuje síť o přesunu UE do nové sledovací oblasti. Procedury iniciované sítí zahrnují autentizaci a řízení bezpečnostního režimu (Security Mode Control) pro navázání šifrování a ochrany integrity a odpojení (Detach) pro řádné odstranění kontextu UE. EMM spolupracuje s protokolem [ESM](/mobilnisite/slovnik/esm/) (EPS Session Management), který spravuje přenosové kanály; EMM procedury často přenášejí zprávy ESM jako užitečné zatížení.

Stavy EMM jsou ústřední pro jeho fungování. Hlavními stavy jsou EMM-DEREGISTERED, kdy MME/AMF o UE neví, a EMM-REGISTERED, kdy kontext existuje. Uvnitř stavu EMM-REGISTERED podstavy jako EMM-IDLE a EMM-CONNECTED indikují, zda je aktivní signalizační spojení k rádiové přístupové síti. Přechody mezi těmito stavy jsou spouštěny specifickými událostmi, jako je úspěšné připojení (z deregistrován na registrován) nebo uvolnění spojení (z připojen na nečinný). Protokol zajišťuje, že bezpečnostní klíče jsou navázány během registrace a jsou použity k ochraně všech následných signalizačních zpráv [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum), čímž poskytuje bezpečný základ pro správu mobility.

## K čemu slouží

EMM bylo vytvořeno jako součást System Architecture Evolution (SAE) ve specifikaci 3GPP Release 8 za účelem poskytnutí jednotného rámce pro správu mobility založeného na IP pro nové Evolved Packet Core (EPC). Předchozí systémy 3GPP, jako [GPRS](/mobilnisite/slovnik/gprs/) a UMTS, měly správu mobility ([GMM](/mobilnisite/slovnik/gmm/)), která byla těsněji provázána s okruhově spínanou doménou a starší síťovou architekturou. Účelem EMM bylo navrhnout čistší a efektivnější protokol optimalizovaný pro plně IP sítě, podporující bezproblémovou mobilitu mezi 3GPP a ne-3GPP přístupovými sítěmi (jako Wi-Fi).

Řešil problém správy mobility v plošší síťové architektuře, kde byla řídicí rovina (zajišťovaná [MME](/mobilnisite/slovnik/mme/)) oddělena od uživatelské roviny. EMM poskytuje standardizovaný způsob, jak mohou UE a síť vyjednávat schopnosti, navazovat zabezpečení a udržovat informace o poloze bez režie starších okruhově spínaných paradigmat. Jeho vytvoření bylo motivováno potřebou vyšších přenosových rychlostí, nižší latence a zjednodušené síťové architektury vyžadované pro LTE a položilo základy pro správu mobility v 5G, kde se vyvinulo v [NAS](/mobilnisite/slovnik/nas/) protokol pro registraci a správu připojení zajišťovaný funkcí AMF.

## Klíčové vlastnosti

- Spravuje registraci a deregistraci uživatelského zařízení (UE) v jádru sítě
- Zpracovává procedury aktualizace sledovací oblasti (TAU) a aktualizace směrovací oblasti (RAU) pro mobilitu
- Provádí autentizaci a navazuje zabezpečení na úrovni NAS (šifrování a ochrana integrity)
- Spravuje stavový automat EMM (Deregistrován, Registrován-Nečinný, Registrován-Připojen)
- Podporuje stránkování iniciované sítí pro lokalizaci nečinných uživatelských zařízení (UE)
- Přenáší zprávy správy relací (ESM) mezi uživatelským zařízením (UE) a MME/AMF

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [ESM – Energy Savings Management](/mobilnisite/slovnik/esm/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions

---

📖 **Anglický originál a plná specifikace:** [EMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/emm/)
