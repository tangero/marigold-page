---
slug: "cpi"
url: "/mobilnisite/slovnik/cpi/"
type: "slovnik"
title: "CPI – Content Protection Information"
date: 2025-01-01
abbr: "CPI"
fullName: "Content Protection Information"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cpi/"
summary: "CPI je bezpečnostní mechanismus v sítích 3GPP, který poskytuje informace pro ochranu multimediálního obsahu, zejména ve službě Multimedia Messaging Service (MMS). Umožňuje zabezpečené doručování obsah"
---

CPI je bezpečnostní mechanismus 3GPP pro ochranu multimediálního obsahu, například v MMS, který specifikuje šifrování, správu klíčů a práva k užití, aby zajistil pouze autorizovaný přístup.

## Popis

Content Protection Information (CPI) je standardizovaný bezpečnostní rámec ve specifikacích 3GPP, který definuje, jak má být multimediální obsah chráněn během přenosu a uložení v mobilních sítích. Mechanismus funguje tak, že vkládá metadata ochrany do protokolu pro doručování obsahu, konkrétně do zpráv [MMS](/mobilnisite/slovnik/mms/), jak je definováno v 3GPP TS 23.140 a souvisejících specifikacích. Tato metadata zahrnují klíčové bezpečnostní parametry, které přijímajícímu zařízení sdělují, jak má s chráněným obsahem nakládat, včetně postupů dešifrování a vymáhání práv k užití.

Z architektonického hlediska CPI funguje jako bezpečnostní vrstva v protokolech na aplikační úrovni a spolupracuje s podpůrnými transportními bezpečnostními mechanismy. Při přípravě obsahu k distribuci poskytovatel obsahu nebo původní aplikace vygeneruje CPI, které specifikuje schéma ochrany (například [OMA](/mobilnisite/slovnik/oma/) [DRM](/mobilnisite/slovnik/drm/) 1.0 nebo novější verze), šifrovací algoritmy, identifikátory klíčů a výrazy práv. Tyto informace jsou pak zabaleny spolu se zašifrovaným obsahem a přenášeny systémem MMS. Klient MMS a agent DRM v přijímacím zařízení interpretují CPI, aby určili, zda má uživatel potřebná práva a klíče pro přístup k obsahu.

Mezi klíčové komponenty rámce CPI patří identifikátor metody ochrany, který specifikuje použitý systém DRM; informace o šifrovacím klíči obsahu, které mohou zahrnovat identifikátory klíčů nebo odkazy na systémy správy klíčů; informace o právech, které definují povolení k užití (jako počet přehrání, data expirace nebo omezení přenosu); a mechanismy ochrany integrity, které zabraňují manipulaci s CPI samotným. Systém spoléhá na standardizovaná rozhraní mezi klientem MMS, agentem DRM a mediálními přehrávači na zařízení, aby zajistil konzistentní vymáhání politik ochrany obsahu napříč různými implementacemi.

V síťové architektuře CPI interaguje s několika prvky včetně MMS centra (MMSC), které může CPI přeposlat beze změny nebo může přidat informace o ochraně specifické pro síť. MMSC obvykle CPI nedešifruje ani neinterpretuje, ale zajišťuje jeho správné doručení příjemcům. Ve složitějších scénářích zahrnujících získávání práv může CPI obsahovat odkazy na servery pro vydávání práv, které musí zařízení kontaktovat, aby získalo dešifrovací klíče nebo další práva k užití. Toto oddělení doručování obsahu a získávání práv umožňuje flexibilní obchodní modely při zachování silné ochrany obsahu.

Role CPI přesahuje jednoduché šifrování obsahu a umožňuje ekosystémy správy digitálních práv v mobilních sítích. Poskytnutím standardizovaného způsobu komunikace požadavků na ochranu umožňuje poskytovatelům obsahu nasazovat chráněný obsah napříč více sítěmi operátorů a typy zařízení s konzistentním vymáháním zabezpečení. Rámec podporuje jak modely forward-lock (jednoduchá ochrana, kde obsah nelze přeposílat), tak combined delivery (kde jsou práva doručena spolu s obsahem), a je rozšiřitelný pro modely separate delivery, kde se práva získávají odděleně od obsahu.

## K čemu slouží

CPI bylo vytvořeno, aby řešilo rostoucí potřebu zabezpečené distribuce prémiového multimediálního obsahu přes mobilní sítě, zejména když [MMS](/mobilnisite/slovnik/mms/) získalo na popularitě na počátku 21. století. Před standardizací CPI měli poskytovatelé obsahu omezené možnosti, jak chránit svůj duševní vlastnictví při doručování obsahu do mobilních zařízení, což vedlo buď k nechráněné distribuci (umožňující pirátství), nebo k proprietárním řešením, která fragmentovala trh a vytvářela problémy s interoperabilitou. 3GPP uznalo, že pro rozvoj mobilních multimediálních služeb je nezbytný standardizovaný mechanismus ochrany obsahu, aby se vytvořila důvěra mezi poskytovateli obsahu, síťovými operátory a spotřebiteli.

Primární problém, který CPI řeší, je umožnění zabezpečené komerční distribuce obsahu při zachování interoperability mezi různými síťovými operátory a výrobci zařízení. Bez standardizovaného přístupu by každý poskytovatel obsahu nebo operátor musel implementovat vlastní schémata ochrany, což by uživatelům ztěžovalo přístup k obsahu z více zdrojů a zvyšovalo složitost pro výrobce zařízení, kteří by museli podporovat více nekompatibilních systémů [DRM](/mobilnisite/slovnik/drm/). CPI poskytuje společný rámec, který specifikuje, jak mají být informace o ochraně komunikovány, což umožňuje různým systémům DRM vzájemně spolupracovat v rámci stejné doručovací infrastruktury.

Historický kontext ukazuje, že vývoj CPI se časově shodoval s nástupem MMS jako klíčové služby generující příjmy pro mobilní operátory. Když operátoři chtěli nabízet vyzváněcí tóny, obrázky, videa a další prémiový obsah přes MMS, potřebovali záruku, že tento obsah lze chránit před neoprávněným šířením. Omezení předchozích přístupů zahrnovala buď žádnou ochranu (vedoucí ke ztrátě příjmů), nebo proprietární systémy, které uzamkly uživatele do specifických ekosystémů obsahu. CPI, zavedené ve verzi 5, poskytlo chybějící standardizační vrstvu, která umožnila růst trhů s mobilním obsahem při ochraně práv duševního vlastnictví.

## Klíčové vlastnosti

- Standardizovaný formát metadat ochrany pro multimediální obsah
- Interoperabilita mezi různými systémy DRM a implementacemi zařízení
- Podpora více modelů ochrany obsahu včetně forward-lock a combined delivery
- Integrace se zásobníkem protokolů MMS pro bezproblémové doručování obsahu
- Rozšiřitelný rámec podporující různé šifrovací algoritmy a systémy správy klíčů
- Jazyk pro vyjádření práv k definování povolení a omezení užití

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [DRM – Data call Routeing Mechanism](/mobilnisite/slovnik/drm/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study

---

📖 **Anglický originál a plná specifikace:** [CPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpi/)
