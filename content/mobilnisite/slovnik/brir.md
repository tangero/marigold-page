---
slug: "brir"
url: "/mobilnisite/slovnik/brir/"
type: "slovnik"
title: "BRIR – Binaural Room Impulse Response"
date: 2025-01-01
abbr: "BRIR"
fullName: "Binaural Room Impulse Response"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/brir/"
summary: "BRIR je prostorová reprezentace zvuku, která zachycuje, jak se zvuk šíří od zdroje k oběma uším v konkrétním akustickém prostředí. Modeluje přenosové funkce závislé na hlavě (HRTF) a odrazy od místnos"
---

BRIR je prostorová reprezentace zvuku, která zachycuje, jak se zvuk šíří od zdroje k oběma uším v konkrétním akustickém prostředí, a to modelováním přenosových funkcí závislých na hlavě (HRTF) a odrazů od místnosti.

## Popis

Binaural Room Impulse Response (BRIR) je komplexní akustický model, který charakterizuje, jak se zvukové vlny šíří od zdroje zvuku k levému a pravému uchu posluchače v konkrétním akustickém prostředí. Na rozdíl od jednoduchých přenosových funkcí závislých na hlavě ([HRTF](/mobilnisite/slovnik/hrtf/)), které modelují pouze směrové filtrační efekty hlavy, ramen a ušních boltců, BRIR zahrnuje jak tyto anatomické efekty, tak i komplexní odrazy, dozvuk a akustické vlastnosti okolní místnosti nebo prostoru. BRIR je v podstatě dvojice impulsních odezev (jedna pro každé ucho), které při konvoluci se zvukovým signálem vytvoří binaurální výstup simulující zážitek poslechu daného zdroje zvuku v daném akustickém prostředí z konkrétní polohy.

Technicky lze BRIR rozložit na několik složek: přímou složku (zvuk putující přímo od zdroje k posluchači), časné odrazy (zřetelné ozvěny od stěn a povrchů přicházející v prvních 50–100 milisekundách) a pozdní dozvuk (hustý, postupně slábnoucí ocas zvukových odrazů). Raná část BRIR je klíčová pro prostorovou lokalizaci a pomáhá mozku určit směr a vzdálenost zdroje zvuku, zatímco pozdní dozvuk poskytuje informace o velikosti, tvaru a akustických vlastnostech prostředí. BRIR se typicky měří pomocí specializovaného vybavení: v akustickém prostředí je umístěna figurína hlavy s mikrofony v uších a impulsní odezvy se zaznamenávají přehráním známého testovacího signálu (jako je sinusový sweep nebo sekvence maximální délky) z různých pozic zdroje.

Ve standardech 3GPP hraje BRIR klíčovou roli v ponořujících multimediálních službách, zejména pro aplikace rozšířené reality ([XR](/mobilnisite/slovnik/xr/)) standardizované v systémech 5G. Specifikace 3GPP definují formáty, metadata a mechanismy pro doručování BRIR dat, aby zajistily interoperabilitu napříč zařízeními a sítěmi. BRIR data mohou být buď předem nahraná pro známá prostředí, nebo dynamicky generována/přizpůsobována na základě kontextu uživatele. Při integraci s audiokodeky a vykreslovacími enginy umožňuje BRIR vytváření přesvědčivých 3D audio scén, kde se virtuální zdroje zvuku zdají vycházet ze specifických míst kolem posluchače, čímž zvyšuje pocit přítomnosti a ponoření v zážitcích virtuální, rozšířené nebo smíšené reality.

Implementace BRIR v systémech 3GPP zahrnuje několik technických aspektů. BRIR data musí být efektivně komprimována pro přenos přes sítě s omezenou šířkou pásma, a to při zachování percepční kvality prostorového audio zážitku. Metadata doprovázející BRIR popisují parametry jako pozici zdroje, orientaci posluchače, rozměry místnosti a akustické materiály. Ve scénářích adaptivního streamování mohou být parametry BRIR aktualizovány v reálném čase, jak se uživatel pohybuje virtuálním prostředím nebo mění orientaci hlavy. Proces vykreslování zahrnuje konvoluci neupraveného (dry) audio signálu s příslušným BRIR pro každý zdroj zvuku a následné smíchání těchto zpracovaných signálů k vytvoření konečného binaurálního výstupu dodávaného do sluchátek nebo náhlavních souprav.

## K čemu slouží

Technologie BRIR byla vyvinuta, aby řešila zásadní výzvu vytváření přesvědčivých prostorových audio zážitků v aplikacích virtuální a rozšířené reality. Tradiční stereo a surround formáty poskytují omezené prostorové informace a nedokážou přesně reprodukovat komplexní akustické interakce, které probíhají v reálných prostředích. S vývojem technologií [XR](/mobilnisite/slovnik/xr/) vzrostla potřeba audio renderingu, který by odpovídal vizuálnímu ponoření a vytvářel koherentní multisenzorický zážitek, kde zvuky zdánlivě vycházejí z konkrétních míst v 3D prostoru, včetně realistické akustiky prostředí.

Vytvoření standardů BRIR v rámci 3GPP bylo motivováno nástupem sítí 5G, které jsou schopné podporovat ponořující multimediální služby s nízkou latencí a vysokými požadavky na šířku pásma. Předchozí audio technologie, jako základní [HRTF](/mobilnisite/slovnik/hrtf/), poskytovaly směrové informace, ale postrádaly kontext prostředí, což vedlo k zvuku, který zněl 'suchě' a byl odtržený od virtuálních prostředí. BRIR tuto limitaci řeší začleněním akustiky místnosti, což umožňuje zvuk, který odpovídá prostorovým charakteristikám vizuální scény. To bylo obzvláště důležité pro aplikace jako teleprezence, virtuální schůzky, hraní her a zážitky z kulturního dědictví, kde autentická akustická prostředí významně zvyšují realismus a zapojení uživatele.

Standardizace BRIR v rámci 3GPP zajišťuje interoperabilitu napříč zařízeními, sítěmi a poskytovateli obsahu, čímž předchází fragmentaci vznikajícího ekosystému XR. Definováním společných formátů, metadat a mechanismů doručování umožňuje 3GPP tvůrcům obsahu produkovat ponořující audio zážitky, které konzistentně fungují na různém hardwaru a v různých síťových podmínkách. Tato standardizace také usnadňuje efektivní síťové doručování prostřednictvím kompresních technik a adaptivního streamování, což činí kvalitní prostorový zvuk praktickým pro masové aplikace přes mobilní sítě.

## Klíčové vlastnosti

- Kombinuje přenosové funkce závislé na hlavě s modelováním akustiky místnosti
- Umožňuje realistickou 3D audio lokalizaci a ponoření do prostředí
- Podporuje statická i dynamická akustická prostředí
- Standardizované formáty pro interoperabilitu napříč systémy 3GPP
- Efektivní komprese pro síťový přenos
- Podpora metadat pro pozici zdroje, vlastnosti místnosti a orientaci posluchače

## Související pojmy

- [HRTF – Head-Related Transfer Function](/mobilnisite/slovnik/hrtf/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP

---

📖 **Anglický originál a plná specifikace:** [BRIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/brir/)
