---
slug: "dpch-ec"
url: "/mobilnisite/slovnik/dpch-ec/"
type: "slovnik"
title: "DPCH_Ec – Dedicated Physical Channel Energy per Chip"
date: 2025-01-01
abbr: "DPCH_Ec"
fullName: "Dedicated Physical Channel Energy per Chip"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dpch-ec/"
summary: "DPCH_Ec je měření na fyzické vrstvě představující průměrnou energii na čip pseudonáhodného (PN) kódu pro vyhrazený fyzický kanál (DPCH) v UMTS. Jde o klíčový parametr pro výpočty link budgetu, řízení"
---

DPCH_Ec je průměrná energie na čip pseudonáhodného kódu pro vyhrazený fyzický kanál (Dedicated Physical Channel) v UMTS, klíčové měření fyzické vrstvy pro výpočet link budgetu, řízení výkonu a hodnocení výkonu přijímače.

## Popis

[DPCH](/mobilnisite/slovnik/dpch/)_[Ec](/mobilnisite/slovnik/ece-c/) je základní parametr fyzické vrstvy definovaný ve specifikacích 3GPP pro UMTS (UTRA), konkrétně pro režim s frekvenčním duplexem ([FDD](/mobilnisite/slovnik/fdd/)). Kvantifikuje průměrnou přijatou energii na čip pseudonáhodného (PN) kódu pro vyhrazený fyzický kanál (DPCH). DPCH přenáší vyhrazená uživatelská data a řídicí informace ([DPDCH](/mobilnisite/slovnik/dpdch/) a [DPCCH](/mobilnisite/slovnik/dpcch/)) pro konkrétní spojení. Měření se provádí po operaci despreadingu v přijímači, která oddělí signál požadovaného uživatele z celkového přijatého signálu aplikací uživatelsky specifických kódů pro skramblování a kanalizaci. Hodnota DPCH_Ec je neodmyslitelně spojena s vysílaným výkonem DPCH a je zeslabena útlumem na rádiovém kanále, stíněním a rychlým únikem.

V provozu systému je DPCH_Ec klíčovým vstupem pro algoritmus vnitřní smyčky řízení výkonu. UE měří přijatý DPCH_Ec a porovnává jej s cílovým poměrem signálu k interferenci (SIR) nastaveným vnější smyčkou řízení výkonu. Na základě tohoto porovnání UE odesílá příkazy řízení vysílacího výkonu (TPC) do Node B, aby mu nařídila zvýšit nebo snížit vysílací výkon DPCH, čímž udržuje kvalitu spoje. Dále se DPCH_Ec používá spolu s celkovou spektrální hustotou přijatého výkonu (Io) pro výpočet přijatého poměru signálu k interferenci (Ec/Io), což je klíčová metrika pro rozhodování o předávání spojení a výběru/reselekci buňky (např. porovnání [CPICH](/mobilnisite/slovnik/cpich/) Ec/Io).

Z pohledu plánování a optimalizace sítě je DPCH_Ec nezbytný pro analýzu link budgetu. Technici jej používají k výpočtu maximálního přípustného útlumu na dráze mezi UE a Node B pro danou službu, čímž zajišťují splnění cílů pokrytí. Rovněž se zohledňuje při výpočtech citlivosti přijímače. Parametr je specifikován v technických normách, jako je 3GPP TS 25.102, která podrobně popisuje požadavky na rádiový přenos a příjem v UE včetně referenčních úrovní citlivosti definovaných pomocí DPCH_Ec.

## K čemu slouží

[DPCH](/mobilnisite/slovnik/dpch/)_[Ec](/mobilnisite/slovnik/ece-c/) byl zaveden, aby poskytl standardizovanou, jednoznačnou míru síly signálu vyhrazeného kanálu na úrovni čipu v UMTS WCDMA systémech. Před formalizací 3GPP vyžadovalo kvantifikování kvality signálu ve spektrálně rozprostřených systémech jasné definice, aby bylo zajištěno konzistentní implementace a testování napříč zařízeními různých výrobců. Parametr řeší problém přesného vyhodnocení výkonové úrovně konkrétního uživatelského kanálu uprostřed širokopásmového šumu a interference charakteristických pro CDMA.

K jeho vytvoření vedla potřeba robustní uzavřené smyčky řízení výkonu, která je zásadní pro kapacitu WCDMA a kvalitu služeb. Bez přesného měření energie na čip pro vyhrazený kanál by smyčka řízení výkonu nemohla efektivně fungovat, což by vedlo buď k nadměrné interferenci (při příliš vysokém výkonu), nebo k přerušeným hovorům (při příliš nízkém výkonu). DPCH_Ec poskytuje přesnou zpětnou vazbu potřebnou pro toto řízení v reálném čase. Slouží také jako základní měření pro zkušební shodu, což umožňuje regulátorům a operátorům ověřit, že přijímače UE splňují minimální výkonnostní specifikace, a zajistit tak základní úroveň výkonu sítě a interoperability.

## Klíčové vlastnosti

- Kvantifikuje průměrnou energii na čip pseudonáhodného kódu pro DPCH
- Základní vstup pro vnitřní smyčku řízení výkonu (generování TPC příkazů)
- Používá se k výpočtu poměru DPCH Ec/Io pro hodnocení kvality spoje
- Základní parametr pro testování citlivosti a výkonu přijímače UE
- Kritický pro výpočty link budgetu a plánování RF pokrytí
- Měřený po despreadingu za použití uživatelsky specifických kanalizačních a skramblovacích kódů

## Související pojmy

- [DPDCH – Dedicated Physical Data Channel](/mobilnisite/slovnik/dpdch/)
- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)

## Definující specifikace

- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics

---

📖 **Anglický originál a plná specifikace:** [DPCH_Ec na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpch-ec/)
