---
slug: "uhd"
url: "/mobilnisite/slovnik/uhd/"
type: "slovnik"
title: "UHD – Ultra High Definition"
date: 2026-01-01
abbr: "UHD"
fullName: "Ultra High Definition"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uhd/"
summary: "Ultra High Definition (UHD) je kategorie video služby definovaná 3GPP pro doručování obsahu s výrazně vyšším rozlišením než standardní HD, typicky 4K (3840x2160) nebo 8K (7680x4320). UHD stanovuje pož"
---

UHD je kategorie video služby 3GPP pro doručování obsahu s vysokým rozlišením, jako je 4K nebo 8K, která vyžaduje extrémní šířku pásma pro downlink a efektivní kódování videa pro pokročilé mediální služby.

## Popis

Ultra High Definition (UHD) v kontextu 3GPP představuje komplexní rámec pro služby a schopnosti pro doručování video obsahu s rozlišením 4K (3840x2160 pixelů) a 8K (7680x4320 pixelů), spolu s přidruženými vylepšeními, jako je vysoký dynamický rozsah ([HDR](/mobilnisite/slovnik/hdr/)), široký barevný gamut (WCG) a vysoká snímková frekvence ([HFR](/mobilnisite/slovnik/hfr/)). Z technického hlediska doručování služby UHD přes mobilní sítě zahrnuje složitý řetězec od přípravy obsahu po jeho zobrazení na uživatelském zařízení (UE). Obsah je kódován pomocí pokročilých kodeků, jako je [HEVC](/mobilnisite/slovnik/hevc/) (H.265) nebo [VVC](/mobilnisite/slovnik/vvc/) (H.266), aby se obrovské datové toky (které mohou pro 8K přesáhnout gigabity za sekundu) zkomprimovaly do bitového toku vhodného pro přenos. Tento zakódovaný bitový tok je pak paketizován a přenášen přes systém 3GPP.

V síťové architektuře klade UHD obrovské nároky na přenosovou cestu downlink. Přístupová rádiová síť (RAN) musí podporovat modulaci vyššího řádu (např. 256QAM, 1024QAM), agregaci nosných a Massive [MIMO](/mobilnisite/slovnik/mimo/), aby dosáhla požadovaných trvalých vysokých přenosových rychlostí – často 50-100 Mbps pro 4K a několik set Mbps pro 8K, v závislosti na kompresi. Jádro sítě 5G navazuje [PDU](/mobilnisite/slovnik/pdu/) relace s QoS toky označenými příslušnými hodnotami [5QI](/mobilnisite/slovnik/5qi/), aby zajistilo vysokou prioritu, nízkou ztrátovost paketů a dostatečnou garantovanou přenosovou rychlost toku pro UHD stream. Funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) a funkce řízení politik (PCF) vynucují politiky pro přidělení potřebných prostředků. Dále, pro zajištění efektivity a škálovatelnosti, se služby UHD výrazně spoléhají na edge caching a Content Delivery Networks (CDN), které přibližují oblíbený obsah uživateli, čímž snižují zatížení páteřní sítě a latenci.

Úlohou UHD je definovat cíle výkonu a architektonické prvky pro video služby nové generace v celé jejich trase. Specifikace jako 26.116 a 26.956 podrobně popisují profily kodeků, transportní protokoly, kvalitativní metriky (např. poměr špičkového signálu k šumu, Video Multi-Method Assessment Fusion) a schopnosti zařízení. To zajišťuje interoperabilitu mezi poskytovateli obsahu, síťovými operátory a výrobci zařízení a umožňuje konzistentní vysoce kvalitní zážitek. UHD je také klíčovým hybatelem pro síťové segmentování, kde může být pro prémiové doručování médií vytvořen vyhrazený síťový řez se zaručenou propustností a latencí.

## K čemu slouží

UHD bylo zavedeno ve verzi 3GPP 13 jako reakce na globální vývoj technologie zobrazování videa a poptávku spotřebitelů po věrnějším vizuálním zážitku. Před standardizací UHD byly mobilní video služby většinou omezeny na standardní rozlišení (SD) a vysoké rozlišení (HD - 720p/1080p). Rozšíření UHD televizorů a tvorba profesionálního obsahu ve 4K/8K vytvořilo nesoulad: obsah existoval, ale mobilním sítím chyběla standardizovaná, efektivní cesta, jak jej doručovat se zaručenou kvalitou. Stávající mechanismy QoS sítě a rádiové schopnosti nebyly navrženy pro nárůst přenosových rychlostí o řád a přísné požadavky na kvalitu.

Standardizace UHD v 3GPP si kladla za cíl tento problém vyřešit vytvořením jednotné sady technických požadavků a řešení. Podnítila vývoj a přijetí efektivnějších video kodeků (HEVC), definovala síťové metriky výkonu pro kvalitu videa a prosazovala vylepšení v propustnosti a spolehlivosti rádiového rozhraní. Tím, že UHD poskytlo jasný cíl pro vývoj sítě, zajistilo, že systémy 3GPP, zejména 4G LTE-Advanced a 5G NR, mohou být pozicovány jako životaschopné platformy pro doručování prémiových, působivých médií, které mohou konkurovat pevným širokopásmovým a vysílacím službám.

## Klíčové vlastnosti

- Podpora videa s rozlišením 4K (3840x2160) a 8K (7680x4320)
- Integrace s vysokým dynamickým rozsahem (HDR) a širokým barevným gamutem (WCG)
- Využití pokročilých video kodeků, jako je HEVC a VVC, pro efektivní kompresi
- Definice přísných požadavků na QoS sítě pro vysokorychlostní, nízkolatenční toky
- Soulad se strategiemi edge computingu a ukládání do mezipaměti pro škálovatelné doručování
- Komplexní rámce pro měření a reportování kvality uživatelského zážitku

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [VVC – Versatile Video Coding](/mobilnisite/slovnik/vvc/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.925** (Rel-19) — Media Traffic Characteristics for 3GPP Networks
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [UHD na 3GPP Explorer](https://3gpp-explorer.com/glossary/uhd/)
