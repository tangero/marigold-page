---
slug: "icsi"
url: "/mobilnisite/slovnik/icsi/"
type: "slovnik"
title: "ICSI – IMS Communication Service Identifier"
date: 2026-01-01
abbr: "ICSI"
fullName: "IMS Communication Service Identifier"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/icsi/"
summary: "ICSI je jedinečný identifikátor používaný v rámci IMS k rozlišení různých IMS komunikačních služeb (ICS), jako je Voice over LTE (VoLTE), Video over LTE (ViLTE) nebo Rich Communication Services (RCS)."
---

ICSI je jedinečný identifikátor používaný v rámci IMS k rozlišení různých komunikačních služeb, jako je VoLTE nebo RCS, který umožňuje síti a UE identifikovat vyvolávanou službu pro správné uplatňování politik.

## Popis

IMS Communication Service Identifier (ICSI) je standardizovaný alfanumerický token (např. 'urn:urn-7:3gpp-service.ims.icsi.mmtel' pro Multimedia Telephony) definovaný organizací 3GPP. Je klíčovým mechanismem pro identifikaci a diferenciaci služeb v rámci IP Multimedia Subsystem. ICSI je asociován s konkrétní IMS komunikační službou ([ICS](/mobilnisite/slovnik/ics/)), což je standardizovaná sada schopností a procedur (jako MMTel pro telefonii). Když User Equipment (UE) zahajuje nebo přijímá relaci, zahrne relevantní hodnotu ICSI do signalizace [SIP](/mobilnisite/slovnik/sip/), typicky v hlavičkovém poli Contact nebo P-Asserted-Service.

Při přijetí SIP požadavku obsahujícího ICSI mohou síťové prvky jako [P-CSCF](/mobilnisite/slovnik/p-cscf/), [S-CSCF](/mobilnisite/slovnik/s-cscf/) a Application Servers ([AS](/mobilnisite/slovnik/as/)) tento identifikátor zkontrolovat. To jim umožní přesně určit, která služba je požadována. Tato identifikace spouští uplatnění služebně specifických politik, směrovací logiky a účtovacích pravidel. Například VoLTE hovor identifikovaný svým ICSI může být směrován na konkrétní Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)), podléhat jiné prioritizaci QoS (Quality of Service) než běžná datová relace a být účtován podle tarifních plánů pro hlas.

ICSI spolupracuje s IMS Application Reference Identifier ([IARI](/mobilnisite/slovnik/iari/)), který identifikuje konkrétní aplikace v rámci služby. ICSI poskytuje širší servisní kontext. S-CSCF používá filtrační kritéria v servisním profilu uživatele, která mohou být porovnána s ICSI, aby rozhodl, zda má relaci předat konkrétnímu Application Serveru. To umožňuje modulární architekturu služeb, kde nové služby lze zavést definováním nového ICSI a odpovídající síťové logiky bez zásadních změn základního směrovacího mechanismu IMS. ICSI je nezbytný pro umožnění více souběžných služeb v rámci jedné registrace IMS a pro zajištění zpětné a dopředné kompatibility mezi UE a síťovými uzly různých verzí.

## K čemu slouží

Vytvoření ICSI bylo motivováno potřebou překročit monolitický koncept 'IMS služby' a přejít k prostředí, kde může koexistovat více různých komunikačních služeb, které lze nezávisle vyvíjet, nasazovat a spravovat na stejné základní infrastruktuře. Před jeho standardizací byla identifikace služby často implicitní nebo založená na nestandardních rozšířeních, což vedlo k problémům s interoperabilitou a obtížím při zavádění nových služeb.

Řeší problém jednoznačného výběru a vyvolání služby. Ve scénáři, kdy zařízení uživatele podporuje VoLTE, ViLTE a [RCS](/mobilnisite/slovnik/rcs/) chat, potřebuje síť vědět, která konkrétní služba je pro danou relaci používána, aby mohla uplatnit správné zacházení (např. směrování pro tísňové služby u hlasu, vyjednávání video kodeku pro video, ukládání a přeposílání zpráv u chatu). ICSI poskytuje tento jasný, standardizovaný signál.

Dále umožňuje efektivní spouštění služeb a vynucování politik. Síťoví operátoři mohou konfigurovat pravidla na základě hodnot ICSI, aby směrovali provoz na příslušné aplikační servery, uplatňovali specifické QoS profily a implementovali přesné účtování. Tato granularita je základní pro komerční nabídky služeb, umožňuje operátorům vytvářet diferencované servisní plány a zajistit konzistentní uživatelský zážitek pro každý typ komunikační služby. ICSI se stal jedním ze základních kamenů komercializace IMS, počínaje MMTel (VoLTE/ViLTE) a rozšiřujíc se na další služby.

## Klíčové vlastnosti

- Jednoznačně identifikuje standardizovanou IMS komunikační službu (např. MMTel, RCS)
- Přenášen v hlavičkách signalizace SIP (např. P-Asserted-Service) pro identifikaci relace
- Používán S-CSCF pro porovnání s Initial Filter Criteria (iFC) a směrování relací na správný Application Server
- Umožňuje uplatnění služebně specifických síťových politik pro QoS, účtování a zabezpečení
- Umožňuje jednomu UE registrovat se k IMS pouze jednou, ale vyvolávat více různých služeb
- Napomáhá interoperabilitě mezi UE a sítěmi od různých výrobců a operátorů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [IARI – IMS Application Reference Identifier](/mobilnisite/slovnik/iari/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [ICSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/icsi/)
