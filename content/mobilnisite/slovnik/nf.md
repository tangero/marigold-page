---
slug: "nf"
url: "/mobilnisite/slovnik/nf/"
type: "slovnik"
title: "NF – Network Function"
date: 2026-01-01
abbr: "NF"
fullName: "Network Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nf/"
summary: "Funkční stavební blok v síti 3GPP s jasně definovanými externími rozhraními a funkčním chováním. Může být implementován jako dedikované hardwarové zařízení, softwarová instance na dedikovaném hardwaru"
---

NF je funkční stavební blok v síti 3GPP, který má jasně definovaná externí rozhraní a chování a může být implementován na dedikovaném hardwaru nebo jako virtualizovaná funkce v cloudu.

## Popis

Síťová funkce (NF) je základní architektonický koncept v systémech 3GPP, který je zvláště klíčový od vydání Release 5 se zavedením IP Multimedia Subsystem (IMS) a plně realizován v 5G Core (5GC) s jeho servisně orientovanou architekturou (SBA). NF je samostatná modulární softwarová funkce, která poskytuje konkrétní telekomunikační schopnost, jako je správa relací, správa mobility, řízení politik nebo ukládání uživatelských dat. Každá NF má jasně definované funkční chování a své schopnosti zpřístupňuje prostřednictvím dobře definovaných rozhraní, primárně servisně orientovaných rozhraní (SBI) využívajících [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/) v 5GC, nebo referenčních bodových rozhraní ve starších architekturách.

Z architektonického hlediska jsou NF uzly, které nahrazují tradiční monolitické síťové elementy. V 5G Core se architektura skládá výhradně z propojených NF. Mezi klíčové NF patří Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), která zpracovává připojení a správu mobility; Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), odpovědná za vytváření relací a přidělování IP adres; User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která provádí směrování a přeposílání paketů; a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), které ukládá data účastníků. Tyto NF vzájemně komunikují v rámci servisně orientovaného rámce, kde mohou vystupovat jako poskytovatelé služeb (zpřístupňující [API](/mobilnisite/slovnik/api/)) a konzumenti služeb (vyvolávající API).

Jak NF funguje, závisí na jejím typu a generaci sítě. V 5G SBA se musí NF zaregistrovat se svými službami u Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)), která funguje jako zprostředkovatel pro vyhledávání služeb. Když NF (konzument) potřebuje využít službu jiné NF (poskytovatele), dotazuje se NRF, aby získala instanci(e) poskytující NF, které mohou požadavek splnit, včetně informací o jejich dostupnosti (IP adresa, port). Komunikace pak probíhá přímo mezi NF pomocí RESTful principů přes HTTP/2. Každá NF je navržena jako bezstavová tam, kde je to možné, se stavovými informacemi externalizovanými do datové vrstvy, což umožňuje škálovatelnost, odolnost a cloud-nativní nasazení.

Její role v síti spočívá v poskytování flexibilního, škálovatelného a dekomponovatelného způsobu poskytování síťových služeb. Rozdělením monolitických síťových elementů na jemněji granulované NF mohou operátoři nasazovat, škálovat a aktualizovat jednotlivé funkce nezávisle na základě poptávky. To podporuje síťové slicing, protože různé slice mohou vytvářet specifické instance NF s přizpůsobenou konfigurací. NF mohou být virtualizované (VNF) nebo kontejnerizované (CNF) a nasazeny na komerčním standardním hardwaru (COTS) v datových centrech, což je základním kamenem virtualizace síťových funkcí (NFV). Koncept NF odděluje softwarovou funkcionalitu od hardwaru, což umožňuje automatizaci, rychlou inovaci a snížení kapitálových i provozních nákladů.

## K čemu slouží

Koncept síťové funkce byl vytvořen, aby řešil omezení tradičních, vertikálně integrovaných síťových zařízení (jako MSC, SGSN, GGSN v 2G/3G). Tyto legacy uzly byly proprietární, vázané na hardware a monolitické, což je činilo drahými pořizovat, obtížně škálovatelnými a pomalými na upgrade s novými funkcemi. Každá nová služba často vyžadovala nový fyzický uzel, což vedlo k rozrůstání sítě a složitým, rigidním propojením. Model NF zavádí softwarově orientovaný, modulární přístup k návrhu sítě.

Primární problém, který řeší, je nepružnost. Definováním síťových schopností jako diskrétních, znovupoužitelných softwarových funkcí umožňuje model NF softwarizaci a cloudifikaci sítě. To operátorům umožňuje nasazovat síťové služby na generické cloudové infrastruktuře, pružně škálovat s poptávkou po přenosu a rychle zavádět nové služby skládáním stávajících NF nebo nasazováním nových bez nutnosti nahrazovat celé hardwarové platformy. Je to základní prvek pro virtualizaci síťových funkcí (NFV) a přechod k cloud-nativním 5G core sítím.

Historicky se tento koncept významně vyvíjel. Ve vydání Release 5 s IMS byly funkce jako CSCF ranými příklady logicky oddělených NF, ačkoli zpočátku stále vázanými na konkrétní implementace. Tlak na snížení nákladů, agilitu služeb a podporu různých případů užití (IoT, nízká latence, vysoká přenosová kapacita) během přechodu ze 4G na 5G učinil model NF nezbytným. Servisně orientovaná architektura (SBA) 5G je plnou realizací tohoto konceptu, kde je core síť doslova definována jako soubor vzájemně komunikujících NF. Toto řeší potřebu automatizace (prostřednictvím standardních API), podporu síťového slicingu (kde slice je soubor instancí NF) a možnost flexibilně distribuovat funkce (např. umístění UPF na okraji sítě pro služby s nízkou latencí). NF je atomovou jednotkou moderního návrhu sítí 3GPP, zásadní pro dosažení cílů 5G a budoucích generací.

## Klíčové vlastnosti

- Modulární softwarová funkce s jasně definovaným chováním a rozhraními
- Může být virtualizována (VNF) nebo kontejnerizována (CNF) na cloudové infrastruktuře
- Komunikuje prostřednictvím servisně orientovaných rozhraní (SBI) využívajících RESTful API (v 5G)
- Registruje a vyhledává služby prostřednictvím Network Repository Function (NRF)
- Navržena pro bezstavový provoz tam, kde je to možné, za účelem vysoké škálovatelnosti
- Umožňuje nezávislý lifecycle management, škálování a upgrade

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 25.866** (Rel-9) — 1.28Mcps TDD Home NodeB Study Report
- **TS 26.531** (Rel-19) — Data Collection & Reporting Architecture for 5G
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.520** (Rel-19) — PM for Virtualized Mobile Networks
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.533** (Rel-19) — Management and orchestration; Architecture framework
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TR 28.816** (Rel-17) — Charging for 5G Cellular IoT
- … a dalších 64 specifikací

---

📖 **Anglický originál a plná specifikace:** [NF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nf/)
