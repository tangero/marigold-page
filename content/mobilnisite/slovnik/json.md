---
slug: "json"
url: "/mobilnisite/slovnik/json/"
type: "slovnik"
title: "JSON – JavaScript Object Notation"
date: 2026-01-01
abbr: "JSON"
fullName: "JavaScript Object Notation"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/json/"
summary: "JSON je odlehčený, textově založený formát pro výměnu dat hojně používaný v 3GPP pro rozhraní založená na službách (SBI), komunikaci síťových funkcí (NF) a reprezentaci řídicích dat. Umožňuje struktur"
---

JSON je odlehčený, textově založený formát pro výměnu dat používaný v 3GPP pro rozhraní založená na službách, komunikaci síťových funkcí a reprezentaci řídicích dat.

## Popis

JavaScript Object Notation (JSON) je textově založený, na jazyku nezávislý datový formát využívající čitelný text k reprezentaci dvojic atribut–hodnota a polí. V 3GPP, počínaje Release 12 a plně přijatý pro jádro 5G sítě (5GC) od Release 15, je JSON primárním formátem pro serializaci dat pro rozhraní založená na službách ([SBI](/mobilnisite/slovnik/sbi/)) mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) využívající [HTTP](/mobilnisite/slovnik/http/)/2. Funguje tak, že strukturovaná data představuje jako kolekce dvojic název/hodnota (objekty) a uspořádané seznamy hodnot (pole), přenášené jako text kódovaný v [UTF-8](/mobilnisite/slovnik/utf-8/). Mezi klíčové architektonické komponenty patří JSON Schema pro definici datových struktur v OpenAPI specifikacích a jeho použití v rámci HTTP/2 zpráv pro operace jako objevování, registrace a vyvolání služeb NF. Datové části (payloady) JSON nesou kritické informace jako profily NF, předplatitelská data, pravidla politik a kontexty správy relací. Jeho role je ústřední pro bezstavovou, modulární architekturu jádra 5G sítě, umožňující efektivní, flexibilní a pro vývojáře přátelskou komunikaci stroj-stroj. Specifikace podrobně popisují použití mediálního typu (application/json), pravidla kódování a povinná/nepovinná pole pro četné servisní operace.

## K čemu slouží

JSON byl v 3GPP přijat, aby poskytl jednodušší a efektivnější alternativu k [XML](/mobilnisite/slovnik/xml/) pro výměnu dat v síťových [API](/mobilnisite/slovnik/api/), zejména s přechodem na cloud-nativní, na službách založené architektury v 5G. Předchozí přístupy používající XML nebo ASN.1 [PER](/mobilnisite/slovnik/per/) mohly být rozvláčné a složité na parsování, což zpomalovalo vývoj a zpracování. JSON tento problém řeší tím, že nabízí odlehčený, snadno parsovatelný formát, který je v souladu s moderními postupy webového vývoje, snižuje režii a zlepšuje interoperabilitu v RESTful API. Historickým motivem byla potřeba agilní expozice a správy služeb v LTE/EPC (počínaje Rel-12 pro určitá rozhraní) a jeho plné přijetí pro [SBI](/mobilnisite/slovnik/sbi/) v 5G za účelem podpory síťového řezání, automatizace a rychlého nasazování služeb.

## Klíčové vlastnosti

- Odlehčený, textově založený formát snižující režii parsování a šířku pásma
- Nativní kompatibilita s webovými technologiemi a návrhem RESTful API
- Strukturován jako kolekce dvojic název/hodnota a uspořádané seznamy
- Kódování UTF-8 zajišťující širokou podporu znakových sad
- Používán pro datové části (payloady) HTTP/2 zpráv v rozhraních založených na službách (SBI) 3GPP
- Definován pomocí JSON Schema v OpenAPI specifikacích 3GPP pro interoperabilitu

## Definující specifikace

- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 24.559** (Rel-19) — Application Data Analytics Enablement Services
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- … a dalších 41 specifikací

---

📖 **Anglický originál a plná specifikace:** [JSON na 3GPP Explorer](https://3gpp-explorer.com/glossary/json/)
