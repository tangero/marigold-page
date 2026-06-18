---
slug: "ctu"
url: "/mobilnisite/slovnik/ctu/"
type: "slovnik"
title: "CTU – Coding Tree Unit"
date: 2025-01-01
abbr: "CTU"
fullName: "Coding Tree Unit"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ctu/"
summary: "CTU je základní zpracovatelská jednotka ve videokódování, která představuje obdélníkový blok pixelů, jenž může být rozdělen na menší kódovací jednotky. Slouží jako kořen struktury dělení založené na k"
---

CTU je základní jednotka kódovacího stromu, která představuje blok pixelů sloužící jako kořen hierarchického dělení založeného na kvadrantovém stromu v moderních video kodecích, jako jsou HEVC a VVC.

## Popis

Kódovací stromová jednotka (CTU) je základním zpracovatelským prvkem v moderních standardech pro kompresi videa, konkrétně ve standardu High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)) a Versatile Video Coding ([VVC](/mobilnisite/slovnik/vvc/)). Představuje čtvercový blok vzorků jasové složky a odpovídajících vzorků barevných složek, s typickými velikostmi od 64×64 do 128×128 pixelů. CTU slouží jako výchozí bod pro rekurzivní proces dělení pomocí kvadrantového stromu, který definuje kódovací strukturu celého snímku.

Každá CTU může být rozdělena na menší Kódovací jednotky (CUs) pomocí dekompozice kvadrantovým stromem. Toto dělení je adaptivní a je určeno během procesu kódování na základě optimalizace přenosového toku a zkreslení. CTU obsahuje nejen obrazová data, ale také přidružené syntaktické elementy, které popisují, jak má být jednotka rozdělena, predikována a transformována. Tato hierarchická struktura umožňuje kodeku efektivně zpracovávat různé úrovně detailů v různých oblastech videosnímku.

Uvnitř každé CTU vytváří dělení stromovou strukturu, kde každý koncový uzel představuje Kódovací jednotku. Tyto CUs mohou být dále rozděleny na Predikční jednotky (PUs) pro pohybovou kompenzaci a Transformační jednotky (TUs) pro prostorovou transformaci. Koncept CTU nahrazuje strukturu makrobloků používanou ve starších standardech, jako je H.264/[AVC](/mobilnisite/slovnik/avc/), a poskytuje větší flexibilitu ve výběru velikosti bloků a lepší kompresní účinnost pro videoobsah s vysokým rozlišením.

Velikost CTU je klíčový parametr, který ovlivňuje jak kompresní výkon, tak výpočetní složitost. Větší CTU (např. 128×128) obecně poskytují lepší kompresi pro homogenní oblasti, ale vyžadují větší výpočetní výkon. Struktura CTU umožňuje možnosti paralelního zpracování, protože více CTU může být zpracováváno nezávisle, což usnadňuje hardwarovou akceleraci a implementace pro více jader. Díky tomu jsou CTU nezbytné pro kódování a dekódování videa v ultra vysokém rozlišení v reálném čase.

V kontextu 3GPP jsou CTU zvláště relevantní pro videoslužby v mobilních sítích, kde efektivní komprese přímo ovlivňuje využití přenosové kapacity a kvalitu uživatelského zážitku. Kódovací struktura založená na CTU umožňuje lepší přizpůsobení síťovým podmínkám prostřednictvím technik škálovatelného videokódování a odolnosti proti chybám. Tento hierarchický přístup také podporuje pokročilé funkce, jako je kódování obrazovkového obsahu a adaptivní změny rozlišení v rámci stejného videoproudu.

## K čemu slouží

CTU byla zavedena, aby odstranila omezení struktury s pevnou velikostí makrobloků používané v předchozích standardech pro videokódování, jako je H.264/[AVC](/mobilnisite/slovnik/avc/). Jak se rozlišení videa zvýšilo ze standardního rozlišení na 4K a 8K, se makroblok 16×16 stal pro reprezentaci velkých homogenních oblastí neefektivním a pro zachycení jemných detailů ve složitých texturách nedostatečným. Větší velikost CTU a její hierarchické dělení poskytují potřebnou flexibilitu pro optimalizaci komprese moderního videoobsahu s vysokým rozlišením.

Tradiční kódování založené na makroblocích se potýkalo s nízkou kompresní účinností pro obsah v ultra vysokém rozlišení, protože nedokázalo efektivně přizpůsobovat velikosti bloků různým prostorovým charakteristikám. Struktura CTU založená na kvadrantovém stromu umožňuje kodeku používat větší bloky pro ploché oblasti (snížení režie) a menší bloky pro detailní oblasti (zachování kvality). Tento adaptivní přístup výrazně zlepšuje kompresní poměry při zachování vizuální kvality, což je klíčové pro mobilní sítě s omezenou přenosovou kapacitou.

Vývoj kódování založeného na CTU byl motivován rostoucí poptávkou po službách videa vysoké kvality v sítích 3GPP. Jak spotřeba mobilního videa exponenciálně rostla, potřebovali síťoví operátoři efektivnější kompresi, aby mohli v rámci dostupné kapacity poskytovat streamování 4K, videokonference a imerzivní média. Architektura CTU také usnadňuje hardwarově příznivé implementace s lepšími možnostmi paralelního zpracování, což umožňuje kódování a dekódování v reálném čase na mobilních zařízeních s omezenými výpočetními zdroji.

## Klíčové vlastnosti

- Hierarchická struktura dělení pomocí kvadrantového stromu
- Adaptivní výběr velikosti bloku od 8×8 do 128×128 pixelů
- Nezávislé zpracování CTU pro paralelní implementaci
- Podpora více velikostí predikčních a transformačních jednotek v rámci jedné CTU
- Efektivní komprese videoobsahu s vysokým rozlišením
- Kompatibilita s pokročilými kódovacími nástroji, jako je intrabloková kopie a režim palety

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [CTU na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctu/)
