---
slug: "scscf"
url: "/mobilnisite/slovnik/scscf/"
type: "slovnik"
title: "SCSCF – Serving Call Session Control Function"
date: 2025-01-01
abbr: "SCSCF"
fullName: "Serving Call Session Control Function"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/scscf/"
summary: "SCSCF je centrální uzel v jádrové síti IMS (IP Multimedia Subsystem). Zajišťuje řízení relací, autentizaci uživatelů a spouštění služeb pro multimediální služby, jako jsou VoLTE a VoNR. Je klíčový pro"
---

SCSCF je centrální uzel v jádrové síti IMS, který zajišťuje řízení relací, autentizaci uživatelů a spouštění služeb pro IP multimediální služby, jako je VoLTE.

## Popis

Serving Call Session Control Function (SCSCF) je základní komponenta v architektuře IP Multimedia Subsystem (IMS) definované 3GPP. Funguje jako [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) server a představuje centrální bod pro řízení relací a poskytování služeb pro účastníky IMS. Při registraci uživatele SCSCF provede jeho autentizaci prostřednictvím [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) a stáhne uživatelský servisní profil, který obsahuje počáteční filtrační kritéria (iFC). Tato iFC se používají k určení, jak mají být příchozí a odchozí SIP relace směrovány na příslušné aplikační servery ([AS](/mobilnisite/slovnik/as/)) pro přidané služby.

Během navazování relace SCSCF provádí rozhodnutí o směrování na základě identifikátoru požadované služby a uživatelského profilu. Interaguje s dalšími funkcemi jádra IMS, jako je [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-CSCF), který je prvním kontaktním bodem pro UE, a [I-CSCF](/mobilnisite/slovnik/i-cscf/) (Interrogating-CSCF), který je zodpovědný za výběr vhodného SCSCF během registrace. SCSCF také vynucuje síťové politiky prostřednictvím interakce s [PCRF](/mobilnisite/slovnik/pcrf/) (Policy and Charging Rules Function) pro autorizaci prostředků a správu kvality služeb (QoS).

Jeho role přesahuje základní směrování hovorů; je zodpovědný za udržování registračního stavu, správu SIP dialogů a generování záznamů o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro účely fakturace. SCSCF je navržen jako bezstavový pro jednotlivé transakce, ale stavový pro dialogy, což umožňuje škálovatelnost a spolehlivost. Je povinným prvkem pro zajištění standardizovaných multimediálních služeb, jako je Voice over LTE (VoLTE), Voice over NR (VoNR), Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)) a dalších služeb reálného času založených na IP napříč mobilními a pevnými sítěmi.

## K čemu slouží

SCSCF byl zaveden, aby poskytl standardizovanou řídicí rovinu pro multimediální služby založené na IP, oddělující servisní logiku od podkladové přenosové sítě. Před IMS byly hlasové a zprávové služby těsně svázány s přepojováním okruhů, což omezovalo inovace a integraci služeb. SCSCF umožňuje konvergenci hlasových, video a datových služeb přes společnou IP infrastrukturu a usnadňuje přechod od starších sítí s přepojováním okruhů k plně IP sítím.

Řeší problém fragmentovaného poskytování služeb tím, že poskytuje centrální, na službách nezávislou funkci řízení relací. To umožňuje síťovým operátorům a poskytovatelům třetích stran nasazovat a spravovat služby nezávisle na přístupové technologii (např. LTE, 5G NR, Wi-Fi). Použití standardizovaných SIP protokolů v SCSCF zajišťuje interoperabilitu mezi zařízeními různých výrobců a napříč hranicemi operátorů, což je nezbytné pro roamování a globální poskytování služeb. Jeho vytvoření bylo motivováno potřebou flexibilní, škálovatelné architektury pro podporu rostoucí poptávky po multimediálních aplikacích a umožnění nových zdrojů příjmů pro operátory.

## Klíčové vlastnosti

- Centrální řízení SIP relací pro IMS
- Autentizace uživatelů a správa registračního stavu
- Spouštění služeb na základě počátečních filtračních kritérií (iFC)
- Interakce s HSS pro účastnická data a s aplikačními servery pro služby
- Vynucování politik prostřednictvím rozhraní k PCRF
- Generování záznamů o účtování (CDR) pro fakturaci

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [SCSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/scscf/)
