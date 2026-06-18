---
slug: "sgcs"
url: "/mobilnisite/slovnik/sgcs/"
type: "slovnik"
title: "SGCS – Squared Generalized Cosine Similarity"
date: 2025-01-01
abbr: "SGCS"
fullName: "Squared Generalized Cosine Similarity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sgcs/"
summary: "Matematická metrika používaná v NR pro kvantifikaci podobnosti mezi beamformingovými vektory nebo charakteristikami kanálu, zejména v operacích s více paprsky. Pomáhá při správě, výběru a zpřesňování"
---

SGCS je metrika používaná v NR pro kvantifikaci podobnosti mezi beamformingovými vektory nebo charakteristikami kanálu, která napomáhá správě a výběru paprsků.

## Popis

Squared Generalized Cosine Similarity (SGCS) je metrika definovaná ve specifikacích 3GPP NR pro vyhodnocení zarovnání nebo podobnosti mezi dvěma komplexními vektory, které často reprezentují beamformingové váhy nebo informace o stavu kanálu. Matematicky se pro vektory **a** a **b** SGCS vypočítá jako |**a**^H **b**|^2 / (||**a**||^2 ||**b**||^2), kde ^H označuje konjugovanou transpozici. Výsledkem je hodnota mezi 0 a 1, která indikuje ortogonalitu (0) nebo dokonalé zarovnání (1). V NR se SGCS primárně používá v procedurách správy paprsků pro posouzení, jak jsou si kandidátní paprsky podobné, což informuje rozhodnutí o přepínání, kombinování nebo zpřesňování paprsků.

Z architektonického hlediska se SGCS využívá v algoritmech fyzické vrstvy gNB a UE, jak je detailně popsáno ve specifikacích jako 38.212 (multiplexování a kódování kanálu) a 38.214 (procedury fyzické vrstvy). Operuje s beamformingovými vektory odvozenými z měření kanálu, například z těch získaných pomocí referenčních signálů pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) nebo bloků synchronizačních signálů (SSB). gNB může vypočítat SGCS mezi různými páry paprsků, aby identifikoval redundantní paprsky nebo optimalizoval vysílání s více paprsky, čímž snižuje interferenci a zlepšuje spektrální účinnost.

Jak funguje: Během správy paprsků UE reportuje měření, jako je Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)), pro více paprsků. gNB může vypočítat SGCS mezi prostorovými charakteristikami reportovaných paprsků, aby určil, zda jsou dostatečně odlišné. Například ve scénáři UE s více panely pomáhá SGCS rozhodnout, zda použít více současných paprsků (prostorové multiplexování), nebo přepnout na jeden paprsek, na základě prahových hodnot podobnosti. To je klíčové pro systémy massive [MIMO](/mobilnisite/slovnik/mimo/), kde je k dispozici mnoho paprsků a efektivní výběr je zásadní pro udržení vysoké propustnosti a pokrytí.

Klíčové komponenty zahrnují beamformingový kodebook, ze kterého jsou vektory vybírány, a modul odhadu kanálu, který poskytuje vstupní vektory. Na SGCS se odkazuje také v 38.843 pro nesatelitní sítě, kde hodnocení podobnosti paprsků musí zohledňovat dynamický pohyb satelitů. Kvantifikací korelace paprsků SGCS umožňuje pokročilé funkce, jako je obnova po selhání paprsku nebo koordinovaný přenos z více bodů, což zajišťuje robustní výkon v různých scénářích nasazení.

## K čemu slouží

SGCS byl zaveden, aby řešil složitost správy paprsků v NR, zejména u massive [MIMO](/mobilnisite/slovnik/mimo/) a vysokofrekvenčních pásem (např. mmWave). Předchozí přístupy se silně spoléhaly na výběr paprsků založený na [RSRP](/mobilnisite/slovnik/rsrp/), což mohlo vést k suboptimálním volbám, když mají paprsky podobný výkon, ale odlišné prostorové vlastnosti, což způsobovalo interferenci nebo promarněné příležitosti pro multiplexování. SGCS poskytuje standardizovanou metriku pro vyhodnocení podobnosti paprsků, což umožňuje inteligentnější koordinaci paprsků a alokaci prostředků.

Historicky byla správa paprsků v LTE jednodušší kvůli omezenému počtu MIMO vrstev. S podporou stovek anténních prvků a flexibilního beamformingu v NR se stala nezbytnou kvantitativní míra podobnosti pro zvládnutí korelace paprsků a vyhnutí se redundantnímu vysílání. SGCS, specifikovaný od Release 18, tuto mezeru zaplňuje tím, že nabízí matematický základ pro porovnávání beamformingových vektorů, a přímo tak podporuje funkce jako operace s více paprsky a vylepšenou mobilitu.

Motivace vychází z potřeby zlepšit spektrální účinnost a snížit režii v prostředích s hustými paprsky. Použitím SGCS mohou sítě identifikovat ortogonální paprsky pro současné vysílání, zvýšit přesnost zpřesňování paprsků a přizpůsobit se rychlým změnám kanálu. To je zvláště důležité pro nesatelitní sítě v 38.843, kde musí být zarovnání paprsků dynamicky upravováno kvůli pohybu satelitů. SGCS nakonec přispívá k vyšším datovým rychlostem, lepšímu pokrytí a spolehlivému připojení v pokročilých nasazeních NR.

## Klíčové vlastnosti

- Kvantifikuje podobnost mezi beamformingovými nebo kanálovými vektory na škále od 0 do 1
- Používá se při správě paprsků v NR pro rozhodování o výběru, přepínání a zpřesňování
- Podporuje massive MIMO a operace s více paprsky za účelem snížení interference
- Integruje se s procedurami fyzické vrstvy definovanými v 38.212 a 38.214
- Aplikovatelné na pozemní i nesatelitní sítě (např. satelitní)
- Zvyšuje spektrální účinnost identifikací ortogonálních paprsků pro multiplexování

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface

---

📖 **Anglický originál a plná specifikace:** [SGCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgcs/)
