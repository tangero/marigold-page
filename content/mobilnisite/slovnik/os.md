---
slug: "os"
url: "/mobilnisite/slovnik/os/"
type: "slovnik"
title: "OS – Operations System"
date: 2026-01-01
abbr: "OS"
fullName: "Operations System"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/os/"
summary: "Nadřazený řídicí systém v telekomunikační síti zahrnující funkce správy prvků (Element Management, EM) a správy sítě (Network Management, NM). Je zodpovědný za správu poruch, konfiguraci, účtování, vý"
---

OS (Operations System) je nadřazený řídicí systém v telekomunikační síti zodpovědný za správu poruch, konfiguraci, účtování, výkon a zabezpečení síťových prvků a služeb.

## Popis

Operations System (OS) v terminologii 3GPP není jediným produktem, ale koncepčním rámcem a souborem standardů pro provozní podporu telekomunikačních sítí. Představuje soubor systémů a funkcí zodpovědných za správu síťových prvků (NEs) a jimi poskytovaných služeb. OS je hierarchicky strukturován a typicky zahrnuje systémy správy prvků (Element Management, [EM](/mobilnisite/slovnik/em/)) a systémy správy sítě (Network Management, [NM](/mobilnisite/slovnik/nm/)). Systém EM spravuje konkrétní typ nebo síťové prvky od jednoho dodavatele (např. všechny základnové stanice od dodavatele) a zajišťuje přímou komunikaci s zařízeními, zatímco systém NM poskytuje širší, integrovaný pohled napříč více systémy EM a různými síťovými doménami pro zajištění služeb a obchodně orientovanou správu.

Z architektonického hlediska OS komunikuje se síťovými prvky prostřednictvím standardizovaných nebo dodavatelsky specifických rozhraní. Mezi klíčové protokoly a rámce definované v mnoha specifikacích 3GPP (např. řada 32) patří SNMP, rozhraní založená na [CORBA](/mobilnisite/slovnik/corba/) a v modernějších implementacích později NETCONF/YANG a RESTful [API](/mobilnisite/slovnik/api/). OS plní funkční oblasti FCAPS: správu poruch (monitorování alarmů, izolace závad), správu konfigurace (zavádění softwaru, nastavování parametrů), správu účtování (sběr dat o využití pro účely fakturace), správu výkonu (sběr a analýza [KPI](/mobilnisite/slovnik/kpi/) a čítačů) a správu zabezpečení (řízení přístupu, auditní záznamy).

Kritickou součástí je báze řídicích informací (Management Information Base, [MIB](/mobilnisite/slovnik/mib/)), která definuje spravovatelné objekty a datové body na síťovém prvku ([NE](/mobilnisite/slovnik/ne/)), které může OS monitorovat a řídit. Role OS je klíčová pro správu životního cyklu sítě, od počátečního nasazení a uvedení do provozu přes každodenní operace, optimalizaci až po případné vyřazení. Umožňuje operátorům udržovat kvalitu služeb, plánovat kapacitu, řešit problémy a automatizovat rutinní úlohy. V moderních sítích se OS vyvíjí ve směru integrovanějších a automatizovanějších systémů, jako jsou centra provozu sítě (Network Operations Centers, NOCs), a s příchodem 5G přijímá koncepty jako uzavřená smyčka automatizace, záměrem řízená správa a integrace s orchestračními systémy pro síťové segmenty (network slicing).

## K čemu slouží

Koncept Operations System byl formalizován, aby řešil obrovskou složitost provozu rozsáhlých telekomunikačních sítí s více dodavateli. Rané sítě se často spoléhaly na proprietární nástroje pro správu specifické pro konkrétní prvky, což vedlo k provozním izolacím, vysokým nákladům na integraci a neefektivním procesům. Nedostatek standardizace ztěžoval operátorům získat jednotný přehled o stavu sítě a výkonu služeb.

Práce 3GPP na standardech OS, která je výrazně zastoupena v specifikacích řady 32, byla motivována potřebou interoperabilní, škálovatelné a efektivní správy sítě. Řeší problém fragmentované správy tím, že poskytuje společný rámec a informační modely. To umožňuje operátorům integrovat systémy správy od různých dodavatelů, automatizovat procesy napříč doménami a snižovat provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)). OS je páteří pro dosahování smluvních úrovní služeb (SLAs), zajišťování spolehlivosti sítě a umožnění rychlého zavádění nových služeb tím, že poskytuje nástroje pro jejich efektivní konfiguraci a monitorování. Jeho vývoj i nadále pohánějí trendy jako virtualizace (NFV), softwarově definované sítě (SDN) a cloud-nativní principy, které vyžadují agilnější, daty řízené a automatizované operace.

## Klíčové vlastnosti

- Zahrnuje vrstvy správy prvků (Element Management, EM) a správy sítě (Network Management, NM)
- Implementuje funkce správy FCAPS (Fault, Configuration, Accounting, Performance, Security)
- Spoléhá se na standardizovaná rozhraní (např. definovaná v 3GPP řadě 32) pro interoperabilitu mezi více dodavateli
- Spravuje síťové prvky (NEs) prostřednictvím definovaných bází řídicích informací (Management Information Bases, MIBs)
- Poskytuje zajištění služeb, monitorování výkonu a analýzu hlavní příčiny problémů
- Tvoří základ pro nástroje centra provozu sítě (Network Operations Center, NOC) a automatizaci

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TS 28.624** (Rel-19) — State Management Data Definition IRP Requirements
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.707** (Rel-19) — EPC NRM IRP Requirements
- **TS 28.734** (Rel-19) — STN Interface NRM IRP Requirements
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- … a dalších 42 specifikací

---

📖 **Anglický originál a plná specifikace:** [OS na 3GPP Explorer](https://3gpp-explorer.com/glossary/os/)
