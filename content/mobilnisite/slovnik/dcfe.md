---
slug: "dcfe"
url: "/mobilnisite/slovnik/dcfe/"
type: "slovnik"
title: "DCFE – Dedicated Control Functional Entity"
date: 2025-01-01
abbr: "DCFE"
fullName: "Dedicated Control Functional Entity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dcfe/"
summary: "DCFE je funkční entita v řadiči rádiové sítě UMTS (RNC) odpovědná za správu vyhrazeného řídicího signalizačního toku pro konkrétní uživatelské zařízení (UE). Zajišťuje zřizování, údržbu a uvolňování s"
---

DCFE je funkční entita v řadiči rádiové sítě UMTS (Radio Network Controller), která spravuje vyhrazený řídicí signalizační tok pro konkrétní uživatelské zařízení (UE) a zajišťuje zřizování, údržbu a uvolňování spojení na vyhrazených kanálech.

## Popis

Dedicated Control Functional Entity (DCFE) je základní funkční komponenta uvnitř řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v pozemní rádiové přístupové síti UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), jak je definováno ve specifikacích 3GPP. Funguje jako součást řídicí roviny, konkrétně ve vrstvě protokolu řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), za účelem správy vyhrazeného řídicího signalizačního toku pro jednotlivá uživatelská zařízení (UE). Instance DCFE se vytváří pro každé UE s aktivním vyhrazeným spojením, což znamená, že je odpovědná za celý životní cyklus vyhrazeného řídicího signalizačního toku tohoto UE od zřízení přes údržbu až po uvolnění. Tato entita komunikuje s dalšími funkčními entitami RNC, jako jsou funkce řízení rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) a entita pro společný řídicí tok (CCFE), za účelem koordinace prostředků a zajištění plynulého provozu.

Z architektonického hlediska sídlí DCFE v obsluhujícím RNC ([SRNC](/mobilnisite/slovnik/srnc/)) pro dané UE, kde zpracovává všechny procedury vyhrazeného řídicího toku. Zpracovává zprávy RRC vyměňované mezi RNC a UE, včetně těch pro zřizování spojení, rekonfiguraci, předávání spojení a uvolnění. DCFE spravuje vyhrazený řídicí kanál ([DCCH](/mobilnisite/slovnik/dcch/)), který se používá pro signalizaci specifickou pro dané UE, a zajišťuje jeho spolehlivé doručování pomocí mechanismů jako potvrzování a retransmise. Dále komunikuje s Node B přes rozhraní Iub za účelem řízení rádiového spoje a s jádrem sítě přes rozhraní Iu pro koordinaci se službami vyšších vrstev.

Klíčové součásti DCFE zahrnují stavové automaty pro stavy RRC spojení (např. CELL_[DCH](/mobilnisite/slovnik/dch/), CELL_[FACH](/mobilnisite/slovnik/fach/)), časovače pro časové limity procedur a vyrovnávací paměti pro signalizační zprávy. Provádí kritické funkce, jako je řízení rádiových přenosových kanálů, správa mobility pro vyhrazená spojení a koordinace řízení výkonu. DCFE funguje tak, že interpretuje datové jednotky protokolu RRC (PDU), provádí odpovídající procedury a aktualizuje kontext UE. Například během předávání spojení DCFE koordinuje prostředky cílové buňky a spouští potřebnou signalizaci pro plynulý přechod vyhrazeného spojení UE.

V síti hraje DCFE zásadní roli při udržování kvality služeb (QoS) pro vyhrazené služby, jako jsou hlasové hovory nebo streamování videa. Zajišťuje efektivní přidělování vyhrazených prostředků, monitoruje kvalitu spoje a iniciuje obnovovací akce v případě selhání. Správou signalizace specifické pro konkrétní UE odlehčuje DCFE úlohy společného řídicího toku od CCFE, čímž optimalizuje výkon a škálovatelnost RNC. Její činnost je základním předpokladem spolehlivosti a rychlé odezvy sítí UMTS a přímo ovlivňuje uživatelský zážitek během vyhrazených relací.

## K čemu slouží

DCFE byla zavedena ve verzi 3GPP Release 99, aby řešila potřebu efektivní a spolehlivé správy vyhrazeného řídicího signalizačního toku v sítích UMTS. Před UMTS používaly systémy 2G, jako je GSM, jednodušší řídicí mechanismy, které byly méně přizpůsobivé dynamickým požadavkům na prostředky u paketově přepínaných služeb. S příchodem 3G, které podporovalo vyšší datové rychlosti a rozmanité služby (např. videohovory, mobilní internet), vzrostl požadavek na vyhrazenou řídicí entitu schopnou zpracovávat komplexní signalizaci pro každé UE bez přetížení prostředků společného řídicího toku. DCFE tento problém vyřešila tím, že poskytla škálovatelnou architekturu, kde je vyhrazené spojení každého UE spravováno nezávisle, což zajišťuje včasné a přesné řídicí procedury.

Historická omezení předchozích přístupů zahrnovala centralizované řízení, které se mohlo stát úzkým hrdlem při vysokém provozním zatížení, a nedostatečnou podporu stavové signalizace specifické pro UE. Zavedení DCFE bylo motivováno potřebou oddělit funkce vyhrazeného a společného řídicího toku, což umožnilo RNC současně obsluhovat více uživatelských zařízení s optimalizovaným využitím prostředků. Umožňuje přesné řízení rádiových přenosových kanálů, usnadňuje pokročilé funkce mobility, jako je měkké předávání spojení, a podporuje diferenciaci kvality služeb pro vyhrazené kanály. Toto oddělení také zvýšilo spolehlivost sítě tím, že izolovalo poruchy na kontexty jednotlivých UE namísto ovlivnění celé řídicí roviny.

Vytvoření DCFE bylo hnací silou cíle 3GPP zvýšit efektivitu a kvalitu služeb v rádiové přístupové síti. Řeší problémy, jako je zahlcení signalizace, zpožděné zřizování spojení a špatný výkon při předávání spojení ve vyhrazených scénářích. Poskytnutím vyhrazené funkční entity zajišťuje DCFE, že kritická řídicí signalizace pro aktivní relace je zpracovávána s vysokou prioritou a minimální latencí, což je nezbytné pro služby v reálném čase. Její návrh odráží vývoj od dominance okruhového přepojování ke smíšeným provozním prostředím a pokládá základy pro pozdější vylepšení řídicí roviny v sítích 4G a 5G.

## Klíčové vlastnosti

- Spravuje vyhrazený řídicí signalizační tok pro každé uživatelské zařízení (UE) v RNC
- Zajišťuje procedury zřizování, údržby a uvolňování spojení RRC
- Koordinuje se s Node B přes rozhraní Iub za účelem řízení rádiového spoje
- Komunikuje s jádrem sítě přes rozhraní Iu pro koordinaci služeb
- Podporuje stavové automaty pro stavy RRC, jako jsou CELL_DCH a CELL_FACH
- Zajišťuje spolehlivé doručování signalizace přes vyhrazený řídicí kanál (DCCH)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [DCCH – Dedicated Control Channel](/mobilnisite/slovnik/dcch/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [DCFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcfe/)
