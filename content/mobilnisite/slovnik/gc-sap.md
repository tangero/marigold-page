---
slug: "gc-sap"
url: "/mobilnisite/slovnik/gc-sap/"
type: "slovnik"
title: "GC-SAP – General Control Service Access Point"
date: 2025-01-01
abbr: "GC-SAP"
fullName: "General Control Service Access Point"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gc-sap/"
summary: "GC-SAP je servisní přístupový bod definovaný ve vrstvě protokolu řízení rádiových zdrojů (RRC). Poskytuje rozhraní pro přenos obecných řídicích informací mezi RRC a vyššími vrstvami, konkrétně pro slu"
---

GC-SAP je servisní přístupový bod ve vrstvě protokolu RRC, který poskytuje rozhraní pro přenos obecných řídicích informací, jako jsou systémové informace a zprávy buněčného vysílání, do vyšších vrstev.

## Popis

General Control Service Access Point (GC-SAP) je klíčovou součástí architektury protokolu řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) v UMTS, standardizovanou v 3GPP TS 25.331. Funguje jako logické rozhraní neboli servisní přístupový bod mezi vrstvou RRC a vyššími vrstvami, především pro nededicovaný přenos informací typu vysílání. GC-SAP je jedním z několika SAP definovaných pro vrstvu RRC, z nichž každý slouží odlišnému účelu, například Notification (Nt-SAP) pro příjem volání nebo Dedicated Control ([DC-SAP](/mobilnisite/slovnik/dc-sap/)) pro vyhrazené signalizační spojení.

Architektonicky se GC-SAP nachází v řídicí rovině uživatelského zařízení (UE) a UTRAN (UMTS Terrestrial Radio Access Network). Jeho primární funkcí je poskytovat standardizovaný mechanismus, pomocí kterého vrstva RRC přijímá a zpracovává obecné řídicí zprávy od základnové sítě nebo doručuje vysílané informace přijaté přes rozhraní vzduch příslušným entitám vyšších vrstev. Tento SAP je pro příjem vysílaných informací jednosměrný, což znamená, že jej UE používá k přijímání bloků systémových informací (SIB) a zpráv služby buněčného vysílání ([CBS](/mobilnisite/slovnik/cbs/)), které jsou přenášeny na společných kanálech, jako je Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) nebo Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)).

Provoz GC-SAP zahrnuje příjem RRC zpráv typu 'System Information' nebo 'Cell Broadcast Information' od sítě vrstvou RRC. Po přijetí a zpracování vrstva RRC použije GC-SAP k doručení relevantních informačních prvků do vyšších vrstev, jako je Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) nebo specifické aplikace, například entita buněčného vysílání. Tím se oddělují rádiově specifické procedury RRC od zpracování vysílaných dat na aplikační vrstvě. Mezi klíčové komponenty interagující s GC-SAP patří entita protokolu RRC, logický kanál BCCH a servisní přístupové body vyšších vrstev pro služby vysílání.

Jeho role v síti je zásadní pro počáteční výběr buňky, převýběr buňky a poskytování základních síťových informací a systémů veřejného varování uživatelům. Poskytnutím čistého, standardizovaného rozhraní GC-SAP zajišťuje konzistentní zpracování vysílaných informací napříč různými implementacemi UE a konfiguracemi sítě, čímž přispívá k spolehlivosti a interoperabilitě systémů UMTS. Tvoří část základního rámce řídicí signalizace, který umožňuje efektivní využití rádiových zdrojů pro šíření společných informací.

## K čemu slouží

GC-SAP byl zaveden, aby řešil potřebu strukturované a efektivní metody pro zpracování vysílaných a obecných řídicích informací v sítích UMTS. Před 3GPP Release 4, které formalizovalo specifikaci protokolu [RRC](/mobilnisite/slovnik/rrc/) v TS 25.331, vyžadovalo zpracování systémových informací a vysílaných zpráv jasnou architektonickou separaci mezi rádiově specifickou řídicí vrstvou a službami vyšších vrstev, které tyto informace spotřebovávají. Vytvoření GC-SAP tuto separaci poskytlo.

Jeho hlavním účelem je řešit problém doručování nededicovaných, síťově iniciovaných řídicích informací všem UE v buňce nebo specifické oblasti bez nutnosti navazovat individuální signalizační spojení. To je klíčové pro efektivitu sítě a úsporu energie UE, protože informace jako parametry buňky, seznamy sousedních buněk a nouzová varování musí být kdykoli dostupné jakémukoli UE. GC-SAP standardizuje servisní primitiva a tok informací pro tento typ dat, čímž zajišťuje, že UE od různých výrobců mohou vysílané zprávy správně interpretovat a podle nich jednat.

Historicky, jak se mobilní sítě vyvíjely z GSM ke složitějšímu UMTS s jeho dedikovanou vrstvou RRC, existovala motivace definovat robustnější a flexibilnější řídicí rovinu. GC-SAP byl spolu s dalšími SAP součástí tohoto úsilí o vytvoření modulární protokolové architektury. Řešil omezení ad-hoc mechanismů doručování informací tím, že poskytl dobře definované rozhraní, což zjednodušilo návrh softwaru UE, zlepšilo testování a certifikaci a umožnilo spolehlivé zavedení nových vysílacích služeb, jako je služba buněčného vysílání pro systémy veřejného varování.

## Klíčové vlastnosti

- Definuje rozhraní pro přenos obecných řídicích informací mezi RRC a vyššími vrstvami
- Primárně slouží pro příjem vysílaných systémových informací a zpráv buněčného vysílání
- Funguje přes společné logické kanály jako BCCH a FACH
- Podporuje jednosměrný tok informací (síť → UE) pro vysílaná data
- Umožňuje efektivní šíření síťových parametrů všem UE v buňce
- Standardizovaná servisní primitiva zajišťují interoperabilitu mezi UE a sítí

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [GC-SAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gc-sap/)
