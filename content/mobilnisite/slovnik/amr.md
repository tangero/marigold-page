---
slug: "amr"
url: "/mobilnisite/slovnik/amr/"
type: "slovnik"
title: "AMR – Adaptive Multi-Rate"
date: 2025-01-01
abbr: "AMR"
fullName: "Adaptive Multi-Rate"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/amr/"
summary: "AMR je rodina řečových kodeků standardizovaná 3GPP pro sítě GSM, UMTS a LTE. Dynamicky přizpůsobuje přenosovou rychlost podle stavu kanálu, aby optimalizovala kvalitu hlasu a kapacitu sítě. To je klíč"
---

AMR je rodina řečových kodeků standardizovaná 3GPP pro mobilní sítě, která dynamicky přizpůsobuje svůj přenosový rychlost podle stavu rádiového kanálu za účelem optimalizace kvality hlasu a kapacity sítě.

## Popis

Kodek Adaptive Multi-Rate (AMR) je rodina algoritmů pro kódování řeči navržená pro systémy mobilní komunikace. Funguje tak, že komprimuje digitalizované řečové signály do řady přenosových rychlostí, od 4,75 kbit/s do 12,2 kbit/s pro úzkopásmový AMR a od 6,60 kbit/s do 23,85 kbit/s pro širokopásmový AMR ([AMR-WB](/mobilnisite/slovnik/amr-wb/)). Základním principem je adaptace rychlosti řízená zdrojem, kdy je režim kodeku (přenosová rychlost) vybírán na základě vyhodnocení kvality rádiového kanálu a vytížení sítě v reálném čase. Tento výběr řídí síť prostřednictvím vestavěné signalizace nebo explicitních řídicích zpráv, což systému umožňuje podle potřeby upřednostnit buď kvalitu hlasu, nebo kapacitu.

Z architektonického hlediska je AMR integrován do řetězce zpracování hlasu v uživatelském zařízení (UE) a v Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) páteřní sítě. Kodek využívá pro úzkopásmový přenos Algebraic Code-Excited Linear Prediction ([ACELP](/mobilnisite/slovnik/acelp/)) a jeho modifikovanou verzi pro širokopásmový přenos, což poskytuje efektivní modelování hlasového ústrojí a excitačního signálu. Mezi klíčové komponenty patří kodér/dekodér řeči (kodek), detektor hlasové aktivity (VAD) pro přerušovaný přenos ([DTX](/mobilnisite/slovnik/dtx/)) a generátor komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) pro maskování přenosových mezer. Kodek pracuje ve spolupráci s kanálovým kódováním a prokládáním na fyzické vrstvě, aby zajistil odolnost vůči chybám.

V síti hraje AMR klíčovou roli v přenosové dráze hlasu. Pro hlas s přepojováním okruhů v sítích GSM a UMTS je aplikován přímo přes rozhraní vzduchu, přičemž TRAU (Transcoder and Rate Adaptation Unit) nebo MGW zajišťují adaptaci rychlosti a překódování na/ze síťových kodeků PSTN, jako je G.711. Pro Voice over LTE (VoLTE) a Voice over NR (VoNR) se jako primární kodek v rámci IP Multimedia Subsystem (IMS) používá AMR-WB, zapouzdřený v paketech RTP/UDP/IP. Přizpůsobivost kodeku umožňuje rádiové přístupové síti (RAN) nařídit nižší přenosovou rychlost při špatných rádiových podmínkách, čímž zvýší ochranu kanálovým kódováním a udrží kontinuitu hovoru, nebo vyšší přenosovou rychlost pro lepší kvalitu za dobrých podmínek.

Vývoj směrem k AMR-WB (uváděnému na trh jako [HD](/mobilnisite/slovnik/hd/) Voice) rozšířil zvukové pásmo z 300–3400 Hz na 50–7000 Hz, což výrazně zlepšilo přirozenost a srozumitelnost. To si vyžádalo aktualizace v celém hlasovém řetězci, včetně akustických komponent v zařízeních a podpory širšího pásma v sítích. Konstrukce AMR také usnadňuje plynulé předávání hovorů mezi různými technologiemi rádiového přístupu (např. z GSM na UMTS) prostřednictvím renegociace režimu kodeku a překódování v páteřní síti. Jeho standardizovaná rámcová struktura a řídicí mechanismy zajišťují interoperabilitu mezi různými výrobci a operátory, což z něj činí základní technologii pro globální mobilní hlasové služby.

## K čemu slouží

AMR byl vytvořen, aby odstranil omezení řečových kodeků s pevnou přenosovou rychlostí používaných v raných digitálních mobilních systémech, jako je GSM, které používaly kodeky Full-Rate ([FR](/mobilnisite/slovnik/fr/)) a Half-Rate (HR). Tyto pevné kodeky se nemohly přizpůsobit měnícím se rádiovým podmínkám: kodek FR poskytoval konzistentní, ale někdy nedostatečnou kvalitu při rušení, zatímco kodek HR nabízel vyšší kapacitu, ale nižší kvalitu. Hlavní motivací bylo dynamicky optimalizovat kompromis mezi kvalitou hlasu a spektrální účinností, což sítím umožňuje udržovat přijatelnou kvalitu při přetížení nebo špatném pokrytí a maximalizovat kapacitu za ideálních podmínek.

Historicky bylo zavedení AMR v 3GPP Release 99 (pro GSM) a jeho přijetí pro UMTS poháněno potřebou jednotného a robustního hlasového kodeku, který by mohl využít pokrok v digitálním zpracování signálu. Vyřešil problém neefektivního využití spektra tím, že umožnil síti nařídit nižší přenosovou rychlost (a tedy silnější ochranu proti chybám) při scénářích na okraji buňky nebo při rušení, čímž se snížil počet přerušených hovorů. Naopak za dobrých podmínek mohl používat vyšší přenosové rychlosti pro audio kvality blízké kvalitě přenosu po pevných linkách. Tato přizpůsobivost byla klíčová pro podporu vyšších hustot uživatelů a zlepšení celkové spolehlivosti služeb.

AMR navíc poskytl migrační cestu pro vylepšené hlasové služby. Položil základy pro širokopásmový přenos zvuku (AMR-WB), který řešil rostoucí poptávku po hlasových službách vysoké kvality, jak se sítě vyvíjely směrem k architekturám s přepojováním paketů IMS v LTE a 5G. Standardizací jediné, přizpůsobivé rodiny kodeků zajistilo 3GPP zpětnou kompatibilitu a plynulou spolupráci mezi staršími a moderními sítěmi, snížilo složitost pro operátory a umožnilo konzistentní kvalitu hlasu napříč generacemi.

## Klíčové vlastnosti

- Dynamická adaptace přenosové rychlosti od 4,75 do 12,2 kbit/s (úzkopásmový režim) na základě stavu kanálu
- Podpora širokopásmového zvuku (AMR-WB) s kmitočtovým pásmem 50–7000 Hz pro HD Voice
- Výběr rychlosti řízený zdrojem a spravovaný sítí pro optimální kompromis mezi kvalitou a kapacitou
- Integrovaný detektor hlasové aktivity (VAD) a přerušovaný přenos (DTX) pro úsporu energie
- Odolnost vůči přenosovým chybám díky synergii adaptace spojení a kanálového kódování
- Standardizovaná rámcová struktura umožňující interoperabilitu mezi různými výrobci a překódování

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TR 24.930** (Rel-19) — IMS Session Setup Signalling Flows
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- … a dalších 53 specifikací

---

📖 **Anglický originál a plná specifikace:** [AMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/amr/)
