---
slug: "mcml"
url: "/mobilnisite/slovnik/mcml/"
type: "slovnik"
title: "MCML – Multi-Class Multi-Link PPP"
date: 2025-01-01
abbr: "MCML"
fullName: "Multi-Class Multi-Link PPP"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcml/"
summary: "Rozšíření protokolu Point-to-Point Protocol (PPP), které agreguje více fyzických spojení do jediného logického svazku a podporuje více tříd provozu. Zvyšuje přenosovou kapacitu a poskytuje diferenciac"
---

MCML je rozšíření protokolu Point-to-Point Protocol, které agreguje více fyzických spojení do jediného logického svazku za účelem zvýšení přenosové kapacity a poskytnutí diferenciace QoS pro více tříd provozu.

## Popis

Multi-Class Multi-Link PPP (MCML) je rozšíření protokolu standardního Point-to-Point Protocol (PPP), definované v [IETF](/mobilnisite/slovnik/ietf/) RFC 2686 a referencované ve specifikacích 3GPP, jako je TS 27.060 pro služby mobilní stanice. Kombinuje dvě klíčové funkčnosti: svazování Multi-Link PPP (MLPPP) a diferenciaci tříd provozu. Za prvé, MCML agreguje více nezávislých fyzických spojení (např. více kanálů B [ISDN](/mobilnisite/slovnik/isdn/), modemových připojení nebo časových slotů E1/T1) do jediného logického kanálu, čímž zvyšuje celkovou dostupnou přenosovou kapacitu a poskytuje redundanci. Datové pakety jsou fragmentovány, očíslovány a distribuovány přes členská spojení k přenosu, na přijímací straně jsou pak znovu sestaveny.

Za druhé, a to klíčově, MCML zavádí v tomto agregovaném svazku koncept více tříd provozu. Na rozdíl od základního MLPPP, které zachází se vším provozem stejně, umožňuje MCML přiřadit různé typy dat (např. hlas v reálném čase, interaktivní data, provoz na pozadí) různým třídám. Každá třída může být asociována se specifickými politikami plánování a přeposílání napříč agregovanými spoji. Protokol používá modifikovanou hlavičku PPP obsahující pole identifikátoru třídy. To umožňuje implementaci jednoduchých mechanismů QoS, zajišťujících, že provoz citlivý na zpoždění (jako hlas v paketové doméně) může být upřednostněn před méně kritickým datovým provozem.

Z architektonického hlediska MCML funguje na vrstvě spojení (vrstva 2). Nachází se nad jednotlivými fyzickými spoji a pod síťovými protokoly, jako je IP. Mezi klíčové komponenty patří logika fragmentace a opětovného sestavení, mechanismus sekvencování pro zvládnutí doručení mimo pořadí přes více cest a klasifikátor, který mapuje pakety z vyšších vrstev na konkrétní třídy provozu na základě nastavených pravidel. V kontextu 3GPP byl MCML zvláště relevantní pro definici toho, jak může mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) navázat paketové datové spojení se sítí využívající paralelně více přenosových kanálů, čímž podporoval diferenciaci služeb v počátcích paketových jader GSM/[GPRS](/mobilnisite/slovnik/gprs/) a UMTS, než byly plně vyvinuty pokročilejší QoS architektury.

## K čemu slouží

MCML byl vyvinut, aby řešil dvě hlavní omezení standardního PPP na konci 90. let a počátku 21. století: omezenou přenosovou kapacitu na jedno fyzické spojení a absenci vestavěné podpory kvality služeb (QoS). S rozvojem datových služeb v mobilních i pevných sítích vznikla potřeba poskytovat připojení s vyšší přenosovou kapacitou spojením více nízkorychlostních okruhů, jako jsou například více [ISDN](/mobilnisite/slovnik/isdn/) linek nebo modemových spojů. Standardní Multi-Link PPP (MLPPP) toto svazování poskytoval, ale zacházel se vším agregovaným provozem homogenně.

Účelem MCML bylo rozšířit MLPPP o diferenciaci tříd provozu. Tato potřeba byla motivována rostoucí nutností přenášet smíšené typy provozu – zejména hlas v reálném čase (VoIP) spolu s tradičními daty – přes stejný agregovaný spoj. Bez diferenciace tříd mohly být hlasové pakety zpožděny za velkými datovými pakety, což degradovalo kvalitu hovoru. MCML to řešil tím, že umožňoval síťovým zařízením upřednostňovat třídy provozu, což zajišťovalo lepší výkon pro aplikace citlivé na zpoždění. V kontextu 3GPP poskytoval standardizovanou metodu pro mobilní stanice k vyjednání a používání více tříd provozu přes svázané spoje směrem k síti, čímž podporoval rané koncepty QoS pro paketové služby ve vydáních jako Rel-4 a Rel-5.

## Klíčové vlastnosti

- Agreguje více fyzických spojení do jediného logického svazku PPP pro zvýšení přenosové kapacity
- Podporuje více tříd provozu (např. v reálném čase, interaktivní, na pozadí) v rámci svazku
- Obsahuje fragmentaci, sekvencování a opětovné sestavení paketů přes členská spojení
- Používá rozšířenou hlavičku PPP s polem identifikátoru třídy pro označování QoS
- Poskytuje redundanci spojů a vyvažování zátěže přes agregovaná připojení
- Definován pro použití v paketové datové konektivitě mobilní stanice v raných architekturách 3GPP

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain

---

📖 **Anglický originál a plná specifikace:** [MCML na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcml/)
