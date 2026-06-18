---
slug: "tmu"
url: "/mobilnisite/slovnik/tmu/"
type: "slovnik"
title: "TMU – Transmission Medium Used"
date: 2025-01-01
abbr: "TMU"
fullName: "Transmission Medium Used"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tmu/"
summary: "Parametr definovaný v 3GPP TS 29.163, který udává typ použitého přenosového média (např. IP, ATM) pro konkrétní přenosový kanál nebo datový tok v rámci IP Multimedia Subsystem (IMS). Je klíčový pro úč"
---

TMU je parametr, který udává typ použitého přenosového média, například IP nebo ATM, pro konkrétní přenosový kanál (bearer) nebo datový tok v rámci IMS, a umožňuje tak účtování a řízení politik na úrovni přenosového kanálu.

## Popis

Transmission Medium Used (TMU) je standardizovaný parametr v architektuře IMS dle 3GPP, podrobně specifikovaný v technické specifikaci 29.163. Funguje jako atribut nebo informační prvek, který je komunikován mezi síťovými funkcemi, primárně mezi Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) a online charging systémy. Hodnota TMU explicitně identifikuje podkladovou transportní technologii přenášející uživatelská data pro konkrétní [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) přenosový kanál nebo služební datový tok. Tato identifikace je pro síť zásadní, aby mohla uplatnit správné tarify účtování a pravidla politik, které jsou specifické pro náklady a charakteristiky přenosového média.

Během provozu, když je přenosový kanál zřízen nebo modifikován, síťový prvek zodpovědný za vynucení (např. Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) fungující jako PCEF) může nahlásit TMU funkci PCRF. PCRF tuto informaci následně využívá jako součást svého rozhodovacího procesu pro výběr a zřízení odpovídajících pravidel Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Například, pravidlo pro video stream přenášený přes vyhrazené, vysokokvalitní přenosové médium jako [ATM](/mobilnisite/slovnik/atm/) může mít jiné parametry QoS a účtovací tarify ve srovnání se stejnou službou přenášenou přes best-effort IP transport. Parametr TMU tedy poskytuje potřebnou granularitu pro mapování vysokorychlostních servisních politik na konkrétní technologickou implementaci přenosového kanálu.

Z architektonického hlediska je TMU klíčovou součástí odděleného rámce pro účtování a řízení politik v moderních sítích 3GPP. Nachází se na průsečíku povědomí o službě a povědomí o transportu. Zatímco jádro IMS zpracovává signalizaci a servisní logiku na úrovni session, TMU poskytuje spojení s charakteristikami fyzické a linkové vrstvy v bearer rovině. To operátorům umožňuje implementovat sofistikované obchodní modely, jako je nabídka prémiových QoS garancí na specifických transportních sítích (např. pronajatá linka) s odpovídající prémiovou cenou, zatímco pro best-effort služby používají standardní IP transport. Jeho role, byť se může zdát technická, je zásadní pro umožnění přesné, na transportu založené monetizace síťových služeb.

## K čemu slouží

TMU byl zaveden, aby řešil potřebu povědomí o transportní vrstvě v účtování a řízení politik IMS. Rané mobilní datové sítě často používaly jediný typ transportu (např. [GPRS](/mobilnisite/slovnik/gprs/) přes IP), ale jak se sítě vyvíjely, operátoři začali v rámci stejné síťové infrastruktury využívat více transportních technologií (jako ATM pro vysoce spolehlivou backhaul přenosovou část a IP pro obecná data). Obecné pravidlo pro účtování nebo politiku mezi nimi nedokázalo rozlišovat, což vedlo k potenciálním únikům výnosů nebo nesprávné aplikaci QoS. Například, drahý ATM okruh se zaručenou přenosovou rychlostí by neměl být účtován stejně jako best-effor IP cesta pro stejnou video službu.

Jeho vytvoření bylo motivováno pohybem průmyslu směrem ke konvergovaným, plně IP sítím, kde je servisní logika (IMS) oddělena od podkladové konektivity. Toto oddělení vyžadovalo standardizovaný mechanismus pro korelaci poskytované služby se specifickými zdroji spotřebovávanými na transportní úrovni. TMU to řeší tím, že poskytuje jasný, standardizovaný identifikátor pro přenosové médium, což umožňuje PCRF činit informovaná rozhodnutí. Zajišťuje, že záznamy o účtování přesně odrážejí náklady na použité podkladové síťové zdroje, a umožňuje tak spravedlivé a podrobné fakturace. To bylo obzvláště důležité pro komercializaci raných služeb založených na IMS, jako je videotelefonie, kde kvalita a náklady na přenosový kanál přímo ovlivňovaly uživatelský zážitek a ziskovost operátora.

## Klíčové vlastnosti

- Standardizovaný identifikátor přenosového média pro PCC rámec
- Umožňuje účtování a fakturační diferenciaci zohledňující transport
- Používán PCRF pro výběr pravidel politik specifických pro médium
- Hlášen PCEF/PGW během zřízení/modifikace přenosového kanálu
- Podporuje různé typy médií (např. IP, ATM, GPRS)
- Nedílný pro přesnou korelaci služebního datového toku s transportem

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [IP-CAN – IP-Connectivity Access Network](/mobilnisite/slovnik/ip-can/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [TMU na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmu/)
