---
slug: "upe"
url: "/mobilnisite/slovnik/upe/"
type: "slovnik"
title: "UPE – User Plane Entity"
date: 2025-01-01
abbr: "UPE"
fullName: "User Plane Entity"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/upe/"
summary: "Logická síťová funkce definovaná v raných studiích systémové architektury LTE (SAE) odpovědná za zpracování a přeposílání datového provozu uživatele. Představovala bránu uživatelské roviny v Evolved P"
---

UPE je logická entita uživatelské roviny (User Plane Entity) v rané architektuře LTE/SAE odpovědná za zpracování a přeposílání datového provozu uživatele v rámci Evolved Packet Core.

## Popis

Entita uživatelské roviny (User Plane Entity, UPE) byl koncept architektury jádra sítě představený během práce 3GPP na vývoji systémové architektury ([SAE](/mobilnisite/slovnik/sae/)) pro Long-Term Evolution (LTE). Byla definována jako logický uzel odpovědný za veškeré zpracování v uživatelské rovině (datový provoz) související s uživatelským zařízením (UE) v rámci Evolved Packet System (EPS). Primární rolí UPE bylo sloužit jako brána mezi LTE rádiovou přístupovou sítí ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a externími paketovými datovými sítěmi ([PDN](/mobilnisite/slovnik/pdn/)), jako je internet nebo služby IMS. Z architektonického hlediska byla koncipována tak, aby kombinovala funkce kotvy mobility a směrování/přeposílání paketů. Udržovala kontext nosiče (bearer context) pro UE, který zahrnoval parametry jako úrovně QoS a paketové filtry, a byla odpovědná za uplatňování odpovídajících politik přeposílání paketů.

Během provozu UPE přijímala datové pakety uživatele od eNodeB přes rozhraní [S1-U](/mobilnisite/slovnik/s1-u/). Tyto pakety následně kontrolovala, porovnávala je s nastavenými kontexty nosičů a aplikovala potřebné zacházení z hlediska QoS (např. plánování, označování) před jejich přeposláním k cílové PDN přes rozhraní SGi. V opačném směru přijímala pakety z PDN, určovala správný nosič a přidružený eNodeB pro cílové UE a pakety podle toho přeposílala. Klíčovým aspektem její funkce bylo působení jako kotva mobility pro předávání spojení mezi eNodeB v rámci LTE; cesta v uživatelské rovině se přepínala mezi eNodeB, zatímco koncový bod UPE zůstával stabilní, což zajišťovalo plynulou kontinuitu dat.

UPE byla ústřední součástí rané, zploštělé all-IP architektury EPC, navržené ke snížení latence a zlepšení efektivity ve srovnání s jádrem 3G UMTS. Jak však práce na SAE pokračovaly, došlo k upřesnění funkční dekompozice. Povinnosti původně seskupené pod UPE byly později rozděleny do dvou samostatných, fyzicky nasaditelných síťových funkcí: Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). SGW převzala roli lokální kotvy mobility a propojení s eNodeB, zatímco PGW se stala konečným bodem kotvy pro mobilitu UE a rozhraním k externím sítím. UPE tedy zůstává důležitým historickým konceptem, který ilustruje proces architektonického návrhu vedoucí ke konečné podobě LTE EPC.

## K čemu slouží

UPE byla koncipována, aby řešila omezení architektury jádra sítě 3G UMTS, která byla často vnímána jako složitá a hierarchická, se samostatnými doménami pro přepojování okruhů a přepojování paketů. Primární motivací pro [SAE](/mobilnisite/slovnik/sae/) a koncept UPE bylo definovat zjednodušené, vysoce výkonné, all-IP jádro sítě optimalizované pro paketová data, aby podpořilo vysokorychlostní a nízkolatentní možnosti LTE rádiové technologie. Cílem bylo řešit problémy jako latence sítě, náklady na vlastnictví a škálovatelnost pro explozivní nárůst mobilních širokopásmových dat.

Historický kontext představuje přechod v polovině let 2000 od 3G zaměřeného na hlas k 4G zaměřenému na data. Předchozí přístupy, jako GGSN a [SGSN](/mobilnisite/slovnik/sgsn/) v UMTS, zahrnovaly více tunelovacích protokolů a síťových vrstev, což přidávalo režii zpracování a latenci. UPE představovala koncept čistého štítu (clean-slate) pro zploštění architektury a snížení počtu síťových skoků pro data uživatele. Cílem bylo vytvořit jedinou, výkonnou entitu uživatelské roviny, která by mohla efektivně zvládat směrování paketů, vynucování politik a mobilitu, čímž by zjednodušila nasazení a provoz sítě. Její vytvoření bylo hnací silou potřeby architektury, která by se mohla lineárně škálovat s datovým provozem při zachování přísných požadavků QoS pro vznikající služby, jako je video a hraní her v reálném čase.

## Klíčové vlastnosti

- Logická agregace funkcí brány uživatelské roviny
- Bod kotvy mobility pro předávání spojení v rámci LTE (intra-LTE handover)
- Směrování a přeposílání paketů mezi E-UTRAN a PDN
- Vynucování QoS na základě kontextů nosičů (bearer contexts)
- Ukončování rozhraní pro referenční body S1-U a SGi
- Evoluční předchůdce rozdělení na SGW a PGW

## Související pojmy

- [SAE – System Architecture Evolution](/mobilnisite/slovnik/sae/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [S1-U – S1 User Plane Interface](/mobilnisite/slovnik/s1-u/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.424** (Rel-19) — X2 Interface User Plane Transport Protocols

---

📖 **Anglický originál a plná specifikace:** [UPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/upe/)
