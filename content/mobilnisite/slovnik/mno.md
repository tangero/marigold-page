---
slug: "mno"
url: "/mobilnisite/slovnik/mno/"
type: "slovnik"
title: "MNO – Mobile Network Operator"
date: 2026-01-01
abbr: "MNO"
fullName: "Mobile Network Operator"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mno/"
summary: "Licencovaná společnost, která poskytuje služby bezdrátové komunikace účastníkům využívající rádiové spektrum a síťovou infrastrukturu. MNO vlastní nebo kontroluje všechny prvky sítě, od rádiového přís"
---

MNO (mobilní síťový operátor) je licencovaná společnost, která poskytuje služby bezdrátové komunikace využívající vlastní rádiové spektrum a síťovou infrastrukturu, od rádiového přístupu po jádro sítě, pod vlastní značkou.

## Popis

Mobile Network Operator (MNO) je primární obchodní a technická entita v ekosystému mobilních telekomunikací. Technicky MNO disponuje vládou udělenou licencí na využívání konkrétního rádiového kmitočtového spektra a provozuje kompletní koncové síťové infrastruktury. Tato infrastruktura je definována architekturami 3GPP a typicky zahrnuje rádiovou přístupovou síť (RAN) s základnovými stanicemi (NodeBs, eNodeBs, gNBs), jádrovou síť (vyvíjející se od jader GSM/UMTS k 5G Core) a přenosovou síť, která je propojuje. MNO je zodpovědné za nasazení, provoz, údržbu a vývoj této celé infrastruktury.

Z architektonické a provozní perspektivy MNO implementuje specifikace 3GPP pro poskytování služeb. To zahrnuje správu identit účastníků (prostřednictvím [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/)), vytváření přenosových cest pro uživatelská data, vynucování politik (prostřednictvím [PCRF](/mobilnisite/slovnik/pcrf/)/[PCF](/mobilnisite/slovnik/pcf/)) a zajišťování správy mobility a relací. MNO provozuje Domovskou síť pro své účastníky, která obsahuje hlavní databázi účastníků a je zodpovědná za jejich autentizaci, i když se účastník nachází v roamingu. Když účastník roamuje, navštívená síť MNO komunikuje se sítí domovského MNO, aby službu poskytla. MNO také integruje s externími sítěmi, jako je telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) a internet.

Mimo základní konektivitu role MNO zahrnuje poskytování služeb, včetně hlasových služeb, [SMS](/mobilnisite/slovnik/sms/) a datových služeb, stejně jako pokročilejší nabídky, jako je konektivita pro IoT, síťové řezy (network slicing) a edge computing v éře 5G. MNO spravuje kvalitu služeb (QoS), zabezpečení a účtování za tyto služby. V moderních architekturách se koncept MNO rozšířil o role jako poskytovatel Neutral Host nebo facilitátor pro Mobile Virtual Network Operators ([MVNO](/mobilnisite/slovnik/mvno/)), kteří si kapacitu od MNO pronajímají. Referenční technické specifikace (např. týkající se požadavků na služby, managementu a zabezpečení) definují schopnosti a odpovědnosti, které se od MNO v systému 3GPP očekávají.

## K čemu slouží

Koncept MNO je základním kamenem buněčného obchodního modelu, vytváří regulovanou entitu odpovědnou za spolehlivé veřejné telekomunikace. Historicky, před buněčnými sítěmi, byly telekomunikace poskytovány státními monopoly přes pevné sítě. Model MNO, začínající s 1G analogovými systémy, zavedl konkurenci tím, že licencoval spektrum více soukromým subjektům ke stavbě a provozu bezdrátových sítí. To pohánělo inovace, zlepšovalo kvalitu služeb a rozšiřovalo pokrytí.

Standardy 3GPP poskytují technický rámec, který umožňuje MNO stavět interoperabilní sítě. Tato standardizace řeší problém závislosti na jediném dodavateli a umožňuje globální roaming – účastník jednoho MNO může používat síť jiného MNO (roamingového partnera), protože obě implementují stejné specifikace. MNO je motivováno investovat do infrastruktury, aby získávalo a udržovalo účastníky, a specifikace 3GPP se vyvíjejí (k 4G, 5G), aby řešily potřeby MNO pro vyšší efektivitu, nové zdroje příjmů (IoT, slicing) a nižší cenu za bit.

## Klíčové vlastnosti

- Vlastní licencované rádiové spektrum od národního regulátora
- Vlastní a provozuje kompletní infrastrukturu RAN a jádrové sítě
- Poskytuje veřejné telekomunikační služby pod vlastní značkou
- Spravuje životní cyklus účastníka, účtování a zákaznickou podporu
- Implementuje standardy 3GPP pro interoperabilitu a roaming
- Vystupuje jako Domovská síť pro své účastníky, což umožňuje globální autentizaci

## Související pojmy

- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 22.368** (Rel-19) — Network Improvements for Machine Type Communications
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 22.809** (Rel-11) — Interworking between 3GPP networks and Enterprise voice
- **TR 22.815** (Rel-14) — Study on Multimedia Broadcast Supplement for PWS
- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TR 22.988** (Rel-19) — Study on MTC Numbering Alternatives
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- … a dalších 31 specifikací

---

📖 **Anglický originál a plná specifikace:** [MNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mno/)
