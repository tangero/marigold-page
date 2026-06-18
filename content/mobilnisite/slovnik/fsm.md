---
slug: "fsm"
url: "/mobilnisite/slovnik/fsm/"
type: "slovnik"
title: "FSM – Finite State Model"
date: 2025-01-01
abbr: "FSM"
fullName: "Finite State Model"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fsm/"
summary: "Formální model používaný k definici chování komunikačních protokolů, kdy systém může být v jednom z konečného počtu stavů a mezi nimi přechází na základě událostí. Je klíčový pro specifikaci jednoznač"
---

FSM je formální model pro definici chování protokolů, v němž systém existuje v jednom z konečného počtu stavů a mezi nimi přechází na základě událostí. Je klíčový pro specifikaci jednoznačných procedur v normách 3GPP.

## Popis

Finite State Model (FSM), známý také jako Finite State Machine (stavový automat s konečným počtem stavů), je abstraktní výpočetní model používaný k návrhu a popisu chování systému. V 3GPP specifikacích se používá k formální definici operačních procedur síťových entit a protokolů. Model se skládá z konečné množiny stavů, množiny vstupních událostí (nebo spouštěčů), množiny výstupních akcí a přechodové funkce, která mapuje stav a vstup na nový stav a případně výstup. Systém existuje vždy přesně v jednom stavu v libovolném daném čase. K přechodu do nového stavu dochází v reakci na událost, kterou může být přijetí zprávy, vypršení časovače nebo interní spouštěč.

Architektura FSM v 3GPP specifikaci protokolu je typicky prezentována pomocí diagramů stavových přechodů a doprovodných tabulek. Každý stav reprezentuje specifický režim činnosti protokolové entity. Například ve specifikacích řízení služeb IP Multimedia Subsystem (IMS) (TS 29.078, TS 29.278) FSM definují chování aplikačních serverů ([AS](/mobilnisite/slovnik/as/)) a bodů řízení služeb během řízení hovorové relace. Mezi klíčové součásti patří stavové proměnné (definující aktuální stav), fronta událostí a logika provádění akcí. Přechodová pravidla jsou detailně definována tak, aby pokrývala všechny normativní scénáře, včetně chybových stavů a abnormálních ukončení, čímž zajišťují konzistentní chování implementací od různých výrobců.

Princip činnosti FSM je procedurální: Protokolová entita se inicializuje do definovaného počátečního stavu (např. IDLE). Poté čeká na události. Po přijetí události entita zkontroluje přechodová pravidla pro svůj aktuální stav a tuto konkrétní událost. Pokud existuje odpovídající pravidlo, provede všechny přidružené akce (např. odešle [SIP](/mobilnisite/slovnik/sip/) zprávu, spustí časovač, aktualizuje interní proměnné) a následně přejde do určeného následujícího stavu. Pokud není pravidlo definováno, může být událost ignorována nebo způsobit chybu, jak je specifikováno. Tento deterministický model je zásadní pro testování shody (conformance testing), kdy jsou testovací sady navrženy tak, aby ověřily, že implementace správně následuje specifikované stavové přechody a akce pro všechny definované posloupnosti událostí.

## K čemu slouží

Účelem Finite State Model je poskytnout přesnou, jednoznačnou a implementovatelnou definici složitého chování komunikačních protokolů. Před zavedením těchto formálních modelů byly specifikace protokolů často popisovány textově, což mohlo vést k různým interpretacím u výrobců zařízení a následně k problémům s interoperabilitou. FSM tento problém řeší tím, že nabízí matematický a diagramatický formalismus, který ponechává minimální prostor pro nejednoznačnost, a přesně definuje, co musí systém dělat za všech možných okolností.

Historicky bylo přijetí stavových modelů v telekomunikacích hnací silou potřeby spolehlivosti a globální interoperability v digitálních sítích, jako je [SS7](/mobilnisite/slovnik/ss7/). V 3GPP, zejména pro řízení relací v IMS (od Release 5 dále), složitost toků hovorů a interakcí služeb vyžadovala rigorózní specifikační metodu. Přístup FSM řeší omezení neformálních popisů explicitním výčtem všech stavů, všech možných spouštěčů a všech požadovaných reakcí, což je kritické pro testování a certifikaci.

Motivací pro jeho pokračující používání napříč releasy je rostoucí složitost síťových služeb a množství síťových funkcí. Jak se protokoly vyvíjejí, aby podporovaly nové funkce, FSM poskytuje strukturovaný rámec pro přidávání nových stavů a přechodů, aniž by došlo k narušení stávající funkcionality. Slouží jako základní plán (blueprint), který inženýři používají pro vývoj protokolových zásobníků a testeři pro jejich ověřování, což zajišťuje předvídatelné a spolehlivé chování sítě pro koncové uživatele.

## Klíčové vlastnosti

- Definuje konečnou množinu diskrétních stavů reprezentujících podmínky protokolu
- Specifikuje deterministické přechody mezi stavy spouštěné událostmi
- Asociuje specifické výstupní akce se stavovými přechody
- Umožňuje jednoznačnou specifikaci a implementaci protokolů
- Usnadňuje testování shody (conformance testing) a validaci interoperability
- Poskytuje jasnou strukturu pro modelování složitého procedurálního chování

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [FSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsm/)
