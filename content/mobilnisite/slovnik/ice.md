---
slug: "ice"
url: "/mobilnisite/slovnik/ice/"
type: "slovnik"
title: "ICE – Interactivity Connectivity Establishment"
date: 2026-01-01
abbr: "ICE"
fullName: "Interactivity Connectivity Establishment"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ice/"
summary: "Rámec definovaný 3GPP pro navazování interaktivních mediálních relací, jako jsou hlasové a videohovory, v různorodých síťových prostředích. Vychází z metodiky IETF pro Interaktivní navázání spojení (I"
---

ICE je 3GPP rámec pro navazování interaktivních mediálních relací, jako jsou hlasové a videohovory, napříč různorodými sítěmi, který rozšiřuje metodiku IETF, aby zajistil robustní průchod přes NAT a firewally.

## Popis

Interaktivní navázání spojení (Interactivity Connectivity Establishment - ICE) v kontextu 3GPP je rámec služeb, který poskytuje standardizovaný mechanismus pro navazování interaktivních mediálních relací (např. Voice over LTE (VoLTE), Video over LTE (ViLTE) a další služby založené na IMS) v prostředí s překladem síťových adres ([NAT](/mobilnisite/slovnik/nat/)) a firewally. Jedná se o adaptaci a profilaci protokolu ICE od [IETF](/mobilnisite/slovnik/ietf/) (RFC 8445) pro použití v architektuře IP Multimedia Subsystem (IMS) 3GPP. Hlavní funkcí ICE je objevit optimální síťovou cestu mezi dvěma koncovými body komunikace shromážděním kandidátních transportních adres (kombinací IP adresy a portu), jejich prioritizací a provedením kontrol spojení pro ověření, které páry mohou úspěšně komunikovat.

Jak to funguje, zahrnuje několik klíčových komponent a kroků, které primárně provádí uživatelské zařízení (UE) za asistence síťových prvků. Nejprve každé UE shromáždí kandidátní adresy. Ty zahrnují Hostitelskou kandidáta (vlastní lokální IP adresu), Server-reflexivní kandidáty (svou veřejnou IP adresu, jak ji vidí STUN server, získanou prostřednictvím STUN binding request) a Relayované kandidáty (adresu na TURN relay serveru, použitou jako poslední možnost). V nasazení IMS 3GPP často [P-CSCF](/mobilnisite/slovnik/p-cscf/) zahrnuje nebo sdílí umístění s funkcemi souvisejícími s ICE a funguje jako STUN/TURN server. Kandidáti jsou poté odesláni vzdálené straně prostřednictvím výměny nabídky/odpovědi protokolu SIP (Session Initiation Protocol) vložené v SDP (Session Description Protocol).

Jakmile obě strany vymění seznamy kandidátů, zahájí kontroly spojení. Každý koncový bod systematicky odesílá STUN binding requests ke kandidátním párům poskytnutým druhým koncovým bodem, přičemž upřednostňuje páry, které mají nejvyšší pravděpodobnost nejrychlejší funkčnosti (např. host-to-host ve stejné podsíti). První pár, který vede k úspěšné obousměrné výměně STUN request/response, je vybrán pro tok médií. Tento proces zajišťuje, že média použijí nejpřímější možnou cestu, a zároveň garantuje záložní přechod na relayovanou cestu, pokud je přímé spojení blokováno. V rámci 3GPP specifikace jako TS 24.229 a TS 29.333 detailně popisují, jak jsou procedury ICE integrovány do signalizace IMS a jak P-CSCF řídí a asistuje procesu, aby byl v souladu se síťovými politikami a mechanismy kvality služeb (QoS).

## K čemu slouží

ICE byl vytvořen k vyřešení základního problému navazování peer-to-peer mediálních relací na moderním internetu, který je ovládán nedostatkem IPv4 adres a následnou všudypřítomnou přítomností [NAT](/mobilnisite/slovnik/nat/) a stavových firewallů. Tato zařízení porušují princip end-to-end spojitosti tím, že skrývají privátní IP adresy a dynamicky přidělují porty, což znemožňuje koncovému bodu za NAT jednoduše oznámit svou privátní adresu a přijímat příchozí mediální toky. Před ICE řešení jako jednoduchý STUN fungovala pouze pro určité typy NAT a často vyžadovala přechod na mediální relay (TURN) pro všechny relace, což je neefektivní a nákladné.

Motivace 3GPP pro přijetí a profilaci ICE byla poháněna přechodem na plně IP sítě s LTE a závislostí na IMS pro telefonní služby (VoLTE). Aby byly hlasové a videohovory na úrovni operátora úspěšné, potřebovaly spolehlivost a kvalitu odpovídající okruhově přepínaným sítím, ale přes IP infrastrukturu sdílenou s best-effort daty. ICE poskytuje robustní, standardizovanou metodu pro průchod NAT, která maximalizuje šanci na navázání přímé, nízkolatenční mediální cesty (optimální pro kvalitu) a zároveň garantuje, že relayované spojení bude fungovat v případě potřeby (zajištění spolehlivosti). To bylo klíčovým faktorem pro komerční úspěch VoLTE.

Dále ICE umožňuje fungování relací napříč různorodými síťovými připojeními, včetně situací, kdy se UE pohybuje mezi mobilní sítí a Wi-Fi ([IFOM](/mobilnisite/slovnik/ifom/), [MAPCON](/mobilnisite/slovnik/mapcon/) nebo později [ATSSS](/mobilnisite/slovnik/atsss/)). Poskytuje jednotnou metodiku pro navazování spojení bez ohledu na podkladovou přístupovou technologii. Standardizací tohoto mechanismu v rámci 3GPP je zajištěno, že všechna UE a síťové prvky implementují kompatibilní, interoperabilní a efektivní mechanismus, čímž se předchází proprietárním řešením a podporuje konzistentní uživatelský zážitek pro interaktivní služby.

## Klíčové vlastnosti

- Shromažďuje více kandidátních transportních adres (hostitelská, server-reflexivní, relayovaná)
- Provádí systematické kontroly spojení pomocí STUN k nalezení funkčních kandidátních párů
- Integruje se s IMS signalizací prostřednictvím SIP a SDP pro výměnu kandidátů
- Prioritizuje kandidátní páry pro výběr nejefektivnější mediální cesty
- Poskytuje garantovaný záložní přechod na TURN relay pro navázání spojení
- Podporuje mobilitu a operace s duálním zásobníkem IPv4/IPv6

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.232** (Rel-19) — Mc Interface Protocol Profile
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [ICE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ice/)
