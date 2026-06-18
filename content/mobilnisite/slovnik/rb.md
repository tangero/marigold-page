---
slug: "rb"
url: "/mobilnisite/slovnik/rb/"
type: "slovnik"
title: "RB – Resource Block"
date: 2025-01-01
abbr: "RB"
fullName: "Resource Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rb/"
summary: "Základní jednotka přidělování fyzických radiových zdrojů v LTE (E-UTRA) a NR. Je to časově-frekvenční mřížka používaná pro přenos dat a řídicích informací. LTE RB má šířku 180 kHz a délku 0,5 ms, zatí"
---

RB je základní jednotkou přidělování fyzických radiových zdrojů v LTE a NR, tvořící časově-frekvenční mřížku používanou pro přenos dat a řídicích informací.

## Popis

Resource Block (RB) je nejmenším prvkem radiových zdrojů, který může plánovač přidělit uživateli na rádiovém rozhraní LTE a NR. Představuje dvourozměrné přidělení v časové a frekvenční doméně. V LTE je definice pevná: jeden Resource Block ve frekvenční doméně tvoří 12 po sobě jdoucích podnosných, každá s rozestupem 15 kHz, což dává celkovou šířku pásma 180 kHz. V časové doméně jeden Resource Block zabírá jeden slot o délce 0,5 ms (7 [OFDM](/mobilnisite/slovnik/ofdm/) symbolů pro normální cyklickou předponu). Základní LTE Resource Block je tedy mřížka 12 podnosných × 7 symbolů (84 Resource Elements pro normální [CP](/mobilnisite/slovnik/cp/)). Síťový plánovač přiděluje celočíselné počty těchto RB různým UE v každém 1ms přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)), který se skládá ze dvou slotů.

V NR je koncept flexibilnější, aby podporoval různá kmitočtová pásma a případy užití. NR Resource Block je definován jako 12 po sobě jdoucích podnosných ve frekvenční doméně. Rozestup podnosných ([SCS](/mobilnisite/slovnik/scs/)) však není pevně nastaven na 15 kHz; může být 15, 30, 60, 120 nebo 240 kHz (s 480 a 960 kHz pro budoucí studium). Absolutní šířka pásma NR RB se tedy mění s SCS (např. 180 kHz pro SCS 15 kHz, 3,84 MHz pro SCS 240 kHz). V časové doméně je plánování NR založeno na slotech, ale délka slotu se také mění nepřímo úměrně s SCS (např. 1 ms pro 15 kHz, 0,125 ms pro 120 kHz). NR fyzická vrstva je definována pomocí Resource Grids, složených z Resource Elements (jedna podnosná po dobu jednoho OFDM symbolu). Resource Block je skupina používaná pro signalizaci přidělení zdrojů.

Přidělování RB je dynamické a provádí jej vrstva Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) na základě plánovacích algoritmů, které berou v úvahu ukazatele kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), stav vyrovnávací paměti, požadavky QoS a koordinaci interference. Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) a Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) přenášejí uživatelská data namapovaná na přidělené RB. Řídicí kanály (PDCCH, PUCCH) jsou také mapovány na konkrétní Resource Elements, často na okrajích kmitočtového pásma nosné. Počet RB v šířce pásma kanálu definuje konfiguraci přenosové šířky pásma kanálu, která je vždy menší nebo rovna celkové RF šířce pásma, aby bylo možné vyčlenit ochranná pásma.

## K čemu slouží

Resource Block byl vytvořen jako standardizovaná, granularní jednotka pro flexibilní a efektivní sdílení spektra mezi více uživateli v systémech založených na OFDMA, jako jsou LTE a NR. Předchozí technologie, jako UMTS, používaly mnohonásobný přístup s kódovým dělením (CDMA), kde byly zdroje primárně odděleny rozprostíracími kódy, což ztěžovalo jemně granularní plánování ve frekvenční doméně. Přechod na OFDMA vyžadoval novou základní jednotku zdrojů, kterou by bylo možné snadno přidělovat v časové i frekvenční doméně, aby bylo možné využít diverzitu více uživatelů a frekvenčně selektivní útlum.

RB řeší problém, jak rozdělit souvislou časově-frekvenční rovinu zdrojů na spravovatelné, přidělitelné bloky pro plánování, přizpůsobení spoje a signalizaci. Poskytuje stavební kámen pro adaptivní modulaci a kódování (výběr MCS může být na skupinu RB), techniky řízení interference, jako je částečné frekvenční využití, a agregaci nosných (kde mohou být RB přiděleny napříč více komponentními nosnými). Jeho pevná struktura v LTE (12 podnosných) byla kompromisním návrhem pro vyvážení granularity plánování, režie řídicí signalizace a složitosti implementace. Flexibilnější definice RB v NR řeší omezení LTE modelu a umožňuje efektivní provoz v obrovském rozsahu spektra od pásem pod 1 GHz až po milimetrové vlny a pro služby s velmi odlišnými požadavky na latenci a šířku pásma, jako je massive IoT a ultra-spolehlivá komunikace s nízkou latencí (URLLC).

## Klíčové vlastnosti

- Definován jako 12 po sobě jdoucích podnosných ve frekvenční doméně
- Časové trvání je jeden slot (LTE: pevné 0,5 ms, NR: mění se s SCS)
- Základní jednotka pro dynamické paketové plánování (OFDMA)
- Šířka pásma se mění s rozestupem podnosných v NR
- Používán pro mapování datových (PDSCH/PUSCH) i řídicích kanálů
- Umožňuje frekvenčně selektivní plánování a koordinaci interference

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 33.821** (Rel-9) — LTE/SAE Security Threat Analysis and Countermeasures
- **TS 34.109** (Rel-19) — UE Conformance Test Functions for UMTS
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- … a dalších 56 specifikací

---

📖 **Anglický originál a plná specifikace:** [RB na 3GPP Explorer](https://3gpp-explorer.com/glossary/rb/)
