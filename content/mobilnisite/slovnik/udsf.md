---
slug: "udsf"
url: "/mobilnisite/slovnik/udsf/"
type: "slovnik"
title: "UDSF – Unstructured Data Storage Function"
date: 2026-01-01
abbr: "UDSF"
fullName: "Unstructured Data Storage Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udsf/"
summary: "Síťová funkce 5G Core, která poskytuje úložiště pro nestrukturovaná data, jako je kontext relace nebo dočasné stavové informace. Nabízí jednoduchou, obecnou úložnou službu přístupnou přes API, což umo"
infografika: "/assets/slovnik/udsf.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním UDSF"
---

UDSF je síťová funkce 5G Core, která poskytuje obecnou úložnou službu pro nestrukturovaná data, umožňující ostatním síťovým funkcím (NF) přesunout správu stavu, čímž podporuje bezestavový návrh a škálovatelnost.

## Popis

Funkce pro ukládání nestrukturovaných dat (UDSF) je komponenta v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G Core (5GC), zavedená ve specifikaci 3GPP Release 15. Jejím hlavním úkolem je poskytovat trvalé úložiště pro nestrukturovaná data jménem ostatních síťových funkcí ([NF](/mobilnisite/slovnik/nf/)). Na rozdíl od [UDR](/mobilnisite/slovnik/udr/), která ukládá strukturované datové profily (předplatné, politiky), je UDSF navržena pro data, která se neřídí předdefinovaným, standardizovaným schématem. Typicky to zahrnuje kontextová data relace, dočasné stavové informace, datové objekty specifické pro aplikaci nebo jakákoli jiná data, která si NF potřebuje uchovat pro účely spolehlivosti, škálovatelnosti nebo kontinuity služeb.

Z architektonického hlediska UDSF vystavuje rozhraní založené na službách, Nudsf, využívající [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/). Rozhraní poskytuje základní operace vytvoření, čtení, aktualizace, odstranění a dotazování (CRUDQ). Síťová funkce (např. Session Management Function, [SMF](/mobilnisite/slovnik/smf/), nebo Application Function, [AF](/mobilnisite/slovnik/af/)) může uložit datový objekt zadáním jedinečného klíče (např. kombinace [SUPI](/mobilnisite/slovnik/supi/), DNN, S-NSSAI) a datové zátěže ve flexibilním formátu (často JSON nebo binární). UDSF obsah neinterpretuje; pouze jej ukládá a načítá. Díky tomu je UDSF obecnou úložnou službou. Klíčovým případem použití je umožnění bezestavového návrhu pro ostatní NF. Například SMF může uložit kontext relace PDU (Protocol Data Unit) v UDSF. Pokud instance SMF selže, nová instance může kontext z UDSF načíst a plynule pokračovat ve správě relace, čímž je zajištěna kontinuita služby.

UDSF funguje nezávisle na sémantice dat. Na formátu dat se musí dohodnout produkující a konzumující NF. UDSF může podporovat funkce jako replikace dat pro vysokou dostupnost, řízení přístupu na základě identity NF a případně čas života (TTL) pro dočasná data. Její nasazení je flexibilní; může to být vyhrazená síťová funkce nebo její funkcionalita může být integrována do cloud-nativní platformy pro ukládání dat. Poskytnutím této služby UDSF umožňuje navrhovat NF jako bezestavové nebo minimálně stavové procesy, což je v souladu s cloud-nativními principy. To zjednodušuje implementaci NF, zlepšuje horizontální škálovatelnost (nové instance NF mohou přistupovat ke sdílenému stavu) a zvyšuje odolnost proti poruchám, což je klíčové pro náročné požadavky služeb 5G.

## K čemu slouží

UDSF byla vytvořena, aby řešila konkrétní výzvu při přechodu na cloud-nativní, službami založený 5G Core: efektivní a spolehlivou správu stavu. Tradiční telekomunikační síťové funkce byly často stavové monolitické systémy, které ukládaly data relací a kontextu lokálně. To ztěžovalo jejich horizontální škálování a činilo je zranitelnými vůči selháním – pokud instance selhala, její relace byly ztraceny. Návrhový princip 5GC prosazuje, pokud možno, bezestavové NF, ale některý stav (jako je kontext relace PDU) je nezbytný a musí být trvalý.

UDSF poskytuje standardizované řešení pro tuto perzistenci, aniž by předepisovala, jak mají NF strukturovat svá interní data. Předchozí přístupy mohly vyžadovat, aby každá NF implementovala vlastní proprietární databázi nebo spoléhala na nestandardizované úložiště, což vedlo ke složitosti a závislosti na dodavateli. UDSF nabízí jednoduchou úložnou službu platnou pro celou síť. Tím řeší problém správy stavu pro bezestavové NF a umožňuje funkce jako plynulé obnovení služby po selhání a efektivní vyvažování zátěže mezi instancemi NF. Je klíčovým prvkem pro síťové řezy (network slicing), protože různé řezy mohou používat stejnou infrastrukturu UDSF při zachování izolovaného úložiště dat pro své příslušné NF. UDSF je tedy základním prvkem pro dosažení odolnosti, elasticity a provozní jednoduchosti, které požadují sítě 5G.

## Klíčové vlastnosti

- Obecné úložiště pro nestrukturovaná data (např. kontext relace, stavové objekty)
- Rozhraní založené na službách (Nudsf) s operacemi CRUDQ využívající HTTP/2/JSON
- Umožňuje bezestavový nebo minimálně stavový návrh ostatních síťových funkcí
- Neinterpretuje obsah dat; ukládá a načítá na základě klíče
- Podporuje kontinuitu služby a obnovu po selhání pro stavové procesy
- Usnadňuje cloud-nativní principy, jako je horizontální škálování a odolnost

## Související pojmy

- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.598** (Rel-19) — UDSF Service Based Interface Stage 3 Protocol
- **TS 29.808** (Rel-16) — Study on Nudsf Service Based Interface
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [UDSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/udsf/)
