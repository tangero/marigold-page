---
slug: "dhcp"
url: "/mobilnisite/slovnik/dhcp/"
type: "slovnik"
title: "DHCP – Dynamic Host Configuration Protocol"
date: 2026-01-01
abbr: "DHCP"
fullName: "Dynamic Host Configuration Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dhcp/"
summary: "DHCP je síťový správní protokol používaný k dynamickému přidělování IP adres a dalších konfiguračních parametrů sítě zařízením. V sítích 3GPP automatizuje přidělování IP adres pro uživatelská zařízení"
---

DHCP je síťový správní protokol používaný v sítích 3GPP k dynamickému přidělování IP adres a dalších konfiguračních parametrů uživatelským zařízením a síťovým funkcím za účelem efektivního řízení zdrojů a zajištění konektivity.

## Popis

Dynamic Host Configuration Protocol (DHCP) je protokol typu klient-server standardizovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 2131) a přijatý v rámci architektur 3GPP k automatizaci přiřazování IP konfigurace síťovým koncovým bodům. V systému 3GPP DHCP funguje primárně v paketově orientované doméně, často za podpory síťových prvků, jako je Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPS nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC. Primární úlohou protokolu je poskytnout UE při připevnění k síti nebo během vytváření [PDN](/mobilnisite/slovnik/pdn/) spojení IP adresu, masku podsítě, výchozí bránu a adresy [DNS](/mobilnisite/slovnik/dns/) serverů, čímž odpadá potřeba manuální konfigurace.

Protokol funguje prostřednictvím čtyřstupňové výměny zpráv známé jako DORA: Discover, Offer, Request a Acknowledge. Když UE zahájí PDN spojení, jeho DHCP klient rozesílá broadcastovou zprávu DHCPDISCOVER. DHCP server, který může být umístěn společně s bránou nebo být samostatnou síťovou entitou, odpoví zprávou DHCPOFFER obsahující navrženou IP adresu a konfiguraci. UE poté odešle DHCPREQUEST, aby formálně požádalo o nabízené parametry, a server potvrdí zprávou DHCPACK, čímž se zapůjčení dokončí. Toto zapůjčení má definovanou dobu platnosti, po jejímž uplynutí může být adresa odebrána a přidělena znovu, což je řízeno procesy obnovy a převazování.

Mezi klíčové architektonické komponenty patří DHCP klient (nacházející se v UE), DHCP server a volitelně DHCP přenosové agenty. Přenosové agenty jsou klíčové pro rozsáhlá nasazení 3GPP, protože přeposílají DHCP zprávy mezi klienty na různých IP podsítích (např. mobilní přístupová síť) a centralizovanými servery. Protokol podporuje různé typy zpráv pro různé operace, včetně obnovení zapůjčení (DHCPREQUEST), uvolnění (DHCPRELEASE) a informačních dotazů (DHCPINFORM). V 3GPP je DHCP nedílnou součástí správy IP adres (IPAM) a používá se nejen pro počáteční konfiguraci UE, ale také pro poskytování parametrů ve scénářích jako je propojení s bezdrátovou lokální sítí ([WLAN](/mobilnisite/slovnik/wlan/)) a konvergence pevných a mobilních sítí.

Nad rámec základního přidělování IP adres může DHCP v sítích 3GPP doručovat širokou škálu konfiguračních voleb definovaných v RFC, jako jsou adresy [SIP](/mobilnisite/slovnik/sip/) serverů, informace pro zjištění P-CSCF pro IMS a specifické směrovací politiky. Jeho integrace je specifikována v řadě technických specifikací 3GPP, které detailně popisují jeho použití v rámci GTP rozhraní S5/S8, procedur aktivace Packet Data Protocol (PDP) kontextu a servisních rozhraní v 5GC. Bezstavový a stavový režim protokolu poskytuje flexibilitu, přičemž bezstavový DHCPv6 se používá pro poskytování parametrů, když jsou adresy konfigurovány jinými prostředky, jako je SLAAC.

## K čemu slouží

DHCP byl vytvořen, aby odstranil administrativní zátěž a omezení škálovatelnosti spojené s manuální konfigurací IP adres (statické přiřazení) v IP sítích. Před DHCP museli správci sítě ručně nakonfigurovat každé zařízení s unikátní IP adresou, maskou podsítě a bránou, což byl proces náchylný k lidské chybě, konfliktům adres a neefektivitě, zejména ve velkých nebo dynamických prostředích, jako jsou mobilní sítě, kde se zařízení často připojují a odpojují.

V kontextu 3GPP bylo přijetí DHCP motivováno přechodem na plně IP jádrové sítě počínaje GPRS a UMTS. Jak se mobilní sítě vyvíjely, aby podporovaly paketově orientované datové služby pro obrovské množství uživatelských zařízení, stala se dynamická, automatizovaná metoda správy IP adres nezbytnou. DHCP umožňuje efektivní sdružování a opětovné používání omezených IPv4 adres, podporuje mobilitu zařízení napříč různými body připojení k síti a umožňuje centralizovanou správu síťových politik. Řeší problém poskytování konzistentní, bezchybné síťové konfigurace milionům zařízení bez manuálního zásahu.

DHCP navíc umožňuje pokročilé služby a síťové architektury. Je základním prvkem pro IP Multimedia Subsystem (IMS), protože poskytuje UE adresy kritických funkcí pro řízení relací (P-CSCF). Také podporuje vývoj sítě, včetně integrace nepůvodního přístupu 3GPP (jako je WLAN) a nasazení duálního zásobníku IPv4/IPv6. Automatizací konfigurace DHCP snižuje provozní náklady, minimalizuje čas potřebný k poskytnutí služby a zlepšuje uživatelský zážitek prostřednictvím bezproblémové 'vždy zapnuté' konektivity.

## Klíčové vlastnosti

- Dynamické přidělování IP adres a správa zapůjčení
- Poskytnutí dalších síťových parametrů (DNS, brána, SIP servery)
- Podpora jak stavového, tak bezstavového režimu konfigurace adres
- Funkce přenosového agenta pro centralizované nasazení serverů napříč podsítěmi
- Integrace s procedurami připojení a vytváření PDN spojení v 3GPP
- Podpora IPv4 (DHCPv4) a IPv6 (DHCPv6) podle IETF RFC

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 23.804** (Rel-7) — SMS/MMS over IP Access Support
- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [DHCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dhcp/)
