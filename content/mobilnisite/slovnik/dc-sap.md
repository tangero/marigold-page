---
slug: "dc-sap"
url: "/mobilnisite/slovnik/dc-sap/"
type: "slovnik"
title: "DC-SAP – Dedicated Control Service Access Point"
date: 2025-01-01
abbr: "DC-SAP"
fullName: "Dedicated Control Service Access Point"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dc-sap/"
summary: "DC-SAP je logický přístupový bod služby v protokolovém zásobníku UTRAN, konkrétně ve vrstvě řízení rádiových prostředků (RRC). Poskytuje definované rozhraní pro výměnu zpráv vyhrazené řídicí signaliza"
---

DC-SAP je logický přístupový bod služby (Service Access Point) ve vrstvě RRC v UTRAN, který poskytuje rozhraní pro vyhrazené řídicí signalizaci mezi entitou RRC a jejími vyššími vrstvami.

## Popis

Dedicated Control Service Access Point (DC-SAP) je základní koncept v architektuře rádiové přístupové sítě UMTS (UTRAN) podle 3GPP, definovaný v protokolové specifikaci pro řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/), 25.331). Funguje jako logický bod v protokolovém zásobníku jak na straně uživatelského zařízení (UE), tak na straně UTRAN (Node B a Radio Network Controller – RNC). DC-SAP není fyzické rozhraní, ale konceptuální hranice služby, která definuje, jak vrstva RRC nabízí své služby vyhrazeného řízení vyšším vrstvám nezávislým na přístuovém stratum ([NAS](/mobilnisite/slovnik/nas/)), jako jsou entity správy mobility ([MM](/mobilnisite/slovnik/mm/)) a řízení hovoru ([CC](/mobilnisite/slovnik/cc/)).

Z architektonického hlediska vrstva RRC poskytuje služby prostřednictvím několika přístupových bodů služeb (SAP), přičemž primárními jsou DC-SAP a [GC-SAP](/mobilnisite/slovnik/gc-sap/) (General Control SAP). Zatímco GC-SAP zpracovává vysílací informace pro všechn UE v buňce, DC-SAP se konkrétně používá pro signalizační spojení, která jsou jedinečná pro jedno konkrétní UE. Když UE naváže signalizační spojení (např. pro aktualizaci polohy, zřízení hovoru nebo správu relace), vytvoří se vyhrazené řídicí spojení. DC-SAP slouží jako vstupní a výstupní bod pro všechny zprávy RRC týkající se tohoto konkrétního spojení. Abstrahuje podkladové transportní mechanismy, které v UMTS zajišťuje vrstva RLC (Radio Link Control) v potvrzeném ([AM](/mobilnisite/slovnik/am/)) nebo nepotvrzeném (UM) režimu.

Fungování DC-SAP je založeno na modelu primitiv, běžném ve vrstvených komunikačních systémech. Vyšší vrstvy (NAS) komunikují s vrstvou RRC vysíláním servisních primitiv (např. REQUEST, INDICATION, RESPONSE, CONFIRM) prostřednictvím DC-SAP. Tato primitiva nesou parametry, které jsou následně vrstvou RRC zapouzdřeny do specifických protokolových datových jednotek (PDU) RRC, jako jsou RRC Connection Request, Measurement Report nebo Handover Command. Tyto PDU jsou odesílány přes rozhraní vzduchu k síti. Naopak příchozí PDU RRC ze sítě jsou zpracovány vrstvou RRC, která následně vyvolá odpovídající primitivum, jež je doručeno směrem vzhůru přes DC-SAP, aby informovalo vrstvu NAS o událostech nebo síťových příkazech. Tato strukturovaná interakce zajišťuje, že řídicí signalizace pro správu mobility, konfiguraci rádiového přenosového kanálu a přenos schopností UE je zpracována spolehlivým a standardizovaným způsobem, což tvoří páteř správy stavů UE (IDLE, CELL_[FACH](/mobilnisite/slovnik/fach/), CELL_[DCH](/mobilnisite/slovnik/dch/) atd.).

## K čemu slouží

DC-SAP byl zaveden, aby poskytl čisté, standardizované a spolehlivé rozhraní pro vyhrazenou řídicí signalizaci v rámci protokolové architektury UMTS. Před formalizovanou vrstvenou architekturou 3GPP byly mechanismy řídicí signalizace často méně strukturované, což vedlo k potenciálním problémům s interoperabilitou a složitou integrací mezi funkcemi řízení rádiových prostředků a funkcemi řízení jádra sítě. DC-SAP byl vytvořen jako součást specifikace vrstvy RRC, aby tento problém vyřešil jasným oddělením zájmů přístupového stratum (zabývajícího se řízením specifickým pro rádiové rozhraní) a nezávislého přístupového stratum (NAS, zabývajícího se mobilitou a správou relací v jádru sítě).

Jeho vytvoření bylo motivováno potřebou efektivního a dynamického řízení individuálních spojení UE v paketově orientovaném buněčném systému. Na rozdíl od GSM, které mělo více okruhově orientované řízení, UMTS potřebovalo robustní mechanismus pro zvládání zřizování, údržby, rekonfigurace a uvolňování vyhrazených signalizačních spojení pro různé služby. DC-SAP toto poskytuje definováním přesného servisního modelu, který umožňuje vrstvám NAS žádat o rádiové prostředky bez nutnosti rozumět složitým detailům protokolů rádiového rozhraní. Řeší omezení spočívající v ad-hoc nebo implicitních signalizačních cestách tím, že vytváří explicitní, dobře definovanou smlouvu mezi RRC a jeho klienty, což je zásadní pro podporu složitých procedur, jako je měkké předání spojení (soft handover), mezisystémová předání spojení (do/z GSM) a současná správa více rádiových přenosových kanálů pro hlasové a datové služby.

## Klíčové vlastnosti

- Poskytuje logické rozhraní pro řídicí signalizaci specifickou pro UE mezi RRC a vyššími vrstvami
- Používá model servisních primitiv (REQUEST, INDICATION, RESPONSE, CONFIRM) pro strukturovanou interakci
- Podporuje spolehlivý přenos zpráv prostřednictvím podkladového transportu RLC v potvrzeném režimu (Acknowledged Mode)
- Zásadní pro správu procedur navázání, údržby a uvolnění spojení RRC
- Umožňuje přenos zpráv NAS (jako MM, CC, SM) přes rádiové rozhraní
- Umožňuje přechody mezi stavy RRC v UE (IDLE, CELL_DCH, CELL_FACH atd.)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [GC-SAP – General Control Service Access Point](/mobilnisite/slovnik/gc-sap/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [DC-SAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dc-sap/)
