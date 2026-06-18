---
slug: "s-core"
url: "/mobilnisite/slovnik/s-core/"
type: "slovnik"
title: "S-CORE – Shared Core"
date: 2025-01-01
abbr: "S-CORE"
fullName: "Shared Core"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/s-core/"
summary: "S-CORE je architektonický koncept 3GPP, který umožňuje více operátorům mobilních sítí (MNO) nebo síťovým řezům sdílet společnou infrastrukturu jádra sítě. Snižuje náklady na nasazení a provoz při zach"
---

S-CORE je architektonický koncept 3GPP, který umožňuje více operátorům mobilních sítí nebo síťovým řezům sdílet společnou infrastrukturu jádra sítě při zachování logického oddělení.

## Popis

Sdílené jádro (S-CORE) je základní architektonický princip definovaný v rámci 3GPP pro umožnění sdílení sítě. Umožňuje více účastnickým operátorům nebo tenantům využívat jedinou společnou infrastrukturu jádra sítě (CN), která zahrnuje síťové funkce jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/) a [UDM](/mobilnisite/slovnik/udm/). Architektura je navržena tak, aby zajistila logickou izolaci mezi sdílejícími partnery, což znamená, že odběratelé, zásady a data každého operátora jsou udržovány odděleně a v bezpečí. Toho je dosaženo použitím vyhrazených identifikátorů, jako jsou specifická [PLMN](/mobilnisite/slovnik/plmn/) ID, a instancí síťových řezů, které jsou logicky odděleny v rámci sdílených fyzických zdrojů.

Z provozní perspektivy zavádí S-CORE specifické schopnosti správy a orchestrace. Sdílenou infrastrukturu spravuje hostitelská strana, kterou může být jeden z účastnických operátorů nebo neutrální hostitel. Každý sdílející operátor si zachovává kontrolu nad vlastní správou odběratelů, řízením zásad a poskytováním služeb. Specifikace 3GPP definují referenční body a procedury pro podporu tohoto rozdělení odpovědnosti, což zajišťuje, že operátor může nezávisle autentizovat své uživatele, uplatňovat vlastní QoS zásady a spravovat záznamy o účtování bez zásahu jiných operátorů sdílejících jádro.

Implementace S-CORE je klíčová pro několik scénářů nasazení. Je základem pro uspořádání mobilního virtuálního síťového operátora ([MVNO](/mobilnisite/slovnik/mvno/)), kde MVNO nevlastní infrastrukturu rádiové přístupové sítě (RAN), ale spoléhá se na jádro hostitelského [MNO](/mobilnisite/slovnik/mno/). Je také nezbytná pro národní roamingové dohody a v poslední době pro umožnění efektivního síťového krájení v 5G. V kontextu síťového krájení mohou být různé řezy (např. pro rozšířené mobilní širokopásmové připojení, hromadný IoT nebo ultra-spolehlivou komunikaci s nízkou latencí) instancovány na sdílené platformě S-CORE, přičemž každý řez představuje logicky izolovanou síť sloužící specifickému tenantovi nebo typu služby. Specifikace, zejména TS 32.130 a TS 32.851, podrobně popisují aspekty správy a orchestrace, včetně plnění smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), oddělení správy poruch a hlášení výkonu pro každou sdílející entitu.

## K čemu slouží

S-CORE bylo zavedeno pro řešení vysokých kapitálových (CAPEX) a provozních (OPEX) výdajů spojených s nasazením a údržbou nezávislých jader sítí, zejména pro nové účastníky trhu nebo ve scénářích s nízkou počáteční hustotou odběratelů. Před standardizovaným sdílením sítě museli operátoři budovat zcela oddělená jádra sítí, což vedlo k neefektivnímu využití zdrojů a vyšším nákladům. S-CORE poskytuje standardizovaný rámec, který umožňuje sdílení infrastruktury při zachování vlastní značky, diferenciace služeb a kontroly nad odběrateli pro každého operátora.

Motivace vychází jak z ekonomických, tak regulačních podnětů. Ekonomicky snižuje vstupní bariéru pro nové operátory a umožňuje stávajícím operátorům zpeněžit nadbytečnou kapacitu. Regulátoři v mnoha regionech podporují sdílení sítí pro urychlení rozšíření pokrytí, zejména ve venkovských oblastech, a pro snížení dopadu na životní prostředí minimalizací duplicitní infrastruktury. Koncept se vyvinul pro podporu dynamičtějších a flexibilnějších modelů sdílení vyžadovaných pro 5G, kde síťové krájení vyžaduje jádro sítě, které lze na požádání rozdělit pro různé vertikální odvětví. S-CORE řeší problém rigidních, fyzicky oddělených jader tím, že poskytuje škálovatelnou víceklientskou architekturu, která zachovává nezbytnou bezpečnost a provozní nezávislost.

## Klíčové vlastnosti

- Umožňuje logickou izolaci více operátorů/tenantů na jediném fyzickém jádru
- Podporuje nezávislou správu odběratelů a autentizaci pro každou sdílející entitu
- Umožňuje oddělené funkce řízení zásad a účtování pro každého operátora
- Usnadňuje správu a orchestraci s oddělenými daty o poruchách a výkonu
- Poskytuje základ pro provoz MVNO a národní roamingové dohody
- Základní architektonická komponenta pro implementaci 5G síťového krájení

## Související pojmy

- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [GWCN – GateWay Core Network](/mobilnisite/slovnik/gwcn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements

---

📖 **Anglický originál a plná specifikace:** [S-CORE na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-core/)
