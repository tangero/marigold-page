---
slug: "cad"
url: "/mobilnisite/slovnik/cad/"
type: "slovnik"
title: "CAD – Complex Activity Detection"
date: 2025-01-01
abbr: "CAD"
fullName: "Complex Activity Detection"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cad/"
summary: "Complex Activity Detection (CAD) je služební schopnost (service capability) 3GPP, která umožňuje síti detekovat a rozpoznávat komplexní aktivity a chování uživatele prostřednictvím analýzy síťové sign"
---

CAD je služební schopnost (service capability) 3GPP, která detekuje komplexní aktivity uživatele analýzou síťové signalizace a dat zařízení za účelem identifikace vzorců v interakcích, využívání a mobilitě pro kontextově-aware služby a optimalizace.

## Popis

Complex Activity Detection (CAD) je sofistikovaná služební schopnost v sítích 3GPP, která využívá pokročilé algoritmy a techniky strojového učení k identifikaci a klasifikaci komplexních vzorců uživatelského chování a aktivit. Systém funguje tak, že sbírá a analyzuje více datových proudů z uživatelského zařízení (UE), síťových prvků a aplikačních serverů, včetně vzorců signalizace, aktualizací polohy, statistik využívání služeb, dat ze senzorů zařízení (pokud jsou dostupná) a časových vzorců síťových interakcí. Tato multidimenzionální analýza umožňuje síti vytvářet komplexní behaviorální profily a detekovat aktivity přesahující pouhé jednoduché využívání služeb, jako jsou dojížděcí vzorce, pracovní rutiny, preference v zábavě a vzorce sociálních interakcí.

Architektonická implementace CAD zahrnuje několik klíčových komponent distribuovaných po síti. V jejím jádru je CAD funkce (CAD Function), typicky implementovaná jako součást Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) nebo jako samostatný aplikační server. Tato funkce komunikuje s různými síťovými prvky včetně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) za účelem sběru relevantních dat. Systém využívá techniky fúze dat ke korelaci informací z různých zdrojů a aplikuje algoritmy pro rozpoznávání vzorců k identifikaci komplexních aktivit. Mechanismy ochrany soukromí a zabezpečení jsou nedílnou součástí architektury a zajišťují, že uživatelská data jsou anonymizována a zpracovávána v souladu s regulatorními požadavky.

Proces detekce sleduje vícefázový pracovní postup začínající sběrem dat ze síťových rozhraní a uživatelského zařízení (UE). Nezpracovaná data procházejí předzpracováním za účelem odstranění šumu a normalizace formátů, než jsou předána do detekčních algoritmů. Tyto algoritmy využívají techniky jako Hidden Markovovy modely, neuronové sítě a shlukovací algoritmy k identifikaci vzorců indikujících specifické aktivity. Systém udržuje modely aktivit, které definují, co tvoří různé typy komplexních aktivit, a tyto modely mohou být dynamicky aktualizovány na základě nových pozorování a zpětné vazby. Detekované aktivity jsou následně zpřístupněny autorizovaným aplikacím prostřednictvím standardizovaných [API](/mobilnisite/slovnik/api/), což umožňuje kontextově-aware služby a síťové optimalizace.

CAD hraje klíčovou roli při umožňování inteligentních síťových služeb tím, že poskytuje hluboké vhledy do uživatelského chování. Tato schopnost podporuje četné aplikace včetně personalizovaných úprav kvality služby (QoS), prediktivní alokace síťových zdrojů, kontextově-aware doporučení služeb a vylepšeného řízení uživatelského zážitku. Schopnost systému detekovat komplexní aktivity namísto jednoduchých událostí umožňuje sofistikovanější personalizaci služeb a strategie síťové optimalizace. CAD navíc podporuje funkce síťové analytiky tím, že poskytuje detailní behaviorální data, která lze využít pro plánování kapacity, vývoj služeb a optimalizaci výkonu sítě.

## K čemu slouží

Complex Activity Detection byl zaveden, aby řešil rostoucí potřebu kontextově-aware služeb v mobilních sítích, kde jednoduché sledování využívání služeb bylo nedostatečné pro poskytování personalizovaného uživatelského zážitku. Před CAD sítě primárně sledovaly základní metriky, jako je objem dat a poloha, a postrádaly schopnost porozumět komplexnímu uživatelskému chování a aktivitám. Toto omezení bránilo poskytovatelům služeb v nabízení skutečně personalizovaných služeb a v optimalizaci síťových zdrojů na základě skutečných vzorců uživatelského chování. Vytvoření CAD bylo motivováno rostoucí poptávkou po inteligentních službách, které by se dokázaly přizpůsobit uživatelskému kontextu a preferencím.

Technologie řeší několik klíčových problémů moderních mobilních sítí. Za prvé umožňuje efektivnější využití síťových zdrojů tím, že umožňuje prediktivní alokaci na základě očekávaných uživatelských aktivit. Za druhé podporuje vývoj služeb s přidanou hodnotou, které se dokážou přizpůsobit uživatelskému kontextu, jako je automatické úpravy nastavení oznámení během schůzek nebo optimalizace kvality streamování na základě vzorců sledování. Za třetí poskytuje síťovým operátorům hlubší vhledy do uživatelského chování, což umožňuje lepší návrh služeb a správu vztahů se zákazníky. Historický kontext vývoje CAD zahrnuje vývoj od základních služeb založených na poloze ke komplexním kontextově-aware systémům, které rozumějí nejen tomu, kde se uživatelé nacházejí, ale také tomu, co dělají a jak interagují se svými zařízeními a službami.

CAD řeší omezení předchozích přístupů tím, že přesahuje pouhou detekci jednoduchých událostí směrem ke komplexnímu rozpoznávání aktivit. Starší systémy dokázaly detekovat jednotlivé události, jako je uskutečnění hovoru nebo přístup na webovou stránku, ale nedokázaly porozumět širšímu kontextu nebo vzorcům chování. Multidimenzionální analýza a schopnosti rozpoznávání vzorců CAD jí umožňují identifikovat komplexní aktivity zahrnující více událostí a časových období. Tento pokrok umožňuje sofistikovanější personalizaci služeb a síťovou optimalizaci a podporuje vývoj směrem k inteligentním, samoopravujícím se sítím, které dokážou anticipovat potřeby uživatelů a přizpůsobit se jim.

## Klíčové vlastnosti

- Sběr dat z více zdrojů – ze síťových prvků a uživatelského zařízení (UE)
- Pokročilé rozpoznávání vzorců využívající algoritmy strojového učení
- Zpracování dat s ochranou soukromí a možnostmi anonymizace
- Detekce a klasifikace aktivit v reálném čase i historických
- Standardizované API pro zpřístupnění služeb autorizovaným aplikacím
- Dynamická aktualizace modelů aktivit na základě nových pozorování

## Související pojmy

- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [CAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/cad/)
