---
slug: "urr"
url: "/mobilnisite/slovnik/urr/"
type: "slovnik"
title: "URR – Usage Reporting Rule"
date: 2025-01-01
abbr: "URR"
fullName: "Usage Reporting Rule"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/urr/"
summary: "Mechanismus řízení politik v 5G pro dynamické, událostmi spouštěné hlášení využití ze SMF do PCF. Umožňuje detailní monitorování datových toků služeb a podporuje pokročilé účtování, vynucování QoS a s"
---

URR je mechanismus řízení politik v sítích 5G, který umožňuje dynamické, událostmi spouštěné hlášení metrik datových toků služeb ze SMF do PCF pro účely účtování, QoS a analýz.

## Popis

Pravidlo pro hlášení využití (Usage Reporting Rule, URR) je základní součástí architektury řízení politik v 5G, definované v rámci [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) a vynucované [SMF](/mobilnisite/slovnik/smf/) (Session Management Function). Jedná se o pravidlo politiky, které určuje, kdy a jak mají být hlášeny informace o využití pro konkrétní datový tok služby (Service Data Flow, [SDF](/mobilnisite/slovnik/sdf/)) nebo agregát SDF. URR je zřízeno PCF jako součást pravidla [PCC](/mobilnisite/slovnik/pcc/) (Policy and Charging Control) a je v rámci [PDU](/mobilnisite/slovnik/pdu/) (Packet Data Unit) session jednoznačně identifikováno. Pravidlo obsahuje spouštěče (triggery), které definují události pro hlášení; ty mohou být založeny na prahových hodnotách (např. objem dat v uplinku/downlinku, doba trvání session), na konkrétních výskytech (např. start/stop služby, změna lokace) nebo jejich kombinaci.

Když je URR aktivní, SMF monitoruje relevantní provoz vůči nastaveným spouštěčům. Při výskytu spouštěcí události SMF vygeneruje hlášení monitorování využití (Usage Monitoring Report). Toto hlášení obsahuje detailní informace, jako je ID URR, monitorované objemy (potenciálně rozdělené podle ratingové skupiny nebo QoS Flow), spouštěcí událost a časová razítka. SMF poté toto hlášení odešle PCF, typicky přes referenční bod N7, pomocí servisní operace Npcf_SMPolicyControl_Update. PCF používá tyto nahlášené údaje pro více účelů, včetně rozhodování o politikách v reálném čase, korelace pro účtování a jako vstup pro [CHF](/mobilnisite/slovnik/chf/) (Charging Function) pro online nebo offline účtování.

Architektonicky URR fungují v rámci modulů pro vynucování politik a sběr dat v SMF. Jsou těsně integrovány se správou QoS Flow a pravidly pro detekci paketů. Jedna PDU session může mít současně aktivních více URR, z nichž každé monitoruje jiný aspekt session – například jedno URR může monitorovat celkový objem dat pro účtování, zatímco jiné monitoruje objem pro konkrétní sponzorovanou službu. Tato granularita umožňuje sofistikovanou diferenciaci služeb. Hlášení může být jednorázové (při jedné události) nebo opakované (např. hlášení každých 100 MB spotřebovaných dat). Framework URR je rozšiřitelný a umožňuje definovat nové typy spouštěčů v pozdějších vydáních 3GPP pro podporu nových služeb, jako je síťové dělení (network slicing) nebo edge computing.

## K čemu slouží

URR bylo zavedeno, aby odstranilo omezení statického hlášení na úrovni session v předchozích generacích sítí, které bylo nedostatečné pro dynamické a na služby bohaté prostředí 5G. V 4G EPC bylo hlášení využití často vázáno na zřizování a modifikaci bearerů a postrádalo granularitu potřebnou pro hlášení na vyžádání řízené událostmi, které vyžadují nové obchodní modely, jako jsou sponzorovaná data, QoS na vyžádání a analýzy v reálném čase. URR poskytuje flexibilní mechanismus řízený politikami, který odděluje hlášení od událostí správy session.

Jeho vytvoření bylo motivováno potřebou inteligentnějšího řízení politik. Operátoři potřebují detailní přehled o využití sítě, aby mohli implementovat pokročilé schémata účtování (např. podle denní doby, specifické pro aplikaci), vynucovat politiky spravedlivého využití a poskytovat záruky služeb. URR to umožňuje tím, že [PCF](/mobilnisite/slovnik/pcf/) může dynamicky instruovat [SMF](/mobilnisite/slovnik/smf/), co má monitorovat a kdy to hlásit, na základě profilu účastníka, stavu sítě nebo logiky služby. Tato flexibilita je klíčová pro podporu síťového dělení (Network Slicing), kde různé slice mohou mít zcela odlišné požadavky na hlášení pro izolaci a účtování.

Dále URR usnadňuje konvergenci politik a účtování. Poskytnutím detailních hlášení založených na spouštěčích umožňuje PCF činit informovaná rozhodnutí, která přímo ovlivňují účtování v CHF. Tím se řeší problém se zpožděnými nebo dávkovanými daty o využití a umožňuje se kontrola výdajových limitů v reálném čase, správa kvót a okamžité snížení nebo zvýšení úrovně služby na základě spotřebovaných prostředků, čímž se zlepšuje uživatelský zážitek a zajištění příjmů operátora.

## Klíčové vlastnosti

- Událostmi spouštěné hlášení na základě konfigurovatelných prahových hodnot (objem, doba trvání) nebo specifických síťových/aplikačních událostí
- Podpora monitorování agregovaného využití napříč více datovými toky služeb (SDF) nebo pro jednotlivý SDF
- Dynamické zřizování, modifikace a odebrání PCF během aktivní PDU session
- Generování detailních hlášení monitorování využití včetně objemů, časových razítek a příčiny spuštění
- Integrace s modelem QoS v 5G, umožňující hlášení korelované ke specifickým identifikátorům QoS Flow
- Rozšiřitelný framework pro definici nových hlášených událostí a metrik v následujících vydáních 3GPP

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [URR na 3GPP Explorer](https://3gpp-explorer.com/glossary/urr/)
