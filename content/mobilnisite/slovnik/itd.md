---
slug: "itd"
url: "/mobilnisite/slovnik/itd/"
type: "slovnik"
title: "ITD – Inter-Channel Time Difference"
date: 2025-01-01
abbr: "ITD"
fullName: "Inter-Channel Time Difference"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/itd/"
summary: "Inter-Channel Time Difference (ITD) je parametr v audiokodecích 3GPP, zejména pro imerzivní hlasové služby, který představuje časový rozdíl zpoždění mezi audiokanály (např. levým a pravým). Je klíčovo"
---

ITD je parametr v audiokodecích 3GPP, který představuje časový rozdíl zpoždění mezi audiokanály, což umožňuje prostorové vykreslování zvuku a lokalizaci zdroje.

## Popis

Inter-Channel Time Difference (ITD) je základní binaurační vodítko používané při zpracování prostorového zvuku a je standardizováno v rámci 3GPP pro audiokodeky nové generace. Kvantifikuje rozdíl v čase příchodu zvukové vlny k levému a pravému uchu posluchače. Tento časový rozdíl je spolu s Inter-Channel Level Difference ([ILD](/mobilnisite/slovnik/ild/)) zásadní pro lidský sluchový systém, aby mohl lokalizovat zdroje zvuku v horizontální rovině. V kontextu 3GPP jsou parametry ITD generovány, kódovány, přenášeny a následně dekódovány, aby věrně rekonstruovaly prostorovou zvukovou scénu pro imerzivní služby, jako je Voice over New Radio (VoNR) s imerzivním hlasem, telekonference a aplikace Extended Reality ([XR](/mobilnisite/slovnik/xr/)).

Technická implementace zahrnuje snímání zvuku pomocí mikrofonních polí nebo analýzu zvukové scény založené na umělé inteligenci pro odhad směru příchodu různých zvukových zdrojů. Pro daný zvukový objekt nebo pár kanálů je ITD vypočítán, typicky v submilisekundovém rozsahu. V kodecích jako je Immersive Voice and Audio Services ([IVAS](/mobilnisite/slovnik/ivas/)) kodec definovaný v 3GPP TS 26.261 jsou tyto prostorové parametry (ITD, ILD a další) parametrizovány, kvantovány a efektivně paketizovány spolu se základním zvukovým signálem. Tato parametrická reprezentace je ve srovnání s přenosem plných vícekanálových zvukových proudů vysoce úsporná z hlediska šířky pásma. Na straně přijímače dekodér využívá přenesené hodnoty ITD spolu s modelem head-related transfer function ([HRTF](/mobilnisite/slovnik/hrtf/)) k syntéze binauračních zvukových signálů pro sluchátka, čímž vytváří vjem zvuku přicházejícího z konkrétních směrů.

Specifikace upravující ITD zahrnují TS 26.253 (konfigurace kodeku), TS 26.260 (specifikace kodeku IVAS) a TS 26.261 (podpora pro imerzivní konverzační služby). Architektura zahrnuje komponenty jak v UE (pro snímání a přehrávání), tak potenciálně v síti (pro zpracování médií). Přesné zachování a vykreslení ITD je klíčové pro kvalitu uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)) v imerzivní komunikaci, protože chyby mohou vést k rozmazanému nebo nesprávně umístěnému zvukovému obrazu, což narušuje pocit ponoření.

## K čemu slouží

ITD byl do standardů 3GPP zaveden, aby řešil omezení tradičních monofonních nebo stereofonních hlasových služeb, kterým chybí prostorová realističnost. Jelikož telekomunikace směřují k podpoře imerzivních zážitků, jako jsou virtuální schůzky, hraní her a [XR](/mobilnisite/slovnik/xr/), roste potřeba přenášet nejen zvukový obsah, ale také prostorové uspořádání zvukových zdrojů. To vytváří přirozenější, poutavější a efektivnější komunikační prostředí, které uživatelům umožňuje rozlišit více mluvčích na konferenčním hovoru, jako by byli ve stejné místnosti.

Problém, který řeší, je neefektivita přenosu diskrétního vícekanálového zvuku (např. 5.1 nebo Ambisonics) přes mobilní sítě z hlediska šířky pásma. Přenos nezpracovaného zvuku pro každý kanál spotřebovává nadměrné množství dat. Extrakcí a přenosem kompaktních prostorových parametrů, jako jsou ITD a [ILD](/mobilnisite/slovnik/ild/), mohou kodeky 3GPP znovu vytvořit přesvědčivou prostorovou zvukovou scénu za zlomek přenosové rychlosti. To činí imerzivní zvuk proveditelným pro masové mobilní služby.

Historicky se prostorové zvukové parametry používaly v profesionální audio technice a hraní her. Jejich zavedení v 3GPP Rel-18, zejména s kodekem [IVAS](/mobilnisite/slovnik/ivas/), bylo motivováno snahou průmyslu směřujícího k 5G-Advanced a 6G případům užití, které vyžadují ultrarealistickou komunikaci. Řeší omezení předchozích hlasových kodeků (jako AMR-WB nebo EVS), které, ačkoli kvalitní, byly primárně navrženy pro mono nebo stereo přehrávání bez vyhrazených prostorových vodítek. Standardizace ITD zajišťuje interoperabilitu mezi různými zařízeními a sítěmi a umožňuje konzistentní imerzivní zvukový zážitek napříč celým ekosystémem.

## Klíčové vlastnosti

- Kvantifikuje časový rozdíl zpoždění mezi audiokanály (např. signály pro levé/pravé ucho)
- Základní binaurační vodítko pro horizontální lokalizaci zdroje zvuku
- Parametrizováno a efektivně zakódováno v imerzivních audiokodecích (např. IVAS)
- Umožňuje přenos prostorových zvukových scén s vysokou efektivitou šířky pásma
- Používá se spolu s Inter-Channel Level Difference (ILD) a dalšími prostorovými parametry
- Klíčové pro vykreslování realistického 3D zvuku ve sluchátkách pro VR/AR a imerzivní telefonii

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals

---

📖 **Anglický originál a plná specifikace:** [ITD na 3GPP Explorer](https://3gpp-explorer.com/glossary/itd/)
