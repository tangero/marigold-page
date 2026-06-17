---
slug: "imsc"
url: "/mobilnisite/slovnik/imsc/"
type: "slovnik"
title: "IMSC – Internet Media Subtitles and Captions"
date: 2025-01-01
abbr: "IMSC"
fullName: "Internet Media Subtitles and Captions"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imsc/"
summary: "IMSC je formát standardizovaný 3GPP pro doručování časovaných textových titulků a skrytých titulků v multimediálních službách přes IP sítě. Je založen na W3C TTML a zajišťuje přesnou synchronizaci, st"
---

IMSC je formát standardizovaný 3GPP a založený na W3C TTML pro přenos časovaných textových titulků a skrytých titulků přes IP sítě, zajišťující přesnou synchronizaci a stylování pro zpřístupnění a vícejazyčnou podporu ve streamovacích a vysílacích službách.

## Popis

IMSC (Internet Media Subtitles and Captions) je profil jazyka W3C Timed Text Markup Language (TTML) standardizovaný 3GPP pro přenos titulků, skrytých titulků a dalšího časovaného textu v multimediálních službách. Definuje omezenou sadu funkcí TTML pro zajištění interoperability, efektivního zpracování a spolehlivého zobrazování na různých zařízeních a sítích. Dokumenty IMSC jsou založeny na XML a popisují sekvence textu s přesným načasováním, pozicováním, stylováním (font, barva) a volitelnými animačními efekty, synchronizované s přidruženým zvukovým nebo obrazovým médiem. Specifikace pokrývá jak IMSC1, což je profil pouze pro text, tak podporu pokročilejších funkcí v pozdějších verzích.

Technicky IMSC funguje tak, že zapouzdřuje data titulků založená na TTML do mediálních kontejnerů nebo je doručuje jako samostatnou časovanou textovou stopu spolu s video a audio streamy v adaptivním streamování (např. [DASH](/mobilnisite/slovnik/dash/)). V typickém nasazení mediální server zahrnuje dokumenty IMSC jako jednu z reprezentačních alternativ v [MPD](/mobilnisite/slovnik/mpd/) (Media Presentation Description). Klient přehrávače na základě systémových schopností a uživatelského výběru načte a zpracuje dokument IMSC a vykreslí textové překryvy v určených časech a s definovanými styly. Vykreslovací engine musí podporovat požadované funkce profilu IMSC, jako je rozložení na základě regionů, vložené stylování a načasování obsahu vyjádřené v SMPTE časových kódech nebo na časových osách média.

V síťové architektuře je IMSC klíčovou součástí vrstvy pro doručování médií, konkrétně v rámci paketově spínané streamovací služby (PSS) a multimediální vysílací služby ([MBMS](/mobilnisite/slovnik/mbms/)). Rozhraní má s nástroji pro přípravu obsahu, kódovacími systémy a streamovacími servery. Jeho úlohou je poskytovat standardizovanou, platformně nezávislou metodu pro doručování funkcí zpřístupnění, jako jsou skryté titulky pro sluchově postižené, titulky pro různé jazyky a popisný text pro zrakově postižené. Tím, že je založen na otevřeném webovém standardu (TTML), usnadňuje široké přijetí v odvětví a integraci s mobilními i pevnými streamovacími ekosystémy.

## K čemu slouží

IMSC byl vyvinut, aby vyřešil problém s fragmentovanými proprietárními formáty titulků používanými v raných mobilních a internetových streamovacích službách, které bránily interoperabilitě a zvyšovaly složitost pro poskytovatele obsahu a výrobce zařízení. Cílem bylo vytvořit jednotný, efektivní a funkčně bohatý formát časovaného textu vhodný pro doručování založené na IP, který by umožnil zpřístupnění a vícejazyčnou podporu vyžadovanou předpisy v mnoha regionech. Jeho vytvoření bylo motivováno růstem spotřeby mobilního videa a potřebou standardu, který by mohl fungovat napříč streamovacími (PSS, [MBMS](/mobilnisite/slovnik/mbms/)) a vysílacími systémy definovanými 3GPP.

Před IMSC byla řešení často založena na bitmapových titulcích (které nejsou škálovatelné ani prohledávatelné) nebo jednoduchých textových formátech s omezeným stylováním a přesností načasování. IMSC, díky profilování TTML, využívá sílu XML k poskytnutí bohatého formátování textu, přesné synchronizace a schopností komplexního rozložení při zachování zvládnutelné velikosti souborů. Řeší požadavky na doručování titulků v náročných prostředích, jako jsou mobilní sítě s proměnlivou šířkou pásma, a zajišťuje, že text může být doručován jako samostatný adaptivní stream. To umožňuje uživatelům zapnout nebo vypnout titulky bez ovlivnění hlavního mediálního streamu a podporuje dynamickou adaptaci na síťové podmínky.

## Klíčové vlastnosti

- Profil TTML založený na XML pro strukturovaný časovaný text
- Přesná časová synchronizace využívající časové osy média
- Bohaté stylování textu (fonty, barvy, obrysy, pozadí)
- Podpora více jazyků a metadat pro zpřístupnění
- Efektivní doručování jako samostatná stopa v adaptivním streamování (DASH)
- Interoperabilita napříč zařízeními, platformami a službami

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 23.892** (Rel-8) — IMS Centralized Services Control
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats

---

📖 **Anglický originál a plná specifikace:** [IMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/imsc/)
