---
slug: "rose"
url: "/mobilnisite/slovnik/rose/"
type: "slovnik"
title: "ROSE – Remote Operation Service Element"
date: 2025-01-01
abbr: "ROSE"
fullName: "Remote Operation Service Element"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rose/"
summary: "ROSE je aplikační protokol vrstvy OSI pro vzdálené operace, který umožňuje interakce typu klient-server, jako je požadavek, odpověď a hlášení chyb. Používá se v 3GPP pro CAMEL a další služby inteligen"
---

ROSE je aplikační protokol vrstvy OSI, který umožňuje vzdálené klient-server operace, jako jsou požadavky a odpovědi, a poskytuje standardizovaný rámec pro služby, jako je CAMEL v sítích 3GPP.

## Popis

Remote Operation Service Element (ROSE) je protokol definovaný v rámci aplikační vrstvy referenčního modelu Open Systems Interconnection ([OSI](/mobilnisite/slovnik/osi/)). Funguje jako servisní prvek, který poskytuje obecný mechanismus pro vyvolání operací na vzdáleném systému a přijímání výsledků. ROSE sám o sobě nedefinuje konkrétní operace; místo toho nabízí protokolovou mašinérii pro přenos vyvolání operací a jejich výsledků. Používá se spolu s dalšími aplikačními servisními prvky, jako je Association Control Service Element ([ACSE](/mobilnisite/slovnik/acse/)), k navázání a správě asociací mezi aplikačními procesy.

V kontextu 3GPP je ROSE základním protokolem používaným v rámci funkce Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)), která umožňuje operátorské specifické služby v mobilních sítích. V rámci CAMEL se ROSE používá pro komunikaci mezi CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) a dalšími síťovými entitami, jako je gsmSCF (CAMEL Service Control Function). Přenáší operace a parametry definované v CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) zprávách. Protokol podporuje pět základních protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)): ROIV (vyvolání), RORS (návrat výsledku), ROER (návrat chyby), RORJ (zamítnutí) a ROIVap (propojené vyvolání).

ROSE funguje tak, že umožňuje vyvolávající aplikační entitě odeslat požadavek RO-INVOKE prováděcí aplikační entitě. Požadavek obsahuje kód operace a přidružené argumenty. Prováděcí entita operaci provede a může vrátit výsledek (RO-RESULT), chybu (RO-ERROR), nebo může vyvolávající entita operaci zamítnout (RO-REJECT). ROSE spravuje korelaci odpovědí s jejich původními požadavky pomocí identifikátorů vyvolání (invoke IDs). Jeho role je klíčová pro umožnění služeb inteligentní sítě ([IN](/mobilnisite/slovnik/in/)), poskytuje spolehlivou, standardizovanou a spojově orientovanou metodu pro vzdálené provádění procedur mezi různými síťovými uzly, což zajišťuje interoperabilitu mezi zařízeními od různých výrobců.

## K čemu slouží

ROSE byl vytvořen, aby řešil potřebu standardizované, na výrobci nezávislé metody provádění vzdálených operací v distribuovaných telekomunikačních systémech. Před jeho přijetím se pro podobné funkce často používaly proprietární protokoly, což vedlo k problémům s interoperabilitou a zvýšené složitosti v síťových prostředích s více výrobci. Jako součást sady protokolů [OSI](/mobilnisite/slovnik/osi/) poskytl ROSE obecný, znovupoužitelný rámec pro interakce klient-server, který byl nezbytný pro vývoj pokročilých, programovatelných síťových služeb.

V 3GPP byla primární motivací pro použití ROSE podpora funkce CAMEL, která byla zavedena pro poskytování operátorských specifických služeb (jako předplacené služby, filtrování hovorů a VPN), které jsou prováděny transparentně napříč navštívenými sítěmi. ROSE poskytl ideální podkladový protokolový mechanismus pro provádění servisní logiky CAMEL. Vyřešil problém, jak spolehlivě a konzistentně vyvolat operace servisní logiky na vzdáleném servisním řídicím bodu (gsmSCF) ze servisního spínacího bodu (MSC nebo GMSC). Jeho formální, strukturovaný přístup k vyvolání operací, hlášení výsledků a zpracování chyb zajistil, že služby CAMEL mohly být robustně nasazeny a škálovány v globálních sítích.

## Klíčové vlastnosti

- Standardizovaný aplikační protokol vrstvy OSI pro vzdálené operace
- Podporuje pět základních PDU: Vyvolání (Invoke), Návrat výsledku (Return Result), Návrat chyby (Return Error), Zamítnutí (Reject) a Propojené vyvolání (Linked Invoke)
- Poskytuje spolehlivou korelaci požadavků a odpovědí pomocí identifikátorů vyvolání (invoke IDs)
- Umožňuje spojově orientovanou, asociací založenou komunikaci při použití s ACSE
- Tvoří transportní mechanismus pro operace CAMEL Application Part (CAP)
- Usnadňuje interoperabilitu mezi výrobci pro služby inteligentní sítě

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [ACSE – Association Control Service Element](/mobilnisite/slovnik/acse/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [ROSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rose/)
