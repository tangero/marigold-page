---
slug: "mpd"
url: "/mobilnisite/slovnik/mpd/"
type: "slovnik"
title: "MPD – Media Presentation Description"
date: 2025-01-01
abbr: "MPD"
fullName: "Media Presentation Description"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpd/"
summary: "Dokument založený na XML používaný v Dynamic Adaptive Streaming over HTTP (DASH) k popisu struktury a charakteristik multimediální prezentace. Poskytuje klientům informace o dostupných mediálních segm"
---

MPD je dokument založený na XML používaný v DASH k popisu struktury multimediální prezentace, dostupných mediálních segmentů a jejich charakteristik pro adaptivní streamování s proměnným datovým tokem.

## Popis

Media Presentation Description (MPD) je klíčový metadatový soubor definovaný 3GPP pro standard Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Je to [XML](/mobilnisite/slovnik/xml/) dokument, který poskytuje kompletní plán multimediální prezentace a umožňuje DASH klientovi dynamicky požadovat a adaptivně přehrávat mediální obsah. MPD popisuje časové a strukturální vztahy mezi mediálními komponentami, jako je video, audio a titulky, které jsou segmentovány a uloženy na HTTP serveru. Neobsahuje samotná mediální data, ale funguje jako manifest nebo playlist, který detailně popisuje, jak je prezentace organizována v čase (Periods) a jak je každá mediální komponenta reprezentována v různých kvalitách (Representations) v rámci Adaptation Sets.

Architektonicky je MPD strukturováno hierarchicky. Na nejvyšší úrovni definuje celkovou prezentaci s atributy jako doba trvání prezentace a minimální doba vyrovnávací paměti. Prezentace je rozdělena na sekvenční Periods, které reprezentují souvislé časové intervaly obsahu a umožňují změny v obsahu (např. hlavní film na reklamu) nebo kódovacích parametrech. V rámci každého Periodu skupiny Adaptation Sets sdružují mediální komponenty, které jsou logicky propojeny, jako jsou všechny video proudy nebo všechny audio stopy v různých jazycích. Každý Adaptation Set obsahuje více Representations, což jsou alternativní zakódování stejné mediální komponenty s různým datovým tokem, rozlišením nebo kodekem. Každá Representation je dále rozdělena na Segments, což jsou skutečné mediální soubory (např. části .mp4 nebo .m4s), které klient stahuje pomocí HTTP GET požadavků. MPD poskytuje pro tyto segmenty [URL](/mobilnisite/slovnik/url/), rozsahy bajtů a časové informace.

Jak to funguje: klient nejprve před začátkem přehrávání získá a zpracuje MPD. Na základě informací v MPD a aktuálních síťových podmínek (např. dostupné šířky pásma) adaptační logika klienta vybere nejvhodnější Representation pro stažení segment po segmentu. To umožňuje adaptivní streamování s proměnným datovým tokem, při kterém může klient mezi segmenty přepnout na vyšší nebo nižší kvalitu Representation, aby udržel plynulé přehrávání bez načítání do vyrovnávací paměti. MPD může být statické (všechny informace jsou známy předem) nebo dynamické (periodicky aktualizované pro živé streamování, s novými Periods a Segments přidávanými, jakmile jsou k dispozici). MPD také obsahuje základní metadata jako informace o kodeku (např. [HEVC](/mobilnisite/slovnik/hevc/), [AAC](/mobilnisite/slovnik/aac/)), podrobnosti o systému ochrany [DRM](/mobilnisite/slovnik/drm/) (např. Common Encryption, signalizace pro MPEG-CENC) a funkce přístupnosti, jako jsou popisovače rolí pro různé audio stopy (např. komentář, popisné video). Jeho úlohou je oddělit popis média od jeho doručování, což poskytuje flexibilní, standardizovaný způsob umožňující efektivní, spolehlivé a vysoce kvalitní streamovací služby přes sítě typu best-effort, jako je internet a mobilní sítě.

## K čemu slouží

MPD bylo vytvořeno, aby řešilo výzvy spojené s doručováním vysoce kvalitního, adaptivního video streamování přes [HTTP](/mobilnisite/slovnik/http/), které se stalo dominantní metodou pro distribuci videa na internetu. Před DASH a MPD proprietární řešení adaptivního streamování (jako Apple HLS nebo Microsoft Smooth Streaming) používala různé formáty manifestů, což vedlo k fragmentaci a zvýšené složitosti pro poskytovatele obsahu, kteří museli kódovat a ukládat více verzí svého obsahu pro různá zařízení a platformy. MPD jako součást standardizované specifikace DASH poskytuje jednotný, interoperabilní formát, který umožňuje popsat a doručit jednu sadu zakódovaných mediálních segmentů jakémukoli kompatibilnímu klientovi, čímž snižuje náklady na úložiště a provoz.

Motivace pro jeho vývoj v rámci 3GPP vycházela z potřeby efektivně doručovat multimediální služby přes mobilní sítě, kde je šířka pásma proměnná a může docházet k přetížení. Tradiční progresivní stahování nebo neadaptivní streamování často vedlo ke špatné uživatelské zkušenosti s častým načítáním do vyrovnávací paměti nebo nízkou kvalitou videa. MPD umožňuje inteligentní adaptaci na straně klienta tím, že poskytuje všechny potřebné informace pro klienta, aby mohl činit informovaná rozhodnutí o tom, který mediální segment má načíst další, na základě aktuálních síťových podmínek a možností zařízení. Tím se řeší problém doručování konzistentního, vysoce kvalitního zážitku ze sledování napříč různorodými sítěmi a zařízeními, což je klíčové pro mobilní operátory a poskytovatele obsahu.

Historicky bylo MPD představeno v 3GPP Release 9 jako součást počátečních specifikací DASH a poskytlo základní prvek pro Packet-Switched Streaming Service (PSS) 3GPP a později pro Enhanced Multimedia Broadcast/Multicast Service (eMBMS) a 5G Media Streaming. Řešilo omezení dřívějších streamovacích protokolů 3GPP, které nebyly nativně adaptivní nebo založené na HTTP. Využitím všudypřítomnosti HTTP, jeho cacheování a schopnosti procházet firewally v kombinaci s bohatým popisem v MPD se DASH stal klíčovým prvkem pro škálovatelné, efektivní doručování videa a vytvořil základ pro moderní streamovací služby, včetně over-the-top (OTT) platforem a služeb podobných vysílání v mobilních sítích.

## Klíčové vlastnosti

- Strukturovaný manifest založený na XML popisující časovou strukturu mediální prezentace
- Podporuje jak statické (on-demand), tak dynamické (live) streamovací scénáře
- Umožňuje adaptivní přepínání datového toku popisem více Representations pro každý Adaptation Set
- Obsahuje komplexní metadata: kodeky, rozlišení, datové toky, informace o DRM a role pro přístupnost
- Umožňuje efektivní doručování segmentů založené na HTTP pomocí šablon nebo explicitních URL
- Podporuje obsah s více periodami pro reklamy, kapitoly nebo proměnné kódovací parametry

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [MPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpd/)
