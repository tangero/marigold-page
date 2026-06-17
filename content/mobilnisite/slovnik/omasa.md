---
slug: "omasa"
url: "/mobilnisite/slovnik/omasa/"
type: "slovnik"
title: "OMASA – Objects (ISM) with Metadata-Assisted Spatial Audio"
date: 2025-01-01
abbr: "OMASA"
fullName: "Objects (ISM) with Metadata-Assisted Spatial Audio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/omasa/"
summary: "OMASA je standard 3GPP, který definuje formát pro přenos interaktivních prostorových zvukových objektů společně s immersivním videem, jako je 360° nebo volumetrický obsah. Umožňuje umístit zvukové obj"
---

OMASA je standard 3GPP, který definuje formát pro přenos interaktivních prostorových zvukových objektů umístěných v 3D prostoru společně s immersivním videem za účelem vylepšení mediálních zážitků.

## Popis

OMASA, standardizovaná v 3GPP TS 26.253 a souvisejících specifikacích, je pokročilý zvukový formát spadající do širší kategorie Interaktivních prostorových médií (Interactive Spatial Media, [ISM](/mobilnisite/slovnik/ism/)). Zaměřuje se na přenos zvukových objektů – diskrétních zvukových signálů spojených s konkrétním zdrojem zvuku ve scéně – doprovázených bohatými metadaty popisujícími jejich prostorové chování. Na rozdíl od kanálového (např. 5.1 surround) nebo scénového (např. Ambisonics) zvuku, formáty na bázi objektů, jako je OMASA, zachází s každým zvukem jako s nezávislou entitou s dynamickými atributy, jako je 3D pozice (souřadnice X, Y, Z), velikost, rychlost a zesílení. To umožňuje přesný rendering a interakci.

Architektura systému OMASA zahrnuje stranu tvorby a stranu přehrávání. Při tvorbě jsou zvukové objekty zachyceny nebo syntetizovány a jsou vytvořena jejich prostorová metadata (pozice v čase atd.). Tato data jsou následně zakódována a zabalena. OMASA využívá [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) a typicky používá framework Immersive Sound Model (ISM) definovaný MPEG-I. Zvukové objekty mohou být kódovány pomocí kodeků jako MPEG-H 3D Audio nebo AC-4. Klíčové je, že metadata jsou synchronizována s časovou osou médií a mohou být také propojena s vizuálními metadaty z doprovodného videa (např. ohraničující rámeček pro vizuální objekt).

Pro přenos OMASA podporuje adaptivní streamovací protokoly jako [DASH](/mobilnisite/slovnik/dash/). Na straně klienta/přehrávače přijímá OMASA renderer proudy zvukových objektů a jejich metadata. Pomocí rendereru (často součástí audio zpracování zařízení nebo dedikovaného SDK) vypočítá výsledný zvukový signál pro konkrétní výstupní nastavení posluchače (sluchátka, soustava reproduktorů) na základě aktuálních pozic objektů a orientace posluchače (sledované např. head-trackingu ve VR). To umožňuje, aby zvuky zůstaly pevně umístěny ve světovém prostoru, i když uživatel otáčí hlavou. V kontextu sítě je OMASA navržena pro spolupráci s video formáty jako [OMAF](/mobilnisite/slovnik/omaf/) a poskytuje tak kompletní audiovizuální immersivní zážitek, kde jsou zvukové objekty propojeny s vizuálními objekty nebo obecnými pozicemi ve scéně.

## K čemu slouží

OMASA byla vytvořena k řešení omezení tradičních zvukových formátů v interaktivních a immersivních mediálních scénářích. Pro 360° video a virtuální realitu může statický kanálový zvuk či dokonce Ambisonics prvního řádu postrádat přesnost a flexibilitu. Tyto formáty nedokážou snadno reprezentovat diskrétní, pohyblivé zdroje zvuku, které odpovídají konkrétním vizuálním objektům (např. postava, která hovoří, zatímco obchází uživatele). To narušuje immersi a snižuje pocit přítomnosti. OMASA to řeší tím, že poskytuje standardizovaný způsob popisu a přenosu takových dynamických zvukových objektů.

Klíčovým problémem, který řeší, je synchronizace a efektivní přenos zvuku, který je vnitřně propojen s vizuálními objekty a jejich metadaty. Před OMASA se používaly ad-hoc metody nebo proprietární formáty, což vedlo k problémům s interoperabilitou. OMASA poskytuje jednotný, interoperabilní formát, který zajišťuje, že zvukový objekt vykreslený jako ‚vzadu a nalevo‘ bude konzistentně reprodukován takto na jakémkoli kompatibilním přehrávacím zařízení. To je klíčové pro masové immersivní služby.

Jeho vývoj v 3GPP Rel-18 byl motivován vývojem immersivních médií za hranicemi jednoduchého 360° videa směrem k interaktivnějším a na objekty bohatším zážitkům, někdy označovaným jako ‚volumetrická média‘ nebo ‚média s 6 stupni volnosti (6DoF)‘. Jako součást širšího pracovního bodu Interactive Spatial Media ([ISM](/mobilnisite/slovnik/ism/)) umožňuje OMASA nové případy užití, jako je interaktivní vyprávění příběhů, sociální VR a immersivní trénink, kde zvukové objekty musí reagovat na interakci uživatele nebo změny scény. Staví na základech [OMAF](/mobilnisite/slovnik/omaf/) pro video a standardů MPEG-I pro audio, a vytváří tak kompletní, standardy založenou sadu nástrojů pro služby příští generace v 5G sítích.

## Klíčové vlastnosti

- Objektový zvuk s dynamickými 3D prostorovými metadaty (pozice, velikost, rychlost)
- Synchronizace zvukových objektů s metadaty vizuálních objektů z immersivního videa
- Podpora interaktivních scénářů, kde lze zvukové objekty aktivovat nebo upravovat
- Přenos prostřednictvím adaptivního streamování (DASH) s využitím ISOBMFF zapouzdření
- Rendering přizpůsobený orientaci hlavy posluchače pro zážitky typu VR/360°
- Využívá pokročilých zvukových kodeků, jako je MPEG-H 3D Audio, v rámci frameworku ISM

## Související pojmy

- [OMAF – Omnidirectional Media Application Format](/mobilnisite/slovnik/omaf/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals

---

📖 **Anglický originál a plná specifikace:** [OMASA na 3GPP Explorer](https://3gpp-explorer.com/glossary/omasa/)
