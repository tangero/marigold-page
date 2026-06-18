---
slug: "sctp"
url: "/mobilnisite/slovnik/sctp/"
type: "slovnik"
title: "SCTP – Stream Control Transmission Protocol"
date: 2025-01-01
abbr: "SCTP"
fullName: "Stream Control Transmission Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sctp/"
summary: "SCTP je spolehlivý, na zprávy orientovaný transportní protokol hojně používaný na signalizačních rozhraních jádra sítě 3GPP. Ve srovnání s TCP poskytuje multihoming, multistreaming a vylepšenou bezpeč"
---

SCTP je spolehlivý, na zprávy orientovaný transportní protokol používaný pro signalizaci v jádru sítě 3GPP, který poskytuje multihoming a multistreaming pro kritická rozhraní jako S1-AP a Diameter.

## Popis

Stream Control Transmission Protocol (SCTP) je transportní protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 4960), který 3GPP vyžaduje pro přenos signalizačních protokolů na mnoha kritických rozhraních. Funguje na ekvivalentní vrstvě jako TCP a [UDP](/mobilnisite/slovnik/udp/), ale je navržen s ohledem na spolehlivost telekomunikační signalizace. V rámci sítě 3GPP se asociace SCTP vytvářejí mezi síťovými funkcemi, například mezi [eNB](/mobilnisite/slovnik/enb/) a [MME](/mobilnisite/slovnik/mme/) (přes [S1-MME](/mobilnisite/slovnik/s1-mme/)), gNB a [AMF](/mobilnisite/slovnik/amf/) (přes NG-C) nebo mezi Diameter partnery (např. MME a [HSS](/mobilnisite/slovnik/hss/)). Poskytuje spolehlivé doručování signalizačních zpráv ve správném pořadí s regulací zahlcení.

SCTP funguje tak, že mezi dvěma koncovými body vytvoří asociaci, která může pro každý koncový bod zahrnovat více IP adres (multihoming). Data se přenášejí v chuncích, které se sdružují do paketů SCTP. Klíčovou architektonickou vlastností je multistreaming: v rámci jedné asociace SCTP existuje více nezávislých logických streamů. Selhání nebo blokování na začátku fronty v jednom streamu (např. kvůli ztracenému chunk) neovlivní doručování chunků v jiných streamech. To je zásadní pro signalizaci, kde různé procedury (např. připojení, předání) mohou probíhat paralelně. Protokol používá čtyřfázový handshake (INIT, INIT-ACK, COOKIE-ECHO, COOKIE-ACK) se stavovými cookies, aby poskytl ochranu před blind SYN flooding útoky.

Klíčové komponenty jeho fungování zahrnují koncový bod SCTP (síťová funkce), asociaci SCTP (spojení), streamy a strukturu paketů založenou na chuncích. Protokol zajišťuje spolehlivost prostřednictvím mechanismu selektivního potvrzování (SACK) a časovačů pro opakovaný přenos. Jeho role v architektuře 3GPP spočívá v tom, že slouží jako základní transport pro téměř všechna rozhraní řídicí roviny jak v Evolved Packet Core (EPC), tak v 5G Core (5GC), včetně S1-MME, S6a, S11, NG-C, N11, N12 a mnoha dalších. Nese aplikační protokoly jako S1-AP, NG-AP a Diameter, čímž zajišťuje robustní doručování signalizačních zpráv pro správu mobility, správu relací a autentizaci i při zahlcení sítě nebo částečném selhání přenosové cesty.

Dále schopnost multihomingu protokolu SCTP umožňuje, aby byla síťová funkce dosažitelná přes více rozhraní IP sítě. Pokud primární cesta selže, provoz může být plynule přepnut na sekundární cestu bez přerušení asociace, což poskytuje redundanci na síťové úrovni. To činí signalizační infrastrukturu jádra sítě vysoce odolnou, což je základním požadavkem pro telekomunikační systémy na úrovni operátora.

## K čemu slouží

SCTP byl 3GPP přijat, aby odstranil nedostatky TCP pro přenos telefonní signalizace. TCP, ačkoli je spolehlivé, způsobuje blokování na začátku fronty, kdy ztráta paketu pro jednu zprávu zpozdí všechny následující zprávy v rámci spojení, což je pro časově kritickou signalizaci, kde musí nezávislé transakce probíhat paralelně, nepřijatelné. Dále je TCP zranitelné vůči některým útokům typu odepření služby (např. SYN floods) a nepodporuje nativně vícesíťové koncové body, což je žádoucí pro odolnost sítě.

Jeho vznik byl motivován potřebou transportního protokolu, který by odpovídal požadavkům signalizace SS7, ale v IP síti. SCTP tyto problémy řeší tím, že poskytuje doručování orientované na zprávy (se zachováním hranic aplikačních zpráv), multistreaming k odstranění blokování na začátku fronty, bezpečný čtyřfázový handshake a vestavěnou podporu multihomingu. To z něj učinilo ideální volbu pro 3GPP při návrhu plně IP jádra sítě (počínaje UMTS R99 a upevněno v EPS), což zajišťuje, že signalizace pro miliony účastníků je robustní i efektivní. Poskytl nezbytný základ pro spolehlivost a dostupnost očekávanou ve veřejných pozemních mobilních sítích.

## Klíčové vlastnosti

- Orientace na zprávy se zachováním hranic datových jednotek aplikačního protokolu
- Multistreaming v rámci jedné asociace k zabránění blokování na začátku fronty
- Podpora multihomingu pro redundanci cest a převzetí služeb při selhání
- Čtyřfázový handshake se stavovými cookies pro vylepšenou bezpečnost proti zahlcení
- Spolehlivé doručování ve správném pořadí s selektivním potvrzováním (SACK)
- Regulace zahlcení a zjišťování maximální přenosové jednotky cesty (path MTU discovery)

## Související pojmy

- [NG-AP – NG Application Protocol](/mobilnisite/slovnik/ng-ap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.803** (Rel-12) — Telepresence using IMS - Study
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.468** (Rel-19) — RANAP User Adaption (RUA) protocol specification
- … a dalších 53 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sctp/)
