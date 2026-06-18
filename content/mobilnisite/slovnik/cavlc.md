---
slug: "cavlc"
url: "/mobilnisite/slovnik/cavlc/"
type: "slovnik"
title: "CAVLC – Context Adaptive Variable Length Coding"
date: 2025-01-01
abbr: "CAVLC"
fullName: "Context Adaptive Variable Length Coding"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cavlc/"
summary: "CAVLC je bezztrátový kompresní algoritmus používaný v kodeku 3GPP Enhanced Voice Services (EVS) k efektivnímu kódování kvantovaných spektrálních koeficientů. Snižuje nároky na datový tok pro přenos vy"
---

CAVLC je bezztrátový kompresní algoritmus používaný v kodeku 3GPP EVS k efektivnímu kódování kvantovaných spektrálních koeficientů využitím statistických redundancí, čímž snižuje datový tok pro vysokokvalitní zvuk.

## Popis

Context Adaptive Variable Length Coding (CAVLC) je sofistikovaná entropická kódovací technika implementovaná v rámci zvukového kodeku 3GPP Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)), standardizovaného v TS 26.906. Pracuje s kvantovanými spektrálními koeficienty vygenerovanými po modifikované diskrétní kosinové transformaci ([MDCT](/mobilnisite/slovnik/mdct/)) ve frekvenční části kodéru EVS. Na rozdíl od jednoduššího Huffmanova kódování CAVLC dynamicky přizpůsobuje své tabulky kódů proměnné délky na základě lokálního statistického kontextu kódovaných dat, konkrétně hodnot dříve zakódovaných koeficientů. Toto přizpůsobení kontextu umožňuje dosáhnout vyšší kompresní účinnosti použitím kratších kódových slov pro pravděpodobnější vzorce koeficientů a delších slov pro méně pravděpodobné.

Algoritmus zpracovává spektrální koeficienty v určitém skenovacím pořadí, typicky začínajíc od nižších frekvencí a postupujíc k vyšším, nebo používá cik-cak vzor pro seskupení koeficientů s podobnými statistickými vlastnostmi. Pro každý koeficient nebo skupinu koeficientů (jako jsou sekvence nul) CAVLC vybírá vhodnou tabulku [VLC](/mobilnisite/slovnik/vlc/) z předdefinované sady na základě kontextových parametrů, jako je počet nenulových koeficientů v sousedních frekvenčních pásmech nebo velikost nedávno zakódovaných koeficientů. Klíčové součásti procesu CAVLC zahrnují kódování celkového počtu nenulových koeficientů a koncových jedniček (koeficientů s absolutní hodnotou 1), kódování znamének těchto koncových jedniček, kódování úrovní (velikostí) zbývajících nenulových koeficientů a kódování celkového počtu nul před posledním nenulovým koeficientem.

V rámci architektury kodeku EVS hraje CAVLC klíčovou roli v multiplexoru bitového toku jádra kodéru. Po kvantování a seskupení spektrálních koeficientů CAVLC tyto data komprimuje pro přenos. Dekodér provádí inverzní proces, využívaje stejná kontextová pravidla k výběru správných tabulek VLC pro parsování bitového toku a rekonstrukci kvantovaných spektrálních koeficientů, které jsou následně inverzně transformovány a syntetizovány pro vytvoření zvukového výstupu. Účinnost CAVLC přímo ovlivňuje provozní rozsah datového toku kodeku EVS, což mu umožňuje poskytovat vysokokvalitní řeč a hudbu při datových tocích od 5,9 kbps až do 128 kbps pro superširokopásmový a plnopásmový obsah.

