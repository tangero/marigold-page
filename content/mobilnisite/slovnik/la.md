---
slug: "la"
url: "/mobilnisite/slovnik/la/"
type: "slovnik"
title: "LA – Local Area Base Station"
date: 2025-01-01
abbr: "LA"
fullName: "Local Area Base Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/la/"
summary: "Local Area Base Station (LA) je nízkovýkonová základnová stanice mobilní sítě určená pro malé pokrytí, jako jsou domácnosti, kanceláře nebo hotspoty, poskytující lokalizovanou kapacitu a pokrytí. Je t"
---

LA (Local Area Base Station) je nízkovýkonová základnová stanice mobilní sítě určená pro malé pokrytí, jako jsou domácnosti nebo kanceláře, poskytující lokalizovanou kapacitu a pokrytí jako základní koncept pro femtobuňky a small cells.

## Popis

Local Area Base Station (LA), často zmiňovaná v kontextu Local Area [BS](/mobilnisite/slovnik/bs/) nebo small cell, je základnová stanice mobilní sítě charakterizovaná nízkým vysílacím výkonem (typicky méně než několik wattů) a malým poloměrem pokrytí (od desítek do několika set metrů). Je navržena pro obsluhu lokalizovaných oblastí, jako jsou obytné domy, firemní kanceláře, městské hotspoty nebo indoorové prostory, a doplňuje makrobuněčnou síť. Ve specifikacích 3GPP zahrnuje LA různé implementace včetně Home NodeB ([HNB](/mobilnisite/slovnik/hnb/)) pro 3G UMTS, Home eNodeB (HeNB) pro 4G LTE a následně ng-eNB nebo NR small cells pro 5G, ačkoli samotný termín 'LA' je obecná klasifikace. Architektura zahrnuje připojení LA k jádru sítě přes backhaulový spoj (často širokopásmový internet jako [DSL](/mobilnisite/slovnik/dsl/) nebo optika) a využití brány (např. HeNB Gateway, Femto Gateway) pro agregaci a zabezpečení.

Provozně LA pracuje na licencovaném spektru, podobně jako makro základnové stanice, ale s redukovaným výkonem pro omezení interference a umožnění hustého nasazení. Poskytuje radiový přístup uživatelským zařízením (UE) ve své lokální oblasti a zvládá všechny procedury fyzické vrstvy, [MAC](/mobilnisite/slovnik/mac/) a [RRC](/mobilnisite/slovnik/rrc/). Mezi klíčové funkce patří výběr/převýběr buňky, handover do/z makro buněk, správa interference a samokonfigurace/samooptimalizace ([SON](/mobilnisite/slovnik/son/)). Pro koordinaci interference se používají techniky jako Almost Blank Subframes ([ABS](/mobilnisite/slovnik/abs/)) v LTE nebo řízení výkonu. LA typicky podporuje uzavřený přístup ([CSG](/mobilnisite/slovnik/csg/) - Closed Subscriber Group) pro soukromé použití, otevřený přístup nebo hybridní režimy, což umožňuje kontrolu nad tím, která UE se mohou připojit.

V ekosystému sítě jsou LA spravovány operátory pro odlehčení provozu z makro sítí, zlepšení indoorového pokrytí tam, kde je signál slabý, a zvýšení kapacity v zónách s vysokou poptávkou. Integrují se s jádrem sítě přes standardní rozhraní: pro LTE se HeNB připojuje k EPC přes rozhraní S1 k MME a S-GW; pro 5G se NR small cells připojují přes rozhraní NG k AMF a UPF. Specifikace pokrývají RF požadavky (např. 36.104, 38.104), testování výkonu (např. 36.141, 38.141) a mobilní procedury (např. 23.271). LA jsou klíčové pro zhušťování sítě, umožňují vyšší datové rychlosti, nižší latenci a lepší spektrální účinnost díky prostorovému opakovanému využití. Tvoří základ moderních heterogenních sítí (HetNets), kde koexistuje více vrstev buněk, a jsou nezbytné pro uspokojení kapacitních požadavků 5G a dalších generací v městských a podnikových scénářích.

## K čemu slouží

Koncept Local Area Base Station vznikl k řešení problémů s pokrytím a kapacitou v mobilních sítích, zejména indoorově a v hustých městských oblastech. Samotné makro buňky mají potíže s pronikáním do budov, což vede ke špatné kvalitě indoorového signálu, a mají omezenou kapacitu na hotspotech. Zpočátku spoléhali rezidenční a podnikoví uživatelé na Wi-Fi pro indoorové pokrytí, ale to postrádalo bezproblémovou mobilitu, kvalitu služeb a kontrolu operátora. Zavedení LA základnových stanic (počínaje 3G femtobuňkami v R99) umožnilo operátorům rozšířit licencované mobilní pokrytí pomocí nízkovýkonových uzlů instalovaných zákazníky, což zlepšilo zákaznický zážitek a snížilo odchod zákazníků.

Historicky byl vývoj LA motivován potřebou nákladově efektivního zhušťování sítě. Nasazení makro buněk je drahé a získání lokalit je obtížné; LA využívají existující širokopásmový backhaul a jednoduchou instalaci. Také umožňují efektivní opakované využití spektra: plánovaným používáním stejné frekvence jako makro buňky zvyšují kapacitu sítě. Napříč releasy se LA vyvinuly z jednoduchých femtobuněk na sofistikované small cells se samo-organizujícími schopnostmi, správou interference a podporou pokročilých funkcí jako je agregace nosných. Tento vývoj řešil omezení raných verzí, jako jsou problémy s interferencí a nedostatečná robustnost mobility, čímž se LA staly nedílnou součástí nasazení 4G a 5G pro uspokojení růstu datového provozu a podporu nových služeb jako IoT a privátní sítě.

## Klíčové vlastnosti

- Nízký vysílací výkon (např. < 1W pro indoor) a malá plocha pokrytí (lokalizované nasazení)
- Podporuje backhaul přes spotřebitelský širokopásmový přístup (např. DSL, kabel, optika) se zabezpečovacími branami
- Umožňuje režimy řízení přístupu: Closed Subscriber Group (CSG), otevřený nebo hybridní
- Integruje se s makro sítí pro mobilitu (handover, převýběr buňky) a koordinaci interference
- Zahrnuje schopnosti samokonfigurace a samooptimalizace (SON) pro provoz typu plug-and-play
- Splňuje 3GPP specifikace pro RF a výkon pro koexistenci s makro buňkami

## Související pojmy

- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [LA na 3GPP Explorer](https://3gpp-explorer.com/glossary/la/)
