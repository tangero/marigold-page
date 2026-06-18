---
slug: "rmc"
url: "/mobilnisite/slovnik/rmc/"
type: "slovnik"
title: "RMC – Reference Measurement Channel"
date: 2025-01-01
abbr: "RMC"
fullName: "Reference Measurement Channel"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/rmc/"
summary: "Přesně definovaná, standardizovaná sada parametrů a konfigurací rádiového signálu používaná pro testování a ověřování shody výkonu přijímače uživatelského zařízení (UE). Poskytuje konzistentní etalon"
---

RMC je standardizovaná sada parametrů rádiového signálu používaná jako konzistentní etalon pro testování a ověřování výkonu přijímače uživatelského zařízení vůči požadavkům, jako je citlivost a propustnost.

## Popis

Reference Measurement Channel (RMC) je normativní, pevná konfigurace kanálu Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) používaná výhradně pro testovací účely v 3GPP specifikacích pro shodu a výkon. Nejde o kanál používaný v provozní síti, nýbrž o nástroj pro vytváření reprodukovatelných testovacích podmínek. Definice RMC zahrnuje kompletní sadu parametrů, jako je modulační schéma (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM), kódovou rychlost, velikost transportního bloku, alokaci zdrojů (počet zdrojových bloků a jejich pozice v kmitočtovém pásmu), konfiguraci referenčních signálů a přesný datový vzor, který má být vysílán. Tím vzniká plně předvídatelný rádiový signál.

V testovacím uspořádání emulátor základnové stanice (testovací zařízení) generuje rádiový signál přesně podle specifikace daného RMC. Testované zařízení ([DUT](/mobilnisite/slovnik/dut/)), typicky UE, je následně prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) instruováno k dekódování tohoto kanálu. Tester pak měří výkon UE vůči této známé referenci, nejčastěji vyhodnocením přesnosti propustnosti (procentuálního podílu správně přijatých transportních bloků) nebo míry chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)) za různých podmínek. Mezi tyto podmínky patří různé úrovně výkonu signálu (pro test citlivosti přijímače), přidané řízené rušení (pro test výběrovosti sousedního kanálu nebo výběrovosti v kanálu) a profily útlumového kanálu (pro test výkonu v podmínkách vícecestného šíření).

Úlohou RMC je odstranit variabilitu. Standardizací testovacího signálu až na poslední bit zajišťuje, že výsledky výkonu jsou srovnatelné mezi různými testovacími laboratořemi, různými modely UE a v čase. To je zásadní pro typové schválení (testování shody), kdy regulační orgán nebo certifikační fórum (jako Global Certification Forum) ověřuje, že UE splňuje minimální výkonnostní standardy stanovené 3GPP. RMC jsou definovány pro všechny hlavní 3GPP rádiové technologie (HSPA, LTE, NR) a pro různá kmitočtová pásma a šířky pásma. Tvoří páteř testovacích případů pro charakteristiky přijímače, výkon demodulace a v konečném důsledku zajišťují základní úroveň kvality a interoperability zařízení uváděných na trh.

## K čemu slouží

RMC bylo vytvořeno k řešení kritického problému objektivního a konzistentního měření výkonu rádiového přijímače UE. V počátcích mobilní technologie bylo testování výkonu méně standardizované, což ztěžovalo porovnávání zařízení od různých výrobců a zaručení minimální kvality služby pro koncové uživatele. Průmysl potřeboval 'společný jazyk' pro testování – referenční signál, který byl jednoznačný a plně specifikovaný ve standardu samotném, tak aby jakýkoli kompatibilní testovací systém generoval naprosto stejný podnět.

Jeho primárním účelem je testování shody, což je povinný proces předtím, než může být UE certifikováno pro komerční použití. Regulační orgány a síťoví operátoři vyžadují důkaz, že zařízení bude na jejich sítích adekvátně fungovat. RMC poskytuje prostředky k provádění opakovatelných testů typu vyhovuje/nevyhovuje pro klíčové metriky přijímače, jako je referenční úroveň výkonu citlivosti (nejslabší signál, který UE spolehlivě dekóduje), maximální vstupní úroveň a výkon při přítomnosti rušivých signálů. Bez takové reference by byla certifikace subjektivní a nespolehlivá.

RMC navíc umožňují spravedlivé srovnávací testování výkonu a validační vývoj. Výrobci čipových sad a zařízení UE používají RMC během svých interních fází výzkumu a vývoje k ověření svých návrhů vůči výkonnostním požadavkům standardu 3GPP. Umožňuje také výrobcům síťového vybavení a operátorům provádět vlastní přijímací testy UE. Poskytnutím stabilního, neměnného testovacího cíle napříč generacemi produktů RMC zajišťuje, že zlepšení výkonu jsou měřena vůči konzistentní základní linii, což pohání skutečný technologický pokrok v návrhu přijímačů a algoritmech zpracování signálu.

## Klíčové vlastnosti

- Plně standardizovaná konfigurace signálu (modulace, kódování, mapování zdrojů, datový vzor)
- Používá se výhradně pro testování shody a výkonu, nikoli pro provozní síťový provoz
- Umožňuje reprodukovatelné měření citlivosti přijímače UE, propustnosti a BLER
- Definováno pro různé šířky kanálu, kmitočtová pásma a technologické verze (HSPA, LTE, NR)
- Tvoří základ testovacích případů v 3GPP specifikacích pro shodu TS 36.521 (LTE) a TS 38.521 (NR)
- Zajišťuje interoperabilitu a základní úroveň výkonnostní kvality všech certifikovaných UE

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [BLER – Block Error Rate](/mobilnisite/slovnik/bler/)

## Definující specifikace

- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [RMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rmc/)
