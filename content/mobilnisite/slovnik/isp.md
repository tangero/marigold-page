---
slug: "isp"
url: "/mobilnisite/slovnik/isp/"
type: "slovnik"
title: "ISP – Internet Service Provider"
date: 2025-01-01
abbr: "ISP"
fullName: "Internet Service Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isp/"
summary: "ISP (poskytovatel internetových služeb) je subjekt, který poskytuje přístup k internetu a souvisejícím službám, jako je webhosting nebo e-mail. V rámci 3GPP ISP spolupracují s operátory mobilních sítí"
---

ISP (poskytovatel internetových služeb) je subjekt, který poskytuje přístup k internetu a souvisejícím službám a spolupracuje s operátory mobilních sítí, aby ovlivňoval QoS, fakturaci a politiky propojení pro mobilní širokopásmové připojení.

## Popis

Internet Service Provider (ISP) je společnost nebo organizace, která nabízí služby pro přístup k internetu, jeho využívání nebo účast v něm. V kontextu 3GPP jsou ISP externí subjekty, s nimiž se operátoři mobilních sítí ([MNO](/mobilnisite/slovnik/mno/)) propojují, aby svým účastníkům poskytovali datové služby. Toto propojení umožňuje uživatelům přístup k internetovým aplikacím, webovým stránkám a cloudovým službám prostřednictvím jejich mobilních zařízení. Specifikace 3GPP řeší interakce s ISP v oblastech, jako je kvalita služby (QoS), řízení politik, účtování a zabezpečení, což zajišťuje, že mobilní sítě mohou hladce integrovat s širším internetovým ekosystémem.

Z architektonického hlediska se ISP připojují k sítím 3GPP prostřednictvím rozhraní jako Gi (ve 2G/3G) nebo SGi (v 4G/5G), která spojují bránu paketové datové sítě (PGW) nebo funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) s externími paketovými datovými sítěmi (PDN). Jádrová síť 3GPP prostřednictvím komponent, jako je funkce pravidel pro politiky a účtování (PCRF) nebo funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), vynucuje politiky, na které mohou mít vliv dohody s ISP, například omezování šířky pásma nebo zvýšení priority provozu pro konkrétní služby. Fakturační systémy také interagují s ISP, aby podporovaly scénáře jako sponzorovaná data, kdy ISP hradí náklady na datový provoz za určitý obsah.

Během provozu, když mobilní uživatel požaduje přístup k internetu, síť 3GPP naváže datovou relaci, která směruje provoz přes síť ISP. Mezi klíčové procesy patří přidělování IP adres (často prostřednictvím [DHCP](/mobilnisite/slovnik/dhcp/) nebo z fondu ISP), ověřování a autorizace (které může zahrnovat servery ISP) a správa provozu na základě smluv o úrovni služeb (SLA). Standardy 3GPP zajišťují, že tyto procesy jsou standardizovány, aby se zabránilo fragmentaci a podporovalo roamování. Například specifikace jako TS 23.060 ([GPRS](/mobilnisite/slovnik/gprs/)) a TS 23.401 (EPS) podrobně popisují, jak se spravují datové relace s externími sítěmi, včetně ISP, aby byl zajištěn konzistentní uživatelský zážitek napříč různými operátory a regiony.

## K čemu slouží

Účelem zohledňování ISP v rámci standardů 3GPP je definovat, jak se mobilní sítě propojují s externí internetovou infrastrukturou, a tím umožnit komplexní datové služby pro účastníky. ISP řeší problém rozšíření dosahu mobilní sítě mimo služby kontrolované operátorem na globální internet, což uživatelům umožňuje přístup k široké škále aplikací a obsahu. Toto propojení řeší omezení raných mobilních sítí, které byly často uzavřenými zahradami s omezeným externím přístupem, a to tím, že usnadňuje otevřené internetové připojení.

Historicky, jak se mobilní sítě vyvíjely z hlasově orientovaných systémů (např. GSM) na paketové datové služby (např. [GPRS](/mobilnisite/slovnik/gprs/) ve verzi 99), stala se potřeba standardizované interakce s ISP klíčovou. Bez jasných standardů by mohly vznikat problémy s interoperabilitou vedoucí ke špatné kvalitě služeb nebo složitým fakturačním dohodám. Specifikace 3GPP poskytují rámce pro diferenciaci QoS, kde se ISP a [MNO](/mobilnisite/slovnik/mno/) mohou dohodnout na prioritách provozu, a pro účtovací mechanismy, jako je objemové nebo časové účtování, které odrážejí partnerství s ISP.

Motivace pro integraci aspektů ISP do 3GPP zahrnuje podporu obchodních modelů, jako je zero-rating (kdy se konkrétní obsah nezapočítává do datového limitu), a zajištění bezpečného a efektivního směrování dat. S růstem mobilního širokopásmového připojení se ISP stali klíčovými partnery při poskytování over-the-top ([OTT](/mobilnisite/slovnik/ott/)) služeb a standardy 3GPP pomáhají tyto vztahy technicky řídit. To zajišťuje, že mobilní sítě zůstávají konkurenceschopné a flexibilní ve světě řízeném internetem, a vyvažují kontrolu operátora s otevřeným přístupem.

## Klíčové vlastnosti

- Poskytování přístupu k internetu a souvisejících služeb koncovým uživatelům
- Propojení se sítěmi 3GPP prostřednictvím rozhraní Gi/SGi pro směrování dat
- Ovlivňování politik QoS prostřednictvím SLA s mobilními operátory
- Podpora fakturačních modelů, jako jsou sponzorovaná data a zero-rating
- Integrace s funkcemi pro řízení politik v 3GPP (např. PCRF/PCF)
- Úloha při přidělování IP adres a ověřování pro datové relace

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.161** (Rel-12) — 3GPP-WLAN Interworking Requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [ISP na 3GPP Explorer](https://3gpp-explorer.com/glossary/isp/)
