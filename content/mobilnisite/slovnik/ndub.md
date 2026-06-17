---
slug: "ndub"
url: "/mobilnisite/slovnik/ndub/"
type: "slovnik"
title: "NDUB – Network Determined User Busy"
date: 2025-01-01
abbr: "NDUB"
fullName: "Network Determined User Busy"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ndub/"
summary: "Doplňková služba v okruhově přepínaných sítích, kde síť určí, že volaná strana je obsazena, a může poskytnout alternativní zpracování, jako je přesměrování volání nebo obsazovací tón. Jedná se o síťov"
---

NDUB je doplňková služba v okruhově přepínaných sítích, kde síť (nikoli koncové zařízení) určí, že volaná strana je obsazena, a může následně poskytnout alternativní zpracování, například přesměrování volání.

## Popis

Network Determined User Busy (NDUB) je klasická doplňková služba v telekomunikacích definovaná v 3GPP pro okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) základnové sítě, například v GSM a UMTS. Jejím hlavním účelem je umožnit samotné síti – konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Visitor Location Register (VLR) – určit, že volaný mobilní účastník je obsazen a nemůže přijmout příchozí volání. Toto určení je provedeno nezávisle na jakémkoli explicitním signálu obsazení ze samotného koncového zařízení (UE). Síť tento úsudek činí na základě znalosti svého interního stavu o relaci účastníka.

Služba funguje během procedur sestavování volání. Když dorazí příchozí volání pro účastníka, MSC/VLR zkontroluje jeho aktuální stav. Pokud je účastník již zapojen do aktivního hovoru, přenosu krátké textové zprávy (SMS) nebo paketové datové relace (v kontextech, kde jsou CS hovory blokovány během datových relací), síť může aktivovat NDUB. Po určení stavu obsazení se síť nepokouší o stránkování (paging) UE ani o zřízení rádiového kanálu. Místo toho okamžitě zpracuje volání podle profilu služeb účastníka, což může zahrnovat odmítnutí volání s obsazovacím tónem pro volajícího nebo aktivaci jiné doplňkové služby, jako je Call Forwarding on Busy ([CFB](/mobilnisite/slovnik/cfb/)), pro přesměrování volání na hlasovou schránku nebo jiné číslo.

Z architektonického hlediska NDUB spoléhá na data účastníka uložená v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a na dynamický stav relace udržovaný ve VLR. Klíčovou komponentou je servisní logika MSC, která vyhodnocuje stav obsazení. Služba interaguje s dalšími uzly základnové sítě a doplňkovými službami. Jejím úkolem je optimalizovat síťové zdroje a zlepšit uživatelský zážitek tím, že zabrání zbytečnému rádiovému signalizačnímu provozu a stránkování pro účastníka, u kterého je známo, že není dostupný, čímž se snižuje zatížení sítě a potenciálně urychluje alternativní zpracování volání. Představuje síťově orientovaný mechanismus efektivity charakteristický pro tradiční okruhově přepínanou telefonii.

## K čemu slouží

NDUB byl vytvořen za účelem zvýšení efektivity a spolehlivosti dokončování volání v raných okruhově přepínaných sítích 2G (GSM) a 3G (UMTS). Při absenci takové funkce by síť typicky stránkovala účastníka pro každé příchozí volání bez ohledu na jeho skutečnou dostupnost. Pokud by bylo UE obsazeno jiným hovorem, prostě by na stránkování neodpovědělo, nebo by odpovědělo odmítnutím, což by spotřebovávalo cenné rádiové zdroje a prodlužovalo čas sestavení volání, než by byl stav obsazení signalizován zpět volajícímu.

Tato služba vyřešila problém plýtvání signalizací a zpožděných indikací obsazení. Tím, že umožnila základnové síti určit stav obsazení na základě svých záznamů o aktivních relacích, mohla zkrátit proces sestavování volání. Tím se ušetřila kapacita rádiového rozhraní, snížilo se zahlcení stránkovacího kanálu a volající straně byl poskytnut rychlejší zážitek, protože obdržela obsazovací tón nebo byla přesměrována téměř okamžitě. Řešila omezení čistě UE-centrické signalizace obsazení, která mohla být pomalejší a méně efektivní z hlediska zdrojů. I když její relevance poklesla s útlumem okruhově přepínaných služeb ve prospěch IP Multimedia Subsystem (IMS) a VoLTE/VoNR, byl NDUB základní funkcí pro optimalizaci tradičních mobilních hlasových služeb.

## Klíčové vlastnosti

- Určení stavu obsazení účastníka na straně sítě bez interakce s UE
- Spouštění na základě aktivního CS hovoru, přenosu SMS nebo určených datových relací
- Integrace s doplňkovou službou Call Forwarding on Busy (CFB)
- Snížení zbytečného rádiového stránkování a signalizační zátěže
- Rychlejší odmítnutí volání nebo alternativní zpracování pro volající stranu
- Řízení založené na profilu služeb účastníka v HLR/VLR

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.093** (Rel-19) — Completion of Calls to Busy Subscriber (CCBS)
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 24.093** (Rel-19) — CCBS Supplementary Service Stage 3
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS
- **TS 29.827** (Rel-16) — Policy and Charging for Volume Based Charging
- **TS 32.275** (Rel-19) — MMTel Charging Specification

---

📖 **Anglický originál a plná specifikace:** [NDUB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ndub/)
