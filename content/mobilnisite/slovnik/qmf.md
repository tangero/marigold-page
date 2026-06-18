---
slug: "qmf"
url: "/mobilnisite/slovnik/qmf/"
type: "slovnik"
title: "QMF – Quadrature Mirror Filter"
date: 2025-01-01
abbr: "QMF"
fullName: "Quadrature Mirror Filter"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qmf/"
summary: "Quadrature Mirror Filter (QMF) je filtrová banka pro zpracování signálu používaná pro subpásmové kódování, zejména v audio kompresi a analýze. Rozděluje signál na více frekvenčních subpásem a umožňuje"
---

QMF je filtrová banka pro zpracování signálu používaná v audio kodecích 3GPP k rozdělení signálu na frekvenční subpásma pro efektivní spektrální reprezentaci a dokonalou rekonstrukci.

## Popis

Filtrová banka typu Quadrature Mirror Filter (QMF) je specifický typ filtrové banky hojně používaný ve zpracování signálu pro subpásmové kódování. Jejím hlavním účelem je rozložit signál s plným pásmem (jako je například audio signál) na sadu subpásmových signálů, z nichž každý zabírá odlišnou část původního frekvenčního spektra. Naopak syntézní filtrová banka může z těchto subpásem rekonstruovat původní signál. Aspekt 'kvadratury' (quadrature) souvisí s návrhem filtrů ve dvojicích se specifickými fázovými vztahy, zatímco 'zrcadlo' (mirror) odkazuje na symetrickou frekvenční charakteristiku analyzačních dolní a horní propusti kolem kvadraturní frekvence (π/2).

QMF banka se skládá ze dvou hlavních komponent: analyzační filtrové banky a syntézní filtrové banky. Analyzační banka typicky používá pár filtrů: dolní propust (H0) a horní propust (H1). Tyto filtry jsou navrženy tak, že jejich frekvenční charakteristiky jsou vzájemně zrcadlové obrazy kolem poloviny Nyquistovy frekvence. Signál je prohnán těmito filtry a výstupy jsou podvzorkovány (decimovány) faktorem dva, čímž vznikají subpásmové signály. Tento proces lze iterovat na výstupu dolní propusti pro vytvoření hierarchického rozkladu s více rozlišeními (jako ve vlnkové transformaci).

Pro dokonalou rekonstrukci – kdy výstupní signál je zpožděnou, případně škálovanou verzí vstupního – musí být syntézní filtry (G0 a G1) pečlivě navrženy ve spojení s analyzačními filtry. Podmínky zahrnují omezení na koeficienty filtrů za účelem eliminace aliasingu a amplitudového zkreslení. Ve specifikacích 3GPP, zejména těch souvisejících s audio kodeky (jako jsou kodeky pro Enhanced Voice Services), se QMF banky používají jako nástroj pro spektrální analýzu a syntézu. Poskytují efektivní způsob rozdělení audio signálu na frekvenční pásma pro následné zpracování, jako je například percepční kódování, kde jsou bity alokovány na základě důležitosti každého subpásma pro lidský sluch.

## K čemu slouží

Filtrové banky typu Quadrature Mirror Filter byly vyvinuty k uspokojení potřeby efektivní, vratné dekompozice signálu pro kompresi a zpracování. Před jejich rozšířeným přijetím bylo přímé zpracování širokopásmových signálů výpočetně náročné a pro aplikace jako audio kódování neefektivní, protože různé frekvenční složky mají různou percepční důležitost. Jednoduché filtrování a podvzorkování by zavedlo aliasingové artefakty, které by při rekonstrukci signál poškodily.

Vytvoření QMF bank vyřešilo kritický problém potlačení aliasingu ve dvoukanálových filtrových bankách. Jejich specifická konstrukční vlastnost umožňuje, aby aliasingové složky zavedené podvzorkováním ve fázi analýzy byly vyrušeny převzorkováním a filtrováním ve fázi syntézy. To umožňuje dokonalou (nebo téměř dokonalou) rekonstrukci, která je zásadní pro bezztrátové nebo vysoce kvalitní ztrátové kódování. V kontextu audio kodeků 3GPP, na které se odkazuje od verze Rel-8 výše, poskytují QMF banky standardizovanou, matematicky správnou metodu pro rozdělení audio signálu na subpásma. To umožňuje kodekům efektivněji aplikovat psychoakustické modely, alokovat méně bitů na méně vnímatelné frekvenční složky, a tím dosáhnout vyšších kompresních poměrů bez znatelné ztráty kvality, což je klíčové pro efektivní přenos hlasu a audia přes mobilní sítě s omezenou šířkou pásma.

## Klíčové vlastnosti

- Rozkládá signál na subpásma pro analýzu s více rozlišeními
- Umožňuje dokonalou rekonstrukci původního signálu při splnění podmínek
- Poskytuje inherentní potlačení aliasingu mezi analyzační a syntézní fází
- Používá se jako stavební blok pro složitější filtrové banky a vlnkové transformace
- Možná efektivní implementace pomocí polyfázových struktur
- Odkazováno v 3GPP pro spektrální zpracování ve specifikacích audio kodeků

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.401** (Rel-19) — Enhanced aacPlus Audio Codec Mapping
- **TS 26.404** (Rel-19) — Enhanced aacPlus SBR Encoder Specification
- **TS 26.405** (Rel-19) — Parametric Stereo Encoder for Enhanced aacPlus
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code

---

📖 **Anglický originál a plná specifikace:** [QMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/qmf/)
