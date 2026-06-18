---
slug: "mc-hsupa"
url: "/mobilnisite/slovnik/mc-hsupa/"
type: "slovnik"
title: "MC-HSUPA – Multi-Carrier High Speed Uplink Packet Access"
date: 2025-01-01
abbr: "MC-HSUPA"
fullName: "Multi-Carrier High Speed Uplink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mc-hsupa/"
summary: "Vylepšení HSPA podle 3GPP, které umožňuje uživatelskému zařízení (UE) vysílat data současně na více nosných frekvencích v uplinku. Agreguje kapacitu dvou 5MHz WCDMA nosných v uplinku, čímž zvyšuje špi"
---

MC-HSUPA je vylepšení HSPA podle 3GPP, které umožňuje uživatelskému zařízení (UE) vysílat data současně na více nosných v uplinku, čímž zvyšuje špičkové přenosové rychlosti a kapacitu uplinku v sítích UMTS/HSPA.

## Popis

Multi-Carrier [HSUPA](/mobilnisite/slovnik/hsupa/) (MC-HSUPA) je protějšek [MC-HSDPA](/mobilnisite/slovnik/mc-hsdpa/) pro uplink, standardizovaný od 3GPP Release 10 jako součást vývoje [HSPA](/mobilnisite/slovnik/hspa/). Umožňuje jednomu uživatelskému zařízení (UE) vysílat současně na více [WCDMA](/mobilnisite/slovnik/wcdma/) nosných v uplinku, čímž agreguje šířku pásma uplinku a zvyšuje špičkovou přenosovou rychlost v uplinku. Podobně jako u downlinku jedna nosná typicky slouží jako Uplink Anchor Carrier (kotvící nosná pro uplink), která zajišťuje nezbytné řídicí signalizaci a vyhrazené kanály, zatímco další Uplink Secondary Carriers (sekundární nosné pro uplink) se používají pro vylepšený přenos dat v uplinku prostřednictvím [E-DCH](/mobilnisite/slovnik/e-dch/) (Enhanced Dedicated Channel).

Provozně, pro UE nakonfigurované s MC-HSUPA, síť přiřadí primární nosnou pro uplink, která nese [DPCCH](/mobilnisite/slovnik/dpcch/) (Dedicated Physical Control Channel) pro řízení výkonu a pilotní signály, stejně jako případný přidružený [DPDCH](/mobilnisite/slovnik/dpdch/) (Dedicated Physical Data Channel). Sekundární nosná(e) pro uplink jsou konfigurovány s vlastní sadou [E-DPDCH](/mobilnisite/slovnik/e-dpdch/) (Enhanced Dedicated Physical Data Channels) pro vysokorychlostní data. UE musí spravovat svůj vysílací výkon napříč více nosnými při dodržení maximálního výkonového omezení zařízení. Plánovací povolení (scheduling grants), která řídí rychlost vysílání UE v uplinku, se spravují pro každou nosnou zvlášť. UE odesílá plánovací informace (SI) a Happy Bits samostatně pro každý aktivní E-DCH nosnou, což umožňuje plánovači v Node B řídit zdroje uplinku na každé z nich nezávisle.

Implementace vyžaduje vylepšení jak v UE, tak v Node B. UE musí podporovat více vysílacích řetězců a výkonové zesilovače schopné simultánního vysílání na různých frekvencích, což má dopady na složitost zařízení a spotřebu baterie. Node B musí být schopen přijímat a demodulovat kombinovaný signál z více nosných uplinku. Klíčové technické specifikace pro MC-HSUPA, včetně podporovaných kombinací nosných a kategorií UE, jsou podrobně popsány v 3GPP TS 25.102 a 25.319. Například Dual-Cell HSUPA (DC-HSUPA) v Release 10 agreguje dvě sousední nosné v uplinku, což může potenciálně zdvojnásobit špičkovou rychlost uplinku z maximální hodnoty pro jednoduchou nosnou 11,5 Mbps na 23 Mbps, v závislosti na kategorii UE a konfiguraci sítě.

