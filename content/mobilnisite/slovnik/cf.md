---
slug: "cf"
url: "/mobilnisite/slovnik/cf/"
type: "slovnik"
title: "CF – Conversion Facility"
date: 2025-01-01
abbr: "CF"
fullName: "Conversion Facility"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cf/"
summary: "Konverzní jednotka (CF) umožňuje vzájemné propojení služeb Teletextu (Ttx) a Telexu (Tx) v sítích 3GPP. Překládá protokoly a formáty, aby umožnila fungování starších textových komunikačních služeb v r"
---

CF (Conversion Facility) je konverzní jednotka, která umožňuje vzájemné propojení služeb Teletextu a Telexu v sítích 3GPP překladem jejich protokolů a formátů za účelem zpětné kompatibility v rámci moderních mobilních systémů.

## Popis

Konverzní jednotka (CF) je síťový prvek specifikovaný ve standardech 3GPP, který poskytuje konverzi protokolů a formátů mezi službami Teletextu (Ttx) a Telexu (Tx). Teletext je informační služba založená na televizním vysílání, zatímco Telex je starší komunikační systém s dálnopisy. CF funguje jako brána, která překládá mezi různými signalizačními protokoly, znakovými kódy a přenosovými formáty používanými těmito staršími textovými službami, což jim umožňuje vzájemnou spolupráci v rámci mobilních sítí 3GPP.

Z architektonického hlediska se CF typicky nachází ve služební vrstvě sítě a rozhraní má jak s prvky jádra sítě, tak s externími služebními platformami. Obsahuje protokolové zásobníky pro protokoly Ttx i Tx spolu s konverzní logikou, která zajišťuje mapování mezi různými znakovými sadami (například ITA2 pro Telex a různé národní varianty pro Teletext), časovými charakteristikami a služebně specifickými funkcemi. CF udržuje informace o stavu relace pro aktivní konverze a zajišťuje správnou synchronizaci mezi oběma službami navzdory jejich odlišným provozním charakteristikám.

Klíčové součásti CF zahrnují vrstvu adaptace protokolů, která zajišťuje konverze na fyzické a spojové vrstvě; konverzní engine pro zprávy, který překládá obsah a formát zpráv; a služební logiku, která řídí celkový proces vzájemného propojení. CF také zahrnuje rozhraní k systémům správy sítě pro účely konfigurace, monitorování a správy poruch. Funguje transparentně pro koncové uživatele a zároveň zajišťuje, že jsou během konverze zachovány základní charakteristiky obou služeb.

CF hraje klíčovou roli při udržování kontinuity služeb pro specializované aplikace, které jsou závislé na těchto starších textových službách, zejména v odvětvích, jako jsou námořní komunikace, letectví a některé vládní služby. Poskytnutím této konverzní schopnosti mohou sítě 3GPP podporovat širší škálu komunikačních služeb, aniž by vyžadovaly od uživatelů výměnu stávajícího zařízení nebo změnu zavedených provozních postupů. CF představuje důležitý příklad toho, jak se mohou mobilní sítě vyvíjet a zároveň zachovávat zpětnou kompatibilitu s etablovanými komunikačními technologiemi.

## K čemu slouží

Konverzní jednotka (CF) byla vytvořena, aby řešila potřebu interoperability mezi staršími textovými komunikačními službami a vznikajícími mobilními sítěmi 3GPP. Služby Teletextu a Telexu byly široce nasazeny v různých průmyslových odvětvích a vládních aplikacích ještě před rozšířeným přijetím mobilních datových služeb. Tyto služby měly etablovanou uživatelskou základnu, specializované vybavení a provozní postupy, které nebylo možné snadno nahradit. CF umožnila těmto stávajícím službám pokračovat v provozu a zároveň uživatelům poskytla výhody mobility a pokrytí sítí 3GPP.

Před zavedením CF fungovaly služby Teletextu a Telexu na samostatných, vyhrazených sítích s nekompatibilními protokoly a formáty. Uživatelé vyžadující obě služby potřebovali samostatné vybavení a připojení pro každou z nich. Omezení předchozích přístupů zahrnovala duplikovanou infrastrukturu, vyšší provozní náklady a neschopnost využít možnosti mobilních sítí pro tyto textové služby. CF tyto problémy vyřešila poskytnutím standardizovaného konverzního mechanismu, který umožnil, aby byly obě služby poskytovány prostřednictvím společné infrastruktury mobilní sítě.

Historický kontext ukazuje, že CF byla obzvláště důležitá během přechodu od sítí druhé generace k sítím třetí generace, kdy operátoři usilovali o maximalizaci nabídky služeb při minimalizaci nákladů na infrastrukturu. Díky umožnění vzájemného propojení Ttx/Tx mohli mobilní operátoři přilákat uživatele ze specializovaných průmyslových odvětví závislých na těchto textových službách, čímž vytvořili nové zdroje příjmů a zároveň poskytli cennou zpětnou kompatibilitu. Vývoj CF odrážel závazek 3GPP podporovat rozmanité komunikační potřeby, jak se mobilní sítě vyvíjely za hranice jednoduchých hlasových služeb.

## Klíčové vlastnosti

- Konverze protokolů mezi signalizačními protokoly Ttx a Tx
- Překlad znakového kódování mezi různými textovými formáty
- Správa relací pro udržení kontinuity služby během konverze
- Transparentní provoz zachovávající charakteristiky služeb
- Standardizovaná rozhraní k prvkům sítě 3GPP
- Podpora starších služebních funkcí a provozních požadavků

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP
- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report

---

📖 **Anglický originál a plná specifikace:** [CF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cf/)
