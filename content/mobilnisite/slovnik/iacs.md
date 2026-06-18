---
slug: "iacs"
url: "/mobilnisite/slovnik/iacs/"
type: "slovnik"
title: "IACS – Immediate Active Codec Set"
date: 2025-01-01
abbr: "IACS"
fullName: "Immediate Active Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iacs/"
summary: "Sada řečových kodeků, které může mobilní síť okamžitě použít pro hlasové volání bez nutnosti dalšího vyjednávání nebo výměny informací o podporovaných možnostech. Umožňuje rychlejší sestavení hovoru a"
---

IACS je sada řečových kodeků, které síť může okamžitě použít pro hlasové volání bez dalšího vyjednávání, což umožňuje rychlejší sestavení hovoru a efektivní záložní řešení pro služby jako CSFB.

## Popis

Immediate Active Codec Set (IACS) je koncept definovaný ve specifikacích 3GPP, zejména v kontextu Circuit-Switched FallBack ([CSFB](/mobilnisite/slovnik/csfb/)) a kontinuity hlasových služeb. Odkazuje na předem definovanou, omezenou sadu řečových kodeků, které síť a uživatelské zařízení (UE) zaručeně podporují, aniž by bylo nutné explicitní vyjednávání podporovaných možností během sestavování hovoru. Když je zahájeno hlasové volání – zejména ve scénářích jako CSFB, kde UE přechází z LTE/5G na 2G/3G síť s přepojováním okruhů – je čas kritický. IACS poskytuje známý společný základ kodeků, aby se zabránilo zpoždění způsobenému úplným postupem vyjednávání kodeku.

Operačně je IACS typicky velmi malá sada, často tvořená jediným povinným kodekem, jako je Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) kodek při konkrétní přenosové rychlosti (např. AMR 12,2 kbps). Síť při spuštění přechodu (fallback) nebo sestavování tísňového volání může přímo přiřadit kodek z IACS. UE je v souladu se standardy 3GPP povinno podporovat kodeky v IACS. Tato vzájemná záruka umožňuje, aby signalizace sestavení hovoru obešla typickou výměnu 'seznamu kodeků'. Síť zahrne zvolený IACS kodek do zprávy pro sestavení hovoru (např. v GSM nebo UMTS Assignment Command nebo v určitých [SIP](/mobilnisite/slovnik/sip/) zprávách pro IMS) a UE tento kodek okamžitě aktivuje pro hlasový přenos.

IACS hraje klíčovou roli v architektuře mobility hlasu mezi různými rádiovými přístupovými technologiemi (inter-RAT). V postupech CSFB specifikovaných v 23.272 a odkazovaných v 28.062 používá [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) IACS k tomu, aby cílové 2G/3G rádiové přístupové síti nařídilo alokovat prostředky pro hlasové volání pomocí známého kodeku. Tím je zajištěno, že proces přechodu je zefektivněn a doba sestavení hovoru je minimalizována, což je zásadní pro uživatelský zážitek a kritické pro tísňová volání. IACS je také relevantní v kontextu Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)), kde je hlasové volání předáno z domény s přepojováním paketů (jako VoLTE) do domény s přepojováním okruhů, což opět vyžaduje rychlé a garantované sladění kodeku, aby byla zachována kontinuita hovoru bez přerušení.

## K čemu slouží

Immediate Active Codec Set byl vytvořen k řešení problému zpoždění při sestavování hovoru, zejména ve scénářích zahrnujících přechod (fallback) z paketově přepínaných sítí na sítě s přepojováním okruhů pro hlasové služby. Se zavedením LTE, kterému zpočátku chyběla nativní doména hlasu s přepojováním okruhů, byl [CSFB](/mobilnisite/slovnik/csfb/) vyvinut jako přechodné hlasové řešení. Klíčovou výzvou bylo minimalizovat dodatečné zpoždění vzniklé při přesměrování UE z LTE na 2G/3G síť za účelem přijetí hlasového hovoru. Významná část doby sestavení hovoru v legacy systémech byla věnována vyjednávání kodeku – výměně seznamů podporovaných kodeků a výběru společného kodeku.

IACS tento krok vyjednávání pro přechodová (fallback) a tísňová volání eliminuje tím, že předem definuje minimální, univerzálně podporovanou sadu kodeků. Tento účel je hnán potřebou spolehlivosti a rychlosti služby. U tísňových hovorů se počítá každá milisekunda. U komerčního CSFB zkrácení doby sestavení hovoru zlepšuje vnímání služby uživatelem a splňuje regulatorní požadavky na doby sestavení hovoru. Historicky, před existencí takových mechanismů, mohly předávání mezi systémy nebo přechody (fallback) trpět selháním při sestavování hovoru nebo dlouhými zpožděními, pokud vyjednávání kodeku selhalo nebo bylo pomalé. IACS poskytuje deterministické, rychlé řešení. Řeší omezení plně flexibilního vyjednávání kodeku tím, že obětuje část optimalizace výběru kodeku ve prospěch rychlosti a garantovaného úspěchu v časově kritických scénářích, a zajišťuje tak robustní kontinuitu hlasových služeb napříč různými generacemi mobilních sítí.

## Klíčové vlastnosti

- Předem definovaná sada kodeků, jejichž podpora je garantována na straně UE i sítí
- Umožňuje obejít úplné postupy vyjednávání kodeků
- Snižuje dobu sestavení hlasového hovoru, což je kritické pro CSFB a tísňová volání
- Typicky zahrnuje povinné kodeky jako AMR při specifických přenosových rychlostech
- Používá se v signalizaci pro přiřazení domény s přepojováním okruhů
- Podporuje kontinuitu služeb ve scénářích SRVCC a mobility mezi různými rádiovými přístupovými technologiemi (inter-RAT)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [IACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/iacs/)
