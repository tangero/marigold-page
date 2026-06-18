---
slug: "cdm"
url: "/mobilnisite/slovnik/cdm/"
type: "slovnik"
title: "CDM – Consolidated Data Model"
date: 2025-01-01
abbr: "CDM"
fullName: "Consolidated Data Model"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cdm/"
summary: "Consolidated Data Model (CDM) je standardizovaný datový model v rámci 3GPP pro správu sítě. Poskytuje jednotný strukturovaný rámec pro reprezentaci síťových prostředků, služeb a dat o výkonu, což umož"
---

CDM je standardizovaný datový model 3GPP, který poskytuje jednotný rámec pro reprezentaci síťových prostředků a služeb za účelem konzistentní správy v sítích s více dodavateli a technologiemi.

## Popis

Consolidated Data Model (CDM) je klíčovou součástí architektury správy 3GPP, navrženou tak, aby poskytovala jednotný koherentní informační model pro všechna data správy sítě. Funguje jako sémantická vrstva, která abstrahuje různorodá a často dodavatelsky specifická datová vyjádření síťových prvků, služeb a účastníků do standardizovaného formátu. Tento model je definován pomocí strukturovaných informačních modelovacích jazyků a je nedílnou součástí rámců 3GPP Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)) a Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)). Stanovením společných definic entit, atributů a vztahů CDM zajišťuje, že systémy správy, rozhraní směrem na sever (northbound) a analytické nástroje pracují s konzistentní sadou dat, což je klíčové pro automatizované síťové operace, zajištění služeb a správu životního cyklu.

Architektonicky CDM není jedinou monolitickou specifikací, ale harmonizovanou sadou datových definic integrovaných napříč různými Technickými specifikacemi (TS) 3GPP, zejména těmi pod pracovní skupinou Service and System Aspects Working Group 5 (SA5). Zahrnuje data týkající se fyzických a virtuálních síťových prostředků (např. gNB, [UPF](/mobilnisite/slovnik/upf/), síťové řezy), služeb (např. [PDU](/mobilnisite/slovnik/pdu/) sezení, QoS toky), měření výkonu, informací o poruchách, konfiguračních parametrů a profilů účastníků. Model je navržen jako rozšiřitelný a technologicky neutrální, podporující správu komponent 4G EPC, 5G Core (5GC) a Radio Access Network (RAN). Mezi klíčové komponenty patří definované třídy objektů, jejich atributy, datové typy a vztahy mezi nimi, které jsou dokumentovány ve specifikacích jako TS 28.622 pro správu výkonu a TS 28.541 pro správu síťových prostředků 5G.

V provozu slouží CDM jako kanonický zdroj pravdy pro data správy v rámci rámce 3GPP. Funkce správy, jako jsou systémy Network Management ([NM](/mobilnisite/slovnik/nm/)) a Element Management ([EM](/mobilnisite/slovnik/em/)), mapují své nativní informační modely na CDM. Toto mapování umožňuje standardizovanou výměnu dat přes rozhraní jako je Itf-N (northbound interface) a podporuje služby správy, jako je zřizování, monitorování a analýza. Například když systém správy výkonu sbírá klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) z gNB, jsou tyto metriky strukturovány podle definic CDM před zpracováním nebo hlášením. Tato konzistence je zásadní pro automatizaci s uzavřenou smyčkou, kde analytické funkce (např. NWDAF) zpracovávají data ve formátu CDM, aby generovaly poznatky a spouštěly automatizované akce prostřednictvím vrstvy Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)).

Role CDM přesahuje pouhou reprezentaci dat; je základním kamenem pro dosažení bezdotykové správy sítě a služeb (ZSM) a usnadnění správy založené na záměru (intent-based). Poskytnutím jednotné datové struktury snižuje integrační složitost, minimalizuje režii transformace dat a umožňuje škálovatelnou správu více domén. V sítích 5G, s důrazem na síťové řezy, edge computing a dynamické přidělování prostředků, CDM zajišťuje, že data správy specifická pro řezy, metriky využití prostředků a smlouvy o úrovni služeb (SLA) jsou modelovány konzistentně. To umožňuje operátorům spravovat složité nasazení služeb end-to-end, od RAN přes core až po aplikační vrstvu, pomocí společného datového jazyka, který podporuje jak rozhodnutí v reálném čase pro provoz, tak dlouhodobé strategické plánování.

