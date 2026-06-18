---
slug: "polqa"
url: "/mobilnisite/slovnik/polqa/"
type: "slovnik"
title: "POLQA – Perceptual Objective Listening Quality Assessment"
date: 2026-01-01
abbr: "POLQA"
fullName: "Perceptual Objective Listening Quality Assessment"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/polqa/"
summary: "POLQA je algoritmus standardizovaný ITU-T a 3GPP pro objektivní měření kvality řeči v telekomunikačních sítích. Predikuje lidské vnímání srozumitelnosti hlasu porovnáním původního a degradovaného zvuk"
---

POLQA je standardizovaný algoritmus pro objektivní měření kvality řeči porovnáním původního a degradovaného zvukového signálu za účelem predikce lidského vnímání; používá se pro testování hlasových služeb jako VoLTE a VoNR.

## Popis

Perceptual Objective Listening Quality Assessment (POLQA) je standardizovaná metodologie, definovaná v doporučení [ITU-T](/mobilnisite/slovnik/itu-t/) P.863 a přijatá 3GPP, pro objektivní hodnocení poslechové kvality systémů přenosu řeči. Jedná se o algoritmus s plnou referencí (full-reference), který porovnává původní referenční řečový signál s degradovanou verzí přijatou po průchodu sítí nebo kodekem a predikuje střední názorové skóre (Mean Opinion Score – [MOS](/mobilnisite/slovnik/mos/)), které by přiřadili lidské posluchači. POLQA funguje analýzou obou signálů v časově-frekvenční doméně a zohledňuje percepční faktory jako hlasitost, spektrální zkreslení a časové artefakty (např. zpoždění, ztráta paketů). Algoritmus modeluje lidský sluchový systém pomocí psychoakustického modelu, který váží chyby podle jejich percepční relevance, a zahrnuje pokročilé funkce pro práci s moderním širokopásmovým ([WB](/mobilnisite/slovnik/wb/)), super-širokopásmovým ([SWB](/mobilnisite/slovnik/swb/)) a plnopásmovým ([FB](/mobilnisite/slovnik/fb/)) audiem až do vzorkovací frekvence 48 kHz. Klíčové součásti POLQA zahrnují časové zarovnání pro kompenzaci přenosových zpoždění, percepční transformaci pro simulaci zpracování v uchu a kognitivní modelování pro odvození skóre MOS na škále typicky od 1 (špatné) do 5 (výborné). V sítích 3GPP se POLQA používá k hodnocení kvality hlasu pro služby jako Voice over LTE (VoLTE), Voice over NR (VoNR) a videohovory, testuje kodeky jako [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/) a Opus za různých síťových podmínek (např. chvění, ztráta paketů). Proces zahrnuje vstřikování testovacích signálů do sítě, zachycení výstupu a spuštění softwaru POLQA pro generování skóre, což pomáhá operátorům optimalizovat síťové parametry a zajistit soulad s QoS. POLQA nahrazuje starší algoritmy jako [PESQ](/mobilnisite/slovnik/pesq/) (ITU-T P.862) a nabízí vylepšenou přesnost pro HD hlas, odolnost vůči šumu a zpracování časových deformací (time-warping) od kodeků s proměnnou přenosovou rychlostí. Jeho role je klíčová v zajišťování kvality, protože umožňuje automatizované testování bez subjektivních lidských panelů, čímž snižuje náklady a čas pro nasazení a monitorování sítě. POLQA je integrován do testovacích zařízení a síťových sond, podporuje scénáře end-to-end a pasivního monitorování a je odkazován ve specifikacích 3GPP pro benchmarkování výkonu.

## K čemu slouží

POLQA byl vytvořen, aby řešil omezení předchozích metod hodnocení kvality řeči, zejména PESQ, které si neporadily s moderními širokopásmovými kodeky a síťovými degradacemi vyskytujícími se v VoIP a mobilních sítích. S vývojem telekomunikací směrem k HD hlasovým službám (např. VoLTE s AMR-WB) a později k vylepšeným hlasovým službám (EVS) v 4G/5G vznikla potřeba objektivního měřicího nástroje, který přesně odráží lidské vnímání napříč širšími audio pásmy a různými typy degradací. Motivací pro vývoj POLQA, standardizovaného ITU-T v roce 2011 a přijatého 3GPP od Release 13 dále, bylo poskytnout spolehlivou, standardizovanou metriku pro hodnocení kvality hlasu v plně IP sítích, řešící problémy jako nekonzistentní výsledky testů a nedostatečné zpracování časových zkreslení. Umožňuje síťovým operátorům a výrobcům zařízení kvantifikovat řečový výkon objektivně, zajišťuje spokojenost uživatelů a regulatorní soulad bez nutnosti spoléhat se na nákladné subjektivní poslechové testy. Historicky byly subjektivní MOS testy časově náročné a proměnlivé, zatímco rané objektivní algoritmy jako PESQ byly navrženy pro úzkopásmové okruhy a selhávaly při ztrátě paketů a chvění běžných v IP sítích. POLQA tuto mezeru zaplňuje začleněním pokročilých psychoakustických modelů a podporou super-širokopásmového audia, což je nezbytné pro hodnocení vysokokvalitních hlasových služeb poskytujících vynikající srozumitelnost. Jeho vznik byl hnán průmyslovou spoluprací na standardizaci testovacích metodologií, což usnadňuje interoperabilitu a benchmarkování kvality napříč globálními sítěmi. POLQA pomáhá řešit problémy s degradací kvality v reálných scénářích, jako je šum na pozadí, transkódování kodeků a síťová kongesce, což umožňuje proaktivní optimalizaci systémů hlasu přes LTE a 5G.

## Klíčové vlastnosti

- Algoritmus s plnou referencí (full-reference) porovnávající původní a degradované řečové signály
- Podporuje úzkopásmové, širokopásmové, super-širokopásmové a plnopásmové audio až do 48 kHz
- Predikuje skóre MOS na základě modelů lidského sluchového vnímání
- Zvládá moderní kodeky a síťové degradace jako ztrátu paketů a chvění (jitter)
- Obsahuje časové zarovnání pro proměnná zpoždění a časové deformace (time-warping distortions)
- Standardizován v ITU-T P.863 a přijat 3GPP pro testování kvality hlasu

## Související pojmy

- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [PESQ – Perceptual Evaluation of Speech Quality](/mobilnisite/slovnik/pesq/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TR 26.910** (Rel-19) — MTSI enhancements for RAN delay budget reporting

---

📖 **Anglický originál a plná specifikace:** [POLQA na 3GPP Explorer](https://3gpp-explorer.com/glossary/polqa/)
