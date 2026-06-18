---
slug: "date"
url: "/mobilnisite/slovnik/date/"
type: "slovnik"
title: "DATE – Device Application Tag"
date: 2024-01-01
abbr: "DATE"
fullName: "Device Application Tag"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/date/"
summary: "Device Application Tag (DATE) je bezpečnostní identifikátor používaný v aplikacích UICC/USIM podle 3GPP, který jednoznačně označuje a spravuje konkrétní aplikace na zabezpečeném prvku. Je klíčový pro"
---

DATE je bezpečnostní identifikátor používaný v aplikacích UICC/USIM podle 3GPP, který jednoznačně označuje a spravuje konkrétní aplikace na zabezpečeném prvku pro účely bezpečného řízení a autentizace.

## Popis

Device Application Tag (DATE) je základní součástí bezpečnostní architektury 3GPP, konkrétně definovaná pro aplikace UICC (Universal Integrated Circuit Card) a [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module). Slouží jako jedinečný identifikátor instance aplikace umístěné na zabezpečeném prvku. DATE je strukturovaný datový prvek, typicky řetězec oktetů, definovaný ve specifikacích pro správu aplikací USIM a Toolkit (TS 31.111). Jeho primární role spočívá v tom, že je odkazován v zabezpečených příkazech, jako jsou ty používané pro [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) správu platformy, aby přesně cílily na konkrétní aplikaci pro operace jako instalace, personalizace, aktivace nebo smazání.

Architektonicky DATE funguje v zabezpečeném prostředí UICC, které hostuje aplikaci USIM a další volitelné aplikace (jako je [ISIM](/mobilnisite/slovnik/isim/) pro IMS). Když síťový operátor nebo poskytovatel služeb potřebuje spravovat aplikaci na dálku, příkaz pro správu (např. REFRESH, DELETE nebo ACTIVATE) obsahuje DATE cílové aplikace. Operační systém UICC použije tento tag k nalezení správných dat aplikace a provedení požadované operace. Tento mechanismus je nedílnou součástí protokolů Secure Channel používaných v OTA správě, což zajišťuje, že příkazy jsou autentizovány a autorizovány pro konkrétní aplikaci.

Klíčové zúčastněné komponenty zahrnují OTA platformu na síťové straně, která generuje a odesílá zabezpečené příkazy, a Card Manager nebo Security Domain na UICC, který tyto příkazy přijímá a interpretuje. DATE je kritický parametr uvnitř struktury příkazu. Jeho hodnota je přiřazena během fáze instalace nebo personalizace aplikace, často je odvozena od Application Identifier ([AID](/mobilnisite/slovnik/aid/)) nebo přiřazena poskytovatelem aplikace. Jedinečnost DATE v daném kontextu UICC je zásadní pro prevenci nejednoznačnosti příkazů a zajištění bezpečné a spolehlivé správy životního cyklu aplikace.

Role DATE přesahuje pouhou identifikaci; je základním kamenem pro zabezpečené provizionování služeb. V moderních mobilních sítích, zejména s rozšířením eSIM a IoT, je schopnost vzdáleně spravovat více aplikací na jediném zabezpečeném prvku prvořadá. DATE to umožňuje tím, že poskytuje úchopný bod pro síť, aby mohla komunikovat s jednotlivými aplikacemi, aniž by byla ohrožena bezpečnost ostatních aplikací na stejném UICC. Podporuje funkce jako správa profilů pro eSIM (kde každý profil operátora je samostatná aplikace) a zabezpečené povolování služeb IoT.

## K čemu slouží

Device Application Tag byl vytvořen, aby řešil rostoucí potřebu bezpečné vzdálené správy více aplikací na UICC. Před jeho standardizací byla správa aplikací méně strukturovaná, často spoléhala na proprietární identifikátory nebo fyzickou výměnu karty. Jak se mobilní sítě vyvíjely, aby nabízely služby s přidanou hodnotou (jako mobilní bankovnictví, autentizační aplikace) přímo na [SIM](/mobilnisite/slovnik/sim/) kartě, stala se standardizovaná, bezpečná metoda pro identifikaci a správu těchto jednotlivých softwarových entit na dálku kritickou. DATE řeší problém jednoznačného cílení v [OTA](/mobilnisite/slovnik/ota/) příkazech, což je zásadní pro bezpečnost – zajišťuje, že příkaz DELETE například ovlivní pouze zamýšlenou aplikaci a nikoliv základní [USIM](/mobilnisite/slovnik/usim/).

Historicky první SIM karty primárně hostovaly jedinou aplikaci: modul pro autentizaci účastníka. Se zavedením SIM Application Toolkit ([SAT](/mobilnisite/slovnik/sat/)/USAT) se objevila možnost pro síťově provizované aplikace. Správa těchto aplikací však vyžadovala robustní identifikační schéma. DATE, zavedený ve 3GPP Release 99 a upřesněný v pozdějších vydáních, toto poskytl. Řešil omezení předchozích ad-hoc přístupů definováním standardizovaného tagu v rámci sady příkazů 3GPP, což zajišťuje interoperabilitu mezi různými výrobci karet, síťovými operátory a OTA platformami.

Motivace byla hnána komerčními a technickými potřebami: operátoři chtěli nasazovat a aktualizovat služby bez nutnosti, aby uživatelé měnili fyzické SIM karty, a poskytovatelé aplikací potřebovali zabezpečený kanál pro správu životního cyklu. DATE to umožňuje tím, že je klíčovým parametrem ve standardizovaných protokolech Remote Application Management (RAM) a OTA. Jeho vytvoření bylo zásadní pro umožnění moderního ekosystému eSIM a služeb založených na zabezpečeném prvku, čímž vytvořilo základ pro důvěryhodnou správu aplikací v sítích GSM, UMTS, LTE a 5G.

## Klíčové vlastnosti

- Jedinečný identifikátor pro aplikace UICC/USIM
- Kritický parametr v OTA příkazech pro správu (např. DELETE, ACTIVATE)
- Umožňuje bezpečné cílení na konkrétní aplikace bez ovlivnění ostatních
- Standardizovaný formát definovaný v 3GPP TS 31.111 a souvisejících specifikacích
- Podporuje správu životního cyklu aplikace (instalace, personalizace, smazání)
- Nezbytný pro správu profilů eSIM a povolování služeb IoT

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TS 31.122** (Rel-18) — USIM Conformance Test Specification
- **TS 31.213** (Rel-18) — Test specification for (U)SIM

---

📖 **Anglický originál a plná specifikace:** [DATE na 3GPP Explorer](https://3gpp-explorer.com/glossary/date/)
