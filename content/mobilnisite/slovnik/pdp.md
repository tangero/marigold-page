---
slug: "pdp"
url: "/mobilnisite/slovnik/pdp/"
type: "slovnik"
title: "PDP – Packet Data Protocol"
date: 2025-01-01
abbr: "PDP"
fullName: "Packet Data Protocol"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdp/"
summary: "PDP definuje protokol používaný pro přenos paketových dat v sítích 2G/3G/4G, který umožňuje IP konektivitu mobilních zařízení. Vytváří logický kontext mezi uživatelským zařízením (UE) a bránou GPRS po"
---

PDP je protokol, který vytváří logický kontext mezi mobilním zařízením a síťovou bránou pro zajištění IP konektivity, spravuje přidělování IP adres, kvalitu služeb (QoS) a směrování pro přenos paketových dat.

## Popis

Packet Data Protocol (PDP) je klíčový koncept v paketových sítích 2G ([GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/)) a 3G (UMTS) a jeho principy se přenášejí do 4G (EPS) prostřednictvím konceptu vyvinuté paketové datové sítě ([PDN](/mobilnisite/slovnik/pdn/)). Definuje zásobník protokolů (např. IPv4, IPv6, [PPP](/mobilnisite/slovnik/ppp/)) používaný pro přenos uživatelských dat přes mobilní jádrovou síť. PDP kontext je ústřední provozní entita – jedná se o sadu informačních parametrů vytvořených mezi uživatelským zařízením (UE), obslužným GPRS podpůrným uzlem ([SGSN](/mobilnisite/slovnik/sgsn/)) a bránou GPRS podpůrného uzlu (GGSN) pro usnadnění paketové datové relace. Tento kontext obsahuje kritické informace, jako je typ PDP (např. IPv4), přidělená PDP adresa (IP adresa), požadovaný profil QoS a název přístupového bodu ([APN](/mobilnisite/slovnik/apn/)), který identifikuje externí paketovou datovou síť (např. internet nebo privátní podnikovou síť), ke které se UE chce připojit.

Vytvoření PDP kontextu je vícekroková signalizační procedura. Začíná žádostí o aktivaci PDP kontextu od UE k SGSN, která specifikuje požadovaný APN a typ PDP. SGSN ověří účastníka, provede autentizaci a použije APN k vyhledání adresy příslušného GGSN. Následně předá žádost tomuto GGSN. GGSN, který funguje jako brána k externí síti, přidělí dynamickou PDP adresu (nebo potvrdí statickou), vytvoří koncový bod tunelu a naváže [GTP](/mobilnisite/slovnik/gtp/) (GPRS Tunneling Protocol) tunel zpět k SGSN pro přenos uživatelských dat. SGSN poté nakonfiguruje potřebné přístupové rádiové přenosové kanály s požadovanou QoS a dokončí aktivaci kontextu s UE. Po vytvoření jsou všechny uživatelské IP pakety zapouzdřeny v rámci GTP tunelů mezi GGSN a SGSN a přes rozhraní rádiového přístupu podle specifikovaného typu PDP.

PDP kontext spravuje celý životní cyklus uživatelské datové relace. Podporuje více souběžných kontextů pro jedno UE (např. jeden pro přístup k internetu a druhý pro IMS hlas), každý s nezávislými nastaveními QoS. Kontext lze upravit (např. pro změnu QoS), zachovat během předávání mezi systémy (jako z 3G na 2G) a deaktivovat po ukončení relace. GGSN používá kontext pro funkce jako účtování, vynucování politik a směrování paketů mezi mobilní sítí a externí PDN. Ve vývoji směrem k 4G EPC je PDP kontext nahrazen přenosovým kanálem EPS (EPS Bearer) a připojením PDN, ale základní koncept navázané stavové datové relace se specifickými parametry QoS zůstává.

## K čemu slouží

Mechanismus PDP kontextu byl vytvořen pro zavedení efektivních, vždy zapnutých paketových datových služeb do mobilních sítí, které byly původně navrženy pro přepojování okruhů pro hlas. Před [GPRS](/mobilnisite/slovnik/gprs/) byly datové služby v GSM pomalé a neefektivní, využívaly kanály pro přepojování okruhů, které blokovaly síťové zdroje po celou dobu spojení, podobně jako vytáčený modem. Model PDP kontextu to vyřešil tím, že umožnil dynamické přidělování paketově orientovaných zdrojů na vyžádání, což umožnilo statistické multiplexování dat mnoha uživatelů přes sdílené kanály, což dramaticky zlepšilo efektivitu sítě a umožnilo první praktické zkušenosti s mobilním internetem.

Poskytl standardizovaný rámec pro správu IP konektivity, adresování a kvality služeb v mobilním prostředí. To bylo klíčové pro podporu široké škály vznikajících datových aplikací s různými požadavky, od základního prohlížení webu po přístup k podnikovým VPN. PDP kontext oddělil řídicí rovinu (signalizaci pro vytvoření kontextu) od uživatelské roviny (skutečný tok dat), což umožnilo flexibilnější a škálovatelnější síťové architektury. Také zavedl koncept názvu přístupového bodu (APN), který dal operátorům kontrolu nad směrováním provozu do různých externích sítí (jako operátorské portály, partnerské služby nebo veřejný internet) a umožnil pokročilé služby, jako je konvergence pevných a mobilních sítí.

Dále PDP kontext položil základy pro nezbytné schopnosti mobilního širokopásmového připojení, jako je vždy zapnutá konektivita (kdy je IP adresa zachována i během stavů nečinnosti v rádiu) a bezproblémová mobilita napříč různými technologiemi rádiového přístupu. Stanovil architektonický vzor tunelování uživatelských dat přes jádrovou síť (pomocí GTP), který poskytl zabezpečení, kotvení mobility a zjednodušenou integraci s externími IP sítěmi. Tento model přímo ovlivnil návrh pozdějších systémů, jako je EPS v 4G a 5GC v 5G.

## Klíčové vlastnosti

- Definuje protokol (IP, PPP) pro přenos uživatelských dat.
- Spravuje přidělování IP adres (PDP adresa) pro UE.
- Vytváří a udržuje logické spojení (PDP kontext) mezi UE, SGSN a GGSN.
- Podporuje více souběžných kontextů na jedno UE pro různé služby.
- Přidružuje profil QoS pro definici priority, zpoždění a propustnosti.
- Využívá GTP tunelování pro zabezpečený transport uživatelské roviny přes jádrovou síť.

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.016** (Rel-19) — Subscriber Data Management Stage 2
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- … a dalších 46 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdp/)
