---
slug: "ebu-tt"
url: "/mobilnisite/slovnik/ebu-tt/"
type: "slovnik"
title: "EBU-TT – European Broadcasting Union Timed Text"
date: 2025-01-01
abbr: "EBU-TT"
fullName: "European Broadcasting Union Timed Text"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ebu-tt/"
summary: "EBU-TT je standardizovaný XML formát pro reprezentaci titulků a skrytých titulků, referencovaný 3GPP pro distribuci přes mobilní vysílání (eMBMS) a unicastové streamy. Poskytuje přesné časování, styly"
---

EBU-TT je standardizovaný formát titulků založený na XML, který je v 3GPP referencován pro distribuci videa do mobilních zařízení a poskytuje přesné časování, styly a pozicování pro profesionální a přístupné titulky.

## Popis

European Broadcasting Union Timed Text (EBU-TT) je rodina formátů titulků založených na [XML](/mobilnisite/slovnik/xml/), standardizovaná organizací [EBU](/mobilnisite/slovnik/ebu/). V rámci 3GPP jsou referencovány specifické profily, jako je EBU-TT-D (pro distribuci, např. v TS 26.953), pro přenos v rámci multimediálních vysílacích a streamovacích služeb. Definuje, jak jsou dokumenty s titulky strukturovány, časovány a stylovány pomocí XML schémat a přidružených stylovacích jazyků jako [CSS](/mobilnisite/slovnik/css/). Typický EBU-TT dokument obsahuje sekvenci textových elementů, každý s přesným počátečním a koncovým časem, vlastnostmi formátování (font, barva, pozadí) a informacemi o rozložení určujícími, kde se má text na obrazovce zobrazit.

Formát funguje na principu oddělení obsahu (text a jeho časování) od prezentace (stylování a rozložení). Toto oddělení umožňuje flexibilní vykreslování na různých zařízeních a velikostech obrazovek při zachování záměru autora. V kontextu distribuce 3GPP, jako je eMBMS vysílání nebo [DASH](/mobilnisite/slovnik/dash/) streamovací relace, je EBU-TT dokument zabalen jako samostatná mediální komponenta spolu s videem a audiem. Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) v DASH nebo File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)) relace v eMBMS signalizuje dostupnost a časování této titulkové komponenty, což klientovi umožňuje ji stáhnout a synchronizovat s přehráváním hlavního média.

Klíčové komponenty EBU-TT dokumentu zahrnují kořenový element `<tt>`, `<head>` pro metadata a definice stylů a `<body>` obsahující elementy `<div>` a `<p>`, které nesou vlastní textové stopy s atributy `begin` a `end`. Stylování je definováno pomocí elementů `<styling>` s odkazy na ID stylů. Pro mobilní distribuci je optimalizován profil EBU-TT-D, který využívá podmnožinu funkcí pro snížení složitosti a velikosti souboru při zachování základní funkcionality. Specifikace 3GPP přesně definují, jak jsou tyto XML dokumenty zapouzdřeny, například v [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Streamech pro vysílání nebo jako segmenty v DASH, což zajišťuje spolehlivou a synchronizovanou distribuci do uživatelského zařízení.

## K čemu slouží

EBU-TT byl vytvořen jako náhrada starších, méně flexibilních formátů titulků (jako [EBU](/mobilnisite/slovnik/ebu/) STL) za moderní, XML standard podporující bohaté stylování, přesné časování a lepší interoperabilitu. Jeho přijetí do 3GPP bylo motivováno potřebou distribuovat vysílací kvalitu videa a přístupné video služby přes sítě LTE a 5G. Předchozí metody mobilního titulkování byly často proprietární, založené na bitmapách nebo používaly jednoduchý text s omezeným formátováním, což bylo nedostatečné pro profesionální obsah a zákonné požadavky na přístupnost.

Primární problém, který EBU-TT v kontextu 3GPP řeší, je poskytnutí jednotného, standardizovaného formátu pro titulky, který funguje napříč tradičním vysíláním i IP mobilní distribucí. To umožňuje poskytovatelům obsahu vytvářet titulky jednou a používat je pro služby DVB-T, DVB-IPTV a 3GPP eMBMS/DASH, což výrazně snižuje provozní náklady. Řeší omezení dřívějších metod přenosu titulků v 3GPP, kterým chyběla sofistikovanost potřebná pro komplexní vícejazyčné titulkování, efekty ve stylu karaoke nebo přesné pozicování pro zabránění překrytí důležitého vizuálního obsahu.

Jeho XML povaha navíc zajišťuje strojovou čitelnost a snadnou transformovatelnost, což podporuje dynamickou adaptaci pro různé velikosti obrazovek a uživatelské preference (např. změna velikosti písma nebo barvy pro uživatele se zrakovým postižením). Tím, že specifikace jako TS 26.953 nařizují použití EBU-TT-D, 3GPP zajišťuje, že všechna kompatibilní zařízení dokážou vykreslovat titulky vysoké kvality, čímž plní regulatorní požadavky na mediální přístupnost a zlepšují uživatelský zážitek při sledování živého sportu, zpráv a zábavy na mobilních zařízeních.

## Klíčové vlastnosti

- Formát založený na XML umožňující bohaté stylování textu a rozložení
- Přesná synchronizace pomocí odkazů na časovou osu média
- Oddělení obsahu (text/časování) a prezentace (stylování)
- Podpora více jazyků a komplexního formátování stop
- Optimalizovaný profil EBU-TT-D pro efektivní distribuci
- Navrženo pro přenos v MPEG-2 TS a DASH/CMAF streamingu

## Související pojmy

- [EBU – European Broadcasting Union](/mobilnisite/slovnik/ebu/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [CMAF – Common Media Application Format](/mobilnisite/slovnik/cmaf/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [EBU-TT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ebu-tt/)
