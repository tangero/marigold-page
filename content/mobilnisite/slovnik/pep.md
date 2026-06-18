---
slug: "pep"
url: "/mobilnisite/slovnik/pep/"
type: "slovnik"
title: "PEP – Policy Enforcement Point"
date: 2025-01-01
abbr: "PEP"
fullName: "Policy Enforcement Point"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pep/"
summary: "Funkční entita v rámci architektury Policy and Charging Control (PCC), která vynucuje rozhodnutí o pravidlech. Sídlí v bráně (např. P-GW, TDF) a aplikuje pravidla pro uzavírání, QoS a tarifní pravidla"
---

PEP (Policy Enforcement Point, bod vynucování pravidel) je funkční entita v rámci architektury PCC, která sídlí v bráně a vynucuje rozhodnutí o pravidlech aplikacím uzavírání, QoS a tarifních pravidel na datové toky uživatele.

## Popis

Policy Enforcement Point (PEP, bod vynucování pravidel) je kritická síťová funkce v rámci rámce 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Je to entita zodpovědná za vynucování rozhodnutí o pravidlech přijatých od funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) v uživatelské rovině. PEP je typicky umístěn společně s bránou, která zpracovává datový provoz uživatele, jako je Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v EPS, Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) v GPRS nebo Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)). Jeho hlavní role spočívá v aplikaci autorizovaných pravidel na jednotlivé IP datové toky, čímž zajišťuje, že síťové zdroje jsou využívány v souladu s profily účastníků, služebními plány a aktuálními podmínkami sítě.

Architektonicky rozhraní PEP s PCRF přes referenční bod Gx (nebo referenční bod Sd pro TDF). Přijímá PCC pravidla, což jsou balíčky instrukcí obsahujících informace pro identifikaci služebního datového toku, jeho přidružené tarifní parametry a řídicí pravidla k aplikaci (např. uzavírání, QoS označování, limity přenosové rychlosti). PEP tato pravidla instaluje, upravuje nebo odstraňuje. Klíčové komponenty uvnitř PEP zahrnují mechanismus detekce služebního datového toku, který používá paketové filtry (např. 5-tice) k identifikaci provozu, a motory pro vynucování uzavírání (povolení/blokování paketů), QoS (nastavení značek [DSCP](/mobilnisite/slovnik/dscp/), správa přenosových kanálů) a tarifní řízení (spouštění událostí řízení kreditu, aplikace limitů šířky pásma pro uplink/downlink).

Jeho fungování je kontinuální smyčka řízení. Když je zahájena nová služba, může PEP vyžádat pravidla od PCRF. Po jejich přijetí pravidlo nainstaluje a začne kontrolovat pakety. Pro každý paket provádí shodu s nainstalovanými filtry. Pokud je nalezena shoda, PEP provede přidružené akce: může paket přeposlat nebo zahodit (uzavírání), označit jeho DiffServ Code Point (QoS), tvarovat nebo regulovat tok na autorizované přenosové rychlosti a sbírat údaje o využití pro offline nebo online tarifní systémy. PEP také hlásí události (jako objem využití, ukončení služby) zpět PCRF. Toto dynamické vynucování umožňuje sofistikovanou diferenciaci služeb, jako je upřednostňování VoIP provozu, omezování P2P provozu nebo umožnění sponzorovaných datových služeb, vše v reálném čase na základě centralizované logiky pravidel.

## K čemu slouží

Policy Enforcement Point existuje, aby překlenul propast mezi vysokou úrovní obchodních pravidel a zpracováním síťových paketů v reálném čase. Před standardizovanou architekturou [PCC](/mobilnisite/slovnik/pcc/) bylo řízení pravidel často statické, konfigurované přímo na síťových branách, což ztěžovalo vytváření dynamických, na účastníka orientovaných nebo služebně specifických pravidel. To omezovalo schopnost operátorů nabízet vrstvenou QoS, implementovat politiky spravedlivého využití nebo vytvářet inovativní tarifní modely, jako je zero-rating.

PEP řeší problém decentralizovaného a nepružného provádění pravidel. Byl motivován potřebou jasného oddělení řídicí a uživatelské roviny, kde jsou inteligentní rozhodnutí o pravidlech přijímána centrálně ([PCRF](/mobilnisite/slovnik/pcrf/)) a vynucována konzistentně v kritických bodech provozu. Tato architektura umožňuje operátorům rychle zavádět nové služby a tarifní plány bez nutnosti individuální rekonfigurace každé brány. Řeší omezení předchozích přístupů poskytnutím standardizovaného rozhraní (Gx) pro dynamické poskytování pravidel, což umožňuje interakci v reálném čase mezi tarifním systémem, databází předplatitelů a síťovým okrajem.

Historicky bylo jeho vytvoření hnací silou evoluce směrem k plně IP sítím a poptávky po sofistikované kontrole služeb nad rámec jednoduchého best-effort přístupu k internetu. PEP umožňuje klíčové schopnosti operátorů: zaručení QoS pro služby IMS jako VoLTE, implementaci rodičovských kontrol, správu zahlcení sítě a umožnění partnerských služeb (jako sponzorovaná data). Je zásadní pro monetizaci a efektivní provoz moderních mobilních širokopásmových sítí, přeměňující jednoduché datové kanály na inteligentní, účtovatelné služby.

## Klíčové vlastnosti

- Vynucuje PCC pravidla přijatá od PCRF přes rozhraní Gx
- Provádí detekci služebního datového toku pomocí paketových filtrů
- Provádí řízení uzavírání (povolení/zamítnutí) pro datové toky
- Aplikuje vynucování QoS (regulace/tvarování přenosové rychlosti, označování DSCP)
- Spouští tarifní události a komunikuje s Online/Offline Charging Systems
- Hlásí využití a spouštěcí události (např. objem, změna polohy) PCRF

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [TDF – Traffic Detection Function](/mobilnisite/slovnik/tdf/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TS 33.794** (Rel-19) — Study on Zero Trust Security Enablers for 5G

---

📖 **Anglický originál a plná specifikace:** [PEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pep/)
