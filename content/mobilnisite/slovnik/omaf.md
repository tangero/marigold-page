---
slug: "omaf"
url: "/mobilnisite/slovnik/omaf/"
type: "slovnik"
title: "OMAF – Omnidirectional Media Application Format"
date: 2025-01-01
abbr: "OMAF"
fullName: "Omnidirectional Media Application Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/omaf/"
summary: "OMAF (Omnidirectional Media Application Format) je standard 3GPP a MPEG, který definuje mediální formát, doručování a zobrazování 360stupňového videa a imerzních médií přes sítě. Specifikuje způsob kó"
---

OMAF je standard 3GPP a MPEG, který definuje formát, doručování a zobrazování 360stupňových a imerzních médií pro konzistentní přehrávání přes sítě.

## Popis

OMAF, standardizovaný jako [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 23090-2 a přijatý organizací 3GPP v TS 26.114 a souvisejících specifikacích, je komplexní mediální formát navržený speciálně pro všesměrová (360stupňová) média. Staví na existujících mediálních základech, jako je ISO Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) a High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)), ale přidává zásadní rozšíření pro sférické video. Jádrem OMAF je definice souřadnicového systému a metod projekce pro mapování 360stupňového sférického videa na 2D obdélníkový video snímek za účelem efektivního kódování a uložení. Mezi běžné projekce patří ekvirektangulární projekce ([ERP](/mobilnisite/slovnik/erp/)) a kubemapová projekce ([CMP](/mobilnisite/slovnik/cmp/)).

Z architektonického hlediska OMAF definuje mediální zpracovatelský řetězec. Na straně tvorby je sférické video projektováno, zakódováno pomocí HEVC (a volitelně [AVC](/mobilnisite/slovnik/avc/)) a zabaleno do segmentů ISOBMFF s metadaty specifickými pro OMAF. Tato metadata zahrnují základní informace, jako je formát projekce, region-wise packing (které mapuje sférické oblasti na 2D snímek) a počáteční orientace pohledu. Pro doručování OMAF podporuje Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) (DASH), kde jsou média rozdělena do segmentů s více úrovněmi kvality (datovými toky). Klíčovou vlastností je viewport-dependent streaming, kdy klient vyžaduje segmenty vyšší kvality pouze pro tu část sféry, která je aktuálně v zorném poli uživatele (viewport), čímž šetří šířku pásma.

Na straně klienta/přehrávače OMAF přehrávač demultiplexuje proud, čte metadata OMAF, dekóduje video a provádí inverzní projekci, aby znovu vykreslil sférické video pro zobrazení, typicky na head-mounted display (HMD) nebo na obrazovce smartphonu používaného s VR prohlížečem. Spravuje sledování viewportu a podle toho přizpůsobuje streamovací požadavky. OMAF také specifikuje audio formáty, včetně kanálového, scénového (Ambisonics) a objektového audia, které doprovází 360stupňové video pro plně imerzní zážitek. Jeho role v síti 5G spočívá v tom, že je klíčovým formátem aplikační vrstvy, který využívá vysokou šířku pásma a nízkou latenci 5G pro poskytování služeb imerzních médií.

## K čemu slouží

OMAF byl vytvořen, aby řešil nedostatek standardizace v rychle se rozvíjejícím oboru 360stupňového a virtuální reality (VR) videa. Před OMAF používali tvůrci obsahu, poskytovatelé služeb a výrobci zařízení proprietární nebo nekompatibilní formáty pro zachycení, kódování a streamování sférického videa. Tato fragmentace hrozila udušením růstu imerzních médií vytvářením uzavřených ekosystémů, kde by obsah jednoho poskytovatele nemusel přehrát na zařízení jiného, podobně jako v počátcích mobilního videa.

Primární problém, který OMAF řeší, je zajištění interoperability. Poskytuje jediný, dohodnutý formát, který zaručuje, že jakýkoli 360stupňový obsah kompatibilní s OMAF bude správně přehrán na jakémkoli přehrávači kompatibilním s OMAF, bez ohledu na výrobce. Tím se snižuje složitost a náklady pro celý ekosystém. Dále OMAF řeší významnou technickou výzvu v podobě šířky pásma. Úplné 360stupňové video ve vysokém rozlišení vyžaduje obrovské datové toky, pokud je streamováno v plné kvalitě neustále. Mechanismus viewport-dependent streamingu v OMAF je klíčovou inovací, která to řeší dynamickým streamováním vysoké kvality pouze tam, kde se uživatel dívá, což činí služby imerzního videa realizovatelné přes mobilní sítě jako 4G a 5G.

K jeho vytvoření motivoval pohyb průmyslu směrem k imerzním zážitkům jako součásti use caseů 5G, jako je enhanced Mobile Broadband (eMBB). Standardizační organizace jako MPEG a 3GPP spolupracovaly, aby zajistily, že formát je optimalizován jak pro uložení/vysílání, tak pro adaptivní streamování přes IP sítě. Tím, že je OMAF součástí specifikací 3GPP, je přímo integrován do architektury pro doručování médií v 5G, což operátorům umožňuje nabízet standardizované, vysoce kvalitní služby VR/360 videa.

## Klíčové vlastnosti

- Standardizované formáty projekce sférického videa (ERP, CMP) a metadata
- Viewport-dependent adaptivní streamování využívající DASH pro efektivitu šířky pásma
- Integrace s video kodeky HEVC/H.265 a AVC/H.264
- Streamovatelný formát souboru a segmentace založená na ISOBMFF
- Podpora imerzních audio formátů (Ambisonics, objektové audio)
- Definuje počáteční viewport, region-wise packing a souřadnicové systémy

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [VR – Virtualized Resource](/mobilnisite/slovnik/vr/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TR 26.999** (Rel-19) — VR Streaming Interoperability Test Material

---

📖 **Anglický originál a plná specifikace:** [OMAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/omaf/)
