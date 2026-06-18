---
slug: "xdms"
url: "/mobilnisite/slovnik/xdms/"
type: "slovnik"
title: "XDMS – XML Document Management Server"
date: 2025-01-01
abbr: "XDMS"
fullName: "XML Document Management Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xdms/"
summary: "XDMS je klíčová komponenta IP Multimedia Subsystem (IMS), která spravuje uživatelsky specifická servisní data ve formátu XML. Umožňuje vytváření, modifikaci, získávání a mazání XML dokumentů používaný"
---

XDMS je klíčová komponenta IMS, která spravuje uživatelsky specifická servisní data ve formátu XML a umožňuje vytváření, modifikaci, získávání a mazání XML dokumentů pro služby, jako je přítomnost (presence) a zasílání zpráv.

## Popis

[XML](/mobilnisite/slovnik/xml/) Document Management Server (XDMS) je základní síťová entita v architektuře 3GPP IP Multimedia Subsystem (IMS), specificky definovaná pro správu konfiguračních dat souvisejících se službami. Funguje jako úložiště a procesní jednotka pro XML dokumenty, které definují uživatelsky specifická nastavení služeb, preference a datové sady. Tyto dokumenty jsou klíčové pro pokročilé služby IMS, jako je Přítomnost (Presence), Zasílání zpráv (Messaging), Konferencování (Conferencing) a Správa skupin (Group Management). XDMS poskytuje standardizovaný, zabezpečený a spolehlivý mechanismus, který autorizovaným klientům – typicky aplikačním serverům ([AS](/mobilnisite/slovnik/as/)) nebo uživatelskému zařízení (UE) prostřednictvím proxy – umožňuje manipulovat s těmito XML dokumenty pomocí protokolu XML Configuration Access Protocol ([XCAP](/mobilnisite/slovnik/xcap/)).

Architektonicky není XDMS jediný monolitický server, ale logická funkce, která může být implementována jako vyhrazený server pro konkrétní službu (např. Presence XDMS pro seznamy přítomnosti) nebo jako sdílený zdroj. Rozhraní má s dalšími základními prvky IMS, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), pro účely autentizace a přístupu k předplatitelským datům. Základním protokolem pro interakci je XCAP, což je protokol založený na [HTTP](/mobilnisite/slovnik/http/), který mapuje prvky a atributy XML dokumentů na HTTP [URI](/mobilnisite/slovnik/uri/). To umožňuje klientům používat standardní HTTP metody (GET, PUT, DELETE) k provádění operací nad specifickými fragmenty XML dokumentu bez nutnosti pracovat s celým dokumentem, což umožňuje efektivní aktualizace a snižuje síťový provoz.

Klíčovou operační rolí XDMS je vynucování autorizačních politik, které zajišťuje, že pouze přihlášení a autentizovaní uživatelé nebo autorizované síťové entity mohou přistupovat nebo upravovat konkrétní dokumenty. Také řeší správu verzí dokumentů a řešení konfliktů při souběžných aktualizacích. XDMS často pracuje ve spojení s Agregačním proxy (Aggregation Proxy), které slouží jako jednotný kontaktní bod pro UE a směruje XCAP požadavky na správnou konkrétní instanci XDMS (např. Shared XDMS, Group XDMS, [RLS](/mobilnisite/slovnik/rls/) XDMS) na základě použití aplikace. Tento modulární design umožňuje škálovatelné nasazení služeb a jasné oddělení odpovědností mezi různými službami v ekosystému IMS.

## K čemu slouží

XDMS byl vytvořen, aby řešil potřebu standardizované, centralizované a zabezpečené metody pro správu uživatelských dat a konfigurace služeb v rámci IMS. Před jeho specifikací byla servisní data často ukládána v proprietárních, izolovaných formátech v rámci jednotlivých aplikačních serverů, což ztěžovalo sdílení dat mezi službami a bránilo interoperabilitě služeb. Tato fragmentace omezovala vytváření složených služeb, které by mohly využívat společná uživatelská data, jako je například sdílený seznam kontaktů pro služby přítomnosti, zasílání zpráv a konferencování.

Jeho zavedení ve verzi 6 (Release 6) bylo motivováno vizí IMS jako platformy pro poskytování služeb schopné podporovat širokou škálu multimediálních služeb od různých dodavatelů. XDMS, využívající [XML](/mobilnisite/slovnik/xml/) pro reprezentaci dat a HTTP/XCAP pro správu, poskytl dodavatelsky neutrální, webu přátelský paradigma pro manipulaci s daty. Tím vyřešil kritické problémy konzistence dat, řízení přístupu a síťové efektivity, což umožnilo personalizované a interaktivní služby. Položil základ pro bohaté komunikační sady tím, že zajistil, aby uživatelsky definovaná data – jako jsou seznamy přátel, definice skupin a preference služeb – mohla být konzistentně spravována a přístupná v celé síti, čímž vytvořil datovou vrstvu pro servisní architekturu IMS.

## Klíčové vlastnosti

- Standardizované ukládání a správa XML dokumentů pro data služeb IMS
- Protokol XCAP založený na HTTP pro manipulaci s dokumenty (GET, PUT, DELETE)
- Podpora detailního přístupu k dokumentům pomocí adresování URI na XML uzly
- Integrace s autentizačními a autorizačními mechanismy IMS
- Podpora Agregačního proxy (Aggregation Proxy) pro směrování požadavků na konkrétní instance služeb XDMS
- Detekce a správa konfliktů při souběžných aktualizacích dokumentů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [XCAP – XML Configuration Access Protocol](/mobilnisite/slovnik/xcap/)

## Definující specifikace

- **TS 23.779** (Rel-13) — MCPTT over LTE Stage 2 Study
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [XDMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/xdms/)
