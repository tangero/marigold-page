---
slug: "imcn"
url: "/mobilnisite/slovnik/imcn/"
type: "slovnik"
title: "IMCN – IP Multimedia Core Network"
date: 2025-01-01
abbr: "IMCN"
fullName: "IP Multimedia Core Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imcn/"
summary: "IP Multimedia Core Network (IMCN) je architektonický rámec definovaný 3GPP pro poskytování IP multimediálních služeb přes mobilní sítě. Umožňuje služby jako hlas přes IP (VoIP), videohovory a instant"
---

IMCN je architektonický rámec 3GPP pro poskytování IP multimediálních služeb, jako je VoIP a videohovory, přes mobilní sítě tím, že poskytuje základní funkce pro řízení relací a správu účastníků.

## Popis

IP Multimedia Core Network (IMCN) je základní architektonický rámec ve standardech 3GPP, který definuje podsystém základní sítě zodpovědný za poskytování IP multimediálních služeb. Je vybudován na IP Multimedia Subsystem (IMS), který slouží jako jeho funkční jádro. Architektura IMCN je navržena jako přístupově agnostická, což znamená, že může služby poskytovat přes různé přístupové sítě jako [GPRS](/mobilnisite/slovnik/gprs/), [WLAN](/mobilnisite/slovnik/wlan/), LTE nebo 5G NR. Funguje nezávisle na podkladové transportní vrstvě a jako primární signalizační protokol pro navazování, úpravu a ukončování multimediálních relací používá Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)). Rámec využívá existující paketově přepínanou doménu základní sítě pro transport, ale přidává vyhrazenou servisní vrstvu pro multimediální řízení.

V jádru se IMCN skládá z několika klíčových logických funkcí. Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) funguje jako SIP server, který zajišťuje řízení a směrování relací. Dělí se na Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), což je první kontaktní bod pro uživatelské zařízení (UE); Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), které provádí řízení relací a komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)); a Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)), které dotazuje HSS, aby našlo příslušné S-CSCF. Home Subscriber Server (HSS) je centrální databáze účastníků obsahující informace o předplatném a autentizaci. Media Resource Function (MRF) poskytuje služby související s médii, jako je konferenční hovor, překódování a přehrávání hlášení. Mezi další kritické komponenty patří Breakout Gateway Control Function (BGCF) pro směrování hovorů do jiných sítí a Application Server (AS) pro hostování a provádění servisní logiky.

IMCN funguje tak, že mezi zařízením uživatele a sítí naváže SIP dialog. Když uživatel zahájí multimediální službu, UE odešle SIP INVITE požadavek P-CSCF. Požadavek je směrován přes uzly CSCF, které uživatele autentizují prostřednictvím HSS a uplatňují servisní logiku z aplikačních serverů. Po autorizaci je relace navázána a média (hlas, video) jsou typicky přenášena přímo mezi koncovými body pomocí protokolů jako Real-time Transport Protocol (RTP) přes IP. IMCN poskytuje klíčové funkce jako autorizaci kvality služby (QoS), řízení politik prostřednictvím Policy and Charging Rules Function (PCRF) a propojení se staršími sítěmi s přepojováním okruhů přes Media Gateway Control Function (MGCF). Jeho úlohou je poskytnout standardizovanou, bezpečnou a škálovatelnou platformu pro interaktivní multimediální služby v reálném čase, která tvoří základ pro doručování služeb jako VoLTE, VoNR, Rich Communication Services (RCS) a dalších aplikací založených na IMS.

## K čemu slouží

IMCN byl vytvořen, aby řešil zásadní průmyslový posun od tradiční telefonie s přepojováním okruhů k paketově přepínané, IP komunikaci. Před jeho zavedením v 3GPP Release 99 byly mobilní sítě primárně navrženy pro hlasové hovory využívající technologii přepojování okruhů, která byla pro datové a multimediální služby neefektivní. Růst internetu a úspěch IP aplikací vytvořil poptávku po tom, aby mobilní operátoři nabízeli integrované hlasové, video a messagingové služby přes IP. Rámec IMCN poskytl potřebný architektonický plán, aby to bylo možné, což umožnilo operátorům vyvíjet své sítě a konkurovat poskytovatelům over-the-top (OTT) služeb.

Primární problém, který IMCN řeší, je poskytování standardizovaných, operátorsky kvalitních multimediálních služeb přes IP sítě. Umožňuje konvergenci pevných a mobilních služeb, což umožňuje funkce jako bezproblémová mobilita, konzistentní uživatelský zážitek napříč různými přístupovými technologiemi a integrace s webovými službami. Standardizací základních síťových funkcí pro IP multimedia zajistil interoperabilitu mezi zařízeními různých výrobců a napříč sítěmi operátorů, což bylo klíčové pro široké přijetí. Poskytl také řízené prostředí pro doručování služeb, což operátorům umožňuje spravovat QoS, implementovat sofistikované modely účtování a zajišťovat bezpečnost a regulatorní shodu – schopnosti, které chyběly v best-effort internetových službách.

Historicky byl jeho vývoj motivován potřebou definovat jasnou evoluční cestu pro sítě GSM a UMTS do éry all-IP. Položil základy pro IMS, které se stalo univerzální platformou pro služby v reálném čase v sítích 4G a 5G. IMCN řešil omezení předchozích přístupů tím, že oddělil řízení služeb od podkladového transportu, což umožnilo rychlou inovaci a nasazení služeb bez nutnosti změn v rádiové přístupové síti. Stanovil základ pro transformaci sítě, která vedla k postupnému ukončování základních sítí s přepojováním okruhů a k plnému přijetí IP hlasu a multimédií jako standardu.

## Klíčové vlastnosti

- Přístupově agnostické poskytování služeb přes jakoukoli IP síť (např. GPRS, WLAN, LTE, 5G)
- Signalizace založená na SIP pro navazování, úpravu a ukončování relací
- Centralizovaná správa dat účastníků a autentizace prostřednictvím Home Subscriber Server (HSS)
- Oddělená servisní vrstva umožňující rychlé zavádění nových multimediálních aplikací
- Integrované Policy and Charging Control (PCC) pro autorizaci QoS a účtování
- Funkce pro propojení se staršími sítěmi s přepojováním okruhů (PSTN, PLMN)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios

---

📖 **Anglický originál a plná specifikace:** [IMCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/imcn/)
