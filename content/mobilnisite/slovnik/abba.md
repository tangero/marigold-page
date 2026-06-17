---
slug: "abba"
url: "/mobilnisite/slovnik/abba/"
type: "slovnik"
title: "ABBA – Anti-Bidding down Between Architectures"
date: 2026-01-01
abbr: "ABBA"
fullName: "Anti-Bidding down Between Architectures"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/abba/"
summary: "ABBA je bezpečnostní mechanismus v 5G, který zabraňuje útokům typu bidding-down mezi různými síťovými architekturami (např. 4G EPC a 5G Core). Zajišťuje, aby bezpečnostní schopnosti uživatele nebyly s"
---

ABBA je bezpečnostní mechanismus 3GPP, který zabraňuje útokům typu bidding-down mezi různými síťovými architekturami, a zajišťuje, aby bezpečnostní schopnosti uživatele nebyly sníženy při přechodu mezi sítěmi, jako jsou 4G a 5G.

## Popis

ABBA (Anti-Bidding down Between Architectures) je klíčový bezpečnostní parametr definovaný ve specifikacích 3GPP, především v rámci bezpečnostního rámce 5G System (5GS). Funguje jako bitový řetězec obsažený v bezpečnostních signalizačních zprávách, konkrétně v rámci kontextu zabezpečení NAS (Non-Access Stratum) a autentizačních procedur. Hlavní technická role ABBA spočívá v poskytnutí kryptografického spojení mezi bezpečnostními schopnostmi UE (User Equipment) a typem architektury obsluhující sítě, čímž zabraňuje útočníkovi vynutit použití bezpečnostních algoritmů nebo procedur z předchozí, potenciálně méně bezpečné generace.

Z architektonického hlediska ABBA funguje v rámci procedur Authentication and Key Agreement (AKA) definovaných pro 5G. Během počáteční registrace nebo procedur předávání spojení zahrnujících mezisystémovou mobilitu (např. mezi 5G Core a 4G Evolved Packet Core) si jak UE, tak síť (konkrétně AMF - Access and Mobility Management Function v 5GC, nebo odpovídající MME v EPC) vymění a ověří parametr ABBA. Tento parametr je konstruován tak, aby byl jedinečný pro síťovou architekturu a vytvářený bezpečnostní kontext. UE odvozuje hodnotu ABBA na základě informací přijatých od sítě v autentizační žádosti a síť nezávisle vypočítává očekávanou hodnotu. Neshoda indikuje potenciální útok typu bidding-down, což vede k neúspěchu procedury.

Klíčové komponenty zapojené do implementace ABBA zahrnují bezpečnostní modul UE (USIM), funkci bezpečnostní kotvy obsluhující sítě (SEAF v 5GC, která komunikuje s AUSF - Authentication Server Function) a autentizační přihlašovací údaje domovské sítě (uložené v UDM/ARPF - Unified Data Management / Authentication Credential Repository and Processing Function). Parametr ABBA sám o sobě není samostatnou zprávou, ale je vložen do jiných bezpečnostních kontejnerů, jako je zpráva Authentication Response odesílaná z UE do sítě. Jeho hodnota je vypočítána pomocí vstupů, které zahrnují jméno obsluhující sítě (SNN), a explicitně indikuje typ jádra sítě (5GC nebo EPC), ke kterému se UE registruje.

V širší 5G bezpečnostní architektuře ABBA doplňuje další bezpečnostní mechanismy, jako je ochrana SUPI (Subscription Permanent Identifier), ochrana integrity signalizace NAS a šifrování dat uživatelské roviny. Jeho specifická role je řešit hrozby spojené s architektonickým přechodem, které nebyly plně zmírněny v předchozích generacích. Tím, že zajišťuje, že bezpečnostní vyjednávání nemohou být zmanipulována k návratu ke starším, slabším protokolům, když se UE pohybuje mezi oblastmi pokrytí 4G a 5G, ABBA udržuje celkovou úroveň bezpečnostní záruky systému 5G, což je základní konstrukční princip. To je obzvláště důležité ve scénářích nasazení non-standalone (NSA), kde 5G NR radiový přístup připojuje k 4G jádru, a v raných fázích migrace, kdy sítě provozují duální architektury.

## K čemu slouží

ABBA byla vytvořena k řešení konkrétní bezpečnostní zranitelnosti známé jako útok typu "bidding-down" nebo "downgrade" v kontextu mezigenerační síťové mobility. V 4G (EPS), zatímco bezpečnostní mechanismy existovaly v rámci jedné architektury, přechod mezi sítěmi 3G a 4G měl potenciální zranitelnosti, kde by útočník mohl manipulovat signalizací, aby přesvědčil UE a síť, že druhá strana podporuje pouze starší, méně bezpečné kryptografické algoritmy (např. vynucení návratu z AES na SNOW 3G). Se zavedením 5G a očekáváním dlouhodobé koexistence se sítěmi 4G EPC (zejména v nasazeních Non-Standalone) identifikovalo 3GPP, že je možná nová forma tohoto útoku: útočník by se mohl pokusit přinutit UE registrující se k síti 5G Core, aby místo toho použila bezpečnostní procedury definované pro 4G Evolved Packet Core, které mohou mít odlišné nebo slabší bezpečnostní vlastnosti.

Historický kontext je zakořeněn ve vývoji mobilní bezpečnosti. Každá generace (3G, 4G, 5G) zaváděla silnější autentizační algoritmy, funkce odvozování klíčů a mechanismy ochrany integrity. Avšak kvůli zpětné kompatibilitě musí UE a sítě podporovat více sad zabezpečení. Aktivní útočník v rádiové cestě mohl zachytit a upravit zprávy výměny bezpečnostních schopností, aby odstranil odkazy na novější, silnější algoritmy, a oklamat tak obě strany, aby souhlasily se starší sadou. ABBA konkrétně řeší tento problém mezi architekturami (5GC vs. EPC), nejen mezi sadami algoritmů v rámci jedné architektury. Zajišťuje, že bezpečnostní kontext je explicitně vázán na typ používaného jádra sítě.

Omezení předchozích přístupů, zejména v 4G, spočívalo v tom, že zatímco vyjednávání algoritmů bylo chráněno v rámci procedury EPS AKA, architektonický kontext (zda se UE připojovalo k EPC nebo předchozímu jádru) nebyl kryptograficky ověřen způsobem, který by zabránil aktivnímu útočníkovi manipulovat s tímto přiřazením. ABBA tuto mezeru zaplňuje tím, že činí architekturu sítě povinným a ověřeným parametrem v procesu autentizace a dohody o klíči. To bylo motivováno konstrukčním principem 5G poskytnout silnější zabezpečení než předchozí generace, zejména pro nové vektory hrozeb zavedené síťovým slicingem, servisně orientovanou architekturou a zvýšenou závislostí na nedůvěryhodných přístupových sítích.

## Klíčové vlastnosti

- Zabraňuje útokům na snížení bezpečnostních schopností mezi architekturami 4G EPC a 5G Core
- Kryptograficky váže autentizaci k typu obsluhující sítě (5GC nebo EPC)
- Vložen jako parametr do 5G signalizace zabezpečení NAS a autentizačních zpráv
- Ověřován jak UE, tak sítí během procedur AKA
- Nezbytný pro bezpečnou mezisystémovou mobilitu v nasazeních 5G non-standalone a standalone
- Funguje transparentně pro uživatele a zároveň poskytuje kritickou ochranu proti útokům typu man-in-the-middle

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps

---

📖 **Anglický originál a plná specifikace:** [ABBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/abba/)
