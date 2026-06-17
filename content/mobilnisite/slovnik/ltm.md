---
slug: "ltm"
url: "/mobilnisite/slovnik/ltm/"
type: "slovnik"
title: "LTM – Lower-layer Triggered Mobility"
date: 2026-01-01
abbr: "LTM"
fullName: "Lower-layer Triggered Mobility"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ltm/"
summary: "Lower-layer Triggered Mobility (LTM) je vylepšení mobility v 5G NR, při kterém jsou rozhodnutí o předání spojení iniciována rádiovou přístupovou sítí na základě měření z nižších vrstev (PHY/MAC), čímž"
---

LTM (Lower-layer Triggered Mobility) je vylepšení mobility v 5G NR, při kterém jsou rozhodnutí o předání spojení iniciována rádiovou přístupovou sítí na základě měření z nižších vrstev za účelem snížení latence.

## Popis

Lower-layer Triggered Mobility (LTM) je klíčové vylepšení mobility zavedené v 5G New Radio pro optimalizaci výkonu předání spojení. Tradičně jsou rozhodnutí o předání spojení v celulárních sítích prováděna protokoly vyšších vrstev v RAN na základě měřicích hlášení od uživatelského zařízení. LTM přesouvá toto rozhodování do nižších vrstev – konkrétně fyzické vrstvy (vrstva 1) a vrstvy řízení přístupu k médiu (vrstva 2) – což umožňuje mnohem rychlejší detekci rádiových podmínek a spouštění procedur mobility. Toho je dosaženo definováním specifických spouštěcích podmínek a událostí přímo na nižších vrstvách, které mohou iniciovat předání spojení bez čekání na pomalejší reportovací cykly signalizace řízení rádiových prostředků vyšší vrstvy.

Z architektonického hlediska LTM zahrnuje vylepšení napříč více síťovými uzly a rozhraními. V gNodeB jsou vrstvy PHY a [MAC](/mobilnisite/slovnik/mac/) vybaveny novými funkcemi pro sledování metrik kvality signálu v reálném čase, jako je Reference Signal Received Power a Reference Signal Received Quality, ve velmi jemném časovém měřítku. Když tyto metriky překročí předdefinované prahové hodnoty signalizující zhoršující se kvalitu spojení nebo přítomnost vhodnější kandidátské buňky, mohou nižší vrstvy okamžitě spustit proceduru přípravy předání spojení. To zahrnuje komunikaci mezi zdrojovým a cílovým gNodeB přes rozhraní Xn s využitím vylepšené signalizace pro urychlení přenosu kontextu a rezervaci prostředků.

Procedura funguje tak, že UE kontinuálně provádí měření na obsluhující a sousední buňky. V LTM jsou tato měření zpracovávána lokálně na nižších vrstvách gNodeB. Po detekci spouštěcí podmínky nižší vrstva gNodeB odešle interní indikaci své entitě [RRC](/mobilnisite/slovnik/rrc/) vyšší vrstvy, nebo v některých implementacích přímo iniciuje signalizaci k cílovému gNodeB. Zapojení jádra sítě, konkrétně funkce Access and Mobility Management Function, je během fáze spuštění minimalizováno, ačkoli je o dokončeném předání spojení informováno. Klíčové pro LTM je snížení doby přerušení při předání spojení, protože latence rozhodování a provedení je drasticky zkrácena, což jej činí ideálním pro scénáře, kdy se UE pohybuje vysokou rychlostí nebo kde je rádiové prostředí vysoce dynamické.

Klíčové komponenty zahrnují vylepšenou konfiguraci měření na UE, nové spouštěcí mechanismy v rámci protokolového zásobníku gNodeB a optimalizované signalizační zprávy Xn-AP pro rychlé provedení předání spojení. Úlohou LTM je doplňovat stávající mechanismy mobility a poskytovat alternativu s nízkou latencí pro kritické podmínky. Je to základní technologie pro zajištění spolehlivého připojení ve vysokorychlostní železniční dopravě, vozidlové komunikaci a průmyslových aplikacích IoT, kde by tradiční latence předání spojení mohly způsobit přerušení služby nebo ztrátu dat.

## K čemu slouží

Lower-layer Triggered Mobility bylo vytvořeno, aby řešilo přísné požadavky na latenci a spolehlivost nových případů užití 5G, jako je rozšířené mobilní širokopásmové připojení ve vysokorychlostních scénářích a ultra-spolehlivá komunikace s nízkou latencí. Tradiční procedury předání spojení, závislé na měřicím reportování a rozhodování na vrstvě [RRC](/mobilnisite/slovnik/rrc/), zavádějí zpoždění, která mohou vést k selhání rádiového spojení, přerušeným hovorům nebo degradované propustnosti dat, když se uživatelé rychle pohybují mezi buňkami. Tato omezení se stala výraznější s nasazením 5G sítí využívajících vyšší frekvenční pásma, která mají menší pokrytí buňkami a rychlejší fluktuace signálu.

Motivace pro LTM vychází z potřeby podporovat plynulou mobilitu pro uživatele ve vozidlech, vlacích a dronech, kde je čas dostupný pro úspěšné předání spojení velmi krátký. Předchozí přístupy zahrnovaly optimalizaci period měřicích hlášení nebo použití duální konektivity, ale ty stále nesly základní zpoždění ze zpracování ve vyšších protokolových vrstvách. LTM zásadně přearchitektuje spouštěcí bod pro mobilitu a využívá rychlejší zpracovací schopnosti vrstev PHY a [MAC](/mobilnisite/slovnik/mac/) k téměř okamžité reakci na měnící se rádiové podmínky.

Zavedeno v 3GPP Release 18, LTM je součástí širší sady vylepšení mobility 5G-Advanced. Řeší problém latence předání spojení tím, že efektivněji umožňuje připojení typu 'make-before-break' a zajišťuje, že UE zachová kontinuitu své relace. To je kritické pro aplikace s požadavkem na vysokou dostupnost, hraní v reálném čase a služby imerzivní rozšířené reality, které nesnesou přerušení. Decentralizací spouštěcího rozhodování do nižších vrstev RAN LTM také snižuje signalizační zátěž na jádru sítě a umožňuje lokalizovanější a rychlejší optimalizaci vzorců mobility přizpůsobující se topologii sítě a podmínkám zatížení v reálném čase.

## Klíčové vlastnosti

- Spouštění předání spojení na základě měření z vrstev PHY/MAC
- Snížená doba přerušení a latence při předání spojení
- Vylepšená signalizace rozhraní Xn pro rychlý přenos kontextu
- Podpora scénářů s vysokou mobilitou (např. vozidlová komunikace, vysokorychlostní železnice)
- Součinnost s tradiční mobilitou řízenou RRC
- Dynamická konfigurace spouštěcích podmínek sítí

## Definující specifikace

- **TS 28.313** (Rel-20) — Management and orchestration; SON for 5G networks
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.420** (Rel-19) — Introduction to Xn interface specifications
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [LTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ltm/)