MC-HSUPA hraje klíčovou roli při vytváření symetrického vysokorychlostního zážitku v sítích HSPA. Zatímco MC-HSDPA řešilo úzké hrdlo v downlinku, mnoho nových aplikací (jako nahrávání videa, synchronizace s cloudem a komunikace v reálném čase) vytvořilo poptávku po vyšší kapacitě uplinku. Díky umožnění agregace nosných v uplinku MC-HSUPA zlepšuje celkovou vyváženost rádiového spoje, snižuje latenci v uplinku pro velké datové dávky a zvyšuje kapacitu uplinku buňky. Umožňuje operátorům lépe využít jejich spárované spektrální zdroje a poskytuje úplnější širokopásmový zážitek v sítích HSPA, čímž doplňuje možnosti downlinku a prodlužuje relevanci této technologie v éře rostoucího množství uživateli generovaného obsahu a interaktivních služeb.

## K čemu slouží

MC-HSUPA byl vyvinut k řešení rostoucí asymetrie mezi možnostmi downlinku a uplinku ve vyvinutých sítích HSPA. Předchozí zaměření bylo na zvyšování rychlostí downlinku pomocí funkcí jako MC-HSDPA a MIMO, což ponechalo uplink jako potenciální úzké hrdlo. Vzestup uživateli generovaného obsahu, videohovorů a cloudových aplikací vytvořil jasnou potřebu vyšší propustnosti a nižší latence v uplinku. MC-HSUPA to vyřešil aplikací principu agregace více nosných na uplink, což přímo zvýšilo špičkovou přenosovou rychlost a spektrální zdroje dostupné pro přenos z UE.

Řešil omezení jednoduché nosné HSUPA, která byla limitována šířkou pásma 5 MHz a omezeným vysílacím výkonem UE. Agregací nosných mohlo UE rozložit svůj přenos na širší šířku pásma a dosáhnout vyšších rychlostí bez nutnosti zvyšovat špičkovou spektrální hustotu výkonu. To bylo efektivnější a technicky proveditelnější než prosté rozšíření jedné nosné. Tato technologie také zlepšila kapacitu buňky v uplinku tím, že umožnila plánovači přidělovat zdroje napříč více nosnými a obsluhovat více uživatelů současně s vysokými přenosovými rychlostmi v uplinku.

Vytvoření MC-HSUPA bylo motivováno snahou poskytnout kompletní a vysoce výkonný vývoj HSPA. Zajistilo, že HSPA+ může poskytovat vyvážený širokopásmový zážitek, což jej učinilo životaschopnější alternativou nebo doplňkem k LTE, zejména na trzích, kde bylo nasazení LTE pomalejší nebo kde bylo pokrytí HSPA rozsáhlejší. Standardizací v Release 10 spolu s vylepšeními MC-HSDPA poskytlo 3GPP operátorům jasnou cestu pro symetrický upgrade jejich sítí, což maximalizovalo užitek z jejich stávajících investic do spektra a infrastruktury UMTS.

## Klíčové vlastnosti

- Agreguje více 5MHz WCDMA nosných v uplinku pro jedno UE
- Používá Uplink Anchor Carrier pro řízení a Secondary Carriers pro data přes E-DCH
- Zvyšuje špičkové přenosové rychlosti v uplinku úměrně počtu nosných
- Vyžaduje UE s podporou více vysílacích řetězců a výkonových zesilovačů
- Obsahuje plánování uplinku pro každou nosnou zvlášť prostřednictvím povolení na E-AGCH a E-RGCH
- Zlepšuje kapacitu buňky v uplinku a snižuje latenci pro datové dávky

## Související pojmy

- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [DC-HSUPA – Dual Cell High Speed Uplink Packet Access](/mobilnisite/slovnik/dc-hsupa/)

## Definující specifikace

- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD

---

📖 **Anglický originál a plná specifikace:** [MC-HSUPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mc-hsupa/)
