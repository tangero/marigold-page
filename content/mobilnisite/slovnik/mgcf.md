---
slug: "mgcf"
url: "/mobilnisite/slovnik/mgcf/"
type: "slovnik"
title: "MGCF – Media Gateway Control Function"
date: 2025-01-01
abbr: "MGCF"
fullName: "Media Gateway Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mgcf/"
summary: "Media Gateway Control Function (MGCF) je klíčový síťový prvek IMS, který zajišťuje převod protokolů mezi signalizací IMS založenou na SIP a starší signalizací okruhového přepojování (např. ISUP, BICC)"
---

MGCF je síťový prvek IMS, který provádí převod protokolů mezi signalizací SIP a starší signalizací okruhového přepojování a řídí IMS-Media Gateway, aby umožnil hovory mezi IMS a tradičními telefonními sítěmi.

## Popis

Media Gateway Control Function (MGCF) je specializovaná funkce řídicí roviny v rámci architektury IP Multimedia Subsystem (IMS). Jejím hlavním úkolem je fungovat jako signalizační brána a řadič pro relace, které musí procházet mezi doménou IMS s paketovým přepojováním (která používá SIP - Session Initiation Protocol) a světem starší telefonie s okruhovým přepojováním ([CS](/mobilnisite/slovnik/cs/)), který používá protokoly jako [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) nebo BICC (Bearer Independent Call Control). MGCF je v IMS protějškem k Media Gateway Controller ([MGC](/mobilnisite/slovnik/mgc/)) v CS doméně, je však speciálně navržena pro provoz v rámci SIP-centrického IMS.

Architektonicky se MGCF nachází na hranici mezi jádrem IMS a externími CS sítěmi, jako je veřejná telefonní síť (PSTN) nebo starší PLMN. Má několik klíčových rozhraní. Směrem k jádru IMS komunikuje s [CSCF](/mobilnisite/slovnik/cscf/) (Call Session Control Function) pomocí rozhraní Mg založeného na SIP. Když uživatel IMS volá na číslo PSTN, je SIP INVITE směrován na MGCF. MGCF pak provede převod protokolu, převede signalizaci SIP na příslušnou zprávu ISUP nebo BICC. Naopak pro příchozí hovor z PSTN přijme signalizaci ISUP/BICC a přeloží ji do SIP INVITE pro směrování do IMS. Pro správu skutečné přenosové cesty médií MGCF řídí IMS-Media Gateway ([IMS-MGW](/mobilnisite/slovnik/ims-mgw/)) pomocí protokolu H.248 přes rozhraní Mn. Příkazuje IMS-MGW, aby provedl potřebné funkce pro propojení médií, jako je překódování mezi kodekem pro paketový hlas (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/) používaný v IMS) a PCM TDM okruhem z PSTN, nebo přehrávání hlášení a tónů.

Při provozu zahrnuje pracovní postup MGCF několik kroků. Provádí analýzu a překlad adres (např. převod čísla E.164 z PSTN na SIP URI pro směrování v IMS a naopak). Spravuje stav hovoru pro část relace zajišťující propojení, čímž zajišťuje koherenci signalizace mezi oběma odlišnými doménami. MGCF také spolupracuje s dalšími funkcemi IMS, jako je Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)), pro výběr vhodné sítě pro přechod do CS domény. Její návrh je klíčový pro zajištění bezproblémové kontinuity služeb, podporuje nejen základní hlasové hovory, ale také doplňkové služby, jako je přesměrování hovoru, identifikace volajícího a čekání na hovor přes síťovou hranici.

## K čemu slouží

MGCF byla vytvořena k řešení zásadní výzvy při přechodu na plně IP sítě: jak zachovat bezproblémovou interoperabilitu mezi novým IMS založeným na SIP a rozsáhlou, zavedenou infrastrukturou globální telefonní sítě s okruhovým přepojováním. Bez MGCF by bylo IMS izolovaným "ostrovem" neschopným komunikovat s miliardami stávajících pevných a mobilních telefonů. Její vývoj byl motivován vizí 3GPP pro IMS jako jednotnou platformu pro poskytování multimediálních služeb, což vyžadovalo robustní a standardizovanou funkci pro vzájemné propojení.

Historicky, jak bylo IMS definováno od 3GPP Release 5 výše, řešila MGCF omezení dřívějších proprietárních řešení bran. Poskytla standardizovaný, škálovatelný způsob, jak zvládnout složitou signalizaci a mapování médií potřebné pro mezidoménové hovory. To umožnilo operátorům sítí nasazovat IMS pro nové služby (jako VoLTE a RCS) a zároveň garantovat zpětnou kompatibilitu, chránit své stávající investice a zajistit hladkou migrační cestu pro účastníky. MGCF spolu s IMS-MGW tvoří podsystém brány PSTN/CS, který je nezbytný pro komerční úspěch jakéhokoli nasazení IMS.

## Klíčové vlastnosti

- Provádí převod protokolů mezi signalizací IMS SIP a signalizací CS sítě (ISUP/BICC)
- Řídí IMS-Media Gateway (IMS-MGW) pomocí protokolu H.248 pro propojení médií
- Komunikuje s CSCF v IMS (rozhraní Mg) a s CS sítěmi (např. přes ISUP)
- Provádí analýzu čísel a směrování pro hovory vstupující do IMS domény nebo z ní vystupující
- Spravuje stav hovoru a vzájemné propojení doplňkových služeb přes síťové hranice
- Spolupracuje s BGCF při výběru vhodného bodu pro přechod do CS sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- … a dalších 42 specifikací

---

📖 **Anglický originál a plná specifikace:** [MGCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgcf/)
