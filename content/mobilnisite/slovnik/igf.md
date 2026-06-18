---
slug: "igf"
url: "/mobilnisite/slovnik/igf/"
type: "slovnik"
title: "IGF – Intelligent Gap Filling"
date: 2025-01-01
abbr: "IGF"
fullName: "Intelligent Gap Filling"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/igf/"
summary: "Intelligent Gap Filling (IGF) je funkcionalita 3GPP pro streamovací služby, která dynamicky generuje a vkládá mediální obsah, aby vyplnila mezery v přehrávání způsobené snížením kvality sítě, jako je"
---

IGF je funkcionalita 3GPP pro streaming, která dynamicky generuje mediální obsah pro vyplnění mezer v přehrávání způsobených snížením kvality sítě, čímž zlepšuje kvalitu uživatelského zážitku (QoE) díky zachování kontinuity.

## Popis

Intelligent Gap Filling (IGF), specifikovaný v dokumentu 3GPP TS 26.253, je pokročilá funkce zpracování médií určená pro streamovací služby, zejména pro Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Jejím hlavním účelem je zmírnit negativní dopad zastavení přehrávání (událostí opětovného načítání bufferu) na kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)). Když se vyprázdní buffer přehrávače kvůli problémům s propustností sítě, IGF namísto zobrazení zamrzlého obrazu nebo indikátoru načítání dokáže vygenerovat a vložit syntetický mediální obsah, který mezeru vyplní, dokud nemůže pokračovat standardní mediální proud. Tento obsah není předem zakódován a uložen; je inteligentně vytvářen v reálném čase na základě okolního skutečného mediálního obsahu.

Architektura IGF zahrnuje komponenty jak v síti, tak potenciálně na straně klienta. Klíčovou entitou je funkce pro zpracování médií, která může být umístěna na aplikačním serveru nebo jako součást Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) v kontextu IMS. Tato funkce monitoruje streamovací relaci a při detekci nebo po obdržení informace o hrozícím vyprázdnění bufferu aktivuje proceduru vyplňování mezer. Analyzuje poslední úspěšně dekódované snímky videa a/nebo zvuku předcházející mezeře. S využitím technik, jako je zamrznutí snímku, extrapolace snímků nebo generování komfortního šumu, vytvoří plynulé pokračování média. Toto vygenerované médium je pak paketizováno a doručeno klientovi, jako by bylo součástí původního proudu, často s využitím reprezentací s nižním datovým tokem pro úsporu zdrojů.

Jak IGF funguje, je vícestupňový proces. Nejprve klient nebo síťový proxy detekuje vyprázdnění bufferu a signalizuje tento stav (explicitně nebo implicitně) funkci IGF. Funkce IGF poté vezme poslední snímek videa a vzorky zvuku. Pro video může opakovaně odesílat tento poslední snímek („zamrzlý snímek“) s odpovídajícími časovými razítky nebo může vytvořit jednoduchou extrapolaci pohybu. Pro audio může generovat komfortní šum nebo opakovat krátký zvukový segment. Zásadní je, že spravuje časovou osu média, aby zajistila plynulé navázání, když se původní vysoce kvalitní proud opět stane dostupným. Klient dekóduje a vykresluje tento vyplňovací mediální obsah, čímž poskytuje uživateli kontinuální, byť potenciálně nižší kvality, zážitek z prohlížení namísto úplného přerušení. IGF úzce souvisí s dalšími funkcemi pro QoE, jako je adaptace šířky pásma a logika přepínání v adaptivním streamingu.

## K čemu slouží

IGF byl vyvinut k řešení přetrvávajícího a velmi nápadného problému internetového videostreamování: opětovného načítání bufferu. I s pokročilými algoritmy adaptivního datového toku může dočasná zahlcení sítě způsobit vyprázdnění bufferu přehrávače, což nutí přehrávání zastavit. Tento „indikátor načítání“ nebo zamrzlý obraz významně snižuje uživatelskou spokojenost. Účelem IGF je inteligentně zamaskovat tyto mezery a vytvořit tak iluzi nepřerušovaného přehrávání, čímž se zlepší vnímaná plynulost a kvalita služby.

Motivace pro jeho vytvoření v rámci 3GPP Release 18 vychází z rostoucí spotřeby vysoce kvalitního videa (včetně 4K/8K, [VR](/mobilnisite/slovnik/vr/)) přes mobilní sítě, kde je proměnlivost šířky pásma inherentní. Předchozí přístupy se spoléhaly výhradně na přehrávač na straně klienta ke správě bufferingu, bez standardizovaného způsobu, jak by síť mohla pomoci zmírnit vizuální dopad zastavení. IGF zavádí standardizovaný síťově asistovaný mechanismus pro vyplňování těchto mezer. Řeší problém pasivního čekání během opětovného načítání bufferu aktivním udržováním mediálního výstupu. To je obzvláště cenné pro živé streamování a komunikaci v reálném čase, kde jsou pauzy obzvlášť rušivé, a umožňuje poskytovatelům služeb diferencovat své nabídky díky lepší, odolnější kvalitě uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

## Klíčové vlastnosti

- Dynamicky generuje vyplňovací mediální obsah (video/zvuk) pro pokrytí mezer při opětovném načítání bufferu
- Využívá techniky jako zamrznutí snímku, extrapolaci a generování komfortního šumu
- Funguje v rámci architektur adaptivního streamování (DASH)
- Může být implementován jako síťová funkce pro zpracování médií
- Udržuje kontinuitu časové osy média pro plynulý přechod po ukončení mezery
- Cílí na zlepšení vnímané kvality uživatelského zážitku (QoE) při snížení kvality sítě

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [IGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/igf/)
