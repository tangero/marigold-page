---
slug: "uni"
url: "/mobilnisite/slovnik/uni/"
type: "slovnik"
title: "UNI – User to Network Interface"
date: 2025-01-01
abbr: "UNI"
fullName: "User to Network Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uni/"
summary: "UNI je demarkační bod nebo referenční bod mezi uživatelským zařízením (nebo zařízením v prostorách zákazníka) a veřejnou telekomunikační sítí. Definuje technickou, provozní a často i smluvní hranici a"
---

UNI je demarkační bod mezi uživatelským zařízením a veřejnou telekomunikační sítí, který definuje technickou, provozní a smluvní hranici.

## Popis

Rozhraní mezi uživatelem a sítí (UNI) je základním konceptem v telekomunikacích a datových sítích, který definuje hranici mezi doménou uživatele a doménou sítě poskytovatele služeb. Nejde o jediný fyzický konektor, ale o logický a fyzický referenční bod zahrnující všechny specifikace potřebné pro interoperabilitu. Technicky UNI definuje protokoly vrstev 1, 2 a 3 pro připojení. Na fyzické vrstvě (vrstva 1) specifikuje elektrické, optické a mechanické charakteristiky, jako je typ konektoru, řádkové kódování a rámcování (např. T1/E1, Ethernet, [DSL](/mobilnisite/slovnik/dsl/) nebo optická rozhraní). Na vrstvě datového spoje (vrstva 2) definuje rámcovací protokol, jako je Ethernet [MAC](/mobilnisite/slovnik/mac/), [HDLC](/mobilnisite/slovnik/hdlc/), [PPP](/mobilnisite/slovnik/ppp/) nebo [ATM](/mobilnisite/slovnik/atm/). Na síťové vrstvě (vrstva 3) může specifikovat pravidla IP adresování, směrovací protokoly (jako BGP pro IP [VPN](/mobilnisite/slovnik/vpn/)) nebo signalizační protokoly. V kontextech 3GPP se koncept UNI objevuje v různých formách. Například v kontextu konvergence pevných a mobilních sítí nebo širokopásmového přístupu by to mohlo být rozhraní mezi domácím gatewayem a sítí IP Multimedia Subsystem (IMS). Vztahuje se také k rozhraní mezi uživatelským zařízením (UE) a jádrem sítě pro přenos řídicí a uživatelské roviny. UNI je klíčové pro smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), protože je to bod, ve kterém jsou měřeny a garantovány poskytovatelem výkonnostní metriky jako šířka pásma, latence a dostupnost. Jeho definice zajišťuje, že zařízení v prostorách zákazníka od libovolného výrobce se může bezproblémově připojit k síti poskytovatele služeb.

## K čemu slouží

UNI existuje za účelem vytvoření jasné, standardizované demarkace mezi odpovědností zákazníka a odpovědností síťového operátora. Tím řeší klíčové problémy izolace závad, interoperability a definice služeb. Bez standardizovaného UNI by vyžadovalo každé zákaznické zařízení vlastní integraci se sítí, což by brzdilo inovace a zvyšovalo náklady. Historicky, jak se sítě vyvíjely od jednoduchých hlasových okruhů ke komplexním datovým a multimediálním službám, stala se potřeba dobře definovaného rozhraní prvořadou. UNI umožňuje síťovým operátorům nabízet dobře definované služby (např. službu Ethernet Line nebo IP [VPN](/mobilnisite/slovnik/vpn/)) s konkrétními technickými parametry, a zároveň dává zákazníkům svobodu volby a konfigurace jejich vlastního zařízení za tímto rozhraním. Usnadňuje prostředí s více dodavateli a je nezbytné pro wholesale scénáře, kdy jeden poskytovatel služeb nakupuje přístup od druhého. V mobilních sítích, zatímco rozhraní Uu je specifickým typem UNI, se tento termín často používá šířeji pro drátová nebo spravovaná přístupová připojení, která vedou do mobilního jádra a podporují služby přenosu nebo propojení.

## Klíčové vlastnosti

- Definuje demarkační bod mezi doménou uživatele a doménou síťového operátora
- Specifikuje protokoly fyzické vrstvy, vrstvy datového spoje a síťové vrstvy pro interoperabilitu
- Slouží jako referenční bod pro měření parametrů smlouvy o úrovni služeb (SLA)
- Umožňuje kompatibilitu zařízení od více dodavatelů
- Podporuje různé přístupové technologie (např. Ethernet, TDM, ATM, DSL)
- Usnadňuje izolaci závad a vymezení odpovědností za správu

## Související pojmy

- [NNI – Network to Network Interfaces](/mobilnisite/slovnik/nni/)
- [SLA – Spending-Limit-Answer](/mobilnisite/slovnik/sla/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TR 26.930** (Rel-19) — WebRTC Enhancements for Immersive RTC over 5G
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [UNI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uni/)
