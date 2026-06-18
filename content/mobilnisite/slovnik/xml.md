---
slug: "xml"
url: "/mobilnisite/slovnik/xml/"
type: "slovnik"
title: "XML – Extensible Markup Language"
date: 2025-01-01
abbr: "XML"
fullName: "Extensible Markup Language"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xml/"
summary: "XML je značkovací jazyk standardizovaný konsorciem W3C, který je v rámci specifikací 3GPP hojně využíván pro reprezentaci a výměnu dat. Poskytuje flexibilní textový formát pro strukturování konfigurač"
---

XML je značkovací jazyk standardizovaný konsorciem W3C, používaný napříč specifikacemi 3GPP pro strukturování a výměnu konfiguračních dat, popisů služeb a řídicích informací v textovém formátu čitelném pro člověka a zpracovatelném počítačem.

## Popis

V rámci architektury 3GPP není Extensible Markup Language (XML) technologií vynalezenou 3GPP, ale základním, široce přijímaným standardem (od [W3C](/mobilnisite/slovnik/w3c/)), který je používán jako datový formát a syntaxe pro zprávy v četných specifikacích. Funguje na principu definování souboru pravidel pro kódování dokumentů ve formátu, který je zároveň čitelný pro člověka a zpracovatelný počítačem. Data jsou strukturována pomocí uživatelsky definovaných značek uzavřených v lomených závorkách, čímž vzniká hierarchický strom elementů a atributů. Tato strukturovaná povaha umožňuje přesnou definici složitých datových modelů, jako jsou příkazy pro správu zařízení, parametry služeb nebo pravidla politik.

Role XML v systémech 3GPP je mnohostranná. V jádru sítě tvoří základ pro protokol Open Mobile Alliance Device Management ([OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/)), používaný pro dálkovou konfiguraci a správu uživatelského zařízení (UE). Řídicí příkazy a data zařízení jsou formátovány jako XML dokumenty pro výměnu mezi DM serverem a klientem na zařízení. Pro služby je XML používáno v IP Multimedia Subsystem (IMS) pro konfiguraci služeb (např. na referenčním bodě Ut pro [XCAP](/mobilnisite/slovnik/xcap/)) a ve formátech dat služby Presence. V oblasti správy sítě Model síťových zdrojů 3GPP ([NRM](/mobilnisite/slovnik/nrm/)) a související specifikace rozhraní často používají XML schémata k definování informačního modelu vyměňovaného mezi síťovými elementy a řídicími systémy.

Zpracování XML v kontextu 3GPP zahrnuje parsery a validátory uvnitř síťových elementů a zařízení. Když je přijat XML dokument, parser jej přečte, zkontroluje jeho správnou formu (správnou syntaxi) a může jej validovat proti předem definovanému XML Schema Definition ([XSD](/mobilnisite/slovnik/xsd/)), aby zajistil, že odpovídá očekávané datové struktuře. Extrahovaná data jsou následně použita aplikační logikou – například pro aktualizaci konfigurace zařízení, aplikaci nové služební politiky nebo naplnění báze řídicích informací. Tím dochází k oddělení reprezentace dat od zpracovací logiky, což podporuje interoperabilitu. Mezi klíčové komponenty jeho použití patří XML namespaces (pro zabránění konfliktům názvů značek), XSD pro validaci a XPath pro dotazování na konkrétní data v rámci XML dokumentu.

## K čemu slouží

XML bylo přijato do specifikací 3GPP, aby vyřešilo problém heterogenní reprezentace dat a potřebu flexibilní, rozšiřitelné výměny informací mezi síťovými entitami, řídicími systémy a zařízeními. Před jeho rozšířeným používáním byly běžné proprietární binární formáty nebo méně strukturované textové formáty, což bránilo interoperabilitě mezi více dodavateli a ztěžovalo a prodražovalo integraci systémů. XML poskytlo standardizovaný, dodavatelsky neutrální způsob popisu a přenosu strukturovaných dat.

Historický kontext jeho přijetí se časově shoduje s přechodem na plně IP sítě v 3G (UMTS) a vývojem rozsáhlých datových služeb. Jak se sítě stávaly více řízenými softwarem a služby složitějšími, objevila se kritická potřeba datového formátu, který by se mohl snadno vyvíjet. Rozšiřitelnost XML umožnila pracovním skupinám 3GPP definovat nové datové elementy pro nové funkce (jako IMS nebo LTE) bez narušení stávajících systémů, protože parsery mohly ignorovat značky, kterým nerozuměly. To bylo klíčové pro dopřednou a zpětnou kompatibilitu.

Dále XML řešilo potřebu automatizace v síťové a zařízeníové správě. Vzestup [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/) vyžadoval formát, který by mohl reprezentovat složité řídicí objekty (jako nastavení APN zařízení nebo preference aplikací). Hierarchická struktura XML tyto objekty dokonale modelovala. Jeho textová povaha také zjednodušila ladění a logování ve srovnání s binárními protokoly. Účelem XML v 3GPP je tedy být lingua franca pro strukturovaná data, umožňující konfiguraci, správu a poskytování stále sofistikovanějších mobilních sítí a služeb interoperabilním způsobem.

## Klíčové vlastnosti

- Textový značkovací jazyk čitelný pro člověka s uživatelsky definovanými značkami
- Hierarchická stromová struktura pro reprezentaci složitých datových modelů
- Podpora validace pomocí XML Schema Definitions (XSD)
- Rozšiřitelnost prostřednictvím jmenných prostorů (namespaces) a tvorby vlastních schémat
- Široké použití pro protokoly OMA Device Management (DM)
- Základ pro reprezentaci dat v IMS (např. XCAP) a rozhraních pro správu sítě

## Související pojmy

- [XCAP – XML Configuration Access Protocol](/mobilnisite/slovnik/xcap/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.337** (Rel-19) — IMS Inter-UE Transfer Protocol Specification
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.424** (Rel-19) — XCAP over Ut for Supplementary Services MO
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 24.608** (Rel-19) — 3GPP TS 24608: TIP/TIR Services Protocol
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [XML na 3GPP Explorer](https://3gpp-explorer.com/glossary/xml/)
