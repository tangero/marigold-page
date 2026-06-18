---
slug: "lmf"
url: "/mobilnisite/slovnik/lmf/"
type: "slovnik"
title: "LMF – Location Management Function"
date: 2026-01-01
abbr: "LMF"
fullName: "Location Management Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lmf/"
summary: "Síťová funkce v jádru sítě 5G odpovědná za správu a koordinaci lokalizačních procedur pro určení polohy uživatelského zařízení (UE). Vypočítává odhady polohy, spravuje lokalizační relace a poskytuje s"
---

LMF (Location Management Function) je síťová funkce v jádru sítě 5G, která spravuje lokalizační procedury pro určení polohy uživatelského zařízení (UE), vypočítává odhady polohy a poskytuje tyto služby autorizovaným konzumentům.

## Popis

Location Management Function (LMF) je klíčová součást architektury lokalizačních služeb jádra sítě 5G, definovaná jako síťová funkce ([NF](/mobilnisite/slovnik/nf/)) v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)). Je primární entitou odpovědnou za orchestraci všech činností souvisejících s určováním zeměpisné polohy uživatelského zařízení (UE). LMF přijímá žádosti o lokalizační služby od jiných síťových funkcí, například od Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) pro externí aplikace nebo od Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) pro žádosti iniciované sítí. Po přijetí žádosti LMF zahájí lokalizační relaci s cílovým UE a s rádiovou přístupovou sítí (RAN).

Fungování LMF zahrnuje několik klíčových kroků. Nejprve vybere vhodnou lokalizační metodu na základě požadované kvality služby (QoS), schopností UE a stavu sítě. Mezi podporované metody patří downlinkové a uplinkové techniky LTE/5G NR, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)), Multi-Cell Round Trip Time (Multi-RTT) a Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). LMF koordinuje s NG-RAN prostřednictvím AMF pomocí rozhraní NLs, aby instruovala gNB k provedení potřebných měření (např. časových měření pro OTDOA) nebo ke konfiguraci lokalizačních referenčních signálů. Pro metody založené na UE může LMF poskytnout UE pomocná data (např. efemeridy satelitů, almanach základnových stanic), aby usnadnila vlastní výpočet polohy.

Architektonicky LMF zpřístupňuje ostatním NF rozhraní založená na službách, především Nlmf_Location. Interaguje s AMF (služba Nlmf_Location) pro dosažení UE a RAN a s GMLC (rozhraní Ngl) pro externí lokalizační požadavky. LMF také komunikuje s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro získání dat o účastníkovi a příslušných politik. Provede výpočet polohy zpracováním měřicích reportů přijatých od RAN (např. měření z gNB) a/nebo od UE. Výsledný odhad polohy, který může mít formu zeměpisných souřadnic (zeměpisná šířka, délka) s elipsou nejistoty, je pak vrácen žadateli.

Kromě základní lokalizace LMF podporuje pokročilé funkce, jako je periodické a spouštěné reportování polohy, odhad rychlosti a fúze dat z barometrických senzorů pro vertikální určení polohy. Také řeší chybové stavy, záložní procedury a vyjednávání QoS. V kontextu síťového řezání může být LMF instancována jako součást řezu, aby poskytovala dedikované lokalizační služby pro specifické vertikály (např. vysoce přesnou lokalizaci pro automatizaci továren). Její návrh klade důraz na škálovatelnost, nízkou latenci a podporu různorodých případů užití od služeb pro masový trh až po aplikace kritické pro provoz.

## K čemu slouží

LMF byla zavedena ve specifikaci 3GPP Release 15 jako součást nového systému 5G (5GS), aby poskytla jednotnou, flexibilní a vylepšenou schopnost správy polohy. Odstraňuje omezení předchozích generací (např. 4G E-SMLC) tím, že je nativně integrována do architektury 5G založené na službách, což nabízí lepší škálovatelnost, nižší latenci a podporu nových rádiových technologií jako 5G NR. Přechod na cloud-nativní design založený na mikroslužbách umožňuje dynamické nasazení LMF pro uspokojení různorodých požadavků služeb.

Její vytvoření bylo motivováno potřebou přesnějších a spolehlivějších lokalizačních služeb pro podporu nových případů užití v 5G. Patří mezi ně komunikace Vehicle-to-Everything (V2X) pro autonomní řízení, která vyžaduje přesnost na úrovni centimetrů; průmyslový IoT pro sledování aktiv a automatizaci; a vylepšené služby tísňového volání (např. Advanced Mobile Location) požadované regulátory. LMF poskytuje základní inteligenci pro koordinaci více lokalizačních zdrojů a metod, aby splnila tyto přísné požadavky.

Dále LMF umožňuje síťovým operátorům nabízet polohu jako službu poskytovatelům aplikací třetích stran standardizovaným a bezpečným způsobem. Centralizací koordinace lokalizace snižuje složitost v RAN a UE, umožňuje optimalizované využití zdrojů a usnadňuje zavádění nových lokalizačních technologií (jako je lokalizace přes sidelink) v budoucích releasech. Je základním prvkem pro naplnění vize 5G o všudypřítomném, vysoce přesném povědomí o poloze.

## Klíčové vlastnosti

- Koordinuje více lokalizačních metod 5G NR a LTE (OTDOA, UTDOA, Multi-RTT, A-GNSS) pro určení polohy UE.
- Zpřístupňuje rozhraní založené na službě Nlmf_Location pro interakci s AMF, GMLC a dalšími síťovými funkcemi jádra 5G.
- Vypočítává odhady polohy pomocí měřicích reportů z gNB a UE, často s využitím hybridních lokalizačních algoritmů.
- Podporuje různé typy lokalizačních služeb: okamžité, odložené (periodické/spouštěné) a aktuální nebo poslední známou polohu.
- Spravuje lokalizační relace, včetně vyjednávání QoS, doručování pomocných dat a kontrol autorizace a ochrany soukromí.
- Může být nasazena jako cloud-nativní síťová funkce s podporou síťového řezání pro specifické požadavky vertikálních služeb.

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 24.572** (Rel-19) — 5G LCS User Plane Protocol Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.517** (Rel-19) — 5G AF Event Exposure Service Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.572** (Rel-19) — Nlmf Service Based Interface Stage 3
- **TS 29.574** (Rel-19) — 5G Data Collection Coordination Services Stage 3
- **TS 29.576** (Rel-19) — 5G Messaging Framework Adaptor Services Stage 3
- **TS 29.591** (Rel-19) — 5G NEF Southbound Services Stage 3
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [LMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmf/)
