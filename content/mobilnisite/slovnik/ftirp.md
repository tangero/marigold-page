---
slug: "ftirp"
url: "/mobilnisite/slovnik/ftirp/"
type: "slovnik"
title: "FTIRP – File Transfer Integration Reference Point"
date: 2025-01-01
abbr: "FTIRP"
fullName: "File Transfer Integration Reference Point"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ftirp/"
summary: "Standardizovaný referenční bod, který definuje způsob integrace přenosových schopností souborů do systému správy sítě (Network Management, NM) 3GPP. Specifikuje rozhraní a procedury pro severovýchodní"
---

FTIRP je standardizovaný referenční bod, který definuje rozhraní a procedury pro integraci služeb přenosu souborů ze správců prvků (Element Managers) nebo síťových prvků (Network Elements) k síťovým manažerům (Network Managers) v systému 3GPP.

## Popis

File Transfer Integration Reference Point (FTIRP) je konceptuální bod definovaný 3GPP, který standardizuje integraci služeb přenosu souborů v rámci hierarchie správy sítě. Není to protokol sám o sobě, ale specifikace služeb, operací a informací, které musí být podporovány napříč rozhraním mezi řídicími a řízenými systémy pro výměnu dat založenou na souborech. FTIRP je typicky realizován pomocí protokolů jako [FTAM](/mobilnisite/slovnik/ftam/) nebo jiných mechanismů přenosu souborů.

Architektonicky se FTIRP nachází mezi správcem prvku ([EM](/mobilnisite/slovnik/em/)) nebo síťovým prvkem ([NE](/mobilnisite/slovnik/ne/)) a nadřazeným síťovým manažerem ([NM](/mobilnisite/slovnik/nm/)). Definuje sadu služeb obecného přenosu souborů (Generic File Transfer, GFT), které musí nižší systém zpřístupnit manažerovi. Tyto služby zahrnují operace pro přenos souborů do řízeného systému a z něj, správu úloh přenosu souborů (např. naplánování, zrušení, monitorování) a získávání katalogů souborů. Specifikace FTIRP podrobně popisují požadované chování, stavové modely a požadavky na shodu pro implementaci těchto služeb.

Jak to funguje: systém NM vyvolá službu přenosu souborů (např. 'fileUpload' nebo 'fileDownload') na EM/NE prostřednictvím FTIRP. EM/NE následně provede přenos, který může zahrnovat jeho interního klienta FTAM nebo jiný mechanismus, a poskytne NM zpětná oznámení o stavu. FTIRP zajišťuje, že bez ohledu na dodavatele podkladového síťového prvku má NM konzistentní způsob, jak požadovat přenosy souborů pro účely jako je sběr záznamů o výkonu (PM), záznamů o poruchách nebo nasazení softwarových balíčků. Odstiňuje složitost skutečného protokolu přenosu souborů od řídicí aplikace, čímž podporuje interoperabilitu a zjednodušuje vývoj systému NM.

## K čemu slouží

FTIRP byl vytvořen, aby řešil nedostatek standardizovaného severovýchodního rozhraní pro operace přenosu souborů v rámci správy sítě. Před jeho definicí mohl každý správce prvku nebo síťový prvek zpřístupňovat proprietární rozhraní pro nahrávání/stahování souborů, což nutilo vývojáře síťových manažerů implementovat vlastní integrace pro každý typ spravovaného zařízení. To zvyšovalo náklady na integraci, zpomalovalo zavádění nových funkcí a bránilo správě sítí více dodavateli.

Hlavní problém, který FTIRP řeší, je poskytnutí jednotné, službami orientované abstrakce pro přenosové schopnosti souborů, kterou musí podporovat všechny kompatibilní řízené systémy. To umožňuje jednomu síťovému manažerovi používat stejnou sadu příkazů ke sběru logovacích souborů z základnové stanice, uzlu jádra sítě nebo mediačního zařízení. Jeho vytvoření bylo motivováno snahou o automatizovanější a integrovanější systémy [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/), kde bezproblémový sběr dat a distribuce softwaru jsou zásadní.

Definováním FTIRP umožnil 3GPP jasné oddělení odpovědností: [NM](/mobilnisite/slovnik/nm/) se soustředí na řídicí logiku (jaký soubor, kdy, odkud), zatímco [EM](/mobilnisite/slovnik/em/)/NE se stará o specifika protokolu skutečného přenosu (jak). Tento návrhový vzor je klíčový pro škálovatelnou správu moderních sítí, kde je třeba jednotně spravovat tisíce uzlů, a položil základy pro pozdější architektury správy, jako je framework Integration Reference Point (IRP).

## Klíčové vlastnosti

- Standardizovaný referenční bod pro severovýchodní služby přenosu souborů
- Definuje operace služby obecného přenosu souborů (Generic File Transfer, GFT)
- Odstiňuje podkladový protokol přenosu souborů (např. FTAM) od manažera
- Podporuje správu úloh přenosu souborů (naplánování, zrušení, monitorování)
- Umožňuje konzistentní procházení katalogů souborů ze síťových manažerů
- Podporuje interoperabilitu více dodavateli pro sběr OAM dat a distribuci softwaru

## Související pojmy

- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [FTAM – File Transfer, Access and Management](/mobilnisite/slovnik/ftam/)

## Definující specifikace

- **TS 32.345** (Rel-9) — XML Definitions for File Transfer IRP
- **TS 32.346** (Rel-19) — File Transfer IRP Solution Set Definitions
- **TS 32.411** (Rel-19) — PM IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [FTIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftirp/)
