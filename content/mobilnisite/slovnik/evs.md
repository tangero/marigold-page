---
slug: "evs"
url: "/mobilnisite/slovnik/evs/"
type: "slovnik"
title: "EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)"
date: 2025-01-01
abbr: "EVS"
fullName: "Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/evs/"
summary: "Vysoce kvalitní audio kodek a servisní rámec pro hlasové služby přes LTE (VoLTE) a další služby založené na IP. Režim AMR-WB IO zajišťuje zpětnou kompatibilitu s široce rozšířeným kodekem AMR-WB, což"
---

EVS je vysoce kvalitní audio kodek a servisní rámec pro VoLTE a služby založené na IP, jehož režim AMR-WB IO zajišťuje zpětnou kompatibilitu se staršími sítěmi využívajícími AMR-WB pro bezproblémovou interoperabilitu.

## Popis

Enhanced Voice Services (EVS) je komplexní audio kodek a servisní rámec standardizovaný 3GPP, navržený primárně pro Voice over LTE (VoLTE), Voice over NR (VoNR) a další komunikační služby založené na IP Multimedia Subsystem (IMS). Představuje významný skok ve kvalitě hlasu, efektivitě a odolnosti ve srovnání s předchozími kodeky, jako jsou [AMR-NB](/mobilnisite/slovnik/amr-nb/) a [AMR-WB](/mobilnisite/slovnik/amr-wb/). Samotný kodek EVS je velmi univerzální, podporuje široké rozpětí přenosových rychlostí, šířek pásma (od úzkopásmového po superširokopásmové) a režimů provozu. Kritickým provozním režimem je režim AMR-WB Interoperable (AMR-WB IO).

Režim AMR-WB IO je specifická funkce kodeku EVS, která zaručuje interoperabilitu se stávajícím kodekem Adaptive Multi-Rate Wideband (AMR-WB), jenž byl základním kamenem služeb [HD](/mobilnisite/slovnik/hd/) Voice v sítích 3G/4G. Z architektonického hlediska během sestavování hovoru probíhá vyjednávání kodeku prostřednictvím nabídek/odpovědí protokolu Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) v rámci signalizace IMS. Pokud jeden koncový bod podporuje pouze AMR-WB a druhý podporuje EVS, může koncový bod s podporou EVS aktivovat svůj režim AMR-WB IO. V tomto režimu kodek EVS kóduje a dekóduje audio pomocí formátu bitového toku, který je plně dekódovatelný standardním dekodérem AMR-WB.

Jeho fungování je složité. Kodek EVS v režimu AMR-WB IO používá stejné základní pásmo (50-7000 Hz) a rámcovou strukturu (20 ms) jako AMR-WB. Generuje bitový tok, který odpovídá specifikaci AMR-WB při konkrétních přenosových rychlostech (např. 12,65 kbps, 15,85 kbps, 18,25 kbps, 19,85 kbps, 23,05 kbps, 23,85 kbps). To umožňuje staršímu přijímači zpracovat audio bez jakékoli znalosti EVS. Proces kódování na straně EVS však může využívat pokročilejší algoritmy (jako je vylepšená odolnost proti šumu nebo lepší maskování ztrát paketů), aby potenciálně dosáhl lepší zvukové kvality než nativní kodér AMR-WB při stejné přenosové rychlosti – koncept známý jako 'vylepšení kodéru'.

Jeho role v síti je klíčová pro hladké zavedení nadřazené hlasové technologie. Odstraňuje problém 'zelené bubliny' u hlasu a zajišťuje, že mezi jakoukoli kombinací zařízení EVS a AMR-WB lze vždy navázat vysoce kvalitní hovor. Tato zpětná kompatibilita byl klíčový konstrukční cíl, který měl chránit investice operátorů do stávajících nasazení HD Voice a zajistit konzistentní uživatelský zážitek během mnohaletého přechodu na plnohodnotné sítě EVS. EVS prostřednictvím režimů jako je AMR-WB IO je základní součástí multimediální telefonní služby IMS, která umožňuje křišťálově čistý hlas jako základní úroveň pro 5G a další generace.

## K čemu slouží

EVS byl vytvořen, aby uspokojil rostoucí poptávku po ještě vyšší kvalitě hlasových služeb, než jakou mohl poskytnout [AMR-WB](/mobilnisite/slovnik/amr-wb/), a optimalizoval hlas pro paketové sítě jako LTE a 5G NR. Zatímco AMR-WB ([HD](/mobilnisite/slovnik/hd/) Voice) byl velkým zlepšením oproti úzkopásmovému přenosu, stále existovala poptávka po superširokopásmovém a plnopásmovém audiu, lepším výkonu v hlučném prostředí a efektivnějším využití rádiového pásma. Stávající kodeky nebyly optimalizovány pro charakteristiky ztrát paketů a kolísání zpoždění (jitter) vlastní IP sítím.

Hlavním problémem, který EVS řeší, je poskytnutí budoucím potřebám odolného, vysoce kvalitního hlasového kodeku, který je zároveň povinný pro soulad s profilem VoLTE/VoNR, čímž zajišťuje minimální laťku kvality. Obrovskou výzvou však byla nainstalovaná základna stovek milionů zařízení s podporou AMR-WB. Zavedení nového, nekompatibilního kodeku by fragmentovalo ekosystém hlasu a vytvořilo scénáře, ve kterých by kvalita hovoru přešla na úzkopásmový [AMR-NB](/mobilnisite/slovnik/amr-nb/), pokud by jedno zařízení nemělo podporu EVS. To by zhoršilo uživatelský zážitek a zpomalilo adopci.

Režim AMR-WB IO byl důmyslným řešením tohoto problému interoperability, motivovaným potřebou plynulého přechodu. Umožnil operátorům nasadit EVS ve svých sítích a na nových telefonech s garancí, že tato nová zařízení mohou stále navazovat vysoce kvalitní HD Voice hovory s obrovskou starší základnou. Tato funkce zpětné kompatibility byla klíčovým komerčním a technickým hnacím motorem pro přijetí EVS, neboť zajišťovala, že jej lze zavést jako skutečné vylepšení bez narušení stávajících služeb. Odstranila tak omezení přístupu 'od nuly' tím, že postavila most mezi generacemi hlasových technologií.

## Klíčové vlastnosti

- Režim AMR-WB Interoperable (IO) pro zaručenou zpětnou kompatibilitu
- Vynikající zvuková kvalita s podporou superširokopásmového (50-14000 Hz) a plnopásmového (20-20000 Hz) přenosu
- Vylepšená odolnost vůči ztrátám paketů a šumu v pozadí
- Široké rozpětí přenosových rychlostí od 5,9 kbps do 128 kbps pro flexibilitu služeb
- Provoz s ohledem na stav kanálu s adaptací režimu kodeku (např. EVS-CMR)
- Efektivní nespojitý přenos (DTX) pro úsporu energie

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.250** (Rel-19) — IVAS Codec Introduction
- … a dalších 38 specifikací

---

📖 **Anglický originál a plná specifikace:** [EVS na 3GPP Explorer](https://3gpp-explorer.com/glossary/evs/)
