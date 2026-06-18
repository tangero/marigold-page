---
slug: "mbs"
url: "/mobilnisite/slovnik/mbs/"
type: "slovnik"
title: "MBS – Frequency Selection Area Identity"
date: 2026-01-01
abbr: "MBS"
fullName: "Frequency Selection Area Identity"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mbs/"
summary: "MBS, jako identifikátor oblasti pro výběr kmitočtu, je identifikátor používaný v sítích 5G pro správu oblastí výběru kmitočtu pro služby vysílání a skupinového vysílání. Pomáhá síti efektivně přidělov"
---

MBS (Multicast/Broadcast Service) je identifikátor oblasti pro výběr kmitočtu (Frequency Selection Area Identity) používaný v sítích 5G pro správu oblastí vysílání a skupinového vysílání za účelem efektivního přidělování rádiových prostředků a současného doručování obsahu.

## Popis

Identifikátor oblasti pro výběr kmitočtu (MBS) je klíčový síťový identifikátor v rámci architektury služby skupinového/vysílacího vysílání (MBS) v 5G, navržený pro správu a optimalizaci doručování vysílacího a skupinového obsahu. V 5G umožňuje MBS efektivní přenos typu point-to-multipoint, kdy je jeden datový proud doručován více uživatelským zařízením (UE) v konkrétní geografické oblasti, čímž šetří rádiové prostředky ve srovnání s individuálními přenosy typu unicast. Identifikátor MBS se používá k definování oblasti pro výběr kmitočtu ([FSA](/mobilnisite/slovnik/fsa/)), což je logická oblast, kde jsou pro přenosy MBS vyčleněny specifické kmitočtové prostředky. Tato oblast může být dynamicky konfigurována na základě faktorů, jako je hustota uživatelů, poptávka po službách a vytížení sítě, což operátorům umožňuje pružně spravovat spektrum.

Architektonicky je identifikátor MBS konfigurován a spravován jádrem sítě 5G (5GC) a rádiovou přístupovou sítí (RAN). Je spojen s kontexty MBS relací a používají jej síťové funkce, jako je funkce služby skupinového/vysílacího vysílání ([MBSF](/mobilnisite/slovnik/mbsf/)) a gNB, pro koordinaci přidělování prostředků. Když se UE přihlásí k odběru služby MBS, síť použije identifikátor MBS k určení příslušných kmitočtových prostředků a parametrů přenosu. Identifikátor zajišťuje, že UE ve stejné FSA mohou efektivně přijímat skupinový/vysílací proud bez zbytečné signalizační režie, protože se mohou synchronizovat na stejné fyzické prostředky identifikované pomocí MBS.

Jak to funguje, zahrnuje několik kroků. Nejprve 5GC zřídí relaci MBS a přiřadí identifikátor MBS odpovídající oblasti pro výběr kmitočtu. Tento identifikátor je prostřednictvím řídicí signalizace, např. v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)) nebo vyhrazených zprávách [RRC](/mobilnisite/slovnik/rrc/), komunikován do RAN a k UE. gNB následně naplánuje přenosy MBS na konkrétních časově-kmitočtových prostředcích (např. ve slotech fyzického sdíleného downlink kanálu) označených tímto identifikátorem. UE monitorující služby MBS používají identifikátor MBS k filtrování a dekódování relevantních přenosů, což jim umožňuje efektivně přijímat obsah, jako je živé streamování videa nebo aktualizace softwaru. Identifikátor také podporuje mobilitu, protože UE přesouvající se mezi FSA mohou být předána k novým identifikátorům MBS, aby byla zachována kontinuita služby.

Klíčové komponenty, které interagují s identifikátorem MBS, zahrnují MBSF v jádře sítě, která spravuje zásady relací MBS, a gNB v RAN, které zpracovává plánování rádiových prostředků. Identifikátor hraje roli v síťových řezech tím, že umožňuje vyčlenění vyhrazených prostředků pro MBS v rámci řezu a zajišťuje QoS pro vysílací služby. Jeho technická implementace zahrnuje kódování v protokolech jako [NGAP](/mobilnisite/slovnik/ngap/) a [F1AP](/mobilnisite/slovnik/f1ap/) pro komunikaci mezi jádrem a RAN a RRC pro konfiguraci UE, což zajišťuje bezproblémovou integraci do systémové architektury 5G.

## K čemu slouží

Identifikátor MBS byl zaveden k řešení neefektivnosti používání přenosů typu unicast pro doručování populárního obsahu mnoha uživatelům současně, jako jsou živé sportovní události nebo nouzová upozornění. V předchozích generacích mobilních sítí existovaly vysílací služby, jako je služba skupinového multimediálního vysílání ([MBMS](/mobilnisite/slovnik/mbms/)) v LTE, které však měly omezení v pružnosti a integraci s architekturou 5G založenou na službách. Motivace pro MBS v 5G, včetně jeho identifikátorů, vychází z rostoucí poptávky po skupinové komunikaci s vysokou kvalitou a nízkou latencí, která je zásadní pro aplikace jako veřejná bezpečnost, aktualizace automobilového softwaru nebo distribuce médií.

Historicky používalo MBMS v LTE dočasné identifikátory mobilních skupin a oblasti služeb, ty však byly méně dynamické a nebyly plně integrovány s možnostmi síťových řezů a edge computingu v 5G. Identifikátor MBS tyto problémy řeší tím, že poskytuje podrobnější a flexibilnější způsob správy kmitočtových prostředků pro skupinové/vysílací vysílání. Umožňuje operátorům dynamicky definovat oblasti na základě poptávky v reálném čase, optimalizovat využití spektra a snižovat interference. To je zvláště důležité v 5G, kde je spektrum vzácným zdrojem a služby vyžadují přísné parametry QoS.

Vytvoření identifikátoru MBS bylo motivováno potřebou podporovat nové případy užití v 5G, jako je komunikace Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)) a imerzivní média, kde je efektivní skupinová komunikace kritická. Díky umožnění přesné kontroly nad oblastmi pro výběr kmitočtu pomáhá identifikátor dosáhnout nízké latence a vysoké spolehlivosti vyžadované pro tyto aplikace. Také usnadňuje konvergenci vysílacích a unicastových služeb v rámci jednotného rámce 5G, což operátorům umožňuje využívat stávající infrastrukturu pro inovativní služby.

## Klíčové vlastnosti

- Definuje logické oblasti pro výběr kmitočtu (FSA) pro přidělování prostředků MBS.
- Umožňuje efektivní přenos typu point-to-multipoint v sítích 5G.
- Podporuje dynamickou konfiguraci na základě poptávky po službách a vytížení sítě.
- Integruje se s funkcemi jádra sítě 5G, jako je MBSF, pro správu relací.
- Umožňuje UE filtrovat a dekódovat toky skupinového/vysílacího vysílání.
- Vylepšuje podporu mobility pro služby MBS při pohybu mezi různými oblastmi.

## Související pojmy

- [MBSF – Multicast/Broadcast Service Function](/mobilnisite/slovnik/mbsf/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.548** (Rel-19) — SEAL Network Resource Management Protocol
- **TS 24.575** (Rel-19) — UE Pre-configuration for MBS
- **TS 24.577** (Rel-19) — A2X Services in 5GS
- **TS 24.578** (Rel-19) — UE policies for A2X services in 5GS
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- … a dalších 57 specifikací

---

📖 **Anglický originál a plná specifikace:** [MBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbs/)
