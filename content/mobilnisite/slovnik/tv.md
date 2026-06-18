---
slug: "tv"
url: "/mobilnisite/slovnik/tv/"
type: "slovnik"
title: "TV – Type and Value"
date: 2025-01-01
abbr: "TV"
fullName: "Type and Value"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tv/"
summary: "TV je kompaktní formát kódování používaný v protokolech 3GPP pro reprezentaci informačních prvků s identifikátorem typu a přidruženou hodnotou. Optimalizuje velikost zpráv vynecháním polí délky pro ho"
---

TV je kompaktní formát kódování používaný v protokolech 3GPP pro reprezentaci informačních prvků s identifikátorem typu a přidruženou hodnotou, který optimalizuje velikost zpráv vynecháním polí délky pro hodnoty pevné délky.

## Popis

Typ a hodnota (TV) je formát kódování dat používaný v různých specifikacích protokolů 3GPP pro efektivní reprezentaci informačních prvků ([IE](/mobilnisite/slovnik/ie/)) v signalizačních zprávách. Při TV kódování se každý IE skládá z pole typu (typicky jeden oktet), které prvek identifikuje, a bezprostředně za ním následujícího pole hodnoty, bez explicitního indikátoru délky. To je v kontrastu s kódováním [TLV](/mobilnisite/slovnik/tlv/) (Typ-Délka-Hodnota), které obsahuje samostatné pole délky. Formát TV se používá pro IE, jejichž délka je pevná a známá z typu, nebo kde lze délku odvodit z kontextu, čímž se snižuje režie a zjednodušuje se parsování. Často se vyskytuje v protokolech, jako jsou ty pro účtování, správu a některé zprávy řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), jak je specifikováno v technických specifikacích jako TS 32.272 a TS 32.295.

Z architektonického hlediska se TV kódování uplatňuje v abstraktní syntaxi jednotek protokolových dat ([PDU](/mobilnisite/slovnik/pdu/)), kde je každý IE definován v jazyce ASN.1 nebo podobných popisných jazycích. Pole typu slouží jako jedinečný identifikátor, často mapovaný na předdefinovaný slovník ve specifikaci protokolu, což umožňuje přijímajícím entitám interpretovat hodnotu na základě typu. Například v záznamech účtovacích dat ([CDR](/mobilnisite/slovnik/cdr/)) může TV kódovaný IE představovat časové razítko nebo identifikátor účastníka se známou velikostí v oktech. Pole hodnoty obsahuje vlastní data, která mohou být primitivních typů, jako je celé číslo, řetězec nebo výčtové hodnoty, formátovaná podle pravidel protokolu. Protože zde není přítomno pole délky, dekodéry se musí spoléhat na externí specifikace nebo implicitní znalosti, aby extrahovaly správný počet oktetů.

V provozu TV kódování zvyšuje efektivitu zpráv minimalizací počtu bajtů, což je klíčové pro rozhraní s omezenou šířkou pásma nebo pro signalizaci s vysokým objemem. Když protokol používá TV, odesílatel vytváří zprávy zřetězením dvojic typ-hodnota a přijímač je parsuje sekvenčně, přičemž podle typu určuje, kolik oktetů má pro hodnotu načíst. To vyžaduje přísnou standardizaci, aby se předešlo nejednoznačnosti; například, pokud může být hodnota proměnné délky, je upřednostněno TLV. V 3GPP se TV často používá v kombinaci s TLV, kde TV zpracovává jednoduché, pevné prvky a TLV složité nebo proměnné. Jeho role je významná v rozhraních pro provoz a údržbu (O&M), v účtovacích bránách a systémech správy sítě, kde kompaktní reprezentace dat snižuje zatížení zpracováním a náklady na přenos.

## K čemu slouží

TV kódování bylo vyvinuto za účelem optimalizace efektivity protokolů snížením režie spojené s přenosem informačních prvků v telekomunikačních sítích. V raných digitálních signalizačních systémech bylo minimalizování velikosti zpráv klíčové kvůli omezené šířce pásma na signalizačních spojích a omezením zpracování v síťových uzlech. Kódování [TLV](/mobilnisite/slovnik/tlv/), ačkoli flexibilní, přidává extra bajty pro pole délky, což může být plýtvání pro prvky s pevnou nebo předvídatelnou velikostí. TV to řešilo odstraněním pole délky za předpokladu, že přijímač již zná délku na základě identifikátoru typu, čímž šetří šířku pásma a urychluje parsování zpráv.

Historický kontext spočívá ve vývoji telekomunikačních protokolů od jednoduchých binárních formátů ke strukturovanějším kódováním, jako je ASN.1. Formát TV se objevil jako pragmatické řešení pro specifické případy užití ve standardech, jako jsou [ITU-T](/mobilnisite/slovnik/itu-t/) a 3GPP, zejména pro data správy a účtování, kde je upřednostňována efektivita. Řešil problémy spojené s výměnou dat vysokého objemu, například v účtovacích systémech, kde se generují četné [CDR](/mobilnisite/slovnik/cdr/), komprimací záznamů bez obětování interoperability. V 3GPP je TV specifikováno ve vydáních od Rel-5 pro aplikace jako řízení výkonu a řízení poruch, což umožňuje štíhlejší rozhraní mezi síťovými prvky a řídicími entitami. Ačkoli je méně flexibilní než TLV, TV zůstává relevantní pro scénáře, kde je přijatelná rigidita schématu a výkonnostní zisky jsou významné.

## Klíčové vlastnosti

- Kompaktní kódování pouze s poli typu a hodnoty, bez explicitních indikátorů délky
- Předpoklad hodnoty pevné délky na základě identifikátoru typu pro efektivní parsování
- Běžné použití v záznamech účtovacích dat (CDR) a zprávách řídicích protokolů
- Interoperabilita s kódováním TLV v prostředích smíšených protokolů
- Snížená režie zpráv ve srovnání s TLV, šetřící šířku pásma na signalizačních rozhraních
- Standardizovaná mapování typů ve specifikacích 3GPP pro zajištění konzistentní interpretace napříč uzly

## Související pojmy

- [TLV – Type, Length, Value](/mobilnisite/slovnik/tlv/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol

---

📖 **Anglický originál a plná specifikace:** [TV na 3GPP Explorer](https://3gpp-explorer.com/glossary/tv/)
