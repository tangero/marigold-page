---
slug: "cfr"
url: "/mobilnisite/slovnik/cfr/"
type: "slovnik"
title: "CFR – Code of Federal Regulations"
date: 2025-01-01
abbr: "CFR"
fullName: "Code of Federal Regulations"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cfr/"
summary: "Code of Federal Regulations (CFR) je kodifikace obecných a trvalých pravidel publikovaných ve Federálním registru výkonnými odděleními a agenturami federální vlády USA. V kontextu 3GPP se na něj odkaz"
---

CFR je kodifikace federálních předpisů USA, na kterou se odkazuje 3GPP při definování regulatorních požadavků pro shodu spektra a rádiových zařízení ve Spojených státech.

## Popis

Code of Federal Regulations (CFR) není technickou specifikací 3GPP, nýbrž kritickým externím regulatorním rámcem. Jedná se o kodifikované souhrny všech pravidel a předpisů stanovených agenturami federální vlády USA. Pro telekomunikace je nejdůležitější Titul 47 (Telekomunikace), který spravuje Federální komunikační komise ([FCC](/mobilnisite/slovnik/fcc/)). CFR obsahuje právně závazná pravidla upravující využívání rádiového frekvenčního spektra, schvalování zařízení, licencování a provozní požadavky pro všechny rádiové služby, včetně mobilních sítí jako 5G NR a LTE.

Ve specifikacích 3GPP se na CFR odkazuje (např. v 36.791, 38.877), aby se technické standardy sladily s regulatorními požadavky USA. Například 3GPP definuje technické parametry pro rádiový přenos, jako jsou maximální výkonové úrovně, nežádoucí emise mimo pásmo a parazitní emise, které musí splňovat limity stanovené v příslušných částech CFR, jako je Část 22 (Cellular), Část 24 (Personal Communications Services), Část 27 (Miscellaneous Wireless Communications Services) a Část 30 (Upper Microwave Flexible Use Service). Tím je zajištěno, že zařízení vyrobená podle standardů 3GPP mohou být legálně certifikována a provozována na americkém trhu.

Vztah je architektonický v tom smyslu, že specifikace 3GPP pro rádiový přístupový síť (RAN) a uživatelské zařízení (UE) obsahují normativní odkazy a body shody vázané na pravidla CFR. Například řada 3GPP TS 38.101 o rádiovém vysílání a příjmu UE definuje kmitočtová pásma a související požadavky. Pro pásma přidělená pro použití v USA jsou technické požadavky vytvořeny tak, aby byly v souladu s ustanoveními CFR pro tato pásma. To zahrnuje detailní rádiovou (RF) zkoušku shody, která je částečně definována 3GPP a částečně ověřována vůči pravidlům CFR během procesů certifikace zařízení FCC, jako jsou certifikace FCC Část 2, 22, 24 nebo 27.

Jeho role je zásadní pro přístup na trh. Žádné zařízení nebo síťové vybavení založené na 3GPP nemůže být komerčně nasazeno ve Spojených státech bez prokázání shody s příslušnými oddíly CFR. Proto pracovní skupiny 3GPP, zejména RAN4 (Radio Performance and Protocol Aspects), pečlivě sledují a začleňují tato regulatorní omezení do technických standardů. Tím je zajištěno, že globální standardy lze přizpůsobit tak, aby splňovaly regionální právní požadavky, což usnadňuje mezinárodní roaming a interoperabilitu zařízení při respektování národní suverenity nad správou spektra.

## K čemu slouží

Účelem odkazování na CFR ve specifikacích 3GPP je zajistit, aby technické standardy pro mobilní technologie byly právně způsobilé pro provoz ve Spojených státech. 3GPP vyvíjí globální technické standardy, ale každá země nebo region má svůj vlastní regulatorní orgán a právní rámec upravující využívání spektra. V USA tato pravidla stanovuje [FCC](/mobilnisite/slovnik/fcc/) v CFR. Bez tohoto sladění by zařízení vyrobená podle čistých specifikací 3GPP nemusela být legální pro prodej nebo použití v USA, což by vedlo k fragmentaci trhu a zvýšeným nákladům pro výrobce, kteří by museli vyvíjet regionálně specifické varianty.

Historicky, jak se mobilní technologie vyvíjely od 2G k 5G, rostla potřeba explicitního regulatorního sladění. Rané standardy často předpokládaly harmonizované globální spektrum, ale realita ukázala odlišná národní přidělení a pravidla. Zařazení odkazů na CFR, zejména od verze Rel-15 s příchodem 5G NR a nových kmitočtových pásem (včetně pásem mmWave jako 28 GHz, 39 GHz, která podléhají pravidlům FCC v Části 30), se stalo nezbytným. Tím se řeší omezení předchozích přístupů, kdy se shoda předpokládala nebo byla řešena čistě regionálními zkušebními orgány po standardizaci, což mohlo vést k pozdním změnám návrhu.

Proaktivním odkazováním na CFR umožňuje 3GPP efektivnější proces certifikace a nasazení. Poskytuje jasné vodítko výrobcům zařízení o regulatorních mezích, v jejichž rámci musí navrhovat, čímž snižuje riziko a čas uvedení na trh. To je zvláště kritické pro nová spektra a technologie, jako je License Assisted Access ([LAA](/mobilnisite/slovnik/laa/)) v LTE nebo [NR-U](/mobilnisite/slovnik/nr-u/) (NR v nelicencovaném spektru), kde provoz musí koexistovat pod striktními pravidly FCC Část 15 pro nelicencovaná zařízení. CFR tedy slouží jako kritický vstup, který zajišťuje, že standardy 3GPP jsou nejen technicky kvalitní, ale také komerčně životaschopné na významném globálním trhu.

## Klíčové vlastnosti

- Definuje právně vymahatelná pravidla pro využívání rádiového spektra ve Spojených státech
- Stanovuje technické limity pro výkon vysílače, nežádoucí emise a frekvenční stabilitu
- Ustavuje postupy schvalování zařízení (např. certifikace FCC)
- Obsahuje provozní pravidla pro licencované i nelicencované služby
- Ukládá specifické provozní požadavky pro různé rádiové služby
- Aktualizuje se ročně, aby odrážela nové politiky a technologický pokrok

## Související pojmy

- [FCC – Federal Communications Commission](/mobilnisite/slovnik/fcc/)

## Definující specifikace

- **TS 22.820** (Rel-15) — Restricted Local Operator Services for Unauthenticated UEs
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [CFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfr/)
