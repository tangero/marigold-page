---
slug: "lcg"
url: "/mobilnisite/slovnik/lcg/"
type: "slovnik"
title: "LCG – Logical Channel Group"
date: 2025-01-01
abbr: "LCG"
fullName: "Logical Channel Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lcg/"
summary: "Mechanismus pro seskupování logických kanálů v LTE a NR používaný pro hlášení stavu vyrovnávací paměti (BSR). Umožňuje uživatelskému zařízení (UE) hlásit obsazenost vyrovnávací paměti pro uplinková da"
---

LCG je skupina logických kanálů v LTE a NR používaná pro hlášení stavu vyrovnávací paměti (buffer status reporting), která umožňuje uživatelskému zařízení (UE) hlásit obsazenost vyrovnávací paměti pro uplinková data po skupinách, čímž umožňuje síti efektivní plánování.

## Popis

Logická skupina kanálů (Logical Channel Group, LCG) je koncept zavedený v LTE (Release 8) a zachovaný v NR (5G), který usnadňuje efektivní hlášení stavu vyrovnávací paměti pro uplink ([BSR](/mobilnisite/slovnik/bsr/)) od uživatelského zařízení (UE) k základnové stanici ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR). Logické kanály, které reprezentují různé typy datových toků (např. řídicí nebo uživatelská data pro konkrétní rádiové přenašeče), jsou namapovány na jednu z malého počtu LCG (až 4 v LTE, až 8 v NR). Každá LCG agreguje obsazenost vyrovnávací paměti všech jí přiřazených logických kanálů. Když potřebuje UE informovat síť o čekajících uplinkových datech, vygeneruje řídicí prvek BSR na vrstvě [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control), který hlásí celkové množství dat připravených k odeslání pro každou LCG, nikoli pro každý jednotlivý logický kanál.

Toto seskupení snižuje signalizační režii, protože hlášení po LCG vyžaduje méně bitů ve srovnání s hlášením každého logického kanálu zvlášť. BSR může být spuštěn událostmi, jako je příchod nových dat do prázdné vyrovnávací paměti, periodické časovače nebo vypršení časovače retxBSR-Timer. Formát BSR (krátký nebo dlouhý) je vybrán na základě toho, kolik LCG má data k hlášení. Po přijetí BSR použije plánovač v eNB/gNB informace o vyrovnávací paměti pro každou LCG spolu s dalšími faktory, jako jsou podmínky na kanálu a požadavky QoS, k přidělení uplinkových prostředků (prostřednictvím uplinkových grantů). Plánovač může upřednostnit LCG spojené s přenašeči s vysokou prioritou, čímž zajistí, že provoz citlivý na zpoždění nebo provoz se zaručenou přenosovou rychlostí je obsloužen neprodleně.

Mapování logických kanálů na LCG je konfigurováno sítí prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), typicky na základě charakteristik QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) nebo [5QI](/mobilnisite/slovnik/5qi/). Například všechny logické kanály s podobnou prioritou nebo požadavky na zpoždění mohou být seskupeny do stejné LCG. To umožňuje síti spravovat QoS na jemné úrovni bez nadměrné signalizace. V NR zahrnují vylepšení podporu většího počtu LCG (až 8), aby bylo možné pojmout širší škálu služeb a jemnější diferenciaci QoS, a BSR může obsahovat dodatečné informace, jako jsou rozpočty zpoždění pro provoz [URLLC](/mobilnisite/slovnik/urllc/) (ultra-reliable low-latency communication). Mechanismus LCG je nedílnou součástí dynamického plánování uplinku, což síti umožňuje optimalizovat využití prostředků a splnit různorodé požadavky služeb.

## K čemu slouží

Logická skupina kanálů (Logical Channel Group, LCG) byla vytvořena, aby vyřešila potřebu efektivního hlášení stavu vyrovnávací paměti pro uplink v systémech LTE a NR, a to vyřešením problému signalizační režie spojené s hlášením obsazenosti vyrovnávací paměti pro každý logický kanál jednotlivě. V systémech před LTE, jako je [HSPA](/mobilnisite/slovnik/hspa/), bylo plánování uplinku méně dynamické a zavedení ploché all-IP architektury LTE vyžadovalo agilnější metodu, pomocí které může UE žádat o prostředky. Bez seskupování by hlášení velikosti vyrovnávací paměti každého logického kanálu spotřebovávalo nadměrné uplinkové prostředky a výpočetní výkon, zejména s rostoucím počtem současných přenašečů u víceúčelových zařízení.

Primární motivací bylo umožnit škálovatelnou správu QoS při minimalizaci řídicí signalizace. Seskuplením logických kanálů s podobnými vlastnostmi QoS mohla síť získat dostatečné informace pro inteligentní plánování bez podrobných hlášení na úrovni jednotlivých kanálů. To bylo klíčové pro podporu různorodých aplikací – od hlasu přes IP po streamování videa – z nichž každá má různé požadavky na zpoždění a propustnost. Koncept LCG umožnil eNB efektivně stanovovat priority prostředků a zajistit, aby data s vysokou prioritou (např. z LCG namapované na přenašeče citlivé na zpoždění) byla naplánována dříve než data s nižší prioritou.

Historicky byl LCG zaveden v LTE Release 8 jako součást nového návrhu vrstvy MAC, který kladl důraz na dynamické plánování pro uplink i downlink. Představoval posun od statičtějších metod přidělování prostředků, což umožnilo lepší spektrální účinnost a uživatelský zážitek. Jak se sítě vyvíjely směrem k NR, byl rámec LCG rozšířen, aby podporoval více skupin (až 8), a vyhověl tak zvýšené komplexitě služeb 5G, včetně massive IoT a URLLC, kde je podrobné hlášení stavu vyrovnávací paměti zásadní pro splnění přísných cílů v oblasti latence a spolehlivosti. LCG tak i nadále zůstává základním prvkem pro uplinkovou QoS v moderních mobilních systémech.

## Klíčové vlastnosti

- Seskupuje logické kanály pro efektivní hlášení stavu vyrovnávací paměti
- Snižuje uplinkovou signalizační režii agregací dat o vyrovnávací paměti
- Konfigurovatelné prostřednictvím RRC na základě charakteristik QoS
- Podporuje až 4 LCG v LTE a až 8 LCG v NR
- Umožňuje prioritní plánování uplinku ze strany základnové stanice
- Nedílná součást mechanismů BSR na vrstvě MAC

## Související pojmy

- [BSR – Buffer Status Report](/mobilnisite/slovnik/bsr/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [LCG na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcg/)
