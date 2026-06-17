---
slug: "eap"
url: "/mobilnisite/slovnik/eap/"
type: "slovnik"
title: "EAP – Extensible Authentication Protocol"
date: 2026-01-01
abbr: "EAP"
fullName: "Extensible Authentication Protocol"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eap/"
summary: "Extensible Authentication Protocol (EAP) je flexibilní rámec definovaný IETF pro autentizaci přístupu k síti, který je široce přijat organizací 3GPP. Podporuje více autentizačních metod (EAP metod) a"
---

EAP (Extensible Authentication Protocol) je flexibilní IETF rámec pro autentizaci přístupu k síti, který podporuje více metod a je klíčovým prvkem pro zabezpečený přístup k sítím 3G, 4G a 5G, zejména pro přístup přes ne-3GPP sítě.

## Popis

Extensible Authentication Protocol (EAP) je autentizační rámec, původně definovaný v [IETF](/mobilnisite/slovnik/ietf/) RFC 3748 a široce začleněný do standardů 3GPP, který poskytuje flexibilní mechanismus pro zabezpečenou autentizaci klienta (nebo UE) vůči síti. Funguje jako sekvenční protokol typu požadavek-odpověď přenášený v rámci transportního protokolu nižší vrstvy, jako je PPP, [IEEE](/mobilnisite/slovnik/ieee/) 802.1X (EAP over [LAN](/mobilnisite/slovnik/lan/) - EAPOL), nebo přímo v rámci signalizace specifické pro 3GPP, jako je [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) nebo DIAMETER. Základní architektura zahrnuje tři entity: EAP peer (klient žádající o přístup), EAP autentizátor (přístupový bod sítě, např. WLAN [AP](/mobilnisite/slovnik/ap/) nebo 3GPP [AAA](/mobilnisite/slovnik/aaa/) Proxy) a EAP server (backendový autentizační server, často AAA server jako [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/) nebo samostatný RADIUS server).

EAP funguje tak, že umožňuje autentizátoru jednat jako průchozí prvek. Autentizátor přijme od peera zprávu EAP-Start nebo EAP-Response/Identity, zapouzdří ji a přepošle EAP serveru. EAP server poté vybere vhodnou EAP metodu (např. EAP-AKA, EAP-AKA', EAP-TLS, EAP-SIM) na základě politiky a identity peera. Následný EAP dialog – série specifických požadavků a odpovědí dané metody – probíhá přímo mezi peerem a serverem, transparentně přeposílán autentizátorem. Tento dialog provádí vzájemnou autentizaci a odvozuje relakční klíče. Po úspěšné autentizaci odešle EAP server autentizátoru zprávu EAP-Success spolu s odvozeným hlavním relakčním klíčem (MSK) a rozšířeným hlavním relakčním klíčem (EMSK). Autentizátor používá MSK k odvození potřebných šifrovacích klíčů linkové vrstvy.

V sítích 3GPP je role EAP klíčová, zejména pro integraci ne-3GPP přístupových sítí (jako WLAN, Wi-Fi a pevný přístup) s 3GPP jádrem. Tvoří základ pro autentizaci při důvěryhodném a nedůvěryhodném ne-3GPP přístupu k EPS a 5GC, jak je definováno v rozhraních S2a, S2b a N3IWF. Uvnitř jádra často funkce Authentication Server Function (AUSF) v 5GC funguje jako EAP server a komunikuje s UDM pro ověření přihlašovacích údajů. EAP metody jako EAP-AKA a EAP-AKA' se používají pro autentizaci využívající přihlašovací údaje USIM, což poskytuje bezproblémovou mobilitu a konzistentní zabezpečení napříč různými přístupovými technologiemi. EAP tedy poskytuje jednotnou, rozšiřitelnou bezpečnostní vrstvu nezávislou na podkladové spojové technologii.

## K čemu slouží

EAP byl vytvořen k vyřešení problému existence více nekompatibilních autentizačních mechanismů pro různé technologie přístupu k síti. Před jeho přijetím měla každá technologie linkové vrstvy (např. vytáčené PPP, kabelový Ethernet, bezdrátová LAN) často svůj vlastní proprietární nebo omezený autentizační režim. Tato roztříštěnost bránila bezproblémovému roamingu a důslednému prosazování bezpečnostních politik napříč heterogenními sítěmi. IETF vyvinulo EAP jako obecný rámec pro oddělení autentizační metody od konkrétních fyzických a linkových protokolů, což umožnilo, aby jediný flexibilní autentizační proces běžel přes jakoukoli linkovou vrstvu schopnou přenášet EAP rámce.

3GPP přijalo EAP k řešení kritické potřeby zabezpečených, jednotných autentizačních mechanismů, zejména pro spolupráci s ne-3GPP přístupovými sítěmi (např. WLAN hotspoty). Když mobilní operátoři začali nabízet bezproblémový přístup napříč mobilními a Wi-Fi sítěmi, potřebovali autentizační metodu, která by mohla využít silné přihlašovací údaje uložené v kartě USIM/SIM. EAP-AKA (a později EAP-AKA') byl vyvinut v rámci spolupráce IETF/3GPP, aby tuto potřebu naplnil, a umožňuje UE autentizovat se v ne-3GPP síti pomocí své 3GPP předplatitelské identity a klíčů. Tím byl vyřešen problém zabezpečeného opakovaného použití přihlašovacích údajů a byl poskytnut standardizovaný, rozšiřitelný základ pro budoucí autentizační metody, podporující vývoj směrem ke konvergovanému přístupu v 4G a 5G.

## Klíčové vlastnosti

- Rámec podporující více autentizačních metod (EAP metod)
- Nezávislost na transportu, funkční přes PPP, IEEE 802, RADIUS, DIAMETER a 3GPP NAS
- Podporuje vzájemnou autentizaci mezi peerem a serverem
- Odvozuje klíčový materiál (MSK, EMSK) pro následnou zabezpečenou komunikaci
- Kritický pro spolupráci přístupu 3GPP a ne-3GPP sítí (např. WLAN, pevné sítě)
- Umožňuje autentizaci založenou na USIM prostřednictvím metod EAP-AKA/EAP-AKA'

## Související pojmy

- [AAA – Authentication, Authorization, and Accounting](/mobilnisite/slovnik/aaa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 28.204** (Rel-18) — Charging management
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application
- **TR 31.826** (Rel-18) — Technical Report
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [EAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/eap/)
