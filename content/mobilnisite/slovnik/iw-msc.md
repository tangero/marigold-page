---
slug: "iw-msc"
url: "/mobilnisite/slovnik/iw-msc/"
type: "slovnik"
title: "IW-MSC – Interworking MSC"
date: 2025-01-01
abbr: "IW-MSC"
fullName: "Interworking MSC"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iw-msc/"
summary: "Interworking MSC (IW-MSC) je funkční entita, která zajišťuje signalizační propojení mezi jádrovou sítí s přepojováním okruhů (CS) 3GPP a externí IP sítí, jako je IMS nebo síť pro SIP trunking. Překlád"
---

IW-MSC je funkční entita, která zajišťuje signalizační propojení mezi jádrem s přepojováním okruhů (CS) 3GPP a externí IP sítí prostřednictvím překladu mezi protokoly ISUP/BICC a SIP.

## Popis

Interworking [MSC](/mobilnisite/slovnik/msc/) (IW-MSC) je specializovaná funkce mobilní ústředny definovaná 3GPP, především v TS 29.235, která zajišťuje signalizační propojení na řídicí rovině mezi starší telefonní sítí s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) a IP sítěmi. Na rozdíl od [IW-MGW](/mobilnisite/slovnik/iw-mgw/), která zpracovává média, se IW-MSC zaměřuje na překlad signalizace pro řízení hovorů. Funguje jako signalizační brána a převodník protokolů, stojící na hranici mezi doménou CS (používající signalizační protokoly jako [ISDN](/mobilnisite/slovnik/isdn/) User Part – [ISUP](/mobilnisite/slovnik/isup/) nebo Bearer Independent Call Control – BICC) a IP doménou, jako je IMS nebo podniková SIP síť (používající protokol Session Initiation Protocol – SIP).

Z architektonického hlediska může být IW-MSC implementována jako samostatný uzel nebo integrovaná s jinými funkcemi, jako je Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)). Jejím jádrovým úkolem je přijmout příchozí požadavek na sestavení hovoru v jednom protokolu, interpretovat parametry hovoru (volané/volající číslo, indikátory služeb) a namapovat je pro sestavení ekvivalentního odchozího požadavku v cílovém protokolu. Například při propojení z CS do IMS přijme zprávu ISUP Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)), namapuje volané číslo na SIP URI a vygeneruje požadavek SIP INVITE směrem k jádru IMS. Spravuje celý signalizační dialog a překládá následné zprávy jako [ACM](/mobilnisite/slovnik/acm/) (Address Complete), ANM (Answer) a REL (Release) na jejich SIP ekvivalenty (180 Ringing, 200 OK, BYE).

IW-MSC také zajišťuje kritické propojení doplňkových služeb, překládá mezi signalizací doplňkových služeb v CS (pomocí zpráv Facility) a metodami založenými na SIP. Je zodpovědná za adaptaci formátu čísel, screening a rozhodování o směrování na základě scénáře propojení. V typickém nasazení pro operátora migrujícího na IMS umožňuje IW-MSC (často ve spojení s MGCF pro úplnou kontrolu MGW) starším MSC v síti směrovat hovory určené pro účastníky v IMS transparentně, přičemž IW-MSC je z pohledu CS sítě vnímána jako další MSC. To umožňuje postupnou migraci, kde se IMS jeví starší infrastruktuře jako virtuální ústředna CS.

## K čemu slouží

IW-MSC byla vyvinuta k vyřešení problému signalizační interoperability, který doprovází problém uživatelské roviny řešený IW-MGW. Když operátoři začali nasazovat IMS a další sítě založené na SIP, potřebovali způsob, jak jejich stávající rozsáhlá signalizační infrastruktura CS sítí (založená na SS7 ISUP) mohla komunikovat s novým světem IP signalizace (SIP). Bez toho by nebylo možné mezi doménami navázat řízení hovoru, i kdyby bylo možné vytvořit přenosovou cestu pro média. IW-MSC poskytuje nezbytnou vrstvu pro překlad protokolů, která umožňuje sestavení, ukončení a aktivaci služeb hovorů napříč hranicí sítě.

Její vznik byl motivován stejnou strategií postupného přechodu jako u IW-MGW. Umožnila plánovačům sítí zavádět do své sítě ostrovy IMS, aniž by museli okamžitě nahradit všechny starší MSC a přepínače. IW-MSC funguje jako brána, díky níž se síť IMS jeví ze strany starší sítě jako tradiční ústředna CS a naopak. Tím se vyřešilo významné omezení a vysoká cena „kompletní“ výměny. Konkrétně řešila problémy jako směrování hovorů k účastníkům, kteří byli převedeni na VoIP služby založené na IMS, umožnění podnikových trunkingových spojení mezi podnikovým SIP PBX a mobilní sítí a usnadnění propojení s dalšími operátory, kteří byli v různých fázích modernizace své sítě.

## Klíčové vlastnosti

- Překlad signalizačních protokolů mezi ISUP/BICC a SIP
- Mapování parametrů hovoru (např. E.164 čísel na SIP URI)
- Propojení pro základní sekvence řízení hovoru (sestavení, vyzvánění, odpověď, uvolnění)
- Podpora propojení doplňkových služeb (např. přesměrování hovoru, CLI)
- Směrovací funkce založená na analýze cíle a pravidlech propojení
- Integrace s MGCF pro koordinovanou kontrolu mediální brány (MGW) ve scénářích IMS

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [ISC – IP multimedia subsystem Service Control interface](/mobilnisite/slovnik/isc/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [IW-MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/iw-msc/)
