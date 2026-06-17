---
slug: "eps"
url: "/mobilnisite/slovnik/eps/"
type: "slovnik"
title: "EPS – Evolved Packet System"
date: 2026-01-01
abbr: "EPS"
fullName: "Evolved Packet System"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eps/"
summary: "Evolved Packet System (EPS) je standardizovaná architektura organizace 3GPP pro sítě 4G LTE, která zahrnuje rádiový přístup (E-UTRAN) a paketové jádro (EPC). Poskytuje plně IP konektivitu pro vysokory"
---

EPS je síťová architektura 4G LTE standardizovaná organizací 3GPP, zahrnující rádiový přístup a paketové jádro, která poskytuje plně IP konektivitu pro vysokorychlostní mobilní širokopásmové služby.

## Popis

Evolved Packet System (EPS) je kompletní síťový systém definovaný organizací 3GPP pro bezdrátovou komunikaci Long-Term Evolution (LTE). Skládá se ze dvou hlavních domén: Evolved Universal Terrestrial Radio Access Network ([E-UTRAN](/mobilnisite/slovnik/e-utran/)), tvořený stanicemi evolved NodeB ([eNB](/mobilnisite/slovnik/enb/)), a Evolved Packet Core (EPC). Architektura EPS představuje zásadní odklon od předchozích systémů 3GPP, protože přijímá plně IP, plochý design s menším počtem síťových uzlů za účelem snížení latence a zvýšení datové propustnosti. Jejím hlavním úkolem je poskytovat zabezpečenou, bezproblémovou IP konektivitu mezi uživatelským zařízením (UE) a externími paketovými datovými sítěmi (PDN), jako je internet nebo privátní firemní sítě.

V srdci EPC se nachází několik klíčových logických entit. Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) zpracovává řídicí rovinu (control-plane), jako je signalizace [NAS](/mobilnisite/slovnik/nas/), autentizace UE, správa sledovacích oblastí (tracking area) a vytváření přenosových kanálů (bearer). Serving Gateway (S-GW) funguje jako kotva (anchor) v uživatelské rovině (user-plane) během předávání spojení (handover) v rámci LTE a směruje datové pakety mezi eNB a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)). P-GW představuje kritické rozhraní k externím PDN a vykonává přidělování IP adres, vynucování pravidel (policy enforcement), účtování (charging) a filtrování paketů. Mezi další nezbytné komponenty patří Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data účastníků a Policy and Charging Rules Function (PCRF) pro pravidla kvality služeb (QoS) a účtování. Konektivita je řízena prostřednictvím přenosových kanálů EPS (EPS bearers) – logických tunelů se specifickými parametry QoS, které sahají od UE až k P-GW.

EPS funguje tak, že při přihlášení (attach) UE k síti vytvoří výchozí přenosový kanál EPS (default EPS bearer), což zajišťuje trvalou IP konektivitu (always-on). Tento kanál je asociován s IP adresou a výchozím profilem QoS. Vyhrazené kanály (dedicated bearers) se zaručeným datovým tokem ([GBR](/mobilnisite/slovnik/gbr/)) mohou být zřizovány na požádání pro služby jako VoIP nebo videostreamování. Řídicí rovina (signaling) a uživatelská rovina (data) jsou odděleny, přičemž rozhraní S1 (S1-MME pro řídicí rovinu, S1-U pro uživatelskou) spojuje E-UTRAN s EPC. Systém podporuje mobilitu v rámci LTE (prostřednictvím předání spojení mezi eNB založeného na rozhraní X2), mobilitu do/z dědičných sítí 2G/3G (prostřednictvím rozhraní S3/S4 ke SGSN) a mobilitu v režimu nečinnosti (idle-mode) s aktualizacemi sledovací oblasti (tracking area update). Zabezpečení je zajištěno vzájemnou autentizací mezi UE a sítí pomocí klíčů z HSS a šifrováním/zajištěním integrity signalizace a datových přenosových kanálů.

## K čemu slouží

EPS byl vytvořen jako součást projektu 3GPP LTE zahájeného kolem roku 2004 s cílem reagovat na explodující poptávku po mobilních datech a omezení stávající architektury 3G UMTS/[HSPA](/mobilnisite/slovnik/hspa/). Jádrová síť UMTS (GPRS Core) byla evolucí přepojování okruhů (circuit-switched) z GSM, s komplexní hierarchií a více tunelovacími protokoly, což vedlo k vyšší latenci a suboptimální datové efektivitě. Průmysl potřeboval systém od základů optimalizovaný pro paketově přepínaná data (packet-switched), aby podporoval vysokorychlostní služby s nízkou latencí, jako je mobilní video, hry v reálném čase a VoIP.

Hlavním účelem EPS bylo zjednodušit síťovou architekturu a dramaticky snížit počet uzlů zapojených do přenosu dat, čímž se sníží náklady a latence. Zavedl „plochou“ architekturu, kde se eNB připojuje přímo k bráně (S-GW/P-GW), čímž odstraňuje Radio Network Controller (RNC) ze systému 3G. Tento plně IP design zjednodušuje přenos (transport), snižuje provozní náklady a usnadňuje zavádění nových služeb. EPS byl dále navržen tak, aby bezproblémově spolupracoval se stávajícími přístupovými technologiemi 3GPP (2G/3G) i non-3GPP (např. Wi-Fi, CDMA), a poskytoval tak kontinuitu služeb. Vyřešil problém síťové složitosti a latence, což umožnilo zážitek z mobilního broadbandu 4G. EPS se svým EPC vytvořil páteř pro služby LTE a později se vyvinul tak, aby se stal základem integrovaným s 5G Core (5GC) v nasazeních 5G non-standalone (NSA).

## Klíčové vlastnosti

- Plně IP, plochá síťová architektura snižující latenci a náklady.
- Oddělení řídicí roviny (MME) a uživatelské roviny (S-GW, P-GW).
- Trvalá konektivita (always-on) prostřednictvím zřízení výchozího přenosového kanálu EPS (default EPS bearer).
- Podpora více úrovní kvality služeb (QoS) prostřednictvím vyhrazených a výchozích přenosových kanálů.
- Bezproblémová mobilita v rámci LTE a do/z sítí 2G/3G.
- Integrované funkce řízení pravidel (PCRF) a účtování (PCEF).

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [E-UTRAN – Evolved Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/e-utran/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TS 23.261** (Rel-19) — IP Flow Mobility between 3GPP and WLAN
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- … a dalších 78 specifikací

---

📖 **Anglický originál a plná specifikace:** [EPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/eps/)
