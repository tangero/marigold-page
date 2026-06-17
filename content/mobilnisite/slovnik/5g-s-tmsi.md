---
slug: "5g-s-tmsi"
url: "/mobilnisite/slovnik/5g-s-tmsi/"
type: "slovnik"
title: "5G-S-TMSI – 5G S-Temporary Mobile Subscription Identifier"
date: 2026-01-01
abbr: "5G-S-TMSI"
fullName: "5G S-Temporary Mobile Subscription Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-s-tmsi/"
summary: "Dočasný identifikátor přiřazený UE v systému 5G pro ochranu trvalého identifikátoru účastníka (SUPI) během počátečního přístupu k síti a volání. Používá se v procedurách řízení rádiových prostředků a"
---

5G-S-TMSI je dočasný identifikátor přiřazený UE v systémech 5G za účelem ochrany trvalého identifikátoru účastníka během počátečního přístupu k síti a volání, používaný v procedurách řízení rádiových prostředků.

## Popis

5G-S-TMSI (5G S-Temporary Mobile Subscription Identifier) je klíčový dočasný identifikátor v architektuře 5G Core Network (5GC), který spravuje konkrétně funkce Access and Mobility Management Function (AMF). Je přiřazen User Equipment (UE) po úspěšné počáteční registrační proceduře. Primárním účelem 5G-S-TMSI je sloužit jako stručný, dočasný alias pro trvalý a na soukromí citlivý Subscription Permanent Identifier (SUPI), čímž se zabrání přenosu SUPI v nezašifrované podobě přes rádiové rozhraní.

Z architektonického hlediska 5G-S-TMSI generuje a přiděluje obsluhující AMF. Je strukturován tak, aby obsahoval informace umožňující síti efektivně směrovat a spravovat UE. Identifikátor se skládá ze dvou hlavních částí: AMF Set ID, AMF Pointer a 5G-TMSI (Temporary Mobile Subscription Identifier). AMF Set ID identifikuje skupinu AMF pro redundanci a vyrovnávání zátěže, zatímco AMF Pointer specifikuje konkrétní AMF v rámci této sady. 5G-TMSI je jedinečné číslo, které daná AMF přiřadí UE na dobu trvání jeho registračního kontextu. Tato struktura umožňuje Radio Access Network (RAN) určit, která instance AMF obsluhuje UE, aniž by potřebovala dekódovat plnou NAS zprávu.

V provozu se 5G-S-TMSI hojně používá v signalizačních procedurách. Během počáteční procedury náhodného přístupu, když je UE ve stavu RRC_IDLE nebo RRC_INACTIVE, zahrne 5G-S-TMSI do zprávy RRCSetupComplete, pokud jej má uložený z předchozí registrace. Co je důležitější, je to primární identifikátor používaný ve zprávě Paging vysílané gNB. Když síť potřebuje kontaktovat UE (např. pro příchozí relaci), volá UE právě pomocí 5G-S-TMSI. Po přijetí volací zprávy obsahující jeho 5G-S-TMSI UE odpoví Service Requestem, který obsahuje stejný identifikátor, což síti umožní znovu navázat spojení a načíst plný kontext UE z AMF.

Role 5G-S-TMSI přesahuje pouhou identifikaci; je zásadní pro efektivitu sítě a bezpečnost. Používáním tohoto dočasného identifikátoru pro časté přenosy přes rozhraní, jako je volání a obnovení spojení, je trvalý SUPI chráněn před odposloucháváním, což řeší významný problém soukromí přítomný v předchozích generacích. Navíc jeho kompaktní velikost (v mnoha případech menší než plný GUTI ze sítě 4G) snižuje signalizační režii. Zahrnutí informací pro směrování AMF přímo v identifikátoru umožňuje efektivní a škálovatelné procesy výběru a změny AMF v rámci služebně orientované architektury 5GC, což podporuje funkce jako mobilita AMF a vyrovnávání zátěže.

## K čemu slouží

5G-S-TMSI byl vytvořen, aby řešil kritické nedostatky v řízení identit účastníků z předchozích generací mobilních sítí, primárně se zaměřením na vylepšené soukromí a efektivitu signalizace. V síti 4G LTE sloužil podobnému účelu Globally Unique Temporary Identifier (GUTI), který však měl větší velikost a odlišnou strukturní logiku vázanou na MME. Systém 5G zavedl přepracovanou, plošší architekturu jádra s jasným oddělením funkce Access and Mobility Management Function (AMF) a Session Management Function (SMF). Tato nová architektura vyžadovala dočasný identifikátor optimalizovaný pro služebně orientovaná rozhraní a specifické procedury 5G, jako je stav RRC_INACTIVE.

Klíčový problém, který 5G-S-TMSI řeší, je ochrana trvalého identifikátoru účastníka (SUPI) před přenosem v nezašifrované podobě přes rádiový spoj. V raných mobilních systémech byl International Mobile Subscriber Identity (IMSI) někdy odesílán nechráněně, což vytvářelo významnou zranitelnost pro sledování účastníků. 5G-S-TMSI, který nahrazuje SUPI téměř ve veškeré rádiové signalizaci po počáteční autentizaci, tuto hrozbu efektivně zmírňuje. Jeho návrh také řeší problém efektivního směrování mezi síťovými uzly. Vložením informací AMF Set a Pointer může RAN přímo určit, která instance AMF drží kontext UE, což umožňuje rychlejší obnovení spojení a efektivnější volání bez nutnosti složitých vyhledávacích procedur, což je zásadní pro podporu případů použití s nízkou latencí, které jsou pro 5G plánovány.

## Klíčové vlastnosti

- Dočasný alias pro trvalý SUPI zajišťující soukromí účastníka
- Obsahuje AMF Set ID a AMF Pointer pro efektivní směrování v rámci 5G Core
- Používá se jako primární identifikátor ve zprávách Paging pro UE v idle/inactive stavech
- Obsažen v RRC signalizaci (např. v RRCSetupComplete) pro získání kontextu
- Kompaktní struktura navržená ke snížení signalizační režie na rádiovém rozhraní
- Jedinečně přiřazen obsluhující AMF každému UE na dobu jeho registrace

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3

---

📖 **Anglický originál a plná specifikace:** [5G-S-TMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-s-tmsi/)
