---
slug: "psm"
url: "/mobilnisite/slovnik/psm/"
type: "slovnik"
title: "PSM – Protocol State Machine"
date: 2025-01-01
abbr: "PSM"
fullName: "Protocol State Machine"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/psm/"
summary: "Formální model definující stavy a přechody entity komunikačního protokolu. Zajišťuje spolehlivou a uspořádanou výměnu zpráv mezi síťovými uzly řízením procedur navázání spojení, přenosu dat a obnovy p"
---

PSM je formální model definující stavy a přechody protokolové entity za účelem zajištění spolehlivé výměny zpráv řízením navázání spojení, přenosu dat a obnovy po chybě.

## Popis

Protocol State Machine (PSM, Stroj konečných stavů protokolu) je abstrakce stroje konečných stavů používaná ve specifikacích 3GPP k formální definici chování protokolové entity. Modeluje entitu jako množinu různých stavů (např. IDLE, CONNECTED, ACTIVE) a událostí (např. přijetí zprávy, vypršení časovače, interní spouštěč), které způsobují přechody mezi těmito stavy. Každý stav představuje konkrétní podmínku protokolu a každý přechod je spojen se sadou akcí, které mají být provedeny, jako je odeslání protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), spuštění nebo zastavení časovače či aktualizace interních proměnných. Tato formalizace je klíčová pro zajištění interoperability mezi zařízeními od různých výrobců, protože poskytuje jednoznačnou specifikaci toho, jak má protokol reagovat za všech možných okolností.

Architektura PSM je typicky dokumentována v přílohách specifikací protokolů pomocí diagramů a tabulek přechodů stavů. Mezi klíčové komponenty patří stavové proměnné, které uchovávají aktuální provozní kontext; časovače, které chrání před uváznutím a spouštějí retransmise nebo resetování stavů; a obslužné rutiny událostí, které zpracovávají příchozí podněty. PSM funguje tak, že kontinuálně čeká na událost. Když událost nastane, entita zkontroluje, zda je pro aktuální stav a danou událost definován platný přechod. Pokud ano, provede přidružené akce a přejde do dalšího stavu. Tento cyklus zajišťuje, že procedury jako připojení (attach), zřízení přenosového kanálu (bearer establishment), předání spojení (handover) a jeho uvolnění (release) jsou prováděny v řízeném a předvídatelném pořadí.

PSM jsou všudypřítomné napříč všemi vrstvami protokolů 3GPP, od protokolů Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), jako jsou [EMM](/mobilnisite/slovnik/emm/) a [ESM](/mobilnisite/slovnik/esm/), které spravují mobilitu a správu relací mezi UE a jádrem sítě, přes protokol Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) řídící rozhraní vzduchu, až po signalizační protokoly v jádru sítě, jako je [GTP-C](/mobilnisite/slovnik/gtp-c/). Jejich úlohou je implementovat procedurální logiku protokolu, řešit normální provoz, výjimečné situace a obnovu po selhání. Definováním jasných předpokladů a následných podmínek pro každou akci PSM předcházejí stavům soutěže (race conditions) a zaručují, že síť dospěje ke stabilnímu, známému stavu, což je zásadní pro spolehlivost služeb a efektivní správu zdrojů.

## K čemu slouží

Protocol State Machine existuje, aby poskytla přísnou, na implementaci nezávislou předlohu pro chování protokolu. Před formálním používáním stavových strojů mohly být specifikace protokolů nejednoznačné, což vedlo k různým interpretacím výrobců zařízení a následně k problémům s interoperabilitou. Formalizmus PSM tento problém řeší převodem textových popisů procedur na přesný matematický model, který ponechává minimální prostor pro nejednoznačnost. To je kritické ve velkých ekosystémech s více výrobci, jako jsou sítě 3GPP, kde je bezproblémová komunikace mezi UE od jednoho výrobce a sítí od jiného základním požadavkem.

Historicky byly komunikační protokoly popisovány pomocí textu a vývojových diagramů, což mohlo být neúplné nebo rozporné při popisu složitého zpracování chyb a okrajových případů. Přijetí modelu stavového stroje, konceptu z teorie automatů a softwarového inženýrství, přineslo do návrhu protokolů inženýrskou disciplínu. Nutí autory specifikací explicitně zvážit všechny možné události v každém stavu a definovat tak úplný behaviorální kontrakt. To nejen pomáhá implementátorům, ale také usnadňuje techniky formální verifikace, kdy lze stavový stroj analyzovat z hlediska vlastností, jako je živost (protokol bude postupovat) a absence uváznutí (deadlock).

Motivace přesahuje počáteční implementaci až k testování a odstraňování problémů. Soubory testů shody (conformance test suites) jsou vytvářeny přímo z definic PSM, přičemž testovací případy jsou navrženy tak, aby ověřily každý stav a přechod. Když dojde k problémům v síti, inženýři mohou vysledovat problém k selhání konkrétního přechodu stavu, což činí diagnostiku systematičtější. Model navíc podporuje vývoj protokolů napříč vydáními; změny mohou být jasně dokumentovány jako úpravy stavů, událostí nebo přechodů, což pomáhá průmyslu zvládat zpětnou a dopřednou kompatibilitu.

## Klíčové vlastnosti

- Definuje konečnou množinu stavů reprezentujících podmínky protokolu
- Specifikuje události, které spouštějí přechody mezi stavy
- Spojuje konkrétní akce (např. odeslání zprávy, spuštění časovače) s každým přechodem
- Zahrnuje časovače pro dohledové a obnovovací procedury
- Poskytuje formální model pro jednoznačnou implementaci a testování
- Zajišťuje deterministické chování pro garanci interoperability

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/psm/)
