---
slug: "hdr"
url: "/mobilnisite/slovnik/hdr/"
type: "slovnik"
title: "HDR – High Dynamic Range"
date: 2025-01-01
abbr: "HDR"
fullName: "High Dynamic Range"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hdr/"
summary: "HDR je standard pro video technologii, který rozšiřuje kontrastní poměr a barevný gamut nad rámec standardního dynamického rozsahu (SDR). Poskytuje větší detail ve světlech a stínech a živější barvy,"
---

HDR je standard pro video technologii, který rozšiřuje kontrastní poměr a barevný gamut, aby poskytl větší detail a živější barvy, a tím zlepšil vizuální kvalitu multimediálních služeb v mobilních sítích.

## Popis

High Dynamic Range (HDR) ve standardech 3GPP definuje technické požadavky a profil kodeků pro zachycení, kódování, přenos a zobrazení videa s rozšířeným rozsahem jasu a širším barevným gamutem ve srovnání se standardním dynamickým rozsahem (SDR). Technologie funguje definováním nových přenosových funkcí, jako je Hybrid Log-Gamma ([HLG](/mobilnisite/slovnik/hlg/)) nebo Perceptual Quantizer (PQ), které mapují úrovně světla odkazující na scénu nebo na displej do digitálních kódových hodnot efektivněji než tradiční gama křivka používaná pro SDR. Tyto přenosové funkce umožňují reprezentaci mnohem širšího rozsahu úrovní jasu, od hlubokých stínů po lesklé světelné odlesky, a zároveň optimalizují využití bitové hloubky pro lidské vnímání. Architektura zahrnuje end-to-end aspekty, od tvorby obsahu pomocí HDR kamer, přes kódování pomocí kodeků jako [HEVC](/mobilnisite/slovnik/hevc/) nebo VVC, které podporují HDR metadata (např. MaxCLL, MaxFALL), síťový přenos, až po dekódování a vykreslování na displejích s podporou HDR. Mezi klíčové specifikované komponenty patří barevné primáry (např. [BT](/mobilnisite/slovnik/bt/).2020), bitové hloubky (10 bitů a více) a signalizace HDR parametrů v rámci mediálního kontejneru a streamovacích protokolů jako [DASH](/mobilnisite/slovnik/dash/) nebo [HLS](/mobilnisite/slovnik/hls/). Jeho úlohou v síti je zajistit, aby systém pro doručování multimédií zachoval zvýšenou vizuální věrnost od zdroje k obrazovce, což vyžaduje soulad mezi specifikacemi aplikační vrstvy (např. profily kodeků) a přenosovými službami, které zvládnou potenciálně vyšší datové toky HDR obsahu. 3GPP TS 26.116 a související specifikace podrobně popisují konformní body pro zařízení a služby, což zajišťuje interoperabilitu v celém ekosystému.

## K čemu slouží

Technologie HDR byla vytvořena, aby řešila omezení videa se standardním dynamickým rozsahem (SDR), které nedokázalo přesně reprezentovat celý rozsah jasu a barev nacházejících se v reálných scénách nebo který je schopná reprodukovat moderní zobrazovací technika. Před HDR bylo video omezeno na omezený kontrastní poměr a barevný gamut (jako [BT](/mobilnisite/slovnik/bt/).709), který pokrýval pouze část lidského vidění, což vedlo k přepáleným světlům, ztrátě detailů ve stínech a méně živým obrazům. Motivací pro standardizaci HDR v rámci 3GPP byl rychlý přechod spotřební elektroniky na HDR televizory a tlak obsahového průmyslu na vyšší kvalitu produkce. Aby bylo možné zajistit bezproblémový zážitek z médií na mobilních zařízeních, bylo nutné definovat, jak je HDR video zabaleno a doručováno přes mobilní sítě, a zajistit tak, aby se chytré telefony a tablety mohly stát primárními zařízeními pro konzumaci prémiového obsahu. Tato standardizace řeší problém fragmentovaných proprietárních HDR formátů tím, že poskytuje jednotný rámec pro poskytovatele služeb a výrobce zařízení, a usnadňuje tak zavádění služeb videa vysoké kvality, jako je mobilní streamování Ultra [HD](/mobilnisite/slovnik/hd/) a vysílání nové generace přes sítě LTE a 5G.

## Klíčové vlastnosti

- Rozšířený rozsah jasu podporující úrovně jasu od 0,005 do 10 000 nitů a více
- Široký barevný gamut využívající primární barvy definované v ITU-R BT.2020
- Podpora HDR přenosových funkcí jako Hybrid Log-Gamma (HLG) a Perceptual Quantizer (PQ)
- Integrace s pokročilými video kodeky (HEVC, VVC) prostřednictvím specifických profilů a úrovní
- Signalizace statických a dynamických HDR metadat (např. SMPTE ST 2086, CTA-861-G)
- End-to-end systémové specifikace pro tvorbu obsahu, distribuci a přehrávání

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [HLG – Hybrid Log Gamma](/mobilnisite/slovnik/hlg/)

## Definující specifikace

- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [HDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hdr/)
