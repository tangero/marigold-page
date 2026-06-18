---
slug: "uea"
url: "/mobilnisite/slovnik/uea/"
type: "slovnik"
title: "UEA – UMTS Encryption Algorithm"
date: 2026-01-01
abbr: "UEA"
fullName: "UMTS Encryption Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/uea/"
summary: "UEA je rodina proudových šifrovacích algoritmů používaných k šifrování uživatelských dat a signalizačních zpráv na rádiovém rozhraní v sítích UMTS. Primární algoritmus UEA1 (založený na KASUMI) byl na"
---

UEA je rodina proudových šifrovacích algoritmů, včetně primárního algoritmu UEA1 založeného na KASUMI, používaných k šifrování uživatelských dat a signalizace na rádiovém rozhraní UMTS pro silnější důvěrnost než u GSM.

## Popis

UMTS Encryption Algorithm (UEA) označuje sadu standardizovaných kryptografických algoritmů používaných k zajištění ochrany důvěrnosti uživatelských dat a signalizačních zpráv přenášených přes vzdušné rozhraní Uu mezi uživatelským zařízením (UE) a pozemní rádiovou přístupovou sítí UMTS ([UTRAN](/mobilnisite/slovnik/utran/)). Šifrování je klíčovou součástí bezpečnostní architektury 3GPP a zabraňuje odposlechu rádiové komunikace. Algoritmy UEA jsou proudové šifry, které generují šifrovací proud (keystream), jenž se kombinuje s otevřeným textem pomocí operace XOR. Generování šifrovacího proudu je synchronizováno mezi UE a řadičem rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) pomocí vstupů, které zahrnují šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)) odvozený během autentizace a časově proměnný parametr [COUNT-C](/mobilnisite/slovnik/count-c/).

Nejvýznamnějším algoritmem v této rodině je UEA1, známý také jako algoritmus f8. UEA1 je založen na blokové šifře KASUMI, která je sama modifikovanou verzí šifry MISTY1. UEA1 pracuje v konkrétním režimu s výstupní zpětnou vazbou (output-feedback mode) pro generování šifrovacího proudu. Algoritmus přijímá několik vstupů: 128bitový šifrovací klíč (CK), 32bitový COUNT-C (sekvenční čítač), 5bitovou identitu BEARER (pro oddělení datových proudů), 1bitový parametr DIRECTION (uplink/downlink) a parametr LENGTH proměnné délky (pro omezení délky šifrovacího proudu). Tato kombinace zajišťuje, že šifrovací proud je jedinečný pro každý rádiový blok, čímž brání opakovaným útokům (replay attacks). Druhý algoritmus, UEA2, byl představen později a je založen na proudové šifře SNOW 3G, což nabízí alternativu pro zvýšenou bezpečnost a výkon.

Rozhodnutí o tom, který algoritmus UEA se pro spojení použije, je součástí bezpečnostního vyjednávání mezi UE a sítí během nastavování spojení řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) nebo procedury příkazu bezpečnostního režimu. Síť označí vybraný algoritmus ze sady podporované jak UE, tak sítí (jak je uvedeno v bezpečnostních schopnostech UE). Šifrování je aplikováno ve vrstvě řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) pro data v transparentním a nepotvrzovaném režimu a ve vrstvě konvergenčního protokolu paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) pro data v potvrzovaném režimu a pro LTE/5G, kde se PDCP používá. RNC je síťová entita odpovědná za šifrování v downlinku a dešifrování v uplinku.

## K čemu slouží

UEA byl vyvinut k řešení dobře zdokumentovaných kryptografických slabin proudových šifer [A5/1](/mobilnisite/slovnik/a5-1/) a A5/2 používaných v GSM. Šifrování GSM mělo několik nedostatků, včetně krátkých délek klíčů a algoritmických zranitelností, které je činily náchylnými ke kryptoanalýze a praktickým útokům. Návrh UMTS (3G) představoval příležitost vybudovat silnější a robustnější bezpečnostní architekturu od základů. Primárním účelem UEA1 bylo poskytnout úroveň důvěrnosti, která byla v době spuštění UMTS považována za bezpečnou pro předvídatelnou budoucnost, odolávat známým kryptoanalytickým technikám a útokům hrubou silou díky svému 128bitovému klíči.

Vývoj UEA1 zahrnoval otevřenější a standardizovanější proces ve srovnání s utajeným návrhem algoritmů GSM A5. Bloková šifra KASUMI byla vyvinuta skupinou SAGE (Security Algorithms Group of Experts) v rámci ETSI a byla zpřístupněna veřejnosti k prověření, což zvýšilo důvěru v její bezpečnost. Zavedení UEA2 (SNOW 3G) v pozdějších vydáních sloužilo několika účelům: poskytlo agilitu algoritmů, umožňující operátorům přepnout algoritmus, pokud by byla objevena slabina v UEA1; nabídlo potenciální výkonnostní výhody; a sladilo se s potřebou nového základního algoritmu pro nadcházející systém LTE, kde SNOW 3G také tvořila základ šifry 128-EEA1. Tento vývoj demonstruje princip nespoléhání se na jediný kryptografický algoritmus.

## Klíčové vlastnosti

- Proudový šifrovací algoritmus pro šifrování dat na rozhraní Uu v UMTS
- UEA1 je založen na blokové šifře KASUMI v konkrétním režimu s výstupní zpětnou vazbou (f8)
- UEA2 je založen na proudové šifře SNOW 3G
- Používá 128bitový šifrovací klíč (CK) odvozený z procedury autentizace a dohody o klíči (AKA)
- Šifrovací proud je jedinečný pro každý rádiový blok díky vstupům jako COUNT-C, BEARER a DIRECTION
- Výběr algoritmu je vyjednáván prostřednictvím procedur příkazu bezpečnostního režimu RRC

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [UEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/uea/)
