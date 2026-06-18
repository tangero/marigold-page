---
slug: "sha"
url: "/mobilnisite/slovnik/sha/"
type: "slovnik"
title: "SHA – Secure Hash Algorithm"
date: 2025-01-01
abbr: "SHA"
fullName: "Secure Hash Algorithm"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sha/"
summary: "Secure Hash Algorithm (SHA) je rodina kryptografických hashovacích funkcí standardizovaných institutem NIST a široce používaných v 3GPP pro zabezpečení. Generuje z vstupních dat pevně daný, jedinečný"
---

SHA je rodina standardizovaných kryptografických hashovacích funkcí, které ze vstupních dat generují jedinečný digitální otisk (hash). V rámci 3GPP se používají pro zajištění integrity dat, digitální podpisy a odvozování klíčů v bezpečnostních mechanismech.

## Popis

Secure Hash Algorithm (SHA) je klíčový kryptografický primitiv, který je hojně využíván v bezpečnostních architekturách 3GPP. Hashovací funkce přijímá vstupní zprávu libovolné délky a zpracuje ji za účelem vytvoření výstupu pevné délky, nazývaného hash nebo otisk zprávy. Základními vlastnostmi kryptografické hashovací funkce, jako je SHA, jsou: odolnost proti kolizím (je výpočetně neproveditelné najít dva různé vstupy, které vytvoří stejný hash), odolnost proti nalezení vzoru (vzhledem k hashi je neproveditelné najít původní vstup) a odolnost proti nalezení druhého vzoru (vzhledem ke vstupu a jeho hashi je neproveditelné najít jiný vstup se stejným hashem).

V systémech 3GPP jsou pro různé bezpečnostní funkce vyžadovány konkrétní varianty SHA. Široce rozšířená je zejména SHA-256, která je součástí rodiny [SHA-2](/mobilnisite/slovnik/sha-2/). Produkuje 256bitový (32bytový) otisk. Její činnost zahrnuje rozdělení vstupu na bloky, použití kompresní funkce a iterativní zpracování každého bloku pomocí série logických operací ([AND](/mobilnisite/slovnik/and/), [OR](/mobilnisite/slovnik/or/), XOR, rotace) a konstant. Vnitřní stav se aktualizuje s každým blokem a výsledkem je finální hash hodnota. SHA-256 se používá v protokolu 5G Authentication and Key Agreement (5G-AKA) pro generování kryptografických klíčů a v algoritmech integrity (jako 128-NIA2) pro signalizační zprávy.

SHA je také základní součástí konstrukce HMAC (Hash-based Message Authentication Code), která se používá pro autentizaci a ověřování integrity zpráv. Dále se funkce založené na SHA používají v funkcích pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)), jako jsou ty definované v 3GPP TS 33.220, k vygenerování více tajných klíčů z jediného sdíleného tajemství vytvořeného během autentizace. Například v 5G používá KDF SHA-256 k odvození konkrétních klíčů používaných pro šifrování a ochranu integrity uživatelských dat a signalizace řídicí roviny mezi UE a sítí. Síla algoritmu zajišťuje, že i nepatrná změna ve vstupních datech vede k zcela odlišnému, nepředvídatelnému hashi, což jej činí ideálním pro ověřování integrity dat a autentizaci síťových entit.

## K čemu slouží

SHA byla začleněna do standardů 3GPP, aby poskytla robustní, standardizovaný základ pro integritu dat, autentizaci a odvozování klíčů. Starší generace mobilních sítí používaly slabší kryptografické algoritmy. S rostoucím výpočetním výkonem se tyto algoritmy staly zranitelnými vůči útokům. Zavedení SHA, zejména SHA-256, bylo motivováno potřebou silnějších, do budoucna odolných bezpečnostních mechanismů schopných ochránit před kolizními útoky a útoky na vzor, které by mohly ohrozit síťovou autentizaci nebo umožnit padělání zpráv.

Jejím hlavním účelem je zajistit důvěryhodnost komunikace v sítích 3GPP. Pro ochranu integrity umožňuje příjemci ověřit, že zpráva nebyla během přenosu změněna. U digitálních podpisů (používaných při validaci certifikátů pro síťové uzly) SHA vytváří z dat otisk, který je následně podepsán, čímž poskytuje autentizaci a nepopiratelnost. Jako klíčová součást odvozování klíčů umožňuje bezpečné generování více sezení klíčů z hlavního klíče, čímž zajišťuje oddělení klíčů a omezuje dopad případného kompromitování klíče. Použití široce prověřeného, mezinárodně uznávaného standardu, jako je SHA, také podporuje interoperabilitu, bezpečnostní záruky a soulad s předpisy v celosvětových telekomunikačních nasazeních.

## Klíčové vlastnosti

- Deterministická: Stejný vstup vždy vytvoří stejný hash
- Pevně daná velikost výstupu (např. 256 bitů pro SHA-256)
- Výpočetně efektivní na výpočet
- Vysoce citlivá na změny ve vstupu (lavinový efekt)
- Odolná proti kolizím a proti nalezení vzoru
- Základ pro HMAC, KDF a digitální podpisy

## Související pojmy

- [KDF – Key Derivation Function](/mobilnisite/slovnik/kdf/)
- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)

## Definující specifikace

- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [SHA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sha/)
