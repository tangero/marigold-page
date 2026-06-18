---
slug: "vbv"
url: "/mobilnisite/slovnik/vbv/"
type: "slovnik"
title: "VBV – Video Buffering Verifier"
date: 2025-01-01
abbr: "VBV"
fullName: "Video Buffering Verifier"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vbv/"
summary: "Video Buffering Verifier je teoretický model používaný ve standardech videokódování k omezení variability zakódovaného datového toku, který zajišťuje, že jej může plynule dekódovat hypotetický dekodér"
---

VBV je Video Buffering Verifier, teoretický model ve videokódování, který omezuje variabilitu datového toku, aby zajistil plynulé dekódování hypotetickým dekodérem s definovanou velikostí vyrovnávací paměti, a zabraňuje tak jejímu vyprázdnění nebo přeplnění.

## Popis

Video Buffering Verifier (VBV) je bod shody definovaný ve specifikacích videokódování, například v těch, na které odkazuje 3GPP pro doručování médií (např. H.264/[AVC](/mobilnisite/slovnik/avc/) v TS 26.937). Nejde o fyzické zařízení, ale o konceptuální model – hypotetickou vyrovnávací paměť dekodéru – sloužící k vynucení omezení pro datový tok generovaný enkodérem. Model se skládá z vyrovnávací paměti určité velikosti (VBV buffer), která se plní definovanou rychlostí (konstantní nebo proměnnou) a vyprazdňuje se okamžitým dekódováním snímků v přesných časových intervalech. Základním pravidlem je, že datový tok musí být vytvořen tak, aby tato hypotetická paměť nikdy nevyprázdnila (což by způsobilo nedostatek dat pro dekodér) ani nepřetekla (což by vedlo ke ztrátě dat).

Jeho fungování je nedílnou součástí procesu kódování. Enkodér lokálně modeluje stejnou VBV paměť. Při kódování každého snímku (I, P nebo B obrazu) vypočítá, kolik bitů tento snímek přidá do paměti a kolik jich bude odebráno při okamžitém dekódování snímku v jeho určeném čase prezentace. Při práci s konstantním datovým tokem ([CBR](/mobilnisite/slovnik/cbr/)) se paměť plní konstantní přenosovou rychlostí a enkodér musí regulovat svůj výstup, aby vyhověl tomuto striktnímu modelu, často za použití algoritmů řízení toku, které upravují kvantizační parametry. Při práci s proměnným datovým tokem ([VBR](/mobilnisite/slovnik/vbr/)) se může paměť plnit špičkovou rychlostí, což umožňuje větší flexibilitu, ale omezení týkající se zaplnění paměti stále platí. Specifikace 3GPP odkazují na tato VBV omezení, aby zajistily interoperabilitu; datový tok vyhovující VBV modelu může být dekódován jakýmkoli standardním dekodérem s vyrovnávací pamětí alespoň specifikované velikosti.

Úloha VBV v ekosystému 3GPP spočívá v poskytnutí formální záruky dekódovatelnosti přenášených videodatových toků. Když mediální server připravuje obsah pro streamování nebo vysílání přes [MBMS](/mobilnisite/slovnik/mbms/), musí generovat datový tok, který odpovídá konkrétnímu VBV modelu (např. jak je definováno na určité úrovni standardu H.264). To umožňuje síti zacházet s videem jako s datovým kanálem se známými požadavky na vyrovnávací paměť v nejhorším případě. Pro přijímací zařízení to znamená, že může alokovat skutečnou dekódovací paměť velikosti specifikované VBV a být si jisté, že za předpokladu včasného doručení paketů sítí, může být video dekódováno a přehráno bez přerušení způsobených porušením modelu paměti. Jde o kritický článek mezi kompresní vrstvou a transportní vrstvou, který umožňuje předvídatelné přehrávání na mobilních zařízeních s omezenými prostředky.

## K čemu slouží

VBV byl vytvořen, aby vyřešil základní problém nevyváženosti přenosových rychlostí mezi videokodéry s proměnným datovým tokem a kanálovými nebo dekódovacími vyrovnávacími paměťmi. Rané systémy digitálního videa se potýkaly s problémy, kdy enkodér mohl vyprodukovat záplavu složitých snímků, která by přetekla konečnou vyrovnávací paměť dekodéru, nebo dlouhé období jednoduchých snímků mohlo způsobit vyprázdnění paměti před časem dekódování dalšího snímku. To vedlo k zamrznutí videa, přeskočení snímků nebo poškozenému přehrávání.

Jeho zavedení, vycházející z [MPEG-2](/mobilnisite/slovnik/mpeg-2/) a pevně přijaté v pozdějších kodecích jako H.264 a [HEVC](/mobilnisite/slovnik/hevc/), poskytlo standardizovaný matematický model pro omezení variability datového toku. To umožnilo nezávislý vývoj enkodérů a dekodérů při zachování interoperability. Pro 3GPP, které standardizuje přenos těchto videodatových toků přes mobilní sítě, bylo odkazování na VBV model zásadní. Poskytlo jasný, na kodeku nezávislý způsob specifikace požadavků na vyrovnávací paměť a časová omezení mediálního datového toku, což se promítá do návrhu transportních protokolů (např. [RTP](/mobilnisite/slovnik/rtp/)) a mediálních schopností zařízení.

Motivací bylo umožnit spolehlivé, kvalitní videoslužby přes nepředvídatelné kanály, jako je mobilní rádiové rozhraní. Omezením datového toku pomocí VBV mohlo síťové plánování a poskytování QoS zohlednit nejhorší případ potřeb vyrovnávací paměti. Řešilo to omezení ad-hoc řízení přenosové rychlosti enkodéru, které mohlo produkovat datové toky nehratelné na standardních dekodérech. V kontextu Rel-8 a eMBMS 3GPP byl VBV model klíčový pro vysílací služby, kde miliony zařízení potřebují spolehlivě dekódovat stejný datový tok, což činí standardizované dodržování shody paměti nezbytným pro kvalitu služby.

## Klíčové vlastnosti

- Hypotetický model dekodéru pro definici shody datového toku
- Zabraňuje vyprázdnění vyrovnávací paměti (nedostatku dat v dekodéru) a jejímu přeplnění (ztrátě dat)
- Podporuje režimy kódování s konstantním (CBR) i proměnným (VBR) datovým tokem
- Definuje velikost vyrovnávací paměti (VBV buffer) a parametry přenosové rychlosti v hlavičkách datového toku
- Umožňuje interoperabilní návrh dekodérů se známými požadavky na paměť vyrovnávací paměti
- Integrován do standardů videokódování (např. H.264, HEVC), na které odkazuje 3GPP

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [VBV na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbv/)
