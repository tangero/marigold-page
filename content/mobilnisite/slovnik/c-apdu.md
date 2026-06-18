---
slug: "c-apdu"
url: "/mobilnisite/slovnik/c-apdu/"
type: "slovnik"
title: "C-APDU – Command Application Protocol Data Unit"
date: 2025-01-01
abbr: "C-APDU"
fullName: "Command Application Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/c-apdu/"
summary: "C-APDU je standardizovaná příkazová struktura používaná v sítích 3GPP pro komunikaci mezi aplikacemi a čipovými kartami (UICC/USIM). Umožňuje zabezpečené provádění příkazů, jako je autentizace, přístu"
---

C-APDU je standardizovaná příkazová struktura používaná v sítích 3GPP pro zabezpečenou komunikaci mezi aplikacemi a čipovými kartami UICC/USIM, umožňující příkazy jako autentizace a přístup k souborům.

## Popis

Command Application Protocol Data Unit (C-APDU) je základní protokolová struktura definovaná ve specifikacích 3GPP pro komunikaci mezi koncovým zařízením ([TE](/mobilnisite/slovnik/te/)) a univerzální čipovou kartou (UICC), která obsahuje aplikaci [USIM](/mobilnisite/slovnik/usim/). Tento protokol vychází z normy [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-4 pro komunikaci s čipovými kartami a poskytuje standardizovaný formát pro odesílání příkazů na UICC. Struktura C-APDU se skládá z povinné hlavičky a volitelného těla, přičemž hlavička obsahuje bajt třídy (CLA), bajt instrukce (INS) a dva bajty parametrů (P1, P2), zatímco tělo obsahuje příkazová data a očekávanou délku odpovědi.

Během provozu koncové zařízení sestaví C-APDU s konkrétními parametry příkazu a odešle jej na UICC prostřednictvím rozhraní terminálu. UICC příkaz zpracuje a vrátí Response [APDU](/mobilnisite/slovnik/apdu/) ([R-APDU](/mobilnisite/slovnik/r-apdu/)) obsahující výsledky provedení. Tato výměna probíhá během různých síťových procedur včetně autentizace, přístupu k souborovému systému, výběru aplikace a zabezpečené výměny zpráv. Protokol podporuje operace typu case 1 (bez dat) i case 4 (jak příkazová, tak odpovědová data), přičemž pole Le v C-APDU udává očekávanou délku dat odpovědi.

Architektura C-APDU umožňuje zabezpečenou komunikaci prostřednictvím různých mechanismů, včetně zabezpečené výměny zpráv s kryptografickou ochranou, řetězení příkazů pro přenos velkých objemů dat a správy logických kanálů pro souběžný přístup aplikací. Mezi klíčové komponenty patří bajt CLA, který definuje třídu příkazu a požadavky na zabezpečenou komunikaci, bajt INS specifikující konkrétní operaci a bajty P1/P2 poskytující parametry specifické pro příkaz. Protokol také podporuje rozšířená pole pro délku pro zpracování větších datových bloků přesahujících 256 bajtů, což se stalo stále důležitějším se zaváděním složitějších aplikací USIM.

V rámci síťové architektury 3GPP jsou příkazy C-APDU nezbytné pro autentizaci účastníka prostřednictvím protokolu [AKA](/mobilnisite/slovnik/aka/), kdy síť zasílá autentizační vektory do USIM právě pomocí C-APDU. Protokol také usnadňuje správu souborového systému na UICC, včetně přístupu k [EF](/mobilnisite/slovnik/ef/) (Elementary File) a DF (Dedicated File), stejně jako správu aplikací pro Java Card aplety. Standardizovaný formát zajišťuje, že UICC od různých výrobců mohou spolupracovat se síťovým vybavením od různých dodavatelů, čímž se zachovává zásadní princip globální interoperability v mobilní telekomunikaci.

## K čemu slouží

Protokol C-APDU byl vytvořen za účelem zavedení standardizovaného příkazového rozhraní mezi mobilními terminály a čipovými kartami (UICC/USIM) v sítích 3GPP. Před standardizací různí výrobci používali proprietární příkazové struktury, což bránilo interoperabilitě a zvyšovalo složitost nasazení sítí. Přijetí normy ISO/IEC 7816-4 jako základu pro C-APDU zajistilo, že sítě 3GPP mohou využívat stávající technologii čipových karet při zachování kompatibility s globálními telekomunikačními standardy.

Hlavní problém, který C-APDU řeší, je potřeba univerzálního příkazového jazyka, který umožňuje zabezpečenou a spolehlivou komunikaci mezi síťovým vybavením a moduly identifikace účastníka. Tato standardizace byla obzvláště klíčová při vývoji mobilních sítí z 2G na 3G, který vyžadoval sofistikovanější autentizační mechanismy a podporu aplikací. Poskytnutím konzistentní příkazové struktury C-APDU umožňuje síťovým operátorům nasazovat UICC od více dodavatelů se zárukou, že budou správně fungovat se všemi kompatibilními síťovými zařízeními.

Historický kontext ukazuje, že rané mobilní systémy čelily problémům s interoperabilitou kvůli proprietárním implementacím. Zavedení C-APDU ve verzi Release 4 tyto omezení odstranilo vytvořením společného protokolového základu, který podporoval rostoucí složitost aplikací USIM. Tato standardizace umožnila pokročilé funkce, jako je zabezpečené stahování aplikací, vylepšené autentizační protokoly a podpora více aplikací na jedné UICC, a to vše při zachování zpětné kompatibility se stávajícími systémy.

## Klíčové vlastnosti

- Standardizovaná příkazová struktura založená na ISO/IEC 7816-4
- Podpora zabezpečené výměny zpráv s kryptografickou ochranou
- Schopnost rozšířené délky pro zpracování velkých datových bloků
- Správa logických kanálů pro souběžný přístup aplikací
- Zpětná kompatibilita napříč vydáními 3GPP
- Podpora pro příkazové operace typu case 1 i case 4

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [R-APDU – Response Application Protocol Data Unit](/mobilnisite/slovnik/r-apdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [C-APDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-apdu/)
