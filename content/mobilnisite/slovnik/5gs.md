---
slug: "5gs"
url: "/mobilnisite/slovnik/5gs/"
type: "slovnik"
title: "5GS – 5G System"
date: 2026-01-01
abbr: "5GS"
fullName: "5G System"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5gs/"
summary: "5G System (5GS) je kompletní architektura pro sítě 5G definovaná standardy 3GPP, zahrnující 5G Core Network (5GC) a Next Generation Radio Access Network (NG-RAN). Poskytuje službami řízené, cloud-nati"
---

5GS je kompletní architektura pro sítě 5G definovaná standardy 3GPP, zahrnující 5G Core Network a Next Generation Radio Access Network.

## Popis

5G System (5GS) je komplexní architektonický rámec standardizovaný konsorciem 3GPP pro sítě páté generace (5G). Jeho struktura je založena na dvou hlavních doménách: Next Generation Radio Access Network (NG-RAN) a 5G Core Network (5GC). NG-RAN se skládá z gNB (next-generation NodeB) a ng-eNB (vylepšených LTE [eNB](/mobilnisite/slovnik/enb/) připojených k 5GC), které zajišťují všechny funkce související s rádiovým rozhraním, včetně plánování, správy rádiových zdrojů a připojení uživatelských zařízení (UE). 5GC je cloud-nativní, službami řízená architektura ([SBA](/mobilnisite/slovnik/sba/)), kde jsou síťové funkce ([NF](/mobilnisite/slovnik/nf/)) implementovány jako softwarové služby komunikující přes společný rámec, typicky využívající službami řízená rozhraní ([SBI](/mobilnisite/slovnik/sbi/)) založená na protokolu [HTTP](/mobilnisite/slovnik/http/)/2. To představuje radikální odklon od monolitických, point-to-point rozhraní předchozích jader sítí, jako bylo Evolved Packet Core (EPC).

Jádro 5GC tvoří klíčové funkce řídicí a uživatelské roviny. Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) ukončuje rozhraní N1 a [N2](/mobilnisite/slovnik/n2/), zajišťuje registraci, připojení a správu mobility, ale je záměrně oddělena od správy relací. Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) je zodpovědná za zřizování, modifikaci a uvolňování relací, včetně přidělování IP adres a vynucování pravidel pro uživatelskou rovinu. User Plane Function (UPF) je paketová brána a směrovač pro datovou rovinu, provádí inspekci paketů, směrování, přeposílání a uplatňuje pravidla kvality služeb (QoS) podle pokynů SMF. UPF také umožňuje lokální breakout pro edge computing a podporuje síťové řezy.

Mezi další klíčové funkce patří Unified Data Management (UDM), které ukládá data účastníků a autentizační údaje, Authentication Server Function (AUSF) pro autentizaci a Policy Control Function (PCF) pro rozhodování o politikách. Network Exposure Function (NEF) bezpečně zpřístupňuje síťové schopnosti aplikacím třetích stran. Architektura 5GS je navržena pro flexibilitu a umožňuje síťové řezy – vytváření více logických, izolovaných sítí na sdílené fyzické infrastruktuře – pro obsluhu různých případů užití s odlišnými požadavky na latenci, šířku pásma a spolehlivost. Systém pracuje s jasným oddělením řídicí a uživatelské roviny (CUPS), což jim umožňuje nezávislé škálování a nasazení blíže k okraji sítě pro služby s nízkou latencí.

## K čemu slouží

5G System byl vytvořen pro překonání omezení technologie 4G LTE a jejího Evolved Packet System (EPS), které byly primárně optimalizovány pro mobilní širokopásmový přenos. Exponenciální růst počtu připojených zařízení, požadavky na aplikace s ultra-nízkou latencí (jako autonomní vozidla a průmyslová automatizace) a potřeba masivní komunikace mezi stroji (mMTC) pro IoT učinily předchozí architekturu nedostatečnou. Monolitické síťové funkce a rigidní, point-to-point rozhraní EPS ztěžovaly inovace, efektivní škálování nebo rychlé nasazování nových služeb.

Hlavní motivací pro 5GS bylo vybudovat budoucím výzvám odolnou, flexibilní a efektivní síťové jádro. Přijetím cloud-nativní, službami řízené architektury 5GS odděluje síťové funkce od proprietárního hardwaru, což umožňuje jejich nasazení na běžných serverech a ve virtualizovaných/kontejnerizovaných prostředích. To umožňuje agilní škálování, rychlejší zavádění služeb a snížení provozních nákladů. Explicitní návrh pro síťové řezy je navíc přímou odpovědí na univerzální povahu předchozích generací, což operátorům umožňuje vytvářet přizpůsobené logické sítě pro konkrétní vertikální odvětví (např. samostatný řez pro veřejnou bezpečnost, tovární automatizaci a rozšířenou mobilní širokopásmovou komunikaci) se zaručenými výkonnostními charakteristikami na společné infrastruktuře.

## Klíčové vlastnosti

- Službami řízená architektura (SBA) s rozhraními založenými na HTTP/2
- Oddělení řídicí a uživatelské roviny (CUPS) pro nezávislé škálování
- Nativní podpora síťových řezů pro vytváření více logických sítí
- Cloud-nativní návrh umožňující virtualizaci a kontejnerizaci
- Integrovaná podpora edge computingu prostřednictvím lokálního breakoutu uživatelské roviny
- Rozšířený bezpečnostní rámec s autentizací služeb a zabezpečením SBA

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.916** (Rel-16) — Rel-16 Description Summary
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.632** (Rel-19) — 5G User Data Interworking and Migration
- **TR 23.732** (Rel-16) — User Data Interworking, Coexistence, Migration Study
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- … a dalších 59 specifikací

---

📖 **Anglický originál a plná specifikace:** [5GS na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gs/)
