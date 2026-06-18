---
slug: "upcm"
url: "/mobilnisite/slovnik/upcm/"
type: "slovnik"
title: "UPCM – Uniform or Linear Pulse Code Modulation"
date: 2025-01-01
abbr: "UPCM"
fullName: "Uniform or Linear Pulse Code Modulation"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/upcm/"
summary: "Standardizovaná metoda pro analogově-digitální převod hlasových signálů v sítích GSM/UMTS. Definuje lineární schéma kódování, typicky využívající 13bitové nebo 16bitové rozlišení, k zajištění vysoce k"
---

UPCM je standardizovaná lineární metoda kódování pro analogově-digitální převod hlasu v sítích GSM/UMTS, využívající 13bitové nebo 16bitové rozlišení k zajištění vysoké kvality hlasového přenosu.

## Popis

Uniform or Linear Pulse Code Modulation (UPCM) je základní technika kódování hlasu standardizovaná v 3GPP pro okruhově přepínané hlasové služby, především v doménách GSM a UMTS. Na rozdíl od kompandovacích algoritmů, jako je A-zákon nebo μ-zákon, které používají nelineární kvantování k optimalizaci pro lidské sluchové vnímání, UPCM používá lineární kvantovací stupnici. To znamená, že velikost kroku mezi úrovněmi kvantování je konstantní v celém rozsahu amplitudy vstupního analogového signálu. Proces zahrnuje vzorkování hlasového signálu standardní rychlostí (např. 8 kHz) a každý vzorek je přímo kvantován do digitálního kódového slova s použitím jednotné velikosti kroku. Typické implementace odkazované ve specifikacích jsou 13bitové nebo 16bitové lineární [PCM](/mobilnisite/slovnik/pcm/), poskytující vysoký dynamický rozsah a věrnost vhodné pro rozhraní páteřní sítě před případným překódováním na účinnější kodeky pro rádiový přenos.

Z architektonického hlediska je UPCM specifikováno pro použití na specifických referenčních bodech a rozhraních v síti, zejména tam, kde je třeba přenášet vysokokvalitní, nekomprimovaný (nebo lehce komprimovaný) hlas. Je definováno v technických specifikacích, jako jsou 3GPP TS 46.008 a TS 46.055, které detailně popisují funkce zpracování řeči pro systém GSM. Jeho role je často jako mezilehlý nebo 'kotvící' kódovací formát. Například hlasové volání pocházející z mobilního zařízení používajícího kodek jako [AMR-NB](/mobilnisite/slovnik/amr-nb/) může být v páteřní síti (např. v Mobile Switching Center nebo Media Gateway) překódováno na UPCM pro přenos přes tradiční [TDM](/mobilnisite/slovnik/tdm/) (Time-Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)) trunky nebo pro rozhraní s dalšími síťovými elementy, které očekávají lineární PCM.

Klíčovými komponentami jsou funkce kodeku v síťových prvcích, jako je Transcoder and Rate Adaptation Unit ([TRAU](/mobilnisite/slovnik/trau/)) nebo Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)). Tyto komponenty provádějí analogově-digitální a digitálně-analogové převody nebo překódování mezi různými digitálními formáty. Lineární povaha UPCM zjednodušuje určité operace zpracování signálu, jako je potlačení echa, detekce hlasové aktivity a generování tónů, ve srovnání s prací s kompandovanými signály. Zatímco spotřebovává více šířky pásma na kanál než komprimované kodeky (např. 64 kbps pro 8bitový μ-zákon/A-zákon nebo 104/128 kbps pro 13/16bitový lineární), jeho použití je oprávněné v segmentech páteřní sítě, kde je šířka pásma dostatečná a zachování kvality signálu je prvořadé před případnou další ztrátovou kompresí pro rádiový přenos.

## K čemu slouží

UPCM bylo zavedeno, aby poskytlo standardizovanou, vysoce věrnou digitální reprezentaci hlasových signálů pro přenos a přepínání v rámci infrastruktury páteřní sítě systémů 2G a 3G. Před GSM a současně s ním telekomunikační sítě široce používaly kompandované [PCM](/mobilnisite/slovnik/pcm/) (A-zákon/μ-zákon) pro digitální hlas, které optimalizuje poměr signál-šum pro typické hlasové amplitudy, ale zavádí nelinearitu. Vytvoření standardu jednotného PCM řešilo potřebu lineárního, předvídatelného kódovacího schématu, které zjednodušuje určité úlohy zpracování hlasu na straně sítě.

Motivace vycházela z architektury raných digitálních mobilních sítí, které často oddělovaly rádiově specifický řečový kodek (jako Full Rate nebo Enhanced Full Rate v GSM) od přenosové páteřní sítě. Páteřní síť, často založená na principech [ISDN](/mobilnisite/slovnik/isdn/) nebo PSTN, vyžadovala stabilní digitální formát pro přepínání a propojení. UPCM sloužilo jako společný, vysokokvalitní mezilehlý formát. Řešilo problém udržení kvality hlasu přes více stupňů případného překódování, zejména když hovory procházely různými síťovými doménami nebo vyžadovaly zpracování síťovými službami, jako je konferenční hovor nebo hlasové oznámení. Jeho lineární charakter přímo řeší omezení kompandovaných formátů, kde jsou lineární operace (jako sčítání dvou hlasových signálů v konferenčním můstku) složitější a mohou degradovat kvalitu, pokud nejsou zpracovány správně.

## Klíčové vlastnosti

- Lineární kvantování s konstantní velikostí kroku napříč amplitudou signálu
- Typicky implementováno jako 13bitové nebo 16bitové rozlišení na vzorek
- Standardní vzorkovací frekvence 8 kHz pro telefonní šířku pásma
- Definováno pro aplikace přenosu a rozhraní v páteřní síti
- Zjednodušuje lineární operace zpracování signálu, jako je míchání a filtrování
- Slouží jako společný mezilehlý formát pro překódování mezi různými řečovými kodeky

## Související pojmy

- [PCM – Pulse Code Modulation](/mobilnisite/slovnik/pcm/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [TRAU – Transcoder and Rate Adaptation Unit (Frame)](/mobilnisite/slovnik/trau/)

## Definující specifikace

- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [UPCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/upcm/)
