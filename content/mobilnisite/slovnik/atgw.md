---
slug: "atgw"
url: "/mobilnisite/slovnik/atgw/"
type: "slovnik"
title: "ATGW – Access Transfer Gateway"
date: 2025-01-01
abbr: "ATGW"
fullName: "Access Transfer Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/atgw/"
summary: "Access Transfer Gateway (ATGW) je funkce v uživatelské rovině v sítích 3GPP, která zajišťuje plynulou kontinuitu služeb při změně přístupové sítě. Kotví provoz v uživatelské rovině a umožňuje efektivn"
---

ATGW je funkce v uživatelské rovině, která kotví provoz, aby umožnila plynulé předávání spojení mezi 3GPP a ne-3GPP přístupovými sítěmi bez přerušení aktivních relací.

## Popis

Access Transfer Gateway (ATGW) je klíčová entita v uživatelské rovině definovaná v architektuře 3GPP pro IP Flow Mobility ([IFOM](/mobilnisite/slovnik/ifom/)) a plynulé propojení s bezdrátovou místní sítí (WLAN). Funkčně působí jako brána paketové datové sítě (PGW) nebo funkce pro odklonění provozu, která ukončuje referenční body S2a, S2b nebo S2c pro ne-3GPP přístup a zároveň se připojuje k rozhraní SGi směrem k paketové datové síti (např. IMS). Její hlavní architektonická role spočívá v tom, že slouží jako společný kotvící bod IP pro IP toky uživatelského zařízení (UE), bez ohledu na to, zda jsou tyto toky směrovány přes 3GPP přístupovou síť (jako LTE nebo 5G NR) nebo důvěryhodnou/nedůvěryhodnou ne-3GPP přístupovou síť (jako Wi-Fi). Toto ukotvení je zásadní pro procedury Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) a Multi-Access Packet Data Network Connectivity ([MAPCON](/mobilnisite/slovnik/mapcon/)).

Technicky ATGW spolupracuje s funkcemi řídicí roviny, jako je 3GPP [AAA](/mobilnisite/slovnik/aaa/) Server a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). Když UE naváže multi-přístupové PDN spojení, ATGW je vybrána jako bod, kde se uživatelská rovina sbíhá. Udržuje IP adresu UE a provádí vynucování politik, účtování a funkce zákonného odposlechu pro ukotvené toky. Během přenosu mezi přístupy – například při přesunu videohovoru z LTE na Wi-Fi – ATGW spravuje přesměrování konkrétního IP toku. Aktualizuje směrování a případně provádí hlubokou inspekci paketů, aby aplikovala správnou kvalitu služeb (QoS) a účtovací politiky na základě nového typu přístupu a síťových politik.

Vnitřní komponenty ATGW zahrnují rozhraní pro [GTP](/mobilnisite/slovnik/gtp/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol) nebo PMIP (Proxy Mobile IP) pro 3GPP přístup, stejně jako podporu pro DSMIPv6 (Dual-Stack Mobile IPv6) nebo GTP přes S2a/S2b pro ne-3GPP přístup. Integruje se s Policy and Charging Rules Function (PCRF) přes rozhraní Gx pro přijímání dynamických pravidel řízení politik a účtování (PCC). Klíčovou schopností je podpora více souběžných tunelů pro stejné UE asociovaných s různými přístupovými technologiemi, což umožňuje rozhodování o směrování na úrovni jednotlivých toků. To umožňuje pokročilé scénáře řízení provozu, kdy například tok citlivý na latenci (online hra) zůstane na 5G, zatímco stahování velkého souboru je odkloněno na Wi-Fi, a vše je řízeno z jediného kotvícího bodu ATGW.

