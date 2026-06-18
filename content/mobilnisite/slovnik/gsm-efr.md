---
slug: "gsm-efr"
url: "/mobilnisite/slovnik/gsm-efr/"
type: "slovnik"
title: "GSM-EFR – GSM Enhanced Full Rate Speech Codec"
date: 2025-01-01
abbr: "GSM-EFR"
fullName: "GSM Enhanced Full Rate Speech Codec"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/gsm-efr/"
summary: "Standard kódování řeči definovaný v 3GPP TS 26.093, který poskytuje výrazně lepší kvalitu hlasu než původní GSM kodek plné rychlosti (FR). Používá pokročilé algoritmy algebraického kódového buzeného l"
---

GSM-EFR je vylepšený řečový kodek definovaný 3GPP, který využívá algoritmy ACELP k poskytnutí téměř pevné linkové kvality hlasu přes GSM kanál, což představuje významné zlepšení oproti původnímu kodeku plné rychlosti (Full Rate).

## Popis

Kodek GSM Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) je algoritmus komprese řeči standardizovaný pro systém GSM. Jeho technická specifikace je obsažena v 3GPP TS 26.093. Kodek pracuje s přenosovou rychlostí 12,2 kbit/s, což je stejné jako u původního kanálu GSM plné rychlosti ([FR](/mobilnisite/slovnik/fr/)), ale využívá mnohem pokročilejší schéma kódování založené na algebraickém kódovém buzeném lineárním prediktoru ([ACELP](/mobilnisite/slovnik/acelp/)). Proces kódování pracuje s 20ms rámci řeči vzorkovanými na 8 kHz. Pro každý rámec enkodér provede lineární prediktivní analýzu k extrakci parametrů reprezentujících filtr hlasového traktu (10 [LPC](/mobilnisite/slovnik/lpc/) koeficientů). Následně prohledá algebraický kodebook (pevný kodebook) a adaptivní kodebook (reprezentující výšku tónu), aby našel nejlepší excitační signál, který při průchodu LPC filtrem reprodukuje původní řeč s minimální chybou. Parametry filtru a indexy nejlepších položek kodebooku jsou kvantovány a přenášeny jako 244bitový blok každých 20 ms, což vede k rychlosti 12,2 kbit/s. Na straně dekodéru jsou tyto parametry použity k rekonstrukci excitačního signálu a syntéze řeči prostřednictvím LPC filtru. Jsou aplikovány postprocesní filtry pro zlepšení percepční kvality výstupu. Kodek EFR je navržen tak, aby byl odolný vůči přenosovým chybám. Používá nerovnoměrnou ochranu proti chybám, kdy nejpercepčně citlivějším bitům v zakódovaném rámci je přiřazeno nejsilnější kanálové kódování (konvoluční kódování), zatímco méně kritické bity dostávají slabší ochranu nebo žádnou. Tím je zajištěno postupné zhoršování kvality hlasu při špatných rádiových podmínkách. Kodek je implementován v digitálním signálovém procesoru ([DSP](/mobilnisite/slovnik/dsp/)) mobilní stanice a v transkódovací jednotce sítě, která se často nachází v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). Když spolu komunikují dvě mobilní zařízení s podporou EFR, je řeč kódována a dekódována pouze na koncových bodech, čímž je zachována kvalita. Při komunikaci se zařízením bez podpory EFR síť provádí transkódování do kompatibilního formátu.

## K čemu slouží

Kodek GSM-EFR byl vyvinut, aby řešil hlavní kritiku kvality hlasu v raných digitálních celulárních sítích, která byla často popisována jako 'robotická' nebo 'syntetická' ve srovnání s analogovými systémy nebo pevnými linkami. Původní kodek GSM plné rychlosti ([FR](/mobilnisite/slovnik/fr/)), ačkoliv ve své době zázrak, používal relativně jednoduché schéma Regular Pulse Excitation-Long Term Prediction ([RPE-LTP](/mobilnisite/slovnik/rpe-ltp/)), které mělo jasná kvalitativní omezení, zejména v přítomnosti šumu na pozadí nebo pro určité typy mluvčích. Motivací pro EFR bylo zvýšit kvalitu hlasu v sítích GSM na úroveň srovnatelnou s pevnou linkovou telefonii, čímž se zlepšila spokojenost zákazníků a GSM se stalo konkurenceschopnějším. Vyřešil problém špatně vnímané kvality, aniž by vyžadoval změny v základní struktuře GSM rádiového kanálu nebo přenosové rychlosti, protože byl navržen pro stávající 13 kbit/s přenosový kanál (22,8 kbit/s po kanálovém kódování). Toto bylo klíčové konstrukční omezení, které umožnilo nasazení aktualizací softwaru v sítích a mobilních zařízeních. Vývoj EFR byl hnán konkurencí a snahou o 'prémiovou' hlasovou službu. Vyřešil omezení kodeku FR použitím špičkové ACELP technologie, která poskytovala nadřazené modelování řečového signálu a excitace. Jeho zavedení v Rel-8 (jako součást konsolidovaných specifikací 3GPP, ačkoliv byl původně vyvinut dříve organizací ETSI) představovalo významný milník ve skutečnosti kvalitního digitálního mobilního hlasu a připravilo cestu pro pozdější kodeky jako AMR, které stavěly na jeho principech.

## Klíčové vlastnosti

- Pracuje s čistou přenosovou rychlostí 12,2 kbit/s (vyhovuje kanálu GSM plné rychlosti)
- Používá algoritmus algebraického kódového buzeného lineárního prediktoru (ACELP)
- Zpracovává 20ms rámce řeči (244 bitů/rámec)
- Poskytuje téměř pevnou linkovou (toll-quality) percepci řeči
- Obsahuje robustní nerovnoměrnou ochranu proti chybám (UEP) pro kanálové chyby
- Zpětně kompatibilní se strukturou kanálu GSM FR pro nasazení v síti

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)

## Definující specifikace

- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS

---

📖 **Anglický originál a plná specifikace:** [GSM-EFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsm-efr/)
