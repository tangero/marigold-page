---
slug: "epdg"
url: "/mobilnisite/slovnik/epdg/"
type: "slovnik"
title: "EPDG – Evolved Packet Data Gateway"
date: 2025-01-01
abbr: "EPDG"
fullName: "Evolved Packet Data Gateway"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/epdg/"
summary: "Evolved Packet Data Gateway (EPDG) je síťový prvek jádrové sítě, který zajišťuje zabezpečené IP připojení mezi uživatelským zařízením (UE) a Evolved Packet Core (EPC) přes nedůvěryhodné přístupové sít"
---

EPDG je síťový prvek jádrové sítě, který zajišťuje zabezpečené IP připojení mezi uživatelským zařízením a jádrovou sítí přes nedůvěryhodný přístup mimo 3GPP, jako je Wi-Fi, tím, že ukončuje IPsec tunely.

## Popis

Evolved Packet Data Gateway (EPDG) je klíčová funkční entita v architektuře Evolved Packet Core (EPC) podle 3GPP, specificky definovaná pro umožnění bezpečné a důvěryhodné integrace nedůvěryhodných přístupových sítí mimo 3GPP. Jejím primárním úkolem je sloužit jako zabezpečená brána a koncový bod tunelů pro uživatelská zařízení (UE) připojující se přes IP přístup jako Wi-Fi, veřejné hotspoty nebo pevné širokopásmové připojení. EPDG navazuje šifrovaný [IPsec](/mobilnisite/slovnik/ipsec/) tunel (pomocí IKEv2) přímo s UE, čímž chrání veškerý provoz v uživatelské a řídicí rovině při průchodu nedůvěryhodným segmentem sítě. Tento tunel končí na EPDG, která následně směruje provoz do zabezpečené domény 3GPP EPC.

Architektonicky EPDG rozhraní s několika klíčovými uzly EPC. Komunikuje se 3GPP [AAA](/mobilnisite/slovnik/aaa/) serverem (a potenciálně 3GPP AAA proxy) pro autentizaci uživatele, autorizaci a načítání politik. Pro správu mobility a relace se připojuje k [PDN](/mobilnisite/slovnik/pdn/) Gateway ([PGW](/mobilnisite/slovnik/pgw/)) přes rozhraní S2b, které je založeno na [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) nebo Proxy Mobile IP ([PMIP](/mobilnisite/slovnik/pmip/)) protokolu. Toto spojení umožňuje EPDG fungovat jako kotva mobility, podobně jako role PGW pro 3GPP přístup, což zajišťuje zachování IP adresy UE při přechodu mezi typy přístupu. EPDG také komunikuje s [HSS](/mobilnisite/slovnik/hss/) pro získání profilů účastníka během procesu autentizace.

Z funkční perspektivy činnost EPDG začíná, když UE zjistí adresu EPDG (pomocí DNS nebo předkonfigurace) a zahájí výměnu IKEv2. EPDG autentizuje UE pomocí metod EAP-AKA nebo EAP-AKA', využívajíc přihlašovací údaje z USIM. Jakmile je IPsec tunel vytvořen, EPDG usnadňuje vytvoření PDN připojení signalizací směrem k PGW. Spravuje vazbu mezi informacemi o tunelu UE a odpovídajícím přenašečem v EPC. EPDG také zajišťuje vynucování politik, aplikuje pravidla QoS a účtovací politiky přijaté od PCRF přes rozhraní Gxb (pokud je použit PMIP) nebo vložené do signalizace PGW. Její role je zásadní pro Access Network Discovery and Selection Function (ANDSF) a později pro Non-3GPP Interworking Function (N3IWF) v 5G, protože poskytuje vzor pro integraci přístupu mimo 3GPP.

## K čemu slouží

EPDG byla představena v 3GPP Release 8 jako součást System Architecture Evolution (SAE) k řešení rostoucí potřeby bezproblémové integrace vysokovýkonných, všudypřítomných Wi-Fi sítí s buněčným paketovým jádrem. Před její standardizací bylo propojení mezi buněčnými sítěmi a WLAN často omezeno na jednoduché odlehčování provozu na IP vrstvě bez integrované autentizace, zabezpečení nebo podpory mobility. To vedlo k roztříštěnému uživatelskému zážitku, přerušeným aplikačním relacím během předávání spojení a nekonzistentním bezpečnostním politikám při přechodu mezi buněčnou sítí a Wi-Fi.

Vytvoření EPDG bylo motivováno snahou považovat některé přístupy mimo 3GPP za "důvěryhodná" rozšíření sítě operátora. Definováním standardizované, zabezpečené brány mohli operátoři využít široce dostupné Wi-Fi infrastruktury k odlehčování datového provozu při zachování stejné úrovně kontroly, zabezpečení a kontinuity služeb, jakou očekávají od 3GPP sítě. Vyřešilo to kritický problém vytvoření důvěryhodné IP cesty přes inherentně nedůvěryhodný přístupový médium, což zajišťuje ochranu uživatelského provozu před odposlechem nebo manipulací na veřejných Wi-Fi sítích.

EPDG dále umožnila nové obchodní modely a technické možnosti, jako je plynulá kontinuita hlasových hovorů mezi VoLTE a Wi-Fi (VoWiFi), která spoléhá na EPDG při poskytování zabezpečeného tunelu s řízenou QoS pro signalizaci IMS a média. Položila základy širšímu konceptu "přístupu mimo 3GPP", který se později vyvinul v Trusted Non-3GPP Gateway Function (TNGF) a Non-3GPP Interworking Function (N3IWF) v jádrové síti 5G, což demonstruje její zásadní význam v architekturách konvergentního přístupu.

## Klíčové vlastnosti

- Ukončuje IPsec (IKEv2) tunely s UE přes nedůvěryhodný IP přístup mimo 3GPP
- Rozhraní s 3GPP AAA serverem pro autentizaci založenou na EAP využívající přihlašovací údaje z USIM
- Připojuje se k PGW přes rozhraní S2b pomocí GTP nebo PMIP pro PDN připojení
- Funguje jako kotva mobility pro relace předávané z/na 3GPP přístup
- Vynucuje politiky QoS a účtování přijaté od PCRF
- Podporuje zjišťování pomocí DNS nebo mechanismů ANDSF

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 28.709** (Rel-19) — EPC NRM IRP Solution Set Definitions
- **TS 32.753** (Rel-9) — EPC NRM IRP CORBA Solution Set
- **TS 32.756** (Rel-11) — EPC NRM IRP Solution Set Definitions

---

📖 **Anglický originál a plná specifikace:** [EPDG na 3GPP Explorer](https://3gpp-explorer.com/glossary/epdg/)
