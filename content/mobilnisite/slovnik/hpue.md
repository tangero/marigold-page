---
slug: "hpue"
url: "/mobilnisite/slovnik/hpue/"
type: "slovnik"
title: "HPUE – High Power User Equipment"
date: 2025-01-01
abbr: "HPUE"
fullName: "High Power User Equipment"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hpue/"
summary: "High Power User Equipment (HPUE) označuje uživatelská zařízení se zvýšeným maximálním vyzařovaným výkonem, konkrétně pro pásmo LTE Band 14 a pásma 5G NR využívaná sítěmi veřejné bezpečnosti. Rozšiřuje"
---

HPUE je typ uživatelského zařízení (User Equipment) se zvýšeným maximálním vyzařovaným výkonem pro specifické pásma LTE a 5G, který rozšiřuje pokrytí v uplinku a zlepšuje spolehlivost pro veřejnou bezpečnost a komunikace s klíčovým významem (mission-critical).

## Popis

High Power User Equipment (HPUE) je schopnost definovaná ve specifikacích 3GPP, která určitým třídám uživatelských zařízení (UE) umožňuje vysílat s vyšším maximálním výkonem než standardní UE. Hlavní uplatnění našla v pásmu Band 14 (700 MHz) pro sítě veřejné bezpečnosti založené na LTE, zejména v Severní Americe pod správou FirstNet. Standardní zařízení výkonové třídy 3 (Power Class 3) mají maximální výstupní výkon 23 dBm, zatímco HPUE jsou definována pro výkonovou třídu 1 (Power Class 1), která umožňuje maximum 31 dBm – což představuje významný nárůst o 8 dB a efektivně více než zdvojnásobuje efektivní izotropně vyzářený výkon.

Technicky dosažení provozu HPUE zahrnuje vylepšení v konstrukci výkonového zesilovače UE, tepelném managementu a kapacitě baterie, aby zvládly vyšší odběr proudu. Na straně sítě musí být eNodeB (pro LTE) a gNB (pro NR) schopny identifikovat a podporovat HPUE, včetně správných mechanismů řízení výkonu pro správu rušení v uplinku. Specifikace 3GPP definují požadavky, testovací postupy a signalizaci (např. prostřednictvím indikace schopností UE) pro zajištění interoperability. UE signalizuje svou schopnost HPUE síti, která pak může odpovídajícím způsobem upravit parametry plánování a řízení výkonu.

Úloha HPUE v síti spočívá v podstatném zlepšení pokrytí v uplinku, zejména na okraji buňky nebo v místech se špatným pronikáním signálu, jako jsou vnitřní prostory budov nebo venkovské oblasti. To je zásadní pro komunikace veřejné bezpečnosti, kde dostupnost sítě nesmí být ohrožena. Vylepšený uplink přímo zlepšuje rozpočet spoje (link budget), čímž zvyšuje maximální přípustný útlum na dráze šíření. To může snížit počet potřebných lokalit pro pokrytí, poskytnout spolehlivější uplink pro přenos dat a videa z terénu a zajistit, že záchranný personál udrží konektivitu i v nepříznivých podmínkách.

## K čemu slouží

HPUE bylo vyvinuto k řešení kritického omezení komerčních LTE sítí při jejich adaptaci pro potřeby veřejné bezpečnosti: nedostatečného pokrytí v uplinku ze zařízení k základnové stanici. V nouzových scénářích záchranné složky často operují na hranici pokrytí, uvnitř staveb nebo v odlehlých oblastech. Standardní limit výkonu UE (23 dBm) mohl vést k neúspěšným přenosům v uplinku a přerušení komunikace. Komunita veřejné bezpečnosti požadovala robustnější spojení, což vedlo k specifikaci zařízení s vyšším výkonem.

Tuto iniciativu poháněly požadavky subjektů jako First Responder Network Authority (FirstNet) ve Spojených státech. Spektrum pásma 700 MHz Band 14 bylo přiděleno speciálně pro veřejnou bezpečnost a HPUE se stalo klíčovým rozlišovacím prvkem pro vytvoření dedikované, nadstandardní sítě pro záchranné složky ve srovnání s komerčními službami. Vyřešilo problém asymetrických rozpočtů spoje, kde je pokrytí v downlinku od výkonné základnové stanice typicky mnohem lepší než v uplinku. Zvýšením vysílacího výkonu UE HPUE tuto asymetrii vyrovnává a rozšiřuje efektivní oblast spolehlivé obousměrné komunikace, což je pro záchranné mise nezbytnou podmínkou.

## Klíčové vlastnosti

- Definováno pro výkonovou třídu 1 (Power Class 1) s maximálním výstupním výkonem 31 dBm (oproti 23 dBm pro třídu 3)
- Primárně specifikováno pro LTE Band 14 a relevantní pásma NR pro veřejnou bezpečnost
- Vyžaduje signalizaci schopností UE k informování sítě
- Významně zlepšuje pokrytí v uplinku a výkon na okraji buňky
- Zahrnuje specifické RF a výkonnostní testy definované ve specifikacích 3GPP
- Kritické pro spolehlivost komunikací s klíčovým významem (mission-critical)

## Definující specifikace

- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TS 36.837** (Rel-11) — TR on Band 14 High Power UE for Public Safety
- **TR 37.829** (Rel-18) — Technical Report
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- **TS 38.795** (Rel-19) — High Power UE Technical Report for NR FR1
- **TS 38.796** (Rel-19) — Rel-19 High Power UE for NR FR1

---

📖 **Anglický originál a plná specifikace:** [HPUE na 3GPP Explorer](https://3gpp-explorer.com/glossary/hpue/)
