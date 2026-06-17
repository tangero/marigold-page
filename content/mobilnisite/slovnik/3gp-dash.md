---
slug: "3gp-dash"
url: "/mobilnisite/slovnik/3gp-dash/"
type: "slovnik"
title: "3GP-DASH – 3GPP Dynamic Adaptive Streaming over HTTP"
date: 2025-01-01
abbr: "3GP-DASH"
fullName: "3GPP Dynamic Adaptive Streaming over HTTP"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/3gp-dash/"
summary: "3GP-DASH je standardizovaný adaptivní streamovací protokol založený na HTTP pro doručování médií přes sítě 3GPP. Umožňuje plynulé přehrávání videa dynamickým přizpůsobováním kvality mediálních segment"
---

3GP-DASH je standardizovaný adaptivní streamovací protokol založený na HTTP pro doručování médií přes sítě 3GPP, který dynamicky přizpůsobuje kvalitu, aby zajistil plynulé přehrávání videa na mobilních zařízeních.

## Popis

3GP-DASH je komplexní specifikace pro doručování médií, která definuje formáty a protokoly pro adaptivní streamování přes [HTTP](/mobilnisite/slovnik/http/). Architektura je řízena klientem a je založena na manifestním souboru nazvaném Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)). MPD je XML dokument popisující strukturu mediální prezentace, včetně časování, URL adres mediálních segmentů a dostupných alternativních reprezentací (např. různé datové toky, rozlišení a kodeky). Klient neboli [DASH](/mobilnisite/slovnik/dash/) přehrávač je zodpovědný za stažení a zpracování MPD a následně autonomně vybírá a stahuje mediální segmenty z HTTP serveru. Základní operační princip spočívá v tom, že klient sleduje stav své vlastní vyrovnávací paměti a odhaduje dostupnou šířku pásma sítě. Na základě tohoto vyhodnocení v reálném čase vybere další mediální segment z nejvhodnější reprezentace uvedené v MPD, aby se předešlo opětovnému načítání (rebuffering) a zároveň se maximalizovala kvalita přehrávání. Segmenty jsou typicky krátké, nezávislé soubory (např. 2-10 sekund) obsahující mediální data formátovaná podle [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) pro obsah na vyžádání nebo [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Stream (M2TS) pro živé vysílání. Klíčové komponenty zahrnují DASH klienta (mediální přehrávač), HTTP webový server (nebo [CDN](/mobilnisite/slovnik/cdn/)) hostující MPD a mediální segmenty, a samotnou MPD, která funguje jako 'recept' pro prezentaci. V síti 3GPP funguje 3GP-DASH jako služba aplikační vrstvy, typicky doručovaná přes IP Multimedia Subsystem (IMS) nebo přímo přes přenosovou síť. Rozhraní s rámcem Policy and Charging Control (PCC) jádrové sítě může poskytovat klientovi informace o síťové podpoře nebo aplikovat QoS politiky na streamovací relaci. Závislost protokolu na standardním HTTP jej činí kompatibilním s firewally a snadno kešovatelným standardními CDN, což je zásadní pro jeho škálovatelnost pro masové video služby.

## K čemu slouží

3GP-DASH byl vytvořen za účelem standardizace a optimalizace doručování videa přes mobilní sítě a řeší výzvy kolísající šířky pásma a různorodých možností zařízení, které jsou vlastní bezdrátovému prostředí. Před [DASH](/mobilnisite/slovnik/dash/) vytvářely proprietární řešení adaptivního streamování (jako Apple HLS nebo Microsoft Smooth Streaming) fragmentaci, což nutilo poskytovatele obsahu kódovat a ukládat více verzí svých médií pro různá ekosystémy. To zvyšovalo složitost a náklady. Primární motivací bylo vytvořit jediný mezinárodní standard pro adaptivní streamování, který by bezproblémově fungoval na všech zařízeních a sítích, podporoval interoperabilitu a snižoval režii pro poskytovatele služeb. Řeší problém trhání videa a dlouhých dob načítání tím, že umožňuje klientovi během přehrávání dynamicky přepínat mezi různými úrovněmi kvality. Historicky by postupné stahování (progressive download) nebo neadaptivní streamování buď plýtvalo šířkou pásma (pokud by pevný datový tok byl příliš nízký), nebo způsobovalo neustálé přerušení (pokud by byl příliš vysoký pro aktuální spojení). 3GP-DASH dává kontrolu klientovi, aby mohl učinit nejlepší rozhodnutí o kvalitě na základě svého bezprostředního kontextu, což zásadně zlepšuje kvalitu uživatelského prožitku (QoE). Jeho vývoj v rámci 3GPP, počínaje Release 10, byl hnána explozivním růstem mobilního video provozu a potřebou mechanismu doručování, který by byl vědomý sítě, efektivní a mohl být integrován s rámci QoS a správy politik 3GPP.

## Klíčové vlastnosti

- Logika adaptivního datového toku řízená klientem na základě manifestu MPD
- Standardizované XML schéma Media Presentation Description (MPD)
- Podpora formátů segmentů ISO Base Media File Format (ISOBMFF) i MPEG-2 TS
- Integrace s 3GPP Policy and Charging Control (PCC) pro síťovou podporu
- Efektivní kompatibilita s kešováním CDN a HTTP
- Podpora živých prezentací, prezentací na vyžádání a prezentací s posunem času

## Definující specifikace

- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 28.406** (Rel-19) — QoE measurement collection: info definition & transport

---

📖 **Anglický originál a plná specifikace:** [3GP-DASH na 3GPP Explorer](https://3gpp-explorer.com/glossary/3gp-dash/)
