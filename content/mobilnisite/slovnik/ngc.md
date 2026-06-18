---
slug: "ngc"
url: "/mobilnisite/slovnik/ngc/"
type: "slovnik"
title: "NGC – Next Generation Core Network"
date: 2025-01-01
abbr: "NGC"
fullName: "Next Generation Core Network"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ngc/"
summary: "NGC označuje 5G Core Network (5GC), cloud-nativní, službami založenou architekturu, která poskytuje konektivitu, správu mobility a správu relací pro 5G zařízení. Je klíčovým prvkem pro síťové řezy, ed"
---

NGC je 5G Core Network, cloud-nativní, službami založená architektura poskytující konektivitu, mobilitu a správu relací pro 5G zařízení a umožňující síťové řezy (network slicing) a edge computing.

## Popis

Next Generation Core Network (NGC), standardizovaná spíše jako 5G Core Network (5GC), představuje radikální architektonický posun oproti předchozímu Evolved Packet Core (EPC). Je postavena na cloud-nativní, Service-Based Architecture ([SBA](/mobilnisite/slovnik/sba/)), kde síťové funkce (NFs) jsou modulární softwarové entity, které zpřístupňují své schopnosti prostřednictvím služebních rozhraní založených na [HTTP](/mobilnisite/slovnik/http/)/2. Klíčové řídicí funkce jádra vzájemně komunikují pomocí těchto RESTful [API](/mobilnisite/slovnik/api/), což umožňuje větší flexibilitu, škálovatelnost a automatizaci. Mezi klíčové síťové funkce patří Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), která ukončuje signalizaci [NAS](/mobilnisite/slovnik/nas/) a zajišťuje mobilitu; Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), zodpovědná za zřizování, modifikaci a uvolňování [PDU](/mobilnisite/slovnik/pdu/) relací včetně přidělování IP adres a řízení QoS politik; User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která slouží jako kotvící bod pro směrování, přeposílání, inspekci a vynucování politik pro datové pakety; Authentication Server Function (AUSF) a Unified Data Management (UDM) pro zabezpečení a data předplatitelů; a Network Repository Function (NRF), která umožňuje objevování služeb. NGC odděluje uživatelskou rovinu (UPF) od řídicí roviny (CP), což je princip známý jako Control and User Plane Separation (CUPS), který umožňuje nezávislé škálování a nasazení zdrojů, klíčové pro edge computing. Zavádí koncept PDU Session, což je spojení mezi UE a Data Network (DN), které poskytuje konkrétní službu se zaručenou sadou QoS toků. NGC funguje tak, že se UE zaregistruje v síti prostřednictvím AMF, která následně orchestruje se SMF a UPF k zřízení PDU Session. Všechna rozhodnutí o politikách jsou centralizována v Policy Control Function (PCF), která poskytuje pravidla pro SMF a UPF. Tato architektura nativně podporuje Network Slicing, umožňující vytváření více logických sítí na společné fyzické infrastruktuře, z nichž každá je přizpůsobena konkrétním služebním potřebám, jako je enhanced Mobile Broadband (eMBB), Massive IoT (mIoT) nebo Ultra-Reliable Low-Latency Communications (URLLC).

## K čemu slouží

NGC byla vytvořena, aby řešila omezení 4G EPC, která byla primárně navržena pro mobilní širokopásmový přístup k internetu. Exploze různorodých případů užití předpokládaných pro 5G – od senzorů massive IoT po komunikace pro kritické mise a imerzivní média – vyžadovala jádrovou síť, která byla mnohem flexibilnější, škálovatelnější a efektivnější. Monolitická architektura EPC a těsné propojení funkcí ztěžovaly rychlé nasazování nových služeb nebo optimalizaci zdrojů pro specifické požadavky na latenci či šířku pásma. NGC tyto problémy řeší svým cloud-nativním, službami založeným designem, který umožňuje agilní nasazení, škálování a správu životního cyklu síťových funkcí s využitím principů DevOps. Motivací byla potřeba podpory síťových řezů jako základní schopnosti, což umožňuje operátorům vytvářet virtualizované, end-to-end sítě pro různé zákazníky nebo služby na požádání. Navíc čistým oddělením uživatelské roviny NGC usnadňuje nasazení UPF na okraji sítě, což drasticky snižuje latenci pro aplikace jako autonomní vozidla a průmyslová automatizace. Její vznik představuje přechod telekomunikačních sítí na skutečné softwarově definované platformy schopné podporovat digitální transformaci průmyslu.

## Klíčové vlastnosti

- Cloud-nativní, Service-Based Architecture (SBA) s API HTTP/2
- Nativní podpora end-to-end síťových řezů (Network Slicing)
- Oddělení řídicí a uživatelské roviny (CUPS) pro flexibilní nasazení
- Sjednocený rámec politik řízený funkcí Policy Control Function (PCF)
- Podpora souběžných typů přístupu (3GPP i non-3GPP), jako je Wi-Fi
- Bezstavové síťové funkce pro vysokou odolnost a škálovatelnost

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes
- **TR 38.801** (Rel-14) — Study on new radio access technology: Radio access architecture and interfaces
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [NGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngc/)
