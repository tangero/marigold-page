---
slug: "s1ap"
url: "/mobilnisite/slovnik/s1ap/"
type: "slovnik"
title: "S1AP – S1 Application Protocol"
date: 2025-01-01
abbr: "S1AP"
fullName: "S1 Application Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/s1ap/"
summary: "S1 Application Protocol (S1AP) je signalizační protokol řídicí roviny používaný na rozhraní S1 mezi E-UTRAN (eNodeB) a Evolved Packet Core (EPC), konkrétně MME. Spravuje kontext UE, zřizování přenosov"
---

S1AP je řídicí protokol používaný na rozhraní S1 mezi LTE rádiovou sítí (eNodeB) a jádrem sítě (MME) pro správu spojení, mobility a relací.

## Popis

Protokol S1 Application Protocol (S1AP) funguje na rozhraní [S1-MME](/mobilnisite/slovnik/s1-mme/), což je řídicí spojení mezi eNodeB v rádiové přístupové síti a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v jádru sítě. Jde o protokol vrstvy 3, který jako spolehlivou transportní vrstvu nad IP používá [SCTP](/mobilnisite/slovnik/sctp/) (Stream Control Transmission Protocol). S1AP je zodpovědný za všechny signalizační procedury potřebné ke správě spojení a mobility uživatelského zařízení (UE) mezi rádiovým přístupem a jádrem sítě.

Protokol definuje soubor elementárních procedur (EPs), které jsou základními jednotkami interakce. Tyto procedury se dělí do třídy 1 (vyžadující odpověď) a třídy 2 (odpověď není vyžadována). Mezi klíčové procedury patří Initial UE Context Setup, která zřizuje první signalizační spojení pro UE a aktivuje výchozí přenosové kanály; procedura UE Context Modification pro aktualizaci parametrů kanálů; a procedury přípravy a provedení předání spojení (Handover Preparation and Execution) pro správu mobility mezi eNodeB nebo k jiným 3GPP rádiovým technologiím. S1AP také zajišťuje vyvolávání (paging) pro lokalizaci nečinných (idle) UE, přenos zpráv [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) pro přenos signalizace mezi UE a MME a funkce indikace chyb.

Z architektonického hlediska jsou zprávy S1AP zapouzdřeny v paketech SCTP. Každý SCTP stream může nést více dialogů S1AP. Protokol používá jedinečné identifikátory, jako je [eNB](/mobilnisite/slovnik/enb/) UE S1AP ID a MME UE S1AP ID, aby koreloval zprávy týkající se konkrétního kontextu UE napříč rozhraním. Návrh S1AP odděluje signalizaci na vrstvě rádiové sítě od transportní vrstvy, což poskytuje robustnost a efektivitu pro kritické řídicí funkce. V architekturách 5G Non-Standalone ([NSA](/mobilnisite/slovnik/nsa/)) ([EN-DC](/mobilnisite/slovnik/en-dc/), [NGEN-DC](/mobilnisite/slovnik/ngen-dc/)) se S1AP nadále používá pro spojení mezi LTE eNodeB a jádrem EPC, zatímco nový protokol NGAP slouží pro spojení 5G NR s 5GC.

## K čemu slouží

S1AP byl vytvořen jako součást standardu 3GPP Long Term Evolution (LTE) za účelem poskytnutí standardizovaného, IP-based řídicího protokolu pro nové rozhraní S1. Předchozí 3GPP systémy, jako UMTS, používaly jinou sadu protokolů (např. RANAP přes rozhraní Iu-CS a Iu-PS), které byly vázány na starší okruhově a paketově orientované architektury. Přechod na plochou, plně IP architekturu v LTE si vyžádal nový, zjednodušený protokol.

Hlavním problémem, který S1AP řeší, je umožnění efektivní a spolehlivé signalizace pro správu mobility, správu relací a správu přenosových kanálů mezi RAN a samostatným, centralizovaným řídicím uzlem v jádře (MME). Odděluje složitost rádiové sítě od inteligence jádra sítě, což umožňuje škálovatelná a flexibilní nasazení sítí. Jeho vytvoření bylo motivováno potřebou snížení latence, vyšší kapacity pro signalizaci a podpory plynulé mobility v novém, na pakety optimalizovaném systému LTE.

## Klíčové vlastnosti

- Spravuje zřízení počátečního kontextu UE a aktivaci přenosových kanálů
- Řídí procedury předání spojení (handover) v rámci LTE a mezi různými RAT
- Přenáší zprávy NAS mezi UE a MME
- Iniciuje vyvolání (paging) UE v nečinném režimu (idle mode)
- Zajišťuje přenos informací o schopnostech UE
- Podporuje procedury ošetření chyb a resetování rozhraní S1

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [NGAP – Next Generation Application Protocol](/mobilnisite/slovnik/ngap/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)

---

📖 **Anglický originál a plná specifikace:** [S1AP na 3GPP Explorer](https://3gpp-explorer.com/glossary/s1ap/)
