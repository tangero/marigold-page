---
slug: "hr"
url: "/mobilnisite/slovnik/hr/"
type: "slovnik"
title: "HR – Half Rate"
date: 2026-01-01
abbr: "HR"
fullName: "Half Rate"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hr/"
summary: "GSM Half Rate (HR) je řečový kodek a režim kanálu, který sníží potřebnou přenosovou rychlost hovoru na polovinu oproti plné rychlosti (Full Rate), a tím efektivně zdvojnásobí kapacitu sítě. Používá vo"
---

HR je řečový kodek a režim kanálu GSM, který pracuje s přibližně 5,6 kbit/s a sníží přenosovou rychlost hovoru na polovinu oproti plné rychlosti (Full Rate), čímž zdvojnásobí kapacitu sítě.

## Popis

GSM Half Rate (HR) je základní režim kanálu a příslušný řečový kodek v systému GSM. Na fyzické vrstvě obvykle kanál pro přenos hovoru (TCH) nese hovor s plnou rychlostí ([FR](/mobilnisite/slovnik/fr/)) s hrubou přenosovou rychlostí 22,8 kbit/s. Režim poloviční rychlosti umožňuje multiplexovat dva samostatné hovory na jeden fyzický TCH přidělením každému hovoru struktury polovičního slotu, čímž efektivně pracuje s hrubou přenosovou rychlostí přibližně 11,4 kbit/s na hovor. Jádrem HR je řečový kodek (původně definovaný v GSM 06.20), který využívá algoritmus Vector Sum Excited Linear Prediction (VSELP) ke kompresi řečového signálu na čistou přenosovou rychlost asi 5,6 kbit/s, doplněnou o kanálové kódování pro ochranu proti chybám.

Z pohledu architektury sítě je režim HR řízen řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). BSC na základě vytížení sítě a konfigurace může rozhodnout o přiřazení příchozího hovoru na kanál s poloviční rychlostí namísto kanálu s plnou rychlostí. Toto rozhodnutí zahrnuje signalizaci směrem k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) a základnové stanici ([BTS](/mobilnisite/slovnik/bts/)) pro nastavení odpovídajícího kanálového kódování a využití časového slotu. MS musí podporovat HR kodek, aby se mohla takového hovoru účastnit. Kanálové kódování pro HR je robustnější než u FR, aby kompenzovalo nižší přenosovou rychlost; využívá vyšší podíl bitů pro opravu chyb, aby zachovalo kvalitu hovoru i v mezních rádiových podmínkách.

Úlohou HR v síti GSM bylo primárně zvýšení kapacity. Umožněním dvou hovorů na jeden fyzický rádiový časový slot efektivně zdvojnásobilo hlasovou kapacitu buňky bez potřeby dodatečného kmitočtového spektra nebo hardwaru. Toto však bylo vykoupeno snížením kvality hovoru oproti FR, zejména v hlučném prostředí. HR bylo často používáno jako nástroj pro zvýšení kapacity během špiček nebo v hustě osídlených oblastech, zatímco FR bylo preferováno pro lepší kvalitu. Jeho specifikace jsou udržovány napříč vydáními 3GPP kvůli zpětné kompatibilitě, i když byly zavedeny pokročilejší kodeky jako Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) a Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)).

## K čemu slouží

GSM Half Rate bylo vyvinuto na počátku 90. let 20. století jako odpověď na naléhavou potřebu zvýšení kapacity sítě v době exponenciálního růstu počtu účastníků GSM. Původní kodek GSM Full Rate využíval pro jeden hovor jeden časový slot. S omezeným spektrem a pevným počtem slotů na nosnou se operátoři potýkali s rychlým vyčerpáním kapacity. Technologie HR byla přímým řešením tohoto problému spektrální účinnosti, které operátorům umožnilo obsloužit více účastníků se stejnou infrastrukturní investicí.

Řešila ekonomickou nutnost maximalizace návratnosti investic do drahých kmitočtových licencí a nasazení základnových stanic. Před širokým přijetím spektrálně účinnějších digitálních technik, jako byla HR, by operátoři potřebovali stavět více buněk – což byl nákladný a pomalý proces. HR poskytlo zvýšení kapacity realizovatelné softwarovou aktualizací. Ačkoli obětovalo část kvality hovoru, tento kompromis byl považován za přijatelný vzhledem k výraznému zisku kapacity, zejména pro síť primárně zaměřenou na hlasové služby. HR připravilo cestu pro pozdější sofistikovanější adaptivní kodeky, jako je [AMR](/mobilnisite/slovnik/amr/), které dokážou dynamicky přepínat mezi režimy kodeků (včetně HR) na základě stavu sítě a požadavků na kvalitu.

## Klíčové vlastnosti

- Zdvojnásobí hlasovou kapacitu přenosem dvou hovorů v jednom fyzickém kanálu pro přenos hovoru
- Používá řečový kodek založený na VSELP s čistou přenosovou rychlostí přibližně 5,6 kbit/s
- Řízeno BSC prostřednictvím algoritmů přidělování kanálů
- Vyžaduje specifické kanálové kódování pro ochranu proti chybám při nižší přenosové rychlosti
- Mobilní stanice musí podporovat funkci HR
- Představuje kompromis mezi kapacitou a kvalitou řeči

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TR 28.827** (Rel-18) — Technical Report on 5G Charging for Roaming Scenarios
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [HR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hr/)
