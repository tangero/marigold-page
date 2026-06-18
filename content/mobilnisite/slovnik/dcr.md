---
slug: "dcr"
url: "/mobilnisite/slovnik/dcr/"
type: "slovnik"
title: "DCR – Degradation Category Rating"
date: 2025-01-01
abbr: "DCR"
fullName: "Degradation Category Rating"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dcr/"
summary: "Metoda hodnocení kategorie degradace (DCR) je standardizovaná subjektivní technika hodnocení kvality používaná v 3GPP k vyhodnocení percepční kvality řečových a audio kodeků za různých podmínek degrad"
---

DCR je standardizovaná subjektivní metoda v 3GPP, při níž lidský poslech hodnotí kvalitu zpracované řeči nebo audia ve srovnání s referencí, aby posoudil dopad degradací sítě.

## Popis

Metoda hodnocení kategorie degradace (DCR) je základní subjektivní metodologie hodnocení definovaná v rámci standardizačního rámce 3GPP, primárně používaná pro hodnocení kvality systémů přenosu řeči a audia. Funguje jako komparativní poslechový test, při kterém jsou lidským subjektům předloženy páry řečových vzorků: referenční (vysoce kvalitní, nepoškozený) vzorek následovaný degradovanou verzí téhož vzorku. Degradace je zavedena testovaným systémem a simuluje reálné poruchy sítě, jako je ztráta paketů, omezení šířky pásma, zkreslení kodeku nebo variace zpoždění. Posluchači následně hodnotí vnímanou degradaci na standardizované pětibodové kategorické škále, známé jako škála kategorie degradace ([DCS](/mobilnisite/slovnik/dcs/)). Tato škála se pohybuje od 1 („Degradace je velmi nepříjemná“) do 5 („Degradace je neslyšitelná“), což poskytuje přímé měření percepčního dopadu zavedených poruch.

Z architektonického hlediska se DCR test provádí v kontrolovaných laboratorních podmínkách podle přísných pokynů uvedených v doporučení [ITU-T](/mobilnisite/slovnik/itu-t/) P.800 a jeho dodatků, které jsou odkazem začleněny do specifikací 3GPP. Mezi klíčové komponenty metodologie DCR patří výběr reprezentativního řečového materiálu (pokrývající různé jazyky, pohlaví a fonetický obsah), návrh podmínek degradace (simulující specifické vzorce chyb sítě nebo provozní režimy kodeků), kalibrace poslechového zařízení a důkladný výcvik testovaných subjektů. Testovací relace je pečlivě strukturována, s náhodným předkládáním párů vzorků a dostatečnými přestávkami, aby se zabránilo únavě posluchačů, což zajišťuje statisticky spolehlivé výsledky. Konečným výstupem je střední hodnota známky ([MOS](/mobilnisite/slovnik/mos/)) pro degradaci, často označovaná jako MOS-DCR, která kvantifikuje průměrné hodnocení posluchačů pro konkrétní testovací podmínku.

Role metody DCR v ekosystému 3GPP je nedílnou součástí charakterizace výkonu a standardizace řečových kodeků, jako jsou [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/) a hlasové služby založené na IMS. Poskytuje primární subjektivní metrikou kvality, vůči níž jsou kalibrovány a validovány objektivní měřicí modely (jako [POLQA](/mobilnisite/slovnik/polqa/) nebo [PESQ](/mobilnisite/slovnik/pesq/)). Během vývoje kodeků a výběrových procesů pro nová vydání 3GPP jsou kandidátské kodeky podrobeny DCR testům pod komplexní sadou profilů poruch sítě. To zajišťuje, že vybrané kodeky poskytují přijatelnou percepční kvalitu nejen v ideálních podmínkách, ale také při ztrátě paketů, chvění a omezeních šířky pásma typických pro mobilní sítě. Metoda je tedy klíčovým nástrojem pro definování minimálních požadavků na výkon, optimalizaci režimů kodeků a algoritmů adaptace přenosové rychlosti a v konečném důsledku zaručuje konzistentní a vysoce kvalitní uživatelský zážitek pro hlasové služby napříč sítěmi 3G, 4G a 5G.

## K čemu slouží

Metoda hodnocení kategorie degradace byla vytvořena, aby řešila základní výzvu kvantitativního hodnocení percepční kvality řeči v telekomunikačních systémech, zejména když se sítě vyvíjely od tradičního přepojování okruhů k paketovému přenosu hlasu (VoIP). Předchozí subjektivní metody byly často ad-hoc a postrádaly standardizaci, což ztěžovalo srovnávání výsledků z různých laboratoří nebo definování jednoznačných požadavků na výkon v technických specifikacích. Přechod na hlas založený na IP přinesl nové typy degradací – především ztrátu paketů, proměnlivé zpoždění a tandemové kódování – které nebyly adekvátně zachyceny stávajícími technikami hodnocení navrženými pro okruhové spoje s konstantní přenosovou rychlostí. DCR poskytla standardizovaný, opakovatelný a vědecky rigorózní rámec speciálně přizpůsobený k hodnocení těchto nových typů poruch.

Historický kontext pro přijetí DCR v rámci 3GPP vychází z potřeby vybrat a optimalizovat řečové kodeky pro 3G UMTS a následující generace. Když 3GPP vyvíjelo rodinu kodeků Adaptive Multi-Rate (AMR), potřebovalo spolehlivou metodu pro hodnocení jeho výkonu za chybových rádiových podmínek sítí WCDMA. DCR umožnila inženýrům systematicky měřit, jak různé režimy AMR, techniky maskování chyb a strategie adaptace rádiového spoje ovlivňují kvalitu poslechu při výskytu výmazů rámců (simulujících chyby rádiových bloků). To byl významný pokrok oproti pouhému měření bitové chybovosti (BER) nebo míry výmazů rámců (FER), protože přímo korelovala technické parametry s lidským vnímáním.

Dále DCR vyřešila problém hodnocení kvality ve složitých scénářích s více uzly, charakteristických pro moderní sítě, jako je překódování mezi různými kodeky nebo průchod ztrátovými IP páteřními sítěmi. Použitím čistého referenčního signálu a aplikací celého řetězce zpracování sítě k vytvoření degradovaného vzorku DCR zachycuje kumulativní efekt všech poruch v přenosové cestě. Tento holistický pohled byl zásadní pro definování cílů kvality end-to-end v architektuře QoS 3GPP a pro standardizaci výkonu služeb IMS Multimedia Telephony. Bez DCR by bylo nemožné stanovit prahové hodnoty objektivní kvality, které jsou základem smluv o úrovni služeb (SLA) a zajišťují interoperabilitu mezi síťovými zařízeními různých výrobců.

## Klíčové vlastnosti

- Standardizovaná pětibodová škála kategorie degradace (DCS) pro subjektivní hodnocení
- Struktura testu párového srovnání (reference následovaná degradovaným vzorkem)
- Hodnocení specifických podmínek poruch sítě, jako je ztráta paketů a chvění (jitter)
- Generování metriky střední hodnoty známky pro degradaci (MOS-DCR)
- Základ pro kalibraci objektivních modelů měření kvality (např. POLQA)
- Integrace do procesů výběru kodeků a specifikace výkonu v 3GPP

## Související pojmy

- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)

## Definující specifikace

- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning
- **TR 33.740** (Rel-18) — Security and Privacy Aspects of Proximity Based Services in 5G System Phase 2
- **TS 33.836** (Rel-16) — Security Study for Advanced V2X Services
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [DCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcr/)
