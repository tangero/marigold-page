---
slug: "e-rucch"
url: "/mobilnisite/slovnik/e-rucch/"
type: "slovnik"
title: "E-RUCCH – E-DCH Random Access Uplink Control Channel"
date: 2025-01-01
abbr: "E-RUCCH"
fullName: "E-DCH Random Access Uplink Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-rucch/"
summary: "Řídicí kanál v uplinku v UMTS TDD používaný pro procedury náhodného přístupu ve vylepšeném uplinku. Umožňuje UE žádat o prostředky pro přenos E-DCH, když nejsou v aktivním stavu, což usnadňuje rychlé"
---

E-RUCCH je řídicí kanál v uplinku v UMTS TDD používaný pro procedury náhodného přístupu ve vylepšeném uplinku, který umožňuje UE žádat o prostředky E-DCH, když nejsou aktivní, za účelem snížení latence.

## Popis

[E-DCH](/mobilnisite/slovnik/e-dch/) Random Access Uplink Control Channel (E-RUCCH) je fyzický kanál v uplinku specifikovaný ve standardech 3GPP UMTS pro režim Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)). Je součástí rámce Enhanced Uplink (E-DCH), který zlepšuje výkon přenosu paketových dat v uplinku v sítích UMTS. E-RUCCH používá uživatelské zařízení (UE) k zahájení procedur náhodného přístupu, když potřebuje vysílat data v uplinku, ale nemá aktivní prostředek E-DCH. Tento kanál přenáší řídicí informace, jako jsou žádosti o plánování a hlášení o stavu bufferu, k Node B, což síti umožňuje rychle přidělit odpovídající prostředky pro uplink. E-RUCCH funguje na principu soutěžení, což znamená, že více UE se o něj může pokoušet současně, což vyžaduje mechanismy pro řešení kolizí.

Z architektonického hlediska je E-RUCCH mapován na konkrétní časové sloty a kódy v uplinku ve struktuře TDD rámce. Využívá prostředky fyzického kanálu pro náhodný přístup ([PRACH](/mobilnisite/slovnik/prach/)), ale je upraven pro účely E-DCH. Přenos na E-RUCCH zahrnuje vyslání preambule následované datovou částí zprávy, která obsahuje podrobnosti jako identitu UE, požadovanou velikost prostředku a rezervu výkonu. Node B tyto přenosy detekuje a reaguje na ně přiděleními na downlinkových kanálech, jako je E-DCH Absolute Grant Channel ([E-AGCH](/mobilnisite/slovnik/e-agch/)). Konstrukce E-RUCCH zahrnuje procedury navyšování výkonu a backoff pro zvládání kolizí a zajištění spolehlivého přístupu za různých podmínek zatížení.

Jak funguje: Když má UE data k odeslání, ale nemá aktivní přidělení E-DCH, vybere příležitost pro náhodný přístup na E-RUCCH na základě dostupných slotů a kódů. Vysílá preambuli, aby upoutala pozornost Node B, a pokud je potvrzena, pokračuje datovou částí zprávy. Node B tyto informace zpracuje a přidělí prostředky E-DCH prostřednictvím signalizace v downlinku. Tento proces snižuje čas potřebný k navázání přenosů v uplinku ve srovnání s tradičními kanály pro náhodný přístup, které jsou pomalejší a méně optimalizované pro paketová data. E-RUCCH hraje klíčovou roli při minimalizaci latence pro přístup k paketovým datům v uplinku, zejména u trhavého provozu jako je prohlížení webu nebo instant messaging, tím, že umožňuje rychlé žádosti o prostředky a jejich přidělování.

## K čemu slouží

E-RUCCH byl vytvořen, aby řešil omezení stávajících kanálů pro náhodný přístup v UMTS [TDD](/mobilnisite/slovnik/tdd/) pro podporu služeb Enhanced Uplink. Před zavedením [E-DCH](/mobilnisite/slovnik/e-dch/) přenos dat v uplinku v TDD spoléhal na Random Access Channel ([RACH](/mobilnisite/slovnik/rach/)), který byl navržen pro počáteční přístup a malé datové přenosy, ale postrádal efektivitu pro vysokorychlostní paketová data. Procedury RACH byly pomalejší a nebyly integrovány s rychlými plánovacími mechanismy, což vedlo k vyšší latenci a nižší propustnosti pro aplikace vyžadující časté přenosy v uplinku. Se zavedením Enhanced Uplink ve vydání 6 vznikla potřeba specializovaného kanálu pro náhodný přístup, který by uměl rychle žádat o prostředky E-DCH, v souladu s cílem zlepšit výkon uplinku.

Motivace pro E-RUCCH vycházela ze snahy zkrátit dobu navazování pro relace paketových dat v uplinku v režimu TDD. Tím, že poskytuje kanál speciálně pro náhodný přístup E-DCH, řeší problém neefektivních mechanismů žádostí o prostředky, které by mohly omezit tok dat v uplinku. To umožňuje UE rychle přejít z klidového nebo neaktivního stavu do aktivního přenosu E-DCH, podporuje služby s nízkou latencí a lepší využití prostředků. E-RUCCH zlepšuje celkový uživatelský zážitek tím, že umožňuje rychlejší uploady a responsivnější aplikace, čímž splňuje požadavky vyvíjejícího se využívání mobilních dat v sítích 3G.

## Klíčové vlastnosti

- Používá se pro náhodný přístup k žádosti o prostředky E-DCH v UMTS TDD
- Přenáší řídicí informace jako žádosti o plánování a stav bufferu
- Funguje na principu soutěžení s řešením kolizí
- Mapován na časové sloty a kódy v uplinku ve struktuře TDD rámce
- Podporuje rychlé navázání přenosů paketových dat v uplinku
- Integruje se s plánovacími mechanismy E-DCH pro nízkou latenci

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)

## Definující specifikace

- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [E-RUCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-rucch/)
