---
slug: "celp"
url: "/mobilnisite/slovnik/celp/"
type: "slovnik"
title: "CELP – Code Excited Linear Prediction"
date: 2025-01-01
abbr: "CELP"
fullName: "Code Excited Linear Prediction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/celp/"
summary: "CELP je řečový kódovací algoritmus standardizovaný organizací 3GPP pro hlasové služby v mobilních sítích. Poskytuje vysoce kvalitní řečovou kompresi s nízkým datovým tokem pomocí modelování lidského h"
---

CELP je řečový kódovací algoritmus standardizovaný organizací 3GPP, který poskytuje vysoce kvalitní kompresi s nízkým datovým tokem modelováním lidského hlasového traktu a využitím kodebooku excitačních signálů pro efektivní přenos hlasu v mobilních sítích.

## Popis

Code Excited Linear Prediction (CELP) je pokročilý řečový kódovací algoritmus, který tvoří základ několika hlasových kodeků 3GPP, nejvýznamněji rodiny kodeků Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)). V jádru je CELP hybridní kodek kombinující principy zdrojového kódování (lineární prediktivní kódování, [LPC](/mobilnisite/slovnik/lpc/)) a vlnového kódování. Algoritmus pracuje tak, že analyzuje krátká rámce řeči (typicky 20 ms) a extrahuje parametry modelující spektrální obálku řečového signálu pomocí lineární predikce. Tento LPC filtr reprezentuje krátkodobé korelace v řeči a efektivně modeluje rezonanční vlastnosti hlasového traktu. Reziduální signál – rozdíl mezi původní řečí a výstupem LPC filtru – je pak aproximován pomocí excitačního signálu vybraného z pevného kodebooku.

Kodér CELP pracuje v cyklu analýza-syntéza. Pro každý rámec řeči prohledává kodebook možných excitačních vektorů (stochastických nebo algebraických), aby našel ten, který po průchodu LPC syntézním filtrem vytvoří syntetizovanou řeč nejlépe odpovídající původnímu vstupu podle percepčního kritéria chyby. Tento percepční váhový filtr zvýrazňuje chyby ve frekvenčních oblastech, kde je lidské ucho citlivější, čímž zlepšuje subjektivní kvalitu řeči. Vybraný index kodebooku spolu s koeficienty LPC filtru (často převedenými na Line Spectral Pairs nebo [LSP](/mobilnisite/slovnik/lsp/) pro efektivitu kvantizace), parametry zesílení a případně dalšími doplňkovými informacemi jsou přeneseny do dekodéru.

V dekodéru jsou přijaté parametry použity pro rekonstrukci řečového signálu. Excitační vektor je získán ze stejného kodebooku, škálován zesílením a zaveden do LPC syntézního filtru, který vytvoří syntetizovaný rámec řeči. Často jsou aplikovány postprocesní techniky, jako je adaptivní post-filtrování, pro zvýšení percepční kvality snížením kvantizačního šumu. Struktura CELP je vysoce adaptabilní a umožňuje vícebitové provozní režimy, kdy lze datový tok dynamicky upravovat na základě síťových podmínek a hlasové aktivity, což umožňuje kompromis mezi kvalitou řeči a využitím šířky pásma.

V ekosystému 3GPP je CELP implementován v různých specifikacích kodeků. Kodek AMR, definovaný v 3GPP TS 26.090, používá pro své hlavní módy strukturu Algebraic CELP ([ACELP](/mobilnisite/slovnik/acelp/)). ACELP používá algebraický kodebook, kde excitační pulzy mají pevné, předdefinované pozice a amplitudy, čímž zjednodušuje vyhledávání v kodebooku. Širokopásmový kodek [AMR-WB](/mobilnisite/slovnik/amr-wb/) specifikovaný v TS 26.190 rozšiřuje CELP na širší zvukové pásmo (50–7000 Hz) pro lepší přirozenost a srozumitelnost. Tyto kodeky jsou nedílnou součástí služby Voice over LTE (VoLTE), zajišťující zpětnou kompatibilitu a vysokou kvalitu hlasu napříč generacemi mobilních sítí.

## K čemu slouží

CELP byl vyvinut pro řešení kritické potřeby efektivní digitální komprese řeči v mobilních komunikačních systémech s omezenou šířkou pásma. Předchozí řečové kodeky, jako je Pulse Code Modulation ([PCM](/mobilnisite/slovnik/pcm/)) používaná v tradiční telefonii, spotřebovávaly 64 kbit/s, což bylo pro omezené rádiové spektrum buněčných sítí nepraktické. Starší vokodéry jako Regular Pulse Excitation-LPC (RPE-LPC) používané v GSM Full Rate poskytovaly kompresi, ale s kompromisem v kvalitě. CELP se objevil jako řešení pro dosažení kvality řeči na úrovni meziměstských hovorů při výrazně nižších datových tocích (např. 4,75 až 12,2 kbit/s v [AMR](/mobilnisite/slovnik/amr/)), což umožnilo více hlasových kanálů na buňku a zlepšilo kapacitu sítě.

Vznik CELP byl motivován pokrokem v digitálním zpracování signálu a výpočetním výkonu v 80. letech 20. století. Přístup analýza-syntéza a percepční optimalizace algoritmu mu umožnily překonat omezení jednodušších vlnových kodérů a parametrických vokodérů. Přesným modelováním mechanismu tvorby řeči a použitím kodebooku pro reprezentaci excitace dosáhl CELP lepší rovnováhy mezi efektivitou datového toku a kvalitou řeči. To jej učinilo ideálním pro vyvíjející se standardy digitálních buněčných sítí, kde byla efektivita spektra a kvalita hlasu prvořadá pro přijetí uživateli a komerční úspěch.

V rámci 3GPP standardizace CELP založených kodeků jako AMR zajistila interoperabilitu mezi zařízeními různých výrobců a konzistentní kvalitu hlasových služeb při vývoji sítí z GSM/[EDGE](/mobilnisite/slovnik/edge/) na UMTS a LTE. Možnost vícebitového provozu CELP kodeků umožnila sítím dynamicky přizpůsobovat datový tok řeči na základě rádiových podmínek (např. použití nižších datových toků při špatném pokrytí pro zachování kontinuity hovoru) a vytížení provozu, optimalizovat kvalitu i kapacitu. Tato přizpůsobivost byla klíčová pro přechod na plně IP sítě a VoLTE, kde se hlas stává jen další datovou službou, ale s přísnými požadavky na latenci a kvalitu.

## Klíčové vlastnosti

- Hybridní řečové kódování kombinující LPC modelování zdroje s kodebookovou excitací
- Optimalizace analýzou-syntézou s percepčním váhováním pro vysokou kvalitu
- Vícebitový provoz umožňující dynamickou adaptaci datového toku od 4,75 do 12,2 kbit/s (AMR)
- Struktura Algebraic Codebook (ACELP) pro efektivní reprezentaci excitace
- Širokopásmové rozšíření (AMR-WB) podporující zvukové pásmo 50-7000 Hz
- Odolnost vůči přenosovým chybám díky redundanci parametrů a skrývání chyb

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [LPC – Linear Predictive Coding](/mobilnisite/slovnik/lpc/)

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.274** (Rel-19) — AMR-WB+ Codec Conformance Testing Specification
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 46.020** (Rel-19) — GSM Half Rate Speech Codec Specification
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec

---

📖 **Anglický originál a plná specifikace:** [CELP na 3GPP Explorer](https://3gpp-explorer.com/glossary/celp/)
