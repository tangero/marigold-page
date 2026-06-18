---
slug: "gdmo"
url: "/mobilnisite/slovnik/gdmo/"
type: "slovnik"
title: "GDMO – Guidelines for the Definition of Managed Objects"
date: 2025-01-01
abbr: "GDMO"
fullName: "Guidelines for the Definition of Managed Objects"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/gdmo/"
summary: "GDMO je standardizovaný rámec a jazyk pro definici spravovaných objektů v telekomunikačních sítích, jak je specifikováno v ITU-T X.722 a přijato 3GPP. Poskytuje formální, objektově orientovaný model p"
---

GDMO je standardizovaný rámec pro definici spravovaných objektů v telekomunikačních sítích, který poskytuje formální, objektově orientovaný model umožňující konzistentní a interoperabilní správu sítí napříč systémy více dodavatelů.

## Popis

Guidelines for the Definition of Managed Objects (GDMO) je formální specifikační jazyk standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) v doporučení X.722 a přijatý ve specifikacích 3GPP pro správu sítí. Poskytuje základní metodologii pro definici spravovaných objektů, což jsou abstraktní reprezentace fyzických nebo logických síťových zdrojů, jako jsou síťové elementy, softwarové moduly nebo spojení. Spravovaný objekt je charakterizován svými atributy, které uchovávají informace o stavu; svými operacemi, což jsou akce, které na něm lze provést (jako GET, [SET](/mobilnisite/slovnik/set/) nebo notifikace); a svým chováním, které definuje, jak objekt reaguje na operace a interní události. GDMO používá objektově orientovaný přístup, který umožňuje dědičnost, kdy lze nové třídy objektů definovat jako rozšíření stávajících, což podporuje znovupoužitelnost a hierarchickou strukturu informací pro správu.

Architektura Management Information Base ([MIB](/mobilnisite/slovnik/mib/)) založené na GDMO je ústřední pro systémy správy sítí, jako je rámec Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)). Definice vytvořené pomocí GDMO jsou kompilovány do reprezentace Abstract Syntax Notation One (ASN.1), která slouží jako strojově čitelná schéma pro spravované objekty. K těmto objektům je pak přistupováno prostřednictvím managementových protokolů, především Common Management Information Protocol ([CMIP](/mobilnisite/slovnik/cmip/)), ačkoli existují adaptace pro [SNMP](/mobilnisite/slovnik/snmp/). Klíčové komponenty definice GDMO zahrnují šablonu třídy objektu, která pojmenovává třídu a specifikuje její nadřazené třídy; šablony atributů, které definují vlastnosti; šablony akcí a notifikací pro operace; a šablony parametrů pro datové struktury.

V síti 3GPP se GDMO rozsáhle používá k definici spravovaných objektů pro síťové elementy (NEs) napříč různými doménami, včetně vrstev Network Management ([NM](/mobilnisite/slovnik/nm/)), Domain Management ([DM](/mobilnisite/slovnik/dm/)) a Element Management (EM). Například specifikace jako 3GPP TS 32.102 (Telecommunication management architecture) a TS 32.150 (Integration Reference Point (IRP) concept and definitions) se opírají o principy GDMO, aby zajistily, že managementová data ze základnové stanice nebo funkce jádra sítě jsou modelována konzistentně. Tato konzistence umožňuje Operations Support Systems (OSS) spravovat heterogenní zařízení od různých dodavatelů prostřednictvím jednotného rozhraní, abstrahující implementace specifické pro dodavatele za standardizovaným objektovým modelem. Role GDMO tedy spočívá v poskytování sémantické a syntaktické přesnosti nezbytné pro interoperabilní, škálovatelnou a automatizovanou správu chyb, konfigurace, účtování, výkonu a zabezpečení (FCAPS) v komplexních sítích 3GPP.

## K čemu slouží

GDMO bylo vytvořeno, aby řešilo kritickou výzvu interoperability více dodavatelů v rozsáhlých telekomunikačních sítích. Před jeho standardizací byla správa sítí často proprietární, přičemž každý dodavatel zařízení poskytoval jedinečná rozhraní a datové modely pro správu. To činilo integraci systémů od různých dodavatelů do soudržného Operations Support System (OSS) pro provozovatele sítí extrémně obtížnou a nákladnou, což vedlo k provozní neefektivitě, vyšším integračním nákladům a závislosti na dodavateli. Rámec TMN od ITU-T, koncipovaný v 80. letech, představoval vrstvený, standardizovaný přístup ke správě a GDMO se objevilo jako nezbytný modelovací jazyk pro naplnění této vize tím, že poskytlo společný způsob popisu jakéhokoli spravovatelného zdroje.

Historický kontext spočívá ve vývoji od jednoduché, protokolem řízené správy (jako jsou jednoduchá vázání proměnných v SNMP) směrem k robustnějšímu, objektově orientovanému a transakčně orientovanému modelu vyžadovanému pro komplexní telekomunikační zařízení. Struktura MIB v SNMP, definovaná pomocí SMI, byla shledána nedostatečnou pro sofistikované chování a bohaté vztahy potřebné v telekomunikačních sítích. GDMO spolu s CMIP nabídlo výkonnější alternativu podporující komplexní operace, vymezení rozsahu, filtrování a potvrzované hlášení událostí. Jeho přijetí 3GPP, zejména pro správu sítí 3G UMTS a následných sítí, bylo hnací silou potřeby rigorózního, budoucím vývojem odolného základu pro definici všech informací pro správu, od inventáře fyzického hardwaru po softwarové čítače výkonu a parametry na úrovni služeb.

Zatímco novější paradigmata správy, jako NETCONF/YANG, získala na významu pro webovou a datovým modelem řízenou správu, účel GDMO při vytváření formálního, objektově orientovaného základu zůstává historicky významný. Vyřešilo základní problém, jak jednoznačně definovat, co lze v síti spravovat, oddělujíc informační model od komunikačního protokolu. To umožnilo vytvoření standardizovaných Integration Reference Points (IRPs) v 3GPP, což dovolilo systémům správy interagovat se síťovými elementy předvídatelným, na dodavateli nezávislým způsobem, což je základním kamenem moderních automatizovaných síťových operací.

## Klíčové vlastnosti

- Objektově orientované modelování síťových zdrojů pomocí formálních definic tříd
- Podpora dědičnosti, umožňující novým třídám spravovaných objektů rozšiřovat stávající
- Definice atributů, akcí, notifikací a chování v rámci standardizovaných šablon
- Těsná integrace s ASN.1 pro přesnou specifikaci datových typů a kódování
- Protokolem nezávislý informační model, primárně navržený pro použití s CMIP
- Umožňuje vytvoření standardizované, hierarchické Management Information Base (MIB)

## Související pojmy

- [CMIP – Common Management Information Protocol](/mobilnisite/slovnik/cmip/)

## Definující specifikace

- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.150** (Rel-19) — IRP Concept and Definitions
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- **TS 32.866** (Rel-15) — REST, HTTP, JSON for Management Interfaces

---

📖 **Anglický originál a plná specifikace:** [GDMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/gdmo/)
