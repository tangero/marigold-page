---
slug: "tcx"
url: "/mobilnisite/slovnik/tcx/"
type: "slovnik"
title: "TCX – Transform Coded Excitation"
date: 2025-01-01
abbr: "TCX"
fullName: "Transform Coded Excitation"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tcx/"
summary: "Technologie kodeku pro řeč a audio používaná ve standardech 3GPP pro efektivní kompresi. Používá techniky kódování v transformační doméně k modelování a zakódování excitačního signálu, čímž zlepšuje k"
---

TCX (Transform Coded Excitation) je komponenta pro kódování řeči a audia v transformační doméně, používaná v kodecích 3GPP, jako je EVS, k efektivnímu modelování excitačního signálu za účelem zlepšení kvality při nízkých přenosových rychlostech.

## Popis

Transform Coded Excitation (TCX) je hlavní kódovací režim v několika kodecích pro řeč a audio standardizovaných 3GPP, nejvýznamněji v kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) standardizovaném ve vydání 12. Jedná se o techniku kódování ve frekvenční doméně používanou k reprezentaci excitačního signálu – reziduálního signálu po lineární prediktivní analýze, který nese jemné spektrální detaily a šumové složky audia. Na rozdíl od tradičního Code-Excited Linear Prediction ([CELP](/mobilnisite/slovnik/celp/)), který pracuje primárně v časové doméně, TCX aplikuje Modified Discrete Cosine Transform ([MDCT](/mobilnisite/slovnik/mdct/)) na okené segmenty excitačního signálu. Tím se signál transformuje do frekvenční domény, kde lze jeho spektrální koeficienty efektivně kvantovat a kódovat. Rámec TCX je typicky delší než rámec CELP (např. 20 ms, 40 ms nebo 80 ms), což umožňuje lepší frekvenční rozlišení a efektivnější kódování stacionárních signálů, jako je hudba nebo znělá řeč. Kvantizace spektrálních koeficientů využívá algebraickou vektorovou kvantizaci a používá rozšíření šířky pásma a percepční tvarování šumu na základě lineárního prediktivního ([LPC](/mobilnisite/slovnik/lpc/)) filtru k maskování kvantizačního šumu. Dekodér rekonstruuje spektrální koeficienty, provede inverzní MDCT pro získání excitačního signálu v časové doméně a ten pak profiltruje přes LPC syntézní filtr, čímž vytvoří výstupní audio. Režimy TCX se často používají v kodeku společně s režimy [ACELP](/mobilnisite/slovnik/acelp/) (Algebraic CELP), přičemž selektor režimu volí pro každý rámec nejlepší kódovací techniku na základě charakteristik signálu, čímž dosahuje vynikající rovnováhy mezi kvalitou řeči, kvalitou hudby a odolností vůči přenosovým chybám.

## K čemu slouží

TCX byl vytvořen, aby řešil omezení tradičních kodeků [CELP](/mobilnisite/slovnik/celp/) pracujících v časové doméně, zejména pro neřečové audio signály, jako je hudba, a pro poskytnutí vyšší kvality při nižších přenosových rychlostech. CELP vyniká v modelování periodické povahy znělé řeči, ale je méně efektivní pro kódování hudby, šumu na pozadí nebo neznělé řeči, což často vede k kovovým nebo robotickým artefaktům. Účelem TCX je poskytnout obecnější, na transformaci založený kódovací nástroj, který poskytuje konzistentně vysokou kvalitu pro širší škálu audio obsahu, což se stalo klíčovým s konvergencí hlasových a multimediálních služeb v mobilních sítích. Řeší problém neefektivního kódování širokopásmového a superširokopásmového audia, což umožňuje vysílání hudby v plném pásmu s vysokou kvalitou a hlasové hovory v rámci stejného kodekového rámce. Historickým motivem byl vývoj od úzkopásmové telefonie k vysokokvalitnímu hlasu a dále, což vyžadovalo kodeky schopné podporovat paradigma služeb „hlas a audio“ pro sítě LTE a 5G. TCX jako součást [EVS](/mobilnisite/slovnik/evs/) přímo reagoval na konkurenční potřebu kodeku nadřazeného stávajícím standardům, jako je [AMR-WB](/mobilnisite/slovnik/amr-wb/), a poskytl operátorům provozní flexibilitu a lepší uživatelský zážitek.

## Klíčové vlastnosti

- Kódování ve frekvenční doméně pomocí MDCT transformace
- Delší délky rámců pro zlepšenou efektivitu kódování stacionárních signálů
- Integrované percepční tvarování šumu založené na LPC analýze
- Efektivní algebraická vektorová kvantizace spektrálních koeficientů
- Bezešvá integrace s režimy ACELP v časové doméně v jednotném kodeku
- Vynikající výkonnost pro hudbu a smíšený obsah při nízkých až středních přenosových rychlostech

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [MDCT – Modified Discrete Cosine Transform](/mobilnisite/slovnik/mdct/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.274** (Rel-19) — AMR-WB+ Codec Conformance Testing Specification
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification

---

📖 **Anglický originál a plná specifikace:** [TCX na 3GPP Explorer](https://3gpp-explorer.com/glossary/tcx/)
