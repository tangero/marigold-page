---
slug: "ctsmsi"
url: "/mobilnisite/slovnik/ctsmsi/"
type: "slovnik"
title: "CTSMSI – Cordless Telephony System Mobile Subscriber Identity"
date: 2025-01-01
abbr: "CTSMSI"
fullName: "Cordless Telephony System Mobile Subscriber Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ctsmsi/"
summary: "CTSMSI je dočasný identifikátor účastníka používaný v architektuře systému bezšňůrové telefonie 3GPP (CTS). Jednoznačně identifikuje CTS mobilní stanici registrovanou u konkrétní pevné části CTS (CTS-"
---

CTSMSI je dočasný identifikátor účastníka používaný v systému bezšňůrové telefonie 3GPP (Cordless Telephony System) k jednoznačné identifikaci mobilní stanice registrované u konkrétní pevné části během aktivních relací.

## Popis

Cordless Telephony System Mobile Subscriber Identity (CTSMSI) je klíčový identifikátor v rámci architektury systému bezšňůrové telefonie 3GPP ([CTS](/mobilnisite/slovnik/cts/)), který byl navržen pro poskytování bezproblémových služeb bezšňůrové telefonie přes sítě GSM/UMTS. CTSMSI funguje jako dočasná, na relaci vázaná identita přidělená mobilní stanici CTS ([CTS-MS](/mobilnisite/slovnik/cts-ms/)) při její registraci u pevné části CTS ([CTS-FP](/mobilnisite/slovnik/cts-fp/)). Tento identifikátor je nezbytný pro správu mobility, směrování hovorů a bezpečnostní procedury v rámci CTS domény. Operuje vedle trvalých identifikátorů, jako je International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), ale poskytuje vylepšené možnosti ochrany soukromí a správy relací.

Z architektonického hlediska CTSMSI funguje v rámci protokolového zásobníku CTS definovaného ve specifikacích 3GPP 43.020 a 43.052. Když CTS-MS zahájí registraci u CTS-FP, síť přidělí CTSMSI, který zůstává platný po dobu trvání relace nebo do explicitní deregistrace. Tento identifikátor je strukturován tak, aby obsahoval informace o obsluhující CTS-FP a konkrétní instanci CTS-MS, což umožňuje efektivní procedury vyhledávání, aktualizace polohy a předávání spojení mezi různými CTS-FP v rámci stejné CTS domény. CTSMSI se používá ve všech následných signalizačních zprávách mezi CTS-MS a CTS-FP, čímž se snižuje potřeba přenášet trvalý IMSI a zvyšuje se tak ochrana soukromí účastníka.

Generování a správa CTSMSI zahrnuje několik klíčových komponent: CTS-MS, která identifikátor žádá; CTS-FP, která jej přiděluje a spravuje; a databázi CTS (CTS-DB), která může uchovávat mapovací informace mezi CTSMSI a trvalými identitami účastníků. Proces přidělení typicky probíhá během procedury registrace CTS, kdy CTS-MS poskytne svou trvalou identitu a CTS-FP odpoví CTSMSI, který je jedinečný v rámci její servisní oblasti. Tento identifikátor je pak používán pro všechny zprávy správy mobility, včetně aktualizací lokalizační oblasti, periodických aktualizací registrace a příprav předání spojení mezi CTS-FP.

Z pohledu provozu sítě hraje CTSMSI klíčovou roli v řízení relací a alokaci prostředků. Umožňuje CTS-FP udržovat aktivní relace pro více zařízení CTS-MS současně a zároveň efektivně spravovat rádiové prostředky. Během zřizování hovoru se CTSMSI používá k identifikaci volajícího a volané strany v rámci CTS domény, což usnadňuje rychlé navázání spojení. Identifikátor také podporuje bezpečnostní funkce tím, že slouží jako reference pro autentizační a šifrovací procedury, ačkoli skutečné bezpečnostní klíče jsou odvozeny od trvalé identity účastníka uložené v síti.

## K čemu slouží

CTSMSI byl vytvořen, aby řešil specifické požadavky architektury systému bezšňůrové telefonie v rámci sítí 3GPP. Před jeho zavedením systémy bezšňůrové telefonie často používaly pro veškerou komunikaci trvalé identifikátory účastníků, což představovalo rizika pro soukromí a neefektivní správu relací. Architektura [CTS](/mobilnisite/slovnik/cts/) potřebovala mechanismus pro dočasnou identifikaci mobilních stanic během aktivních relací při zachování schopnosti mapovat tyto dočasné identity na trvalé záznamy účastníků pro účely účtování a správy.

Primární motivací pro vývoj CTSMSI bylo zvýšení ochrany soukromí účastníka v rámci CTS domény. Použitím dočasného identifikátoru namísto přenosu trvalého [IMSI](/mobilnisite/slovnik/imsi/) při každé signalizační výměně systém snižuje riziko sledování účastníka a krádeže identity. Tento přístup je v souladu se širšími bezpečnostními principy 3GPP, které minimalizují vystavování trvalých identifikátorů na rádiovém rozhraní. Dále CTSMSI umožňuje efektivnější správu relací tím, že síti dovoluje rychle identifikovat a spravovat aktivní zařízení [CTS-MS](/mobilnisite/slovnik/cts-ms/) bez neustálého odkazování se na backendové databáze účastníků.

Dalším klíčovým problémem, který CTSMSI řeší, je potřeba efektivní správy mobility v rámci oblastí pokrytí CTS. Struktura dočasného identifikátoru zahrnuje informace o obsluhující [CTS-FP](/mobilnisite/slovnik/cts-fp/), což usnadňuje rychlejší předávání spojení a aktualizace polohy, když se účastníci pohybují mezi různými pevnými částmi. Tato schopnost byla obzvláště důležitá pro podporu bezproblémového uživatelského zážitku bezšňůrové telefonie v prostředích, jako jsou firemní areály, obytné komplexy a další definované servisní oblasti, kde může být nasazeno více CTS-FP pro poskytnutí komplexního pokrytí.

## Klíčové vlastnosti

- Dočasná identifikace účastníka pro zvýšení ochrany soukromí
- Jednoznačné přidělení na relaci CTS-MS u konkrétní CTS-FP
- Podpora efektivní správy mobility mezi CTS-FP
- Umožňuje rychlé zřízení a ukončení relace
- Snižuje vystavení trvalého identifikátoru na rádiových rozhraních
- Umožňuje mapování na trvalé záznamy účastníků pro účely účtování

## Související pojmy

- [CTS-MS – Cordless Telephony System - Mobile Station](/mobilnisite/slovnik/cts-ms/)
- [CTS-FP – Cordless Telephony System - Fixed Part](/mobilnisite/slovnik/cts-fp/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [CTSMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctsmsi/)
