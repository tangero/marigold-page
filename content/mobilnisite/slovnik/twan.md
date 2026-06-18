---
slug: "twan"
url: "/mobilnisite/slovnik/twan/"
type: "slovnik"
title: "TWAN – Trusted WLAN Access Network"
date: 2025-01-01
abbr: "TWAN"
fullName: "Trusted WLAN Access Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/twan/"
summary: "Trusted WLAN Access Network (TWAN) je architektonický koncept definovaný 3GPP, který představuje řízenou WLAN operátora bezpečně integrovanou s mobilní jádrovou sítí. Zahrnuje funkční uzly jako TWAG a"
---

TWAN je architektonický koncept 3GPP pro řízenou WLAN operátora, která je bezpečně integrována s mobilní jádrovou sítí za účelem poskytování bezproblémových služeb 3GPP s podporou autentizace, řízení politik a mobility.

## Popis

Trusted [WLAN](/mobilnisite/slovnik/wlan/) Access Network (TWAN) není jediné zařízení, ale logický architektonický konstrukt definovaný 3GPP. Představuje bezdrátovou lokální síť (WLAN), která je považována za "důvěryhodnou" jádrovou sítí operátora 3GPP. Tato důvěra je založena na tom, že TWAN implementuje specifická rozhraní a funkce definované 3GPP, což umožňuje její integraci jako bezproblémové, bezpečné a politikami řízené přístupové sítě na stejné úrovni jako technologie 3GPP rádiového přístupu, například LTE. TWAN zahrnuje soubor síťových funkcí, které společně poskytují důvěryhodný přístup přes WLAN k Evolved Packet Core (EPC) a v pozdějších vydáních k 5G Core (5GC).

Architektura TWAN je postavena kolem tří klíčových funkčních entit: Trusted WLAN Access Gateway ([TWAG](/mobilnisite/slovnik/twag/)), Trusted WLAN [AAA](/mobilnisite/slovnik/aaa/) Proxy ([TWAP](/mobilnisite/slovnik/twap/)) a podkladových WLAN přístupových bodů ([AP](/mobilnisite/slovnik/ap/)). TWAG zpracovává uživatelskou rovinu a vytváří tunely [GTP](/mobilnisite/slovnik/gtp/) nebo [PMIP](/mobilnisite/slovnik/pmip/) přes rozhraní S2a k Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC. TWAP zpracovává řídicí rovinu a funguje jako proxy pro signalizaci Authentication, Authorization, and Accounting (AAA) mezi UE/WLAN a 3GPP AAA Server/Proxy. WLAN AP poskytují skutečné rádiové spojení. Tyto funkce mohou být umístěny v jednom fyzickém uzlu nebo distribuovány. TWAN se připojuje k EPC přes dvě hlavní referenční body: STa (mezi TWAP a 3GPP AAA Server pro AAA) a S2a (mezi TWAG a PGW pro uživatelská data).

Z procesního hlediska, když se UE připojí k TWAN, podstoupí autentizaci založenou na EAP vůči infrastruktuře 3GPP AAA pomocí přihlašovacích údajů ze své USIM karty. TWAP tento proces usnadňuje. Po úspěšné autentizaci TWAG vytvoří pro UE datový přenos. PGW přidělí IP adresu a veškerý uživatelský provoz je směrován přes zabezpečený tunel mezi TWAG a PGW. Tato architektura umožňuje jádrové síti aplikovat konzistentní pravidla řízení politik a účtování (PCC), spravovaná funkcí Policy and Charging Rules Function (PCRF), na provoz z UE připojené přes TWAN. Také umožňuje podporu mobility, například předávání IP relací mezi TWAN a sítí 3GPP přístupu (např. LTE) bez změny IP adresy, protože PGW slouží jako společná kotva.

