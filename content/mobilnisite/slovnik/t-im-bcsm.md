---
slug: "t-im-bcsm"
url: "/mobilnisite/slovnik/t-im-bcsm/"
type: "slovnik"
title: "T-IM-BCSM – Terminating IP Multimedia Basic Call State Model"
date: 2025-01-01
abbr: "T-IM-BCSM"
fullName: "Terminating IP Multimedia Basic Call State Model"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-im-bcsm/"
summary: "Terminating IP Multimedia Basic Call State Model (T-IM-BCSM) je konečný automat používaný pro řízení relací v IP Multimedia Subsystem (IMS). Modeluje události a body kontroly pro ukončovanou (příchozí"
---

T-IM-BCSM je konečný automat v IMS, který modeluje události a kontrolní body pro příchozí SIP relaci z pohledu obslužného CSCF a definuje místa, kde lze vyvolat servisní logiku.

## Popis

Terminating IP Multimedia Basic Call State Model (T-IM-BCSM) je základním konceptem v servisní architektuře 3GPP IP Multimedia Subsystem (IMS), konkrétně v rámci frameworku Camel Application Part ([CAP](/mobilnisite/slovnik/cap/)) a IP Multimedia Service Switching Function ([IM-SSF](/mobilnisite/slovnik/im-ssf/)). Jedná se o formální konečný automat definovaný v 3GPP TS 23.218 a TS 23.278, který modeluje životní cyklus ukončované [SIP](/mobilnisite/slovnik/sip/) relace – tedy relace, kde volanou stranou je účastník obsluhovaný síťovým uzlem obsahujícím tento model. T-IM-BCSM poskytuje standardizovanou abstrakci procesu řízení hovoru/relace a identifikuje konkrétní body ve volání (Points In Call, [PIC](/mobilnisite/slovnik/pic/)) a detekční body (Detection Points, [DP](/mobilnisite/slovnik/dp/)).

Z architektonického hlediska je T-IM-BCSM instancován uvnitř Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)), resp. jeho interakce se servisní logikou je řízena přes IM-SSF při použití [CAMEL](/mobilnisite/slovnik/camel/) pro servisní kontrolu. Model začíná příchodem počáteční SIP požadavku (jako je INVITE) určeného pro účastníka. Poté postupuje přes stavy jako 'Authorize_Termination_Attempt', 'Collect_Info', 'Analyze_Info', 'Select_Route', 'Authorize_Call_Setup' a nakonec 'Active' a 'Disconnect'. Každý stav reprezentuje specifickou fázi navázání relace. Mezi těmito stavy jsou detekční body (DP) – okamžiky, kdy může být zpracování volání přerušeno pro interakci s externí servisní logikou, jako je CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) nebo Application Server (AS).

Jeho funkce je nedílnou součástí servisního spouštění. Například v detekčním bodě 'Termination_Attempt_Authorized' může IM-SSF odeslat zprávu CAP do CAMEL služby, aby ověřila, zda volaný účastník smí přijmout hovor, nebo zda mají být aplikovány nějaké služby pro příchozí volání (jako přesměrování, hlasová schránka nebo filtrování příchozích hovorů). Servisní logika pak může instruovat IM-SSF/CSCF, aby pokračoval ve zpracování, ukončil hovor nebo upravil jeho parametry. Tento model odděluje základní logiku řízení hovoru v CSCF od komplexní servisní logiky, což umožňuje vytváření sofistikovaných, na síti založených IP multimediálních služeb standardizovaným a interoperabilním způsobem. Je to protějšek pro ukončované volání k O-IM-BCSM (Originating IM-BCSM).

## K čemu slouží

T-IM-BCSM byl vytvořen za účelem rozšíření osvědčených principů Inteligentní sítě (IN) a možností CAMEL, široce používaných pro služby v okruhově komutovaných telefonnních sítích, do plně IP světa IMS. Před IMS používal CAMEL modely základního stavu volání (BCSM) v mobilní ústředně pro spouštění služeb, jako je předplacená služba nebo překlad čísel. S přechodem na SIP-based IMS byl potřeba nový model, který by reprezentoval řízení SIP relací způsobem, kterému by stávající CAMEL servisní logika rozuměla a mohla s ním interagovat.

Jeho primárním účelem je poskytnout standardizovaný 'háček' nebo rozhraní pro externí servisní platformy, aby mohly řídit a ovlivňovat zpracování příchozích SIP relací. Tím se řeší problém, jak implementovat síťově řízené služby (jako bezpodmínečné přesměrování, při obsazení nebo při nezvednutí) v distribuované, na SIP založené architektuře, kde stav volání není centralizován v jedné ústředně. T-IM-BCSM definuje společný jazyk a sadu událostí, na kterých se shodne jak kontrolér relací (CSCF/IM-SSF), tak servisní logika (Application Server).

Tato abstrakce byla klíčová pro hladkou migraci služeb z okruhově komutovaných sítí do IMS a pro vývoj nových multimediálních služeb. Umožnila operátorům znovu využít své investice do prostředí pro tvorbu CAMEL služeb a SCP (Service Control Points) při přechodu na síť nové generace. Zajistila také konzistentní a přenositelné chování služeb napříč IMS jádrovými zařízeními různých výrobců, protože všechna implementují stejný stavový model a detekční body pro řízení ukončovaného volání.

## Klíčové vlastnosti

- Konečný automat modelující životní cyklus ukončované IMS (SIP) relace
- Definuje konkrétní body ve volání (Points In Call, PIC) reprezentující fáze navazování relace
- Obsahuje detekční body (Detection Points, DP) pro vyvolání externí servisní logiky (např. CAMEL)
- Umožňuje síťově řízené služby pro příchozí volání, jako je přesměrování nebo zákaz
- Integruje řízení IMS hovorů s protokolem CAMEL prostřednictvím IM-SSF
- Standardizován v 3GPP pro zajištění multivendorové interoperability při servisním spouštění

## Související pojmy

- [O-IM-BCSM – Originating IP Multimedia Basic Call State Model](/mobilnisite/slovnik/o-im-bcsm/)
- [IM-SSF – IP Multimedia Service Switching Function](/mobilnisite/slovnik/im-ssf/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [T-IM-BCSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-im-bcsm/)
