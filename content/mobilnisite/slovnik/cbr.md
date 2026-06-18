---
slug: "cbr"
url: "/mobilnisite/slovnik/cbr/"
type: "slovnik"
title: "CBR – Channel Busy Ratio"
date: 2025-01-01
abbr: "CBR"
fullName: "Channel Busy Ratio"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbr/"
summary: "CBR je klíčová metrika představující podíl času, po který je rádiový kanál obsazený nebo vytížený, typicky měřený za definované pozorovací období. Je zásadní pro vyhodnocení využití spektra, úrovní ru"
---

CBR (Channel Busy Ratio) je podíl času, po který je rádiový kanál obsazený. Měří se za účelem vyhodnocení využití spektra, úrovně rušení a zatížení sítě pro plánování přenosů a správu kvality služeb (QoS).

## Popis

Channel Busy Ratio (CBR) je základní měření v bezdrátových komunikačních systémech, které kvantifikuje obsazenost rádiového prostředku, jako je konkrétní frekvenční kanál, časový slot nebo blok zdrojů. Je definován jako poměr času, po který je kanál detekován jako vytížený, k celkové době pozorování. Stav 'vytížený' je typicky určen porovnáním přijímaného výkonu signálu na kanálu s předdefinovanou prahovou hodnotou; pokud výkon tuto hodnotu překročí, je kanál považován za obsazený. Toto měření provádějí síťové uzly, jako je uživatelské zařízení (UE) nebo základnové stanice (např. gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v LTE), a je často specifikováno na kanál nebo na nosnou. Pozorovací okno a metodika měření jsou standardizovány, aby byla zajištěna konzistence napříč implementacemi, což umožňuje spolehlivé řízení a optimalizaci sítě.

Při provozu zahrnuje měření CBR kontinuální nebo periodické snímání rádiového prostředí. Například v LTE a 5G NR měří UE nebo základnová stanice přijímaný výkon na konfigurované sadě zdrojových prvků nebo subnosičů po konkrétní dobu, jako je podrámec nebo slot. Naměřený výkon je následně porovnán s prahovou hodnotou, která může být konfigurována sítí nebo odvozena ze standardů. Poměr vytížení se vypočítá vydělením počtu měřicích vzorků, kde výkon překročil práh, celkovým počtem vzorků. Tento proces je klíčový pro technologie využívající sdílené nebo neregulované spektrum, jako je License-Assisted Access ([LAA](/mobilnisite/slovnik/laa/)) nebo [NR-U](/mobilnisite/slovnik/nr-u/), kde je dynamické sdílení spektra a koexistence s jinými systémy (jako je Wi-Fi) zásadní.

Z architektonického hlediska slouží CBR jako vstup pro funkce správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) na vyšších vrstvách. Naměřené hodnoty CBR jsou hlášeny síti nebo použity lokálně pro autonomní rozhodování. Mezi klíčové zapojené komponenty patří obvody pro měření na fyzické vrstvě pro detekci výkonu signálu, logika vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro porovnání s prahem a výpočet poměru a protokoly řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) pro konfiguraci a hlášení. V síti jsou tyto hlášení agregovány a analyzovány inteligencí rádiové přístupové sítě (RAN) za účelem vyhodnocení zahlcení, predikce rušení a úpravy přenosových parametrů.

Role CBR v síti je mnohostranná. Slouží jako primární vstup pro dynamický přístup ke spektru, což systémům umožňuje vyhýbat se přetíženým kanálům a vybírat pro přenos čistší. Ve scénářích s agregací nosných pomáhá CBR při výběru sekundárních buněk (SCell) s příznivými podmínkami zatížení. Pro správu QoS vysoké hodnoty CBR indikují možné zhoršení latence a propustnosti, což spouští mechanismy řízení přístupu, aby zablokovaly nová připojení nebo předání spojení. Dále se v mechanismech koexistence, jako jsou ty definované pro 5G NR v neregulovaných pásmech (NR-U), používá CBR k implementaci naslouchání před vysíláním ([LBT](/mobilnisite/slovnik/lbt/)) a adaptivnímu výběru kanálu, čímž se zajišťuje spravedlivé sdílení s přítomnými systémy, jako je Wi-Fi a další mobilní operátoři.

## K čemu slouží

CBR bylo zavedeno, aby řešilo rostoucí potřebu efektivního využití spektra a řízení rušení v čím dál přetíženějších bezdrátových prostředích. Jak se celulární sítě vyvíjely z nasazení na vyhrazeném, regulovaném spektru tak, aby zahrnovaly i sdílená a neregulovaná pásma, tradiční statické plánování frekvencí se stalo nedostatečným. Původní motivací v raných vydáních 3GPP (jako [R99](/mobilnisite/slovnik/r99/)) bylo poskytnout standardizovanou metriku pro síťové operátory, aby mohli sledovat obsazenost a zatížení kanálů, což umožnilo základní správu provozu a plánování kapacity. S příchodem technologií jako LTE-U, LAA a 5G NR-U se však účel rozšířil o usnadnění dynamického sdílení spektra, kde zařízení musí snímat a přizpůsobovat se podmínkám kanálu v reálném čase, aby koexistovala s jinými rádiovými přístupovými technologiemi (RAT) a splňovala regulatorní požadavky, například pro použití neregulovaného spektra.

Historicky předchozí přístupy spoléhaly na pevné přiřazení kanálů nebo zjednodušené indikátory zatížení, jako je počet připojených uživatelů, které přesně neodrážely skutečné prostředí rádiového (RF) rušení. Tyto metody často vedly k neoptimálnímu využití spektra, zvýšené míře kolizí a zhoršenému uživatelskému zážitku v hustých nasazeních. CBR poskytuje přímé měření aktivity kanálu na fyzické vrstvě, které zachycuje jak zamýšlené přenosy, tak vnější rušení. To umožňuje inteligentnější přidělování prostředků, snižuje pravděpodobnost kolizí paketů a zlepšuje celkovou propustnost a spolehlivost systému. Vytvoření CBR bylo motivováno omezeními předchozích metrik zatížení, které nezohledňovaly časovou a prostorovou variabilitu rušení, zejména v heterogenních sítích a scénářích s více operátory.

## Klíčové vlastnosti

- Kvantifikuje obsazenost kanálu jako poměr času vytížení k celkové době pozorování
- Používá konfigurovatelnou prahovou hodnotu výkonu k určení stavu 'vytížený'
- Podporuje měření a hlášení jak ze strany UE, tak síťových uzlů (např. gNB)
- Zásadní pro dynamický přístup ke spektru a výběr kanálu ve sdílených pásmech
- Integruje se se správou rádiových prostředků (RRM) pro řízení přístupu, plánování a zmírňování rušení
- Standardizováno napříč vydáními 3GPP pro konzistentní implementaci v LTE a 5G NR

## Související pojmy

- [LBT – Listen Before Talk](/mobilnisite/slovnik/lbt/)
- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.881** (Rel-15) — MBMS FEC for Mission Critical Services Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [CBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbr/)
