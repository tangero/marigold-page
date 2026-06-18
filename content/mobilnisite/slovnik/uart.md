---
slug: "uart"
url: "/mobilnisite/slovnik/uart/"
type: "slovnik"
title: "UART – Universal Asynchronous Receiver and Transmitter"
date: 2025-01-01
abbr: "UART"
fullName: "Universal Asynchronous Receiver and Transmitter"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uart/"
summary: "Hardwarové rozhraní nebo protokol pro asynchronní sériovou komunikaci, běžně používaný pro nízkorychlostní výměnu dat a ladění. V kontextech 3GPP často odkazuje na fyzické rozhraní na UE nebo testovac"
---

UART je hardwarové rozhraní nebo protokol používaný pro asynchronní sériovou komunikaci, běžně využívaný v kontextech 3GPP na UE nebo testovacích zařízeních pro nízkorychlostní výměnu dat, ladění a diagnostické účely.

## Popis

Universal Asynchronous Receiver and Transmitter (UART) je počítačové hardwarové zařízení nebo, v moderních systémech, blok integrovaného obvodu, který zajišťuje asynchronní sériovou komunikaci. Funguje tak, že převádí paralelní data z výpočetního zařízení (jako je [CPU](/mobilnisite/slovnik/cpu/) nebo základnový procesor) na sériový bitový proud pro přenos a naopak převádí přijatý sériový bitový proud zpět na paralelní data. Komunikace je 'asynchronní', protože nepoužívá sdílený hodinový signál mezi vysílačem a přijímačem; místo toho musí být oba konce předem nakonfigurovány pro použití stejného datového formátu a přenosové rychlosti (symbolů za sekundu). Standardní datový rámec zahrnuje startovací bit, 5–9 datových bitů, volitelný paritní bit pro detekci chyb a jeden nebo více stop bitů.

V kontextu specifikací 3GPP a vývoje mobilních zařízení je rozhraní UART často implementováno jako fyzický port na vývojové desce uživatelského zařízení (UE), referenčním designu nebo testovacím telefonu. Tento port se nepoužívá pro uživatelský datový provoz, ale plní klíčové role ve vývoji, testování a diagnostice. Poskytuje nízkourovňový, spolehlivý komunikační kanál, který je nezávislý na vyšších vrstvách rádiových protokolů (jako LTE nebo 5G NR). Inženýři toto rozhraní používají k odesílání AT příkazů (definovaných v 3GPP TS 27.007), zaznamenávání ladících a trasovacích informací z modemu zařízení, monitorování sekvencí bootování a v určitých scénářích k provádění aktualizací firmwaru.

Rozhraní UART je typicky charakterizováno svou jednoduchostí, nízkou cenou a robustností. Vyžaduje pouze několik signálových linek: vysílání ([TX](/mobilnisite/slovnik/tx/)), příjem (RX) a společnou zem. Protože se jedná o základní a dobře pochopenou technologii, je univerzálně podporováno ladícími nástroji a softwarem hostitelského počítače. V rámci architektury UE může UART propojovat aplikační procesor s modemovým procesorem nebo může poskytovat externí přímý přístup k subsystému modemu. Jeho role je klíčová během fází integrace a testování shody, kdy je vyžadována přesná kontrola a viditelnost do provozu modemu ještě předtím, než je plně funkční celý bezdrátový stack zařízení.

## K čemu slouží

UART existuje jako základní, nízkourovňové komunikační rozhraní, které předchází systémům 3GPP. Jeho účelem v ekosystému 3GPP je poskytnout standardizovanou, jednoduchou a přímou metodu pro řízení a diagnostiku modemového hardwaru. Během vývoje mobilních zařízení potřebují inženýři způsob, jak komunikovat se základnovým procesorem, který nespoléhá na právě vyvíjené a testované rádiové protokoly. UART tuto roli dokonale plní.

Řeší problém počátečního zprovoznění, ladění a továrního programování. Předtím, než je celulární stack zařízení funkční, lze UART použít k načtení počátečního firmwaru, konfiguraci parametrů a získání bootovacích záznamů. Řeší omezení spočívající v absenci jiného funkčního rozhraní v 'holém' stavu zařízení. Dále pro standardizované testování shody sítě testovací systémy používají UART (často v kombinaci s AT příkazy) k přepnutí UE do specifických testovacích režimů, řízení jejího rádiového vysílání a ověření chování protokolu podle požadavků specifikací 3GPP.

Historický kontext je takový, že sériová komunikační rozhraní jako UART jsou desítky let základním prvkem designu vestavěných systémů. 3GPP začala odkazovat na UART, protože se jedná o všudypřítomnou hardwarovou vlastnost v mikrokontrolérech a procesorech používaných v mobilních zařízeních. Jeho pokračující specifikace zajišťuje, že výrobci testovacích zařízení a vývojáři zařízení mají společné, spolehlivé fyzické rozhraní pro klíčové úkoly vývoje a certifikace, nezávislé na rostoucí složitosti vzdušného rozhraní.

## Klíčové vlastnosti

- Provádí převod paralelních dat na sériová a sériových na paralelní.
- Funguje asynchronně bez sdíleného hodinového signálu.
- Konfigurovatelné parametry: přenosová rychlost, datové bity, parita, stop bity.
- Poskytuje přímé hardwarové rozhraní pro diagnostiku a řízení.
- Běžně používán pro komunikaci pomocí AT příkazů s modemy zařízení.
- Nezbytný pro ladění firmwaru zařízení a testování shody.

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [UART na 3GPP Explorer](https://3gpp-explorer.com/glossary/uart/)