Návrh CAVLC v EVS je optimalizován pro statistické charakteristiky zvukových signálů. Efektivně zpracovává distribuční funkci s těžkými konci pro velikosti koeficientů (mnoho nul a malých hodnot, s méně velkými hodnotami). Kontextové modelování je pečlivě navrženo ke sledování lokálních statistik bez nadměrné výpočetní složitosti nebo paměťových nároků, což jej činí vhodným pro implementaci v reálném čase na mobilních zařízeních. Jeho integrace je bezproblémová s dalšími komponentami EVS, jako je šířkopásmově adaptivní lineární predikce, zaplňování šumem a časové tvarování šumu, což přispívá k celkové odolnosti kodeku proti ztrátám paketů a jeho schopnosti udržet vysokou zvukovou kvalitu v různých síťových podmínkách.

## K čemu slouží

CAVLC byl představen v 3GPP Release 12 jako součást kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) k řešení rostoucí poptávky po vyšší kvalitě zvukových služeb (jako [HD](/mobilnisite/slovnik/hd/) hlas) v mobilních sítích při optimalizaci využití šířky pásma. Předchozí kodeky, jako [AMR-WB](/mobilnisite/slovnik/amr-wb/), používaly jednodušší metody entropického kódování nebo pevné kódové knihy, které byly méně účinné při kompresi spektrálních dat širokopásmového a superširokopásmového zvuku. Tato neefektivita buď omezovala zvukovou kvalitu při daném datovém toku, nebo vyžadovala vyšší datové toky k dosažení kvalitativních cílů, což zatěžovalo kapacitu sítě, zejména s rozšiřováním nasazení Voice over LTE (VoLTE).

Primární problém, který CAVLC řeší, je efektivní, bezztrátová komprese kvantovaných koeficientů ve frekvenční oblasti. Zvukové signály transformované do frekvenční oblasti (pomocí [MDCT](/mobilnisite/slovnik/mdct/)) vykazují specifické statistické vzorce: velký počet koeficientů je nulový nebo blízký nule, zejména na vyšších frekvencích, a nenulové koeficienty mají předvídatelné rozdělení velikostí. Jednoduché kódování s pevnou délkou nebo základní kódování s proměnnou délkou plýtvá bity. Kontextově adaptivní přístup CAVLC využívá tyto lokální korelace, což výrazně snižuje průměrný počet bitů potřebných na koeficient. Tato úspora bitů je přímo reinvestována, aby umožnila jemnější kvantování koeficientů při stejném celkovém datovém toku, což vede k vyšší percepční kvalitě zvuku, nebo ke snížení provozního datového toku pro ekvivalentní kvalitu, čímž se uvolňují rádiové prostředky.

Historicky vytvořil vývoj od úzkopásmových k širokopásmovým a plnopásmovým zvukovým službám výzvu v kompresi dat. Kodek EVS byl navržen jako nástupce AMR-WB, což vyžadovalo špičkové kompresní nástroje pro konkurenceschopný výkon. CAVLC, čerpající principy z pokročilých standardů pro kódování videa jako H.264/[AVC](/mobilnisite/slovnik/avc/) (který používá podobnou techniku pro reziduální data), byl přizpůsoben unikátním charakteristikám zvuku. Řešil omezení předchozích kódových knih založených na algebraickém kódovém buzeném lineárním prediktoru (ACELP) a transformačně kódované excitaci (TCX) tím, že poskytoval flexibilnější a účinnější způsob reprezentace spektrální obálky a detailů, což bylo klíčové pro podporu hudby a smíšeného obsahu kromě řeči, což byl hlavní cíl EVS.

## Klíčové vlastnosti

- Bezztrátová komprese kvantovaných spektrálních koeficientů
- Dynamické přizpůsobení tabulek VLC na základě lokálních statistik koeficientů
- Efektivní kódování sekvencí nul a velikostí koeficientů
- Optimalizováno pro distribuční funkci s těžkými konci u zvukových MDCT koeficientů
- Umožňuje vysokokvalitní zvuk při nižších datových tocích pro kodek EVS
- Návrh s nízkou složitostí vhodný pro zpracování v reálném čase na mobilních zařízeních

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [CAVLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cavlc/)
