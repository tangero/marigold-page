---
slug: "pdg"
url: "/mobilnisite/slovnik/pdg/"
type: "slovnik"
title: "PDG – Packet Data Gateway"
date: 2025-01-01
abbr: "PDG"
fullName: "Packet Data Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdg/"
summary: "Funkce brány v síti jádra 3GPP systémů, která poskytuje zabezpečené IP připojení mezi uživatelským zařízením (UE) a externími sítěmi s paketovými daty (PDN), jako je internet nebo podnikové intranety."
---

PDG je brána v síti jádra v systémech 3GPP, která zajišťuje zabezpečené IP spojení mezi mobilním uživatelským zařízením (User Equipment) a externími sítěmi s paketovými daty, jako je internet.

## Popis

Packet Data Gateway (PDG) je kritický síťový prvek v rámci architektury 3GPP, konkrétně definovaný pro doménu sítě jádra. Funguje jako přístupově agnostická brána, která zajišťuje připojení mezi zařízením uživatele (User Equipment, UE) a externími IP sítěmi, známými jako Packet Data Networks ([PDN](/mobilnisite/slovnik/pdn/)). PDG představuje centrální kotvící bod pro IP relaci uživatele. Plní několik klíčových rolí: vytváří a spravuje [IPsec](/mobilnisite/slovnik/ipsec/) tunely (pomocí IKEv2) s UE za účelem zajištění zabezpečeného přenosu dat, slouží jako bod pro vymáhání pravidel pro aplikaci kvality služeb (QoS) a tarifování a provádí překlad síťových adres a přidělování IP adres pro UE.

Architektonicky se PDG nachází v domovské síti účastníka. Komunikuje se serverem 3GPP [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting) pro ověření a autorizaci uživatele. Zároveň se připojuje k Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)) pro účely fakturace. Provoz PDG zahrnuje několik protokolů. Pro komunikaci se serverem 3GPP AAA za účelem autentizace používá referenční bod Wm. Datový provoz uživatele protéká přes PDG přes zřízený IPsec tunel (přes referenční bod Wn z přístupové sítě) a je pak směrován do externí PDN (přes referenční bod Wi). PDG také podporuje funkčnost podobnou Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) pro specifické typy přístupu, čímž slouží jako topologický kotvící bod pro IP adresu uživatele.

V širším vývoji sítí byl PDG základním prvkem pro umožnění zabezpečeného přístupu z netechnologií 3GPP (jako je [WLAN](/mobilnisite/slovnik/wlan/)) ke službám sítě jádra 3GPP, což je koncept formalizovaný jako Interworking WLAN ([I-WLAN](/mobilnisite/slovnik/i-wlan/)). Zajišťoval, že uživatelé mohli zabezpečeně přistupovat k operátorským službám z jakékoli IP přístupové sítě, a to s konzistentní autentizací, autorizací a aplikací politik. Konstrukční principy PDG – zabezpečené tunelování, vymáhání politik a kotvení relace – byly následně rozvinuty a začleněny do pokročilejších bran, jako je evolved Packet Data Gateway (ePDG) pro nedůvěryhodný přístup netechnologií 3GPP v EPS a Non-3GPP InterWorking Function (N3IWF) v systémech 5G.

## K čemu slouží

PDG byl vytvořen, aby vyřešil problém zabezpečené a bezproblémové integrace přístupových sítí netechnologií 3GPP (primárně bezdrátových lokálních sítí – WLAN) s mobilní sítí jádra 3GPP. Na počátku 21. století se technologie WLAN rozšířila, ale postrádala integrované bezpečnostní, správu mobility a fakturační rámce buněčných sítí. Standardizační organizace 3GPP potřebovala způsob, jak umožnit mobilním operátorům rozšířit své služby přes WLAN a vytvořit tak jednotný uživatelský zážitek.

PDG tento problém řešil tím, že poskytl standardizovanou bránu v síti jádra operátora, která mohla ukončovat zabezpečené tunely ze zařízení v nedůvěryhodných IP sítích. Tím bylo vyřešeno několik klíčových problémů: poskytla silné ověření pomocí SIM přihlašovacích údajů (přes AAA server), zašifrovala veškerý uživatelský provoz ze zařízení do sítě operátora a umožnila operátorovi aplikovat stejné služební politiky a fakturační mechanismy jako u buněčných dat. To umožnilo nové obchodní modely, jako je 'Operátorský WiFi', a byl to klíčový krok ke konvergenci buněčných a IP sítí. Položilo to základy pro budoucí vizi poskytování služeb nezávislých na přístupu, což je základním kamenem architektur 4G a 5G.

## Klíčové vlastnosti

- Ukončuje IPsec zabezpečená spojení (IKEv2, ESP) s uživatelským zařízením (UE)
- Slouží jako topologický kotvící bod pro IP adresu UE
- Vynucuje QoS a tarifní politiky na základě uživatelského předplatného a služby
- Komunikuje s 3GPP AAA pro ověření a autorizaci
- Zajišťuje připojení mezi UE a externími sítěmi s paketovými daty (PDN)
- Podporuje propojení mezi přístupovými sítěmi 3GPP a netechnologiemi 3GPP (např. WLAN)

## Související pojmy

- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS
- **TS 28.601** (Rel-12) — Telecom management; CN and non-3GPP access NRM IRP Requirements
- **TS 28.602** (Rel-12) — CN & non-3GPP NRM IRP Information Service
- **TS 29.161** (Rel-12) — 3GPP-WLAN Interworking Requirements
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.252** (Rel-12) — 3GPP WLAN Interworking Charging
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDG na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdg/)
