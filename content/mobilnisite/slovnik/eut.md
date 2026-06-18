---
slug: "eut"
url: "/mobilnisite/slovnik/eut/"
type: "slovnik"
title: "EUT – Equipment Under Test"
date: 2025-01-01
abbr: "EUT"
fullName: "Equipment Under Test"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eut/"
summary: "Standardizovaný termín pro uživatelské zařízení (UE) nebo UE s příslušným příslušenstvím, které je testováno v konformních a výkonnostních testovacích specifikacích 3GPP. Definuje zařízení podrobené z"
---

EUT je standardizovaný termín pro uživatelské zařízení (User Equipment) nebo zařízení testované v rámci specifikací 3GPP, aby bylo zajištěno, že splňuje požadavky sítě a rádiového rozhraní.

## Popis

Equipment Under Test (EUT) je formální označení používané v technických specifikacích 3GPP, především v řadách 3GPP TS 25, 36 a 37, které definují testovací metodologie pro uživatelská zařízení. Odkazuje na konkrétní zařízení UE nebo na UE v kombinaci s nezbytným příslušenstvím, jako jsou testovací adaptéry nebo specifické antény, které je předmětem konformního, rádiového nebo výkonnostního testování. EUT je řízenou entitou v testovacím uspořádání, vůči které jsou prováděny všechny testovací případy a měřicí postupy za účelem ověření shody se standardy 3GPP.

Role EUT je klíčová pro proces certifikace a schvalování typu mobilních zařízení. Testovací specifikace podrobně definují testovací podmínky, konfigurace a kritéria úspěšnosti/neúspěšnosti pro EUT napříč různými provozními scénáři, včetně charakteristik vysílače a přijímače, správy rádiových zdrojů, signalizačních protokolů a výkonu end-to-end. EUT musí být konfigurováno v konkrétním, opakovatelném stavu (např. konkrétní výkonová třída, podporovaná pásma a aktivované funkce), aby byly výsledky testů reprodukovatelné a srovnatelné mezi různými testovacími laboratořemi.

Klíčové součásti definice EUT zahrnují jeho [RF](/mobilnisite/slovnik/rf/) konektory, podporovaná kmitočtová pásma, výkonové třídy a konkrétní implementace testovaného protokolového zásobníku. Testovací specifikace podrobně popisují, jak EUT rozhraní s testovacím systémem, kterým je často emulátor základnové stanice nebo tester rádiové komunikace. Měření prováděná na EUT zahrnují výstupní výkon, kmitočtovou chybu, přesnost modulace ([EVM](/mobilnisite/slovnik/evm/)), citlivost přijímače, charakteristiky blokování a správnost signalizace protokolů. Důsledným testováním EUT zajišťuje 3GPP, že komerční zařízení UE budou spolehlivě fungovat a nebudou způsobovat škodlivé rušení v živých sítích, čímž je garantována základní úroveň výkonu a interoperability pro koncové uživatele.

## K čemu slouží

Koncept EUT existuje, aby poskytoval jasný, jednoznačný referenční bod v testovacích specifikacích 3GPP. Před zavedením standardizovaného testování byla interoperabilita zařízení významnou výzvou, protože výrobci mohli standardy implementovat s drobnými odchylkami vedoucími k selhání sítě nebo špatnému uživatelskému zážitku. Definice 'zařízení podrobeného testu' formalizuje hodnocené zařízení, odděluje jej od testovací instrumentace a vytváří konzistentní rámec pro certifikaci.

Jeho vytvoření bylo motivováno potřebou globálního, harmonizovaného procesu schvalování typu pro mobilní terminály. Jak se buněčná technologie vyvíjela od 2G přes 3G (UMTS) až po 4G (LTE), složitost rádiové části a protokolů exponenciálně rostla. Bylo nutné definovat standardizovaný testovací objekt pro vývoj opakovatelných, objektivních testovacích případů, které mohou být provedeny nezávislými testovacími laboratořemi po celém světě. To zajišťuje, že jakékoli zařízení UE nesoucí certifikační značku prošlo prokazatelně stejnou přísnou sadou testů, což posiluje důvěru spotřebitelů a umožňuje globální roaming.

Označení EUT řeší omezení ad-hoc testovacích metodologií. Specifikuje přesně, co je testováno (např. [RF](/mobilnisite/slovnik/rf/) přední část UE, nikoli celé zařízení včetně nebuněčných komponent), za jakých podmínek a s jakými rozhraními. Tato přesnost je klíčová pro testování pokročilých funkcí, jako je agregace nosných, [MIMO](/mobilnisite/slovnik/mimo/) a úsporné stavy napájení, kde musí být chování EUT přesně řízeno a měřeno, aby byla ověřena shoda se standardem.

## Klíčové vlastnosti

- Standardizovaná reference pro veškeré konformní a výkonnostní testování UE
- Zahrnuje UE a jakékoli povinné příslušenství pro testování
- Definováno specifickými RF a protokolovými konfiguracemi pro reprodukovatelnost testů
- Centrální entita pro měření charakteristik vysílače a přijímače
- Předmět přísných testů validace signalizace protokolů a procedur
- Základ pro globální schvalování typu a certifikaci interoperability sítě

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.127** (Rel-18) — UICC-terminal interaction testing specification
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.113** (Rel-19) — EMC Requirements for E-UTRA Base Stations
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.114** (Rel-19) — EMC Requirements for NR Repeaters and NCR
- **TS 38.124** (Rel-19) — NR UE EMC Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [EUT na 3GPP Explorer](https://3gpp-explorer.com/glossary/eut/)
