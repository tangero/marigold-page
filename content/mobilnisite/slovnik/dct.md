---
slug: "dct"
url: "/mobilnisite/slovnik/dct/"
type: "slovnik"
title: "DCT – Discrete Cosine Transformation"
date: 2025-01-01
abbr: "DCT"
fullName: "Discrete Cosine Transformation"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dct/"
summary: "DCT (Diskrétní kosinová transformace) je matematická transformace používaná ve video a audio kodecích v rámci standardů 3GPP pro účinnou kompresi dat. Převádí prostorová nebo časová signálová data na"
---

DCT (Diskrétní kosinová transformace) je matematická transformace používaná ve video a audio kodecích 3GPP, která převádí signálová data na frekvenční koeficienty pro účinnou kompresi odstraněním méně vnímatelných informací.

## Popis

Diskrétní kosinová transformace (DCT) je ztrátová kompresní technika klíčová pro mnoho multimediálních kodeků standardizovaných 3GPP. Funguje tak, že vezme blok pixelových dat (pro video) nebo okno audio vzorků a převede tato data z prostorové nebo časové oblasti do oblasti frekvenční. Tato transformace vede k sadě koeficientů reprezentujících různé frekvenční složky. Lidský zrakový a sluchový systém je méně citlivý na vysokofrekvenční detaily, což umožňuje hrubší kvantizaci těchto vyšších frekvenčních koeficientů nebo jejich nastavení na nulu s minimálním vnímaným zhoršením kvality. Toto selektivní odstranění informací je hlavním mechanismem pro dosažení vysokých kompresních poměrů.

V kontextu specifikací 3GPP jako TS 26.110 (Kodek pro okruhově spínanou multimediální telefonní službu) a TS 26.234 (Transparentní koncově koncová paketově spínaná streamovací služba) tvoří DCT jádro kodeků jako H.263, MPEG-4 Part 2 a částí audio kodeku [AMR-WB](/mobilnisite/slovnik/amr-wb/)+. Proces typicky zahrnuje rozdělení snímku obrazu na makrobloky (např. 8x8 nebo 16x16 pixelů), aplikaci DCT na každý blok, kvantizaci výsledných koeficientů pomocí kvantizační matice a následné kódování kvantizovaných hodnot pomocí technik entropického kódování, jako je Huffmanovo nebo aritmetické kódování. Inverzní DCT (IDCT) je aplikována v dekodéru pro rekonstrukci aproximace původního bloku.

Klíčové architektonické komponenty zahrnující DCT zahrnují transformační a kvantizační moduly kodéru a inverzně kvantizační a inverzně transformační moduly dekodéru. Její role v síti spočívá v umožnění efektivního využití vzácných rádiových a přenosových prostředků drastickým snížením velikosti multimediálního obsahu bez úměrné ztráty subjektivní kvality. Tato efektivita je klíčová pro poskytování služeb videotelefonie, mobilní televize a streamování přes buňkové sítě s omezenou přenosovou kapacitou a přímo ovlivňuje uživatelský zážitek a kapacitu sítě.

## K čemu slouží

DCT byla začleněna do standardů 3GPP, aby řešila základní výzvu poskytování multimediálních služeb přes mobilní sítě s omezenou a drahou přenosovou kapacitou. Před zavedením účinné komprese bylo vysílání nezpracovaného videa nebo vysokověrného audia nepraktické kvůli obrovským požadavkům na datový tok. Účelem DCT je provádět percepční kódování, využívající psychoakustické a psychovizuální vlastnosti lidského vnímání k odstranění informací, které budou nejméně postřehnuty, čímž vznikne mnohem menší, přenosový datový tok.

Historický kontext vychází z vývoje standardů komprese digitálního videa a audia vyvinutých v 80. a 90. letech 20. století, jako [JPEG](/mobilnisite/slovnik/jpeg/) a MPEG-1/2, které DCT etablovaly jako osvědčenou a efektivní metodu. 3GPP tyto techniky přijala a specifikovala, aby umožnila multimediální služby pro 3G (UMTS) a následující generace. Bez komprese založené na DCT by služby jako videohovor a mobilní televize byly na raných 3G sítích nemožné, nebo by spotřebovávaly neudržitelný podíl síťových prostředků, což by bránilo masovému rozšíření. Řešila problém vměstnání médií s vysokým datovým tokem do bezdrátových kanálů s nízkým datovým tokem a náchylných k chybám.

## Klíčové vlastnosti

- Transformuje prostorová/časová data na koeficienty ve frekvenční oblasti
- Umožňuje vysoké kompresní poměry prostřednictvím percepční kvantizace
- Tvoří základní výpočetní blok blokových video kodeků (např. H.263, MPEG-4)
- Používá se v modifikované formě v audio kodecích jako AMR-WB+ pro spektrální kompresi
- Definována pro velikosti bloků 8x8 a 16x16 v různých profilech kodeků 3GPP
- Umožňuje kompromisy mezi kompresní účinností a výpočetní složitostí

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [DCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dct/)
