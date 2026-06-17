---
slug: "eds"
url: "/mobilnisite/slovnik/eds/"
type: "slovnik"
title: "EDS – Enhanced Dialled Services"
date: 2025-01-01
abbr: "EDS"
fullName: "Enhanced Dialled Services"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eds/"
summary: "Enhanced Dialled Services (EDS) je funkce 3GPP, která poskytuje pokročilé zpracování hovorů a doplňkové služby nad rámec základního vytáčení. Umožňuje síťovým operátorům nabízet bohatší telefonní služ"
---

EDS je funkce 3GPP, která poskytuje pokročilé zpracování hovorů a doplňkové služby nad rámec základního vytáčení, umožňující bohatší telefonní služby, jako je podmíněné přesměrování hovoru a vylepšená identifikace volajícího.

## Popis

Enhanced Dialled Services (EDS) je standardizovaná sada schopností definovaná v rámci jádrové sítě 3GPP, konkrétně v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně. Funguje jako rozšíření tradičních mechanismů vytáčení a řízení hovorů, řízených protokoly v jádrové síti. Z architektonického hlediska jsou funkce EDS implementovány v síťových entitách, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), které komunikují s uživatelským zařízením (UE) prostřednictvím signalizačních protokolů. Servisní logika pro EDS je definována v rámci [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic) nebo jako nativní funkce MSC/HLR, což umožňuje provádění složitých servisních skriptů spouštěných specifickými vzory vytáčení nebo profily účastníka.

Princip fungování EDS zahrnuje zachycení a analýzu vytáčeného čísla nebo servisního kódu sítí. Když uživatel zahájí hovor nebo aktivaci doplňkové služby, MSC zkontroluje vytáčené číslice vůči sadě předdefinovaných pravidel a datům účastníka z HLR. Pokud je nalezena shoda s funkcí EDS, MSC vyvolá odpovídající servisní logiku. Tato logika může upravit postup zpracování hovoru – například přesměrováním hovoru na jiné číslo na základě denní doby, uplatněním specifických tarifů nebo prezentací vylepšených informací o identitě volajícího volané straně. Provedení je pro koncového uživatele transparentní, který jednoduše zaznamená výsledek vylepšené služby.

Klíčové komponenty umožňující EDS zahrnují servisní řídicí logiku, databázi účastníků (HLR) a funkci řízení hovorové relace v rámci MSC. Specifikace, především 3GPP TS 23.078 a TS 29.078, podrobně popisují signalizační toky a informační elementy vyžadované mezi těmito síťovými uzly pro podporu EDS. Jejím úkolem je obohatit paletu základních telefonních služeb a poskytnout standardizovaný způsob, jak mohou operátoři nasazovat konzistentní, pokročilé funkce hovorů ve svých sítích, čímž překračují pouhou hlasovou konektivitu směrem k inteligentnímu řízení hovorů.

## K čemu slouží

EDS bylo vytvořeno jako odpověď na rostoucí tržní poptávku po inteligentnějších a flexibilnějších telefonních službách nad rámec prostých hlasových hovorů. Před jeho standardizací byly doplňkové služby často základní, proprietární nebo omezeného rozsahu, což vedlo k problémům s interoperabilitou a pomalému tempu inovací. Mezi omezení předchozích přístupů patřil nedostatek síťové inteligence pro podmíněné zpracování hovorů a neschopnost snadno vytvářet přizpůsobené služby pro různé segmenty účastníků.

Historický kontext spočívá ve vývoji od sítí GSM 2G k UMTS 3G, kdy operátoři usilovali o zvýšení průměrného výnosu na uživatele ([ARPU](/mobilnisite/slovnik/arpu/)) zaváděním služeb s přidanou hodnotou. EDS, zavedené ve verzi 6, poskytlo rámec v jádrové síti pro implementaci těchto služeb standardizovaným způsobem. Vyřešilo problém servisních komor definováním společné sady vylepšených postupů vytáčení a provádění servisní logiky, což umožnilo funkce jako víceramenné hovory, pokročilé blokování hovorů a personalizované směrování hovorů na základě komplexních kritérií.

V konečném důsledku EDS motivovalo vytvoření jádrové sítě více orientované na služby, což umožnilo operátorům konkurovat na základě rozdílnosti služeb, nikoli pouze pokrytí nebo ceny. Položilo základy pro konvergenci telefonie s koncepty inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a zajistilo, že mobilní sítě mohly nabízet bohatost služeb srovnatelnou nebo překonávající tehdejší pevné sítě.

## Klíčové vlastnosti

- Podmíněné přesměrování hovoru na základě pravidel definovaných účastníkem
- Vylepšená prezentace (CLIP) a omezení (CLIR) identifikace volající linky
- Síťové třídění a blokování hovorů s více kritérii
- Podpora specializovaných vytáčecích kódů a servisních spouštěčů
- Integrace s CAMEL pro přizpůsobenou aplikační logiku
- Standardizovaná signalizace mezi MSC, HLR a dalšími uzly jádra pro provádění služeb

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [EDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/eds/)
