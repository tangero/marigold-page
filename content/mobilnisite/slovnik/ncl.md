---
slug: "ncl"
url: "/mobilnisite/slovnik/ncl/"
type: "slovnik"
title: "NCL – Neighbour Cell List"
date: 2025-01-01
abbr: "NCL"
fullName: "Neighbour Cell List"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncl/"
summary: "Seznam sousedních buněk nakonfigurovaný sítí a poskytovaný uživatelskému zařízení (UE) pro podporu procedur měření buněk a přechodů mezi buňkami. Obsahuje klíčové parametry, jako jsou fyzické identifi"
---

NCL je síťově nakonfigurovaný seznam sousedních buněk, poskytovaný uživatelskému zařízení (UE) pro usnadnění měření buněk a přechodů mezi buňkami (handover), který obsahuje klíčové parametry jako fyzické identifikátory buněk a kmitočty.

## Popis

Seznam sousedních buněk (NCL) je klíčový koncept správy mobility v celulárních sítích, včetně UMTS, LTE a NR. Jedná se o databázi nebo informační prvek udržovaný sítí (např. základnovou stanicí nebo [RNC](/mobilnisite/slovnik/rnc/)) a sdělovaný uživatelskému zařízení (UE), aby jej informoval o blízkých buňkách, které jsou potenciálními kandidáty pro měření a přechody mezi buňkami. NCL obsahuje položky pro každou sousední buňku, typicky včetně parametrů jako fyzický identifikátor buňky ([PCI](/mobilnisite/slovnik/pci/)), kmitočet nosné a v závislosti na technologii i dalších informací, jako je kód sledovací oblasti nebo globální identifikátor buňky. Ve specifikacích 3GPP je NCL spravován jako součást konfigurace řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a je doručován uživatelskému zařízení prostřednictvím systémových informačních bloků ([SIB](/mobilnisite/slovnik/sib/)) nebo vyhrazené signalizace RRC (např. RRCConnectionReconfiguration).

Z architektonického hlediska je NCL generován a udržován systémem provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)) sítě nebo prostřednictvím funkcí samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), jako je automatický vztah sousedních buněk ([ANR](/mobilnisite/slovnik/anr/)). Obsluhující buňka sestavuje seznam na základě síťového plánování, historických dat o přechodech a hlášení od uživatelských zařízení. Když uživatelské zařízení NCL obdrží, použije tyto informace k omezení svých měřicích úsilí na určené buňky a kmitočty, namísto provádění slepého prohledávání celého spektra. Tím se snižuje spotřeba baterie uživatelského zařízení, urychluje se hlášení měření a zajišťují se včasná rozhodnutí o přechodu mezi buňkami. Uživatelské zařízení měří referenční signály (např. [PSS](/mobilnisite/slovnik/pss/)/SSS v NR, CRS v LTE) od uvedených buněk a hlásí metriky, jako je přijatý výkon referenčního signálu (RSRP) a jeho kvalitu (RSRQ), zpět do sítě, která pak tato data použije k vyvolání přechodů mezi buňkami, je-li to nutné.

Jak to funguje, zahrnuje průběžnou optimalizaci: síť dynamicky aktualizuje NCL na základě měření od uživatelských zařízení, úspěšnosti přechodů a změn v topologii (např. nasazení nových buněk). V pokročilých sítích funkce ANR umožňuje síti automaticky objevovat nové vztahy sousedních buněk, když uživatelská zařízení detekují buňky, které nejsou v aktuálním NCL, a hlásí je síti k přidání. Role NCL je klíčová pro bezproblémovou mobilitu, koordinaci rušení a vyrovnávání zatížení. Zajišťuje, že se uživatelská zařízení mohou při pohybu rychle a spolehlivě připojit k nejlepší dostupné buňce, čímž se udržuje kontinuita služby a kvalita uživatelského zážitku. Specifikace jako TS 25.300 (UTRAN), TS 36.300 (E-UTRAN) a TS 38.300 (NR) podrobně popisují její procedury a parametry.

## K čemu slouží

NCL byl zaveden, aby vyřešil základní výzvu efektivního objevování buněk a přechodů mezi buňkami v celulárních sítích. V raných systémech bez předdefinovaného seznamu sousedních buněk musela uživatelská zařízení provádět rozsáhlá a časově náročná skenování všech možných kmitočtů, aby našla vhodné cíle pro přechod, což vedlo k opožděným přechodům, přerušeným hovorům a vysoké spotřebě baterie. To bylo obzvláště problematické, jak sítě houstly s více buňkami a kmitočtovými vrstvami. NCL poskytuje řízený přístup tím, že uživatelskému zařízení přesně řekne, kde má hledat, a tím optimalizuje proces měření.

Jeho vytvoření bylo motivováno potřebou robustní správy mobility pro podporu bezproblémových hlasových a datových služeb při pohybu uživatelů. Předkonfigurací známých vztahů sousedních buněk mohou sítě zajistit rychlejší a spolehlivější přechody, snížit rušení a zlepšit celkovou kapacitu systému. V průběhu vydání specifikací se NCL vyvinul ze statického, ručně konfigurovaného seznamu na dynamickou, samooptymalizující se komponentu prostřednictvím funkcí SON, jako je ANR, která automaticky aktualizuje seznam na základě hlášení uživatelských zařízení v reálném čase. Tím se řeší omezení ručního plánování, které je náchylné k chybám a nepružné v měnícím se síťovém prostředí, a umožňuje se tak adaptivnější a efektivnější mobilita v moderních heterogenních sítích.

## Klíčové vlastnosti

- Obsahuje parametry jako fyzický identifikátor buňky a kmitočet nosné pro sousední buňky
- Konfigurován síťovým OAM nebo funkcemi SON, jako je Automatický vztah sousedních buněk (ANR)
- Doručen uživatelskému zařízení prostřednictvím systémových informací nebo vyhrazené signalizace RRC
- Snižuje dobu měření a spotřebu baterie uživatelského zařízení omezením rozsahu hledání
- Umožňuje včasná rozhodnutí o přechodu mezi buňkami na základě cílených měření uživatelského zařízení
- Dynamicky aktualizován na základě hlášení uživatelských zařízení a změn síťové topologie

## Definující specifikace

- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [NCL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncl/)
