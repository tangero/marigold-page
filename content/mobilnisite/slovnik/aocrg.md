---
slug: "aocrg"
url: "/mobilnisite/slovnik/aocrg/"
type: "slovnik"
title: "AOCRG – Add-On Charging Information"
date: 2025-01-01
abbr: "AOCRG"
fullName: "Add-On Charging Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aocrg/"
summary: "AOCRG je mechanismus účtování dle 3GPP, který operátorům umožňuje aplikovat dodatečné, kontextově specifické poplatky nad rámec základních tarifů služeb. Umožňuje dynamické cenotvorba na základě vzorc"
---

AOCRG je mechanismus účtování dle 3GPP, který operátorům umožňuje aplikovat dodatečné, kontextově specifické poplatky nad rámec základních tarifů služeb na základě vzorců využití, typu obsahu nebo stavu sítě.

## Popis

Add-On Charging Information (AOCRG, informace o doplňkovém účtování) představuje sofistikovaný rámec účtování v rámci sítí 3GPP, který operátorům umožňuje implementovat doplňková pravidla účtování nad rámec standardních tarifů služeb. Architektura je integrována s rámcem Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), konkrétně komunikuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)). AOCRG funguje jako rozšíření stávajících mechanismů účtování, umožňuje operátorům definovat podrobná účtovací pravidla, která lze dynamicky aplikovat na základě reálného stavu sítě, profilu účastníka nebo charakteristik služby.

Z technického hlediska AOCRG funguje definováním doplňkových účtovacích parametrů, které doplňují primární účtovací pravidla. Když účastník zahájí služební relaci, PCRF vyhodnotí jak standardní účtovací politiky, tak případná platná pravidla AOCRG. Tato pravidla mohou být spuštěna na základě různých podnětů, včetně typu služby, denní doby, zatížení sítě, úrovně předplatitele nebo konkrétního přístupovaného obsahu. Účtovací informace jsou následně sděleny OCS nebo Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)) prostřednictvím standardizovaných rozhraní, což zajišťuje správné generování záznamů pro fakturaci.

Klíčové komponenty zapojené do implementace AOCRG zahrnují PCRF, která ukládá a aplikuje účtovací pravidla; OCS/OFCS, která zpracovávají účtovací data; a Application Function ([AF](/mobilnisite/slovnik/af/)), která může poskytovat služebně specifické informace ovlivňující rozhodnutí AOCRG. Pravidla AOCRG jsou typicky definována pomocí standardizovaných šablon, které specifikují podmínky, akce a účtovací parametry. Tyto šablony umožňují operátorům vytvářet složité účtovací scénáře bez nutnosti rozsáhlého vlastního vývoje.

V rámci síťového ekosystému hraje AOCRG klíčovou roli při umožňování strategií monetizace přesahujících jednoduché objemové nebo časové účtování. Podporuje vrstvené modely služeb, propagační nabídky a cenotvorbu založenou na kvalitě, kde různé úrovně QoS znamenají různé poplatky. Rámec také usnadňuje dodržování regulatorních požadavků tím, že umožňuje transparentní aplikaci dodatečných poplatků s odpovídajícími mechanismy upozornění pro účastníky.

Z pohledu implementace informace AOCRG proudí existujícími rozhraními založenými na protokolu Diameter, primárně využívají rozhraní Gx mezi PCRF a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a rozhraní Gy mezi PGW a OCS. Účtovací pravidla jsou typicky zřizována prostřednictvím manažerských systémů a mohou být dynamicky aktualizována, aby odrážela měnící se obchodní požadavky nebo tržní podmínky.

## K čemu slouží

AOCRG byl vyvinut, aby uspokojil rostoucí potřebu flexibilních, vícerozměrných modelů účtování v mobilních sítích. Před jeho zavedením byly mechanismy účtování 3GPP poměrně rigidní, primárně podporující objemové, časové nebo událostní účtování. Jak se mobilní služby rozvíjely za hranice základního hlasu a dat, potřebovali operátoři sofistikovanější způsoby, jak monetizovat různorodé služby jako streamování obsahu, IoT aplikace a podniková řešení.

Technologie vznikla v reakci na tržní poptávku po personalizovaných nabídkách služeb a konkurenční diferenciaci. Tradiční účtovací systémy měly potíže podporovat složité obchodní modely, jako je zero-rating konkrétních aplikací, vrstvené cenotvorby založené na kvalitě služeb (QoS) nebo kontextově informované propagační nabídky. AOCRG poskytl technický základ pro implementaci těchto pokročilých účtovacích scénářů v rámci standardizovaných architektur 3GPP.

Tím, že umožnil schopnosti doplňkového účtování, AOCRG vyřešil několik klíčových omezení: umožnil operátorům vytvářet služebně specifické ceny bez nutnosti přestavby celé jejich účtovací infrastruktury; podpořil úpravy účtování v reálném čase na základě stavu sítě; a usnadnil transparentní aplikaci dodatečných poplatků. Tato flexibilita se stala stále důležitější, protože operátoři čelili tlaku na monetizaci síťových investic při současné nabídce konkurenceschopných, diferenciovaných služeb na nasycených trzích.

## Klíčové vlastnosti

- Dynamická aplikace účtovacích pravidel na základě podmínek v reálném čase
- Integrace se stávající architekturou PCC prostřednictvím standardizovaných rozhraní
- Podpora služebně specifických a obsahu si vědomých modelů účtování
- Flexibilní spouštěcí mechanismy zahrnující čas, polohu a zatížení sítě
- Kompatibilita s online i offline systémy účtování
- Standardizované šablony pro definování pravidel doplňkového účtování

## Definující specifikace

- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information

---

📖 **Anglický originál a plná specifikace:** [AOCRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/aocrg/)
