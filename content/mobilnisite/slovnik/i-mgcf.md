---
slug: "i-mgcf"
url: "/mobilnisite/slovnik/i-mgcf/"
type: "slovnik"
title: "I-MGCF – Incoming - Media Gateway Control Function"
date: 2025-01-01
abbr: "I-MGCF"
fullName: "Incoming - Media Gateway Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/i-mgcf/"
summary: "I-MGCF je funkční komponenta v rámci IP Multimedia Subsystem (IMS), která zpracovává příchozí relace hovorů z přepojovaných okruhů sítí, jako je PSTN nebo starší PLMN. Provádí protokolovou interoperab"
---

I-MGCF je funkční komponenta IMS, která zpracovává příchozí relace hovorů z přepojovaných okruhů sítí tím, že provádí protokolovou interoperabilitu a řídí Media Gateway pro převod médií.

## Popis

Incoming - Media Gateway Control Function (I-MGCF) je klíčový síťový prvek v architektuře 3GPP IP Multimedia Subsystem (IMS), speciálně navržený pro zpracování řízení relací u příchozích hovorů pocházejících z externích přepojovaných okruhů ([CS](/mobilnisite/slovnik/cs/)) sítí, jako je Public Switched Telephone Network ([PSTN](/mobilnisite/slovnik/pstn/)) nebo starší Public Land Mobile Networks ([PLMN](/mobilnisite/slovnik/plmn/)). Funguje jako signalizační brána a řadič na hranici mezi doménou IMS s přepojováním paketů a světem přepojování okruhů. Hlavní úlohou I-MGCF je provádět protokolovou interoperabilitu mezi signalizací [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) nebo BICC (Bearer Independent Call Control) používanou v CS sítích a protokolem [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) používaným v IMS. Po přijetí příchozího hovoru ISUP/BICC I-MGCF ukončí CS signalizaci, interpretuje informace o sestavení hovoru a iniciuje odpovídající SIP relaci směrem k jádru IMS. Řídí přidružené Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pomocí protokolu H.248 (Megaco), kterému nařizuje vytvoření potřebných přenosových spojení a provedení převodu médií mezi kanály s časovým multiplexem ([TDM](/mobilnisite/slovnik/tdm/)) nebo přenosovými kanály s přepojováním okruhů a paketovými proudy RTP/RTCP používanými v IMS. I-MGCF komunikuje s dalšími entitami IMS, jako je Breakout Gateway Control Function (BGCF) pro rozhodování o směrování a Home Subscriber Server (HSS) pro autorizaci služeb. Jeho fungování je podrobně popsáno v několika specifikacích 3GPP, včetně TS 24.411 (mapování ISUP na SIP), TS 24.428 (pokyny), TS 24.528 (konfigurace) a TS 29.163 (interoperabilní signalizace). Díky této roli je I-MGCF základním kamenem pro konvergenci pevných a mobilních sítí a bezproblémovou integraci starších telefonních služeb s moderními IP multimediálními službami.

## K čemu slouží

I-MGCF byl vytvořen k vyřešení zásadního problému vývoje sítí: jak propojit rozsáhlou stávající infrastrukturu telefonních sítí s přepojováním okruhů s novým plně IP jádrem IMS. Bez vyhrazené funkce pro interoperabilitu by byli účastníci ve starších sítích izolováni od pokročilých multimediálních služeb nabízených IMS, a naopak. I-MGCF poskytuje standardizovanou, škálovatelnou bránu, která překládá nejen média (přes MGW), ale, což je důležitější, signalizaci řízení hovoru. To umožňuje síťovým operátorům zavádět IMS postupně, aniž by narušili stávající služby PSTN/PLMN. Řeší omezení předchozích, často proprietárních, řešení brán tím, že definuje jasné funkční oddělení mezi řízením hovoru (I-MGCF) a zpracováním médií (MGW), v souladu s principem IMS oddělovat řídicí a uživatelskou rovinu. Jeho vytvoření ve vydání 7 bylo motivováno potřebou upevnit IMS jako zralou architekturu schopnou podporovat telekomunikační služby na úrovni operátora, včetně propojení se sítěmi jiných operátorů. Umožnil vizi jednotného jádra sítě, které by mohlo obsluhovat jak mobilní, tak pevné přístupové technologie, a tím zajistit interoperabilitu služeb, jako je Voice over LTE (VoLTE) a Rich Communication Services (RCS), s globální telefonní sítí.

## Klíčové vlastnosti

- Ukončuje signalizaci ISUP nebo BICC ze sítí s přepojováním okruhů
- Iniciuje SIP relace směrem k jádru IMS pro příchozí hovory
- Řídí Media Gateway pomocí protokolu H.248 (Megaco)
- Provádí nezbytné vyjednávání kodeků a správu přenosových prostředků
- Spolupracuje s BGCF při rozhodování o směrování příchozích hovorů
- Podporuje nezbytnou interoperabilitu doplňkových služeb (např. přesměrování hovoru, CLIP)

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [BGCF – Breakout Gateway Control Function](/mobilnisite/slovnik/bgcf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [I-MGCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-mgcf/)
