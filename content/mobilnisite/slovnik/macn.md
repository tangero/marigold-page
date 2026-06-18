---
slug: "macn"
url: "/mobilnisite/slovnik/macn/"
type: "slovnik"
title: "MACN – Mobile Allocation Channel Number"
date: 2026-01-01
abbr: "MACN"
fullName: "Mobile Allocation Channel Number"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/macn/"
summary: "V GSM jde o číselný index odkazující na konkrétní absolutní rádiový kmitočtový kanál v seznamu mobilní alokace. Síť jej používá k instruování mobilní stanice, kterou timeslot(y) a kmitočet má použít p"
---

MACN je číselný index v GSM, který identifikuje konkrétní absolutní rádiový kmitočtový kanál v rámci seznamu mobilní alokace pro směrování paketového datového provozu mobilní stanice.

## Popis

Mobile Allocation Channel Number (MACN) je základní parametr v řízení rádiových zdrojů GSM, konkrétně pro službu General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) a Enhanced Data rates for GSM Evolution ([EDGE](/mobilnisite/slovnik/edge/)). Funguje v rámci mechanismů přeskakování kmitočtů a alokace kanálů. Síť definuje seznam 'Mobile Allocation' ([MA](/mobilnisite/slovnik/ma/)), což je uspořádaná množina čísel absolutních rádiových kmitočtových kanálů ([ARFCN](/mobilnisite/slovnik/arfcn/)), které lze pro spojení použít. MACN je prostě index do tohoto seznamu. Například, pokud seznam MA obsahuje ARFCN [23, 45, 67, 89], pak MACN=0 odkazuje na ARFCN 23, MACN=1 na ARFCN 45 atd.

Když síť přiděluje zdroje pro přenos paketových dat, vysílá k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) přiřazovací zprávy. Tyto zprávy specifikují timeslot(y) a, což je klíčové, vzor přeskakování kmitočtů. Tento vzor je definován seznamem MA a číslem hopping sekvence ([HSN](/mobilnisite/slovnik/hsn/)). Aby síť sdělila MS, který konkrétní kmitočet má v daný okamžik použít, poskytne výchozí bod nazvaný Mobile Allocation Index Offset ([MAIO](/mobilnisite/slovnik/maio/)) a využívá koncept MACN v rámci algoritmu. MS vypočítá kmitočet pro jakékoli dané období rádiového bloku pomocí vzorce, který bere v úvahu HSN, velikost seznamu MA a aktuální číslo bloku, čímž efektivně prochází indexy MACN v pseudonáhodném pořadí určeném HSN.

Z architektonického hlediska je MACN parametr generovaný a řízený Base Station Controllerem ([BSC](/mobilnisite/slovnik/bsc/)) nebo Packet Control Unit (PCU). Je komunikován k MS prostřednictvím zpráv vrstvy 3 pro řízení rádiových zdrojů, jako jsou PACKET TIMESLOT RECONFIGURE nebo PACKET CHANNEL REQUEST. Fyzická vrstva MS používá tuto informaci spolu s údaji z přiřazeného timeslotu k naladění svého vysílače a přijímače na správný kmitočet pro každý TDMA rámec. Tento mechanismus umožňuje efektivní přeskakování kmitočtů, které je v mnoha nasazeních pro GPRS/EDGE povinné pro potlačení interference a útlumu, čímž se zlepšuje kvalita spoje a celková spektrální účinnost. Použití indexu (MACN) namísto plného ARFCN v signalizačních zprávách šetří cennou šířku pásma na rozhraní vzduch.

## K čemu slouží

MACN byl vyvinut jako součást standardu GSM k umožnění efektivní a dynamické alokace rádiových zdrojů pro paketově orientované datové služby (GPRS), což byla významná evoluce oproti původnímu GSM navrženému primárně pro okruhově orientované hovory. U okruhově orientovaných hovorů byl přenosovému kanálu (TCH) přiřazen pevný kmitočet nebo jednoduchá hopping sekvence po dobu volání. Paketová data se svým prchavým charakterem vyžadovala flexibilnější systém, kde by kanály mohly být rychle přidělovány a uvolňovány po blocích více uživatelům sdílejícím stejný timeslot.

Použití seznamu Mobile Allocation indexovaného pomocí MACN vyřešilo několik problémů. Za prvé snížilo signalizační režii: namísto vysílání plného ARFCN (který vyžaduje více bitů) pro každé přiřazení nebo hoppingový výpočet mohla síť vysílat kratší index. Za druhé oddělilo logické přiřazení kanálu od fyzického kmitočtu, což umožnilo síti centrálně (prostřednictvím BSC/PCU) spravovat hoppingové sekvence a jednoduše instruovat MS, jak navigovat předdefinovaný seznam. To bylo klíčové pro implementaci diverzity interference prostřednictvím přeskakování kmitočtů v paketové doméně, aby odpovídala odolnosti již dosažené v GSM pro hlas. Mechanismus MACN byl tedy klíčovým prvkem pro to, aby se GPRS/EDGE stalo spektrálně účinnou a spolehlivou technologií mobilních dat v široké geografické oblasti.

## Klíčové vlastnosti

- Slouží jako index do seznamu Mobile Allocation (MA) obsahujícího ARFCN pro dané spojení.
- Zásadní pro definování sekvence přeskakování kmitočtů při přenosech paketových dat v GSM/GPRS/EDGE.
- Snižuje signalizační režii na rozhraní vzduch ve srovnání s přenosem plných hodnot ARFCN.
- Používá se v zprávách pro přiřazení rádiových zdrojů od sítě (BSC/PCU) k mobilní stanici.
- MS používá index MACN, HSN a MAIO k výpočtu skutečného vysílacího/přijímacího kmitočtu pro každý TDMA blok.
- Klíčový parametr pro dynamickou alokaci paketových zdrojů a potlačení interference prostřednictvím přeskakování kmitočtů.

## Související pojmy

- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)
- [MAIO – Mobile Allocation Index Offset](/mobilnisite/slovnik/maio/)
- [HSN – Hopping Sequence Number](/mobilnisite/slovnik/hsn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [PCU – Packet Control Unit](/mobilnisite/slovnik/pcu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements

---

📖 **Anglický originál a plná specifikace:** [MACN na 3GPP Explorer](https://3gpp-explorer.com/glossary/macn/)
