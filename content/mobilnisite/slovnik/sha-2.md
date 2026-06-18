---
slug: "sha-2"
url: "/mobilnisite/slovnik/sha-2/"
type: "slovnik"
title: "SHA-2 – Secure Hash Algorithm 2"
date: 2025-01-01
abbr: "SHA-2"
fullName: "Secure Hash Algorithm 2"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sha-2/"
summary: "SHA-2 je rodina kryptografických hašovacích funkcí standardizovaná institutem NIST a přijatá organizací 3GPP. Poskytuje integritu dat a autentizaci a tvoří základ pro digitální podpisy a odvozování kl"
---

SHA-2 je rodina kryptografických hašovacích funkcí standardizovaných institutem NIST a přijatá organizací 3GPP pro zajištění integrity dat a autentizace. Tvoří základ pro digitální podpisy a odvozování klíčů v bezpečnostních protokolech sítí.

## Popis

SHA-2 je soubor kryptografických hašovacích funkcí, včetně SHA-224, SHA-256, SHA-384 a SHA-512, definovaných Národním institutem pro standardy a technologie ([NIST](/mobilnisite/slovnik/nist/)) ve standardu [FIPS](/mobilnisite/slovnik/fips/) PUB 180-4. V rámci architektury 3GPP není SHA-2 samostatným protokolem, ale základním kryptografickým primitivem integrovaným do různých bezpečnostních mechanismů. Funguje tak, že vezme vstupní zprávu libovolné délky a zpracuje ji pomocí kompresní funkce založené na konstrukci Merkle-Damgård (u většiny variant) nebo na dedikované struktuře pro SHA-512/224 a SHA-512/256, čímž vytvoří hash (otisk) pevné délky. Tento deterministický proces zajišťuje, že jakákoliv změna vstupních dat vede ke zcela odlišnému hashi, což umožňuje ověření integrity.

Vnitřní struktura algoritmu zahrnuje doplnění zprávy (padding), rozdělení na bloky a iterativní zpracování prostřednictvím série logických funkcí (Ch, Maj, Σ, σ) a konstantních slov. Například SHA-256 zpracovává 512bitové bloky zprávy pomocí 256bitové mezihodnoty hashe, která se aktualizuje přes 64 kol. V systémech 3GPP je SHA-256 obzvláště významný. Používá se v procedurách Autentizace a Dohody o Klíči ([AKA](/mobilnisite/slovnik/aka/)) pro generování kryptografických klíčů, v algoritmech ochrany integrity (jako 128-EIA3) pro signalizační zprávy a v bezpečnosti síťových funkcí založené na certifikátech. Jednosměrná vlastnost hašovací funkce a odolnost proti kolizím jsou nezbytné pro prokázání autenticity dat bez odhalení původní informace.

Integrace do specifikací 3GPP, jako je TS 35.934, zahrnuje definici konkrétních variant hash a jejich aplikačních kontextů v rámci bezpečnostní architektury Universal Mobile Telecommunications System (UMTS) a Long-Term Evolution (LTE). Pro 5G je SHA-256 povinnou součástí 5G AKA a primární volbou pro ochranu integrity ve vrstvě [PDCP](/mobilnisite/slovnik/pdcp/). Výpočetní efektivita a prověřená bezpečnost algoritmu jej činí vhodným pro prostředí s omezeným výpočetním výkonem v uživatelských zařízeních a síťových uzlech, což zajišťuje robustní ochranu proti padělání a manipulaci napříč všemi rozhraními rádiového přístupu a jádra sítě.

## K čemu slouží

SHA-2 byl do standardů 3GPP zaveden jako náhrada starších hašovacích funkcí MD5 a SHA-1, které se stávaly zranitelnými vůči praktickým kolizním útokům. Hlavní motivací bylo posílit kryptografické základy bezpečnosti mobilních sítí s rostoucím výpočetním výkonem a pokrokem kryptografických útoků. SHA-1, dříve používaná v některých raných bezpečnostních kontextech 3GPP, vykazovala teoretické slabiny, které mohly ohrozit integritu autentizačních a klíčových protokolů.

Přijetím rodiny SHA-2 standardizované NISTem zajistila 3GPP soulad s globálními osvědčenými postupy v kryptografii a poskytla dlouhodobé robustní řešení pro integritu dat a autentizaci zdroje. To bylo obzvláště důležité pro vývoj směrem k LTE a 5G, kde nové služby a síťové architektury vyžadovaly vyšší bezpečnostní záruky. SHA-2 řeší omezení svých předchůdců tím, že nabízí větší velikosti hashe (např. 256bitový) a bezpečnější vnitřní strukturu, čímž účinně zmírňuje známé vektory útoků, jako je rozšíření délky a hledání kolizí. Jeho implementace podporuje rostoucí potřebu zabezpečeného síťového slicingu, autentizace zařízení IoT a ochrany dat uživatelské roviny v stále více propojeném ekosystému.

## Klíčové vlastnosti

- Rodina hašovacích funkcí (SHA-224, SHA-256, SHA-384, SHA-512)
- Založeno na konstrukci Merkle-Damgård s kompresí Davies-Meyer
- Produkuje otisky (digesty) pevné délky (např. 256 bitů pro SHA-256)
- Poskytuje odolnost proti kolizím a odolnost proti nalezení vzoru (pre-image resistance)
- Používá se pro ochranu integrity (např. v 128-EIA3) a odvozování klíčů
- Standardizováno NIST ve FIPS 180-4 a přijato v 3GPP TS 35.934

## Definující specifikace

- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [SHA-2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sha-2/)
