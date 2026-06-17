---
slug: "msch"
url: "/mobilnisite/slovnik/msch/"
type: "slovnik"
title: "MSCH – MBMS point-to-multipoint Scheduling Channel"
date: 2025-01-01
abbr: "MSCH"
fullName: "MBMS point-to-multipoint Scheduling Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/msch/"
summary: "Logický kanál v UMTS používaný k přenosu plánovacích informací pro vysílání služby Multimedia Broadcast Multicast Service (MBMS). Informuje uživatelská zařízení (UE) o tom, kdy a kde přijímat MBMS dat"
---

MSCH je logický kanál v UMTS, který přenáší plánovací informace k uživatelskému zařízení (UE), a sděluje mu, kdy a kde přijímat MBMS data na přenosovém kanálu MTCH pro efektivní příjem.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) point-to-multipoint Scheduling Channel (MSCH) je downlink logický kanál definovaný v architektuře rádiového rozhraní Universal Mobile Telecommunications System (UMTS) – UTRAN pro podporu služby Multimedia Broadcast Multicast Service (MBMS). Funguje jako klíčová součást MBMS řídicí roviny, konkrétně navržený pro přenos dynamických plánovacích informací pro jeden nebo více MBMS Traffic Channels ([MTCH](/mobilnisite/slovnik/mtch/)). MSCH je mapován na Secondary Common Control Physical Channel (S-CCPCH) pro přenos vzduchem. Jeho primárním obsahem je plánovací zpráva, která poskytuje seznam MTCH a jim odpovídající parametry příjmu pro dané plánovací období.

Princip fungování MSCH je klíčový pro efektivitu MBMS. Radio Network Controller (RNC) sítě určuje plán vysílání datových burstů MBMS na MTCH. Tento plán, který zahrnuje čas začátku, dobu trvání a relevantní transportní formát pro každý MTCH, je sestaven do plánovací zprávy a odeslán na MSCH. Uživatelská zařízení (UE) zajímající se o MBMS služby musí nejprve monitorovat MBMS Control Channel ([MCCH](/mobilnisite/slovnik/mcch/)), aby se dozvěděla konfiguraci MSCH (např. jeho spreading kód a časování). Po nakonfigurování UE periodicky čte MSCH. Po přijetí plánovacích informací UE přesně ví, kdy aktivovat svůj přijímač pro dekódování MTCH požadované služby, což mu umožňuje vypnout přijímač během nečinných period a významně tak šetřit životnost baterie – klíčová vlastnost známá jako discontinuous reception ([DRX](/mobilnisite/slovnik/drx/)) pro MBMS.

Architektonicky se MSCH nachází v protokolovém stacku vrstvy 2 UTRAN. Je definován ve specifikacích vrstvy [MAC](/mobilnisite/slovnik/mac/) (TS 25.321). Plánovací informace na MSCH jsou typicky opakovány s periodicitou, která vyvažuje úsporu energie UE a aktuálnost aktualizací plánu. MSCH je asociován s konkrétní MBMS point-to-multipoint Service Area. Jeho návrh je optimalizován pro charakteristiku one-to-many MBMS; jediný přenos MSCH může naplánovat více MTCH, čímž minimalizuje režii řídicích kanálů. Tento efektivní plánovací mechanismus je tím, co umožňuje UTRAN podporovat rozsáhlé broadcastové služby, jako je mobilní TV, kde tisíce UE potřebují současně přijímat stejný obsah bez individuální signalizace se sítí, čímž se šetří cenné rádiové zdroje i energie baterie UE.

## K čemu slouží

MSCH byl zaveden, aby řešil základní výzvy efektivního doručování broadcastových a multicastových služeb přes celulární síť navrženou primárně pro point-to-point komunikaci. Před [MBMS](/mobilnisite/slovnik/mbms/) by doručení stejného obsahu mnoha uživatelům vyžadovalo zřízení individuálních vyhrazených kanálů pro každého uživatele, což je z hlediska spotřeby rádiových zdrojů vysoce neefektivní. MBMS zavedlo point-to-multipoint sdílené kanály ([MTCH](/mobilnisite/slovnik/mtch/)), ale byl potřebný mechanismus pro koordinaci, kdy budou data přenášena, aby UE nemusela kanál nepřetržitě monitorovat, což by rychle vybilo jejich baterie.

Účelem MSCH je poskytnout tuto přesnou koordinaci. Řeší kritický problém spotřeby energie UE ve scénářích broadcastu, který je vždy aktivní. Dodáním centralizovaného, předvídatelného plánu umožňuje MSCH UE přejít do režimu nízké spotřeby (sleep mode) a probouzet se pouze pro příjem dat v předem definovaných časech. To byla klíčová technologie umožňující komerční životaschopnost MBMS služeb, jako je mobilní TV, na zařízeních napájených baterií. Dále MSCH umožňuje statistické multiplexování a flexibilní přidělování zdrojů v časové doméně, protože síť může dynamicky upravovat vysílací plán různých MBMS služeb na základě poptávky a dostupné kapacity. Jeho zavedení v UMTS Rel-6 bylo základním kamenem pro sadu funkcí MBMS, neboť poskytlo potřebný mechanismus řídicí roviny, který učinil vysílání služeb s vysokou datovou rychlostí praktickým a uživatelsky přívětivým.

## Klíčové vlastnosti

- Logický kanál přenášející dynamické plánovací informace pro MBMS Traffic Channels (MTCH).
- Mapován na Secondary Common Control Physical Channel (S-CCPCH) pro přenos v UTRAN.
- Umožňuje UE discontinuous reception (DRX), což vede k významným úsporám energie baterie během příjmu MBMS.
- Plánovací zprávy udávají čas začátku, dobu trvání a transportní formát pro naplánované MTCH.
- Konfigurován a oznamován prostřednictvím MBMS Control Channel (MCCH) jako součást získání MBMS služby.
- Optimalizován pro přenos one-to-many, kde jediný MSCH může naplánovat více MTCH.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)

## Definující specifikace

- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture

---

📖 **Anglický originál a plná specifikace:** [MSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/msch/)
