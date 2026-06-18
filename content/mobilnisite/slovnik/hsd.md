---
slug: "hsd"
url: "/mobilnisite/slovnik/hsd/"
type: "slovnik"
title: "HSD – HTTP Streaming and Download"
date: 2025-01-01
abbr: "HSD"
fullName: "HTTP Streaming and Download"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hsd/"
summary: "Standardizační služba 3GPP, která standardizuje doručování multimediálního obsahu přes HTTP. Definuje protokoly pro adaptivní streamování s proměnnou přenosovou rychlostí a progresivní stahování, čímž"
---

HSD je standardizační služba 3GPP, která standardizuje doručování multimediálního obsahu přes HTTP pro adaptivní streamování s proměnnou přenosovou rychlostí a progresivní stahování, čímž zajišťuje efektivní přenos médií v mobilních sítích.

## Popis

[HTTP](/mobilnisite/slovnik/http/) Streaming and Download (HSD) je standardizační služba 3GPP definovaná v dokumentu TS 26.247. Standardizuje doručování multimediálního obsahu pomocí protokolů založených na HTTP, především za účelem podpory adaptivního streamování v mobilních sítích. Architektura je typu klient-server, kde je mediální obsah připraven jako segmentované soubory (např. ve formátech MPEG-DASH nebo 3GPP Adaptive HTTP Streaming) a hostován na běžném HTTP webovém serveru nebo na vyhrazeném streamovacím serveru. Klient, typicky uživatelské zařízení (UE) s aplikací mediálního přehrávače, používá požadavky HTTP GET nebo částečné GET k získání mediálních segmentů a manifestů (jako je [MPD](/mobilnisite/slovnik/mpd/) v [DASH](/mobilnisite/slovnik/dash/)). Klíčovou součástí je adaptační logika na straně klienta, která sleduje stav sítě a vybírá segment s odpovídající přenosovou rychlostí, aby zajistila plynulé přehrávání bez přerušení kvůli načítání.

Technologie funguje tak, že médium rozdělí na malé, nezávisle dekódovatelné segmenty kódované v různých přenosových rychlostech. Manifestový soubor tyto segmenty a jejich vlastnosti popisuje. Klient nejprve získá manifest a poté začne požadovat segmenty. Na základě dostupné propustnosti, stavu vyrovnávací paměti a možností zařízení adaptační engine klienta dynamicky volí přenosovou rychlost následujícího segmentu. To umožňuje, aby se kvalita streamu v reálném čase přizpůsobovala síťovému přetížení nebo zlepšení podmínek, což poskytuje konzistentní uživatelský zážitek. U progresivního stahování je celý soubor stažen přes HTTP, ale přehrávání může začít ještě před dokončením stahování, pokud to formát souboru umožňuje.

Úlohou HSD v síti je služba na aplikační vrstvě, která se nachází nad transportní vrstvou poskytovanou paketovým jádrem (EPC, 5GC). Využívá podkladovou službu IP konektivity. Nedefinuje procedury v rádiové nebo jádrové síti, ale spoléhá na ně pro efektivní doručování IP paketů. Specifikace zajišťuje interoperabilitu mezi nástroji pro přípravu obsahu, servery a klientskými zařízeními od různých výrobců, což bylo klíčové pro růst ekosystému služeb mobilního videa. Integruje se s dalšími službami 3GPP, jako je Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), pro vylepšení rozhlasového doručování.

## K čemu slouží

HSD bylo vytvořeno, aby řešilo rostoucí poptávku po efektivním a spolehlivém doručování videa v mobilních sítích. Před jeho standardizací vedly proprietární streamovací řešení k fragmentaci, vyžadovaly specifické páry klient-server a komplikovaly distribuci obsahu. Hlavním problémem bylo doručování videa přes IP sítě s best-effort službou, které trpí proměnlivou šířkou pásma a latencí, což způsobovalo časté načítání do vyrovnávací paměti a špatnou uživatelskou zkušenost ([QoE](/mobilnisite/slovnik/qoe/)).

Motivací bylo využít všudypřítomný protokol [HTTP](/mobilnisite/slovnik/http/), který na rozdíl od specializovaných streamovacích protokolů (např. [RTSP](/mobilnisite/slovnik/rtsp/)) snadno prochází firewally a překladem síťových adres ([NAT](/mobilnisite/slovnik/nat/)). Standardizace adaptivního přístupu založeného na HTTP umožnila klientům přizpůsobovat kvalitu videa na základě aktuálních síťových podmínek, což byl významný pokrok oproti streamování s pevnou přenosovou rychlostí. Toto bylo zavedeno ve vydání 10, což časově odpovídalo nástupu chytrých telefonů a růstu spotřeby mobilních dat. Řešilo to omezení dřívějšího paketového streamování 3GPP (PSS), které bylo složitější a méně adaptivní, a poskytlo tak internetu přátelské a škálovatelné řešení pro služby videa na vyžádání a živého streamování.

## Klíčové vlastnosti

- Standardizované adaptivní streamování s proměnnou přenosovou rychlostí využívající HTTP/1.1
- Podpora profilů MPEG-DASH a 3GPP Adaptive HTTP Streaming (AHS)
- Adaptace kvality řízená klientem na základě síťových metrik a stavu vyrovnávací paměti
- Použití manifestových souborů (Media Presentation Description) pro popis obsahu
- Podpora režimů služeb videa na vyžádání i živého streamování
- Možnosti integrace s mechanismy QoS a rozhlasového přenosu (MBMS) 3GPP

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)

## Definující specifikace

- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP

---

📖 **Anglický originál a plná specifikace:** [HSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsd/)
