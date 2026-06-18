---
slug: "rcaf"
url: "/mobilnisite/slovnik/rcaf/"
type: "slovnik"
title: "RCAF – RAN Congestion Awareness Function"
date: 2025-01-01
abbr: "RCAF"
fullName: "RAN Congestion Awareness Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rcaf/"
summary: "Síťová funkce, která monitoruje a hlásí přetížení v rádiové přístupové síti (RAN) do jádra sítě. Umožňuje řízení provozu na základě politik a úpravy QoS při vysokém zatížení, čímž zlepšuje efektivitu"
---

RCAF je síťová funkce, která monitoruje a hlásí přetížení v rádiové přístupové síti, aby umožnila řízení provozu na základě politik a úpravy QoS při vysokém zatížení.

## Popis

RAN Congestion Awareness Function (RCAF) je funkční entita zavedená ve specifikaci 3GPP Release 13, primárně definovaná v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Funguje jako logická funkce, která může být integrována v rámci rádiové přístupové sítě (RAN), například v eNodeB nebo gNB, nebo jako samostatný síťový prvek. Jejím hlavním úkolem je detekovat a kvantifikovat podmínky přetížení na specifických rádiových zdrojích, jako jsou buňky, sledovací oblasti nebo rádiové přístupové technologie. RCAF monitoruje klíčové ukazatele výkonu, jako je využití rádiových zdrojů, počet aktivních uživatelů a zatížení provozem, a převádí tyto surové metriky na standardizované reporty o přetížení. Tyto reporty jsou následně komunikovány do funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) v jádru sítě prostřednictvím standardizovaných rozhraní, jako je Rx nebo N5, v závislosti na generaci sítě (EPC nebo 5GC). Tato komunikace umožňuje, aby rámec pro politiky měl přehled o podmínkách v RAN v reálném čase, což byla schopnost, která v dřívějších vydáních z velké části chyběla. RCAF sama politiky přímo nevynucuje; místo toho funguje jako poskytovatel informací, který umožňuje inteligentní, na kontextu založená rozhodnutí o politikách v jádru sítě. V systému 5G jsou principy RCAF integrovány do funkce Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) pro komplexnější analýzy, ale samostatná RCAF zůstává specifikována pro určitá nasazení a rozhraní, což zajišťuje zpětnou kompatibilitu a specifické scénáře reportování přetížení. Její architektura je navržena jako škálovatelná a technologicky neutrální, podporující reportování přetížení pro LTE, NR a dokonce i pro ne-3GPP typy přístupu, pokud jsou zřízena relevantní rozhraní.

## K čemu slouží

RCAF byla vytvořena, aby vyřešila kritickou mezeru mezi podmínkami zatížení v RAN a vynucováním politik v jádru sítě. Před jejím zavedením byla rozhodnutí o politikách v architektuře [PCC](/mobilnisite/slovnik/pcc/) primárně založena na profilech účastníků, tocích služebních dat a podmínkách v jádru sítě, s omezeným přehledem o přetížení na rádiovém rozhraní v reálném čase. To často vedlo k neefektivní alokaci zdrojů, kdy mohly být služby s vysokou prioritou omezeny nebo blokovány během přetížení v RAN, aniž by systém politik znal hlavní příčinu, nebo naopak politiky nemohly proaktivně zmírňovat přetížení úpravou provozu. Motivace vycházela z rostoucí poptávky po mobilních datech a potřeby sofistikovanějšího řízení provozu pro zajištění kvality uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)), zejména pro služby citlivé na zpoždění, jako je VoLTE nebo hry v reálném čase. Poskytnutím informace o přetížení v RAN pro [PCRF](/mobilnisite/slovnik/pcrf/)/[PCF](/mobilnisite/slovnik/pcf/) získali operátoři schopnost implementovat dynamická pravidla politik reagující na zatížení sítě. Například během přetížení mohl systém politik dočasně omezit aplikace s vysokými nároky na šířku pásma a nízkou prioritou nebo upřednostnit nouzové služby, čímž optimalizoval celkové využití sítě a udržel kvalitu služeb pro kritické uživatele. To představovalo významný vývoj směrem k inteligentnějším sítím reagujícím na podmínky, a připravilo cestu pro pozdější analytické funkce v 5G.

## Klíčové vlastnosti

- Monitoruje ukazatele přetížení v RAN v reálném čase, jako je zatížení buňky a využití zdrojů
- Generuje standardizované reporty o přetížení pro funkce řízení politik
- Komunikuje s PCRF v EPC přes Rx a s PCF v 5GC přes N5
- Podporuje reportování přetížení na úrovni buňky, sledovací oblasti nebo RAT
- Umožňuje dynamické úpravy politik na základě rádiových podmínek
- Usnadňuje správu QoS a směrování provozu při vysokém zatížení

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.153** (Rel-19) — Ns Reference Point Protocol between SCEF and RCAF
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification
- **TS 29.405** (Rel-19) — Nq-AP Protocol Specification
- **TS 29.810** (Rel-13) — Diameter Load Control Study
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [RCAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcaf/)
