---
slug: "cbim"
url: "/mobilnisite/slovnik/cbim/"
type: "slovnik"
title: "CBIM – Common Baseline Information Model"
date: 2025-01-01
abbr: "CBIM"
fullName: "Common Baseline Information Model"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cbim/"
summary: "CBIM je standardizovaný informační model definovaný organizací 3GPP pro správu sítí. Poskytuje společný rámec pro reprezentaci spravovaných objektů a jejich vztahů napříč různými síťovými doménami a d"
---

CBIM je 3GPP-standardizovaný informační model, který poskytuje společný rámec pro reprezentaci spravovaných objektů za účelem konzistentní správy sítí ve více-dodavatelském prostředí.

## Popis

Common Baseline Information Model (CBIM) je komplexní rámec pro informační modelování specifikovaný v dokumentech pro správu v rámci 3GPP, zejména v dokumentech řady 32. Slouží jako základní datový model pro reprezentaci všech spravovaných entit v rámci 3GPP sítě, včetně síťových elementů, síťových funkcí, služeb a účastníků. CBIM definuje strukturu, atributy, vztahy a chování těchto spravovaných objektů za použití objektově orientovaných principů, čímž zajišťuje, že systémy správy mohou interagovat se síťovými prostředky konzistentním a předvídatelným způsobem bez ohledu na podkladovou implementaci.

Architektonicky je CBIM organizován kolem několika klíčových konceptů: spravovaných objektů, které reprezentují fyzické nebo logické prostředky; atributů, které popisují vlastnosti těchto objektů; operací, které definují, jaké akce lze na objektech provádět; notifikací, které umožňují řízení řízené událostmi; a vztahů, které definují, jak jsou objekty vzájemně propojeny. Model využívá dědičné hierarchie, kde specializované objekty dědí vlastnosti od obecnějších rodičovských tříd, což umožňuje rozšiřitelnost při zachování konzistence. Tato hierarchická struktura umožňuje systémům správy porozumět schopnostem a omezením různých síťových elementů prostřednictvím standardizovaných rozhraní.

CBIM funguje tak, že poskytuje společný jazyk pro výměnu informací o správě mezi síťovými elementy a systémy správy. Když je síťový element nasazen, zpřístupňuje své spravovatelné aspekty prostřednictvím rozhraní kompatibilních s CBIM, obvykle za použití protokolů jako [SNMP](/mobilnisite/slovnik/snmp/) nebo NETCONF/YANG. Aplikace správy pak mohou tyto elementy objevovat, monitorovat, konfigurovat a řídit za použití standardizovaných operací definovaných v modelu. Model zahrnuje podrobné specifikace pro správu konfigurace (umožňující nastavování a získávání parametrů), správu poruch (umožňující hlášení alarmů a diagnostiku), správu výkonu (shromažďování čítačů a měření) a správu zabezpečení (řízení přístupu a auditování změn).

Klíčové komponenty CBIM zahrnují Jádrový informační model (Core Information Model), který definuje základní třídy a vztahy; Doménově specifická rozšíření (Domain-Specific Extensions), která přidávají specializované objekty pro konkrétní síťové domény jako RAN, Core nebo IMS; a Definice rozhraní pro správu (Management Interface Definitions), které specifikují, jak je model zpřístupněn prostřednictvím různých protokolů. Model také zahrnuje komplexní metadata popisující omezení, výchozí hodnoty a charakteristiky chování spravovaných objektů. Tato metadata umožňují inteligentním aplikacím správy validovat konfigurace, detekovat nekonzistence a poskytovat usměrněné konfigurační pracovní postupy.

Role CBIM v síti je klíčová pro dosažení provozní efektivity v komplexních, více-dodavatelských prostředích. Poskytnutím jednotného pohledu na síťové prostředky umožňuje automatizaci, snižuje chyby ruční konfigurace a usnadňuje interoperabilitu mezi různými systémy správy. Model podporuje jak northbound rozhraní k systémům vyšší úrovně správy (jako [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/)), tak southbound rozhraní k síťovým elementům, čímž vytváří konzistentní strukturu správy v celé síťové architektuře.

## K čemu slouží

CBIM byl vytvořen, aby řešil rostoucí komplexitu správy telekomunikačních sítí s více dodavateli. Před jeho standardizací typicky každý dodatel zařízení implementoval proprietární rozhraní a datové modely pro správu, což od provozovatelů sítí vyžadovalo udržování samostatných systémů správy pro zařízení různých dodavatelů. Tato fragmentace zvyšovala provozní náklady, komplikovala automatizaci a ztěžovala implementaci správy služeb od konce ke konci v heterogenních síťových prostředích. Rozmnožení síťových funkcí a přechod na virtualizované, cloud-nativní architektury tyto výzvy dále prohlubovaly.

Historicky telekomunikační průmysl identifikoval potřebu standardizovaných rámců pro správu již v době architektury [TMN](/mobilnisite/slovnik/tmn/) (Telecommunications Management Network), ale tyto rané snahy často zůstaly na konceptuální úrovni bez podrobných implementačních specifikací. S vývojem 3GPP sítí od 2G přes 3G a dále se komplexita správy dramaticky zvýšila kvůli zavádění nových síťových elementů, rozhraní a služeb. CBIM se objevil jako konkrétní realizace standardizace správy v rámci ekosystému 3GPP, navazující na předchozí práce, ale poskytující mnohem podrobnější a implementovatelné specifikace.

Mezi primární problémy, které CBIM řeší, patří interoperabilita správy mezi zařízeními různých dodavatelů, snížení integračních nákladů pro nové síťové elementy, umožnění automatizovaných pracovních postupů pro provisioning a zajištění služeb (assurance) a vytvoření základu pro pokročilé možnosti správy jako samoorganizující se sítě ([SON](/mobilnisite/slovnik/son/)) a automatizace se zpětnovazební smyčkou (closed-loop automation). Poskytnutím společného základu umožňuje vývojářům systémů správy vytvářet nástroje, které fungují napříč více síťovými doménami, aniž by vyžadovaly vlastní integraci pro každou implementaci dodavatele. Tato standardizace je zvláště klíčová, jak se sítě vyvíjejí směrem k otevřeným architekturám, virtualizaci síťových funkcí a softwarově definovaným sítím, kde se schopnost konzistentně spravovat prostředky bez ohledu na jejich fyzickou nebo virtuální implementaci stává nezbytnou pro provozní efektivitu.

## Klíčové vlastnosti

- Standardizovaný objektově orientovaný informační model pro všechny síťové elementy 3GPP
- Komplexní dědičná hierarchie umožňující rozšiřitelnost a konzistenci
- Nezávislý návrh na protokolu podporující více rozhraní pro správu (SNMP, NETCONF/YANG atd.)
- Integrovaná podpora pro správu FCAPS (Fault, Configuration, Accounting, Performance, Security – poruchy, konfigurace, účtování, výkon, zabezpečení)
- Doménově specifická rozšíření pro RAN, Core, IMS a další síťové domény
- Bohatá metadata definicí včetně omezení, výchozích hodnot a specifikací chování

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)

## Definující specifikace

- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- **TS 32.182** (Rel-19) — UDC Common Baseline Information Model (CBIM)
- **TR 32.901** (Rel-19) — UDC Application Data Models Study

---

📖 **Anglický originál a plná specifikace:** [CBIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbim/)
