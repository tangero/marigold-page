---
slug: "rwp"
url: "/mobilnisite/slovnik/rwp/"
type: "slovnik"
title: "RWP – Region-Wise Packing"
date: 2025-01-01
abbr: "RWP"
fullName: "Region-Wise Packing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rwp/"
summary: "Region-Wise Packing je technika kódování a doručování videa pro multimediální služby. Rozděluje snímek videa na prostorové oblasti a efektivně je zabalí pro přenos, čímž optimalizuje využití šířky pás"
---

RWP je technika kódování videa, která rozděluje snímek na prostorové oblasti a efektivně je zabalí pro přenos za účelem optimalizace šířky pásma a umožnění streamování oblasti zájmu.

## Popis

Region-Wise Packing (RWP) je sofistikovaný mechanismus zpracování videa definovaný v rámci Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a Media Streaming ve specifikacích 3GPP. Funguje na pomezí kódování videa a síťového doručování a je speciálně navržen pro pokročilé videoformáty, jako je omnidirekční média (360stupňové video). Základním architektonickým principem je rozdělení snímku videa, typicky projekce sférického pohledu, na více obdélníkových oblastí, z nichž každá představuje odlišnou prostorovou část celé panoramy. Tyto oblasti jsou následně nezávisle zakódovány, často s různou úrovní kvality, a 'zabaleny' do jediného video bitstreamu odpovídajícího standardu, například [HEVC](/mobilnisite/slovnik/hevc/) bitstreamu založeného na dlaždicích (tiles). Tento proces balení je řízen metadaty, která popisují prostorovou polohu a uspořádání každé oblasti v rámci celkového plátna snímku.

Z pohledu sítě RWP umožňuje vysoce efektivní doručování. Namísto přenosu celého vysokorozlišujícího omnidirekčního video streamu na uživatelské zařízení může síť využít tuto strukturu. Klientská aplikace, která zná aktuální zorné pole (viewport) uživatele, může požadovat pouze konkrétní zabalené oblasti potřebné k vykreslení tohoto viewportu ve vysoké kvalitě, zatímco ostatní oblasti mohou být doručeny v nižší kvalitě nebo vůbec. To je umožněno protokoly jako Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), kde Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) obsahuje metadata RWP, což klientovi umožňuje mapovat požadované prostorové segmenty na odpovídající datové segmenty v bitstreamu.

Úlohou RWP v síti je umožnit přenos pásmově efektivních immersivních mediálních služeb. Nachází se na aplikační vrstvě a ovlivňuje činnost mediálního kodéru, generátoru manifest souborů a adaptivního streamovacího klienta. Oddělením prostorové organizace video obsahu od jeho kódování a přenosu poskytuje RWP základní strukturu pro viewport-adaptivní streamování, což je klíčové pro doručování kvalitního [VR](/mobilnisite/slovnik/vr/) a 360stupňového videa přes rádiové přístupové sítě s omezenou kapacitou. Transformuje monolitický video obsah na strukturovaný, prostorově informovaný obsah, se kterým mohou síť a klient inteligentně interagovat.

## K čemu slouží

Region-Wise Packing byl vytvořen k řešení významné výzvy v podobě šířky pásma při streamování immersivních médií, zejména 360stupňového a virtuálně-reálného videa. Tradiční video streamování přenáší celý snímek pro každý video segment, což je u omnidirekčního obsahu velmi neefektivní, protože uživatel typicky sleduje pouze část (např. 90–120 stupňů) z celé sféry 360x180 stupňů v daný okamžik. Přenos celé sféry ve vysokém rozlišení by spotřebovával nadměrné síťové zdroje a vedl by ke špatnému uživatelskému zážitku kvůli bufferingu nebo snížené kvalitě.

Historický kontext vývoje RWP spočívá v normalizaci 5G multimediálních služeb ve 3GPP Release 15 a novějších, kde byly klíčovými hnacími silami enhanced Mobile Broadband (eMBB) a mediální služby. Předchozí přístupy buď streamovaly celé monoskopické či stereoskopické video (plýtvavé), nebo vyžadovaly komplexní vykreslování viewportu na straně serveru a vyhrazené unicast streamy (neškálovatelné). RWP poskytuje standardizované střední řešení. Podněcuje posun směrem k klientem řízenému adaptivnímu modelu tím, že strukturování obsahu provádí již u zdroje. Tím řeší problém tím, že umožňuje síti doručovat jediný strukturovaný bitstream, který může být efektivně spotřebován více klienty s různými viewporty, čímž vyvažuje úspory šířky pásma s flexibilitou výběru viewportu na straně klienta.

## Klíčové vlastnosti

- Prostorové rozdělení video snímků na nezávisle přístupné oblasti
- Zabalení více zakódovaných oblastí do jediného standardům odpovídajícího video bitstreamu (např. HEVC dlaždice/tiles)
- Generování standardizovaných metadat popisujících umístění oblastí a strukturu balení
- Umožňuje viewport-adaptivní streamování pro omnidirekční média
- Úspora šířky pásma díky možnosti selektivního vyžádání a doručení oblastí ve vysoké kvalitě
- Kompatibilita s MPEG-DASH pro dynamickou adaptaci na základě viewportu a síťových podmínek

## Související pojmy

- [OMAF – Omnidirectional Media Application Format](/mobilnisite/slovnik/omaf/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines

---

📖 **Anglický originál a plná specifikace:** [RWP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rwp/)
