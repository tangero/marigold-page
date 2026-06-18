---
slug: "psnr"
url: "/mobilnisite/slovnik/psnr/"
type: "slovnik"
title: "PSNR – Peak Signal-to-Noise Ratio"
date: 2025-01-01
abbr: "PSNR"
fullName: "Peak Signal-to-Noise Ratio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/psnr/"
summary: "Objektivní metrika používaná k posouzení kvality zpracovaného nebo komprimovaného videa nebo obrazu jeho porovnáním s původním nekomprimovaným zdrojem. Měří poměr mezi maximálním možným výkonem signál"
---

PSNR je objektivní metrika používaná v 3GPP k hodnocení kvality videa nebo obrazu měřením poměru mezi maximálním možným výkonem signálu a výkonem zkreslujícího šumu.

## Popis

Peak Signal-to-Noise Ratio (PSNR) je matematická, objektivní metrika hodnocení kvality vyjádřená v decibelech (dB). V kontextu multimediálních specifikací 3GPP se používá ke kvantifikaci věrnosti rekonstruovaného snímku videa nebo obrazu poté, co prošel zpracováním, jako je kódování, dekódování, přenos a skrytí chyb. 'Signálem' je v tomto případě původní referenční data (např. nezpracovaný snímek videa ve formátu YUV) a 'šumem' je chyba nebo zkreslení zavedené zpracovatelským řetězcem, vypočítané jako rozdíl mezi původním a zpracovaným signálem. Vyšší hodnota PSNR značí menší rozdíl a tedy vyšší kvalitu rekonstrukce, ačkoli ne vždy dokonale koreluje se subjektivním lidským vnímáním.

Výpočet PSNR pro video typicky probíhá pro každý snímek zvlášť, často pro složku jasu (Y), protože lidský vizuální systém je citlivější na zkreslení jasu. Proces začíná výpočtem střední kvadratické chyby ([MSE](/mobilnisite/slovnik/mse/)) mezi původním a zpracovaným snímkem. MSE je průměr druhých mocnin rozdílů intenzity každého pixelu. PSNR je pak odvozeno z MSE pomocí vzorce: PSNR = 10 * log10( (MAX_I)^2 / MSE ), kde MAX_I je maximální možná hodnota pixelu (např. 255 pro 8bitové vzorky). Tento vzorec ukazuje, že PSNR je logaritmická míra poměru mezi špičkovým výkonem signálu (druhá mocnina maximální hodnoty) a výkonem šumu (MSE). Pro barevné video lze PSNR vypočítat samostatně pro složky Y, U a V a někdy je zprůměrovat.

V pracovních skupinách pro Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a Media Streaming v rámci 3GPP slouží PSNR jako klíčový ukazatel výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)) při charakterizaci a výběru kodeků. Jeho úlohou je poskytovat reprodukovatelný, kvantitativní etalon pro porovnání různých standardů video kódování (jako H.264/[AVC](/mobilnisite/slovnik/avc/), H.265/[HEVC](/mobilnisite/slovnik/hevc/), H.266/[VVC](/mobilnisite/slovnik/vvc/)), parametrů kódování (datový tok, kvantizace) a nástrojů odolnosti proti chybám. Testovací plány ve specifikacích jako 26.904 definují přísné metodologie pro výpočet PSNR za různých síťových podmínek (např. při ztrátě paketů). Ačkoli je PSNR klíčové pro inženýrská porovnání, často se používá společně se subjektivními testovacími metodami (jako je Mean Opinion Score - [MOS](/mobilnisite/slovnik/mos/)), protože PSNR nemusí zachytit určité typy percepčních artefaktů, které jsou pro diváky rušivější, ale přispívají méně k číselné hodnotě MSE.

## K čemu slouží

PSNR existuje jako základní inženýrský nástroj pro objektivní a automatické hodnocení výkonnosti algoritmů a systémů komprese videa. Primární problém, který řeší, je potřeba rychlé, konzistentní a nákladově efektivní metody pro porovnání výstupní kvality různých kodeků nebo nastavení kódování během vývoje, standardizace a plánování sítě. Subjektivní testování s lidskými pozorovateli, ačkoli je konečným etalonem, je časově náročné, drahé a obtížně škálovatelné nebo automatizovatelné. PSNR poskytuje okamžité číselné skóre, které lze integrovat do automatizovaných testovacích pracovišť a regresního testování.

Motivace pro jeho přijetí v 3GPP vychází z potřeby vybrat a specifikovat video kodeky pro mobilní služby, jako je paketově přepínané streamování ([PSS](/mobilnisite/slovnik/pss/)) a MBMS. Během konkurenčních procesů výběru kodeků musí zastánci různých technologií prokázat efektivitu svých návrhů. Křivky PSNR-datový tok, které vynášejí dosažené PSNR vůči požadovanému datovému toku, se staly standardním způsobem porovnání poměru zkreslení a datového toku (rate-distortion) kodeků. To umožnilo rozhodování založená na datech o tom, který kodek poskytuje nejlepší kvalitu při daném omezení šířky pásma – což je klíčový aspekt pro mobilní sítě s omezenými a sdílenými rádiovými prostředky.

Vznik a pokračující používání PSNR však také uznává jeho omezení, která se snaží řešit následný výzkum a standardizační práce. PSNR je metrika rozdílu založená na pixelech, která není dokonale sladěna s lidským viděním; všechny chyby váží stejně, zatímco lidské oko je citlivější na chyby v plochých oblastech než v texturovaných. Toto omezení motivovalo vývoj a zkoumání pokročilejších percepčních metrik kvality (jako SSIM, VMAF) v rámci pozdějších studií 3GPP. Přesto zůstává PSNR široce chápaným a historicky důležitým etalonem díky své jednoduchosti, reprodukovatelnosti a obrovskému množství existujícího výzkumu a výsledků, které na něj spoléhají, což poskytuje společnou základnu pro hodnocení výkonnosti napříč odvětvím.

## Klíčové vlastnosti

- Poskytuje objektivní, číselnou míru věrnosti rekonstrukce v decibelech (dB)
- Vypočítává se ze střední kvadratické chyby (MSE) mezi původním a zpracovaným signálem
- Primárně se aplikuje na složku jasu (Y) pro hodnocení kvality videa
- Používá se k vytváření křivek poměru zkreslení a datového toku (PSNR vs. datový tok) pro porovnání kodeků
- Nedílná součást automatizovaného testování a srovnávání výkonnosti ve specifikacích 3GPP
- Slouží jako klíčová metrika pro hodnocení technik odolnosti proti chybám a skrytí chyb

## Související pojmy

- [MSE – Mobility Speed Estimation](/mobilnisite/slovnik/mse/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.812** (Rel-18) — Technical Report
- **TS 26.855** (Rel-19) — Study on Film Grain Synthesis
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [PSNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/psnr/)
