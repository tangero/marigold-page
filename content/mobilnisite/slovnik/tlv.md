---
slug: "tlv"
url: "/mobilnisite/slovnik/tlv/"
type: "slovnik"
title: "TLV – Type, Length, Value"
date: 2025-01-01
abbr: "TLV"
fullName: "Type, Length, Value"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/tlv/"
summary: "Flexibilní formát kódování dat hojně používaný v protokolech 3GPP, zejména v hlavičkách GTP. Informace strukturované do samopopisné trojice umožňují efektivní a rozšiřitelné parsování zpráv. Tento for"
---

TLV je flexibilní formát kódování dat, který strukturovaně ukládá informace do samopopisné trojice Typ, Délka a Hodnota, což umožňuje efektivní a rozšiřitelné parsování zpráv v protokolech 3GPP.

## Popis

Formát Typ, Délka, Hodnota (TLV) je základní schéma kódování dat používané k uspořádání informačních prvků v protokolech 3GPP. Skládá se ze tří povinných polí: pole Typ identifikuje druh přenášené informace (např. konkrétní parametr jako [IMSI](/mobilnisite/slovnik/imsi/) nebo [APN](/mobilnisite/slovnik/apn/)), pole Délka určuje velikost pole Hodnota v oktetech a pole Hodnota obsahuje vlastní datový obsah parametru. Tato struktura vytváří samopopisnou datovou jednotku, která umožňuje přijímající entitě správně zpracovat zprávu, i když narazí na neznámý kód typu – ten může na základě uvedené délky jednoduše přeskočit. Formát je zarovnán na bajty a velikost samotných polí Typ a Délka může být pevná nebo proměnná v závislosti na konkrétní implementaci protokolu, což nabízí flexibilitu.

V kontextu 3GPP je TLV nejznámější použití v protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), který slouží k přenosu uživatelských dat a signalizačních zpráv mezi uzly GPRS jádrové sítě, jako jsou [SGSN](/mobilnisite/slovnik/sgsn/), GGSN, [PGW](/mobilnisite/slovnik/pgw/) a [SGW](/mobilnisite/slovnik/sgw/). V rámci zprávy GTP následuje za hlavičkou sekvence informačních prvků ([IE](/mobilnisite/slovnik/ie/)), z nichž každý je zakódován ve formátu TLV. Tento modulární přístup umožňuje přenášet bohatou sadu parametrů a podporuje vše od zřizování relací a vyjednávání QoS až po účtování a správu mobility. Příjemce tyto IE zpracovává postupně, přičemž pomocí typu identifikuje každý parametr a pomocí délky ví, kolik oktetů má načíst pro jeho hodnotu.

Paradigma TLV je klíčové pro rozšiřitelnost protokolů a zpětnou kompatibilitu. S příchodem nových funkcí v pozdějších vydáních 3GPP lze definovat nové informační prvky s novými kódy typu a přidávat je do zpráv. Starší síťové uzly, které novou funkci nepodporují, nový typ nerozpoznají. Protože je však délka explicitně uvedena, mohou tyto starší uzly bezpečně přeskočit celé pole hodnoty neznámého IE a pokračovat ve zpracování zbytku zprávy. Tím se předchází chybám při parsování a zajišťuje se, že síťové aktualizace lze zavádět postupně, aniž by došlo k narušení stávající funkčnosti. Robustnost a jednoduchost TLV z něj činí základní kámen mnoha telekomunikačních a síťových protokolů i mimo 3GPP.

## K čemu slouží

Formát TLV byl vytvořen, aby vyřešil potřebu robustní, rozšiřitelné a efektivní metody kódování strukturovaných dat v komunikačních protokolech. Před zavedením takového standardizovaného kódování často protokoly používaly zprávy s pevným formátem, které byly nepružné a obtížně rozšiřitelné bez narušení kompatibility. Přidání jakéhokoli nového parametru by vyžadovalo nový typ zprávy nebo verzi, což vedlo ke složitosti a problémům s interoperabilitou. TLV to řeší tím, že každý parametr učiní samostatným a samopopisným.

Jeho hlavním účelem v rámci 3GPP, zejména pro GTP, je usnadnit složitou signalizaci a tunelování dat potřebné pro mobilní paketové datové služby. Jediná zpráva GTP, jako je například žádost o vytvoření relace (Create Session Request), musí přenést desítky parametrů týkajících se účastníka, požadovaného přenosového kanálu, síťových adres a pravidel. Pevný formát zprávy pro tento účel by byl nemožně velký a plýtvavý, protože mnoho parametrů je volitelných. TLV umožňuje zahrnout pouze nezbytné parametry, čímž snižuje režii. Důležitější je, že protokol chrání před zastaráváním. Jak se mobilní sítě vyvíjely z GPRS přes EPS až k 5GS a vyžadovaly podporu nových modelů QoS, identifikátorů účtování a parametrů síťového řezání, tyto novinky mohly být plynule přidávány jako nové informační prvky kódované v TLV.

Motivace pro jeho široké přijetí spočívá v jeho elegantním řešení problému verzování. Umožňuje „dopřednou kompatibilitu“ pro starší implementace a „zpětnou kompatibilitu“ pro nové implementace komunikující se starými uzly. To je nezbytné ve velkých mobilních sítích s více dodavateli, kde je koordinovaná a současná aktualizace všech síťových prvků nepraktická. TLV umožňuje síti se plynule vyvíjet, podporovat nové služby na novějších uzlech a zároveň zachovávat základní služby pro účastníky připojené přes starší uzly, čímž chrání investice operátorů a zajišťuje kontinuitu služeb.

## Klíčové vlastnosti

- Samopopisná datová struktura s poli Typ, Délka a Hodnota
- Umožňuje efektivní a flexibilní kódování volitelných a povinných parametrů
- Poskytuje inherentní podporu pro rozšiřitelnost protokolů a zpětnou kompatibilitu
- Umožňuje přijímačům bezpečně přeskočit neznámé informační prvky
- Široce používán v GTP pro signalizaci v jádrové síti a správu přenosových kanálů
- Bajtově zarovnaný formát vhodný pro různé datové typy od celých čísel po řetězce

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [TLV na 3GPP Explorer](https://3gpp-explorer.com/glossary/tlv/)
