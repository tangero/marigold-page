---
slug: "5gcn"
url: "/mobilnisite/slovnik/5gcn/"
type: "slovnik"
title: "5GCN – 5G Core Network"
date: 2025-01-01
abbr: "5GCN"
fullName: "5G Core Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5gcn/"
summary: "5G Core Network (5GCN) je centrální mozek systémů 5G, definovaný od 3GPP Release 15 dále. Poskytuje funkce řídicí a uživatelské roviny pro konektivitu, mobilitu a správu politik. Jeho cloud-nativní, s"
---

5GCN je centrální mozek systémů 5G, který poskytuje funkce řídicí a uživatelské roviny pro konektivitu, mobilitu a správu politik s cloud-nativní, službami založenou architekturou.

## Popis

5G Core Network (5GCN) je základní architektonický rámec pro základní síť v systémech 5G, standardizovaný 3GPP počínaje Release 15. Představuje radikální odklon od předchozích architektur Evolved Packet Core (EPC) tím, že přijímá plně cloud-nativní, službami založenou architekturu (SBA). To znamená, že síťové funkce jsou implementovány jako modulární, znovupoužitelné softwarové služby, které komunikují přes standardizovaná rozhraní založená na HTTP/2 (např. N1, N2, N4). Architektura čistě odděluje uživatelskou rovinu (UPF - User Plane Function) od řídicí roviny, což umožňuje nezávislé škálování, nasazení a optimalizaci přenosu dat a signalizační logiky. Toto oddělení je základním kamenem pro podporu různorodých požadavků služeb, od vysoko-přenosových videostreamů až po kriticky důležitou průmyslovou automatizaci.

V jádru 5GCN funguje tak, že vytváří a spravuje Protocol Data Unit (PDU) Sessions pro uživatelské zařízení (UE). Řídicí rovina, řízená funkcemi jako Access and Mobility Management Function (AMF) a Session Management Function (SMF), zpracovává registraci, autentizaci, mobilitu a zřizování relací. AMF je jediným vstupním bodem pro veškerou řídicí signalizaci UE, ukončuje rozhraní N1 a N2. SMF je zodpovědná za správu relací, včetně přidělování IP adres, výběru UPF a konfigurace pravidel pro směrování provozu a vynucování politik přes rozhraní N4 směrem k UPF. UPF pak funguje jako inteligentní datový směrovač, provádí směrování a přeposílání paketů, inspekci paketů, zpracování QoS a reportování využití provozu.

Mezi klíčové architektonické komponenty patří Network Repository Function (NRF), která umožňuje objevování služeb a umožňuje síťovým funkcím se dynamicky vyhledávat a vzájemně komunikovat. Funkce Unified Data Management (UDM) spravuje data účastníků a generuje autentizační přihlašovací údaje. Policy Control Function (PCF) poskytuje pravidla politik funkcím řídicí roviny. Authentication Server Function (AUSF) provádí autentizaci s UE. Společně tyto funkce umožňují pokročilé schopnosti jako síťové krájení (network slicing), kdy jsou na společné fyzické infrastruktuře vytvářeny vícečetné logické, izolované sítě, každá přizpůsobená specifickým potřebám služeb (např. jeden výsek pro vylepšené mobilní širokopásmové připojení, další pro masivní IoT). Úlohou 5GCN je poskytnout flexibilní, škálovatelný a programovatelný základ, který může efektivně podporovat širokou škálu případů užití 5G definovaných ITU-R IMT-2020.

## K čemu slouží

5GCN byl vytvořen, aby řešil omezení 4G Evolved Packet Core (EPC), která byla primárně navržena pro mobilní širokopásmové připojení. Monolitická, uzlově založená architektura EPC se potýkala se škálovatelností, flexibilitou a různorodými požadavky na výkon, které byly předpokládány pro 5G, jako je ultra-nízká latence, masivní konektivita zařízení a síťové krájení. Primární motivací bylo vybudovat základní síť, která je od základu cloud-nativní, což operátorům umožňuje nasazovat síťové funkce jako software na běžném komerčním hardwaru, využívat virtualizaci síťových funkcí (NFV) a přijmout moderní DevOps postupy pro rychlou inovaci a nasazení služeb.

Historicky každá generace mobilních sítí představila novou základní síť (např. jádro s přepojováním okruhů pro GSM, jádro pro UMTS, EPC pro 4G). Přechod na 5G vyžadoval jádro, které by mohlo být více než jen rychlejším potrubím pro smartphony. Potřebovalo to být všestrannou služební platformou schopnou podporovat vertikální odvětví jako automobilový průmysl, výroba a zdravotnictví. 5GCN to řeší svou službami založenou architekturou, která odděluje software od hardwaru, a svým jasným oddělením uživatelské a řídicí roviny, což umožňuje nasazení datové roviny na okraji sítě pro minimalizaci latence. Přímo řeší problém síťové nepružnosti tím, že umožňuje síťové krájení, poskytuje vyhrazené virtuální sítě se specifickými charakteristikami a podporuje širší škálu autentizačních metod a typů relací nad rámec jednoduché IP konektivity.

## Klíčové vlastnosti

- Cloud-nativní, službami založená architektura (SBA) s rozhraními HTTP/2
- Oddělení řídicí a uživatelské roviny (CUPS) pro nezávislé škálování
- Nativní podpora síťového krájení pro vytváření logických, izolovaných sítí
- Jednotný rámec politik pro správu kvality relací a služeb
- Podpora souběžného přístupu k lokálním a centrálním datovým sítím
- Integrace společného API rámce pro vystavení aplikacím třetích stran

## Definující specifikace

- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [5GCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gcn/)
