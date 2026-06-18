---
slug: "eeirp"
url: "/mobilnisite/slovnik/eeirp/"
type: "slovnik"
title: "EEIRP – Expected Equivalent Isotropic Radiated Power"
date: 2025-01-01
abbr: "EEIRP"
fullName: "Expected Equivalent Isotropic Radiated Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eeirp/"
summary: "Vypočtená metrika představující celkový výkon, který by vyzařovala izotropní anténa, aby vytvořila stejnou maximální hustotu výkonu jako skutečná anténa ve svém směru největšího vyzařování. Je klíčová"
---

EEIRP je vypočtený celkový výkon, který by musela vyzařovat izotropní anténa, aby vyrovnala maximální hustotu výkonu skutečné antény ve svém směru největšího vyzařování.

## Popis

Expected Equivalent Isotropic Radiated Power (EEIRP, očekávaný ekvivalentní výkon vyzářený izotropní anténou) je základním parametrem v radiofrekvenční ([RF](/mobilnisite/slovnik/rf/)) technice a plánování sítí, standardizovaným v 3GPP Release 19 pro New Radio (NR). Představuje teoretický vyzářený výkon vysílacího systému, který zohledňuje výstupní výkon rádiové jednotky, ztráty v kabelech a konektorech a směrový zisk antény. Konkrétně je EEIRP součinem výkonu dodávaného do antény a zisku antény vztaženého k izotropnímu zářiči (dBi) ve směru největšího vyzařování, mínus případné ztraty ve výživném vedení. Poskytuje standardizovaný způsob kvantifikace efektivního vyzářeného výkonu ve směru hlavního paprsku, umožňující přímé srovnání různých konfigurací základnových stanic.

Z architektonického hlediska je EEIRP klíčovým vstupem pro RF plánovací nástroje používané operátory sítí. Počítá se ve fázi návrhu sítě pro každou lokalitu buňky a anténní sektor. Výpočet zahrnuje maximální výstupní výkon základnové stanice (jak je definováno v specifikacích jako TS 38.104 pro rádiový přenos základnové stanice), dokumentovanou vložnou ztrátu koaxiálních kabelů a propojek spojujících rádio s anténou a špičkový zisk antény získaný z listu dat jejího vyzařovacího diagramu. Vzorec je typicky: EEIRP (dBm) = Výstupní výkon vysílače (dBm) - Ztráty ve vedení (dB) + Zisk antény (dBi).

Fungování EEIRP v praxi zahrnuje několik úrovní. Za prvé definuje plochu pokrytí buňky. Vyšší EEIRP obecně znamená větší oblast pokrytí pro danou frekvenci a prostředí. Za druhé, a to je klíčové, se používá k zajištění regulatorní shody. Národní regulátoři stanovují maximální povolené úrovně EEIRP pro různá frekvenční pásma za účelem kontroly interference a omezení vystavení veřejnosti RF polím. Operátoři sítí musí prokázat, že jejich nasazené zařízení tyto limity nepřekračuje, což činí přesný výpočet a dokumentaci EEIRP nezbytnou. Za třetí, v rámci 3GPP se EEIRP používá jako reference pro definování tříd základnových stanic (např. široká oblast, střední dosah, lokální oblast) a pro specifikaci požadavků ve standardech pro testování shody jako TS 38.141.

Jeho role sahá k optimalizaci výkonu a správě interference. Modelováním EEIRP sousedních buněk mohou operátoři předpovídat možné scénáře interference a upravovat parametry jako sklon antény nebo výkon pro optimalizaci poměru signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) v síti. V masivních [MIMO](/mobilnisite/slovnik/mimo/) systémech s beamformingem se tento koncept aplikuje na každý paprsek, kde je efektivní výkon vyzářený izotropní anténou ([EIRP](/mobilnisite/slovnik/eirp/)) každého formovaného paprsku dynamicky řízen a EEIRP představuje očekávanou maximální hodnotu za definovaných podmínek. To je klíčové pro zajištění, že celkový výkon z více paprsků zůstává v rámci regulatorních omezení při maximalizaci prostorové efektivity.

## K čemu slouží

EEIRP byl formálně definován a zdůrazněn v 3GPP Release 19, aby poskytl jasnou, standardizovanou metriku pro vyzářený výkon, která je nezbytná pro stále složitější [RF](/mobilnisite/slovnik/rf/) prostředí 5G-Advanced a budoucích 6G systémů. Předchozí přístupy se často spoléhaly na jednodušší metriky, jako je vedený výkon (výkon na anténním portu), nebo používaly termín [EIRP](/mobilnisite/slovnik/eirp/) bez standardizované metodiky výpočtu 'očekávané' hodnoty, což vedlo k možným nekonzistencím v plánování sítí, specifikaci zařízení a regulatorním hlášeních napříč různými dodavateli a operátory.

Primární problém, který EEIRP řeší, je potřeba spolehlivé a reprodukovatelné reference pro maximální vyzářený výkon základnové stanice. To je kritické z několika důvodů. Za prvé zajišťuje shodu s přísnými mezinárodními ([ITU](/mobilnisite/slovnik/itu/)) a národními regulatorními limity RF emisí, které jsou vždy definovány z hlediska efektivního vyzářeného výkonu za účelem ochrany před škodlivou interferencí a řízení obav o veřejné zdraví. Za druhé poskytuje společný základ pro plánování kapacity sítě a pokrytí. Přesné hodnoty EEIRP umožňují plánovačům správně simulovat šíření rádiových vln, předpovídat hranice buněk a dimenzovat sítě pro splnění cílů kvality služeb, zejména s použitím nového spektra v pásmech FR2 (mmWave), kde je pokrytí vysoce směrové.

Motivace pro jeho standardizaci pramení z nasazení pokročilých anténních systémů ([AAS](/mobilnisite/slovnik/aas/)) a beamformingu. V těchto systémech není vyzářený výkon jednou statickou hodnotou, ale dynamicky se mění s beamformingovými váhami. EEIRP poskytuje konzervativní, statickou 'očekávanou maximální' hodnotu, kterou mohou regulátoři a plánovači sítí používat pro analýzu nejhoršího případu. Řeší omezení předchozích, méně přesných metod tím, že ukládá konkrétní výpočet zahrnující všechny relevantní systémové ztráty a zisky, čímž snižuje nejednoznačnost, zlepšuje interoperabilitu mezi nástroji pro plánování sítí a zajišťuje, že produkty základnových stanic od různých výrobců jsou hodnoceny na konzistentním výkonovém základu jak z hlediska výkonu, tak shody.

## Klíčové vlastnosti

- Standardizovaný výpočet zahrnující výkon vysílače, ztráty ve vedení a zisk antény
- Referenční metrika pro regulatorní shodu s limity pro vystavení RF záření a emise
- Základní vstup pro nástroje předpovědi RF pokrytí a plánování sítě
- Definuje výkonové třídy základnových stanic a požadavky pro testování shody
- Poskytuje konzistentní základ pro srovnání vyzářeného výkonu různých modelů základnových stanic
- Nezbytný pro analýzu interference a koordinaci mezi sousedními buňkami a operátory

## Související pojmy

- [EIRP – Effective Isotropic Radiated Power](/mobilnisite/slovnik/eirp/)

## Definující specifikace

- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TR 38.908** (Rel-19) — NR Band n104 FSS UL Protection

---

📖 **Anglický originál a plná specifikace:** [EEIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/eeirp/)
