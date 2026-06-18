---
slug: "cpm"
url: "/mobilnisite/slovnik/cpm/"
type: "slovnik"
title: "CPM – Collective Perception Message"
date: 2026-01-01
abbr: "CPM"
fullName: "Collective Perception Message"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpm/"
summary: "CPM je standardizovaný formát zprávy pro komunikaci Vehicle-to-Everything (V2X), který umožňuje vozidlům a infrastruktuře sdílet detailní, aktuální percepční data o svém okolí získaná senzory. Je klíč"
---

CPM je standardizovaný formát zprávy pro komunikaci V2X určený k sdílení aktuálních, senzory získaných percepčních dat o okolí za účelem zvýšení situačního povědomí a podpory kooperativní automatizované mobility.

## Popis

Collective Perception Message (CPM) je základní služba v ekosystému 3GPP pro komunikaci [V2X](/mobilnisite/slovnik/v2x/), definovaná jako součást Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a později rozvíjená v rámci 5G V2X frameworku. Funguje tak, že umožňuje stanici CPM – což může být vozidlo, roadside unit ([RSU](/mobilnisite/slovnik/rsu/)) nebo zranitelný účastník provozu ([VRU](/mobilnisite/slovnik/vru/)) – generovat a vysílat zprávy obsahující objekty zachycené jejími lokálními senzory (např. LiDAR, radar, kamery). Tyto objekty jsou abstrahovány do standardizovaných datových struktur obsahujících informace jako typ objektu (vozidlo, chodec, překážka), pozice, rychlost, rozměry a úroveň spolehlivosti. Zpráva je šířena pomocí sidelink komunikace přes rozhraní PC5 (např. LTE-V2X PC5, NR V2X PC5) nebo potenciálně přes rozhraní Uu prostřednictvím mobilní sítě, což umožňuje distribuci v široké oblasti.

Z architektonického hlediska generování CPM zahrnuje entitu aplikační vrstvy uvnitř stanice CPM, která sbírá a zpracovává surová senzorová data. Tato entita filtruje a mapuje detekované objekty do kontejneru PerceptionData zprávy CPM, který obsahuje seznam vnímaných objektů a volitelně i informace o stavu vysílající stanice (jako její vlastní pozice a dynamika). Zpráva je poté předána přístupové vrstvě (Access Stratum) pro přenos přes rozhraní rádiového rozhraní. Specifikace 3GPP definují protokolový zásobník, strukturu zprávy (ASN.1 kódování) a procedury pro generování, správu a spouštění CPM, včetně podmínek jako periodický přenos nebo aktualizace spouštěné událostí na základě změn ve vnímaném prostředí.

V síti hrají CPM klíčovou roli při vytváření sdíleného percepčního obrazu. Přijímající stanice spojují data z CPM s vlastními senzorovými vstupy, čímž výrazně rozšiřují svůj percepční dosah a zlepšují přesnost detekce, zejména u skrytých nebo vzdálených objektů. Toto podporuje aplikace CCAM vyšších vrstev, jako je kooperativní vnímání, zabránění kolizím a zvýšení efektivity provozu. Služba je integrována s dalšími zprávami V2X, jako jsou Cooperative Awareness Messages ([CAM](/mobilnisite/slovnik/cam/)) a Decentralized Environmental Notification Messages ([DENM](/mobilnisite/slovnik/denm/)), ale CPM se specificky zaměřuje na přenos bohatých, senzory získaných seznamů objektů, nikoli pouze na stav vysílající entity nebo varování před událostmi.

Mezi klíčové technické komponenty patří protokolová datová jednotka CPM ([PDU](/mobilnisite/slovnik/pdu/)), správa její generační frekvence a obsahu a mechanismy pro zabezpečení a validaci zajišťující integritu a důvěryhodnost dat. Služba je navržena jako škálovatelná a efektivní, s funkcemi jako preference zařazení objektů a správa kontejnerů pro kontrolu velikosti a relevance zprávy, což umožňuje přizpůsobení se různým síťovým podmínkám a požadavkům aplikací v hustém městském prostředí nebo na dálnicích s vysokou rychlostí.

## K čemu slouží

CPM byl zaveden, aby řešil kritické omezení raných systémů [V2X](/mobilnisite/slovnik/v2x/), které se primárně spoléhaly na Cooperative Awareness Messages (CAM) a Decentralized Environmental Notification Messages (DENM). CAM vysílají vlastní stav vozidla (pozice, rychlost), zatímco DENM hlásí specifické události (např. nehody). Tyto zprávy však nepřenášejí komplexní pohled na okolní prostředí detekovaný senzory, což omezuje situační povědomí na přímou komunikaci a přímou viditelnost. Pro vysoce automatizovanou jízdu, zejména na úrovních SAE 4-5, vozidla vyžadují 360stupňové porozumění dynamickým objektům i za hranicí přímé viditelnosti, což jednotlivé senzory nemohou vždy poskytnout kvůli fyzickým překážkám, omezenému dosahu nebo selhání senzorů.

Vytvoření CPM bylo motivováno potřebou kooperativního vnímání, kde vozidla a infrastruktura společně vytvářejí sdílený model prostředí. To zvyšuje bezpečnost a efektivitu tím, že umožňuje dřívější detekci nebezpečí, lepší plánování trajektorie a zlepšený tok provozu. Historicky, před standardizací v 3GPP, existovala proprietární řešení vedoucí k fragmentaci a problémům s interoperabilitou. Standardizací CPM ve vydání 10 a jeho dalším vývojem v následujících vydáních umožnil 3GPP jednotný přístup pro automobilový průmysl, což usnadňuje globální nasazení a bezproblémovou interakci mezi systémy různých výrobců a infrastrukturou.

CPM řeší problém senzorového omezení využitím kolektivní inteligence. Umožňuje vozidlu 'vidět' prostřednictvím senzorů jiných entit, čímž efektivně násobí své percepční schopnosti. To je obzvláště důležité pro ochranu zranitelných účastníků provozu, bezpečnost na křižovatkách a složité městské scénáře, kde je viditelnost často omezena. Technologie podporuje přechod ke konektivní a automatizované mobilitě tím, že poskytuje datový základ pro pokročilé aplikace, jako je jízda v konvoji, rozšířené senzory a integrace vozidlo-síť, s konečným cílem snížit počet nehod, kongescí a emisí.

## Klíčové vlastnosti

- Standardizované ASN.1 kódování pro interoperabilní výměnu percepčních dat
- Podpora přenosu seznamů vnímaných objektů s typem, pozicí, rychlostí a metrikami spolehlivosti
- Integrace s rozhraními sidelink LTE-V2X PC5 i NR V2X pro nízkolatenční přímou komunikaci
- Mechanismy pro spouštění generování zpráv na základě periodických časovačů nebo dynamické detekce událostí
- Správa kontejnerů pro flexibilní zařazení dat o objektech a informací o vysílající stanici
- Bezpečnostní framework pro integritu a autenticitu zpráv, který zabraňuje podvržení a zajišťuje důvěryhodnost

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 23.204** (Rel-19) — SMS over generic IP access; Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.824** (Rel-10) — IP-SM-GW enhancements for CPM-SMS Interworking
- **TS 29.311** (Rel-19) — Service Level Interworking for Messaging
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study

---

📖 **Anglický originál a plná specifikace:** [CPM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpm/)
