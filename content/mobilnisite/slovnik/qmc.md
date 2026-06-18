---
slug: "qmc"
url: "/mobilnisite/slovnik/qmc/"
type: "slovnik"
title: "QMC – QoE Measurement Collection"
date: 2026-01-01
abbr: "QMC"
fullName: "QoE Measurement Collection"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qmc/"
summary: "QMC je rámec pro sběr měření kvality uživatelského zážitku (Quality of Experience, QoE) od uživatelského zařízení (UE) v sítích 3GPP. Operátorům umožňuje shromažďovat subjektivní a objektivní data o k"
---

QMC je rámec pro sběr měření kvality uživatelského zážitku (Quality of Experience) od uživatelského zařízení za účelem získání dat o kvalitě služby vnímané uživatelem pro optimalizaci sítě a zajištění služeb.

## Popis

[QoE](/mobilnisite/slovnik/qoe/) Measurement Collection (QMC, sběr měření kvality uživatelského zážitku) je standardizovaný rámec v rámci 3GPP pro sběr metrik kvality uživatelského zážitku (QoE) od koncových uživatelských zařízení. QoE se od tradiční kvality služeb (QoS) liší tím, že se zaměřuje na subjektivní vnímání služby koncovým uživatelem, jako je kvalita videa, čistota zvuku nebo odezva aplikace. Rámec QMC definuje postupy, signalizaci a informační modely nezbytné pro to, aby síť mohla konfigurovat, aktivovat a přijímat měření QoE od uživatelského zařízení (UE). Funguje napříč více typy služeb, přičemž primárně se zaměřuje na služby streamování médií, jako je [HTTP](/mobilnisite/slovnik/http/) Adaptive Streaming (HAS).

Architektura zahrnuje několik síťových funkcí. Funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) nebo aplikační funkce ([AF](/mobilnisite/slovnik/af/)) mohou požadovat měření QoE pro konkrétní uživatele nebo služby. Tento požadavek je komunikován k UE prostřednictvím funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a rádiové přístupové sítě (RAN). UE, vybavené klientem pro měření QoE, poté provádí měření podle přijaté konfigurace. Tato konfigurace zahrnuje parametry jako typ služby (např. streamování videa), cílové metriky (např. počáteční zpoždění přehrávání, poměr opětovného načítání, informace o videokodeku) a spouštěče hlášení (např. periodické, založené na událostech).

UE shromažďuje data během relace služby. Pro streamování videa to mohou zahrnovat metriky aplikační vrstvy, jako je stav vyrovnávací paměti, změny rozlišení a události zastavení přehrávání. Po shromáždění jsou zprávy s měřeními odeslány zpět určené sběrné entitě, často zprostředkovací funkci ([MF](/mobilnisite/slovnik/mf/)) nebo přímo aplikační funkci (AF), jako je server pro analýzu videa. Zprávy jsou přenášeny přes standardizovaná rozhraní, jako je Nq mezi UE a AMF, a potenciálně Nm mezi AMF a MF. Shromážděná data jsou následně operátorem nebo poskytovatelem služeb agregována a analyzována, aby získali přehled o reálném výkonu služeb, identifikovali problematické oblasti a řídili zlepšování sítě a služeb.

## K čemu slouží

QMC bylo zavedeno, aby vyřešilo rostoucí potřebu operátorů a poskytovatelů služeb porozumět skutečnému zážitku koncového uživatele, který není plně zachycen tradičními síťově orientovanými metrikami QoS. Jak se služby jako streamování videa staly dominantními, problémy jako zastavování videa, degradace rozlišení a pomalé časy spuštění přímo ovlivňovaly spokojenost a udržení uživatelů. Před QMC se operátoři spoléhali na síťové sondy, hlubokou kontrolu paketů (DPI) nebo omezené proprietární hlášení ze zařízení, což poskytovalo neúplný nebo nepřímý pohled na [QoE](/mobilnisite/slovnik/qoe/).

Vytvoření QMC bylo motivováno posunem průmyslu k uživatelsky orientovanému řízení sítě. Řeší problém získávání přímých, standardizovaných a bohatých dat QoE z koncového bodu samotného – z UE. To umožňuje korelovat síťové podmínky (např. sílu rádiového signálu, propustnost) se skutečným výkonem aplikace, jak jej vnímá uživatel. Standardizací tohoto sběrného rámce ve verzi Rel-14 a novějších zajistil 3GPP interoperabilitu mezi zařízeními a síťovými analytickými platformami, což umožňuje škálovatelnou, automatizovanou optimalizaci řízenou QoE a operace s uzavřenou smyčkou.

## Klíčové vlastnosti

- Standardizovaná konfigurace měření QoE ze sítě k UE
- Podpora více typů služeb, primárně zaměřená na streamování médií (např. DASH)
- Sběr metrik aplikační vrstvy, jako jsou události přehrávání, úrovně vyrovnávací paměti a informace o kodeku
- Flexibilní spouštěče hlášení včetně periodického hlášení a hlášení spouštěného událostmi
- Přenos zpráv s měřeními přes rozhraní jádra sítě (např. Nq, Nm)
- Integrace s řízením politik (PCF) a aplikačními funkcemi (AF) pro cílené kampaně měření

## Související pojmy

- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TR 26.812** (Rel-18) — Technical Report
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.308** (Rel-19) — QoE Measurement Collection IRP: Information Service
- **TS 28.405** (Rel-19) — QoE Measurement Control & Configuration
- **TS 28.406** (Rel-19) — QoE measurement collection: info definition & transport
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.410** (Rel-19) — NG Interface Introduction for NG-RAN to 5GC
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [QMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/qmc/)
