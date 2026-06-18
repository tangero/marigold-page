---
slug: "abs"
url: "/mobilnisite/slovnik/abs/"
type: "slovnik"
title: "ABS – Almost Blank Subframe"
date: 2025-01-01
abbr: "ABS"
fullName: "Almost Blank Subframe"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/abs/"
summary: "Podrámec s minimální přenosovou aktivitou, primárně používaný v heterogenních sítích LTE (HetNets) ke snížení rušení. Umožňuje rozšířené koordinování mezičlánkového rušení (eICIC) tím, že chrání ohrož"
---

ABS je podrámec s minimální přenosovou aktivitou, používaný v sítích LTE ke snížení rušení od makročlánků a ochraně uživatelských zařízení v malých buňkách, čímž zlepšuje výkon na okraji buňky a kapacitu sítě.

## Popis

Almost Blank Subframe (ABS, téměř prázdný podrámec) je speciální konfigurace podrámce ve struktuře rámce LTE, ve které vysílající článek (typicky makročlánek) výrazně snižuje svůj vysílací výkon a aktivitu. Zatímco článek stále vysílá nezbytné referenční signály (Cell-Specific Reference Signals – [CRS](/mobilnisite/slovnik/crs/)) a kritické rozhlasové kanály nutné pro provoz starších UE a systémové informace, utlumí nebo výrazně sníží výkon pro datové kanály ([PDSCH](/mobilnisite/slovnik/pdsch/)), řídicí kanály ([PDCCH](/mobilnisite/slovnik/pdcch/), [PHICH](/mobilnisite/slovnik/phich/), [PCFICH](/mobilnisite/slovnik/pcfich/)) a další přenosy. Tím vznikají periodické „klidné“ intervaly ve vzoru vysílání makročlánku.

Primární technický mechanismus spočívá v tom, že makro-eNB nakonfiguruje vzor ABS podrámců a tento vzor signalizuje sousedním malým buňkám (např. pikobuňkám, femtobuňkám) přes rozhraní [X2](/mobilnisite/slovnik/x2/), jak je specifikováno v 3GPP TS 36.423. Malá buňka, která působí jako agresorský článek vůči UE na svém okraji, tyto informace využívá k tomu, aby naplánovala přenos pro své vlastní citlivé UE – tedy ta, která zažívají vysoké rušení od makročlánku – konkrétně během těchto ABS period od makročlánku. Tato koordinace umožňuje malé buňce vysílat k jejím ohroženým UE s mnohem vyšší spolehlivostí a dosažitelnou přenosovou rychlostí během chráněných podrámců.

Z pohledu UE může být UE připojená k malé buňce nakonfigurována s omezeními měření (pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/)), které ji instrukují provádět měření správy radiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), jako je Reference Signal Received Power (RSRP) a Reference Signal Received Quality (RSRQ), pouze během ABS podrámců indikovaných její obslužnou buňkou. To poskytne přesnější obraz o kvalitě signálu malé buňky, protože vyloučí období silného makro rušení. Vzor je charakterizován svou periodicitou a offsetem podrámce, což umožňuje flexibilní sladění mezi rušícími buňkami.

Účinnost ABS je základním kamenem koordinace mezičlánkového rušení v časové oblasti (TD-ICIC) neboli rozšířené ICIC (eICIC) zavedené v LTE-Advanced (Release 10). Řeší tak náročný scénář ko-kanálového nasazení v HetNets, kde nízkovýkonová malá buňka pracuje na stejném kmitočtovém kanále jako překrývající se vysokovýkonový makročlánek. Bez ABS by byla UE poblíž okraje malé buňky vážně rušena makro downlinkem, což by vedlo k nízké propustnosti a potenciálním selháním spojení. Vytvořením chráněných časových prostředků ABS umožňuje robustní provoz malých buněk a efektivní odlehčování provozu z makro vrstvy.

## K čemu slouží

ABS bylo vytvořeno k řešení kritického problému rušení v heterogenních sítích LTE (HetNets), konkrétně ve scénářích ko-kanálového nasazení. Před Release 10 byly techniky koordinace rušení, jako koordinace rušení ve frekvenční oblasti (ICIC) z Release 8, nedostatečné pro závažné downlinkové rušení, kterému čelila uživatelská zařízení (UE) na okraji malé buňky (např. pikobuňky nebo femtobuňky) od vysokovýkonového překrývajícího se makročlánku pracujícího na stejné frekvenci. Toto „makro-to-piko“ rušení omezovalo kapacitu a zisky v pokrytí očekávané od zahušťování sítě, protože efektivní dosah služby malé buňky byl výrazně snížen.

Motivace vycházela z tlaku průmyslu na zahušťování sítí k uspokojení explodující poptávky po mobilních datech. Pouhé přidávání dalších makročlánků bylo neefektivní a nákladné. Malé buňky nabízely řešení, ale jejich nasazení na stejné frekvenci (ko-kanál) kvůli spektrální efektivitě vytvořilo nové výzvy v rušení. Stávající metody řízení výkonu a frekvenčního dělení nedokázaly adekvátně chránit ohrožená UE nacházející se v rozšířeném rozsahu malé buňky (kde je signál malé buňky pouze o něco silnější než signál makročlánku). ABS poskytlo řešení v časové oblasti a vytvořilo čisté oddíly prostředků bez potřeby dodatečného spektra nebo složitého frekvenčního plánování.

Zavedením ABS v Release 10 jako součásti eICIC umožnilo 3GPP operátorům nasazovat nízkovýkonové uzly pod deštníkem pokrytí makročlánku na stejném nosiči, což významně zlepšilo celkovou kapacitu sítě a uživatelský zážitek na okraji buňky. Odstranilo tak omezení předchozích přístupů v prostorové a frekvenční oblasti přidáním časové dimenze do správy rušení, což bylo zvláště účinné pro ochranu řídicích kanálů a umožnění rozšíření dosahu pro malé buňky. Toto byla zásadní technologie pro praktická a vysoce výkonná nasazení HetNets.

## Klíčové vlastnosti

- Vytváří chráněné časové prostředky utlumením přenosů datových a řídicích kanálů makročlánku
- Udržuje vysílání nezbytných Cell-Specific Reference Signals (CRS) pro zpětnou kompatibilitu
- Umožňuje rozšířené koordinování mezičlánkového rušení v časové oblasti (eICIC) pro HetNets
- Usnadňuje rozšíření dosahu malých buněk ochranou ohrožených UE na okraji buňky
- Vyžaduje koordinaci přes rozhraní X2 mezi makro a malobuněčnými eNB
- Podporuje omezení měření na straně UE pro přesné RRM během ABS period

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification

---

📖 **Anglický originál a plná specifikace:** [ABS na 3GPP Explorer](https://3gpp-explorer.com/glossary/abs/)
