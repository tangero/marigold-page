---
slug: "gsm-r"
url: "/mobilnisite/slovnik/gsm-r/"
type: "slovnik"
title: "GSM-R – Global System for Mobile Communications – Rail(way)"
date: 2025-01-01
abbr: "GSM-R"
fullName: "Global System for Mobile Communications – Rail(way)"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gsm-r/"
summary: "Specializovaný mobilní komunikační systém založený na GSM, navržený pro železniční provoz. Poskytuje služby hlasové a datové komunikace s požadavky na vysokou spolehlivost (mission-critical) pro řízen"
---

GSM-R je specializovaný mobilní komunikační systém založený na GSM, navržený pro poskytování služeb hlasové a datové komunikace s požadavky na vysokou spolehlivost (mission-critical) pro železniční provoz, včetně řízení vlaků a dispečinku.

## Popis

GSM-R je digitální standard mobilní komunikace odvozený od GSM, ale přizpůsobený speciálně pro železniční aplikace. Funguje ve vyhrazených kmitočtových pásmech, typicky kolem 900 MHz, aby zajistil spolehlivé pokrytí podél železničních tratí, v tunelech a na nádražích. Architektura systému je založena na základních síťových prvcích GSM, včetně ústředen mobilní komunikace (MSCs), registrů domácích účastníků (HLRs) a subsystémů základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), ale s vylepšeními pro podporu funkcí specifických pro železnici, jako je funkční adresování (Functional Addressing), adresování závislé na poloze (Location-Dependent Addressing) a služba hlasového vysílání ([VBS](/mobilnisite/slovnik/vbs/)) a služba skupinového hovoru ([VGCS](/mobilnisite/slovnik/vgcs/)). Tyto funkce umožňují efektivní komunikaci mezi strojvedoucími, dispečery a údržbářským personálem a podporují kritické operace, jako je řízení vlaků a nouzová komunikace.

Klíčové součásti GSM-R zahrnují mobilní stanice GSM-R (palubní jednotky a ruční terminály), základnové stanice rozmístěné podél železniční trasy a jádrovou síť GSM-R, která je propojena se železničními zabezpečovacími systémy, jako je Evropský vlakový zabezpečovací systém (ETCS). Systém podporuje jak hlasové služby s přepojováním okruhů, nezbytné pro přímou komunikaci strojvedoucího s dispečerem, tak datové služby s přepojováním paketů pro aplikace, jako je automatické řízení vlaku a monitorování trati. GSM-R zajišťuje vysokou dostupnost a spolehlivost prostřednictvím funkcí, jako je rychlé navázání hovoru, mechanismy priority a přerušení (preemption) a robustní postupy předávání hovoru (handover) optimalizované pro prostředí vysokorychlostních vlaků.

V provozu se GSM-R integruje se železničními zabezpečovacími a řídicími systémy, aby umožnil funkce jako přenos povolení k jízdě a automatický vlakový zabezpečovač. Systém používá funkční adresování (Functional Addressing), kdy je uživatel adresován podle své role (např. 'Strojvedoucí vlaku 1234') a nikoli osobního čísla, což umožňuje dynamickou a kontextově citlivou komunikaci. Adresování závislé na poloze (Location-Dependent Addressing) směruje hovory na příslušné dispečerské centrum na základě geografické polohy vlaku. GSM-R také podporuje skupinové hovory a vysílací hovory, které jsou klíčové pro koordinaci zásahů při mimořádných událostech nebo údržbových činností mezi více stranami. Jeho role je zásadní pro moderní železniční komunikaci, neboť poskytuje standardizovanou, interoperabilní platformu, která zvyšuje bezpečnost, efektivitu a kapacitu železničních sítí.

## K čemu slouží

GSM-R byl vytvořen, aby odstranil omezení analogových železničních rádiových systémů, které byly roztříštěné, postrádaly interoperabilitu a nabízely omezenou kapacitu a funkčnost. Předchozí systémy se lišily podle země a regionu, což bránilo přeshraničnímu železničnímu provozu a zvyšovalo náklady. Potřeba jednotného, digitálního komunikačního standardu se stala naléhavou s růstem vysokorychlostní železnice a poptávkou po integrovaných systémech řízení vlaků, jako je ETCS, které vyžadují spolehlivé datové spoje pro bezpečnostně kritické aplikace.

Hlavní motivací bylo zvýšit bezpečnost a provozní efektivitu železnice poskytnutím robustního, standardizovaného systému mobilní komunikace. GSM-R řeší problémy, jako je neefektivní hlasová komunikace mezi vlakovými četami a dispečery, nedostatečná podpora přenosu dat pro zabezpečovací zařízení a špatná interoperabilita mezi různými národními železničními sítěmi. Tím, že využívá technologii GSM, nabídl ověřenou, škálovatelnou platformu s funkcemi přizpůsobenými pro železnici, což umožňuje bezproblémovou komunikaci přes hranice a podporuje pokročilé systémy řízení a správy vlaků.

Historicky se GSM-R objevil na konci 90. a na počátku 2000. let jako součást evropských snah o modernizaci železnice, přičemž standardizace v 3GPP začala ve vydání 8, aby bylo zajištěno sladění s širšími mobilními standardy. Řeší specifické výzvy železničního prostředí, jako je vysokorychlostní mobilita, rozšířené pokrytí v odlehlých oblastech a spolehlivost s požadavky na vysokou dostupnost (mission-critical), a vytváří tak základ pro budoucí vývoj železniční komunikace směrem k systémům založeným na IP.

## Klíčové vlastnosti

- Funkční adresování (Functional Addressing) pro komunikaci založenou na rolích
- Adresování závislé na poloze (Location-Dependent Addressing) pro dynamické směrování hovorů
- Služba hlasového vysílání (VBS) a služba skupinového hovoru (VGCS)
- Priorita a přerušení (preemption) pro bezpečnostně kritické hovory
- Předávání hovoru (handover) optimalizované pro vysoké rychlosti v železničních koridorech
- Integrace s ETCS pro signalizaci řízení vlaků

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [GSM-R na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsm-r/)
