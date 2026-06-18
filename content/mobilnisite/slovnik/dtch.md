---
slug: "dtch"
url: "/mobilnisite/slovnik/dtch/"
type: "slovnik"
title: "DTCH – Dedicated Traffic Channel"
date: 2025-01-01
abbr: "DTCH"
fullName: "Dedicated Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtch/"
summary: "DTCH je logický kanál v UMTS a LTE, který přenáší uživatelská data vyhrazená pro jedno koncové zařízení (UE). Jedná se o bod-bod, obousměrný kanál zřízený po nastavení rádiového přenosového kanálu pro"
---

DTCH je vyhrazený obousměrný logický kanál v UMTS a LTE, který po zřízení rádiového přenosového kanálu přenáší uživatelská aplikační data bod-bod pro jedno koncové zařízení (UE).

## Popis

Dedicated Traffic Channel (DTCH) je základní logický kanál v rádiové protokolové architektuře 3GPP, definovaný pro systémy UMTS (3G) i LTE (4G). Logický kanál je definován typem přenášených informací. DTCH je přenosový kanál, což znamená, že jeho jediným účelem je přenos uživatelských dat. Je 'vyhrazený' (dedicated), protože je přidělen konkrétnímu koncovému zařízení (UE) na dobu trvání datové relace, čímž vytváří bod-bod spojení mezi UE a sítí. To kontrastuje se společnými kanály, které sdílí všechna UE v buňce. DTCH přenáší veškerá data aplikační vrstvy, jako jsou webové stránky, video streamy, pakety VoIP nebo stahované soubory, pro dané konkrétní UE.

V protokolovém zásobníku existuje DTCH na vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Je mapován na transportní kanály, které jsou následně mapovány na fyzické kanály. Toto mapování je konfigurovatelné a je klíčovou součástí správy rádiových prostředků. V UMTS může být DTCH mapován na vyhrazené transportní kanály, jako je Dedicated Channel ([DCH](/mobilnisite/slovnik/dch/)), nebo na sdílené kanály, jako je High-Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)) v [HSPA](/mobilnisite/slovnik/hspa/). V LTE, které je v downlinku zcela založeno na sdílených kanálech, je DTCH vždy mapován na sdílené transportní kanály: Downlink Shared Channel ([DL-SCH](/mobilnisite/slovnik/dl-sch/)) a Uplink Shared Channel ([UL-SCH](/mobilnisite/slovnik/ul-sch/)). Vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) je zodpovědná za zřizování, rekonfiguraci a uvolňování rádiových přenosových kanálů, které využívají DTCH, na základě požadavků na QoS služby vyžádané UE.

Provoz DTCH je vázán na zřízení rádiového přenosového kanálu. Když UE zahájí datovou relaci (např. aktivuje [PDP](/mobilnisite/slovnik/pdp/) kontext v UMTS nebo PDN připojení v LTE), jádrová síť požádá RAN o nastavení rádiového přenosového kanálu se specifickými parametry QoS (např. garantovaný přenosový výkon, priorita, rozpočet zpoždění). RAN nakonfiguruje potřebné prostředky, což zahrnuje vytvoření logického kanálu DTCH pro tento přenosový kanál. Vrstva MAC poté využívá plánovací algoritmy pro multiplexování dat z více DTCH (a dalších logických kanálů) od různých UE na sdílené fyzické rádiové prostředky. V downlinku rozhoduje plánovač v eNodeB (LTE) nebo NodeB (UMTS), která data DTCH kterého UE mají být přenesena v každém přenosovém časovém intervalu. V uplinku vysílá UE podle přidělení (grantů) přijatých od sítě. DTCH je identifikován identifikátorem logického kanálu (LCID) uvnitř vrstvy MAC, což příjemci umožňuje správně demultiplexovat datové toky.

Konfigurace DTCH přímo definuje uživatelský zážitek. Parametry jako modulační a kódovací schéma, množství plánovaných prostředků a procesy Hybrid ARQ (HARQ) jsou všechny řízeny tak, aby splňovaly cíle QoS spojené s rádiovým přenosovým kanálem DTCH. Pro služby vyžadující nízké zpoždění (např. hraní her) bude plánovač upřednostňovat časté přidělování malých přenosových příležitostí pro DTCH daného UE. Pro služby s vysokou propustností (např. streamování videa) přidělí větší bloky prostředků. DTCH tedy není jen pasivní přenosovou cestou, ale dynamicky řízeným prostředkem, který je klíčový pro schopnost rádiové sítě efektivně doručovat různé služby s požadovanou kvalitou.

## K čemu slouží

DTCH existuje, aby poskytoval strukturovaný mechanismus, který je vědomý si QoS, pro doručování uživatelských dat přes rádiové rozhraní v celulární síti. Před standardizovanými logickými kanály, jako je DTCH, byly mechanismy přenosu dat méně flexibilní a integrované. Zavedení DTCH řešilo potřebu efektivní, vyhrazené alokace prostředků pro jednotlivé uživatele ve sdíleném médiu, což je nezbytné pro podporu jak služeb s garantovanými parametry podobných okruhově spínaným, tak i služeb s přenosem paketových dat s proměnným tokem v rámci jednotné architektury.

Jeho vývoj byl motivován evolucí od čistě hlasově orientovaných sítí 2G k sítím 3G (UMTS) a 4G (LTE) s podporou multimédií. V GSM používal uživatelský provoz pro hovor vyhrazený fyzický kanál (TCH), ale koncept byl pevněji svázán s fyzickou vrstvou. DTCH jako logický kanál zavedl vrstvu abstrakce. Tato abstrakce odděluje požadavek služby (přenést uživatelská data pro UE X s QoS Y) od fyzické implementace (které konkrétní kódy, časové sloty nebo bloky prostředků použít). Toto oddělení je klíčové pro pokročilé rádiové techniky, jako je dynamická alokace kanálů, provoz se sdílenými kanály (HSPA, LTE) a sofistikované plánování paketů, které se přizpůsobuje rychle se měnícím rádiovým podmínkám a požadavkům provozu.

DTCH řeší problém multiplexování více datových toků s různými požadavky na stejné fyzické rádiové prostředky. Tím, že existuje vyhrazený logický kanál pro každý rádiový přenosový kanál každého UE, může síť aplikovat odlišné zpracování QoS, prioritu a mechanismy opravy chyb na každý datový tok. Například hovor VoIP a stahování souboru na pozadí pro stejné UE by byly přenášeny na samostatných DTCH s různou konfigurací, což síti umožňuje upřednostnit pakety VoIP citlivé na zpoždění. Tato detailní kontrola je zásadní pro poskytování mixu služeb slibovaných sítěmi 3G a 4G, od hlasu a videokonferencí po prohlížení webu a komunikaci mezi stroji, vše přes společnou paketově spínanou infrastrukturu.

## Klíčové vlastnosti

- Bod-bod logický kanál vyhrazený pro jedno koncové zařízení (UE)
- Přenáší veškerá uživatelská data (IP pakety) pro konkrétní rádiový přenosový kanál
- Existuje ve vrstvě řízení přístupu k médiu (MAC) protokolového zásobníku
- Mapován na transportní kanály (např. DCH v UMTS, DL-SCH/UL-SCH v LTE)
- Konfigurace je definována řízením rádiových prostředků (RRC) na základě požadavků QoS
- Identifikován identifikátorem logického kanálu (LCID) pro multiplexování/demultiplexování

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [DTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtch/)
