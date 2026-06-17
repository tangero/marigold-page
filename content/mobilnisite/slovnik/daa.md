---
slug: "daa"
url: "/mobilnisite/slovnik/daa/"
type: "slovnik"
title: "DAA – Detect And Avoid"
date: 2026-01-01
abbr: "DAA"
fullName: "Detect And Avoid"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/daa/"
summary: "DAA je mechanismus koexistence spektra pro NR-U (New Radio v nelicencovaném spektru), který detekuje původní systémy, jako je Wi-Fi nebo radar, a zabraňuje interferenci vyklizením nebo úpravou přenosů"
---

DAA je mechanismus koexistence spektra pro 5G NR-U, který detekuje původní systémy, jako je Wi-Fi, a zabraňuje interferenci vyklizením nebo úpravou svých přenosů, aby zajistil spravedlivé a regulatorně konformní sdílení.

## Popis

Detect And Avoid (DAA) je klíčová funkce pro provoz New Radio v nelicencovaném spektru ([NR-U](/mobilnisite/slovnik/nr-u/)), která je vyžadována pro zajištění harmonické koexistence s původními systémy, jako je Wi-Fi ([IEEE](/mobilnisite/slovnik/ieee/) 802.11) a radar, ve sdílených kmitočtových pásmech, například 5 GHz a 6 GHz. Mechanismus funguje prostřednictvím kontinuálního dvoufázového procesu: detekce a následného vyhýbání. Ve fázi detekce provádí gNB (Next Generation NodeB) nebo UE (User Equipment) detekci energie nebo specifické snímání tvaru signálu (např. pro radarové pulsy) na cílovém kanálu před a během přenosových příležitostí. Toto snímání je definováno regulatorními požadavky (např. [FCC](/mobilnisite/slovnik/fcc/), [ETSI](/mobilnisite/slovnik/etsi/)) a zahrnuje naslouchání signálům nad předdefinovaným prahem po minimální dobu obsazení kanálu. gNB koordinuje toto snímání, případně za použití měření asistovaných UE, aby vytvořil komplexní obraz o prostředí kanálu.

Po detekci signálu původního systému vstoupí systém do fáze vyhýbání. Základním principem je, že přenos NR-U musí okamžitě vyklidit kanál nebo významně snížit svůj potenciál způsobit interferenci. Toho je dosaženo mechanismy, jako je přepínání kanálů, kdy gNB plánuje přenosy na alternativním čistém kanálu identifikovaném během předchozího snímání. Případně může gNB použít dynamické řízení výkonu, snížením svého vysílacího výkonu pod práh interference pro původní systém. Pro vyhýbání radaru je často vyžadován přísnější protokol 'move away', kdy systém nesmí kanál používat po stanovenou dobu klidu. gNB spravuje tyto procedury prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), konfiguruje UE s měřicími mezery pro snímání a aktualizuje rozhodnutí o plánování na základě výsledků snímání.

Architektonicky je funkce DAA integrována v rámci [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) a PHY (Physical Layer) gNB, s podporou vyšší vrstvy RRM (Radio Resource Management). gNB funguje jako centrální kontrolér, který instruuje UE, kdy mají provádět měření Listen-Before-Talk ([LBT](/mobilnisite/slovnik/lbt/)) a DAA. Tato měření jsou hlášena zpět gNB, který data konsoliduje, aby učinil rozhodnutí o obsazení kanálu. Systém podporuje jak širokopásmové, tak úzkopásmové snímání, aby vyhověl různým charakteristikám signálů původních systémů. Role DAA je základní pro NR-U, přeměňující nelicencované spektrum z oblasti 'best-effort' na řízený zdroj, kde může 5G fungovat předvídatelně při respektování zákonných požadavků a podpoře spektrální efektivity prostřednictvím inteligentního, reaktivního sdílení.

## K čemu slouží

DAA bylo vytvořeno, aby řešilo základní výzvu nasazení 5G New Radio v globálně dostupných nelicencovaných a sdílených kmitočtových pásmech. Primární motivací bylo rozšířit kapacitu mobilní sítě a podporovat služby s vysokou propustností a nízkou latencí bez výhradní závislosti na licencovaném spektru, které je vzácné a drahé. Pásma jako 5 GHz a 6 GHz jsou však již obsazena zavedenými technologiemi, především Wi-Fi pro spotřebitelské a podnikové využití, a radarovými systémy pro meteorologické, vojenské a satelitní aplikace. Regulační orgány po celém světě ukládají novým účastníkům v těchto pásmech přísná pravidla 'koexistence' nebo 'ochrany původních systémů'. Bez DAA by přenosy [NR-U](/mobilnisite/slovnik/nr-u/) mohly způsobit škodlivou interferenci, degradovat výkon Wi-Fi nebo narušit kritické radarové operace, což by vedlo k nedodržení regulatorních požadavků a selhání služby.

Tato technologie řeší problém, jak naplánovaný synchronní mobilní systém, jako je 5G NR, může spravedlivě sdílet spektrum se systémy založenými na soutěžení a asynchronními, jako je Wi-Fi, a s chráněnými radarovými službami. Předchozí přístupy v LTE-LAA (License Assisted Access) zavedly základní Listen-Before-Talk (LBT), ale to bylo primárně navrženo pro koexistenci s jinými systémy založenými na LBT. DAA rozšiřuje tento koncept sofistikovanějšími detekčními schopnostmi přizpůsobenými specifickým charakteristikám původních systémů (např. vzorům radarových pulsů) a determinističtějšími protokoly vyhýbání požadovanými regulátory. Řeší omezení jednoduchého LBT, které nemusí spolehlivě detekovat signály nevyužívající LBT, jako jsou některé typy radarů, začleněním detekce specifických rysů a delších měřicích period. Vytvoření DAA v 3GPP Release-18 bylo hnací silou potřeby standardizovat jednotný, globálně aplikovatelný rámec, který umožní zařízením NR-U splnit různorodé regionální regulatorní požadavky, čímž zajistí interoperabilitu zařízení a úspěšné tržní nasazení 5G ve sdíleném spektru.

## Klíčové vlastnosti

- Detekce signálů původních systémů prostřednictvím detekce energie a specifického snímání rysů
- Regulatorně konformní vyklizení kanálu a řízení vysílacího výkonu
- Procedury měření a hlášení koordinované gNB a asistované UE
- Podpora koexistence se systémy Wi-Fi (IEEE 802.11) a radarovými systémy
- Integrace s Listen-Before-Talk (LBT) pro komplexní přístup ke kanálu
- Dynamické plánování zdrojů a přepínání kanálů na základě výsledků snímání

## Související pojmy

- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)
- **TS 33.256** (Rel-19) — Security for Uncrewed Aerial Systems (UAS)
- **TS 33.759** (Rel-19) — UAS Security Enhancements Phase 3 Study
- **TR 33.891** (Rel-18) — Security and Privacy Threats for UAVs and UAM
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/daa/)
