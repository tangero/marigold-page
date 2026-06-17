---
slug: "adrf"
url: "/mobilnisite/slovnik/adrf/"
type: "slovnik"
title: "ADRF – Analytical Data Repository Function"
date: 2026-01-01
abbr: "ADRF"
fullName: "Analytical Data Repository Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/adrf/"
summary: "Analytical Data Repository Function (ADRF, funkce úložiště analytických dat) je funkce 5G sítě, která shromažďuje, ukládá a spravuje analytická data o síti. Poskytuje centralizované úložiště pro data"
---

ADRF je funkce 5G sítě, která shromažďuje, ukládá a spravuje analytická data v centralizovaném úložišti pro využití dalšími analytickými funkcemi, aby umožnila optimalizaci sítě řízenou daty.

## Popis

Analytical Data Repository Function (ADRF, funkce úložiště analytických dat) je standardizovaná síťová funkce zavedená ve specifikaci 3GPP Release 17 jako součást rámce pro správu a orchestraci architektury 5G. Slouží jako centralizovaná entita pro ukládání a správu dat, která je speciálně navržena pro podporu síťových analytických funkcí. ADRF funguje tak, že shromažďuje, agreguje a trvale ukládá různé typy síťových dat, včetně měření výkonu, konfiguračních dat, informací o účastnících a vzorců využívání služeb. Tato data jsou následně zpřístupněna autorizovaným analytickým spotřebitelům prostřednictvím standardizovaných rozhraní směrem nahoru (northbound), primárně podporujících Network Data Analytics Function (NWDAF) a Management Data Analytics Function (MDAF).

Architektonicky je ADRF implementována jako samostatná síťová funkce s dobře definovanými rozhraními založenými na službách (SBI), která dodržují principy architektury založené na službách podle 3GPP. Zpřístupňuje služby jako Nnrf_NFManagement, Nnrf_NFDiscovery a specifické služby správy dat definované ve specifikacích řady 29.5xx. Vnitřní architektura ADRF typicky zahrnuje moduly pro příjem dat, vrstvy pro správu úložiště, zpracovatelské jádro dat a komponenty pro vynucování politik. Podporuje různé technologie ukládání dat a dokáže zpracovávat strukturované i nestrukturované formáty dat, včetně mechanismů pro správu životního cyklu dat, jako jsou politiky uchovávání, archivace a mazání dat.

Během provozu ADRF přijímá data z více zdrojů, včetně síťových funkcí (NF), systémů pro podporu provozu (OSS) a externích poskytovatelů dat. Před uložením aplikuje procesy validace, normalizace a obohacení dat. Funkce implementuje sofistikované schémata organizace dat, včetně databází časových řad, úložišť typu klíč-hodnota a relačních databází, aby optimalizovala různé vzorce dotazů. Bezpečnost je prvořadá, přičemž ADRF implementuje politiky řízení přístupu, šifrování dat v klidu i při přenosu a auditní záznamy pro všechny operace přístupu k datům. Dále podporuje anonymizaci a pseudonymizaci dat za účelem ochrany soukromí účastníků při zachování analytické využitelnosti.

ADRF hraje klíčovou roli při umožnění provozu sítě řízeného daty tím, že poskytuje jediný zdroj pravdy pro analytická data. Odstraňuje datové izolované celky (silosy), které dříve existovaly napříč různými síťovými doménami a systémy správy. Standardizací formátů dat a metod přístupu ADRF snižuje složitost integrace pro analytické aplikace a umožňuje sofistikovanější analýzy napříč doménami. Její škálovatelná architektura podporuje obrovské objemy dat generované sítěmi 5G při zachování výkonu pro případy užití analýz v reálném čase a téměř reálném čase.

## K čemu slouží

ADRF byla vytvořena, aby řešila rostoucí potřebu centralizované a standardizované správy dat v sítích 5G, zejména pro podporu pokročilých analýz a aplikací umělé inteligence/strojového učení (AI/ML). Před jejím zavedením musely síťové analytické funkce shromažďovat data z různorodých zdrojů pomocí proprietárních rozhraní a formátů, což vedlo k problémům s integrací, nekonzistencím dat a omezené škálovatelnosti. Tento roztříštěný přístup bránil rozvoji komplexních síťových analýz a automatizovaných optimalizačních schopností, které jsou klíčové pro slibovanou automatizaci a inteligenci sítě 5G.

Historicky operátoři sítí spravovali analytická data prostřednictvím více izolovaných systémů, včetně systémů pro správu výkonu, systémů pro správu poruch a různých provozních databází. Každá analytická aplikace vyžadovala vlastní integraci s těmito datovými zdroji, což vedlo k vysokým nákladům na vývoj, režii údržby a zpoždění uvedení nových analytických služeb na trh. Nedostatek standardizovaných datových modelů a rozhraní také ztěžoval korelaci dat napříč různými síťovými doménami nebo implementaci konzistentních politik správy a zabezpečení dat.

ADRF tyto problémy řeší tím, že poskytuje jednotný, standardy založený přístup ke správě analytických dat. Umožňuje operátorům sítí implementovat konzistentní politiky sběru, ukládání a přístupu k datům napříč celou jejich síťovou infrastrukturou. Oddělením úložiště dat od analytického zpracování umožňuje ADRF analytickým funkcím soustředit se na jejich hlavní analytické úkoly namísto složitostí správy dat. Toto architektonické oddělení také umožňuje efektivnější využití zdrojů, protože více analytických funkcí může sdílet stejné datové úložiště, místo aby každá udržovala duplicitní kopie dat. Standardizovaná rozhraní ADRF usnadňují vývoj ekosystému, což umožňuje snadnější integraci analytických aplikací třetích stran s operátorskými sítěmi.

## Klíčové vlastnosti

- Centralizované úložiště pro analytická data o síti z více zdrojů
- Standardizovaná rozhraní založená na službách (rozhraní Nadrf) pro přístup k datům
- Podpora analýz dat v reálném čase i historických dat
- Správa životního cyklu dat včetně politik uchovávání a archivace
- Bezpečnostní funkce včetně řízení přístupu, šifrování a auditního zaznamenávání
- Škálovatelná architektura podporující obrovské objemy dat v sítích 5G

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.574** (Rel-19) — 5G Data Collection Coordination Services Stage 3
- **TS 29.575** (Rel-19) — 5G Analytics Data Repository Services Stage 3
- **TS 29.576** (Rel-19) — 5G Messaging Framework Adaptor Services Stage 3

---

📖 **Anglický originál a plná specifikace:** [ADRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/adrf/)
