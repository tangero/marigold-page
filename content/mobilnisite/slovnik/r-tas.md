---
slug: "r-tas"
url: "/mobilnisite/slovnik/r-tas/"
type: "slovnik"
title: "R-TAS – R2D Timing Acquisition Signal"
date: 2026-01-01
abbr: "R-TAS"
fullName: "R2D Timing Acquisition Signal"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/r-tas/"
summary: "Referenční signál zavedený ve specifikacích 3GPP Release 19 pro komunikaci mezi zařízeními (D2D) a přenosovou (relay) komunikaci. Vzdálené zařízení (R-UE) jej využívá k získání přesného časování a syn"
---

R-TAS je referenční signál zavedený ve verzi 19 (Release 19), který vzdálené zařízení využívá k získání přesného časování a synchronizace od přenosové stanice UE (relay UE) pro spolehlivou komunikaci mezi zařízeními (D2D) a přenosovou komunikaci na postranním spoji (sidelink).

## Popis

Signál pro získání časování na spoji [R2D](/mobilnisite/slovnik/r2d/) (R-TAS) je specifický signál fyzické vrstvy definovaný v rámci architektury 5G New Radio (NR) pro scénáře postranního spoje (sidelink) a přenosové komunikace (relay). Jeho primární funkcí je umožnit přesnou časovou a frekvenční synchronizaci vzdáleného uživatelského zařízení (R-UE) od přenosové stanice UE (služebního uzlu R-UE v kontextu komunikace mezi zařízeními). R-UE, které může být mimo přímý dosah gNB, využívá signál R-TAS vysílaný přenosovou stanicí UE k seřízení svého lokálního oscilátoru a časovacích čítačů. Tato synchronizace je nezbytným předpokladem pro to, aby R-UE mohlo správně přijímat a dekódovat další řídicí a datové kanály na postranním spoji, jako je Physical Sidelink Control Channel ([PSCCH](/mobilnisite/slovnik/pscch/)) a Physical Sidelink Shared Channel ([PSSCH](/mobilnisite/slovnik/pssch/)). Signál je navržen se specifickými sekvencemi a mapováním na zdroje, aby bylo zajištěno robustní zachycení i v náročných rádiových podmínkách.

Z architektonického hlediska je R-TAS generován a vysílán stanicí UE, která funguje jako přenosový nebo synchronizační zdroj, jak je definováno v příslušných specifikacích vrstvy 1. Struktura signálu, včetně generování sekvence, časového průběhu a mapování na zdrojové elementy v rámci zdrojového bloku, je podrobně popsána tak, aby byla zajištěna ortogonalita a minimalizován interference s jinými signály. Příjemce R-UE provádí na předdefinovaných časově-frekvenčních zdrojích detekci založenou na korelaci, aby odhadl časový posun a posun nosné frekvence vůči přenosové stanici UE. Tento odhadnutý posun je následně použit k seřízení přijímače R-UE, což umožňuje koherentní demodulaci následných přenosů.

Role R-TAS je zásadní pro pokročilé případy užití v 5G-Advanced, jako je integrovaný přístup a přenosová síť ([IAB](/mobilnisite/slovnik/iab/)), komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)) a sítě pro veřejnou bezpečnost, kde jsou přímé spoje mezi zařízeními nezbytné. Funguje jako součást bloku synchronizačních signálů postranního spoje ([S-SSB](/mobilnisite/slovnik/s-ssb/)) nebo jako samostatný signál v závislosti na konfiguraci. Tím, že poskytuje časový referenční signál s nízkou režií a vysokou přesností, R-TAS zkracuje dobu počátečního přístupu pro vzdálená zařízení a zvyšuje celkovou spolehlivost a kapacitu více-skokových sítí na postranním spoji. Jeho specifikace zajišťuje interoperabilitu mezi stanicemi UE od různých výrobců ve scénářích přenosové (relay) komunikace.

## K čemu slouží

R-TAS byl vytvořen, aby řešil problémy se synchronizací v decentralizovaných, na zařízeních orientovaných sítích 5G-Advanced. Před jeho zavedením komunikace na postranním spoji (sidelink) primárně spoléhala na synchronizační signály z buněčné sítě (gNB) nebo od vybrané synchronizační referenční stanice UE (SyncRef UE). Ve scénářích, kde je vzdálená stanice UE připojena přes více-skokový přenosový řetězec nebo je v oblasti s částečným pokrytím, však může být příjem stabilní a přesné časové reference přímo od gNB nemožný. Stávající synchronizační mechanismy nebyly optimalizovány pro specifické potřeby získání časování mezi vzdáleným zařízením a jeho bezprostředním přenosovým uzlem, což mohlo vést ke zvýšené latenci přístupu, synchronizačním chybám a neúspěšnému navázání spojení.

Motivace pro R-TAS vychází z potřeby zvýšit výkon a spolehlivost postranního spoje NR, zejména pro služby kritické komunikace a nasazení IoT. Definováním vyhrazeného signálu pro získání časování na spoji [R2D](/mobilnisite/slovnik/r2d/) chtěla skupina 3GPP standardizovat tento proces a zajistit, aby se vzdálená zařízení mohla rychle a přesně synchronizovat se svým přenosovým uzlem. Tím se řeší problém časového driftu ve více-skokových scénářích a podporují se přísné požadavky na nízkou latenci a vysokou spolehlivost v aplikacích, jako je autonomní řízení, průmyslová automatizace a síťově řízené opakovače. Představuje vývoj od síťově orientované synchronizace k flexibilnějšímu paradigmatu synchronizace za pomoci zařízení, které je vyžadováno pro pokročilé přenosové (relay) a [D2D](/mobilnisite/slovnik/d2d/) topologie.

## Klíčové vlastnosti

- Vyhrazený signál fyzické vrstvy pro získání časování mezi R-UE a přenosovou stanicí UE (relay UE)
- Definované generování sekvence pro robustní detekci a nízkou vzájemnou korelaci
- Specifické mapování na zdroje v rámci mřížky zdrojů postranního spoje NR
- Umožňuje rychlou a přesnou časovou/frekvenční synchronizaci pro postranní spoj (sidelink)
- Podporuje provoz jak v oblasti s pokrytím, tak mimo ni
- Tvoří základ pro spolehlivou demodulaci řídicích a datových kanálů postranního spoje

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.291** (Rel-19) — Ambient IoT Physical Layer Specification
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [R-TAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-tas/)
