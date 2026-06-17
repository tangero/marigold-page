---
slug: "bmg"
url: "/mobilnisite/slovnik/bmg/"
type: "slovnik"
title: "BMG – Broadcast Message Gateway"
date: 2025-01-01
abbr: "BMG"
fullName: "Broadcast Message Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bmg/"
summary: "Broadcast Message Gateway (BMG) je funkce jádra sítě 5G zavedená ve specifikaci 3GPP Release 18. Umožňuje efektivní doručování vysílacích a skupinových zpráv, jako jsou veřejná varování nebo skupinová"
---

BMG je funkce jádra sítě 5G, která slouží jako brána pro efektivní doručování vysílacích (broadcast) nebo skupinových (multicast) zpráv, například veřejných varování, z aplikačních serverů k velkému počtu uživatelských zařízení.

## Popis

Broadcast Message Gateway (BMG) je funkční entita v jádru sítě 5G (5GC), standardizovaná ve specifikaci 3GPP Release 18. Slouží jako primární vstupní bod a řídicí uzel pro doručování vysílacích a skupinových služeb od externích aplikačních funkcí ([AF](/mobilnisite/slovnik/af/)) nebo poskytovatelů obsahu do systému 3GPP. Z architektonického hlediska rozhraní BMG komunikuje s funkcí pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) pomocí servisního rozhraní Nnef, což umožňuje autorizovaným externím aplikacím vyžádat doručení vysílací zprávy. Také komunikuje s řídicí rovinou jádra sítě 5G, konkrétně spolupracuje s funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) za účelem řízení distribuce zpráv do příslušných oblastí rádiové přístupové sítě (RAN) a nakonec k cílovým uživatelským zařízením (UE).

Provozně BMG přijímá požadavky na vysílací služby, které zahrnují obsah zprávy, cílové geografické oblasti (definované pomocí sledovacích oblastí nebo identifikátorů buněk) a parametry doručení, jako je priorita a doba platnosti. BMG je zodpovědný za autorizaci těchto požadavků, přičemž může kontrolovat předplatitelská data a síťové politiky prostřednictvím interakcí s funkcí pro jednotnou správu dat ([UDM](/mobilnisite/slovnik/udm/)) a funkcí pro řízení politik ([PCF](/mobilnisite/slovnik/pcf/)). Následně orchestruje doručení tím, že vydá pokyny AMF, která následně koordinuje s RAN (gNB), aby byla zpráva vysílána přes rozhraní vzduchu pomocí mechanismů jako jsou bloky systémových informací (SIB) nebo vyhrazené skupinové/vysílací přenosy. BMG také zvládá správu životního cyklu vysílacích relací, včetně aktivace, modifikace a deaktivace.

Klíčovým technickým aspektem BMG je jeho schopnost podporovat jak službu vysílání do buněk ([CBS](/mobilnisite/slovnik/cbs/)) pro systémy veřejného varování, jako jsou varování před zemětřesením a tsunami (ETWS) a komerční mobilní výstražný systém ([CMAS](/mobilnisite/slovnik/cmas/)), tak vylepšenou multimediální vysílací a skupinovou službu (eMBMS) pro bohatší mediální obsah. Poskytuje jednotnou bránu, která abstrahuje od aplikační vrstvy podkladové mechanismy pro vysílací doručení v 5G. BMG zajišťuje spolehlivé a efektivní doručení správou síťových zdrojů, uplatňováním politik řízení zahlcení a poskytováním hlášení o stavu doručení zpět žádající aplikaci. Jeho návrh je nedílnou součástí umožnění služeb kritických pro misi ([MCS](/mobilnisite/slovnik/mcs/)) a efektivní skupinové komunikace v sítích 5G.

## K čemu slouží

BMG byl vytvořen pro potřeby standardizovaného, efektivního a sítí řízeného mechanismu pro doručování vysílacích a skupinových zpráv v sítích 5G. Před jeho zavedením byly vysílací služby, jako je vysílání do buněk, často řešeny prostřednictvím více proprietárních nebo méně integrovaných rozhraní, bez jednotné, službami řízené architektury sladěné se základními principy 5G. Vývoj směrem k samostatné síti 5G (SA) a zvýšená poptávka po službách, jako je komunikace s masivním IoT, výstražné systémy pro veřejné bezpečí a distribuce obsahu skupinám (např. pro vozidlovou komunikaci nebo aktualizace softwaru), si vyžádaly vyhrazenou funkci brány.

Primární problémy, které BMG řeší, zahrnují neefektivní doručování skupinových zpráv pomocí individuálního přenosu (unicast), které spotřebovává nadměrné síťové zdroje, a absenci bezpečného, vystaveného rozhraní pro aplikace třetích stran, aby mohly spouštět vysílání v celé síti. Poskytnutím centralizované brány umožňuje BMG škálovatelné doručování, snižuje signalizační zátěž jádra sítě a zajišťuje, že vysílací požadavky jsou řádně autorizovány a řízeny podle pravidel operátora sítě. Je klíčovým prvkem pro podporu vertikálních odvětví a služeb kritických pro misi v 5G, kde je spolehlivá skupinová komunikace s nízkou latencí nezbytná.

## Klíčové vlastnosti

- Slouží jako servisní vstupní bod (prostřednictvím NEF) pro externí požadavky na vysílací služby
- Orchestruje vysílací/skupinové doručení napříč řídicí rovinou 5GC (AMF) a RAN
- Podporuje mechanismy doručení služby vysílání do buněk (CBS) i vylepšené multimediální vysílací a skupinové služby (eMBMS)
- Provádí autorizaci, vynucování politik a řízení zahlcení pro vysílací relace
- Spravuje životní cyklus vysílací relace včetně aktivace, modifikace a deaktivace
- Poskytuje žádajícím aplikacím možnosti hlášení o stavu doručení a monitorování

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 29.538** (Rel-19) — MSGin5G Service API Specification

---

📖 **Anglický originál a plná specifikace:** [BMG na 3GPP Explorer](https://3gpp-explorer.com/glossary/bmg/)
