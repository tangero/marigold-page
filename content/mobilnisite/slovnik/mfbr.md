---
slug: "mfbr"
url: "/mobilnisite/slovnik/mfbr/"
type: "slovnik"
title: "MFBR – Maximum Flow Bit Rate"
date: 2026-01-01
abbr: "MFBR"
fullName: "Maximum Flow Bit Rate"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mfbr/"
summary: "Parametr QoS, který definuje maximální trvalý přenosový tok povolený pro datový tok v rámci PDU relace. Jde o klíčový ukazatel pro vynucení regulace provozu a zajištění spravedlivého rozdělení prostře"
---

MFBR je parametr QoS, který definuje maximální trvalý přenosový tok povolený pro datový tok v rámci PDU relace pro účely regulace provozu a alokace prostředků.

## Popis

Maximum Flow Bit Rate (MFBR) je parametr kvality služeb (QoS) definovaný v modelu 5G QoS. Platí pro jednotlivé QoS toky v rámci relace protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)). QoS tok je nejjemnější úroveň pro diferenciaci QoS v systému 5G a každý tok je spojen s profilem QoS obsahujícím parametry jako 5G QoS Identifikátor ([5QI](/mobilnisite/slovnik/5qi/)), Guaranteed Flow Bit Rate (GFBR) a MFBR. MFBR specifikuje špičkový přenosový tok, který by síť pro daný konkrétní QoS tok neměla překročit. Představuje horní limit pro trvalou přenosovou rychlost.

V praxi se MFBR používá ve funkci uživatelské roviny sítě ([UPF](/mobilnisite/slovnik/upf/)) pro provádění regulace provozu. Když dorazí datové pakety uživatele pro konkrétní QoS tok, UPF změří přenosový tok. Pokud se rychlost toku pokusí překročit nakonfigurovaný MFBR, UPF obvykle nadbytečné pakety zahodí nebo označí (např. pomocí Explicit Congestion Notification), aby limit vynutila. Tím se zabrání tomu, aby jeden QoS tok spotřebovával neúměrné síťové prostředky, což je zásadní pro udržení kvality služeb pro ostatní toky a uživatele. MFBR se vynucuje pro každý tok zvlášť, což umožňuje detailní kontrolu.

MFBR se signalizuje během procedur zřizování nebo modifikace PDU relace. [SMF](/mobilnisite/slovnik/smf/) je zodpovědná za odvození parametrů QoS, včetně MFBR, na základě předpisů od [PCF](/mobilnisite/slovnik/pcf/) a požadované služby. SMF následně tyto parametry poskytuje UPF pro vynucení a RAN (přes [AMF](/mobilnisite/slovnik/amf/)) pro případné zohlednění při alokaci rádiových prostředků. Zatímco RAN pro toky bez garance (non-GBR) primárně používá Aggregate Maximum Bit Rate ([AMBR](/mobilnisite/slovnik/ambr/)), MFBR na úrovni toku je v jádru sítě zásadní pro přesné řízení provozu. Jeho hodnota se obvykle vyjadřuje v kilobitech za sekundu (kbps) nebo megabitech za sekundu (Mbps) a je kritickou součástí pro realizaci síťového segmentování (network slicing), protože různé segmenty mohou mít výrazně odlišné limity MFBR přizpůsobené jejich služebním požadavkům (např. Enhanced Mobile Broadband vs. IoT).

## K čemu slouží

MFBR existuje jako mechanismus pro přesnou regulaci provozu a správu prostředků na úrovni jednotlivých QoS toků. Bez tohoto parametru by datové toky mohly potenciálně spotřebovávat neomezenou šířku pásma, což by vedlo k zahlcení sítě, nespravedlivému rozdělování prostředků a zhoršení služeb pro ostatní uživatele. Je to základní nástroj pro implementaci smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) a diferencovaných tarifních modelů, kde jsou uživatelům nebo službám přidělena specifická maximální přenosová práva.

Historicky podobné koncepty existovaly v dřívějších systémech (jako Maximum Bit Rate v EPS), ale model 5G QoS jej zpřesňuje v rámci flexibilnější, na toky založené architektury. Motivace pro MFBR v 5G je zvýšená díky širokému spektru služeb, od ultra HD videa (vyžadujícího vysoký MFBR) po massive IoT (vyžadující velmi nízký MFBR). Umožňuje provozovatelům sítí efektivně nabízet stupňované datové služby, vynucovat politiky fér použití a zajistit, že kritické služby (s garantovanou přenosovou rychlostí) nebudou strádat kvůli best-effort provozu, který se snaží využít nadměrnou šířku pásma. MFBR je klíčovým prvkem pro efektivitu a monetizaci sítí 5G.

## Klíčové vlastnosti

- Definuje limit špičkového trvalého přenosového toku pro konkrétní QoS tok v rámci PDU relace.
- Používá se v UPF pro regulaci provozu, což zahrnuje zahazování nebo označování paketů při překročení.
- Signalizováno SMF během procedur správy relace.
- Součást profilu 5G QoS spolu s parametry jako 5QI a GFBR.
- Umožňuje detailní kontrolu šířky pásma a vynucení služebního členění.
- Klíčové pro zajištění spravedlivého sdílení prostředků a předcházení zahlcení sítě.

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [MFBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mfbr/)
