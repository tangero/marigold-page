---
slug: "pdn"
url: "/mobilnisite/slovnik/pdn/"
type: "slovnik"
title: "PDN – Packet Data Network"
date: 2026-01-01
abbr: "PDN"
fullName: "Packet Data Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdn/"
summary: "Paketová datová síť (PDN) je jakákoli externí síť založená na IP protokolu (jako internet nebo podniková intranetová síť), ke které se zařízení mobilního uživatele připojuje prostřednictvím jádrové sí"
---

PDN je externí síť založená na IP protokolu, například internet nebo podniková intranetová síť, ke které se mobilní uživatel připojuje prostřednictvím jádrové sítě operátora pro datové služby.

## Popis

V architektuře 3GPP je paketová datová síť (PDN) externí síť, která poskytuje paketově přepínané datové služby uživatelskému zařízení (UE). V podstatě se jedná o IP síť, která se nachází mimo doménu operátora 3GPP. Mezi běžné příklady patří veřejný internet, síť IMS (Internet Multimedia Subsystem) pro VoIP a VoLTE nebo privátní podniková intranetová síť. Primární funkcí jádrové sítě 3GPP – ať už jde o [GPRS](/mobilnisite/slovnik/gprs/), EPS (4G) nebo 5GS (5G) – je poskytovat zabezpečené, politikami řízené připojení mezi UE a jednou či více PDN.

Připojení k PDN se navazuje prostřednictvím kontextu [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) v 3G/4G nebo [PDU](/mobilnisite/slovnik/pdu/) (Protocol Data Unit) session v 5G. Toto logické spojení je ukotveno v uzlu brány: v GGSN (Gateway GPRS Support Node) pro 3G, v [PDN-GW](/mobilnisite/slovnik/pdn-gw/) (nebo [PGW](/mobilnisite/slovnik/pgw/)) pro 4G EPS a v [UPF](/mobilnisite/slovnik/upf/) (User Plane Function) pro 5G. Tato brána slouží jako vstupní a výstupní bod pro veškerý provoz v uživatelské rovině mezi sítí 3GPP a externí PDN. Plní klíčové funkce, jako je přidělování IP adresy UE (často z adresního prostoru PDN), směrování a přeposílání paketů, vynucování politik, účtování a filtrování provozu.

Každá PDN je identifikována pomocí [APN](/mobilnisite/slovnik/apn/) (Access Point Name), textového popisku, který UE uvádí ve své žádosti o připojení. Síť používá APN k určení správné brány a konkrétní externí sítě, ke které se má připojit. Jedno UE může mít současně více připojení k různým PDN (např. jedno pro internet, jedno pro IMS), přičemž každé má svou vlastní IP adresu a sadu charakteristik QoS. Koncept PDN abstrahuje detaily externí sítě, což umožňuje jádru 3GPP poskytovat konzistentní sadu funkcí pro mobilitu, zabezpečení a politiky bez ohledu na to, zda je cílem veřejný internet nebo specializovaná servisní síť.

Role PDN se vyvíjela s generacemi sítí. V 5G je koncept zobecněn, ale princip zůstává. Jádrová síť 5G poskytuje 'služby PDU konektivity' 'datovým sítím' ([DN](/mobilnisite/slovnik/dn/)), což je 5G ekvivalent PDN. Kontinuita služeb mezi EPS a 5GS je z velké části závislá na udržení připojení k PDN / PDU sessions během předávání mezi systémy. Bezpečnostní hranice mezi důvěryhodným jádrem operátora a externí PDN je důsledně vynucována na bráně pomocí firewallů, NAT (Network Address Translation) a tunelovacích protokolů jako GTP nebo IPsec.

## K čemu slouží

Koncept paketové datové sítě (PDN) byl zaveden, aby formalizoval a standardizoval způsob, jakým mobilní sítě poskytují přístup k externím datovým službám založeným na IP protokolu. V raných celulárních sítích byly datové služby přepínané okruhově a omezené. Přechod na paketově přepínaná data vyžadoval model, kde mobilní síť fungovala jako přístupová síť k širšímu internetu a dalším IP sítím. Koncept PDN vytvořil jasnou architektonickou separaci mezi doménou správy mobility operátora a širokou škálou externích servisních sítí.

Řešil problém, jak směrovat IP pakety k mobilnímu účastníkovi a od něj, přičemž jeho připojovací bod k rádiové síti se neustále mění. Brána PDN (jako GGSN/PGW) slouží jako pevný ukotvovací bod v IP topologii, který skrývá mobilitu účastníka před externí PDN. To umožňuje UE udržovat stabilní IP adresu a pokračující session i při pohybu mezi základnovými stanicemi. Bez tohoto modelu ukotvení a tunelování k definované PDN by mobilní IP datové služby byly nepraktické.

Historicky model PDN umožnil komerční úspěch mobilního internetu. Poskytl rámec pro účtování (různé sazby pro různé PDN prostřednictvím APN), diferenciaci služeb (upřednostňování IMS provozu před best-effort internetem) a zabezpečený přístup do podnikových sítí (přes privátní APN). Vývoj od 3G k 5G vedl k větší flexibilitě konceptu PDN (podpora ne-IP provozu v 5G) a jeho integraci s network slicing, kde slice může poskytovat vyhrazenou konektivitu ke specifickému typu PDN (např. průmyslové IoT síti). Zůstává základní abstrakcí pro všechny mobilní datové služby.

## Klíčové vlastnosti

- Představuje jakoukoli externí IP síť (Internet, IMS, podnikovou), přístupnou přes mobilní jádro
- Identifikována pomocí APN (Access Point Name), které se používá pro směrování a politiky
- Konektivita je ukotvena v uzlu brány (GGSN, PGW, UPF)
- Podporuje simultánní připojení UE k více PDN
- Umožňuje přidělování IP adres z adresního prostoru PDN
- Tvoří hranici pro zabezpečení a vynucování politik mezi operátorem a externími sítěmi

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [DN – Distinguished Name](/mobilnisite/slovnik/dn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdn/)
