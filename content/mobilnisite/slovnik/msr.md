---
slug: "msr"
url: "/mobilnisite/slovnik/msr/"
type: "slovnik"
title: "MSR – Multi-Standard Radio Base Station"
date: 2025-01-01
abbr: "MSR"
fullName: "Multi-Standard Radio Base Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/msr/"
summary: "Multi-Standard Radio (MSR) základnová stanice je radiový uzel schopný současně vysílat a přijímat více technologií radiového přístupu 3GPP (např. GSM, UMTS, LTE) za použití společného rádiového frekve"
---

MSR je základnová stanice, která může současně provozovat více radiových technologií 3GPP, jako jsou GSM, UMTS a LTE, za použití sdíleného hardwaru a softwaru pro efektivní a nákladově efektivní nasazení.

## Popis

Multi-Standard Radio (MSR) základnová stanice je pokročilý uzel radiového přístupu definovaný ve specifikacích 3GPP, který podporuje provoz dvou nebo více technologií radiového přístupu 3GPP (RAT) v rámci jedné stanice. Podporované RAT typicky zahrnují GSM/[EDGE](/mobilnisite/slovnik/edge/) ([GERAN](/mobilnisite/slovnik/geran/)), UMTS (UTRAN) a LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)), a potenciálně 5G NR v pozdějších implementacích, přičemž všechny operují v definovaných frekvenčních pásmech. Klíčovým architektonickým principem MSR [BS](/mobilnisite/slovnik/bs/) je sdílení společných hardwarových komponent – jako jsou výkonové zesilovače, filtry, transceivery a antény – napříč různými RAT. Toho je dosaženo prostřednictvím principů softwarově definovaného rádia (SDR) a pokročilého zpracování základní pásma. Stanice obsahuje více jednotek pro zpracování základní pásma (pro každý RAT), které jsou napájeny do společné radiové jednotky. Tato jednotka používá širokopásmové RF komponenty schopné pokrýt agregovanou šířku pásma všech aktivních nosných. Dynamické sdílení spektra je klíčovou schopností, kdy MSR BS může alokovat radiové zdroje (frekvenční bloky, výkon) mezi koexistujícími RAT na základě provozní zátěže a politik operátora. MSR BS musí splňovat přísné požadavky 3GPP na výkon (specifikované v sérii TS 37.1xx) pro každou podporovanou RAT nezávisle, což zajišťuje, že sdílený provoz nezhorší výkon žádné jednotlivé technologie. Rozhraní k příslušným jádrovým sítím (např. [MSC](/mobilnisite/slovnik/msc/) pro GSM/UMTS, [MME](/mobilnisite/slovnik/mme/) pro LTE) zprostředkovává prostřednictvím standardních rozhraní (Iu, S1). Správa je jednotná, což operátorům umožňuje konfigurovat a monitorovat všechny RAT prostřednictvím jediného systému správy.

## K čemu slouží

MSR základnová stanice byla vyvinuta k řešení praktických a ekonomických výzev spojených s vývojem sítě a koexistencí více technologií. Když mobilní operátoři nasazovali postupně generace technologií (2G, 3G, 4G), často čelili fragmentaci spektra, přeplněnosti lokalit a rostoucím nákladům na údržbu samostatných skříní základnových stanic, antén a přenosových tras pro každý RAT. Koncept MSR, představený v 3GPP Rel-9, poskytl standardizované řešení v podobě jedné hardwarové platformy schopné podporovat více standardů. Tím vyřešil problém neefektivního využití spektra a vysokých kapitálových/provozních výdajů (CapEx/OpEx) spojených s paralelními nasazeními sítí. Umožnil plynulejší migraci technologií, což operátorům dovolilo dynamicky přerozdělovat spektrum ze starších technologií (jako GSM) na novější (jako LTE) bez nutnosti fyzické výměny hardwaru. Vznik MSR byl motivován potřebou průmyslu po budoucím, škálovatelném infrastrukturním řešení, které by zvládlo rostoucí složitost sítí radiového přístupu a zároveň zjednodušilo získávání lokalit, spotřebu energie a údržbu.

## Klíčové vlastnosti

- Současná podpora více technologií radiového přístupu 3GPP (např. GSM, WCDMA, LTE) v jedné základnové stanici.
- Sdílený RF hardware (výkonové zesilovače, filtry, antény) snižující prostorové nároky a náklady.
- Softwarově definovaná konfigurovatelnost pro úpravu podpory RAT a alokace nosných.
- Dynamické sdílení spektra mezi koexistujícími technologiemi na základě provozní zátěže.
- Dodržování individuálních specifikací 3GPP pro výkon každé podporované RAT.
- Jednotná správa a údržba (O&M) pro všechny integrované technologie.

## Související pojmy

- [BS – Base Station](/mobilnisite/slovnik/bs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.744** (Rel-14) — CBRS 3.5GHz Band Specification for US
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 36.858** (Rel-14) — LTE 2.6 GHz SDL Band Technical Report
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [MSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/msr/)
