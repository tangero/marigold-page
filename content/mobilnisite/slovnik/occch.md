---
slug: "occch"
url: "/mobilnisite/slovnik/occch/"
type: "slovnik"
title: "OCCCH – ODMA Common Control Channel"
date: 2025-01-01
abbr: "OCCCH"
fullName: "ODMA Common Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/occch/"
summary: "Logický kanál v protokolu ODMA (Opportunity Driven Multiple Access), alternativním konceptu přenosu zkoumaném v raném UMTS. Byl používán pro vysílání systémových informací a přenos společných řídicích"
---

OCCCH je ODMA Common Control Channel (společný řídicí kanál ODMA), logický kanál používaný v raném konceptu přenosu UMTS pro vysílání systémových informací a přenos společných řídicích signalizací mezi přenosovými mobilními stanicemi.

## Popis

[ODMA](/mobilnisite/slovnik/odma/) Common Control Channel (OCCCH) byl logický kanál definovaný v rámci protokolu Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/) (ODMA), což byla výzkumná a vývojová funkce v raných standardech UMTS (Universal Mobile Telecommunications System). ODMA byla koncipována jako decentralizované rozšíření UMTS ve stylu mobilní ad-hoc sítě (MANET), kde uživatelské zařízení (UE) mohlo fungovat jako přenosový uzel pro rozšíření pokrytí a kapacity bez nutnosti pevného infrastrukturního uzlu pro každý skok. OCCCH fungoval jako vysílací a společný signalizační kanál v této ad-hoc přenosové síti. Pracující na vyhrazeném zdroji, jeho primární rolí bylo přenášet systémové informace nezbytné pro to, aby UE mohla objevit síť ODMA, identifikovat sousední uzly schopné přenosu a získat parametry potřebné k navázání a udržování přenosových spojení. To zahrnovalo informace jako identifikátory přenosových uzlů, dostupné zdroje a směrovací metriky. Kanál byl navržen tak, aby k němu měla přístup všechna UE v režimu ODMA v dosahu příjmu. V protokolovém zásobníku byl OCCCH službou poskytovanou vrstvami Radio Link Control (RLC) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) specifickými pro ODMA vyšším vrstvám pro správu sítě a operace směrovacích protokolů (např. pro objevování a údržbu tras). Přenos a příjem zpráv OCCCH se řídil procedurami specifickými pro ODMA, které zahrnovaly mechanismy jako naslouchej-před-mluvením a další mechanismy ad-hoc sítí, nikoli centralizované plánování tradičního UMTS. Kanál byl součástí sady logických kanálů ODMA, která zahrnovala také vyhrazené kanály pro přenos dat a řízení ([ODTCH](/mobilnisite/slovnik/odtch/), [ODCCH](/mobilnisite/slovnik/odcch/)). Celý koncept ODMA, včetně OCCCH, však zůstal předmětem studií a nikdy nebyl implementován v komerčních sítích, protože průmysl se vydal alternativními cestami pro rozšíření pokrytí, jako jsou opakovače a později integrovaný přístup a přenos (IAB) v 5G.

## K čemu slouží

Účelem OCCCH bylo umožnit samoorganizaci a přenos řídicí signalizace decentralizované, více-skokové mobilní sítě, jak ji koncipoval koncept [ODMA](/mobilnisite/slovnik/odma/). Cílem bylo řešit problémy s dírami v pokrytí, kapacitou v hustě obydlených oblastech a náklady na infrastrukturu tím, že umožňoval přímý přenos mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)). V tradiční mobilní síti veškerá komunikace prochází základnovou stanicí; ODMA navrhovala síť typu mesh, kde se UE mohlo komunikovat se sítí prostřednictvím jiného UE fungujícího jako přenosový uzel. OCCCH byl základním řídicím kanálem pro tuto síť mesh, který řešil klíčový problém objevování sítě a počáteční asociace v prostředí bez infrastruktury nebo s řídkou infrastrukturou. Poskytoval nezbytný mechanizmus majáčkování a vysílání, aby přenosové uzly mohly oznamovat svou přítomnost a schopnosti a aby hledající UE mohla nalézt potenciální cesty k síti. Historickým motivem pro ODMA a OCCCH koncem 90. a počátkem 2000. let (R99) bylo prozkoumat alternativní architektury rádiového přístupu, které by mohly snížit náklady na nasazení a zlepšit výkon v náročných rádiových podmínkách. Řešila omezení čistě celulárních topologií, zejména pro pokrytí na okrajích buněk nebo v scénářích rychlého nasazení. Složitost správy interference, směrování, zabezpečení a účtování v takovém decentralizovaném systému spolu s úspěšným vývojem konvenční mobilní technologie však vedly k odložení ODMA, což učinilo z OCCCH historický artefakt standardizace 3GPP.

## Klíčové vlastnosti

- Logický vysílací kanál pro ad-hoc přenosovou síť ODMA.
- Přenášel systémové informace pro objevování sítě ODMA a identifikaci přenosových uzlů.
- Umožňoval počáteční přístup a objevování sousedů pro UE pracující v režimu ODMA.
- Součást zásobníku protokolů specifických pro ODMA nad fyzickou vrstvou.
- Podporoval decentralizované, neplánované přístupové mechanismy typické pro ad-hoc sítě.
- Definován jako součást sady kanálů (spolu s ODTCH, ODCCH) pro kompletní přenosový protokol.

## Související pojmy

- [ODMA – Opportunity Driven Multiple Access](/mobilnisite/slovnik/odma/)
- [D2D – Device-to-Device](/mobilnisite/slovnik/d2d/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [OCCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/occch/)
