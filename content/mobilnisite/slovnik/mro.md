---
slug: "mro"
url: "/mobilnisite/slovnik/mro/"
type: "slovnik"
title: "MRO – Mobility Robustness Optimisation"
date: 2025-01-01
abbr: "MRO"
fullName: "Mobility Robustness Optimisation"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mro/"
summary: "Funkce samo-organizující sítě (SON), která automaticky detekuje a koriguje problémy související s nastavením parametrů předávání spojení (HO). Jejím cílem je minimalizovat selhání spojení (jako Radio"
---

MRO je funkce samo-organizující sítě (SON), která automaticky detekuje a koriguje problémy s parametry předávání spojení, aby minimalizovala selhání spojení a zbytečná předávání spojení analýzou hlášení od UE a událostí selhání.

## Popis

Mobility Robustness Optimisation (MRO, optimalizace robustnosti mobility) je klíčová funkce samo-organizující sítě ([SON](/mobilnisite/slovnik/son/)) definovaná v 3GPP pro LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a následující rádiové přístupové technologie. Jejím primárním cílem je automatizovat ladění řídicích parametrů předávání spojení pro optimalizaci výkonu mobility. MRO funguje tak, že shromažďuje a analyzuje specifická měření výkonu a hlášení selhání ze sítě. Mezi klíčové zdroje dat patří: hlášení Radio Link Failure ([RLF](/mobilnisite/slovnik/rlf/)) odesílaná UE po opětovném připojení, hlášení Handover Failure ([HOF](/mobilnisite/slovnik/hof/)) a běžná hlášení měření od UE (např. Reference Signal Received Power - [RSRP](/mobilnisite/slovnik/rsrp/), Reference Signal Received Quality - [RSRQ](/mobilnisite/slovnik/rsrq/)). Funkce běží v rámci systému Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) nebo distribuovaně v základnových stanicích (eNBs/gNBs), v závislosti na architektuře SON (centralizovaná, distribuovaná nebo hybridní).

Algoritmus MRO identifikuje specifické vzorce selhání mobility. Tři hlavní problémy, které detekuje, jsou: 1) **Příliš pozdní předání spojení (Too Late Handover)**: Předání spojení je spuštěno až poté, co se rádiové spojení se zdrojovou buňkou již výrazně zhoršilo, což často vede k RLF před nebo během procedury předání spojení. 2) **Příliš brzké předání spojení (Too Early Handover)**: Předání spojení je úspěšně provedeno do cílové buňky, ale UE v cílové buňce rychle utrpí RLF a znovu se připojí zpět ke zdrojové buňce nebo k jiné buňce. 3) **Předání spojení do nesprávné buňky (Handover to Wrong Cell)**: Předání spojení je úspěšné, ale krátce poté v cílové buňce dojde k RLF a UE se připojí k třetí buňce, která nebyla ani zdrojovou, ani cílovou. Pro každý detekovaný vzorec MRO koreluje selhání s konkrétními zúčastněnými buňkami a nastavením parametrů předávání spojení (především hystereze předání spojení, čas do spuštění a individuální posuny buňky), které byly v daném čase aktivní.

Na základě této analýzy MRO generuje optimalizační akce. Jedná se typicky o doporučení nebo automatické úpravy řídicích parametrů předávání spojení pro příslušné páry buněk (vztahy sousedství). Pro "Příliš pozdní předání spojení" z buňky A do buňky B může MRO navrhnout snížení prahové hodnoty nebo hystereze předání spojení pro tento směr. Pro "Příliš brzké předání spojení" může navrhnout zvýšení prahové hodnoty nebo času do spuštění. Úpravy jsou aplikovány opatrně, často v malých krocích, a jejich dopad je sledován, aby byla zajištěna stabilita a zabránilo se oscilacím parametrů. MRO pracuje kontinuálně, přizpůsobuje se změnám v rádiovém prostředí, distribuci uživatelů a topologii sítě, čímž udržuje optimální výkon mobility s minimálním manuálním zásahem.

## K čemu slouží

MRO byla vytvořena, aby řešila hlavní provozní výzvu v mobilních sítích: manuální, časově náročný a náchylný k chybám proces optimalizace parametrů předávání spojení. Před [SON](/mobilnisite/slovnik/son/) museli síťoví inženýři ručně analyzovat data z testů jízdy a klíčové ukazatele výkonu (KPI), jako je úspěšnost předání spojení, a pak metodou pokus-omyl upravovat parametry pro tisíce vztahů sousedství buněk. Tento proces byl statický, nemohl rychle reagovat na denní nebo sezónní změny v provozu a šíření signálu a často vedl k neoptimálnímu nastavení, které způsobovalo přerušení hovorů, špatný uživatelský zážitek a neefektivní využití zdrojů.

Snaha o SON a konkrétně MRO byla motivována rostoucí složitostí sítí (více buněk, heterogenní nasazení) a potřebou snížit provozní výdaje (OPEX). MRO tento optimalizační cyklus automatizuje. Řeší problémy pozdních/brzkých předání spojení, které jsou hlavními příčinami přerušení hovorů a špatné kontinuity služeb. Minimalizací Radio Link Failure a zbytečných předání spojení (ping-pong) MRO přímo zlepšuje kvalitu vnímanou koncovým uživatelem, zvyšuje spolehlivost sítě a snižuje signalizační zátěž sítě. Její zavedení v LTE Release 10 bylo zásadním krokem k plně autonomním sítím, což umožnilo efektivní provoz hustých a složitých budoucích nasazení RAN, jako jsou ta s malými buňkami.

## Klíčové vlastnosti

- Automaticky detekuje vzorce selhání mobility: Příliš pozdní, příliš brzké a předání spojení do nesprávné buňky
- Analyzuje data hlášená UE včetně hlášení Radio Link Failure (RLF) a Handover Failure (HOF)
- Optimalizuje klíčové řídicí parametry předávání spojení: hysterezi, čas do spuštění a individuální posuny buňky
- Funguje jako klíčová funkce samo-organizující sítě (SON) v rámci systému OAM nebo eNB/gNB
- Podporuje optimalizaci mobility intra-RAT (např. LTE-LTE) a v pozdějších releasech i inter-RAT (např. LTE-UMTS)
- Umožňuje kontinuální, adaptivní optimalizaci, která snižuje potřebu manuálních zásahů a zlepšuje robustnost sítě

## Související pojmy

- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [ANR – Automatic Neighbour Relationship](/mobilnisite/slovnik/anr/)
- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)

## Definující specifikace

- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.887** (Rel-12) — Energy Saving Enhancement for E-UTRAN Study
- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study
- **TS 37.822** (Rel-12) — SON Enhancements for UE Types and Active Antennas

---

📖 **Anglický originál a plná specifikace:** [MRO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mro/)
