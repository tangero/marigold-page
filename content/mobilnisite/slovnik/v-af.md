---
slug: "v-af"
url: "/mobilnisite/slovnik/v-af/"
type: "slovnik"
title: "V-AF – Visited AF"
date: 2025-01-01
abbr: "V-AF"
fullName: "Visited AF"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-af/"
summary: "Aplikační funkce (Application Function) umístěná ve navštívené síti (VPLMN), když je uživatel v roamingu. Komunikuje s funkcí řízení politik a účtování (V-PCRF) navštívené sítě, aby aplikovala dynamic"
---

V-AF je aplikační funkce (Application Function) umístěná ve navštívené síti, která komunikuje s navštívenou funkcí PCRF (Policy and Charging Rules Function) za účelem aplikace dynamického řízení politik a umožnění lokalizovaného poskytování služeb pro roamujícího účastníka.

## Popis

Navštívená aplikační funkce (V-AF) je logická síťová funkce v architektuře řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) podle 3GPP, která je relevantní zejména v roamingu. Aplikační funkce ([AF](/mobilnisite/slovnik/af/)) je obecně prvek, který vyžaduje dynamické řízení politik a/nebo účtování pro [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) relaci uživatele; příklady zahrnují Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) pro IMS nebo streamovací server. Když je účastník v roamingu mimo svou domovskou síť, může služební aplikace hostovaná v navštívené síti potřebovat komunikovat se systémem PCC. Tato aplikační funkce umístěná v navštívené síti se označuje jako V-AF.

V-AF funguje tak, že komunikuje s funkcí řízení politik a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) v navštívené síti, známou jako [V-PCRF](/mobilnisite/slovnik/v-pcrf/). Tato komunikace probíhá přes referenční bod Rx. Když V-AF potřebuje ovlivnit politiku pro relaci roamujícího účastníka (např. požádat o garantovaný přenosový výkon pro videohovor), odešle Diameter zprávu AA-Request (AAR) k V-PCRF. V-PCRF následně komunikuje s PCRF domovské sítě ([H-PCRF](/mobilnisite/slovnik/h-pcrf/)) přes roamující rozhraní S9. H-PCRF je konečným rozhodovatelem, protože má přístup k profilu účastníka a domovským politikám. H-PCRF učiní rozhodnutí o politice a poskytne příslušná pravidla V-PCRF, která je pak předá funkci vynucování politik a účtování ([V-PCEF](/mobilnisite/slovnik/v-pcef/)) v navštívené síti k provedení v uživatelské rovině.

Klíčovými komponentami této architektury jsou samotná V-AF, V-PCRF, H-PCRF a rozhraní S9. Role V-AF je fungovat jako žadatel o politiky ze servisní vrstvy v navštívené doméně. Její existence umožňuje efektivní, lokalizované poskytování služeb. Například, pokud roamující uživatel přistupuje k videoslužbě hostované v navštívené zemi, může AF této služby (V-AF) požadovat nezbytnou QoS přímo od lokální V-PCRF, čímž se minimalizuje latence a navštívená síť může spravovat své vlastní zdroje, přičemž stále respektuje celková rozhodnutí o politikách domovského operátora koordinovaná přes H-PCRF. Toto oddělení odpovědností je klíčové pro škálovatelný a pro operátory vstřícný roaming.

## K čemu slouží

Koncept V-AF byl zaveden, aby řešil složitost aplikace dynamického řízení politik v roamingu v rámci PCC architektury definované ve verzi 7 a dále vylepšované. Před jeho formalizací byl interakční model pro AF v roamingu nejasný. Klíčovým problémem bylo určit, která PCRF – ta v domovské nebo navštívené síti – by měla přijímat žádosti o politiky od AF umístěné v navštívené síti. Architektura potřebovala podporovat scénáře, kde jsou služby optimálně doručovány z navštívené sítě (local breakout), při zachování kontroly domovského operátora nad politikami a účtováním účastníka.

Její vytvoření bylo motivováno potřebou jasné, standardizované roamingu architektury pro PCC. Řeší tento problém definováním jasného řetězce odpovědnosti: lokálně hostovaná služba (V-AF) komunikuje s lokálním řadičem politik (V-PCRF), který funguje jako proxy k domovskému řadiči politik (H-PCRF). To zajišťuje, že domovský operátor si zachovává konečnou autoritu (klíčový obchodní požadavek), zatímco navštívená síť může efektivně zpracovávat žádosti o politiky pro služby, které sama hostuje. Tento model umožňuje pokročilé roamingu funkce, jako je optimalizované doručování multimediálních služeb, kde může být QoS pro lokálně hostovanou IMS aplikaci řízena bez toho, aby veškerá signalizace procházela domovskou sítí, což zlepšuje výkon a snižuje náklady na přenosové trasy.

## Klíčové vlastnosti

- Entita aplikační funkce (Application Function) sídlící v navštívené veřejné pozemní mobilní síti (VPLMN)
- Komunikuje s navštívenou funkcí PCRF (V-PCRF) přes rozhraní Rx
- Iniciuje dynamické žádosti o politiky (např. pro QoS) pro roamující účastníky
- Umožňuje řízení politik pro služby doručované přes Local Breakout (LBO) v navštívené síti
- Součástí end-to-end roamingu architektury PCC zahrnující rozhraní S9 mezi V-PCRF a H-PCRF
- Umožňuje poskytovatelům služeb v navštívené síti integraci s rámcem politik roamujícího uživatele

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification

---

📖 **Anglický originál a plná specifikace:** [V-AF na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-af/)
