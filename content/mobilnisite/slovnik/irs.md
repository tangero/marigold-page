---
slug: "irs"
url: "/mobilnisite/slovnik/irs/"
type: "slovnik"
title: "IRS – Intermediate Reference System"
date: 2025-01-01
abbr: "IRS"
fullName: "Intermediate Reference System"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/irs/"
summary: "Standardizovaný referenční bod nebo systém používaný pro testování výkonu a porovnávání řečových kodeků a kvality zvuku v 3GPP. Poskytuje konzistentní základnu, často popisovanou jako 'spíše plochá',"
---

IRS (Intermediate Reference System) je standardizovaný referenční systém používaný pro testování výkonu a porovnávání řečových kodeků a kvality zvuku v 3GPP, který poskytuje konzistentní základnu pro hodnocení výkonu kodeků za řízených podmínek.

## Popis

Intermediate Reference System (IRS) je klíčový koncept ve specifikacích 3GPP pro hodnocení kvality zvuku a řeči. Je definován jako standardizovaný elektroakustický řetězec, který simuluje charakteristiky typického telefonního sluchátka včetně mikrofonu, sluchátka a přidružených frekvenčních charakteristik. IRS není fyzické zařízení, ale matematický model nebo sada filtrů specifikovaných v doporučeních [ITU-T](/mobilnisite/slovnik/itu-t/) (např. P.48) a přijatých 3GPP. Jeho primární role spočívá v tom, že slouží jako referenční bod při subjektivním a objektivním testování řečových kodeků, čímž zajišťuje, že hodnocení jsou konzistentní a reprodukovatelná napříč různými laboratořemi a výrobci. Termín 'No IRS' nebo 'spíše plochá' odkazuje na podmínku, kdy se filtr IRS nepoužije, což znamená, že zvukový signál je zpracován bez typického telefonního omezení pásma, což vede k plošší frekvenční charakteristice bližší původnímu širokopásmovému zvuku.

Architektonicky je IRS implementován v rámci testovacích sestav definovaných ve specifikacích jako 26.975 (Speech and video telephony tester) a 26.978 (Voice over IP test). V těchto sestavách je filtr IRS aplikován na vysílací (mluvící) a přijímací (poslouchající) cestu, aby emuloval akustické rozhraní tradičního telefonu. IRS na straně vysílání upravuje vstupní řečový signál tak, aby napodobil frekvenční charakteristiku typického mikrofonu sluchátka, která má typicky charakter pásmové propusti (např. 100 Hz až 8 kHz) se specifickými útlumy. IRS na straně příjmu dělá totéž pro výstup, simuluje sluchátko přijímače. Tím se zajišťuje, že výkon kodeku je hodnocen za podmínek, které odpovídají reálnému použití, nikoli ideálním laboratorním podmínkám s dokonalými měniči.

Jak to funguje, zahrnuje integraci filtru IRS do testovacích sekvencí pro kvalifikaci kodeků. Během subjektivních testů, jako jsou hodnocení Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)), posluchači hodnotí kvalitu řeči poté, co signál prošel IRS, a poskytují hodnocení odrážející typický uživatelský zážitek. Pro objektivní testy mohou algoritmy jako POLQA nebo PESQ používat IRS jako referenci pro porovnání degradované řeči s neporušenou referencí. IRS je klíčový pro zajištění toho, že metriky výkonu kodeků, jako jsou ty pro kodeky [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/) nebo VoLTE/VoNR, jsou srovnatelné napříč různými implementacemi a síťovými podmínkami. Jeho zařazení do specifikací 3GPP, jako je 29.163 (Interworking between SIP-I and BICC) a 46.008 ([MS](/mobilnisite/slovnik/ms/) speech codec), podtrhuje jeho důležitost pro interoperabilitu a zajištění kvality hlasových služeb.

## K čemu slouží

Účelem Intermediate Reference System (IRS) je poskytnout standardizovanou a reprodukovatelnou akustickou referenci pro testování řečových kodeků a kvality zvuku v telekomunikacích. Před jeho přijetím byla hodnocení kodeků často nekonzistentní, protože různé testovací sestavy používaly různé charakteristiky mikrofonů a přijímačů, což vedlo k nesrovnatelným výsledkům. IRS tento problém řeší definováním jednotného elektroakustického řetězce, který napodobuje typické telefonní sluchátko, a zajišťuje, že všechny testy jsou prováděny za stejných podmínek. To umožňuje spravedlivé porovnání různých kodeků (např. GSM [FR](/mobilnisite/slovnik/fr/) vs. [AMR-WB](/mobilnisite/slovnik/amr-wb/)) a zajišťuje, že metriky výkonu, jako je kvalita řeči, odolnost proti šumu a zpoždění, jsou měřeny způsobem, který odráží reálný uživatelský zážitek.

Historicky potřeba IRS vyvstala s rozšířením digitálních řečových kodeků v sítích 2G/3G, kde se zajištění kvality stalo klíčovým pro přijetí služby. [ITU-T](/mobilnisite/slovnik/itu-t/) vyvinulo koncept IRS (např. v doporučení P.48) pro standardizaci testování a 3GPP jej začlenilo počínaje Release 8 pro podporu hlasových služeb přes GSM, UMTS a později LTE/5G. Podmínka 'spíše plochá' (No IRS) byla zavedena, aby vyhověla širokopásmovým a super-širokopásmovým kodekům, jako jsou AMR-WB a EVS, které těží z širší frekvenční charakteristiky. Tím se řeší omezení úzkopásmového IRS, které bylo přizpůsobeno tradiční telefonní šířce pásma (300-3400 Hz), a umožňují se testy, které lépe reprezentují vylepšené hlasové služby.

Motivace pro zařazení IRS do 3GPP byla hnána potřebou interoperability a konzistence kvality napříč globálními sítěmi. Použitím IRS mohou výrobci a operátoři ověřit, že kodeky splňují minimální standardy kvality, usnadnit roamování a zajistit zpětnou kompatibilitu. Také podporuje vývoj od přepojování okruhů k paketovému přepojování VoLTE/VoNR, kde je udržení kvality řeči napříč různorodými sítěmi a zařízeními prvořadé. IRS tedy zůstává základním prvkem testování zvuku, který umožňuje spolehlivé nasazení hlasových služeb od 2G do 5G.

## Klíčové vlastnosti

- Standardizovaný elektroakustický filtrační řetězec simulující charakteristiky telefonního sluchátka
- Definován v doporučeních ITU-T (např. P.48) a přijat ve specifikacích 3GPP
- Používán pro subjektivní (MOS) a objektivní (PESQ/POLQA) testování kvality řeči
- Podporuje hodnocení jak úzkopásmových (300-3400 Hz), tak širokopásmových (50-7000 Hz) kodeků
- Umožňuje konzistentní a reprodukovatelné porovnání výkonu kodeků napříč laboratořemi
- Integrální součást testovacích sestav ve specifikacích 26.975, 26.978 a specifikacích pro hlasovou interoperabilitu

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [IRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/irs/)
