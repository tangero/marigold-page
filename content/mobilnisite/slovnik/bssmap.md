---
slug: "bssmap"
url: "/mobilnisite/slovnik/bssmap/"
type: "slovnik"
title: "BSSMAP – Base Station Subsystem Management Application Part"
date: 2025-01-01
abbr: "BSSMAP"
fullName: "Base Station Subsystem Management Application Part"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bssmap/"
summary: "BSSMAP je signalizační protokol používaný mezi řadičem základnových stanic (BSC) a ústřednou mobilní sítě (MSC) v sítích GSM. Spravuje přidělování rádiových prostředků, řízení předávání hovorů a funkc"
---

BSSMAP je signalizační protokol používaný mezi řadičem základnové stanice (BSC) a ústřednou mobilní sítě (MSC) v sítích GSM pro správu rádiových prostředků, předávání hovorů (handover) a operací subsystému základnových stanic.

## Popis

BSSMAP (Base Station Subsystem Management Application Part) je klíčový signalizační protokol v architektuře GSM, který funguje mezi řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v subsystému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) a ústřednou mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) v přepínacím subsystému sítě ([NSS](/mobilnisite/slovnik/nss/)). Působí jako aplikační protokol, který využívá základní transportní mechanismus [SCCP](/mobilnisite/slovnik/sccp/) (Signaling Connection Control Part) přes rozhraní A. Protokol je zodpovědný za správu rádiových prostředků a koordinaci událostí mobility, čímž zajišťuje plynulou komunikaci mezi rádiovou přístupovou sítí a přepínacími funkcemi jádra sítě.

Z architektonického hlediska jsou zprávy BSSMAP přenášeny v rámci spojovaných nebo nespojovaných služeb SCCP v závislosti na konkrétním postupu. Protokol definuje četné typy zpráv rozdělených do funkčních skupin: správa rádiových prostředků (včetně přidělení, předání hovoru a šifrování), správa mobility (aktualizace polohy a připojení/odpojení [IMSI](/mobilnisite/slovnik/imsi/)) a provoz a údržba (reset BSS, řízení přetížení a hlášení stavu prostředků). Mezi klíčové komponenty patří přístupový bod služby BSSMAP (BSAP), který poskytuje rozhraní k entitám řízení hovoru ([CC](/mobilnisite/slovnik/cc/)) a správy mobility ([MM](/mobilnisite/slovnik/mm/)) v MSC, a různé procedurální elementy, které zpracovávají specifické síťové funkce jako žádost o předání hovoru, přidělení kanálu a vyhledávání.

BSSMAP funguje prostřednictvím dobře definované sady procedur, které koordinují činnosti mezi BSC a MSC. Pro předání hovoru (handover) MSC použije BSSMAP k požádání cílového BSC o přidělení prostředků a následně přikáže mobilní stanici, aby přešla na nový kanál. Při sestavování hovoru BSSMAP spravuje přidělení hovorových kanálů poté, co MSC obdrží žádost o hovor. Protokol také zvládá funkce správy BSS, jako jsou resetovací procedury (při restartu BSC nebo MSC), řízení přetížení (k zabránění zahlcení systému) a blokování/odblokování rádiových prostředků. BSSMAP spolupracuje s protokolem Direct Transfer Application Part (DTAP), který transparentně přenáší zprávy správy mobility a řízení hovoru přes BSS mezi mobilní stanicí a MSC.

V celkové síťové architektuře hraje BSSMAP klíčovou roli při oddělení funkcí specifických pro rádiové rozhraní (spravovaných BSC) od přepínacích funkcí a servisní logiky (spravovaných MSC). Toto oddělení umožňuje nezávislý vývoj technologií rádiového přístupu při zachování konzistentních rozhraní jádra sítě. Návrh protokolu umožňuje efektivní využití prostředků tím, že MSC může činit centralizovaná rozhodnutí na základě informací o rádiových prostředcích poskytovaných BSC prostřednictvím zpráv BSSMAP. Komplexní mechanismy pro zpracování chyb a obnovení v BSSMAP zajišťují spolehlivost sítě během různých scénářů selhání.

## K čemu slouží

BSSMAP byl vytvořen k řešení základní potřeby standardizované signalizace mezi subsystémem základnových stanic (BSS) a přepínacím subsystémem sítě (NSS) v sítích GSM. Před standardizací GSM používaly celulární systémy často proprietární rozhraní mezi rádiovým zařízením a přepínacími systémy, což omezovalo interoperabilitu mezi zařízeními od různých výrobců a zvyšovalo náklady na nasazení. BSSMAP poskytl standardizovaný protokol, který umožnil interoperabilitu mezi více výrobci a zároveň podporoval složitou koordinaci potřebnou pro správu mobility a přidělování rádiových prostředků v celulárních sítích.

Protokol konkrétně řeší problém koordinace rozhodnutí o správě rádiových prostředků mezi BSC (které má detailní znalost rádiových podmínek a dostupných kanálů) a MSC (které spravuje směrování hovorů a služby účastníků). Bez BSSMAP by bylo velmi obtížné koordinovat předání hovoru mezi buňkami řízenými různými BSC a MSC by při rozhodování o přijetí hovoru postrádalo přehled o dostupnosti rádiových prostředků. BSSMAP také řeší provozní požadavky tím, že poskytuje mechanismy pro údržbu BSS, správu poruch a řízení přetížení – což jsou nezbytné funkce pro komerční provoz sítí.

Historicky bylo vytvoření BSSMAP motivováno cílem standardizačního úsilí GSM vytvořit skutečně otevřený, interoperabilní celulární systém. Definováním jasného funkčního oddělení mezi rádiovou přístupovou sítí (BSS) a jádrem sítě (NSS), s BSSMAP jako signalizačním rozhraním, GSM umožnilo konkurenci mezi dodavateli infrastruktury a zároveň zajistilo spolehlivost sítě a konzistenci služeb. Tento architektonický přístup ovlivnil následující generace mobilních sítí, ačkoli BSSMAP jako takový je specifický pro GSM a rané verze UMTS, kde byl adaptován pro rozhraní Iu-cs mezi RNC a MSC.

## Klíčové vlastnosti

- Správa rádiových prostředků včetně přidělení a uvolnění kanálů
- Řízení předání hovoru mezi buňkami a BSC
- Funkce provozu a údržby BSS
- Řízení přetížení a hlášení stavu prostředků
- Řízení a správa režimu šifrování
- Transparentní přenos zpráv DTAP mezi MS a MSC

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [DTAP – Direct Transfer Application Part](/mobilnisite/slovnik/dtap/)
- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- **TS 49.008** (Rel-19) — BSSAP on E-interface for inter-MSC handover

---

📖 **Anglický originál a plná specifikace:** [BSSMAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bssmap/)
