---
slug: "kdf"
url: "/mobilnisite/slovnik/kdf/"
type: "slovnik"
title: "KDF – Key Derivation Function"
date: 2026-01-01
abbr: "KDF"
fullName: "Key Derivation Function"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/kdf/"
summary: "Kryptografická funkce, která generuje jeden nebo více tajných klíčů z hlavního klíče a dalších vstupních parametrů. Je základním prvkem bezpečnostní architektury 3GPP a umožňuje bezpečnou derivaci klí"
---

KDF je kryptografická funkce, která generuje jeden nebo více tajných klíčů z hlavního klíče a dalších parametrů pro šifrování, integritu a autentizaci v sítích 3GPP.

## Popis

Funkce pro derivaci klíče (KDF) je klíčovým prvkem bezpečnostního rámce 3GPP, specifikovaným v řadě dokumentů 3GPP TS 33. Jedná se o deterministický algoritmus, který přijímá hlavní tajný klíč (např. [CK](/mobilnisite/slovnik/ck/)/[IK](/mobilnisite/slovnik/ik/) z [AKA](/mobilnisite/slovnik/aka/) nebo K_[ASME](/mobilnisite/slovnik/asme/) z EPS-AKA) spolu s dalšími specifickými vstupními parametry a vytváří jeden nebo více kryptograficky silných, odvozených klíčů. Tyto odvozené klíče slouží pro různé bezpečnostní účely, jako je šifrování (ciphering) a ochrana integrity uživatelských dat a řídicí signalizace na různých rozhraních (např. Uu, N1, [N2](/mobilnisite/slovnik/n2/)). KDF zajišťuje separaci klíčů, což znamená, že klíče používané pro různé účely, v různých síťových doménách nebo pro různé uživatele jsou kryptograficky odlišné, i když jsou odvozeny ze stejného kořenového tajemství.

Z architektonického hlediska je KDF implementována v bezpečnostních entitách jak ve vybavení uživatele (UE), tak v síti, například v USIM, v bezpečnostním modulu UE, v autentizační serverové funkci ([AUSF](/mobilnisite/slovnik/ausf/)) a ve funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). Její provoz je úzce integrován s postupy autentizace a dohody o klíči, jako jsou 5G-AKA a EAP-AKA'. Samotná funkce je typicky založena na hashovacím kódu pro autentizaci zpráv (HMAC), často s využitím SHA-256, což poskytuje osvědčenou a standardizovanou metodu pro derivaci klíčů.

Jak funguje, zahrnuje přesnou konstrukci vstupního řetězce. Standardní vstup zahrnuje hlavní klíč, hodnotu [FC](/mobilnisite/slovnik/fc/) (Function Code) identifikující účel odvozeného klíče (např. pro NAS šifrování, RRC integritu) a sadu parametrů (P0, P1, ... L0, L1, ...). Tyto parametry poskytují kontext, jako je název obslužné sítě, rozlišovač typu algoritmu a pořadová čísla. KDF tyto vstupy zpracuje a vygeneruje bitový řetězec požadované délky, který je následně rozdělen na konkrétní odvozené klíče (např. K_{NASenc}, K_{RRCint}, K_{UPenc}). Tento proces zaručuje, že pro každý specifický kryptografický kontext je vygenerován jedinečný klíč, čímž se zabrání tomu, aby kompromitace jednoho klíče ovlivnila ostatní.

## K čemu slouží

KDF existuje k řešení kritického problému správy a životního cyklu klíčů v rámci složité, vícevrstvé mobilní sítě. Spoléhání se na jediný statický klíč pro všechny bezpečnostní funkce představuje závažnou slabinu; pokud je tento klíč kompromitován, celá bezpečnost relace účastníka je ohrožena. KDF umožňuje vytvoření hierarchie klíčů z jediného kořenového klíče, který je stanoven během autentizace. Tento kořenový klíč nikdy neopouští zabezpečené úložiště, zatímco odvozené, relaci specifické klíče jsou používány pro skutečnou ochranu provozu.

Historicky, jak se sítě vyvíjely od 2G přes 3G a dále, se stala zjevnou potřeba silnější a podrobnější bezpečnosti. Rané systémy měly jednodušší použití klíčů. Zavedení KDF v 3GPP Release 8 s EPS (LTE) bylo formalizací a posílením tohoto konceptu, které poskytlo standardizovaný, na algoritmech agilní rámec. Vyřešilo to omezení předchozích ad-hoc přístupů tím, že zajistilo kryptografickou separaci klíčů používaných pro řídicí rovinu a uživatelskou rovinu, pro integritu a důvěrnost a pro různé síťové přístupové technologie (např. 3G vs LTE). Tato separace omezuje dopad případného prozrazení klíče a je základním principem zabezpečení navrženého do systému.

Kromě toho KDF poskytuje flexibilitu potřebnou pro vývoj sítě. Jak jsou zaváděny nové služby (jako síťové segmentování), nová rozhraní a nové kryptografické algoritmy, lze rámec KDF rozšířit definováním nových funkčních kódů (Function Codes) a vstupních parametrů bez změny základního autentizačního mechanismu. Tím se zajišťuje dlouhodobá životnost bezpečnostní architektury a umožňuje čistá integrace nových odvozených klíčů pro nové bezpečnostní kontexty, jako jsou ty vyžadované pro přístup Non-3GPP nebo rozhraní architektury založené na službách.

## Klíčové vlastnosti

- Standardizovaný algoritmus založený na HMAC-SHA-256 pro kryptografickou robustnost
- Vynucuje princip separace klíčů pro různé kryptografické kontexty (např. NAS vs RRC, integrita vs šifrování)
- Používá strukturovaný vstupní řetězec s funkčním kódem (Function Code) a parametry k jednoznačné definici účelu klíče
- Generuje více relaci specifických klíčů z jediného dlouhodobého hlavního klíče
- Integrální součást autentizačních postupů 5G-AKA, EPS-AKA a EAP-AKA'
- Poskytuje agilitu algoritmu, umožňující budoucí aktualizace podkladové kryptografické hashovací funkce

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 33.110** (Rel-19) — UICC-Terminal Key Establishment
- **TS 33.122** (Rel-19) — Security Architecture for CAPIF
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.224** (Rel-19) — Generic Push Layer (GPL) Specification
- **TS 33.259** (Rel-19) — Key Establishment between UICC Hosting & Remote Device
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps
- **TR 33.739** (Rel-18) — Study on security enhancement of support for
- **TR 33.834** (Rel-16) — Long Term Key Update Procedures Study
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TS 33.863** (Rel-14) — Security for Battery-Efficient IoT Device to Enterprise
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [KDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/kdf/)
