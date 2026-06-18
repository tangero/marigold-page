---
slug: "pti"
url: "/mobilnisite/slovnik/pti/"
type: "slovnik"
title: "PTI – Procedure Transaction Identity"
date: 2025-01-01
abbr: "PTI"
fullName: "Procedure Transaction Identity"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pti/"
summary: "Jedinečný identifikátor používaný ve signalizačních protokolech ke korelaci zpráv náležejících k téže transakci nebo proceduře. Je nezbytný pro správu souběžných signalizačních výměn mezi síťovými ent"
---

PTI je jedinečný identifikátor používaný ke korelaci zpráv v rámci stejné signalizační transakce mezi síťovými entitami, což umožňuje správu souběžných procedur.

## Popis

Procedure Transaction Identity (PTI) je základním prvkem signalizačních protokolů 3GPP, zejména v rámci Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a některých procedur Access Stratum ([AS](/mobilnisite/slovnik/as/)). Slouží jako lokální identifikátor, přidělený při zahájení transakce, který jednoznačně označuje všechny následné zprávy vyměněné pro danou konkrétní proceduru mezi dvěma partnerskými entitami, jako je User Equipment (UE) a core network. To umožňuje paralelní zpracování více současných signalizačních transakcí (např. více procedur správy relací nebo správy mobility) bez záměny. PTI je zahrnuto v hlavičce protokolu příslušných zpráv, což umožňuje přijímající entitě správně přiřadit příchozí zprávu příslušnému probíhajícímu kontextu procedury a stavovému automatu.

Z architektonického hlediska PTI funguje v rámci protokolů řídicí roviny definovaných ve specifikacích jako 24.301 (NAS pro EPS) a 24.501 (NAS pro 5GS). Je to kritická součást pro procedury správy relací, jako je zřizování nebo modifikace Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) session. Když UE iniciuje proceduru, vybere nepoužitou hodnotu PTI a zahrne ji do počáteční požadovací zprávy. Síť tuto stejnou hodnotu PTI opakuje ve svých odpovědních zprávách. Toto párování zajišťuje, že i pokud zprávy z různých transakcí dorazí neuspořádaně nebo promíchaně, každá entita je dokáže správně demultiplexovat. Prostor hodnot PTI spravuje lokálně entita iniciující transakci; nejedná se o globálně jedinečný identifikátor, ale je jedinečný po dobu trvání transakce mezi dvěma komunikujícími partnery.

Role PTI sahá až k zajištění spolehlivé signalizace a prevenci poškození stavů. Poskytnutím jasné korelační značky podporuje složité procedury zahrnující více výměn zpráv, jako jsou handovery nebo vyjednávání kvality služeb (QoS). V rádiové přístupové síti specifikace jako 36.321 (LTE [MAC](/mobilnisite/slovnik/mac/)) také využívají podobné koncepty identifikátorů transakcí pro některé procedury MAC vrstvy, což zdůrazňuje jeho důležitost napříč různými protokolovými vrstvami. Bez mechanismu jako je PTI by správa souběžné signalizace vyžadovala složitější sekvencování nebo serializaci, což by zvyšovalo latenci a riziko chyb. Jeho jednoduchost a účinnost z něj činí základní kámen robustní signalizační architektury 3GPP.

## K čemu slouží

PTI bylo zavedeno, aby vyřešilo základní problém správy více současných signalizačních transakcí mezi síťovými entitami. V raných mobilních systémech byly signalizační procedury často jednodušší nebo více serializované, ale jak se sítě vyvíjely pro podporu složitých služeb, staly se souběžné procedury nezbytnými. Například UE může potřebovat aktivovat datovou relaci a současně provádět aktualizaci polohy nebo přijímat [SMS](/mobilnisite/slovnik/sms/). Bez identifikátoru transakce by korelace požadavků a odpovědí v takových scénářích byla náchylná k chybám, což by vedlo k selhání protokolu nebo nesprávně aplikovaným operacím.

Jeho vznik byl motivován potřebou efektivní a spolehlivé správy stavových automatů v rámci spojově orientovaných signalizačních protokolů. Předchozí přístupy mohly spoléhat na implicitní sekvencování nebo vyhrazené fyzické kanály, které nebyly škálovatelné pro paketově přepínané, IP-based core networky, jaké jsou definovány od 3GPP Release 8 (EPS) dále. PTI poskytuje odlehčené řešení v pásmu, které přidává minimální režii zprávám a zároveň umožňuje jasnou izolaci transakcí. To je obzvláště kritické ve vrstvě [NAS](/mobilnisite/slovnik/nas/), kde si UE a core network musí udržovat synchronizovaný pohled na více probíhajících procedur, jako je správa [PDU](/mobilnisite/slovnik/pdu/) session, přidělování prostředků beareru a události správy mobility.

Historicky koncept čerpá z identifikátorů transakcí používaných v jiných telekomunikačních a datových síťových protokolech. Jeho standardizace v rámci 3GPP zajistila interoperabilitu napříč dodavateli a nasazeními sítí. Tím, že řeší omezení nejednoznačného přiřazování zpráv, PTI zvyšuje spolehlivost sítě, podporuje pokročilé funkce jako network slicing a QoS flows a tvoří základ bezproblémového uživatelského zážitku očekávaného v moderních sítích 4G a 5G. Řeší problém souběžnosti v signalizaci, což je předpoklad pro vysokovýkonné, multiservisní schopnosti současných mobilních systémů.

## Klíčové vlastnosti

- Jedinečný lokální identifikátor pro korelaci zpráv v rámci jedné signalizační transakce
- Umožňuje souběžné provádění více NAS a AS procedur
- Obsaženo v hlavičkách protokolů zpráv řídicí roviny (např. zprávy Session Management)
- Přiděluje iniciátor transakce (UE nebo síť)
- Nezbytné pro správnou činnost stavového automatu v UE a síťových entitách
- Podporováno napříč více releasy a technologiemi 3GPP (EPS, 5GS)

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pti/)
