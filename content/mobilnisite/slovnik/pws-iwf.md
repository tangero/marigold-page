---
slug: "pws-iwf"
url: "/mobilnisite/slovnik/pws-iwf/"
type: "slovnik"
title: "PWS-IWF – Public Warning System - Interworking Function"
date: 2025-01-01
abbr: "PWS-IWF"
fullName: "Public Warning System - Interworking Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pws-iwf/"
summary: "PWS-IWF je funkce jádra sítě, která umožňuje doručování zpráv systému varování veřejnosti (Public Warning System), jako je systém varování před zemětřesením a tsunami (ETWS) a komerční systém mobilníc"
---

PWS-IWF je funkce jádra sítě, která slouží jako brána, překládá a směruje zprávy systému varování veřejnosti od poskytovatelů výstrah k síťovým prvkům pro rozhlasové vysílání napříč různými přístupovými technologiemi.

## Popis

Funkce pro propojení systému varování veřejnosti (Public Warning System - Interworking Function, PWS-IWF) je specializovaný síťový uzel definovaný v architektuře 3GPP, specifikovaný primárně v TS 29.168. Jeho hlavní úlohou je sloužit jako vstupní bod a adaptační vrstva pro zprávy systému varování veřejnosti vstupující do sítě 3GPP od externích varovných orgánů, jako jsou vládní agentury. PWS-IWF přijímá varovné zprávy přes standardizovaná rozhraní, typicky od entity pro rozhlasové vysílání buňkami (Cell Broadcast Entity, [CBE](/mobilnisite/slovnik/cbe/)), která je zdrojem obsahu výstrahy. Po přijetí PWS-IWF vykonává několik klíčových funkcí: autentizuje zdroj zprávy, aby zajistil její legitimitu, ověřuje formát a obsah zprávy a následně zprávu upravuje pro doručení přes síť 3GPP. Tato úprava zahrnuje mapování příchozích informací o výstraze na specifické datové jednotky protokolu ([PDU](/mobilnisite/slovnik/pdu/)) požadované jádrem sítě, jako jsou ty pro centrum rozhlasového vysílání buňkami (Cell Broadcast Center, [CBC](/mobilnisite/slovnik/cbc/)).

PWS-IWF komunikuje s centrem rozhlasového vysílání buňkami (CBC) pomocí rozhraní SBc, což je standardní rozhraní pro distribuci varovných zpráv v rámci sítě 3GPP. Architektura PWS-IWF je navržena jako technologií přístupu nezávislá, což znamená, že může podporovat doručování výstrah k uživatelským zařízením (UE) připojeným přes Evolved Packet Core (EPC) pro 4G/LTE, 5G Core (5GC) pro 5G a dokonce i přes starší systémy. Zajišťuje potřebné převody protokolů a správu relací, aby byla varovná zpráva správně předána CBC, které následně orchestruje vysílání zprávy do cílových geografických oblastí přes příslušné základnové stanice ([eNB](/mobilnisite/slovnik/enb/), gNB).

Kritickým technickým aspektem PWS-IWF je jeho podpora různých typů varovných systémů, primárně ETWS a [CMAS](/mobilnisite/slovnik/cmas/). Pro ETWS zpracovává primární a sekundární notifikační zprávy, které vyžadují velmi nízkou latenci. Pro CMAS spravuje širší škálu kategorií a stupňů závažnosti výstrah. PWS-IWF také hraje roli v prioritizaci zpráv, zajišťuje, aby kritická varování měla přednost před ostatním síťovým provozem. Může zaznamenávat doručování zpráv pro účely auditu a poskytovat zprávy o doručení zpět varovnému orgánu. Jeho implementace je klíčová pro splnění regulatorních požadavků na systémy varování veřejnosti v mnoha zemích, neboť poskytuje standardizovanou, spolehlivou a bezpečnou bránu pro informace zachraňující životy.

## K čemu slouží

PWS-IWF byl vytvořen, aby řešil kritickou potřebu standardizovaného, spolehlivého a bezpečného mechanismu pro doručování zpráv systému varování veřejnosti mobilním účastníkům. Před jeho standardizací byly varovné systémy často proprietární, roztříštěné a neefektivní při využití všudypřítomného pokrytí mobilních sítí. Tsunami v Indickém oceánu v roce 2004 a další katastrofy poukázaly na omezení stávajících metod varování, což vedlo regulatorní orgány po celém světě k nařízení, aby mobilní sítě byly schopny vysílat nouzové výstrahy.

3GPP vyvinulo rámec systému varování veřejnosti ([PWS](/mobilnisite/slovnik/pws/)) pro splnění těchto regulatorních požadavků. PWS-IWF konkrétně řeší problém interoperability mezi externími, ne-3GPP varovnými systémy (jako jsou vládní varovné platformy) a interní architekturou sítě 3GPP. Poskytuje jediný, standardizovaný vstupní bod, který zajišťuje, že výstrahy od jakéhokoli autorizovaného zdroje mohou být přijaty, autentizovány a správně naformátovány pro vysílání v celé síti. Tím odpadá potřeba vícečetných, vlastních integrací mezi poskytovateli výstrah a každým mobilním operátorem, což snižuje složitost a zvyšuje spolehlivost.

Dále PWS-IWF umožňuje podporu pokročilých funkcí varování, jako je geografické cílení (výstrahy pro konkrétní buňky), prioritizace zpráv a podpora více typů varování (zemětřesení, tsunami, pohřešované dítě atd.) v rámci jednotného rámce. Jeho vytvoření bylo motivováno cílem zachraňovat životy včasnou komunikací, což z něj činí základní součást příspěvku moderních mobilních sítí k veřejné bezpečnosti.

## Klíčové vlastnosti

- Slouží jako standardizovaná brána mezi externími poskytovateli výstrah (např. CBE) a jádrem sítě 3GPP.
- Podporuje více technologií varování veřejnosti včetně ETWS a CMAS.
- Provádí autentizaci a ověření příchozích varovných zpráv pro zajištění bezpečnosti a legitimity.
- Přizpůsobuje a překládá protokoly varovných zpráv pro doručení přes rozhraní SBc do centra rozhlasového vysílání buňkami (CBC).
- Umožňuje technologií přístupu nezávislé doručování výstrah napříč 4G EPC, 5G 5GC a staršími jádry sítí.
- Poskytuje mechanismy pro prioritizaci zpráv a jejich zaznamenávání pro účely auditu a dodržování předpisů.

## Související pojmy

- [CMAS – Commercial Mobile Alert Service](/mobilnisite/slovnik/cmas/)

## Definující specifikace

- **TS 29.168** (Rel-19) — SBc-AP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PWS-IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pws-iwf/)