V kontextu 5G se koncept TWAN vyvinul. Funkce byly přehodnoceny pro propojení se sítí 5G Core přes Non-3GPP InterWorking Function (N3IWF) pro nedůvěryhodný přístup nebo přímoji přes Trusted Non-3GPP Gateway Function (TNGF), která přebírá role TWAG a TWAP pro důvěryhodný přístup. Tento vývoj zachovává princip důvěryhodné ne-3GPP přístupové sítě, ale sladí ji s architekturou založenou na službách a protokoly 5G. Během svého životního cyklu byl TWAN klíčový pro umožnění operátorům nasadit Wi-Fi úrovně operátora jako nedílnou součást jejich strategie heterogenních sítí.

## K čemu slouží

TWAN byl vytvořen k formální definici standardizované architektury pro integraci řízených Wi-Fi sítí operátora nebo partnera do ekosystému mobilních sítí 3GPP jako důvěryhodného typu přístupu. Před jeho zavedením byla Wi-Fi typicky neřízená, best-effort přístupová síť, což vedlo k roztříštěnému uživatelskému zážitku, samostatným přihlášením a žádné integraci s mobilními službami jako IMS nebo bezproblémovou mobilitou. Hlavním problémem byl nedostatek standardizovaného modelu založeného na síti, který by mohl poskytnout zabezpečení, autentizaci, řízení politik a kontinuitu služeb ekvivalentní přístupu přes buněčné sítě.

Vývoj TWAN ve vydání 11 byl strategickou reakcí na explozivní růst Wi-Fi a potřebu mobilních operátorů efektivně odlehčovat datový provoz při zachování kontroly nad uživatelským zážitkem a kvalitou služeb. Řešil omezení dřívějšího modelu "nedůvěryhodného ne-3GPP přístupu" (který vyžadoval klientem iniciované IPsec tunely), který byl složitý pro implementaci v zařízení a nepodporoval efektivní mobilitu založenou na síti ani hlubokou integraci politik. Model TWAN přesunul složitost do sítě, což umožnilo jednodušší UE a umožnilo operátorovi zacházet s Wi-Fi jako s prvotřídní přístupovou technologií.

Stanovením TWAN jako důvěryhodné entity 3GPP vyřešilo několik klíčových problémů: umožnilo bezproblémovou autentizaci pomocí přihlašovacích údajů 3GPP (na bázi SIM), umožnilo jádrové síti vynucovat konzistentní kvalitu služeb a účtovací politiky napříč buněčnými sítěmi a Wi-Fi a poskytlo základ pro skutečnou mobilitu přístupové sítě. To bylo zásadní pro umožnění služeb jako Voice over Wi-Fi (VoWiFi) s IMS a pro realizaci skutečné Fixed-Mobile Convergence (FMC), kde jsou služby uživatele nezávislé na podkladové přístupové technologii. Architektura TWAN poskytla vzor pro hlubokou integraci WLAN, která se později vyvinula v základní součást závazku 5G podporovat heterogenní přístup.

## Klíčové vlastnosti

- Definuje standardizovanou architekturu pro integraci důvěryhodné WLAN operátora s jádrovými sítěmi 3GPP
- Zahrnuje klíčové funkce: TWAG (brána uživatelské roviny), TWAP (AAA proxy) a WLAN přístupové body
- Podporuje autentizaci EAP-AKA/AKA' pomocí přihlašovacích údajů 3GPP (USIM) pro zabezpečený přístup
- Poskytuje rozhraní (S2a, STa) pro připojení k PGW a AAA infrastruktuře EPC
- Umožňuje mobilitu založenou na síti a kontinuitu relací mezi WLAN a 3GPP přístupem
- Umožňuje aplikaci pravidel 3GPP Policy and Charging Control (PCC) na provoz přes WLAN

## Související pojmy

- [TWAG – Trusted WLAN Access Gateway](/mobilnisite/slovnik/twag/)
- [TWAP – Trusted WLAN AAA Proxy](/mobilnisite/slovnik/twap/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [TWAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/twan/)
