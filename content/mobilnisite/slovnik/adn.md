---
slug: "adn"
url: "/mobilnisite/slovnik/adn/"
type: "slovnik"
title: "ADN – Abbreviated Dialling Numbers"
date: 2025-01-01
abbr: "ADN"
fullName: "Abbreviated Dialling Numbers"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/adn/"
summary: "ADN je funkce telekomunikační služby, která uživatelům umožňuje ukládat často vytočená telefonní čísla s kratšími, zapamatovatelnými kódy. Zjednodušuje vytáčení nahrazením dlouhých čísel krátkými číse"
---

ADN je funkce telekomunikační služby, která uživatelům umožňuje ukládat často vytočená telefonní čísla a přiřazovat je kratším, zapamatovatelným číselným kódům pro zjednodušené vytáčení v mobilních sítích.

## Popis

Abbreviated Dialling Numbers (zkrácená čísla, ADN) je základní funkce telefonní služby standardizovaná 3GPP, která mobilním účastníkům umožňuje přiřazovat často používaná telefonní čísla krátkým číselným kódům. Systém funguje prostřednictvím strukturovaného úložného mechanismu v modulu Universal Subscriber Identity Module (USIM) nebo SIM kartě, kde každá položka ADN sestává z krátkého kódu (obvykle 1–2 číslice) namapovaného na úplné telefonní číslo. Když uživatel vytočí zkrácený kód, telefonní aplikace mobilního zařízení zachytí krátkou sekvenci, provede vyhledání v databázi ADN uložené na USIM, získá odpovídající plné telefonní číslo a zahájí proceduru sestavení hovoru pomocí kompletního čísla.

Z architektonického hlediska je funkce ADN implementována napříč více síťovými elementy, přičemž USIM slouží jako primární úložiště. Struktura databáze ADN je definována specifikacemi 3GPP s konkrétní organizací souborů (EF_ADN) obsahující záznamy, které zahrnují zkrácený kód, plné telefonní číslo a přidružené parametry, jako jsou jmenné štítky pro identifikaci volajícího. Mobile Equipment (ME) komunikuje s USIM prostřednictvím standardizovaných příkazů definovaných v TS 31.111 za účelem čtení, zápisu a správy položek ADN. Toto oddělení mezi ukládáním (USIM) a zpracováním (ME) umožňuje přenositelnost funkce ADN mezi různými mobilními zařízeními při zachování uživatelského komfortu.

Z pohledu sítě probíhá zpracování ADN zcela uvnitř User Equipment (UE) před sestavením hovoru. Když uživatel zahájí hovor pomocí zkráceného kódu, UE provede lokální překlad bez zapojení síťových elementů, což činí z ADN funkci na straně klienta, která nevyžaduje podporu nebo úpravy sítě. Sestavení hovoru následně probíhá normálně, jakmile je plné číslo přeloženo, přičemž MSC (Mobile Switching Center) přijímá kompletní vytočené číslice, jako kdyby je uživatel zadal ručně. Tato architektura zajišťuje zpětnou kompatibilitu s existující síťovou infrastrukturou a zároveň poskytuje vyšší uživatelský komfort.

Technická implementace zahrnuje ošetření chyb pro neplatné kódy, správu kapacity pro omezené úložiště USIM a synchronizační mechanismy při změně položek ADN. Specifikace 3GPP definují maximální kapacity pro úložiště ADN (obvykle 50–100 položek v závislosti na implementaci USIM), kódování znaků pro přidružená jména (obvykle UCS2 pro mezinárodní podporu) a bezpečnostní mechanismy pro zabránění neautorizovaným změnám. Služba je integrována s dalšími funkcemi založenými na SIM, jako jsou Fixed Dialing Numbers (FDN) a Last Number Dialed (LND), čímž vytváří komplexní ekosystém správy telefonie na USIM.

## K čemu slouží

ADN bylo vytvořeno za účelem řešení základního problému použitelnosti – zapamatování si a přesného vytočení dlouhých telefonních čísel v raných systémech mobilní telefonie. Před rozšířením seznamů kontaktů a rozhraní chytrých telefonů museli uživatelé ručně zadávat kompletní čísla (včetně kódů zemí, směrových čísel a čísel účastníků) pro každý hovor. Tento proces byl náchylný k chybám, časově náročný a zvláště obtížný pro často kontaktovaná čísla. ADN poskytlo jednoduché, standardizované řešení, které fungovalo napříč různými síťovými operátory a výrobci zařízení.

Technologie řešila konkrétní omezení předchozích přístupů, jako jsou papírové telefonní seznamy nebo paměť zařízení, která nebyla přenositelná mezi telefony. Ukládáním zkrácených čísel na SIM kartu namísto do paměti zařízení ADN zajišťovalo, že uživatelský komfort přetrvá při změně mobilních přístrojů – což byl v raných mobilních trzích běžný jev, kdy se zařízení často měnila nebo půjčovala. Tento přístup zaměřený na SIM byl v souladu s vizí 3GPP o přenositelnosti identifikace účastníka a konzistentním uživatelském zážitku napříč různými přístupovými technologiemi.

Historicky ADN představovalo důležitý krok v designu rozhraní mezi člověkem a strojem v telekomunikacích, překlenující propast mezi technickými číslovacími schématy a kognitivními vzorci uživatelů. Řešilo psychologický aspekt zapamatování si čísel tím, že uživatelům umožňovalo vytvářet osobní, smysluplné asociace (jako '1' pro domov nebo '2' pro kancelář), při zachování technické shody s mezinárodními číslovacími plány. Pokračující relevance této funkce napříč více vydáními 3GPP ukazuje její základní roli v základních telefonních službách, a to i přes vývoj pokročilejších systémů správy kontaktů.

## Klíčové vlastnosti

- Úložiště na bázi SIM/USIM pro přenositelnost mezi zařízeními
- Mapování krátkého kódu na plné číslo (obvykle kódy o 1–2 číslicích)
- Integrováno se souborovým systémem USIM (struktura EF_ADN)
- Lokální zpracování v UE bez zapojení sítě
- Zpětná kompatibilita s existujícími postupy sestavení hovoru
- Standardizovaná kapacita a kódování znaků dle specifikací 3GPP

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [ADN na 3GPP Explorer](https://3gpp-explorer.com/glossary/adn/)
