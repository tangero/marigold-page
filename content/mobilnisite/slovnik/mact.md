---
slug: "mact"
url: "/mobilnisite/slovnik/mact/"
type: "slovnik"
title: "MACT – Message Authentication Code T"
date: 2025-01-01
abbr: "MACT"
fullName: "Message Authentication Code T"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mact/"
summary: "MACT je konkrétní hodnota Message Authentication Code (MAC) označená jako T, vygenerovaná během algoritmu AES-CMAC. Je to klíčová součást bezpečnostních protokolů 3GPP pro zajištění integrity dat a au"
---

MACT je konkrétní hodnota Message Authentication Code označená jako T, vygenerovaná algoritmem AES-CMAC, která zajišťuje integritu dat a autentizaci původu v bezpečnostních protokolech 3GPP pro systémy EPS a 5G.

## Popis

Message Authentication Code T (MACT) je kryptografický výstup definovaný v bezpečnostních specifikacích 3GPP, konkrétně TS 33.401. Je výsledkem algoritmu AES-CMAC (Cipher-based Message Authentication Code), což je [MAC](/mobilnisite/slovnik/mac/) funkce založená na blokové šifře. Písmeno 'T' konkrétně označuje konečnou hodnotu MAC vyprodukovanou tímto algoritmem. V architekturách 3GPP se AES-CMAC, a tedy i MACT, používá pro ochranu integrity a autentizaci v různých mechanismech odvozování klíčů a ochrany signalizace.

Z architektonického hlediska se MACT generuje v bezpečnostních modulech síťových prvků, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a User Equipment (UE). Výpočet zahrnuje šifrovací algoritmus [AES](/mobilnisite/slovnik/aes/) pracující v režimu CMAC. Vstupy typicky zahrnují tajný klíč (např. Kasme v EPS) a řetězec zprávy, který často sestává z různých síťových parametrů (např. identita obsluhující sítě, pořadová čísla). Algoritmus zpracuje tyto vstupy sérií kryptografických operací, aby vytvořil výstup pevné délky (např. 128-bitů), což je MACT.

Jeho role je klíčová v odvozování hierarchie klíčů. Například v EPS [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement) se hodnoty MACT používají jako stavební bloky pro výpočet konkrétních kryptografických klíčů, jako je Kenb (klíč pro přístupovou síť). Integrita procesu odvozování klíčů závisí na bezpečnostních vlastnostech AES-CMAC; jakákoliv změna ve vstupní zprávě by vytvořila zcela odlišný MACT, a tím by zabránila odvození správných relakčních klíčů. Dále může být MACT přímo použit v signalizačních zprávách pro zajištění ochrany integrity, což umožňuje přijímající entitě ověřit, že zpráva nebyla pozměněna a pochází od legitimního zdroje disponujícího správným klíčem.

## K čemu slouží

MACT a podkladový algoritmus AES-CMAC byly zavedeny za účelem poskytnutí robustního, standardizovaného kryptografického mechanismu pro integritu a autentizaci v systémech 3GPP, který nahradil dřívější algoritmy. Vývoj od 3G k 4G (EPS) vyžadoval silnější a efektivnější bezpečnostní algoritmy. AES-CMAC byl přijat díky kryptografické síle blokové šifry [AES](/mobilnisite/slovnik/aes/) a prokazatelné bezpečnosti režimu provozu CMAC.

Řeší kritický problém zajištění integrity bezpečnostně kritických parametrů používaných při odvozování klíčů. Bez takového mechanismu by útočník mohl potenciálně manipulovat s parametry, jako je ID obsluhující sítě během generování klíčů, což by vedlo k odvození nesprávných nebo kompromitovaných relakčních klíčů. MACT vytváří kryptograficky silnou vazbu mezi těmito parametry a odvozenými klíči. Jeho vznik byl motivován potřebou algoritmové flexibility a vylepšené bezpečnosti ve srovnání s předchozími integritními algoritmy, čímž poskytl základ pro bezpečnou hierarchii klíčů, která chrání uživatelská data a signalizaci v sítích LTE a 5G.

## Klíčové vlastnosti

- Výstup standardizovaného kryptografického algoritmu AES-CMAC.
- Používá se jako základní součást v odvozovacích funkcích klíčů (KDF) pro EPS a 5G.
- Poskytuje integritu dat a autentizaci původu pro bezpečnostní parametry.
- Typicky se jedná o 128-bitovou hodnotu odvozenou z tajného klíče a vstupní zprávy.
- Nezbytný pro generování bezpečnostních klíčů pro přístupovou vrstvu (access-stratum) i pro vrstvu mimo přístupovou (non-access-stratum).
- Umožňuje algoritmovou flexibilitu v rámci bezpečnostního rámce 3GPP.

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [MACT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mact/)
