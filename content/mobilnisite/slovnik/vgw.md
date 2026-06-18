---
slug: "vgw"
url: "/mobilnisite/slovnik/vgw/"
type: "slovnik"
title: "VGW – Voice over IP Gateway"
date: 2025-01-01
abbr: "VGW"
fullName: "Voice over IP Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vgw/"
summary: "VGW je síťová brána, která propojuje okruhově přepínané hlasové sítě (jako PSTN nebo starší mobilní sítě) s IP sítěmi (jako IMS nebo internet). Převádí hlasový provoz mezi TDM a IP formáty, čímž umožň"
---

VGW je síťová brána, která propojuje okruhově přepínané hlasové sítě s IP sítěmi převodem hlasového provozu mezi TDM a IP formáty, aby umožnila kontinuitu hovorů a interoperabilitu služeb.

## Popis

Voice over IP Gateway (VGW) je základní síťový prvek definovaný ve specifikacích 3GPP, který usnadňuje interoperabilitu mezi tradičními okruhově přepínanými ([CS](/mobilnisite/slovnik/cs/)) hlasovými sítěmi a paketově přepínanými ([PS](/mobilnisite/slovnik/ps/)) IP sítěmi. Architektonicky funguje jako kombinace mediální brány a signalizační brány, která zvládá jak převod hlasových médií, tak překlad řídicích protokolů. Mezi klíčové komponenty patří jednotky pro zpracování médií, které převádějí hlas mezi formáty s časovým multiplexem ([TDM](/mobilnisite/slovnik/tdm/)) používanými v CS sítích (např. [PSTN](/mobilnisite/slovnik/pstn/), GSM) a proudy Realtime Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) používanými v IP sítích (např. IMS, VoIP služby), a také signalizační adaptéry, které převádějí protokoly jako [ISUP](/mobilnisite/slovnik/isup/) nebo BICC na [SIP](/mobilnisite/slovnik/sip/) nebo Diameter. VGW je typicky nasazena na hranicích sítí, například mezi CS jádrem mobilního operátora a IP Multimedia Subsystem (IMS), aby umožnila plynulou kontinuitu hlasových hovorů a integraci služeb.

Během provozu VGW přijímá hlasové hovory z CS domény přes rozhraní jako Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo přímo z Mobile Switching Centre (MSC). Extrahuje hlasové datové jednotky z TDM časových slotů, komprimuje je pomocí kodeků jako AMR nebo G.711 a zabalí je do RTP paketů pro přenos přes IP sítě. Naopak pro příchozí IP hlasový provoz rozbalí RTP proudy, dekóduje hlasová data a namapuje je na TDM okruhy pro doručení do CS koncových bodů. Z pohledu signalizace VGW překládá zprávy pro navázání, ukončení hovoru a aktivaci služeb mezi CS signalizačními protokoly (např. ISUP pro trunkovou signalizaci) a IP signalizačními protokoly (např. SIP pro IMS), často pod kontrolou samostatného Media Gateway Controller (MGC) nebo MGCF. Tento obousměrný převod zajišťuje, že účastníci na starších sítích mohou komunikovat s těmi na moderních IP sítích bez degradace služby.

VGW hraje klíčovou roli v strategiích vývoje sítí, jako je Voice over LTE (VoLTE) a nasazení hlasu v 5G, kde operátoři migrují z CS na plně IP jádra. Podporuje funkce jako přechod na CS pro hlasové hovory, když není dostupné IP pokrytí, známé jako Circuit-Switched Fallback (CSFB), a spolupráci během předávání hovorů Single Radio Voice Call Continuity (SRVCC). VGW může navíc zahrnovat bezpečnostní funkce jako šifrování a překonávání firewallů a mechanismy kvality služeb (QoS) pro upřednostnění hlasového provozu na IP spojích. Tím, že propojuje CS a PS domény, umožňuje VGW operátorům zachovat starší hlasové služby během přechodu na IP architektury a zajišťuje spolehlivou hlasovou komunikaci napříč heterogenními sítěmi.

## K čemu slouží

VGW byla vytvořena k řešení přechodu z okruhově přepínaných na paketově přepínané hlasové sítě, což je zásadní změna v telekomunikacích poháněná efektivitou a flexibilitou IP technologie. Před její standardizací byly hlasové služby převážně poskytovány přes vyhrazené CS sítě jako PSTN a GSM, které používaly TDM pro přenos hlasu a spotřebovávaly pevnou šířku pásma bez ohledu na zatížení provozem. Vzestup VoIP a IMS sliboval úsporu nákladů, bohatší služby a integraci s datovými sítěmi, ale vyžadoval způsob propojení s existující CS infrastrukturou, aby se předešlo narušení služeb pro miliardy účastníků na starších sítích. VGW to řeší tím, že poskytuje bránu, která překládá hlas a signalizaci mezi CS a IP doménami, což umožňuje postupnou migraci bez nutnosti okamžité výměny všech síťových prvků.

Motivace vychází z potřeby operátorů zavádět IP hlasové služby jako VoLTE při zachování zpětné kompatibility se 2G/3G CS sítěmi, zejména během dlouhého přechodného období, kdy obě koexistují. Bez VGW by byly CS a IP sítě izolované, což by bránilo mezidoménovým hovorům a vynucovalo duální nasazení. VGW umožňuje operátorům využívat IP pro přenos v jádru sítě, přičemž stále mohou spojovat PSTN nebo starší mobilní účastníky, což snižuje provozní náklady díky konsolidaci sítě. Také podporuje regulatorní požadavky na tísňová volání a zákonné odposlechy napříč doménami, což zajišťuje soulad během migrace.

Historicky se VGW objevila v 3GPP Release 10 jako součást širší standardizace IMS a VoLTE, což odráželo posun odvětví k plně IP sítím. Řešila omezení starších bran, které byly závislé na dodavateli nebo měly omezenou funkčnost, tím, že poskytla standardizované rozhraní pro interoperabilitu. VGW umožňuje klíčové případy použití jako CSFB, kde sítě LTE pouze pro data spoléhají na CS pro hlas, a SRVCC, které předávají hovory VoLTE do oblastí s CS pokrytím. Tím, že usnadňuje tuto spolupráci, VGW zajišťuje kontinuitu hlasových služeb, zlepšuje uživatelský zážitek a podporuje případné ukončení provozu CS sítí, což je v souladu s globálními trendy směrem k IP konvergenci.

## Klíčové vlastnosti

- Převod médií mezi TDM okruhově přepínaným hlasem a paketově přepínanými RTP hlasovými proudy
- Signalizační spolupráce mezi CS protokoly (ISUP/BICC) a IP protokoly (SIP/Diameter)
- Podpora převodu hlasových kodeků (např. AMR na G.711) a zabalení do paketů
- Umožňuje Circuit-Switched Fallback (CSFB) a Single Radio Voice Call Continuity (SRVCC)
- Integrace s IMS přes MGCF pro služby VoLTE a hlasu v 5G
- Poskytuje bezpečnostní a QoS (kvalita služeb) vynucování pro mezidoménový hlasový provoz

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)

## Definující specifikace

- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework

---

📖 **Anglický originál a plná specifikace:** [VGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/vgw/)
