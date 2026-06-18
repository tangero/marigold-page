---
slug: "dane"
url: "/mobilnisite/slovnik/dane/"
type: "slovnik"
title: "DANE – DASH Aware Network Element"
date: 2025-01-01
abbr: "DANE"
fullName: "DASH Aware Network Element"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dane/"
summary: "Síťový prvek, který je obeznámen s operacemi Dynamic Adaptive Streaming over HTTP (DASH) za účelem optimalizace doručování médií. Monitoruje chování klienta DASH a stav sítě, aby zlepšil kvalitu uživa"
---

DANE (DASH-Aware Network Element) je síťový prvek, který monitoruje chování klienta DASH a stav sítě za účelem optimalizace doručování médií a zlepšení kvality uživatelského zážitku (Quality of Experience) prostřednictvím streamování s podporou sítě.

## Popis

[DASH](/mobilnisite/slovnik/dash/) Aware Network Element (DANE) je funkční entita v rámci síťové architektury 3GPP, která je speciálně navržena pro vylepšení doručování mediálního obsahu pomocí MPEG-DASH (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)). Na rozdíl od tradičních síťových prvků, které zacházejí se vším HTTP provozem stejně, DANE disponuje inteligencí týkající se protokolů specifických pro DASH, chování klientů a adaptační logiky. Funguje jako prostředník mezi klienty DASH a obsahovými servery, aktivně monitoruje a potenciálně ovlivňuje streamovací relaci, aby udržel optimální kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) pro koncového uživatele.

Z architektonického hlediska může být DANE implementován jako samostatná síťová funkce nebo integrován do existujících uzlů, jako je Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)), Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), nebo v rámci uživatelské roviny (např. jako součást vylepšení User Plane Function ([UPF](/mobilnisite/slovnik/upf/))). Jeho základní operace spočívá v analýze HTTP provozu za účelem identifikace DASH relací, typicky kontrolou HTTP hlaviček a souboru Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) – manifestu, který popisuje dostupné mediální segmenty, jejich datové toky, rozlišení a další charakteristiky. Analýzou MPD DANE rozumí dostupné adaptační sadě a potenciálním volbám klienta.

Klíčem k funkčnosti DANE je jeho schopnost shromažďovat a korelovat dva primární informační toky: stav sítě a chování klienta. Monitoruje metriky sítě v reálném čase, jako je dostupná šířka pásma, latence a ztrátovost paketů na přenosovém kanálu obsluhujícím klienta DASH. Současně sleduje požadavky klienta na mediální segmenty, zaznamenává vybraný datový tok, rozlišení a načasování těchto požadavků. Kombinací těchto znalostí může DANE detekovat suboptimální rozhodnutí klienta, například když klient volí vysoký datový tok v době hrozícího zahlcení sítě nebo setrvává u nízkého datového toku navzdory dostupné šířce pásma.

Na základě své analýzy může DANE iniciovat různé optimalizační akce. Ty jsou často usnadněny rozhraními s řízením politik (např. rozhraní Rx) nebo přímo v rámci uživatelské roviny. Například DANE může spustit síťové politiky pro přidělení garantovaných zdrojů ([GBR](/mobilnisite/slovnik/gbr/)) pro streamovací relaci během kritických období přehrávání, aby se zabránilo opětovnému načítání. Může také poskytovat klientovi informace o síťové podpoře, a to buď implicitně formováním provozu, nebo explicitně prostřednictvím signalizace v pásmu nebo vylepšených MPD, aby nasměroval adaptační logiku klienta k volbě, která maximalizuje QoE vzhledem k aktuálnímu stavu sítě. Tím se proces streamování mění z čistě klientem řízené, reaktivní adaptace na optimalizační smyčku s podporou sítě, která je více prediktivní.

## K čemu slouží

DANE byl vytvořen, aby řešil základní výzvy doručování vysoce kvalitního video streamování přes mobilní sítě, kde je šířka pásma proměnná a sdílená mezi mnoha uživateli. Před DANE byla adaptace DASH zcela řízena klientem (klientská adaptace). Klient odhadoval dostupnou šířku pásma na základě vlastních pozorování (jako je doba stahování segmentů) a vybíral vhodný datový tok z MPD. Tento přístup má významná omezení: odhady klienta mohou být nepřesné kvůli křížovému provozu, klient nemá přehled o širším zahlcení sítě nebo rádiových podmínkách a jeho rozhodnutí mohou vést k nestabilitě (kolísání datových toků), neefektivnímu využití síťových zdrojů nebo špatné QoE (časté opětovné načítání nebo nízká kvalita videa).

Motivace pro DANE vycházela z potřeby operátora získat zpět určitou kontrolu a přehled nad dominantním typem provozu v jejich sítích – videem. Operátoři disponují holistickými znalostmi sítě, které jednotlivým klientům chybí. DANE umožňuje posun směrem k streamování s podporou sítě, kde síť poskytuje návod nebo vynucuje podmínky pro zlepšení celkové efektivity a spokojenosti uživatelů. To je obzvláště důležité v mobilním prostředí, kde jsou rádiové zdroje omezené a náklady neefektivního streamování (z hlediska uživatelského zážitku i kapacity sítě) jsou vysoké.

Historicky bylo jeho zavedení ve verzi 12 součástí širšího zaměření 3GPP na sítě s povědomím o službách a optimalizaci QoE. Představovalo krok za pouhou jednoduchou prioritizaci provozu (Deep Packet Inspection) směrem k opravdovému povědomí a spolupráci na aplikační vrstvě. Řešením problému informační asymetrie mezi klientem a sítí umožňuje DANE stabilnější streamovací relace, lepší využití síťových zdrojů během zahlcení a nakonec konzistentnější a kvalitnější video zážitek pro účastníky, což je klíčový konkurenční rozdíl pro mobilní operátory.

## Klíčové vlastnosti

- Analýza provozu s povědomím o MPD pro identifikaci a porozumění DASH streamovacím relacím
- Korelace adaptačního chování klienta s měřeními stavu sítě v reálném čase
- Schopnost spouštět řízení politik (např. přes PCRF) pro přidělení vyhrazených zdrojů přenosového kanálu pro streamování
- Podpora síťového návodu pro adaptaci datového toku pro klienty DASH
- Shromažďování a monitorování metrik QoE pro služby DASH (např. poměr opětovného načítání, průměrný datový tok)
- Integrační body s funkcemi jádra sítě, jako jsou TDF, PCRF a brány uživatelské roviny

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [TDF – Traffic Detection Function](/mobilnisite/slovnik/tdf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.957** (Rel-19) — Evaluation of MPEG DASH SAND for 3GPP

---

📖 **Anglický originál a plná specifikace:** [DANE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dane/)
