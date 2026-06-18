---
slug: "rtti"
url: "/mobilnisite/slovnik/rtti/"
type: "slovnik"
title: "RTTI – Real-time Transfer of Tariff Information"
date: 2025-01-01
abbr: "RTTI"
fullName: "Real-time Transfer of Tariff Information"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rtti/"
summary: "RTTI je standardizovaný mechanismus pro výměnu informací o účtování a tarifech mezi síťovými operátory a poskytovateli služeb v reálném čase. Umožňuje přesné a okamžité vyúčtování služeb, jako jsou pr"
---

RTTI je standardizovaný mechanismus pro výměnu informací o účtování a tarifech mezi síťovými operátory a poskytovateli služeb v reálném čase, který umožňuje přesné a okamžité vyúčtování.

## Popis

Real-time Transfer of Tariff Information (RTTI) je klíčovou součástí architektury účtování v rámci 3GPP, konkrétně definovanou pro [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile networks Enhanced Logic) a další systémy online účtování. Funguje jako protokol a rámec pro výměnu dat, který umožňuje okamžitou komunikaci tarifních detailů – jako jsou náklady na službu, ratingové skupiny a parametry účtování – mezi síťovými entitami, jako je Service Control Point ([SCP](/mobilnisite/slovnik/scp/)) nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)), a síťovými prvky provádějícími službu (např. [MSC](/mobilnisite/slovnik/msc/), [SGSN](/mobilnisite/slovnik/sgsn/), GGSN). Tato schopnost fungovat v reálném čase je zásadní pro služby, u kterých musí být cena známa a autorizována před nebo během jejich poskytnutí, čímž se předchází úniku příjmů a umožňují se modely předplaceného a konvergentního účtování.

Architektura RTTI je integrována do signalizační a řídicí roviny. Když účastník zahájí zpoplatnitelnou událost (např. hovor na prémiové číslo nebo mobilní datovou relaci), síťový prvek se dotazuje účtovacího systému prostřednictvím standardizovaných rozhraní, jako je [CAP](/mobilnisite/slovnik/cap/) (CAMEL Application Part). Účtovací systém odpoví s příslušnými tarifními informacemi, které mohou zahrnovat cenu, měnu a dobu platnosti. Tyto informace jsou pak použity k autorizaci služby, aplikaci správné účtovací sazby a případnému upozornění účastníka prostřednictvím mechanismů, jako je Advice of Charge (AoC). Tento proces zajišťuje synchronizaci účtování s využitím služby, podporuje složité tarifní plány, akce a vypořádání mezi operátory.

Klíčové komponenty zapojené do RTTI zahrnují Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)), která detekuje zpoplatnitelné události; Online Charging System (OCS), který uchovává tarifní data a provádí rating; a prostředí CAMEL služeb, které poskytuje rámec inteligentní sítě pro řízení v reálném čase. Role RTTI přesahuje rámec jednoduchého účtování; je základem pro diferenciaci služeb, což operátorům umožňuje nabízet přizpůsobené účtování v reálném čase pro služby s přidanou hodnotou, roamingové scénáře a nové datové služby, čímž zlepšují zákaznický zážitek a provozní efektivitu.

## K čemu slouží

RTTI bylo vytvořeno, aby řešilo omezení tradičních systémů účtování založených na dávkovém zpracování nebo účtování po události, které byly nedostačující pro dynamické služby v reálném čase vznikající v mobilních sítích. Před jeho standardizací se účtování prémiových služeb nebo předplacených účtů často opíralo o zpožděnou výměnu dat, což vedlo k nepřesnostem, ztrátám příjmů a špatnému zákaznickému zážitku kvůli neočekávaným poplatkům. Růst služeb inteligentní sítě, jako je [CAMEL](/mobilnisite/slovnik/camel/), vyžadoval mechanismus pro autorizaci a tarifikaci služeb v reálném čase, který by zajistil, že účastníci mohou být účtováni přesně v okamžiku spotřeby.

Primární problém, který RTTI řeší, je potřeba okamžitého vyřešení tarify a řízení kreditu. Pro předplacené účastníky umožňuje kontrolu zůstatku a odčítání v reálném čase, čímž zabraňuje využití služeb nad rámec dostupného kreditu. Pro účtování postpaid a konvergentní účtování umožňuje okamžitou aplikaci složitých tarifních pravidel, jako jsou sazby podle denní doby nebo balíčky pro konkrétní služby. Tato schopnost je klíčová pro ochranu příjmů operátora, protože minimalizuje riziko nezaplaceného využití a podporuje sofistikované obchodní modely pro poskytovatele obsahu a služeb třetích stran.

Historicky byl vývoj RTTI v 3GPP Release 8 a jeho pokračování v následujících verzích motivováno evolucí směrem k plně IP sítím a rostoucí rozmanitostí zpoplatnitelných služeb, od SMS po mobilní broadband. Poskytuje standardizovaný, interoperabilní rámec, který nahrazuje proprietární řešení a usnadňuje bezproblémový roaming a nasazení sítí od více dodavatelů. Tím, že zajišťuje transparentnost a kontrolu tarifů v reálném čase, RTTI podporuje komerční životaschopnost moderních mobilních služeb.

## Klíčové vlastnosti

- Výměna tarifních informací v reálném čase během poskytování služby
- Integrace s architekturami CAMEL a Online Charging System (OCS)
- Podpora modelů účtování předplacených (prepaid) i následně placených (postpaid) služeb
- Umožňuje upozornění účastníka prostřednictvím Advice of Charge (AoC)
- Usnadňuje účtování mezi operátory a roamingové zúčtování
- Standardizováno v rámci specifikací 3GPP pro zajištění interoperability

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.002** (Rel-19) — GSM/EDGE Radio Physical Layer Specification
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [RTTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtti/)
