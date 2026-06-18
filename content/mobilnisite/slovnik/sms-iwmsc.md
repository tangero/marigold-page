---
slug: "sms-iwmsc"
url: "/mobilnisite/slovnik/sms-iwmsc/"
type: "slovnik"
title: "SMS-IWMSC – Short Message Service Interworking MSC"
date: 2025-01-01
abbr: "SMS-IWMSC"
fullName: "Short Message Service Interworking MSC"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/sms-iwmsc/"
summary: "SMS-IWMSC je propojovací MSC, který slouží jako výstupní bod pro mobilní zprávy (MO-SM) z GSM/UMTS jádra sítě do externího centra služby krátkých zpráv (SMSC). Přijímá zprávy z obsluhujícího MSC a dor"
---

SMS-IWMSC je propojovací MSC (Mobile Switching Center), který slouží jako výstupní bod pro mobilní zprávy (MO-SM) z jádra sítě. Přijímá je z obsluhujícího MSC a doručuje je příslušnému externímu SMSC.

## Popis

Short Message Service Interworking [MSC](/mobilnisite/slovnik/msc/) (SMS-IWMSC) je funkční protějšek [SMS-GMSC](/mobilnisite/slovnik/sms-gmsc/), který zajišťuje odchozí cestu pro mobilní zprávy (MO-SM) v jádrech sítí 2G/3G s přepojováním okruhů. Když mobilní účastník odešle [SMS](/mobilnisite/slovnik/sms/), zpráva je nejprve doručena přes rozhraní rádiové sítě k jeho aktuálnímu obsluhujícímu MSC. Obsluhující MSC, které rozpozná zprávu jako mobilní, ji poté přepošle na SMS-IWMSC. SMS-IWMSC slouží jako určená brána z [PLMN](/mobilnisite/slovnik/plmn/) do externího centra služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)). Podobně jako SMS-GMSC se obvykle jedná o funkční roli umístěnou společně s fyzickým MSC.

SMS-IWMSC přijímá MO-SM z obsluhujícího MSC prostřednictvím interní signalizace [MAP](/mobilnisite/slovnik/map/) (MAP_FORWARD_SHORT_MESSAGE). Jeho klíčovou odpovědností je určit správný cílový SMSC pro zprávu. Toto směrovací rozhodnutí je často založeno na konfiguraci, například na výchozím SMSC pro domovskou síť účastníka nebo na konkrétní adrese SMSC poskytnuté [HLR](/mobilnisite/slovnik/hlr/) při získávání profilu účastníka. SMS-IWMSC poté provede případnou potřebnou adaptaci protokolu a odešle zprávu identifikovanému externímu SMSC, obvykle pomocí stejného rozhraní založeného na MAP (např. MAP_[MT](/mobilnisite/slovnik/mt/)_FORWARD_SHORT_MESSAGE) přes SS7 nebo IP spoje.

Tato entita také spravuje hlášení o doručení a chyby ve směru od mobilního zařízení. Pokud externí SMSC potvrdí úspěšný příjem, SMS-IWMSC může přeposlat kladné hlášení o doručení zpět přes obsluhující MSC k odesílajícímu mobilnímu zařízení. Naopak, pokud SMSC zprávu odmítne nebo je nedostupný, SMS-IWMSC zpracuje chybu a může o tom informovat obsluhující MSC. SMS-IWMSC poskytuje jediný, řízený výstupní bod pro veškerý provoz MO-SM, což umožňuje centralizované účtování, zákonné odposlechy a kontrolu zpráv předtím, než opustí síť operátora. Společně se SMS-GMSC tvoří kompletní funkcionalitu SMS brány pro doménu CS.

## K čemu slouží

SMS-IWMSC byl standardizován, aby poskytoval řízený a standardizovaný výstupní bod z PLMN pro textové zprávy odeslané účastníkem, čímž zrcadlí vstupní funkci SMS-GMSC. Jeho zavedení vyřešilo problém, jak má obsluhující MSC, které řeší mobilitu účastníka, směrovat odchozí SMS na potenciálně externí a pevný SMSC. Bez vyhrazené propojovací funkce by každé MSC potřebovalo přímou konektivitu a směrovací konfigurace pro všechny možné SMSC, což by vedlo k provozní složitosti a problémům se škálováním.

Tato architektura centralizuje propojovací funkci, zjednodušuje správu sítě a umožňuje funkce jako centralizované účtování za odeslané zprávy a konzistentní uplatňování regulatorních požadavků (např. filtrování obsahu, zákonné odposlechy) na hranici sítě. Řeší omezení spočívající v tom, že provoz odeslaný z mobilních zařízení opouštěl síť nahodile z jakéhokoli MSC. Tím, že veškerý provoz MO-SM prochází přes SMS-IWMSC, získávají operátoři strategický bod kontroly a přehledu pro odchozí služby zasílání zpráv. Byl to klíčový prvek pro to, aby se SMS stala pro síťové operátory spolehlivou, účtovatelnou a řiditelnou službou.

## Klíčové vlastnosti

- Brána (gateway) pro mobilní SMS směrem k externím SMSC
- Přijímá MO-SM z obsluhujícího MSC prostřednictvím přeposílání MAP
- Určuje a směruje zprávy na příslušný cílový SMSC
- Zpracovává hlášení o doručení a oznámení o chybách ze SMSC
- Poskytuje centralizovaný výstupní bod z PLMN pro odchozí SMS provoz
- Umožňuje centralizované účtování, filtrování a zákonné odposlechy pro MO-SM

## Související pojmy

- [SMS-GMSC – Short Message Service Gateway MSC](/mobilnisite/slovnik/sms-gmsc/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [SMS-IWMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-iwmsc/)
