---
slug: "adch"
url: "/mobilnisite/slovnik/adch/"
type: "slovnik"
title: "ADCH – Associated Dedicated Channel"
date: 2025-01-01
abbr: "ADCH"
fullName: "Associated Dedicated Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/adch/"
summary: "Associated Dedicated Channel (ADCH) je vyhrazený fyzický kanál v GSM/EDGE Radio Access Network (GERAN), který přenáší datový provoz uživatele, jako je hlas nebo paketová data, ve směru uplink nebo dow"
---

ADCH je vyhrazený fyzický kanál v GERAN, který je dynamicky přidělován pro přenos hlasového nebo paketového datového provozu konkrétního uživatele v obou směrech, aby zajistil spolehlivou službu s nízkou latencí.

## Popis

Associated Dedicated Channel (ADCH) je základní koncept v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), specificky definovaný ve specifikacích 3GPP pro správu vyhrazených rádiových prostředků. Funguje na fyzické vrstvě a nižších protokolových vrstvách rádiového rozhraní a poskytuje obousměrný bod-bod kanál mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)). ADCH je zřizován během sestavování hovoru nebo inicializace datové relace po signalizačních procedurách na společných řídicích kanálech a je charakteristický svým výhradním přidělením jednomu uživateli po dobu trvání relace. Kanál podporuje jak okruhově spínaný provoz, jako je hlas s plnou nebo rozšířenou plnou rychlostí, tak paketově spínaná data prostřednictvím technologií jako General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) nebo Enhanced Data rates for GSM Evolution (EDGE).

Z architektonického hlediska je ADCH součástí rodiny vyhrazených kanálů ([DCH](/mobilnisite/slovnik/dch/)) a je úzce propojen s vyhrazeným řídicím kanálem, typicky Slow Associated Control Channel ([SACCH](/mobilnisite/slovnik/sacch/)) nebo Fast Associated Control Channel ([FACCH](/mobilnisite/slovnik/facch/)), který zpracovává signalizaci během hovoru, řízení výkonu a informace o časovém předstihu. Samotný ADCH přenáší uživatelskou datovou část (user plane payload) a jeho fyzická implementace závisí na schématu mnohonásobného přístupu: v systémech s časovým dělením (TDMA) zabírá konkrétní časové sloty a kmitočtové nosiče, zatímco modulační a kódovací schémata se přizpůsobují na základě rádiových podmínek a požadavků služby. Například v nasazeních EDGE může ADCH používat modulace vyššího řádu, jako je 8-PSK, pro zvýšení datového propustnosti, což je dynamicky upravováno prostřednictvím mechanismů adaptace spoje.

Klíčové komponenty zapojené do provozu ADCH zahrnují Mobilní stanici (MS), která vysílá a přijímá na přiděleném kanálu; BTS, která spravuje rádiový přenos a příjem; a Řadič základnové stanice (BSC), který zajišťuje přiřazování kanálů, rozhodování o předávání hovoru a správu prostředků. ADCH funguje tak, že využívá přiřazené časové sloty v rámci TDMA rámců, přičemž každý rámec je strukturován do burstů nesoucích zakódovaná uživatelská data. Uplink a downlink přenosy jsou odděleny frekvenčním duplexem (FDD) nebo, v některých konfiguracích, časovým duplexem (TDD). Kanál podporuje různá schémata kódování kanálu, prokládání a šifrování pro zajištění integrity a bezpečnosti dat, přičemž pro hlas se často používají adaptivní vícerychlostní (AMR) kodeky pro optimalizaci využití šířky pásma.

V širším kontextu sítě hraje ADCH klíčovou roli při udržování kontinuity a kvality služby. Během aktivních relací síť průběžně monitoruje kvalitu kanálu prostřednictvím měření hlášených na přidružených řídicích kanálech, což umožňuje funkce jako řízení výkonu, předávání hovoru a přepřiřazení kanálu pro zmírnění rušení nebo útlumu. Pro služby paketových dat může být ADCH dočasně přidělen během fází přenosu dat ve spojení s paketovými datovými kanály (PDCH), přičemž prostředky jsou během nečinných období uvolňovány pro úsporu kapacity. Toto dynamické přidělování je v souladu s principem statistického multiplexování a zvyšuje celkovou spektrální účinnost v systémech GERAN.

## K čemu slouží

Associated Dedicated Channel (ADCH) byl zaveden, aby řešil potřebu efektivního řízení vyhrazených rádiových prostředků v sítích GSM pro služby v reálném čase a datové služby. Před jeho formalizací se rané systémy GSM spoléhaly na základní přidělování hovorových kanálů bez strukturovaného propojení s řídicí signalizací, což mohlo vést k neoptimálnímu výkonu při obsluze hlasových hovorů a nových datových aplikací. Koncept ADCH poskytl standardizovaný rámec pro zajištění spolehlivých spojení s nízkou latencí tím, že vyhradil fyzické prostředky jednotlivým uživatelům, čímž řešil problémy jako nekonzistentní kvalita hlasu, omezená datová propustnost a neefektivní využití spektra v dynamickém rádiovém prostředí.

Historicky, jak se GSM vyvíjelo z hlasově orientovaného systému na podporu paketově spínaných dat s GPRS a EDGE, se ADCH stal nezbytným pro správu smíšených typů provozu. Řešil omezení sdílených kanálů, které mohly trpět kolizemi a proměnlivou latencí, tím, že nabízel garantovanou šířku pásma pro kritické služby. Motivací pro jeho vytvoření byla rostoucí poptávka po mobilních datech a vylepšených hlasových službách, která vyžadovala mechanismus kanálu schopný přizpůsobit se různým podmínkám zatížení při zachování přísných parametrů kvality služby (QoS). Díky integraci s přidruženými řídicími kanály umožnil ADCH pokročilé síťové funkce, jako je plynulé předávání hovoru, řízení výkonu a adaptace spoje, které byly klíčové pro mobilitu uživatele a optimalizaci kapacity sítě.

Dále ADCH podporoval přechod k plně IP sítím tím, že usnadňoval efektivní přenos paketových dat vedle tradičního okruhově spínaného hlasu. Řešil problém fragmentace prostředků tím, že umožňoval dynamické přidělování a uvolňování na základě požadavků relace, na rozdíl od statického přiřazování kanálů, které plýtvalo kapacitou. Tato flexibilita byla obzvláště důležitá pro operátory usilující o maximalizaci výnosů z omezených rádiových prostředků při současné podpoře různorodých aplikací, od hlasových hovorů po mobilní přístup k internetu, v rámci omezení technologií 2G a 2.5G.

## Klíčové vlastnosti

- Vyhrazený bod-bod kanál pro exkluzivní přidělení uživatelské relace
- Podpora jak okruhově spínaného hlasového, tak paketově spínaného datového provozu
- Dynamické přiřazování a uvolňování prostředků na základě aktivity relace
- Integrace s přidruženými řídicími kanály (např. SACCH, FACCH) pro signalizaci během hovoru
- Adaptivní modulační a kódovací schémata, včetně vylepšení EDGE
- Správa kvality služby (QoS) prostřednictvím podpory řízení výkonu a předávání hovoru

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [ADCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/adch/)
