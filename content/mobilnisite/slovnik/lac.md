---
slug: "lac"
url: "/mobilnisite/slovnik/lac/"
type: "slovnik"
title: "LAC – L2TP Access Concentrator"
date: 2025-01-01
abbr: "LAC"
fullName: "L2TP Access Concentrator"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lac/"
summary: "Síťová funkce, která ukončuje L2TP tunely od uživatelského zařízení a agreguje jejich provoz pro směrování do paketové datové sítě (PDN). Funguje jako protějšek L2TP Network Serveru (LNS) a umožňuje z"
---

LAC je síťová funkce, která ukončuje L2TP tunely od uživatelského zařízení a agreguje jejich provoz pro směrování do paketové datové sítě.

## Popis

[L2TP](/mobilnisite/slovnik/l2tp/) Access Concentrator (LAC) je síťový prvek definovaný v architekturách 3GPP pro scénáře zahrnující Layer 2 Tunneling Protocol (L2TP). Jeho hlavní úlohou je iniciovat a ukončovat L2TP tunely na síťové straně, čímž usnadňuje přístup uživatele k paketovým datovým službám. V typické architektuře s mobilním přístupem naváže uživatelské zařízení (UE) relaci Point-to-Point Protocol (PPP). LAC, který je často kolokován nebo rozhraní s Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway (PGW) ve starších releasech 3GPP, tuto PPP relaci ukončí a zapouzdří PPP rámce do L2TP tunelů.

Operačně LAC spolupracuje s L2TP Network Serverem ([LNS](/mobilnisite/slovnik/lns/)). LAC je zodpovědný za procedury navázání a udržování tunelu s LNS, jak je definováno v [IETF](/mobilnisite/slovnik/ietf/) RFC 2661 a pozdějších aktualizacích. Přeposílá PPP rámce uživatele zabezpečeným L2TP tunelem k LNS, který je následně de-encapsuluje a vloží IP provoz do cílové paketové datové sítě (PDN). LAC zajišťuje agregaci více uživatelských relací do menšího počtu tunelů směrem k LNS, čímž optimalizuje využití síťových zdrojů. Hraje také roli v autentizaci, často se účastní výměn [CHAP](/mobilnisite/slovnik/chap/) nebo PAP proxyováním autentizačních zpráv mezi UE a LNS nebo RADIUS serverem.

V rámci síťové architektury 3GPP je LAC klíčovou komponentou pro umožnění určitých typů přístupu a interoperabilních scénářů. Byl zvláště relevantní pro dial-up a [DSL](/mobilnisite/slovnik/dsl/) interoperabilitu, kde mobilní sítě potřebovaly poskytovat bezproblémový přístup k podnikovým intranetům nebo službám [ISP](/mobilnisite/slovnik/isp/), které spoléhaly na PPP autentizaci a adresování. LAC se nachází ve visitorské nebo domovské síti a poskytuje rozhraní mezi paketovým jádrem 3GPP a ne-3GPP, PPP založenými přístupovými sítěmi, čímž zajišťuje zabezpečenou a řízenou konektivitu pro roamingové a fixed-mobile konvergenční use case.

## K čemu slouží

LAC byl zaveden, aby vyřešil problém integrace 3GPP mobilních sítí s existujícími podnikovými a infrastrukturami internetových poskytovatelů ([ISP](/mobilnisite/slovnik/isp/)), které byly postaveny na technologiích PPP a L2TP. Před všudypřítomnou nativní IP konektivitou v mobilních zařízeních mnoho řešení vzdáleného přístupu pro podniky používalo dial-up sítě s PPP. Účelem LAC bylo umožnit mobilnímu zařízení emulovat dial-up klienta, připojit se přes paketové jádro 3GPP k podnikovému LNS, a tím poskytnout zabezpečený přístup k privátní síti bez nutnosti změn v podnikovém firewallu a autentizačních serverech.

Jeho vznik byl motivován potřebou interoperability a kontinuity služeb během evoluce od 2G/3G k plně IP jádru. Řešil omezení raných mobilních datových služeb, kterým chyběly sofistikované mechanismy zabezpečeného tunelování a autentizace vyžadované podniky. Implementací L2TP ukončení v síti mohli operátoři nabízet přidanou službu 'mobilního VPN'. Tato technologie překlenula mezeru mezi vyvíjejícím se mobilním paketovým jádrem a zavedenou legacy infrastrukturou vzdáleného přístupu, čímž usnadnila podnikové přijetí mobilních dat. Poskytla standardizovanou metodu pro tunelování a správu uživatelských relací, která byla nezávislá na podkladové rádiové přístupové technologii (GERAN, UTRAN).

## Klíčové vlastnosti

- Ukončuje PPP relace iniciované uživatelským zařízením (UE)
- Iniciuje a udržuje L2TP tunely směrem k L2TP Network Serveru (LNS)
- Encapsuluje a de-encapsuluje PPP rámce v rámci L2TP tunelů
- Agreguje více uživatelských relací do konsolidovaných tunelů pro efektivitu sítě
- Proxyuje autentizaci (např. CHAP, PAP) mezi UE a LNS/AAA serverem
- Umožňuje zabezpečený přístup k podnikovým intranetům a službám ISP přes mobilní sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [LAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lac/)
