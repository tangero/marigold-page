---
slug: "iana"
url: "/mobilnisite/slovnik/iana/"
type: "slovnik"
title: "IANA – Internet Assigned Numbers Authority"
date: 2025-01-01
abbr: "IANA"
fullName: "Internet Assigned Numbers Authority"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iana/"
summary: "Globální organizace odpovědná za koordinaci klíčových parametrů internetových protokolů, včetně přidělování IP adres, přiřazování čísel protokolů a správy kořenové zóny DNS. Přestože se nejedná o subj"
---

IANA je globální organizace odpovědná za koordinaci klíčových parametrů internetových protokolů, jako je přidělování IP adres a čísel protokolů, na která odkazují standardy 3GPP pro síťová rozhraní.

## Popis

Internet Assigned Numbers Authority (IANA) je funkce, kterou historicky vykonává organizace ICANN, jež koordinuje klíčové technické prvky globálního internetu, aby zajistila jeho stabilní a bezpečný provoz. Její hlavní odpovědnosti zahrnují přidělování bloků IP adres regionálním internetovým registrům (RIR), správu číselného prostoru [AS](/mobilnisite/slovnik/as/) a správu kořenové zóny [DNS](/mobilnisite/slovnik/dns/). Pro vývoj protokolů je zásadní, že IANA spravuje rejstříky „parametrů protokolů“ – hodnot, čísel a identifikátorů používaných v internetových protokolech (např. čísla protokolů IP, čísla portů TCP/[UDP](/mobilnisite/slovnik/udp/), enterprise čísla pro [SNMP](/mobilnisite/slovnik/snmp/) a [RADIUS](/mobilnisite/slovnik/radius/)).

V kontextu standardů 3GPP je role IANA referenční. Technické specifikace (TS) 3GPP nedefinují nová globální čísla protokolů svévolně. Místo toho, když protokol definovaný 3GPP potřebuje pro použití v IP sítích jedinečný identifikátor (např. nové rozšíření [GTP](/mobilnisite/slovnik/gtp/), DIAMETER aplikaci nebo typ protokolu v hlavičce paketu), specifikace určuje, že hodnota musí být přiřazena IANA. Například TS 29.060 (GTP) stanoví, že typy zpráv GTPv1-C musí být registrovány u IANA, a TS 29.272 (DIAMETER rozhraní pro [E-UTRAN](/mobilnisite/slovnik/e-utran/)) definuje DIAMETER Application-Ids, které vyžadují přiřazení od IANA. To zajišťuje globální interoperabilitu a předchází konfliktům s jinými standardizačními orgány.

Proces zahrnuje podání žádosti 3GPP k IANA prostřednictvím [IETF](/mobilnisite/slovnik/ietf/) RFC nebo přímou vazbou podle pokynů IETF (RFC 5226). Po přiřazení jsou tato čísla publikována v online rejstřících IANA. Zařízení a síťové uzly 3GPP (např. PGW, MME, PCRF) jsou pak implementovány s použitím těchto globálně jedinečných hodnot přiřazených IANA. Tato závislost zdůrazňuje hlubokou integraci architektur 3GPP s širším ekosystémem internetových protokolů a zajišťuje, že sítě 5G a LTE mohou bezproblémově vyměňovat data a signalizaci se servery a sítěmi na veřejném internetu.

## K čemu slouží

IANA existuje jako centrální, neutrální koordinační bod pro technické parametry, které jsou základem interoperability globálního internetu. Bez takové centrální autority by různí výrobci, operátoři a standardizační orgány mohli nezávisle přiřazovat stejná čísla pro různé účely, což by vedlo ke konfliktům protokolů, chybnému směrování paketů a výpadkům služeb. Vznik IANA (původně spravované Jonem Postelem) byl motivován potřebou řádu v raném, rychle se rozvíjejícím ARPANETu a internetu, aby byly základní prostředky, jako jsou IP adresy a čísla protokolů, přidělovány spravedlivě a konzistentně.

Pro 3GPP řeší odkazování na IANA problém integrace mobilních protokolů do globální infrastruktury internetu. Sítě 3GPP nejsou izolované; denně se připojují k internetu a spolupracují s protokoly definovanými IETF. Použitím čísel přiřazených IANA zajišťuje 3GPP, že její protokoly (např. GTP, DIAMETER, PFCP) jsou celosvětově v IP sítích jednoznačně identifikovatelné. Tento přístup řeší omezení proprietárních nebo organizaci specifických číselných prostorů, které by v prostředí více dodavatelů a operátorů způsobily problémy s interoperabilitou. Historickým kontextem je konvergence telekomunikačních a internetových technologií, kde 3GPP přijalo IP za svůj hlavní transport, což si vyžádalo dodržování zavedených koordinačních mechanismů internetu.

## Klíčové vlastnosti

- Globální přidělování prostorů IP adres RIR
- Správa kořenové zóny DNS a domény .int
- Správa rejstříků parametrů protokolů (čísla, kódy)
- Přiřazování čísel autonomních systémů (AS)
- Koordinace čísel portů TCP/UDP a čísel IP protokolů
- Registrace enterprise čísel pro vendor-specific MIB/atributy

## Související pojmy

- [IETF – Internet Engineering Task Force Standard](/mobilnisite/slovnik/ietf/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.816** (Rel-7) — IMS Communication Service Identifier
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.230** (Rel-19) — 3GPP Diameter Protocol Codes Specification
- **TS 29.329** (Rel-19) — Diameter Protocol for Sh Interface
- **TS 29.336** (Rel-19) — HSS Diameter Interfaces for PDN Interworking
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [IANA na 3GPP Explorer](https://3gpp-explorer.com/glossary/iana/)
