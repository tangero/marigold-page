---
slug: "cw"
url: "/mobilnisite/slovnik/cw/"
type: "slovnik"
title: "CW – Continuous Wave"
date: 2026-01-01
abbr: "CW"
fullName: "Continuous Wave"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cw/"
summary: "Spojitá nemodulovaná nosná vlna rádiové frekvence. Slouží jako základní referenční signál pro testování, kalibraci a ověřování výkonu rádiových vysílačů a přijímačů v systémech 3GPP. Její čistota a st"
---

CW je spojitá nemodulovaná nosná vlna rádiové frekvence používaná jako základní referenční signál pro testování, kalibraci a ověřování výkonu vysílačů a přijímačů v systémech 3GPP.

## Popis

Continuous Wave (CW) je základní elektromagnetický signál charakterizovaný konstantní amplitudou a frekvencí v čase, prostý jakékoli modulace. V kontextu specifikací 3GPP se CW signály nepoužívají pro přenos uživatelských dat nebo řídicích informací, ale jsou nezbytným nástrojem pro testování a charakterizaci rádiových frekvenčních ([RF](/mobilnisite/slovnik/rf/)) komponent uživatelských zařízení (UE) a základnových stanic (např. NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB). Primární aplikací je testování shody, kdy je CW signál generován testovacím systémem a použit k vyhodnocení klíčových parametrů RF výkonu testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)).

Z technického pohledu CW signál představuje čistý tón na konkrétní nosné frekvenci. Tato jednoduchost umožňuje izolovat a měřit základní charakteristiky hardwaru bez složitosti zavedené modulačními schématy jako [QPSK](/mobilnisite/slovnik/qpsk/) nebo 256-QAM. Mezi klíčové výkonnostní testy používající CW patří měření přesnosti výstupního výkonu vysílače, hodnocení referenční úrovně citlivosti přijímače a vyhodnocení úniku lokálního oscilátoru a nežádoucích emisí. Stabilita signálu je prvořadá; jakýkoli fázový šum nebo frekvenční drift ve zdroji CW by se přímo přenesl do chyb měření, což z vysokopřesných generátorů signálu činí klíčovou součást testovací sestavy.

Role CW se rozprostírá přes celý životní cyklus rádiového zařízení, od výzkumu a vývoje a typového schvalování přes testování na výrobní lince až po údržbu v terénu. Technické specifikace 3GPP (TS), zejména série 36.521 a 38.521 pro testování shody UE pro LTE a NR, ukládají konkrétní testovací případy používající CW signály. Například pro test maximálního výstupního výkonu UE dá testovací systém příkaz UE, aby vysílala CW na jednom fyzickém bloku zdrojů ([PRB](/mobilnisite/slovnik/prb/)), a výkon se změří pomocí výkonoměru nebo spektrálního analyzátoru. Podobně testy přijímače často zahrnují aplikaci CW signálu na anténní konektor UE, aby se určila minimální úroveň signálu, při které může přijímač dosáhnout stanovené chybovosti bitů ([BER](/mobilnisite/slovnik/ber/)) nebo bloků ([BLER](/mobilnisite/slovnik/bler/)).

Z architektonického hlediska je CW generován externě vůči UE nebo základnové stanici standardizovaným testovacím zařízením. Rozhraním je typicky RF anténní konektor. Vnitřní komponenty DUT – jako výkonový zesilovač, šumově nízký zesilovač, filtry a mixéry – jsou tímto čistým signálem buzeny. Jejich výkonnost je pak posuzována analýzou signálu po jeho průchodu těmito komponenty (pro testy vysílače) nebo schopností DUT detekovat a zpracovat příchozí CW (pro testy přijímače). To poskytuje základní porozumění výkonu analogového RF předkoncového stupně před provedením složitějších testů s modulovanými signály.

Shrnuto, Continuous Wave je základním kamenem validace RF výkonu v sítích 3GPP. Jeho nemodulovaná povaha poskytuje řízený a opakovatelný podnět, který umožňuje přesné kvantifikaci nejzákladnějších, avšak kritických charakteristik rádiového hardwaru, a zajišťuje tak, že všechna zařízení nasazená v síti splňují přísné standardy kvality a interoperability.

## K čemu slouží

Účelem specifikace a použití signálů Continuous Wave ve standardech 3GPP je stanovit základní, jednoznačnou referenci pro testování výkonnosti rádiových frekvencí. Před nástupem složitých digitálních modulačních schémat používaných v buněčné komunikaci byl CW primárním signálem používaným v rádiovém inženýrství. Jeho začlenění do specifikací 3GPP poskytuje nadčasovou a technologicky neutrální metodu pro ověření analogového výkonu [RF](/mobilnisite/slovnik/rf/) komponent, která je nezávislá na konkrétním rádiovém rozhraní (např. WCDMA, OFDMA). To umožňuje izolovat hardwarové nedostatky od problémů s protokolem nebo digitálním zpracováním signálu.

Základní problém, který CW testování řeší, je potřeba přesné a opakovatelné charakterizace hardwaru vysílače a přijímače. Modulované signály obsahují proměnlivé úrovně výkonu a spektrální charakteristiky, které mohou zakrýt měření základních parametrů, jako je absolutní výstupní výkon nebo šumové pozadí přijímače. Použitím čistého, stabilního CW mohou testovací inženýři získat základní měření klíčových metrik, jako je přesnost výkonu, spektrální čistota (např. nežádoucí emise) a citlivost. To je zásadní pro zajištění, že zařízení od různých výrobců spolehlivě spolupracují a nezpůsobují v síti škodlivé rušení.

Historicky se spoléhání na CW pro základní testování vypořádává s omezeními výhradního použití testů s modulovanými signály, na které mohou mít vliv implementačně specifické digitální algoritmy. CW poskytuje společnou 'základní pravdu'. Jeho specifikace v desítkách technických dokumentů 3GPP, od raných specifikací 3G (R99) po nejnovější specifikace 5G NR (Rel-20), podtrhuje jeho trvalou roli. Motivuje konstruktéry zařízení, aby splnili základní minimální úrovně RF výkonu, které tvoří nezbytný základ, na němž jsou vybudovány všechny komunikační protokoly vyšších vrstev a pokročilé funkce.

## Klíčové vlastnosti

- Čistá, nemodulovaná sinusová nosná vlna
- Používá se jako referenční signál pro testování shody RF
- Umožňuje měření výstupního výkonu a přesnosti vysílače
- Umožňuje testování citlivosti a selektivity přijímače
- Kritické pro ověření nežádoucích emisí a spektrální masky
- Poskytuje stabilní základnu pro kalibraci testovacího zařízení

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- **TS 24.607** (Rel-19) — OIP and OIR Supplementary Services Stage 3
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.616** (Rel-19) — Malicious Call Identification (MCID) Protocol
- … a dalších 62 specifikací

---

📖 **Anglický originál a plná specifikace:** [CW na 3GPP Explorer](https://3gpp-explorer.com/glossary/cw/)
