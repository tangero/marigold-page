---
slug: "fep"
url: "/mobilnisite/slovnik/fep/"
type: "slovnik"
title: "FEP – Frame Error Probability"
date: 2025-01-01
abbr: "FEP"
fullName: "Frame Error Probability"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fep/"
summary: "Frame Error Probability (FEP, pravděpodobnost chyby rámce) je statistická míra používaná v 3GPP ke kvantifikaci pravděpodobnosti, že přenášený datový rámec bude přijat s chybami. Je to klíčový ukazate"
---

FEP je statistická míra, která kvantifikuje pravděpodobnost, že přenášený datový rámec bude přijat s chybami, a slouží jako klíčový ukazatel výkonu pro spolehlivost na úrovni spojení v mobilních sítích.

## Popis

Frame Error Probability (FEP, pravděpodobnost chyby rámce) je základní metrika definovaná ve specifikacích 3GPP, primárně pro technologie GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Představuje pravděpodobnost, že přenášený rámec bude přijat s chybami, které nelze opravit mechanismy detekce chyb přijímače. Tato pravděpodobnost se vypočítává na základě podmínek kanálu, použitého schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) a výkonu zpracování fyzické vrstvy. FEP není přímo měřená chybovost, ale predikovaná nebo modelovaná pravděpodobnost odvozená z poměru signálu k šumu (SNR) nebo poměru nosná/interference ([C/I](/mobilnisite/slovnik/c-i/)) a z výkonnostních charakteristik kanálového kódování a modulace.

V provozu síť využívá FEP k přijímání klíčových rozhodnutí týkajících se adaptace spojení a řízení výkonu. Například Base Station System ([BSS](/mobilnisite/slovnik/bss/)) může odhadnout FEP pro danou mobilní stanici na základě hlášení o kvalitě kanálu. Pokud odhadnuté FEP překročí určitou prahovou hodnotu, což signalizuje špatnou kvalitu spojení, systém může přepnout na robustnější (avšak s nižší propustností) schéma modulace a kódování nebo zvýšit vysílací výkon pro zlepšení spolehlivosti. Naopak, je-li FEP velmi nízké, což signalizuje výborné podmínky, systém může použít modulaci vyššího řádu pro zvýšení datových rychlostí.

Specifikace 45.903, která FEP podrobně popisuje, stanovuje požadavky na výkon a testovací podmínky pro GSM/EDGE. Definuje referenční úrovně citlivosti a scénáře interference, za kterých FEP nesmí překročit stanovené hodnoty. Tím je zajištěna interoperabilita a základní úroveň výkonu pro uživatelské zařízení (UE) a síťovou infrastrukturu. FEP je úzce spojeno s kvalitou služeb (QoS), kterou zažívá koncový uživatel, protože vysoké FEP vede k retransmisím, zvýšené latenci a snížené efektivní propustnosti. Přesné modelování a řízení FEP je proto klíčové pro efektivní správu rádiových zdrojů a udržení uspokojivého uživatelského zážitku v sítích 2G/2.5G.

## K čemu slouží

Metrika Frame Error Probability byla zavedena, aby poskytla standardizovaný pravděpodobnostní rámec pro hodnocení a zaručení spolehlivosti rádiového spoje v sítích GSM a [EDGE](/mobilnisite/slovnik/edge/). Před jejím formálním definováním v 3GPP byl výkon systému často hodnocen pomocí ad-hoc metrik nebo měřených chybovostí ([FER](/mobilnisite/slovnik/fer/)). FEP poskytuje prediktivní model, který síti umožňuje proaktivně spravovat spojení ještě před výskytem chyb, což je klíčové pro optimalizaci spektrální účinnosti a využití výkonu. Reaguje na potřebu konzistentního výkonnostního kritéria, vůči kterému lze všechna zařízení testovat a certifikovat.

Její vytvoření bylo motivováno vývojem směrem k paketově orientovaným datovým službám s EDGE, kde se dynamická adaptace spojení stala klíčovou. Jednoduchý test vyhovuje/nevyhovuje založený na pevné úrovni signálu byl pro proměnlivé podmínky mobilního rádiového kanálu nedostatečný. FEP umožňuje specifikovat výkon v řadě podmínek interference a útlumu, čímž zajišťuje, že zařízení spolehlivě fungují v reálných scénářích. Řeší problém definice 'jak dobré je dostatečně dobré' pro citlivost přijímače a potlačení interference kvantifikovatelným a opakovatelným způsobem, který je základem pro plánování sítě, návrh zařízení a optimalizaci výkonu.

## Klíčové vlastnosti

- Pravděpodobnostní výkonnostní metrika pro spolehlivost přenosu rámců
- Používá se jako klíčový vstup pro algoritmy adaptace spojení v GERAN
- Definována za specifických referenčních podmínek interference a citlivosti v 45.903
- Podporuje hodnocení různých modulačních schémat (GMSK, 8-PSK)
- Základní pro stanovení požadavků na výkon přijímače
- Umožňuje prediktivní správu rádiových zdrojů oproti reaktivní korekci

## Související pojmy

- [FER – Frame Erasure Rate / Frame Error Rate](/mobilnisite/slovnik/fer/)
- [BER – Basic Encoding Rules](/mobilnisite/slovnik/ber/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks

---

📖 **Anglický originál a plná specifikace:** [FEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/fep/)