## K čemu slouží

Consolidated Data Model byl vytvořen, aby řešil významné provozní výzvy plynoucí z množství různorodých, dodavatelsky specifických datových modelů v telekomunikačních sítích. Před jeho zavedením operátoři spravovali prostředí s více dodavateli, kde každý dodavatel zařízení používal vlastní proprietární informační modely pro reprezentaci síťových prostředků a dat o výkonu. Tato různorodost vedla ke složitým, nákladným integracím, omezené interoperabilitě a neefektivním procesům správy. Operátoři museli vyvíjet vlastní adaptéry a provádět rozsáhlou normalizaci dat, aby dosáhli jednotného pohledu na síť, což zpomalovalo nasazování služeb, bránilo automatizaci a zvyšovalo provozní výdaje. CDM byl motivován potřebou standardizovaného, dodavatelsky neutrálního datového modelu, který by mohl sloužit jako společný jazyk pro všechny interakce správy, čímž by zjednodušil síťové operace a umožnil škálovatelná řešení správy.

Historicky získal tlak na standardizaci dat správy na síle s evolucí směrem k plně IP sítím a zavedením LTE v 3GPP Release 8. Avšak s nástupem 5G a jeho přidruženými složitostmi – jako jsou síťové řezy, cloud-nativní architektury a massive IoT – se limity fragmentovaných datových modelů staly neudržitelnými. Pracovní skupina 3GPP SA5 uznala, že bez konsolidovaného přístupu by byla správa dynamické, softwarově definované povahy sítí 5G nepraktická. CDM poskytuje základní datový rámec nezbytný pro podporu pokročilých paradigmat správy, jako je automatizace s uzavřenou smyčkou, analýzy řízené umělou inteligencí a síťování založené na záměru. Řešením problému datových sil umožňuje operátorům implementovat efektivní, automatizované pracovní postupy pro zřizování, zajištění služeb a optimalizaci napříč hybridními síťovými infrastrukturami.

Dále CDM řeší potřebu konzistentní expozice dat aplikacím vyšší vrstvy a poskytovatelům služeb třetích stran. V moderních telekomunikačních ekosystémech jsou síťové schopnosti často vystavovány prostřednictvím API, aby umožnily nové služby a obchodní modely. Standardizovaný datový model zajišťuje, že tato API dodávají data v předvídatelném, dobře definovaném formátu, což podporuje inovace a snižuje dobu vývoje pro externí aplikace. Poskytnutím jednotného zdroje pravdy CDM také zvyšuje přesnost a spolehlivost síťových analýz, což umožňuje efektivnější analýzu hlavní příčiny, plánování kapacity a správu kvality služeb. Jeho konečným účelem je snížit provozní bariéry, urychlit digitální transformaci a podporovat agilní, službami řízené operace vyžadované v éře 5G a dále.

## Klíčové vlastnosti

- Standardizované sémantické definice pro síťové prostředky, služby a data o výkonu
- Dodavatelsky neutrální model umožňující interoperabilitu více dodavatelů a technologií
- Podpora jak fyzických, tak virtualizovaných síťových funkcí (VNFs/CNFs)
- Integrace s rámci správy 3GPP jako MDA a NWDAF pro analýzu
- Rozšiřitelný design pro akomodaci nových síťových technologií a služeb
- Základ pro automatizovanou správu, operace s uzavřenou smyčkou a síťování založené na záměru (intent-based)

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- **TR 32.901** (Rel-19) — UDC Application Data Models Study
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO

---

📖 **Anglický originál a plná specifikace:** [CDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdm/)
