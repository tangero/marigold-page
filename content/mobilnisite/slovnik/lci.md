---
slug: "lci"
url: "/mobilnisite/slovnik/lci/"
type: "slovnik"
title: "LCI – Layer Convergence Information"
date: 2025-01-01
abbr: "LCI"
fullName: "Layer Convergence Information"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lci/"
summary: "LCI je protokolový mechanismus používaný k předávání informací o konvergenci protokolových vrstev, zejména pro efektivní přenos dat a správu relací. Umožňuje síti a uživatelskému zařízení sladit konfi"
---

LCI je protokolový mechanismus, který přenáší informace o konvergenci protokolových vrstev, aby umožnil síti a uživatelskému zařízení sladit konfigurace a schopnosti pro efektivní přenos dat a správu relací.

## Popis

Layer Convergence Information (LCI, informace o konvergenci vrstev) je informační prvek na úrovni protokolu definovaný ve specifikacích 3GPP, který usnadňuje konvergenci a koordinaci různých protokolových vrstev, primárně v kontextu protokolu konvergence paketových dat (PDCP) a protokolu adaptace servisních dat (SDAP). Funguje tak, že nese metadata popisující, jak jsou protokoly nebo služby vyšších vrstev mapovány na transportní mechanismy nižších vrstev, včetně podrobností o kompresi hlaviček, bezpečnostních kontextech a mapování toků kvality služeb (QoS). Tyto informace jsou vyměňovány mezi uživatelským zařízením (UE) a síťovými uzly, jako je gNB v 5G nebo [eNB](/mobilnisite/slovnik/enb/) v LTE, během zřizování relace, procedur předávání spojení nebo při událostech rekonfigurace.

Architektura LCI zahrnuje jeho zařazení do signalizačních zpráv řídicí roviny, jako jsou ty definované v protokolu [NGAP](/mobilnisite/slovnik/ngap/) (Next Generation Application Protocol) a [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). V praxi jsou parametry LCI zakódovány v informačních prvcích, které specifikují konfigurace konvergenční vrstvy, což umožňuje dynamickou adaptaci na síťové podmínky a požadavky služeb. Například během předání spojení z LTE do 5G NR může LCI sdělit, jak mají být PDCP kontexty zachovány nebo obnoveny, čímž zajišťuje plynulé přesměrování dat a minimální přerušení. Mezi klíčové komponenty patří samotná hodnota LCI, která může indikovat specifické konvergenční protokoly nebo režimy, a přidružené časovače nebo příznaky, které řídí její platnost a použití.

Role LCI v síti je klíčová pro podporu heterogenních síťových prostředí a scénářů s více spojeními. Poskytnutím standardizovaného způsobu signalizace vlastností konvergence vrstev umožňuje efektivní využití zdrojů, snížení režie a zvýšení výkonu pro služby jako VoIP nebo streamované video. V systémech 5G je LCI integrováno s mechanismy síťového řezání a QoS, což umožňuje přizpůsobené zásobníky protokolů pro různé typy řezů. Jeho specifikace pokrývají více vydání, což odráží jeho vývoj směrem k řešení nových rádiových technologií a požadavků služeb, s podrobnými postupy popsanými v technických specifikacích, jako je 25.346 pro LTE a 29.500 pro protokoly 5G jádra sítě.

## K čemu slouží

LCI bylo zavedeno, aby vyřešilo problém nevyrovnanosti a neefektivity protokolových vrstev v konvergovaných síťových prostředích, kde koexistuje více přístupových technologií (např. LTE, 5G NR, Wi-Fi) a různorodých služeb. Před jeho standardizací často správa konvergence protokolů – jako je komprese hlaviček nebo přenos bezpečnostního kontextu – během událostí mobility nebo modifikací relací vedla ke zvýšené latenci, ztrátě paketů nebo suboptimálnímu využití zdrojů. Vytvoření LCI bylo motivováno potřebou jednotného signalizačního mechanismu, který by mohl dynamicky koordinovat konfigurace vrstev mezi UE a sítí, čímž by zajišťoval konzistentní poskytování služeb a zpětnou kompatibilitu.

Historicky, jak se sítě 3GPP vyvíjely od vydání Rel-6 dále, rozšíření datových služeb a zavedení plně IP architektur zdůraznilo omezení stávajících zásobníků protokolů, které nebyly navrženy pro bezproblémovou vzájemnou spolupráci mezi různými rádiovými přístupovými sítěmi (RAN). LCI tato omezení řeší tím, že poskytuje flexibilní informační prvek, který zapouzdřuje konvergenční parametry, což umožňuje sítím přizpůsobovat chování protokolů bez nutnosti rozsáhlého nového vyjednávání nebo narušení služby. To je zvláště důležité pro scénáře, jako je předávání spojení mezi 4G a 5G, kde je udržení kontinuity relace a QoS prvořadé.

Pokračující relevance LCI spočívá v jeho podpoře pokročilých funkcí, jako je duální konektivita, síťové řezání a ultra-spolehlivá komunikace s nízkou latencí (URLLC). Standardizací způsobu, jakým jsou informace o konvergenci sdělovány, snižuje implementační složitost a podporuje interoperabilitu napříč zařízeními různých dodavatelů, což nakonec přispívá k efektivnějšímu a škálovatelnějšímu ekosystému mobilních sítí.

## Klíčové vlastnosti

- Zapouzdřuje parametry konvergence protokolových vrstev pro dynamickou konfiguraci
- Podporuje plynulá předání spojení a kontinuitu relací napříč heterogenními sítěmi
- Integruje se s vrstvami PDCP a SDAP pro optimalizovaný přenos dat
- Umožňuje efektivní správu komprese hlaviček a bezpečnostních kontextů
- Usnadňuje mapování toků QoS a sladění síťového řezání
- Snižuje signalizační režii konsolidací informací o konvergenci v řídicích zprávách

## Související pojmy

- [NGAP – Next Generation Application Protocol](/mobilnisite/slovnik/ngap/)

## Definující specifikace

- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [LCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/lci/)
