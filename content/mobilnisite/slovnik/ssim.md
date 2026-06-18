---
slug: "ssim"
url: "/mobilnisite/slovnik/ssim/"
type: "slovnik"
title: "SSIM – Structural Similarity Index Measure"
date: 2025-01-01
abbr: "SSIM"
fullName: "Structural Similarity Index Measure"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssim/"
summary: "Percepční metrika, která predikuje kvalitu digitálních obrázků a videí porovnáním zpracované nebo komprimované verze s neporušenou referencí. Posuzuje degradaci na základě charakteristik lidského zrak"
---

SSIM je percepční metrika používaná v 3GPP pro objektivní hodnocení kvality multimediálních služeb porovnáním zpracovaného videa s referencí za účelem predikce kvality založené na lidském vidění.

## Popis

Structural Similarity Index Measure (SSIM) je algoritmus pro hodnocení kvality obrázků a videa s plnou referencí. Na rozdíl od jednoduchých metod sumarizace chyb, jako je střední kvadratická chyba ([MSE](/mobilnisite/slovnik/mse/)) nebo poměr šumové složky k špičkové hodnotě signálu ([PSNR](/mobilnisite/slovnik/psnr/)), které počítají absolutní rozdíly pixelů, SSIM usiluje o modelování vnímané vizuální kvality. Vychází z hypotézy, že lidský zrakový systém je vysoce adaptován na extrakci strukturálních informací ze scény. SSIM proto měří vnímanou změnu ve strukturálních informacích, jasu a kontrastu mezi referenčním (originálním, nezkresleným) obrázkem a zkresleným (např. komprimovaným, přenášeným) obrázkem.

Index SSIM se počítá pro lokální okna (typicky bloky 8x8 nebo 11x11 pixelů) obrázku. Pro každé okno se vypočítají tři porovnávací funkce: porovnání jasu, porovnání kontrastu a porovnání struktury. Jas je odhadován jako střední hodnota intenzity pixelů, kontrast jako směrodatná odchylka a struktura jako normalizované hodnoty pixelů (odečtením střední hodnoty a dělením směrodatnou odchylkou). Tyto tři složky jsou kombinovány multiplikativně za vzniku mapy lokálních indexů SSIM. Celkové skóre SSIM pro celý obrázek je obvykle průměr této mapy lokálních SSIM, což vede k hodnotě mezi -1 a 1, kde 1 označuje dokonalou shodu s referencí.

V rámci 3GPP je SSIM standardizován jako nástroj pro objektivní měření kvality, primárně v rámci Technické specifikační skupiny pro služby a aspekty systému ([SA4](/mobilnisite/slovnik/sa4/)), která se zabývá kodeky a doručováním médií. Specifikace jako 3GPP TS 26.812 (Metriky výkonu pro streamovací služby) a TS 26.955 (Metriky [QoE](/mobilnisite/slovnik/qoe/) pro služby [VR](/mobilnisite/slovnik/vr/)) uvádějí SSIM jako klíčovou metriku. Používá se k vyhodnocení výkonu video kodeků (jako [AVC](/mobilnisite/slovnik/avc/)/H.264, [HEVC](/mobilnisite/slovnik/hevc/)/H.265 a [VVC](/mobilnisite/slovnik/vvc/)/H.266), algoritmů adaptivního streamování s proměnným datovým tokem a mechanismů odolnosti proti chybám za různých síťových podmínek (ztráta paketů, kolísání zpoždění, omezení šířky pásma).

Pro optimalizaci sítě a služeb poskytuje SSIM přesnější korelaci se subjektivním hodnocením lidí (střední hodnota známky kvality - MOS) než PSNR, zejména pro kompresní artefakty typické pro moderní video kodeky. V mediální funkci (např. v architektuře 5G Media Streaming) nebo na straně klienta ve video přehrávači lze SSIM vypočítat (pokud je k dispozici reference) pro sledování kvality uživatelského prožitku (QoE) v reálném čase. Tato data mohou být vrácena zpět do sítě nebo na obsahový server, aby spustila adaptivní akce, jako je přepnutí na reprezentaci s jiným datovým tokem nebo aplikace skrytí chyb, za účelem udržení vysoké vnímané kvality pro koncového uživatele. Jeho přijetí odráží posun od metrik zaměřených na síť (propustnost, zpoždění) k uživatelsky orientovaným percepčním metrikám kvality v doručování multimediálních služeb.

## K čemu slouží

SSIM byl vyvinut na počátku 21. století, aby řešil nedostatečnost tradičních pixelových metrik chyb, jako je PSNR, pro hodnocení vizuální kvality. PSNR často špatně koreluje s lidskými subjektivními názory, zejména u moderních kompresních technik, které zavádějí strukturované artefakty (např. blokování, rozmazání, okrajové jevy), jež jsou více či méně rušivé než náhodný šum, s nímž PSNR počítá. Existovala jasná potřeba objektivní metriky, která by dokázala automaticky predikovat subjektivní kvalitu bez nutnosti nákladných a časově náročných testů s lidmi.

Standardizace SSIM a dalších percepčních metrik v 3GPP byla motivována explozivním růstem mobilního video provozu a potřebou efektivně využívat omezené rádiové zdroje při zajištění uspokojivého uživatelského zážitku. Operátoři a poskytovatelé služeb potřebovali spolehlivé, automatizované způsoby, jak ladit parametry kódování videa, navrhovat logiku adaptivního streamování a porovnávat různé kodeky. Pouhé používání PSNR mohlo vést k suboptimálním rozhodnutím, která buď plýtvala šířkou pásma na nepostřehnutelná zlepšení kvality, nebo naopak degradovala kvalitu způsobem velmi nápadným pro uživatele.

Začleněním SSIM do svých technických specifikací poskytlo 3GPP standardizovaný, na dodavateli nezávislý nástroj pro objektivní hodnocení kvality. To umožňuje spravedlivé porovnání různých implementací od dodavatelů, napomáhá testování shody pro profily kodeků a podporuje vývoj systémů správy sítě citlivých na QoE. Pro služby jako 5G-enhanced Mobile Broadband (eMBB) a imerzivní média (VR/AR), kde je vizuální věrnost prvořadá, SSIM pomáhá zajistit, aby složité kompromisy mezi šířkou pásma, latencí a kompresí byly řízeny způsobem, který upřednostňuje percepční zážitek koncového uživatele.

## Klíčové vlastnosti

- Percepční metrika kvality založená na modelu lidského vidění
- Metrika s plnou referencí vyžadující originální nezkreslený signál
- Rozkládá porovnání obrázků na jas, kontrast a strukturu
- Produkuje skóre od -1 do 1, přičemž 1 označuje dokonalou shodu
- Vyšší korelace se subjektivní střední hodnotou známky kvality (MOS) než u PSNR
- Aplikovatelný na obrázky i video sekvence (snímek po snímku nebo prostorově/časově agregovaný)

## Související pojmy

- [PSNR – Peak Signal-to-Noise Ratio](/mobilnisite/slovnik/psnr/)

## Definující specifikace

- **TR 26.812** (Rel-18) — Technical Report
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application

---

📖 **Anglický originál a plná specifikace:** [SSIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssim/)
