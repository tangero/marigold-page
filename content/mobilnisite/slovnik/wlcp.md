---
slug: "wlcp"
url: "/mobilnisite/slovnik/wlcp/"
type: "slovnik"
title: "WLCP – Wireless LAN Control Plane Protocol"
date: 2025-01-01
abbr: "WLCP"
fullName: "Wireless LAN Control Plane Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wlcp/"
summary: "Řídicí protokol založený na GTP používaný mezi důvěryhodným přístupovým bránovým uzlem WLAN (TWAG) a uživatelským zařízením (UE) přes referenční bod SWw. Spravuje vytváření, modifikaci a ukončování př"
---

WLCP je řídicí protokol založený na GTP mezi důvěryhodným přístupovým bránovým uzlem WLAN (Trusted WLAN Access Gateway) a uživatelským zařízením (UE), který spravuje vytváření, modifikaci a ukončování připojení k PDN a přenosových kanálů (bearerů) přes důvěryhodný přístup WLAN.

## Popis

Protokol řídicí roviny pro bezdrátové lokální sítě (Wireless [LAN](/mobilnisite/slovnik/lan/) Control Plane Protocol, WLCP) je klíčový protokol definovaný pro architekturu důvěryhodného přístupu [WLAN](/mobilnisite/slovnik/wlan/) založenou na S2a ve specifikacích 3GPP. Působí mezi uživatelským zařízením ([WLAN-UE](/mobilnisite/slovnik/wlan-ue/)) a důvěryhodným přístupovým bránovým uzlem WLAN ([TWAG](/mobilnisite/slovnik/twag/)), což je síťová entita spojující důvěryhodnou síť WLAN s jádrem Evolved Packet Core (EPC). WLCP je koncepčně analogický k řídicí rovině protokolu [GTP](/mobilnisite/slovnik/gtp/) používaného přes rozhraní [S1-U](/mobilnisite/slovnik/s1-u/) a S5/S8, ale je přizpůsoben pro přístupovou vrstvu WLAN. Jako transportní protokol používá [UDP](/mobilnisite/slovnik/udp/).

Hlavní funkcí WLCP je spravovat připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)) pro uživatelské zařízení připojené přes důvěryhodnou síť WLAN. Přenáší signalizační zprávy pro procedury připojení k PDN: vytvoření připojení k PDN, modifikaci připojení k PDN a uvolnění připojení k PDN. Během vytváření připojení k PDN uživatelské zařízení použije WLCP k odeslání žádosti o připojení k PDN (PDN Connectivity Request) do uzlu TWAG. Uzel TWAG následně komunikuje s bránou PGW (přes GTP-C na S2a), aby připojení navázal, a přiřazenou IP adresu (adresy) a další parametry vrátí uživatelskému zařízení prostřednictvím odpovědi WLCP. WLCP také podporuje řízení na úrovni přenosového kanálu, což umožňuje vytváření, modifikaci a zrušení vyhrazených přenosových kanálů pro poskytnutí různých úrovní kvality služeb (QoS) pro různé datové toky přes přístup WLAN.

Zprávy WLCP jsou pro přenos přes IEEE 802.11 spojení mezi uživatelským zařízením a přístupovým bodem WLAN (který je součástí důvěryhodné sítě WLAN) zapouzdřeny v rámci EAP přes WLAN (konkrétně v rámci rámců EAPoL-Key). Toto zapouzdření zajišťuje, že signalizace je přenášena bezpečně přes spojení WLAN po dokončení počáteční autentizace založené na EAP. Protokol obsahuje nezbytné prvky, jako jsou TEID (identifikátory koncových bodů tunelu) pro identifikaci konkrétních připojení a přenosových kanálů, a podporuje procedury zpracování chyb a obnovy. Poskytnutím této standardizované řídicí roviny umožňuje WLCP integraci důvěryhodné sítě WLAN do EPC jako skutečné přístupové sítě s podporou QoS, která je rovnocenná přístupu 3GPP.

## K čemu slouží

WLCP byl vytvořen, aby vyřešil zásadní mezeru v počátečních architekturách propropojení 3GPP a WLAN: absenci standardizované řídicí roviny s podporou přenosových kanálů pro důvěryhodný přístup WLAN. Rané metody propropojení (např. přes ePDG pro nedůvěryhodný přístup) se zaměřovaly na tunelování IPsec a nepodporovaly nativní, efektivní diferenciaci QoS nebo bezproblémové procedury mobility, které byly standardem v přístupech 3GPP. Motivací bylo umožnit koncept „důvěryhodné sítě WLAN“, kde má operátor plnou kontrolu nad infrastrukturou WLAN, nabízet služby se stejnou spolehlivostí a kvalitou jako v celulárních sítích.

Problém, který řešil, bylo, jak rozšířit model PDN a přenosových kanálů EPC – klíčový pro architekturu QoS v LTE – přes ne-3GPP přístupový spoj IEEE 802.11. Bez WLCP mohla důvěryhodná síť WLAN poskytovat pouze jednoduché IP připojení bez možnosti vytvářet vyhrazené přenosové kanály pro služby se zaručenou přenosovou rychlostí nebo efektivně spravovat více připojení k PDN (např. pro IMS a internet současně). WLCP poskytl potřebný signalizační protokol, který přinesl bohaté možnosti připojení a řízení politik EPC přímo k uživatelskému zařízení připojenému přes WLAN.

Zavedený ve vydání 12 jako součást funkce důvěryhodného přístupu WLAN založeného na S2a (TWAN), byl WLCP klíčovým prvkem umožňujícím hlubokou síťovou integraci. Umožnil operátorům nasazovat operátorské Wi-Fi, které mohlo nejen odlehčovat datový provoz, ale také doručovat hlas přes Wi-Fi (VoWiFi) s patřičnou QoS, podporovat bezproblémovou kontinuitu relace a být spravováno jako nedílná část mobilní sítě. Tento protokol položil základy pro pozdější konvergenci typů přístupu ve společném jádru 5G.

## Klíčové vlastnosti

- Spravuje životní cyklus připojení k PDN (vytvoření, modifikace, uvolnění) přes důvěryhodnou síť WLAN
- Podporuje operace s vyhrazenými přenosovými kanály pro správu toků QoS
- Používá UDP transport a je zapouzdřen v rámcích EAPoL-Key přes spojení WLAN
- Vyměňuje si zprávy podobné GTP-C mezi uživatelským zařízením a uzlem TWAG přes rozhraní SWw
- Přenáší parametry jako APN, typ PDN, adresa PDN a QoS přenosového kanálu EPS
- Umožňuje uzlu TWAG fungovat jako koncový bod založený na GTP pro řídicí rovinu uživatelského zařízení

## Související pojmy

- [TWAG – Trusted WLAN Access Gateway](/mobilnisite/slovnik/twag/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)
- [GTP-C – GPRS Tunnelling Protocol for Control Plane](/mobilnisite/slovnik/gtp-c/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN

---

📖 **Anglický originál a plná specifikace:** [WLCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/wlcp/)
