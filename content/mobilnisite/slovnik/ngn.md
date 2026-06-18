---
slug: "ngn"
url: "/mobilnisite/slovnik/ngn/"
type: "slovnik"
title: "NGN – Next Generation Networks"
date: 2025-01-01
abbr: "NGN"
fullName: "Next Generation Networks"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ngn/"
summary: "NGN je široký architektonický koncept pro migraci telekomunikačních sítí z přepojování okruhů na paketovou (IP) infrastrukturu. V 3GPP označuje vývoj jádrové sítě pro podporu multimediálních služeb př"
---

NGN je architektonický koncept 3GPP pro vývoj jádrových sítí směrem k paketově orientované, IP infrastruktuře pro podporu multimediálních služeb a umožnění konvergence pevných a mobilních sítí.

## Popis

V rámci 3GPP představují sítě příští generace (NGN) zastřešující architektonický vývoj od tradičních, izolovaných telekomunikačních sítí ([PSTN](/mobilnisite/slovnik/pstn/), starší mobilní jádro) směrem k jednotné, paketové infrastruktuře schopné poskytovat širokou škálu multimediálních služeb. Klíčovou technickou realizací NGN v 3GPP je IP Multimedia Subsystem (IMS), definovaný jako podsystém v rámci paketově orientované domény. IMS poskytuje standardizovanou platformu pro poskytování služeb, která pro řízení relací používá protokol Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a běží na IP transportu, čímž odděluje služební logiku od přístupové technologie.

NGN/IMS funguje na principu vrstvené architektury. Transportní vrstva poskytuje IP konektivitu, řídicí vrstva (obsahující [CSCF](/mobilnisite/slovnik/cscf/) - Call Session Control Functions) zpracovává signalizaci SIP pro navázání, změnu a ukončení relace a aplikační vrstva hostí vlastní služební logiku (Application Servers). Mezi klíčové komponenty patří [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) pro uživatelská data a různé funkce hraničního řízení ([P-CSCF](/mobilnisite/slovnik/p-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/), [S-CSCF](/mobilnisite/slovnik/s-cscf/)), které spravují přístup do sítě a směrování. Toto uspořádání umožňuje poskytování hlasových služeb (VoIP), videa, zpráv a dalších pokročilých komunikačních služeb s odpovídající kvalitou služeb (QoS) a řízením účtování, a to nezávisle na tom, zda je uživatel připojen přes GSM, [WCDMA](/mobilnisite/slovnik/wcdma/), LTE nebo dokonce pevný širokopásmový přístup.

Jeho role se s pozdějšími vydáními 3GPP rozšířila o celý Evolved Packet Core (EPC) pro LTE, což je čistě IP jádrová síť pro 4G. Zde jsou principy NGN plně realizovány prostřednictvím ploché, plně IP architektury podporující vysokorychlostní data a hlas přes IMS (VoLTE). Rámec NGN zajišťuje kontinuitu služeb, interoperabilitu se staršími systémy a migrační cestu pro operátory. Je základem pro Fixed-Mobile Convergence (FMC), což umožňuje bezproblémové služby napříč různými přístupovými sítěmi, a připravil půdu pro plně cloud-nativní, službami orientovanou architekturu 5G Core (5GC).

## K čemu slouží

NGN bylo koncipováno pro řešení kritických omezení starších telekomunikačních sítí, které byly postaveny na vyhrazené technologii přepojování okruhů pro každou službu zvlášť (např. jedna síť pro hlas, jiná pro data). Tento model byl neefektivní, nákladný na škálování a nepružný pro zavádění nových multimediálních služeb. Hlavním problémem byla neschopnost sloučit služby na jedinou efektivní infrastrukturu a vysoké provozní náklady na údržbu více paralelních sítí.

Motivací pro NGN, a konkrétně pro IMS v rámci 3GPP, bylo využít všudypřítomnost a efektivitu internetového protokolu (IP) k vytvoření budoucím potřebám odolné služební platformy. Cílem bylo umožnit bohaté, reálné multimediální komunikace (nad rámec prostého hlasu) a odstranit bariéry mezi pevnými, mobilními a internetovými službami. Tím se řešila potřeba operátorů konkurovat poskytovatelům OTT (Over-the-Top) služeb a vytvářet nové zdroje příjmů z balíčků komunikačních služeb.

Historicky, počínaje 3GPP Release 5 (kde bylo IMS poprvé specifikováno), poskytlo NGN strategickou odpověď na 'all-IP' transformaci. Vyřešilo problém, jak doručovat služby hlasu a zasílání zpráv na úrovni operátora přes paketové sítě s požadovanou spolehlivostí, zabezpečením a možnostmi účtování, které chyběly službám typu best-effort na internetu. Standardizací IMS zajistilo 3GPP globální interoperabilitu pro multimediální služby, usnadnilo případné vyřazení sítí s přepojováním okruhů a umožnilo úspěšný přechod na 4G LTE a 5G, kde jsou všechny služby, včetně hlasu, doručovány jako data přes IP.

## Klíčové vlastnosti

- Paketově orientovaná, plně IP architektura jádrové sítě
- Řízení služeb založené na IMS a protokolu Session Initiation Protocol (SIP)
- Oddělení služební vrstvy od technologie přístupové sítě
- Podpora multimediálních služeb (hlas, video, zprávy) s QoS
- Umožňuje Fixed-Mobile Convergence (FMC) a interoperabilitu služeb
- Standardizovaná rozhraní pro integraci služeb třetích stran a roaming

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 21.202** (Rel-19) — Common IMS Specifications List
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.408** (Rel-7) — TIP/TIR Services Protocol Specification
- **TS 24.410** (Rel-8) — Protocol Description of HOLD Services
- … a dalších 23 specifikací

---

📖 **Anglický originál a plná specifikace:** [NGN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngn/)
