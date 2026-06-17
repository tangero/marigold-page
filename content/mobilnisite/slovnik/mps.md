---
slug: "mps"
url: "/mobilnisite/slovnik/mps/"
type: "slovnik"
title: "MPS – Multimedia Priority Service"
date: 2026-01-01
abbr: "MPS"
fullName: "Multimedia Priority Service"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mps/"
summary: "Standardizovaná služba zajišťující prioritní zpracování multimediálních relací (např. hlas, video) pro oprávněné uživatele při přetížení sítě. Je klíčová pro veřejnou bezpečnost, národní bezpečnost a"
---

MPS je standardizovaná služba, která zajišťuje prioritní zpracování multimediálních relací pro oprávněné uživatele při přetížení sítě, čímž garantuje kritickou komunikaci pro veřejnou bezpečnost a zásahové složky.

## Popis

Multimedia Priority Service (MPS) je služba definovaná 3GPP, která poskytuje zvýhodněné zacházení s multimediálními relacemi iniciovanými oprávněnými uživateli, jako jsou vládní úředníci, záchranáři a personál kritické infrastruktury. Její architektura je integrována do funkcí jádra sítě, především do rámce Policy and Charging Control (PCC). Když uživatel s předplatným MPS zahájí relaci, síť požadavek identifikuje pomocí předplatitelských dat a uplatní prioritní politiky. Mezi klíčové součásti patří Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro ukládání profilů předplatného MPS, Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro autorizaci a vynucování prioritních politik a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G (nebo PGW v 4G) pro implementaci těchto politik během zřizování relace a správy přenosových cest.

MPS funguje tak, že označí služební požadavek specifickou hodnotou Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)) a identifikátorem třídy kvality služby Quality of Service (QoS) Class Identifier ([QCI](/mobilnisite/slovnik/qci/)), které indikují vysokou prioritu. Při přetížení sítě mohou být relace s nižší prioritou vytlačeny nebo blokovány, aby byly prostředky k dispozici pro relace MPS. PCF hraje ústřední roli tím, že určuje autorizovanou úroveň priority na základě uživatelského profilu a síťových podmínek a tuto informaci předává SMF a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). UPF pak uplatňuje odpovídající způsob přeposílání paketů, čímž zajišťuje nízkou latenci a garantovanou šířku pásma pro prioritní mediální toky.

V rádiové přístupové síti MPS ovlivňuje Radio Resource Management (RRM). Základnová stanice (gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v 4G) přijme parametry QoS pro prioritní přenosovou cestu a podle toho plánuje rádiové prostředky, dávající přednost provozu MPS před neprioritním provozem. Toto komplexní prioritní zpracování se rozprostírá od uživatelského zařízení přes RAN a jádro sítě až k cíli, který může být ve stejné síti nebo v partnerské síti prostřednictvím propojení. MPS je definována jak pro služby založené na IP Multimedia Subsystem (IMS), jako je Voice over LTE (VoLTE), tak pro služby mimo IMS, což zajišťuje širokou použitelnost pro kritickou komunikaci.

## K čemu slouží

MPS byla vytvořena, aby řešila kritickou potřebu spolehlivé komunikace pro oprávněný personál během mimořádných událostí, katastrof nebo při přetížení sítě. Tradiční sítě s principem "nejlepšího úsilí" nemohou garantovat dostupnost služby při náhlém nárůstu poptávky, což může bránit práci zásahových složek a operacím národní bezpečnosti. Služba zajišťuje, že životně důležitá komunikace od vládních, vojenských a bezpečnostních uživatelů je zachována, i když jsou veřejné sítě přetížené, což je běžný scénář během přírodních katastrof nebo velkých veřejných akcí.

Historicky existovaly prioritní služby pro přepojování okruhů hlasu (např. Government Emergency Telecommunications Service), ale s migrací na plně IP sítě, jako jsou LTE a 5G, se stala nezbytnou standardizovaná metoda pro upřednostňování multimediálních relací (včetně hlasu, videa a dat). 3GPP zavedlo MPS, aby poskytlo konzistentní, interoperabilní rámec napříč operátory a hranicemi. Řeší problém degradace nebo odmítnutí služby pro kritické uživatele definováním standardizovaného profilu a síťových procedur, které nařizují prioritní zacházení napříč všemi síťovými vrstvami, od plánování rádiových prostředků až po přidělování prostředků v jádru sítě.

Motivace přesahuje rámec národní bezpečnosti a zahrnuje i základní služby, jako je zdravotnictví, energetika a doprava během krizí. Formalizací MPS ve specifikacích 3GPP je umožněno globální roamování pro prioritní uživatele a zajištěno, že síťová zařízení od různých výrobců mohou spolupracovat na podpoře této služby. Tato standardizace je klíčová pro přeshraniční spolupráci při mimořádných událostech a pro poskytování předvídatelné kvality služby oprávněným subjektům za jakýchkoli síťových podmínek.

## Klíčové vlastnosti

- Komplexní prioritní zpracování pro IMS i ne-IMS multimediální relace
- Integrace s architekturou Policy and Charging Control (PCC) pro dynamické vynucování politik
- Využití standardizovaných parametrů QoS (ARP, QCI/5QI) pro signalizaci priority
- Podpora vytlačování relací a rezervace prostředků při přetížení
- Možnost roamingu pro prioritní uživatele napříč různými síťovými operátory
- Autorizace založená na předplatitelských datech uložených v HSS/UDM

## Definující specifikace

- **TS 22.153** (Rel-20) — Multimedia Priority Service (MPS) requirements
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TR 22.854** (Rel-17) — Feasibility Study on Multimedia Priority Service - Phase 2
- **TR 22.862** (Rel-14) — Critical Communications Feasibility Study
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.216** (Rel-19) — SRVCC Architecture Enhancements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- … a dalších 30 specifikací

---

📖 **Anglický originál a plná specifikace:** [MPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mps/)
