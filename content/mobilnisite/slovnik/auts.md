---
slug: "auts"
url: "/mobilnisite/slovnik/auts/"
type: "slovnik"
title: "AUTS – Re-synchronisation Token"
date: 2025-01-01
abbr: "AUTS"
fullName: "Re-synchronisation Token"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/auts/"
summary: "AUTS je bezpečnostní token používaný v sítích 3GPP pro opětovnou synchronizaci pořadového čísla (SQN) mezi uživatelským zařízením (UE) a Autentizačním centrem (AuC) během protokolu AKA. Generuje jej U"
---

AUTS je bezpečnostní token generovaný UE pro opětovnou synchronizaci pořadového čísla s Autentizačním centrem sítě při selhání synchronizace protokolu AKA.

## Popis

AUTS (Re-synchronisation Token) je základní součást protokolu 3GPP Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), který je speciálně navržen pro řešení selhání synchronizace pořadového čísla ([SQN](/mobilnisite/slovnik/sqn/)). Protokol AKA spoléhá na čítač, SQN, který je nezávisle udržován Autentizačním centrem (AuC) v síti a univerzálním účastnickým identifikačním modulem ([USIM](/mobilnisite/slovnik/usim/)) v zařízení uživatele. Tento SQN se musí s každým pokusem o autentizaci zvýšit, aby se zabránilo replay útokům. Kvůli problémům v síti, chybám ve správě stavu nebo použití USIM v jiné síti však může očekávaný SQN USIM překročit přijatelné rozmezí SQN přijatého ze sítě, což způsobí selhání autentizace.

Když k takovému selhání synchronizace dojde, UE (konkrétně USIM) autentizaci nejen prostě odmítne. Místo toho spustí proceduru opětovné synchronizace. V rámci této procedury UE vytvoří token AUTS. AUTS je spojením dvou hlavních prvků: SQN skrytého před sítí (SQN_[MS](/mobilnisite/slovnik/ms/)) a kódu autentizace zprávy ([MAC-S](/mobilnisite/slovnik/mac-s/)). SQN_MS je aktuální odhad pořadového čísla USIM, skrytý pomocí klíče anonymity ([AK](/mobilnisite/slovnik/ak/)) pro ochranu soukromí identity účastníka. MAC-S je kryptografický kontrolní součet vypočítaný nad SQN_MS pomocí klíče pro opětovnou synchronizaci (K) a specifického algoritmu (f1*), který zajišťuje integritu a autentizaci žádosti o opětovnou synchronizaci.

UE odešle tento token AUTS zpět do sítě v rámci zprávy odpovědi na selhání autentizace. Po přijetí jej obsluhující síť (např. [VLR](/mobilnisite/slovnik/vlr/)/[SGSN](/mobilnisite/slovnik/sgsn/) nebo MME) přepošle do domovské sítě účastníka (HLR/HSS). HSS/AuC následně AUTS zpracuje. Nejprve extrahuje skrytý SQN_MS aplikací klíče anonymity (AK), který je odvozen ze sdíleného tajného klíče (K) a náhodné výzvy (RAND). Poté ověří MAC-S pomocí stejného algoritmu f1* a sdíleného klíče K. Pokud je MAC-S platný, AuC přijme SQN_MS od UE jako nové, správné pořadové číslo, aktualizuje svou interní databázi a vygeneruje nový autentizační vektor s čerstvým SQN, který je synchronizován s UE.

Celý tento proces umožňuje síti zotavit se z desynchronizovaného stavu bez nutnosti manuálního zásahu nebo trvalého odepření služby uživateli. Mechanismus AUTS je integrován do standardního toku odpovědi na autentizaci (specifikovaného v TS 33.102 a souvisejících specifikacích), což zajišťuje, že je nedílnou součástí síťových bezpečnostních operací. Jeho návrh zajišťuje, že samotná opětovná synchronizace je bezpečná, protože MAC-S dokazuje, že žádost pochází od legitimního USIM disponujícího správným tajným klíčem, a brání tak zlomyslným aktérům vynutit reset pořadového čísla.

## K čemu slouží

Token AUTS byl vytvořen pro řešení kritického problému robustnosti v protokolu 3GPP AKA. Bezpečnost původního protokolu AKA silně závisela na synchronizaci čítače SQN mezi sítí a USIM. Bez mechanismu obnovy by jakákoliv přetrvávající neshoda – způsobená chybami v síťové databázi, použitím USIM v jiné síti s jiným prostorem SQN nebo jinými provozními závadami – trvale blokovala účastníka před autentizací, což by vedlo k odepření služby. To byl pro komerční mobilní sítě nepřijatelný problém spolehlivosti.

Před standardizací procedury založené na AUTS v 3GPP bylo řešení takových selhání nestandardní a potenciálně nezabezpečené. Operátoři mohli spoléhat na manuální resetování nebo proprietární záložní metody, které mohly ohrozit bezpečnost. Zavedení AUTS v Release 6 poskytlo standardizovanou, kryptograficky zabezpečenou metodu pro automatickou obnovu. Odstranilo tím omezení dřívějšího, rigidnějšího toku AKA přidáním zpětné vazby od UE k AuC, což umožnilo síti být korigována stavem klienta kontrolovaným způsobem.

Motivací bylo zlepšit jak bezpečnost, tak dostupnost služeb sítí 3G (a později 4G/5G). Zajišťuje, že silná vzájemná autentizace AKA je zachována, aniž by byla křehká. Řešením problému synchronizace SQN AUTS předchází třídě selhání, která by jinak mohla být zneužita pro útoky typu odepření služby nebo vést ke špatné zákaznické zkušenosti, čímž činí celkovou bezpečnostní architekturu odolnější a operátorsky přívětivější.

## Klíčové vlastnosti

- Umožňuje bezpečné obnovení při neshodě pořadového čísla (SQN) v protokolu AKA
- Obsahuje skrytou verzi pořadového čísla UE (SQN_MS) pro ochranu soukromí
- Obsahuje kód autentizace zprávy (MAC-S) pro ověření pravosti žádosti o opětovnou synchronizaci
- Zabraňuje útokům typu odepření služby vyplývajícím z trvalých selhání autentizace
- Funguje v rámci standardního toku zprávy odpovědi na selhání autentizace
- Umožňuje HSS/AuC bezpečně aktualizovat svůj záznam SQN na základě legitimního vstupu od UE

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 33.223** (Rel-19) — GBA Push Function Specification
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TS 35.234** (Rel-19) — MILENAGE-256 Algorithm Set Specification

---

📖 **Anglický originál a plná specifikace:** [AUTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/auts/)
