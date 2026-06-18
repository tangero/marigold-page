---
slug: "dofftdd"
url: "/mobilnisite/slovnik/dofftdd/"
type: "slovnik"
title: "DOFFTDD – TDD Default DPCH Offset value"
date: 2025-01-01
abbr: "DOFFTDD"
fullName: "TDD Default DPCH Offset value"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dofftdd/"
summary: "DOFFTDD je parametr v režimu UMTS TDD, který nastavuje výchozí časový posun pro downlinkový DPCH. Zajišťuje správné zarovnání přenosů vyhrazeného kanálu v rámci specifické struktury časových slotů TDD"
---

DOFFTDD je parametr v režimu UMTS TDD, který nastavuje výchozí časový posun pro downlinkový DPCH, aby bylo zajištěno správné zarovnání přenosů vyhrazeného kanálu v rámci struktury časových slotů TDD.

## Popis

Hodnota výchozího posunu [DPCH](/mobilnisite/slovnik/dpch/) pro [TDD](/mobilnisite/slovnik/tdd/) (DOFFTDD) je časovací parametr specifikovaný v 3GPP TS 25.402 pro [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network) pracující v režimu časového duplexu (TDD). Na rozdíl od [FDD](/mobilnisite/slovnik/fdd/) používá TDD jediné kmitočtové pásmo, kde jsou přenosy rozděleny do střídajících se časových slotů pro downlink a uplink. Parametr DOFFTDD definuje výchozí časový posun, vyjádřený v čipech, který určuje počáteční bod přenosu downlinkového vyhrazeného fyzického kanálu (DPCH) v rámci jeho přiřazeného časového slotu vůči síťovému časovému referenčnímu bodu. To je klíčové pro strukturování rámu a zajištění správného zarovnání přenosů od různých uživatelů a buněk za účelem minimalizace interference.

V UMTS TDD je rádiový rámec rozdělen na 15 časových slotů, z nichž každý může být alokován jako downlinkový nebo uplinkový na základě konfigurace přepínacích bodů. DPCH může být alokován do konkrétních slotů. Hodnota DOFFTDD poskytuje základní časování pro okamžik, kdy Node B začne vysílat datová pole DPCH v jeho určeném downlinkovém slotu. Tento časový referenční bod je odvozen od systémového čísla rámce buňky a musí být koordinován, aby se zajistilo, že downlinkové přenosy z jedné buňky nepřekrývají uplinkový příjemní periodu sousední buňky nebo UE, což je významný problém v synchronizovaných TDD sítích.

Parametr funguje ve spojení s dalšími časovacími úpravami a celkovou strukturou TDD rámce. Když [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller) naváže rádiové spojení, nakonfiguruje Node B potřebnými parametry, včetně DOFFTDD pro DPCH. UE je o tomto časování informováno signalizací vyšší vrstvy (např. v [RRC](/mobilnisite/slovnik/rrc/) zprávě jako Radio Bearer Setup). UE tyto informace používá k přesnému určení, kdy má očekávat a dekódovat downlinkový DPCH ve svém přiřazeném slotu. Správné zarovnání, řízené tímto výchozím posunem, je nezbytné pro to, aby rake přijímač UE správně kombinoval vícecestné signály a aby celý systém udržoval ortogonalitu mezi různými kanalizačními kódy používanými ve stejném časovém slotu.

## K čemu slouží

DOFFTDD byl vytvořen k řešení jedinečných výzev časové synchronizace vlastních [TDD](/mobilnisite/slovnik/tdd/) systémům, kde uplink a downlink sdílejí stejný kmitočtový kanál oddělený v čase. Standardizovaný výchozí posun pro přenos downlinkového [DPCH](/mobilnisite/slovnik/dpch/) je nezbytný pro předvídatelné strukturování časové osy přenosů sítě. Bez takového parametru by byl počáteční bod přenosů vyhrazeného kanálu nejednoznačný, což by vedlo k nezarovnání mezi přenosy Node B a očekáváními UE, což by mělo za následek selhání dekódování, zvýšenou intersymbolovou interferenci a závažnou mezibuněčnou interferenci, pokud by sousední buňky nebyly časově synchronizovány.

Řeší problém vytvoření společného časového referenčního bodu pro provoz vyhrazeného kanálu v rámci složité architektury TDD slotů. To je obzvláště důležité pro počáteční přístup, předávání spojení a ve scénářích vyžadujících přísnou mezibuněčnou synchronizaci pro řízení interference (klíčový aspekt TD-SCDMA, varianty TDD). Parametr umožňuje síti efektivně spravovat rádiové prostředky tím, že poskytuje známý, konfigurovatelný kotvící bod pro downlinkové časování, na jehož základě lze provádět dynamické úpravy. Jeho specifikace v dokumentu rozhraní Iur (TS 25.402) podtrhuje jeho roli v umožnění interoperability více dodavatelů a konzistentní správy rádiových spojení napříč různými částmi UTRAN, což podporuje pokročilé funkce TDD a plánování sítě.

## Klíčové vlastnosti

- Definuje výchozí počáteční časování pro downlinkový DPCH v rámci TDD časového slotu
- Parametr měřený v čipech, klíčový pro zarovnání struktury TDD rámce
- Zabraňuje intersymbolové a mezibuněčné interferenci v synchronizovaných TDD sítích
- Signalizován prostřednictvím rozhraní Iur/Iub pro koordinované navázání rádiového spojení
- Poskytuje časový referenční bod pro příjem downlinkového DPCH v UE
- Nezbytný pro správný provoz vyhrazených kanálů v režimu UMTS TDD

## Související pojmy

- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms

---

📖 **Anglický originál a plná specifikace:** [DOFFTDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dofftdd/)
