---
slug: "icc"
url: "/mobilnisite/slovnik/icc/"
type: "slovnik"
title: "ICC – Inter Channel Coherence"
date: 2025-01-01
abbr: "ICC"
fullName: "Inter Channel Coherence"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/icc/"
summary: "Parametr stereofonního zvuku používaný v kodecích 3GPP k vyjádření korelace nebo podobnosti mezi levým a pravým zvukovým kanálem. Je klíčový pro efektivní kompresi stereofonního signálu, umožňuje vyso"
---

ICC je parametr stereofonního zvuku vyjadřující korelaci mezi levým a pravým kanálem. Používá se v kodecích 3GPP pro efektivní kompresi využitím redundance mezi kanály.

## Popis

Inter Channel Coherence (ICC) je parametr definovaný v různých specifikacích zvukových kodeků 3GPP, zejména těch, které podporují stereofonní nebo vícekanálový zvuk, jako je Extended Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)+) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Kvantifikuje míru korelace nebo podobnosti mezi levým a pravým kanálem stereofonního zvukového signálu v určitých časově-frekvenčních intervalech. Technicky je ICC často odvozen jako normalizovaný korelační koeficient, jehož hodnoty se typicky pohybují od 0 (zcela nekorelované nebo ve fázovém protifázi) do 1 (dokonale korelované nebo totožné). V technikách parametrického stereofonního kódování vysílač namísto přenosu dvou plných nezávislých kanálů přenáší monofonní směšovací signál spolu s parametrovými vedlejšími informacemi, jako je ICC (a Inter Channel Level Difference, ICLD), které popisují prostorové vlastnosti.

Parametr funguje v rámci percepčního rámce zvukového kódování pracujícího ve frekvenční oblasti, jako je reprezentace Modified Discrete Cosine Transform ([MDCT](/mobilnisite/slovnik/mdct/)). Kodér analyzuje stereofonní vstupní signál v časově-frekvenčních segmentech a pro každý segment vypočítá ICC. Tento parametr je pak spolu s dalšími kvantován a odeslán jako součást zakódovaného datového toku. Dekodér používá přijatý monofonní signál a parametr ICC (spolu s ICLD) k rekonstrukci stereofonního výstupu aplikací příslušných pravidel pro zpětný rozklad směsi. Například vysoká hodnota ICC indikuje, že kanály jsou podobné, takže dekodér může vytvořit stereofonní obraz aplikací minimální de-korelace, zatímco nízká hodnota ICC může aktivovat specifické de-korelační filtry k vytvoření širšího, rozptýlenějšího stereofonního obrazu.

Klíčovými součástmi jeho fungování jsou modul parametrické stereofonní analýzy v kodéru a syntézy v dekodéru. Jeho role je zásadní pro dosažení vysoké kompresní účinnosti pro stereofonní obsah, jako je hudba, v mobilní komunikaci a streamovacích službách. Přenosem pouze jednoho kanálu základních zvukových dat plus kompaktních parametrových vedlejších informací je dosaženo významných úspor přenosové rychlosti ve srovnání s nezávislým kódováním kanálů, bez vnímatelné ztráty stereofonní kvality ve většině poslechových scénářů. To z něj činí základní kámen šíření zvuku vysoké kvality s efektivním využitím šířky pásma v systémech 3GPP.

## K čemu slouží

ICC byl vyvinut k řešení výzvy přenosu stereofonního zvuku vysoké věrnosti přes mobilní sítě s omezenou šířkou pásma. Rané mobilní zvukové služby, jako byly řečové kodeky, byly monofonní a pro hudbu neefektivní. Jak se služby rozvíjely a zahrnovaly hudební streamování a multimediální zprávy, vznikla potřeba stereofonního kódování schopného pracovat při nízkých přenosových rychlostech. Jednoduché techniky sdruženého sterea, jako je kódování střed-součet (M/S), poskytovaly určité zisky, ale byly méně flexibilní. Parametrické stereofonní přístupy využívající parametry jako ICC a ICLD byly motivovány potřebou větší komprese využitím vysokého stupně redundance a specifických prostorových vztahů mezi stereofonními kanály.

Tato technologie řeší problém neefektivního využití přenosové rychlosti při naivním stereofonním přenosu. Přenos dvou nezávislých kanálů v podstatě zdvojnásobuje požadavky na přenosovou rychlost. Analýzou a parametrizací prostorového obrazu může parametrické stereo rekonstruovat percepčně přesvědčivý stereofonní signál z monofonní směsi za zlomek přenosové rychlosti. Vytvoření standardizovaných parametrů ICC v rámci kodeků 3GPP, jako jsou [AMR-WB](/mobilnisite/slovnik/amr-wb/)+ a [EVS](/mobilnisite/slovnik/evs/), zajistilo interoperabilitu a konzistentní vysokou kvalitu stereofonního výkonu napříč různými zařízeními a sítěmi, což umožnilo, aby se bohaté zvukové služby jako hudební telefonie a streamování staly životaschopnými na sítích 3G, 4G a 5G. Odstranila tak omezení předchozích neparametrických nebo jednodušších metod stereofonního kódování, které buď spotřebovávaly příliš mnoho šířky pásma, nebo produkovaly horší stereofonní kvalitu při velmi nízkých přenosových rychlostech.

## Klíčové vlastnosti

- Kvantifikuje korelaci mezi levým a pravým zvukovým kanálem v časově-frekvenčních doménách
- Umožňuje parametrické stereofonní kódování pro vysokou kompresní účinnost
- Přenášen jako vedlejší informace spolu s jádrovým datovým tokem monofonní směsi
- Používán v kodecích jako AMR-WB+ a EVS pro hudbu a služby vysokokvalitního hlasu
- Umožňuje percepční rekonstrukci stereofonního obrazu v dekodéru
- Hodnoty se typicky pohybují od 0 (nekorelované) do 1 (plně korelované)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.405** (Rel-19) — Parametric Stereo Encoder for Enhanced aacPlus
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance

---

📖 **Anglický originál a plná specifikace:** [ICC na 3GPP Explorer](https://3gpp-explorer.com/glossary/icc/)
