---
slug: "matf"
url: "/mobilnisite/slovnik/matf/"
type: "slovnik"
title: "MATF – MAP Application Terminating Function"
date: 2025-01-01
abbr: "MATF"
fullName: "MAP Application Terminating Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/matf/"
summary: "Funkce v jádru sítě v legacy sítích GSM/UMTS, která ukončuje signalizační protokol Mobile Application Part (MAP). Zpracovává signalizaci pro správu mobility a služeb účastníků, slouží jako brána nebo"
---

MATF je funkce v jádru sítě v legacy sítích GSM/UMTS, která ukončuje protokol MAP za účelem zpracování signalizace pro správu mobility a služeb účastníků mezi prvky, jako jsou HLR a VLR.

## Popis

[MAP](/mobilnisite/slovnik/map/) Application Terminating Function (MATF) je klíčová signalizační komponenta v jádru sítě (CN) legacy systémů 2G GSM a 3G UMTS. Působí jako funkční entita, která ukončuje signalizační protokol Mobile Application Part (MAP), jenž je primárním signalizačním protokolem pro komunikaci mezi uzly jádra sítě, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Visitor Location Register (VLR), Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)). MATF je zodpovědná za zpracování, interpretaci a odpovídání na MAP zprávy, čímž zajišťuje korektní provedení procedur spojených se správou mobility, zpracováním hovorů a doplňkovými službami.

Z architektonického hlediska není MATF samostatným fyzickým uzlem, nýbrž logickou funkcí, kterou lze implementovat v rámci různých síťových prvků. Například MSC obsahuje MATF pro obsluhu MAP dialogů s HLR při úkonech, jako je aktualizace polohy účastníka nebo získávání směrovacích informací pro mobilní příchozí hovory. Podobně VLR zahrnuje MATF pro komunikaci s HLR při správě dat účastníka. Tato funkce zapouzdřuje aplikační logiku protokolu MAP, spravuje identifikátory transakcí, zpracovává chyby a zajišťuje spolehlivou výměnu informací po základních transportních vrstvách Signalizačního systému č. 7 (SS7).

Její role je zásadní pro okruhově spínanou doménu, usnadňuje klíčové operace jako aktualizace polohy, předávání hovoru (handover), autentizaci účastníka a doručování služby krátkých zpráv (SMS). Tím, že poskytuje standardizovaný koncový bod pro MAP signalizaci, umožňuje MATF interoperabilitu mezi síťovými prvky od různých dodavatelů, což byl základní kámen globálního úspěchu GSM a UMTS. S vývojem sítí směrem k architektuře All-IP v 4G LTE a 5G význam MATF poklesl s vyřazováním okruhově spínaného jádra sítě a nahrazením protokolu MAP rozhraními S6a/S6d založenými na Diameter a později rozhraními s architekturou založenou na službách (service-based) využívajícími [HTTP](/mobilnisite/slovnik/http/)/2.

## K čemu slouží

MATF byla vytvořena, aby poskytla standardizovaný a spolehlivý koncový bod pro signalizační protokol [MAP](/mobilnisite/slovnik/map/), což bylo nezbytné pro automatizaci správy mobility a poskytování služeb účastníkům v sítích 2G a 3G. Před jejím formalizováním byla potřeba bezproblémové komunikace mezi různými síťovými registry (jako [HLR](/mobilnisite/slovnik/hlr/) a VLR) pro sledování mobilních účastníků a směrování hovorů motivací k vývoji robustního protokolu na aplikační vrstvě. MATF vyřešila problém interoperability definováním jasné funkční hranice, kde lze zahajovat, udržovat a ukončovat MAP dialogy, což zajišťovalo, že kritické procedury jako aktualizace polohy nebo zřízení hovoru mohou spolehlivě probíhat v síťových nasazeních s více dodavateli.

Historicky zavedení protokolu MAP a jeho ukončovacích funkcí představovalo významný vývoj od starších, více manuálních nebo proprietárních architektur mobilních sítí. Řešilo to omezení předchozích přístupů, kterým chyběla jednotná mezinárodní norma pro signalizaci nesouvisející s hovory mezi síťovými databázemi. Zapouzdřením této složitosti umožnila MATF výrobcům síťových zařízení a operátorům vyvíjet a nasazovat škálovatelné, automatizované systémy schopné podporovat rychlý růst počtu mobilních účastníků a zavádění pokročilých služeb, jako je roaming a SMS, které byly silně závislé na dotazech a aktualizacích databází v reálném čase.

## Klíčové vlastnosti

- Ukončuje signalizační protokol Mobile Application Part (MAP)
- Umožňuje procedury správy mobility, jako je aktualizace polohy a předání hovoru (handover)
- Usnadňuje získávání a správu dat účastníka mezi HLR a VLR
- Podporuje směrování a doručení mobilních příchozích hovorů
- Zpracovává aktivaci a dotazování na doplňkové služby
- Poskytuje standardizované rozhraní pro interoperabilitu mezi uzly jádra sítě

## Související pojmy

- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [MATF na 3GPP Explorer](https://3gpp-explorer.com/glossary/matf/)
