---
slug: "cpch"
url: "/mobilnisite/slovnik/cpch/"
type: "slovnik"
title: "CPCH – Common Packet Channel"
date: 2025-01-01
abbr: "CPCH"
fullName: "Common Packet Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpch/"
summary: "Common Packet Channel (CPCH) je transportní kanál pro uplink v UMTS (UTRA-FDD) navržený pro trhavý přenos paketů s nízkou až střední datovou rychlostí z uživatelského zařízení (UE) do sítě. Funguje v"
---

CPCH je transportní kanál pro uplink v UMTS navržený pro efektivní, konkurující přenos paketů z uživatelského zařízení do sítě, primárně pro trhavý datový provoz.

## Popis

Common Packet Channel (CPCH) je klíčový transportní kanál pro uplink v rádiovém rozhraní UMTS (Universal Mobile Telecommunications System), konkrétně definovaný pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)) v [UTRA](/mobilnisite/slovnik/utra/) (UMTS Terrestrial Radio Access). Funguje jako sdílený, konkurující kanál optimalizovaný pro přenos paketových dat z uživatelského zařízení (UE) k Node B (základnové stanici). Na rozdíl od vyhrazených kanálů, které přidělují pevné prostředky jednomu UE, umožňuje CPCH více UE soutěžit o přístup, což jej činí vhodným pro aplikace s trhavými a přerušovanými datovými toky, jako je prohlížení webu, instant messaging nebo nahrávání malých souborů. Kanál funguje v rámci fyzické vrstvy [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) a využívá specifické kódy pro rozprostření spektra a časové struktury pro správu uplinkových přenosů.

Architektonicky je CPCH integrován do protokolů vrstvy 2 a 3 rádiového rozhraní UMTS a rozhraní s podsoubory Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)). Kanál využívá přístupový mechanismus založený na slotted ALOHA kombinovaný s procedurami rychlé indikace zachycení a řízení výkonu pro zvládnutí konkurujících přístupů a minimalizaci kolizí. Když má UE data k odeslání, zahájí proceduru přístupu CPCH vysláním krátkého přístupového preambule na určeném přístupovém slotu, po němž následuje preambule pro detekci kolizí. Node B odpoví na Acquisition Indicator Channel ([AICH](/mobilnisite/slovnik/aich/)) pro potvrzení úspěšné detekce preambule, načež UE vysílá preambuli pro řízení výkonu, aby navázalo uzavřenou smyčku řízení výkonu před odesláním vlastního datového paketu. Tento vícestupňový proces zajišťuje spolehlivý uplinkový přenos při současném řízení interference ve sdíleném rádiovém prostředí.

Klíčovými součástmi CPCH jsou CPCH Status Indicator Channel ([CSICH](/mobilnisite/slovnik/csich/)), který vysílá informace o dostupnosti prostředků CPCH z Node B k UE, a CPCH Control Channel (CCCH), používaný pro přenos řídicích informací během přístupové fáze. Kanál podporuje proměnné datové rychlosti, typicky až několik set kilobitů za sekundu, a zahrnuje funkce jako rychlé řízení výkonu, vnitřní smyčka řízení výkonu a volitelný site selection diversity transmission (SSDT) pro zvýšený výkon. CPCH funguje ve spojení s downlinkovými vyhrazenými kanály pro přenos příkazů řízení výkonu a potvrzení, čímž zajišťuje obousměrnou koordinaci. Jeho návrh klade důraz na nízkou latenci a efektivní využití prostředků, což z něj činí základní prvek pro uplinkové paketové služby v raných sítích 3G, ačkoli byl později nahrazen pokročilejšími technologiemi, jako je Enhanced Uplink (HSUPA) v pozdějších verzích UMTS.

## K čemu slouží

CPCH byl zaveden v UMTS Release 99, aby řešil omezení stávajících uplinkových kanálů pro přenos paketových dat, zejména Random Access Channel (RACH). RACH, ačkoli vhodný pro malé řídicí zprávy a počáteční přístup, byl pro trhavý datový provoz neefektivní kvůli své konkurující povaze bez rychlého řízení výkonu nebo mechanismů řešení kolizí, což vedlo k vyšší latenci a ztrátě paketů. Růst služeb mobilního internetu na konci 90. let 20. století vyžadoval robustnější uplinkové řešení pro aplikace jako e-mail, webová nahrávání a interaktivní služby, které potřebovaly lepší propustnost a spolehlivost, než mohl RACH poskytnout. CPCH byl navržen, aby tuto mezeru zaplnil tím, že nabídl sdílený, konkurující kanál s vylepšenými funkcemi pro paketově orientovanou komunikaci.

Vytvoření CPCH bylo motivováno potřebou optimalizovat využití rádiových prostředků v sítích UMTS a snížit režii spojenou s vyhrazenými kanály pro sporadické přenosy dat. Vyhrazené kanály, ačkoli nabízely garantovanou kvalitu služeb, způsobovaly významnou signalizační režii a plýtvání prostředky při použití pro přerušovaný provoz, protože vyžadovaly nepřetržité přidělování i během nečinných období. CPCH poskytl střední cestu, umožňující dynamické sdílení uplinkových prostředků mezi více UE bez trvalého přidělení, čímž zlepšil spektrální účinnost a podporoval větší počet uživatelů s nízkou datovou rychlostí. Tento přístup byl v souladu s vizí 3GPP pro efektivní paketově spínané služby a umožnil nákladově efektivní nasazení raných mobilních datových aplikací.

Historicky CPCH představoval evoluční krok v návrhu uplinkových kanálů, který překlenul mezeru mezi čistě konkurujícím přístupem a vyhrazeným přidělováním prostředků. Řešil specifické výzvy v systémech UMTS FDD, jako je interference blízko-daleko a řízení výkonu ve sdíleném prostředí, začleněním mechanismů rychlého zachycení a řízení výkonu. Jeho složitost a omezené přijetí v komerčních sítích však vedly k jeho postupnému vyřazení ve prospěch pokročilejších vylepšení uplinku, jako je HSUPA, která nabízela vyšší datové rychlosti a lepší efektivitu plánování. Přesto zůstává CPCH pozoruhodným příkladem snah 3GPP inovovat přístup k uplinkovým paketům během přechodu od okruhově spínaných k paketově spínaným mobilním sítím.

## Klíčové vlastnosti

- Konkurující přístup pro uplink pro více UE
- Rychlá indikace zachycení přes AICH pro snížení kolizí
- Uzavřená smyčka řízení výkonu během přenosu dat
- Podpora proměnných datových rychlostí pro trhavý provoz
- CPCH Status Indicator Channel (CSICH) pro signalizaci dostupnosti prostředků
- Integrace s vrstvami MAC a RLC v UMTS pro zpracování paketů

## Související pojmy

- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [AICH – Acquisition Indication Channel](/mobilnisite/slovnik/aich/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.303** (Rel-19) — Radio Resource Control Procedures
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture

---

📖 **Anglický originál a plná specifikace:** [CPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpch/)
