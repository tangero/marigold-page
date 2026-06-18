---
slug: "ior"
url: "/mobilnisite/slovnik/ior/"
type: "slovnik"
title: "IOR – Interoperable Object Reference"
date: 2025-01-01
abbr: "IOR"
fullName: "Interoperable Object Reference"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ior/"
summary: "Standardizovaný formát reference na objekt používaný v systémech správy sítí 3GPP, konkrétně pro framework Integration Reference Point (IRP). Umožňuje konzistentní identifikaci a správu spravovaných o"
---

IOR je standardizovaný formát reference na objekt používaný v systémech správy sítí 3GPP, který zajišťuje konzistentní identifikaci a správu objektů napříč více-dodavatelskými a více-doménovými sítěmi.

## Popis

Interoperable Object Reference (IOR, referenční identifikátor objektu pro interoperabilitu) je základní koncept v rámci modelu síťových zdrojů ([NRM](/mobilnisite/slovnik/nrm/)) a architektury Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)) 3GPP, definovaný v řadě specifikací 32 pro správu a orchestraci. Slouží jako jedinečný standardizovaný identifikátor pro spravované objekty ([MO](/mobilnisite/slovnik/mo/)) v telekomunikační síti. IOR není pouze jednoduchý název; jedná se o strukturovanou referenci, která zapouzdřuje identitu MO, včetně jeho hierarchie umístění v rámci stromu správy informací sítě. Tato struktura typicky zahrnuje prvky jako distinguished name ([DN](/mobilnisite/slovnik/dn/)) objektu, který definuje jeho pozici vůči kořeni stromu správy, a další atributy nezbytné pro jednoznačnou identifikaci.

Architektonicky jsou IOR používány systémy správy, jako jsou Element Managers ([EM](/mobilnisite/slovnik/em/)), Network Managers ([NM](/mobilnisite/slovnik/nm/)) a Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)), k adresování a manipulaci se specifickými síťovými zdroji. Když nadřazený systém správy vydá příkaz (např. GET, [SET](/mobilnisite/slovnik/set/), CREATE, DELETE) přes IRP rozhraní, jako je Basic CM IRP nebo Notification IRP, použije IOR k přesné identifikaci cílového objektu v bázi správy informací (MIB) podřízeného síťového elementu. Tento mechanismus je klíčový pro řešení založená na CORBA nebo později na webových službách/HTTP používaných v implementacích IRP. IOR zajišťuje, že příkaz určený pro konkrétní základnovou stanici, konkrétní buňku nebo kontext uživatelského zařízení je správně směrován a proveden.

Jeho role přesahuje pouhé provádění příkazů. IOR jsou nedílnou součástí mechanismů odběru a notifikací. Systém správy se může přihlásit k odběru notifikací (např. alarmů, změn stavu) týkajících se konkrétních spravovaných objektů. Žádost o odběr obsahuje IOR pro definici rozsahu zájmu. Když dojde ke změně, síťový element vygeneruje notifikaci obsahující IOR zasaženého objektu, což umožňuje systému správy korelovat události se svým interním modelem. To umožňuje efektivní správu poruch, monitorování výkonu a správu konfigurace ve velkých heterogenních sítích. Standardizace formátu IOR je tím, co umožňuje více-dodavatelskou interoperabilitu na úrovni správy, neboť poskytuje společný 'jazyk' pro identifikaci zdrojů, oddělující logiku správy od dodavatelsky specifických implementací samotných spravovaných zdrojů.

## K čemu slouží

IOR byl vytvořen k řešení zásadní výzvy v telekomunikačním managementu: absence standardizovaného způsobu, jak jednoznačně a konzistentně identifikovat síťové zdroje napříč zařízeními a systémy správy různých dodavatelů. Před jeho standardizací proprietární schémata pojmenování a odkazování ztěžovala integraci mezi systémy OSS/BSS a síťovými elementy od více dodavatelů, což bylo složité, nákladné a náchylné k chybám. To bránilo automatizované provizionování, korelaci poruch a zajištění služeb end-to-end v prostředích s více dodavateli.

Zavedení IOR jako součásti frameworku 3GPP IRP ve Release 8 poskytlo formální interoperabilní řešení. Bylo motivováno přechodem průmyslu k otevřenějším, standardizovaným rozhraním správy za účelem snížení provozních nákladů (OPEX) a urychlení nasazování nových služeb. Definováním společného referenčního modelu umožňuje IOR vývoj aplikací správy nezávisle na podkladové síťové technologii a dodavateli, což podporuje konkurenční ekosystém a zjednodušuje správu životního cyklu sítě.

Jeho existence řeší omezení ad-hoc nebo dodavatelsky uzamčených paradigmat správy. Umožňuje skutečnou integraci síťových elementů typu plug-and-play na úrovni řídicí roviny, což je pro provozní efektivitu stejně kritické jako interoperabilita na uživatelské rovině (např. hlasové hovory, datové relace). IOR je základním předpokladem pro automatizovanou, politikami řízenou správu sítě a v konečném důsledku pro koncepty jako Self-Organizing Networks (SON) a orchestrace síťových řezů, které spoléhají na přesné, programovatelné řízení specifických síťových zdrojů.

## Klíčové vlastnosti

- Standardizovaný jedinečný identifikátor pro spravované objekty v rámci 3GPP NRM
- Zapouzdřuje distinguished name (DN) a hierarchii umístění objektu
- Umožňuje jednoznačné adresování v operacích rozhraní IRP založených na CORBA a následných
- Klíčový pro vymezení rozsahu příkazů správy (GET, SET, CREATE, DELETE)
- Základní pro mechanismy odběru a notifikací v rámci správy poruch a výkonu
- Zajišťuje více-dodavatelskou interoperabilitu na úrovni správy sítě

## Související pojmy

- [CORBA – Common Object Request Broker Architecture](/mobilnisite/slovnik/corba/)

## Definující specifikace

- **TS 32.303** (Rel-9) — Notification IRP CORBA Solution Set
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set

---

📖 **Anglický originál a plná specifikace:** [IOR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ior/)
