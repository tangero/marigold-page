---
slug: "pesq"
url: "/mobilnisite/slovnik/pesq/"
type: "slovnik"
title: "PESQ – Perceptual Evaluation of Speech Quality"
date: 2026-01-01
abbr: "PESQ"
fullName: "Perceptual Evaluation of Speech Quality"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pesq/"
summary: "Objektivní metoda standardizovaná ITU-T (ITU-T P.862) pro automatické hodnocení kvality řeči, jak ji vnímají lidské posluchače. Porovnává degradovaný řečový signál (např. po přenosu sítí) s čistým ref"
---

PESQ je objektivní metoda standardizovaná ITU-T pro automatické hodnocení vnímané kvality řeči porovnáním degradovaného signálu s čistým referenčním signálem za účelem predikce středního hodnotícího skóre (MOS).

## Popis

Perceptual Evaluation of Speech Quality (PESQ) je algoritmus definovaný v doporučení [ITU-T](/mobilnisite/slovnik/itu-t/) P.862 pro objektivní predikci subjektivní kvality úzkopásmových a širokopásmových řečových kodeků tak, jak by ji ohodnotili lidské posluchače v poslechovém testu. Na rozdíl od jednoduchých měření poměru signálu a šumu PESQ modeluje lidský sluchový systém, aby poskytl hodnocení s vysokou korelací s výsledky subjektivních testů středního hodnotícího skóre ([MOS](/mobilnisite/slovnik/mos/)). Algoritmus přijímá dva vstupy: původní, nezkreslený referenční řečový signál a degradovaný výstupní signál, který prošel testovaným systémem (např. hlasový kodek, paketová síť nebo kompletní cesta hlasového hovoru). PESQ provádí percepční transformaci obou signálů, časově je zarovná, aby kompenzovalo zpoždění, a následně je porovná, aby vypočítalo hodnotu poruchy, která kvantifikuje vnímané rozdíly.

Interní zpracování PESQ zahrnuje několik klíčových fází. Nejprve provede zarovnání úrovně a času, aby zajistilo spravedlivé srovnání, a opraví variace zesílení a hrubá přenosová zpoždění. Poté jsou oba signály transformovány do percepčně relevantní reprezentace pomocí modelu lidského sluchového systému, který zahrnuje kmitočtové přeškálování (na Barkovu stupnici), aby napodobil nelineární kmitočtovou citlivost ucha. Algoritmus následně vypočítá percepční poruchu, která je kombinací „asymetrické“ poruchy (kde je přidaný šum nebo zkreslení váhován) a „symetrické“ poruchy (pro jiná lineární zkreslení). Tyto poruchy jsou agregovány v čase a kmitočtu, čímž vzniknou dvě mezihodnoty: hustota poruchy a hustota asymetrické poruchy.

Nakonec PESQ mapuje tyto agregované hodnoty poruchy na predikci subjektivního skóre poslechové kvality. Výstupem je surové PESQ skóre, které typicky leží v rozsahu od -0,5 do 4,5 a může být dále mapováno na stupnici [MOS-LQO](/mobilnisite/slovnik/mos-lqo/) (Mean Opinion Score - Listening Quality Objective) od 1 (špatné) do 5 (výborné). Zatímco je PESQ vysoce účinné pro hodnocení jednosměrných zhoršení kvality řeči, jako jsou zkreslení kodeku, ztráta paketů a šum, má svá omezení. Nemodeluje efekty velmi dlouhých zpoždění, ozvěny nebo místního tónu, které jsou lépe hodnoceny jinými metrikami, jako je [POLQA](/mobilnisite/slovnik/polqa/) (P.863). V rámci 3GPP je PESQ odkazováno (např. v TS 22.179 pro služby Mission Critical Push-to-Talk) jako standardní metodologie pro definování minimálních požadavků na výkonnost kvality řeči pro kodeky a koncové systémy, čímž zajišťuje konzistentní a opakovatelný kvalitativní benchmark v rámci odvětví.

## K čemu slouží

PESQ bylo vyvinuto, aby vyřešilo kritickou potřebu efektivní, opakovatelné a standardizované metody pro hodnocení kvality řeči v telekomunikacích, která by nahradila nákladné a časově náročné subjektivní poslechové testy. Před objektivními modely, jako je PESQ, byl jedinou spolehlivou cestou k posouzení percepční kvality řečového kodeku nebo síťové cesty provedení formálních subjektivních testů s lidskými posluchači, které jsou drahé, pomalé a obtížně konzistentně opakovatelné v různých laboratořích a podmínkách. S rozšířením digitálních hlasových kodeků a paketových sítí (jako je VoIP) odvětví potřebovalo nástroj pro rychlý vývoj, optimalizaci a benchmarkování algoritmů zpracování řeči.

Primární motivací bylo vytvořit algoritmus, který by dokázal přesně napodobit výsledky poslechového testu absolutního kategoriálního hodnocení ([ACR](/mobilnisite/slovnik/acr/)), zlatého standardu pro subjektivní kvalitu definovaného v [ITU-T](/mobilnisite/slovnik/itu-t/) P.800. PESQ řešilo nedostatky dřívějších objektivních modelů (jako PSQM), které si neporadily s moderními zkresleními specifickými pro kodeky, jako je proměnné zpoždění a výpadky rámců běžné v paketových sítích. Začleněním sofistikovanějšího percepčního modelu a robustního časového zarovnání poskytlo PESQ vysokou korelaci s lidskými soudy pro širokou škálu zhoršení, včetně kódovacích zkreslení, ztráty paketů, chvění (jitteru) a efektů překódování.

Jeho přijetí standardizačními orgány, jako jsou 3GPP a ITU-T, umožnilo výrobcům zařízení a síťovým operátorům specifikovat a ověřovat výkonnost kvality řeči konzistentním způsobem. Například 3GPP používá skóre odvozená z PESQ k definování minimálních kvalitativních prahů pro hlasové služby přes LTE (VoLTE) a 5G (VoNR), čímž zajišťuje základní uživatelský zážitek. Stalo se nepostradatelným nástrojem pro výzkum a vývoj, plánování sítě, monitorování kvality a ověřování smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), což odvětví umožnilo s důvěrou nasazovat nové hlasové technologie při zachování nebo zlepšení vnímané kvality hovoru.

## Klíčové vlastnosti

- Objektivní predikce subjektivní poslechové kvality (MOS)
- Vysoká korelace s subjektivními poslechovými testy ITU-T P.800
- Robustní časové zarovnání pro zvládnutí proměnných síťových zpoždění
- Percepční modelování založené na lidském sluchovém systému (Barkova stupnice)
- Hodnocení zhoršení od kodeků, ztráty paketů a šumu
- Výstup surového PESQ skóre a namapované hodnoty MOS-LQO

## Související pojmy

- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TS 22.179** (Rel-20) — MCPTT Service Requirements

---

📖 **Anglický originál a plná specifikace:** [PESQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/pesq/)
