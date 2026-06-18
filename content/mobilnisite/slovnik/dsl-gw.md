---
slug: "dsl-gw"
url: "/mobilnisite/slovnik/dsl-gw/"
type: "slovnik"
title: "DSL-GW – DSL Gateway"
date: 2025-01-01
abbr: "DSL-GW"
fullName: "DSL Gateway"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dsl-gw/"
summary: "DSL Gateway (DSL-GW) je síťový prvek, který funguje jako rozhraní mezi přístupovými sítěmi Digital Subscriber Line (DSL) a mobilním jádrovou sítí, konkrétně jádrem GPRS. Umožňuje integraci pevného DSL"
---

DSL-GW je síťový prvek, který zprostředkovává rozhraní mezi DSL přístupovými sítěmi a mobilním GPRS jádrem, umožňuje konvergenci pevných a mobilních sítí směrováním uživatelských dat a vynucováním politik pro účastníky využívající DSL širokopásmové připojení.

## Popis

[DSL](/mobilnisite/slovnik/dsl/) Gateway funguje jako entita podobná bráně [GPRS](/mobilnisite/slovnik/gprs/) support node (GGSN) pro provoz pocházející z nebo směřující do DSL přístupových sítí. Ukončuje uživatelskou rovinu a řídicí rovinu spojení DSL, typicky využívající relace [PPP](/mobilnisite/slovnik/ppp/) nebo IP přes DSL linku. DSL-GW se připojuje k mobilní jádrové síti přes referenční bod Gi, díky čemuž se DSL přístup z pohledu GGSN nebo [PGW](/mobilnisite/slovnik/pgw/) jeví jako další paketová datová síť. Provádí klíčové funkce, jako je přidělování IP adres (často pomocí [DHCP](/mobilnisite/slovnik/dhcp/)), směrování a přeposílání paketů a řízení provozu.

Z architektonického hlediska se DSL-GW nachází na okraji mobilního jádra, na jedné straně se připojuje k DSL přístupovým multiplexorům (DSLAM) a na straně druhé k GGSN/PGW. Obsahuje komponenty pro správu relací, vynucování politik a generování účtovacích dat. V architektuře 3GPP Rel-8 hraje roli při umožnění bezproblémové kontinuity služeb a společné kontroly politik pro uživatele, kteří mohou přepínat mezi 3GPP radiovým přístupem a pevným DSL přístupem.

Specifikace 25.467 podrobně popisuje DSL-GW v kontextu celkového popisu [UTRAN](/mobilnisite/slovnik/utran/). Jeho úlohou je poskytnout standardizovaný mechanismus pro vzájemné propojení mezi mobilními sítěmi UMTS/GPRS a pevnými širokopásmovými sítěmi založenými na DSL. To umožňuje mobilním operátorům, kteří vlastní také pevné sítě, nabízet integrované služby a optimalizovat směrování provozu napříč jejich kombinovanými aktivy.

## K čemu slouží

DSL-GW byl vytvořen pro podporu konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)), což umožňuje operátorům s mobilními i pevnými aktivy nabízet sjednocené služby a sdílet síťové zdroje. Řešil problém oddělených, izolovaných sítí pro mobilní a pevný širokopásmový přístup, které vedly k provozní neefektivitě a roztříštěným uživatelským zkušenostem. Poskytnutím standardizované brány umožnil poskytování služeb mobilního jádra (jako je IMS, mobilní datové tarify) přes pevný [DSL](/mobilnisite/slovnik/dsl/) přístup.

Motivace vycházela z trendu směřujícího ke konvergentním službám na konci let 2000 (období Rel-8). Operátoři chtěli využít svou DSL infrastrukturu k odlehčení mobilního datového provozu (raná forma offload) a nabízet služby jako „connected home“, kde by jediné předplatné pokrývalo jak mobilní, tak pevný přístup. DSL-GW odstranil omezení předchozích ad-hoc nebo proprietárních bran tím, že definoval standardizovaný síťový prvek v rámci architektury 3GPP, čímž zajistil interoperabilitu mezi zařízeními od různých výrobců.

## Klíčové vlastnosti

- Funkce vzájemného propojení mezi DSL přístupem a jádrem GPRS (rozhraní Gi)
- Správa a přidělování IP adres pro UE připojená přes DSL
- Směrování a přeposílání paketů mezi přístupovou a jádrovou sítí
- Vynucování politik na základě profilů účastníků
- Generování záznamů o účtování dat pro využití přes DSL
- Podpora scénářů konvergentních služeb pro pevné a mobilní sítě

## Definující specifikace

- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B

---

📖 **Anglický originál a plná specifikace:** [DSL-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsl-gw/)
