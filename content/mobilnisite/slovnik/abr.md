---
slug: "abr"
url: "/mobilnisite/slovnik/abr/"
type: "slovnik"
title: "ABR – Adaptive Bit Rate"
date: 2025-01-01
abbr: "ABR"
fullName: "Adaptive Bit Rate"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/abr/"
summary: "ABR je technika doručování streamovaných médií, při které je zdrojový obsah zakódován do více bitových rychlostí a segmentován do malých částí. Klientův přehrávač dynamicky vybírá segment s odpovídají"
---

ABR je technika streamování, při které je obsah zakódován do více bitových rychlostí, což klientovi umožňuje dynamicky vybírat segmenty pro přizpůsobení kvality videa aktuálním síťovým podmínkám za účelem plynulého přehrávání.

## Popis

Adaptivní streaming s proměnnou bitovou rychlostí (ABR) je základní technologií v architektuře služeb streamování médií ([MSS](/mobilnisite/slovnik/mss/)) standardu 3GPP, která umožňuje efektivní doručování video a audio obsahu přes mobilní sítě. Základním principem je zakódování zdrojového média do více reprezentací (či variant), každé s různou bitovou rychlostí, rozlišením a úrovní kvality. Tyto reprezentace jsou následně fragmentovány na krátké, typicky 2–10 sekund dlouhé mediální segmenty. Manifestový soubor, například Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) ve standardu MPEG-DASH, poskytuje klientovi „menu“ dostupných segmentů a jejich charakteristik. Logika adaptivní bitové rychlosti (ABR) na straně klienta, často označovaná jako algoritmus adaptace rychlosti, průběžně sleduje klíčové ukazatele výkonu jako dostupnou propustnost, stav bufferu a možnosti zařízení. Na základě tohoto aktuálního vyhodnocení vybere a požádá o další segment z nejvhodnější reprezentace s cílem maximalizovat kvalitu a přitom se vyhnout opětovnému načítání do bufferu.

Specifikace 3GPP, zejména TS 26.247 ([PSS](/mobilnisite/slovnik/pss/)) a ty definující profily [DASH](/mobilnisite/slovnik/dash/) (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)), standardizují formáty doručování a interakce klient-server pro ABR. Architektura je typicky založená na HTTP a využívá existující webovou infrastrukturu pro ukládání do mezipaměti ([CDN](/mobilnisite/slovnik/cdn/)) a škálovatelnost. Mezi klíčové součásti patří entita přípravy obsahu, která provádí kódování do více bitových rychlostí a balení; původní server nebo CDN, který ukládá a doručuje segmenty a manifest; a klientský přehrávač se svým správcem ABR. Algoritmus správce ABR je klíčový – využívá heuristiku nebo pokročilejší modely (jako predikce propustnosti, řízení na základě bufferu nebo hybridní metody) k rozhodování, kdy přepnout bitovou rychlost. Konzervativní algoritmus může upřednostnit bezpečnost bufferu, zatímco agresivní může usilovat o vyšší kvalitu, přičemž každý přináší různé kompromisy v oblasti stability kvality a rizika opětovného načítání.

Úlohou ABR v síti je oddělit doručování médií od proměnlivosti přenosové vrstvy. Mobilní rádiové podmínky se rychle mění kvůli pohybu uživatele, rušení a zatížení buňky. Tradiční progresivní stahování nebo streamování s konstantní bitovou rychlostí by způsobovalo buď časté pauzy (buffering), nebo by trvale nevyužívalo dostupnou šířku pásma a poskytovalo podprůměrnou kvalitu. ABR tuto proměnlivost proměňuje ve výhodu. Když je propustnost vysoká, klient vybere segmenty s vysokou bitovou rychlostí a poskytne vynikající vizuální kvalitu. Když propustnost poklesne, třeba kvůli vstupu uživatele do přeplněné oblasti, klient plynule přejde na segment s nižší bitovou rychlostí a udržuje nepřerušované přehrávání. Tato adaptabilita je zásadní pro kvalitu uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) a efektivitu sítě, protože zabraňuje plýtvání retransmisemi paketů s vysokou bitovou rychlostí, které by byly při zahlcení ztraceny nebo zpožděny. Práce 3GPP zajišťuje, že tyto streamovací služby jsou optimalizované pro mobilní ekosystémy a jsou v jejich rámci interoperabilní.

## K čemu slouží

Technologie ABR byla vytvořena k vyřešení základní výzvy doručování kvalitního, nepřerušovaného streamovaného videa přes 'best-effort' IP sítě, zejména mobilní sítě charakteristické vysoce proměnlivou šířkou pásma a latencí. Před ABR se pro streamování primárně používaly protokoly jako Real-Time Streaming Protocol ([RTSP](/mobilnisite/slovnik/rtsp/)) s RTP, které vyžadovaly trvalé připojení a konstantní bitovou rychlost. Tento přístup byl křehký; jakýkoli významný pokles dostupné šířky pásma způsobil viditelné artefakty, zamrznutí nebo úplné selhání přehrávání. Progresivní stahování, další před-ABR metoda, načítalo jeden velký soubor, což bylo neefektivní a nenabízelo žádnou adaptaci po zahájení stahování.

Motivací pro vývoj a standardizaci ABR v rámci 3GPP byl explozivní růst spotřeby mobilního videa. Poskytovatelé služeb a distributoři obsahu potřebovali škálovatelnou a spolehlivou metodu pro doručování videa milionům uživatelů na různých zařízeních a v různých síťových podmínkách. ABR to řeší přesunutím rozhodovací inteligence na klienta. Síť jednoduše doručuje HTTP objekty (segmenty), zatímco klient činí veškerá adaptační rozhodnutí lokálně na základě svého bezprostředního prostředí. To činí systém vysoce škálovatelným, protože využívá standardní HTTP servery a cache, a robustním, protože rozhodnutí klienta jsou založena na pozorovaném výkonu namísto síťové signalizace. Přímo řeší omezení předchozích přístupů tím, že umožňuje plynulé snižování a zvyšování kvality v reakci na změny sítě, což je nezbytné pro udržení spokojenosti uživatelů (QoE) v mobilním kontextu, kde jsou takové změny časté a nepředvídatelné.

## Klíčové vlastnosti

- Vícebitové kódování zdrojového obsahu do odlišných reprezentací
- Časová segmentace média na krátké, nezávisle dekódovatelné části
- Klientsky řízená adaptační logika založená na aktuálním sledování propustnosti a bufferu
- Použití standardizovaných manifestových souborů (např. MPD) pro popis dostupných segmentů
- Doručování založené na HTTP pro kompatibilitu s webovou infrastrukturou a CDN
- Plynulé přepínání mezi úrovněmi kvality během přehrávání bez přerušení

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.999** (Rel-19) — VR Streaming Interoperability Test Material

---

📖 **Anglický originál a plná specifikace:** [ABR na 3GPP Explorer](https://3gpp-explorer.com/glossary/abr/)
