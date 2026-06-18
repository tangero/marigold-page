---
slug: "rtt"
url: "/mobilnisite/slovnik/rtt/"
type: "slovnik"
title: "RTT – Round Trip Time"
date: 2026-01-01
abbr: "RTT"
fullName: "Round Trip Time"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rtt/"
summary: "Celková doba potřebná k přenosu signálu nebo paketu ze zdroje k cíli a zpět, měřená v milisekundách. V sítích 3GPP je RTT klíčovou metrikou pro hodnocení zpoždění, která ovlivňuje výkon aplikací jako"
---

RTT je celková doba v milisekundách potřebná k přenosu signálu ze zdroje k cíli a zpět, což je klíčová metrika zpoždění v sítích 3GPP.

## Popis

Round Trip Time (RTT) je základní metrika výkonnosti sítě, která kvantifikuje zpoždění dvousměrné komunikační výměny. Zahrnuje zpoždění šíření, přenosu, zpracování a zpoždění ve frontách na celé trase, včetně rádiového přístupu, přenosových sítí a prvků jádrové sítě. V architekturách 3GPP se RTT měří mezi uživatelským zařízením (UE) a síťovými uzly, jako jsou základnové stanice (gNB v 5G) nebo servery, pomocí protokolů jako [ICMP](/mobilnisite/slovnik/icmp/) ping nebo specializovaných měřicích postupů definovaných ve specifikacích (např. 37.320 pro samoorganizující se sítě). Hodnota se typicky udává v milisekundách a liší se v závislosti na faktorech jako vzdálenost, vytížení sítě a generace technologie.

Fungování RTT spočívá ve změření intervalu od odeslání paketu žádosti do přijetí odpovídající odpovědi. Například v LTE nebo 5G lze RTT měřit během procedur řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) nebo přenosů v rovině dat. Mezi klíčové komponenty přispívající k RTT patří zpoždění na rádiovém rozhraní (např. struktura rámce a plánování), zpoždění backhaulového připojení a zpracování v jádrové síti (např. v [AMF](/mobilnisite/slovnik/amf/) nebo [UPF](/mobilnisite/slovnik/upf/)). Specifikace 3GPP, jako je 38.306 pro rádiové přístupové schopnosti 5G UE, definují požadavky na maximální RTT pro zajištění kvality služeb, s cíli až 1 ms pro ultra spolehlivé nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) v 5G.

Úloha RTT v síti je klíčová pro správu kvality služeb (QoS) a ovlivňuje uživatelský zážitek u aplikací citlivých na zpoždění, jako je VoIP, online hry nebo autonomní vozidla. RTT se používá v algoritmech pro řízení zahlcení, rozhodování o předávání hovorů a optimalizaci sítě. Monitorováním RTT mohou operátoři identifikovat úzká místa a zavádět techniky jako edge computing nebo síťové segmenty ke snížení zpoždění. Ve vývoji 3GPP jsou metriky RTT nedílnou součástí benchmarkingu výkonnosti a hnací silou inovací v návrhu rádiového rozhraní a architektury jádrové sítě.

## K čemu slouží

RTT existuje jako metrika pro kvantifikaci a správu síťového zpoždění a řeší problémy související s rychlostí a spolehlivostí komunikace v reálném čase. V raných mobilních sítích mohlo vysoké RTT degradovat kvalitu hovoru a propustnost dat, čímž omezovalo přijetí služeb. Měřením RTT standardy 3GPP umožňují optimalizaci síťových parametrů pro dosažení cílových hodnot zpoždění a řeší problémy jako přerušované hovory nebo buffering ve streamovacích službách. Jeho zavedení v Rel-4 poskytlo standardizovaný způsob hodnocení výkonu end-to-end a podpořilo přechod na paketové služby v UMTS.

Historicky rostl důraz na RTT s nástupem interaktivních aplikací; například sítě 3G potřebovaly nižší zpoždění pro videokonference. Dřívější přístupy spoléhaly na zjednodušená měření zpoždění, ale RTT nabídl komplexní pohled na obousměrné zpoždění, nezbytný pro výkon TCP a adaptivní aplikace. Řešil omezení metrik jednosměrného zpoždění tím, že zohledňuje asymetrii sítě a zpětnovazební smyčky, což je klíčové pro mechanismy řízení zahlcení v postupujících vydáních 3GPP.

V moderním kontextu se účel RTT rozšiřuje na podporu technologií jako 5G [URLLC](/mobilnisite/slovnik/urllc/) a IoT, kde milisekundy hrají roli pro průmyslovou automatizaci nebo záchranné služby. Specifikace 3GPP od Rel-15 definují přísné požadavky na RTT pro podporu těchto případů užití, což pohání inovace v návrhu rádiových rámců a disagregaci jádrové sítě. Průběžným zdokonalováním technik měření a snižování RTT zajišťuje 3GPP, že sítě dokážou poskytovat nízkolatenční zážitky požadované pokročilou digitální společností.

## Klíčové vlastnosti

- Měří obousměrné zpoždění end-to-end v milisekundách
- Ovlivňuje QoS pro aplikace v reálném čase, jako je VoIP a hry
- Používá se v algoritmech optimalizace sítě a řízení zahlcení
- Definováno ve specifikacích 3GPP pro výkon rádiové a jádrové sítě
- Podporuje cíle pro ultra nízké zpoždění v 5G URLLC
- Integruje se s měřicími protokoly pro kontinuální monitoring

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.812** (Rel-18) — Technical Report
- **TR 26.910** (Rel-19) — MTSI enhancements for RAN delay budget reporting
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [RTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtt/)
