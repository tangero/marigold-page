---
slug: "ms-ssim"
url: "/mobilnisite/slovnik/ms-ssim/"
type: "slovnik"
title: "MS-SSIM – Multi-Scale Structural Similarity Index"
date: 2025-01-01
abbr: "MS-SSIM"
fullName: "Multi-Scale Structural Similarity Index"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ms-ssim/"
summary: "MS-SSIM (Multi-Scale Structural Similarity Index) je objektivní algoritmus pro hodnocení kvality videa s úplnou referencí, standardizovaný organizací 3GPP. Vyhodnocuje percepční kvalitu videa porovnán"
---

MS-SSIM je standardizovaný algoritmus pro hodnocení kvality videa s úplnou referencí, který porovnává zpracované video s jeho původním zdrojem na více prostorových úrovních, aby vytvořil skóre percepční kvality.

## Popis

Multi-Scale Structural Similarity Index (MS-SSIM) je model pro měření percepční kvality videa přijatý organizací 3GPP pro objektivní hodnocení kvality. Na rozdíl od jednoduchých metrik založených na pixelech, jako je poměr šum/signál (PSNR), je MS-SSIM navržen tak, aby napodoboval vnímání věrnosti obrazu lidským vizuálním systémem. Funguje jako metrika s úplnou referencí, což znamená, že vyžaduje přístup k původnímu, nezkreslenému zdrojovému videu i k testovanému zpracovanému nebo degradovanému videu. Algoritmus pracuje analýzou strukturálních informací ve videích, založené na principu, že lidský vizuální systém je vysoce adaptovaný pro extrakci strukturálních informací. Aspekt 'Multi-Scale' je klíčový: algoritmus aplikuje dolní propust a iterativně snižuje rozlišení původního a zpracovaného videa, aby vytvořil pyramidu obrazů v různých rozlišeních neboli úrovních. Na každé úrovni vypočítá lokální statistiky – světlost, kontrast a strukturu – v rámci posuvného okna. Tyto statistiky jsou porovnány mezi referenčním a testovaným videem. Porovnání světlosti měří rozdíly střední intenzity, porovnání kontrastu měří směrodatnou odchylku intenzity a porovnání struktury měří korelační koeficient mezi dvěma obrazovými oblastmi. Výsledky z každé úrovně jsou následně kombinovány pomocí váženého součinu, přičemž je kladen větší důraz na jemnější úrovně (vyšší rozlišení), kde je lidské oko citlivější na detaily. Konečným výstupem je jediné skóre, typicky v rozsahu 0 až 1 (kde 1 značí dokonalou podobnost), které predikuje střední subjektivní hodnocení ([MOS](/mobilnisite/slovnik/mos/)), které by pravděpodobně udělil panel lidských pozorovatelů. V rámci 3GPP se MS-SSIM používá ve specifikacích pro testování výkonu k vyhodnocení vlivu na kvalitu při krocích zpracování videa, jako je komprese (např. pomocí [AVC](/mobilnisite/slovnik/avc/) nebo [HEVC](/mobilnisite/slovnik/hevc/)), přenos přes kanály náchylné k chybám a aplikace technik maskování chyb, čímž poskytuje standardizovaný, opakovatelný způsob kvantifikace percepční kvality.

## K čemu slouží

MS-SSIM byl standardizován, aby řešil nedostatečnost tradičních metrik, jako je PSNR, pro hodnocení percepční kvality videa v moderní telekomunikaci. PSNR, ačkoli je výpočetně jednoduché, často špatně koreluje s lidskými subjektivními soudy, zejména u moderních kodeků a komplexních zkreslení. Jak se video stalo primární službou v sítích 3G, 4G a 5G, vznikl silný požadavek na objektivní, automatizovaný nástroj pro hodnocení kvality, který by spolehlivě předpovídal spokojenost diváka během vývoje kodeků, plánování sítě a monitorování kvality uživatelského prožitku (QoE). Motivací pro jeho zařazení do specifikací 3GPP (počínaje Release 12) bylo poskytnout společnou, v odvětví dohodnutou metodologii pro testování výkonu video kodeků a přenosových systémů. To umožňuje spravedlivé a srovnatelné benchmarkování mezi různými implementacemi dodavatelů a technologiemi. Před jeho přijetím bylo zlatým standardem subjektivní testování s lidskými pozorovateli, které však bylo drahé, časově náročné a nebylo možné je ve velkém měřítku opakovat. MS-SSIM to vyřešil tím, že nabídl výpočetní model, který se blíže přibližuje subjektivním skóre. Konkrétně řeší víceúrovňovou povahu lidského vidění, kde mají zkreslení na různých prostorových frekvencích rozdílný percepční dopad, což jej činí přesnějším než jednoúrovňové metriky, jako je původní SSIM, pro hodnocení kvality videa v rozsahu rozlišení a podmínek prohlížení relevantních pro mobilní streamování.

## Klíčové vlastnosti

- Metrika s úplnou referencí porovnávající zpracované video s původním zdrojem
- Víceúrovňová analýza využívající Gaussovu pyramidu k hodnocení kvality v různých rozlišeních
- Vypočítá lokální porovnání světlosti, kontrastu a struktury
- Produkuje jediné skóre percepční kvality vysoce korelující s subjektivním MOS
- Standardizovaný výpočetní model zajišťující konzistentní výsledky napříč implementacemi
- Používá se pro objektivní testování výkonu video kodeků a odolnosti přenosu

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [MS-SSIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ms-ssim/)
