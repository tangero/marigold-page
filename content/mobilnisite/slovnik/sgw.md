---
slug: "sgw"
url: "/mobilnisite/slovnik/sgw/"
type: "slovnik"
title: "SGW – Signalling Gateway"
date: 2025-01-01
abbr: "SGW"
fullName: "Signalling Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgw/"
summary: "Signalizační brána (SGW) je síťový prvek, který usnadňuje vzájemné propojení různých technologií přenosu signalizace, typicky převádějící zastaralou signalizaci SS7 po TDM linkách na protokoly SIGTRAN"
---

SGW je síťový prvek, který převádí zastaralou signalizaci SS7/TDM na protokoly SIGTRAN založené na IP, aby umožnil vzájemné propojení různých technologií přenosu signalizace.

## Popis

Signalizační brána (SGW) je klíčová funkce pro vzájemné propojení v telekomunikačních sítích, zejména v architektuře 3GPP pro signalizaci jádra sítě. Jejím primárním úkolem je zprostředkování mezi zastaralými systémy přenosu signalizace a moderním přenosem signalizace založeným na IP. Konkrétně často rozhraní mezi tradičním protokolovým zásobníkem [SS7](/mobilnisite/slovnik/ss7/) (Signalling System No. 7), který typicky běží na [TDM](/mobilnisite/slovnik/tdm/) (Time-Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)) okruzích jako E1/T1, a sadou protokolů SIGTRAN (Signalling Transport) založených na IP, definovaných [IETF](/mobilnisite/slovnik/ietf/). SGW provádí konverzi signalizačních zpráv na transportní vrstvě, což umožňuje signalizačním entitám (jako [MSC](/mobilnisite/slovnik/msc/), [HLR](/mobilnisite/slovnik/hlr/) nebo [SCP](/mobilnisite/slovnik/scp/)), které používají SS7, komunikovat s jinými entitami používajícími SIGTRAN přes IP sítě, a naopak.

Architektonicky se SGW nachází na hranici mezi signalizační sítí založenou na TDM a IP signalizační sítí. Má fyzická rozhraní pro obě technologie: TDM linky (např. pro [MTP2](/mobilnisite/slovnik/mtp2/)) na jedné straně a IP síťová rozhraní na straně druhé. Interně implementuje nezbytnou adaptaci protokolů. Například přijímá zprávy SS7 přes vrstvy Message Transfer Part (MTP) po TDM lince. SGW poté extrahuje signalizační zprávu (užitečné zatížení, jako je zpráva ISUP nebo MAP), zapouzdří ji do protokolu SIGTRAN, jako je M3UA (MTP3 User Adaptation), SCTP (Stream Control Transmission Protocol) a IP, a přenese ji přes IP síť k cíli, jako je IP-based MSC nebo Media Gateway Controller. Opačně přijímá pakety SIGTRAN přes IP, extrahuje užitečné zatížení SS7 zprávy a doručí jej přes MTP a TDM do zastaralé ústředny.

Provoz SGW je transparentní pro signalizační aplikace vyšších vrstev (jako MAP, CAP nebo ISUP). Neinterpretuje ani nemodifikuje obsah aplikační vrstvy; pouze adaptuje transportní mechanismus. To umožňuje integraci zastaralých síťových prvků založených na SS7 do vyvíjejícího se jádra sítě založeného na IP bez nutnosti nákladných hardwarových upgradů. SGW je často nasazována společně s Media Gateway (MGW) pro hlasové vzájemné propojení, čímž tvoří kompletní bránové řešení pro migraci sítí z TDM na all-IP. Ve specifikacích 3GPP je SGW zmiňována v kontextech zahrnujících vzájemné propojení sítí, podporu zastaralých technologií a migrační cesty, což zajišťuje, že kritická signalizace pro řízení hovorů, správu mobility a služby může pokračovat mezi starými a novými síťovými doménami.

## K čemu slouží

Signalizační brána byla vytvořena k řešení problému migrace sítí ze zastaralé signalizace založené na TDM na moderní přenos signalizace založený na IP. Jak se mobilní sítě vyvíjely ze 2G/3G na all-IP architektury jako IMS a LTE, hlavní výzvou bylo, jak umožnit existujícím síťovým prvkům založeným na SS7 (např. zastaralé MSC, HLR) komunikovat s novými prvky založenými na IP (např. softswitche, IMS uzly). Bez SGW by tyto sítě byly izolované, což by přerušilo nezbytnou signalizaci pro hovory, SMS a mobilitu.

Historická motivace pramení z posunu průmyslu směrem k IP z důvodu nákladů, škálovatelnosti a flexibility. SS7 přes TDM bylo robustní, ale rigidní a nákladné na škálování. SIGTRAN přes IP nabízel efektivnější přenos. SGW tento rozdíl překlenuje a umožňuje postupnou migraci. Řeší omezení nekompatibilních transportních vrstev provedením nezbytné adaptace, což umožňuje operátorům zavádět uzly založené na IP bez okamžitého vyřazení veškerého zastaralého zařízení. To bylo klíčové pro ekonomickou a technickou proveditelnost vývoje sítě, zajišťující kontinuitu služeb během přechodných období. Její specifikace napříč mnoha vydáními 3GPP odráží její pokračující relevanci při podpoře zastaralých rozhraní v stále více IP-centrických sítích.

## Klíčové vlastnosti

- Konverze transportní vrstvy mezi SS7/MTP přes TDM a SIGTRAN (např. M3UA/SCTP) přes IP
- Transparentní adaptace pro signalizační protokoly vyšších vrstev (MAP, CAP, ISUP)
- Podpora obou směrů signalizačního toku (TDM-to-IP a IP-to-TDM)
- Rozhraní pro zastaralé TDM linky (E1/T1) a IP síťová připojení
- Často nasazována společně s Media Gateway pro kompletní migraci z okruhově komutované na IP síť
- Umožňuje propojení mezi zastaralým jádrem s okruhovou komutací a jádrovými sítěmi založenými na IP

## Související pojmy

- [M3UA – SS7 MTP3 – User Adaptation Layer](/mobilnisite/slovnik/m3ua/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 23.857** (Rel-11) — EPC Node Failure & Restoration Study
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TR 26.924** (Rel-19) — MTSI QoS Improvement Study
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [SGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgw/)
