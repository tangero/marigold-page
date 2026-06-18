---
slug: "zsp"
url: "/mobilnisite/slovnik/zsp/"
type: "slovnik"
title: "ZSP – Zero Sequence Position"
date: 2025-01-01
abbr: "ZSP"
fullName: "Zero Sequence Position"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zsp/"
summary: "ZSP je parametr používaný v řadiči základnové stanice (BSC) k definování konkrétní, rezervované pozice časového slotu ve struktuře multirámce GSM rádiového kanálu. Slouží jako referenční bod pro admin"
---

ZSP je parametr, který definuje rezervovanou pozici časového slotu ve struktuře multirámce GSM rádiového kanálu a slouží jako referenční bod pro administrativní signalizaci a signalizaci pro údržbu mezi BSC a BTS.

## Popis

Zero Sequence Position (ZSP, pozice nulové sekvence) je koncept definovaný v dokumentu 3GPP TS 48.020, který specifikuje přímou signalizaci řízení (inband control signaling) na rozhraní Abis v sítích GSM. Rozhraní Abis spojuje řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) a základnovou přenosovou stanici ([BTS](/mobilnisite/slovnik/bts/)). ZSP označuje určený, rezervovaný časový slot v rámci 26-rámcového provozního multirámce (pro [TCH/F](/mobilnisite/slovnik/tch-f/)) nebo 51-rámcového řídicího multirámce (pro [BCCH](/mobilnisite/slovnik/bcch/), [CCCH](/mobilnisite/slovnik/ccch/) nebo [SDCCH](/mobilnisite/slovnik/sdcch/)) na GSM rádiovém kanálu. Tato konkrétní pozice časového slotu se používá výhradně pro přenos zpráv provozu a údržby (O&M) mezi BSC a BTS, které jsou přenášeny přes přímý signalizační kanál.

Fungování ZSP je svázáno s pevnou [TDMA](/mobilnisite/slovnik/tdma/) strukturou GSM. Každý fyzický rádiový nosič je rozdělen na 8 časových slotů (TS0-TS7) a tyto sloty jsou dále organizovány do multirámců. BSC administrativně přiřadí hodnotu ZSP (např. konkrétní číslo rámce v multirámci) pro daný kanál. BTS je nakonfigurována tak, aby očekávala zprávy O&M na této předem definované pozici. Zprávy přímé signalizace, které nesou kritická data správy, jako jsou bloky pro stahování softwaru, hlášení poruch a konfigurační příkazy, jsou multiplexovány na provozní nebo řídicí kanál právě v tomto rezervovaném ZSP. Tím je zajištěno, že komunikace O&M má v datovém toku garantovaný, předvídatelný slot, což zabraňuje jejímu přepsání uživatelským provozem a zaručuje její včasné doručení.

Klíčovými komponentami jsou BSC (která generuje a odesílá zprávy O&M), BTS (která je přijímá a podle nich jedná), přenosový okruh rozhraní Abis a konkrétní GSM kanál (jako provozní kanál nebo samostatný vyhrazený řídicí kanál), který přímou signalizaci nese. Úlohou ZSP je poskytnout robustní transportní mechanismus na nízké úrovni pro základní řídicí funkce bez nutnosti vyhrazeného fyzického O&M okruhu pro každou BTS. Umožňuje vzdálené aktualizace softwaru, monitorování výkonu a obnovu po poruše, což je klíčové pro provozní stabilitu a udržovatelnost GSM rádiové přístupové sítě. Přesná definice ZSP zajišťuje interoperabilitu mezi zařízeními BSC a BTS od různých výrobců.

## K čemu slouží

ZSP byl vytvořen, aby vyřešil problém efektivní a spolehlivé komunikace provozu a údržby (O&M) mezi [BSC](/mobilnisite/slovnik/bsc/) a BTS v raných sítích GSM. Před standardizovanou přímou signalizací mohla O&M vyžadovat samostatné fyzické linky, což zvyšovalo náklady a složitost nasazení. Motivací bylo využít stávající přenosové kanály rozhraní Abis pro účely správy, a tím snížit požadavky na infrastrukturu. Zero Sequence Position poskytuje deterministický, rezervovaný slot ve struktuře rámce kanálu pro přenos těchto řídicích dat.

Tento přístup odstranil omezení spočívající v potřebě řešení mimo pásmo nebo proprietárních signalizačních metod. Definováním konkrétní pozice („nulové“ sekvence) zajistil, že se zprávy O&M nesrazí s uživatelským provozem ani jinou řídicí signalizací, a garantoval jejich doručení i při vysokém zatížení provozem. To bylo zásadní pro kritické funkce, jako je vzdálené stahování softwaru pro aktualizaci firmwaru BTS nebo nahrávání dat o poruchách pro řešení problémů v síti. Vytvoření ZSP v Release 8 (a jeho dokumentace v TS 48.020) tento mechanismus standardizovalo napříč odvětvím, čímž zajistilo interoperabilitu mezi různými výrobci a spolehlivou správu sítě pro 2G GSM sítě – princip, který podporoval provoz sítí po mnoho následujících vydání.

## Klíčové vlastnosti

- Definuje rezervovanou pozici časového slotu v rámci TDMA multirámce GSM pro signalizaci O&M
- Používá se pro přenos přímé signalizace přes rozhraní Abis mezi BSC a BTS
- Podporuje kritické řídicí funkce, jako je stahování softwaru a hlášení poruch
- Administrativně konfigurováno BSC pro každý relevantní kanál
- Zajišťuje spolehlivé doručení dat O&M tím, že zabraňuje soupeření s uživatelským provozem
- Standardizováno v TS 48.020 za účelem zajištění interoperability mezi různými výrobci

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)

## Definující specifikace

- **TS 48.020** (Rel-19) — PLMN Rate Adaptation Functions

---

📖 **Anglický originál a plná specifikace:** [ZSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/zsp/)
