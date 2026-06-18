---
slug: "fsn"
url: "/mobilnisite/slovnik/fsn/"
type: "slovnik"
title: "FSN – Frame Sequence Number"
date: 2025-01-01
abbr: "FSN"
fullName: "Frame Sequence Number"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fsn/"
summary: "Číslo přiřazené datovým rámcům v sekvenci za účelem zajištění správného pořadí, detekce ztrát a podpory mechanismů retransmise. Je základním prvkem v protokolech linkové a transportní vrstvy v rozhran"
---

FSN (číslo sekvence rámce) je číslo sekvence rámce přiřazené datovým rámcům za účelem zajištění správného pořadí, detekce ztrát a podpory retransmisce v protokolech rozhraní UTRAN Iur a Iub.

## Popis

Frame Sequence Number (FSN) je pole v hlavičce protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), které identifikuje sekvenční pozici rámce v datovém proudu. V kontextu specifikací 3GPP pro [UTRAN](/mobilnisite/slovnik/utran/) (Universal Terrestrial Radio Access Network), zejména v protokolových zásobnících rozhraní Iur (rozhraní mezi [RNC](/mobilnisite/slovnik/rnc/)) a Iub (rozhraní mezi RNC a Node B), je FSN používáno Frame Protocol ([FP](/mobilnisite/slovnik/fp/)) a Data Stream Protocol. Jeho primární funkcí je umožnit přijímající entitě rekonstruovat původní pořadí vyslaných rámců, které mohou dorazit mimo pořadí kvůli stavu sítě, a identifikovat chybějící rámce.

Z architektonického hlediska FSN funguje v transportní vrstvě uživatelské roviny těchto rozhraní. Když je PDU vyšší vrstvy (např. [MAC](/mobilnisite/slovnik/mac/) PDU obsahující uživatelská data) předáno transportní vrstvě k přenosu přes Iub/Iur, je zapouzdřeno do rámce Frame Protocol. Vysílající entita přiřadí každému rámci v rámci konkrétního transportního kanálu nebo datového proudu monotónně rostoucí FSN. Prostor FSN je cyklický, což znamená, že se po dosažení maximální hodnoty (např. 0 až 4095) přeteče, což vyžaduje, aby přijímač zvládal přetečení pomocí algoritmů založených na oknech.

Jak to funguje, zahrnuje jak vysílací, tak přijímací procedury. Na straně odesílatele se FSN zvyšuje pro každý nový rámec na daném logickém spojení. Rámec se svým FSN je odeslán přes transportní síť (např. IP nebo [ATM](/mobilnisite/slovnik/atm/)). Na straně přijímače jsou přijaté rámce uloženy do bufferu. Přijímač používá FSN k umístění rámců do správného sekvenčního pořadí před jejich předáním vyšší vrstvě. Pokud je přijat rámec s FSN, které není následující očekávané, indikuje to mezeru – potenciálně ztracený nebo nadměrně zpožděný rámec. V závislosti na konkrétním protokolu a konfiguraci to může vyvolat žádost o retransmisi (pokud je podporována) nebo být nahlášeno systémům provozu a údržby. FSN je tedy kritickou součástí pro doručování ve správném pořadí, což je klíčový aspekt kvality služby (QoS) pro vyhrazené kanály.

## K čemu slouží

FSN existuje k řešení základních problémů paketových transportních sítí: doručování mimo pořadí a ztráty paketů. V architektuře [UTRAN](/mobilnisite/slovnik/utran/) používají rozhraní Iub a Iur paketově přepínaný transport (původně [ATM](/mobilnisite/slovnik/atm/), později IP). Tyto sítě negarantují pořadí ani doručení paketů. Bez sekvenčních čísel by Radio Network Controller (RNC) nebo Node B nebyl schopen správně zrekonstruovat proud uživatelských dat, což by vedlo k předání poškozených informací na rádiové rozhraní nebo k nesprávným rozhodnutím o předání spojení.

Historicky dřívější okruhově přepínaná spojení inherentně zachovávala pořadí. Migrace na paketovou páteřní síť z důvodu nákladů a flexibility tento problém přinesla. FSN poskytuje jednoduchý, nenáročný mechanismus pro opětovné zavedení pořadí a spolehlivosti ve vrstvě, kde je to potřeba – mezi RNC a Node B – bez spoléhání se na složité transportní protokoly jako TCP, které by mohly zavést nepřijatelnou latenci pro real-time rádiový provoz. Řeší tak omezení použití 'best-effort' transportní sítě pro přenos časově citlivých a na pořadí závislých dat rádiového rozhraní.

Jeho vytvoření bylo motivováno potřebou robustního, efektivního řídicího mechanismu přizpůsobeného real-time požadavkům buněčných sítí. Tím, že umožňuje doručování ve správném pořadí a detekci ztrát na úrovni Frame Protocol, umožňuje FSN RAN udržovat vysokou integritu dat a podporovat plynulou mobilitu (např. během měkkého předání spojení, kdy jsou data rozdělena přes více Iub spojení). Je to základní prvek, který zajišťuje integritu dat uživatelské roviny přes transportní síť RAN, což je nezbytné pro udržení kvality služby (QoS) koncového uživatele.

## Klíčové vlastnosti

- Poskytuje sekvenční číslování rámců v datovém proudu
- Umožňuje přijímací straně přeřazení rámců přijatých mimo pořadí
- Umožňuje detekci ztracených nebo chybějících rámců identifikací mezer v sekvenci
- Typicky používá cyklický číselný prostor (např. modulo 4096)
- Funguje v rámci Frame Protocol uživatelské roviny rozhraní Iub/Iur
- Podporuje QoS zajištěním doručování ve správném pořadí pro vyhrazené kanály

## Definující specifikace

- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [FSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsn/)
