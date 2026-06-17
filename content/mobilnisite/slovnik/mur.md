---
slug: "mur"
url: "/mobilnisite/slovnik/mur/"
type: "slovnik"
title: "MUR – Modify UE context Request"
date: 2025-01-01
abbr: "MUR"
fullName: "Modify UE context Request"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mur/"
summary: "Příkaz založený na protokolu Diameter používaný v architektuře Řízení politik a účtování (PCC) k žádosti o změny v kontextu relace uživatelského zařízení (UE). Umožňuje dynamické aktualizace politik,"
---

MUR je příkaz (command) v architektuře Diameter v rámci PCC, který žádá o změny v kontextu relace UE a umožňuje dynamické aktualizace politik, jako jsou změny QoS, bez nutnosti úplného obnovení relace.

## Popis

Modify UE context Request (MUR) je příkaz (command) protokolu Diameter definovaný ve specifikacích 3GPP, primárně používaný při interakci mezi funkcí pravidel politik a účtování (PCRF) a funkcí vynucování politik a účtování (PCEF) nebo funkcí vázání přenosových kanálů a hlášení událostí ([BBERF](/mobilnisite/slovnik/bberf/)). Funguje v rámci referenčních bodů Gx a Gxx. Když se změní síťové podmínky, aktualizuje se služební profil účastníka nebo je třeba použít nová účtovací pravidla, PCRF zahájí příkaz MUR. Tento příkaz nese aktualizovaná pravidla řízení politik a účtování (PCC), která zahrnují parametry jako identifikátory třídy služeb ([QCI](/mobilnisite/slovnik/qci/)), prioritu přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)) a informace o účtovacím klíči. Příjemce (PCEF/BBERF) pak tato nová pravidla vynutí na příslušném přenosovém kanálu (kanálech), čímž zajistí, že relace UE odpovídá aktualizované politice. Tento mechanismus je klíčový pro implementaci dynamického řízení politik a umožňuje služby, jako je okamžité zvýšení QoS pro streamování videa nebo aplikace sponzorovaných datových tarifů v reálném čase. Proces MUR zachovává kontinuitu relace a zároveň umožňuje síti přizpůsobit se měnícím se požadavkům, čímž tvoří jádro rámce politik 3GPP pro inteligentní správu provozu a jeho zpoplatnění.

## K čemu slouží

Příkaz MUR byl zaveden, aby řešil potřebu dynamických změn politik v průběhu relace v rámci architektury PCC 3GPP. Před jeho standardizací často změny politik vyžadovaly těžkopádné postupy, jako je deaktivace a opětovná aktivace přenosového kanálu, nebo dokonce úplné ukončení a znovunavázání relace. To bylo neefektivní, způsobovalo přerušení služeb a omezovalo schopnost sítě nabízet služby v reálném čase a pružně reagovat. Vytvoření MUR bylo motivováno rostoucí poptávkou po sofistikované diferenciaci služeb, jako jsou vrstvené datové tarify, nabídky kvality na vyžádání a scénáře síťového řezání (network slicing). Umožňuje operátorům okamžitě aplikovat nové obchodní pravidla nebo se přizpůsobit přetížení sítě bez dopadu na uživatelský zážitek. Historicky, jak se mobilní sítě vyvíjely z jednoduchých datových kanálů na platformy citlivé na služby, schopnost dynamicky upravovat relace se stala základním požadavkem pro zpoplatnění a efektivní využití zdrojů, což MUR naplňuje.

## Klíčové vlastnosti

- Umožňuje dynamické aktualizace pravidel PCC v průběhu relace
- Nese aktualizované parametry QoS (např. QCI, ARP) pro vynucení
- Podporuje změnu účtovacích pravidel a účtovacích klíčů
- Funguje přes referenční body Gx a Gxx založené na protokolu Diameter
- Umožňuje změny politik spouštěné událostmi (např. změna polohy, vyčerpání kvóty)
- Zachovává kontinuitu relace během aplikace politiky

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface

---

📖 **Anglický originál a plná specifikace:** [MUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mur/)