V širším síťovém ekosystému je ATGW základním kamenem pro dosažení skutečné konvergence sítí. Skrývá složitost podkladových přístupových sítí před vrstvou služeb (např. IMS) a představuje stabilní IP koncový bod. To umožňuje kontinuitu služeb pro IMS-based Voice over Wi-Fi (VoWiFi) a Video over LTE (ViLTE), jak je definováno v technických specifikacích jako 3GPP TS 23.237 (IMS Service Continuity). Její role se vyvinula s virtualizací síťových funkcí (NFV), kde může být implementována jako virtualizovaná síťová funkce (VNF) pro větší škálovatelnost a flexibilitu v cloud-nativních architekturách 5G, přičemž její základní kotvící funkce zůstává klíčová pro scénáře multi-access edge computing (MEC) a uplink classifier (UL CL) v 5G.

## K čemu slouží

ATGW byla zavedena, aby vyřešila kritický problém plynulé kontinuity služeb a efektivního řízení provozu napříč heterogenními rádiovými přístupovými sítěmi. Před její standardizací bylo předávání spojení mezi 3GPP mobilními sítěmi a WLAN typicky typu „přeruš a pak navaz“ (break-before-make), což způsobovalo přerušení relací pro služby v reálném čase, jako jsou hlasové hovory. Raná řešení pro propojení s ne-3GPP sítěmi často spoléhala na síťovou mobilitu (např. PMIP), která mohla být neefektivní pro jemně odstupňované řízení na úrovni toků. Průmysl potřeboval standardizovaný mechanismus, který by umožnil současně využívat více přístupových rádií na zařízení pro vyrovnávání zátěže a lepší uživatelský zážitek, aniž by to vyžadovalo, aby si aplikace byly vědomy změn v podkladové síti.

Historicky vycházela motivace z rozšíření Wi-Fi a touhy bezproblémově ji integrovat do portfolia služeb mobilního operátora. Operátoři chtěli Wi-Fi využívat nejen jako odklonovou cestu pro datový provoz typu best-effort, ale jako důvěryhodné, řízené rozšíření své mobilní sítě schopné doručovat kvalitní hlasové a video služby. ATGW jako součást Evolved Packet Core (EPC) definovaná ve 3GPP Release 10 poskytla potřebný architektonický kotvící bod, aby to bylo možné. Odstranila omezení předchozích přístupů s volným propojením (loose-coupling) tím, že umožnila těsné propojení (tight coupling) pro uživatelskou rovinu, což umožňuje řízenou, na politice založenou mobilitu jednotlivých IP toků mezi přístupy na základě politik operátora, síťových podmínek a uživatelských preferencí.

Dále ATGW umožňuje pokročilé paradigmaty řízení provozu, jako je IP Flow Mobility (IFOM) a Multi-Access PDN Connectivity (MAPCON), které nebyly proveditelné s jednoduššími odklonovými branami. IFOM umožňuje, aby různé IP toky stejného PDN spojení byly současně směrovány přes různé přístupové sítě, zatímco MAPCON umožňuje, aby UE mělo více PDN spojení ke stejnému APN přes různé přístupy. ATGW je centrální uzel, který činí tato komplexní rozhodování o směrování uskutečnitelnými v uživatelské rovině, čímž řeší problém, jak udržet konzistentní IP adresu a stav relace, zatímco jsou pakety fyzicky přenášeny různými síťovými cestami. Tento účel zůstává velmi relevantní v 5G pro podporu funkcí access traffic steering, switch, and splitting (ATSSS).

## Klíčové vlastnosti

- Plynulá kontinuita IP relací během předávání spojení mezi 3GPP a ne-3GPP přístupem
- Mobilita a směrování na úrovni jednotlivých IP toků na základě síťových politik (IFOM)
- Společný kotvící bod IP adresy pro multi-přístupová PDN spojení
- Integrace s PCRF pro dynamické vynucování politik a účtování
- Podpora více tunelovacích protokolů (GTP, PMIP, DSMIPv6)
- Umožňuje simultánní využití více rádií pro řízení a agregaci provozu

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.916** (Rel-14) — eSRVCC Transcoding Minimization Study
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [ATGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/atgw/)
