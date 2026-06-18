---
slug: "rdf"
url: "/mobilnisite/slovnik/rdf/"
type: "slovnik"
title: "RDF – Routing Determination Function"
date: 2025-01-01
abbr: "RDF"
fullName: "Routing Determination Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rdf/"
summary: "Síťová funkce, která určuje optimální směrovací cestu pro relace nebo zprávy na základě dat účastníka, služebních politik a stavu sítě. Používá se v systémech CAMEL, IMS a dalších 3GPP systémech k umo"
---

RDF je síťová funkce, která určuje optimální směrovací cestu pro relace nebo zprávy na základě dat účastníka, služebních politik a stavu sítě.

## Popis

Routing Determination Function (RDF) je logická entita v architekturách 3GPP, která vyhodnocuje směrovací kritéria pro výběr vhodné cesty pro relace nebo signalizační zprávy. Funguje v různých kontextech, jako je Customized Applications for Mobile networks Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) pro inteligentní síťování, IP Multimedia Subsystem (IMS) pro multimediální relace a systémy pro zasílání zpráv. RDF analyzuje vstupy, jako jsou cílové adresy, profily účastníků, služební triggery, denní doba a dostupnost sítě, aby vypočítala směrovací rozhodnutí. Architektonicky může být implementována jako část Service Control Point ([SCP](/mobilnisite/slovnik/scp/)) v CAMEL, Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v IMS nebo jako vyhrazený směrovací engine.

Při provozu, když dorazí požadavek na zahájení relace (např. [SIP](/mobilnisite/slovnik/sip/) INVITE v IMS nebo zpráva [ISUP](/mobilnisite/slovnik/isup/) v okruhově přepínaných sítích), je RDF vyvolána, aby určila další směrovací krok nebo konečný cíl. Přistupuje k databázím, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo servery [ENUM](/mobilnisite/slovnik/enum/), aby získala směrovací informace. Například v IMS používá RDF uvnitř S-CSCF initial Filter Criteria (iFC) k aktivaci služební logiky, která může změnit směrování na základě uživatelských preferencí. Mezi klíčové komponenty patří sady směrovacích pravidel, policy enginy a rozhraní k úložištím dat účastníků. Funkce podporuje pokročilé vlastnosti, jako je řešení přenositelnosti čísel, nejnižší nákladové směrování, přestup do jiných sítí (např. [PSTN](/mobilnisite/slovnik/pstn/)) a vyrovnávání zatížení mezi více aplikačními servery.

Role RDF je klíčová pro umožnění flexibilního poskytování služeb a efektivity sítě. Zajišťuje, že relace jsou směrovány podle obchodní logiky – například přesměrování hovorů na hlasovou schránku během špičky nebo výběr konkrétního mediálního brány pro mezinárodní hovory. V CAMEL RDF interaguje s gsmSCF k provedení přizpůsobených směrovacích skriptů pro předplacené služby nebo služby virtuální privátní sítě. V systémech 5G může být podobná směrovací logika vestavěna v Network Exposure Function (NEF) nebo Session Management Function (SMF) pro datové relace. Funkce musí zvládat požadavky v reálném čase, škálovatelnost pro vysoké objemy provozu a záložní mechanismy v případě selhání, což z ní dělá základní kámen inteligentních síťových operací.

## K čemu slouží

Routing Determination Function byla vyvinuta k poskytování dynamického, na politikách založeného směrování v telekomunikačních sítích, což představuje posun od statických směrovacích tabulek k podpoře pokročilých služeb a kontroly operátora. V raných mobilních sítích (před R99) bylo směrování často pevně zakódované nebo omezené na základní analýzu cíle, což bránilo funkcím jako přenositelnost čísel, personalizace služeb a efektivní využití zdrojů. RDF zavedla programovatelnou vrstvu, která umožňuje operátorům implementovat komplexní směrovací logiku na základě faktorů v reálném čase.

Řeší to problémy, jako je neefektivní dokončování hovorů, neschopnost přizpůsobit se přetížení sítě a nedostatek diferenciace služeb. Tím, že umožňuje inteligentní směrování, RDF podporuje výnosové služby, jako jsou bezplatná čísla, prémiové směrování a bezproblémová spolupráce mezi legacy a IP sítěmi. Její vytvoření bylo motivováno potřebou větší flexibility v nasazeních CAMEL a IMS, což operátorům umožňuje konkurovat inovativními nabídkami při optimalizaci využití sítě.

## Klíčové vlastnosti

- Vyhodnocuje více kritérií (účastník, služba, síť) pro směrovací rozhodnutí
- Integruje se s databázemi účastníků (HSS, ENUM) pro přístup k datům v reálném čase
- Podporuje služební logiku CAMEL a triggery IMS initial Filter Criteria
- Umožňuje optimalizace pro přenositelnost čísel a nejnižší nákladové směrování
- Poskytuje přestupové směrování do externích sítí (PSTN, jiní operátoři)
- Umožňuje vyrovnávání zatížení a převzetí služeb při selhání mezi síťovými elementy

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [RDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rdf/)
