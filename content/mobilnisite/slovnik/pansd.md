---
slug: "pansd"
url: "/mobilnisite/slovnik/pansd/"
type: "slovnik"
title: "PANSD – PSNR of Average Normalized Square Difference"
date: 2025-01-01
abbr: "PANSD"
fullName: "PSNR of Average Normalized Square Difference"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pansd/"
summary: "Objektivní metrika pro hodnocení kvality videa definovaná 3GPP. Vypočítává poměr špičkového signálu k šumu (PSNR) na základě průměrného normalizovaného kvadrátu rozdílu mezi původními a zpracovanými s"
---

PANSD je objektivní metrika kvality videa definovaná 3GPP, která vypočítává poměr špičkového signálu k šumu (PSNR) z průměrného normalizovaného kvadrátu rozdílu mezi původními a zpracovanými snímky za účelem kvantifikace vizuální degradace.

## Popis

[PSNR](/mobilnisite/slovnik/psnr/) of Average Normalized Square Difference (PANSD) je objektivní, plně referenční metrika kvality videa standardizovaná 3GPP. Je navržena tak, aby automaticky předpovídala percepční kvalitu zpracované nebo přenášené video sekvence jejím porovnáním s původním nekomprimovaným zdrojovým videem. Jádrem výpočtu je hodnota 'Average Normalized Square Difference' (ANSD). Pro každý pixel ve snímku videa se vypočítá rozdíl mezi původní a zpracovanou hodnotou pixelu, tento rozdíl se umocní na druhou a součet se provede přes všechny pixely ve snímku. Tento součet je následně normalizován, typicky počtem pixelů a druhou mocninou maximální možné hodnoty pixelu (např. 255 pro 8bitové video). Tím se získá normalizovaná střední kvadratická chyba ([MSE](/mobilnisite/slovnik/mse/)) v rozsahu 0-1 nebo podobném.

Komponenta 'PSNR' v rámci PANSD je pak odvozena z této hodnoty ANSD. PSNR se vypočítá pomocí standardního logaritmického vzorce: PSNR = 10 * log10( (MAX^2) / ANSD ), kde MAX je maximální možná hodnota pixelu. Výsledek je vyjádřen v decibelech (dB). Vyšší hodnota PANSD indikuje lepší kvalitu (menší zkreslení), protože rozdíl (ANSD) mezi původním a zpracovaným videem je menší vzhledem k špičce signálu. Metrika se aplikuje snímek po snímku a celkové skóre pro video sekvenci může být vypočteno jako časový průměr (např. střední hodnota nebo medián) hodnot PANSD na úrovni snímků.

PANSD pracuje v pixelové doméně a je klasifikována spíše jako metrika matematické věrnosti než jako percepční model. Měří jednoduché, absolutní rozdíly v hodnotách jasu (a případně barevnosti). Její role v ekosystému 3GPP je primárně v rámci testování výkonnosti a hodnocení kodeků, jak je uvedeno ve specifikaci TS 26.902. Poskytuje reprodukovatelný, automatizovaný způsob porovnání výstupů různých video procesních řetězců, jako jsou enkodéry, transratéry nebo algoritmy pro skrytí chyb, za kontrolovaných laboratorních podmínek. Přestože je výpočetně jednoduchá, nemusí vždy dokonale korelovat s lidskými subjektivními názory, zejména u komplexních zkreslení.

## K čemu slouží

PANSD byla vytvořena, aby splnila potřebu standardizované, objektivní metody pro hodnocení kvality videa v rámci multimediálních specifikací 3GPP. S vývojem mobilních sítí pro podporu video služeb se stalo klíčovým mít dohodnuté metriky pro specifikaci minimálních požadavků na výkonnost video kodeků, definici testovacích postupů a porovnání implementací od různých dodavatelů. Subjektivní testování s lidskými pozorovateli, ačkoli je konečným měřítkem, je drahé, časově náročné a nevhodné pro automatizované regresní testování nebo certifikaci zařízení.

Metrika řeší problém kvantifikace vizuální degradace konzistentním a opakovatelným způsobem. Před standardizací mohly různé organizace používat mírně odlišné varianty [PSNR](/mobilnisite/slovnik/psnr/) nebo [MSE](/mobilnisite/slovnik/mse/), což ztěžovalo vzájemná porovnání. Definice PANSD v TS 26.902 od 3GPP poskytla přesný, normativní vzorec pro telekomunikační průmysl. To umožňuje jednoznačnou specifikaci prahových hodnot kvality v jiných standardních dokumentech a zajišťuje, že když dvě strany uvádějí hodnotu PANSD, vypočítaly ji shodně.

Její historický kontext spadá do širší práce na službě Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a paketově přepínaném streamování, kde bylo zásadní pochopit dopad komprese a přenosových chyb na video. Přestože existují pokročilejší percepční metriky (jako VQM nebo [SSIM](/mobilnisite/slovnik/ssim/)), PANSD slouží jako dobře pochopená základní metrika. Je zvláště užitečná pro měření věrnosti ztrátových kompresních procesů, kde je hlavním zkreslením šumově podobná aditivní chyba, a poskytuje tak jasné, matematické měřítko úrovně zavedeného zkreslení.

## Klíčové vlastnosti

- Plně referenční metrika vyžadující původní a zpracované video sekvence
- Jako mezikrok vypočítá normalizovanou střední kvadratickou chybu (ANSD)
- Z hodnoty ANSD odvozuje hodnotu poměru špičkového signálu k šumu (PSNR) v decibelech
- Poskytuje skóre kvality na úrovni snímků i celé sekvence
- Standardizovaný, reprodukovatelný vzorec pro objektivní testování
- Primárně používána pro testování výkonnosti kodeků a video procesních funkcí v 3GPP

## Související pojmy

- [PSNR – Peak Signal-to-Noise Ratio](/mobilnisite/slovnik/psnr/)
- [MSE – Mobility Speed Estimation](/mobilnisite/slovnik/mse/)

## Definující specifikace

- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services

---

📖 **Anglický originál a plná specifikace:** [PANSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/pansd/)
