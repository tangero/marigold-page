---
slug: "tdma-efr"
url: "/mobilnisite/slovnik/tdma-efr/"
type: "slovnik"
title: "TDMA-EFR – TDMA Enhanced Full Rate Speech Codec"
date: 2025-01-01
abbr: "TDMA-EFR"
fullName: "TDMA Enhanced Full Rate Speech Codec"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/tdma-efr/"
summary: "Standardizovaný hlasový kodek, definovaný jako TIA IS-641, poskytující kvalitu hlasu Enhanced Full Rate (EFR) pro digitální mobilní systémy založené na TDMA. Ve srovnání se staršími plnorychlostními k"
---

TDMA-EFR je standardizovaný hlasový kodek Enhanced Full Rate (TIA IS-641), který poskytuje vynikající kvalitu hlasu pro TDMA mobilní systémy díky použití pokročilých kódovacích technik.

## Popis

TDMA-EFR je algoritmus pro kódování řeči standardizovaný jako [TIA](/mobilnisite/slovnik/tia/) IS-641 a přijatý 3GPP pro interoperabilitu a jako referenční. Jedná se o kodek Enhanced Full Rate navržený pro digitální mobilní systémy s přístupem s časovým dělením (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) – [TDMA](/mobilnisite/slovnik/tdma/)), jako jsou systémy založené na standardu IS-136. Kodek pracuje s čistou přenosovou rychlostí 7,4 kbit/s, ale s kanálovým kódováním pro ochranu proti chybám je celková rychlost přenášená přes rozhraní vzduchu vyšší. Je založen na paradigmatu kódování Algebraic Code Excited Linear Prediction ([ACELP](/mobilnisite/slovnik/acelp/)), podobně jako kodeky GSM [EFR](/mobilnisite/slovnik/efr/) a [AMR](/mobilnisite/slovnik/amr/).

Kodek pracuje tak, že analyzuje 20ms rámce hlasového signálu (vzorkovaného na 8 kHz). Pro každý rámec extrahuje parametry reprezentující filtr hlasového traktu (koeficienty lineární prediktivní kódování) a excitační signál (pevný kodek a adaptivní kodek pro výšku tónu). Tyto parametry jsou kvantovány, zakódovány a přeneseny. Na přijímací straně jsou parametry dekódovány a použity k syntéze hlasového signálu prostřednictvím ACELP syntetizačního filtru. Klíčem k jeho vylepšené kvalitě je efektivnější a robustnější kvantování těchto parametrů ve srovnání se staršími plnorychlostními kodeky, což vede ke kvalitě řeči blízké kvalitě pevné sítě (toll quality) i za mírných chybových podmínek na kanálu.

Jeho úlohou v síti je složka hlasové služby v rámci uživatelské roviny (User Plane). Je implementován v řečových procesorových jednotkách jak mobilních stanic, tak síťových transkodérů. Kodek definuje přesný formát bitového toku pro komprimované hlasové rámce, které jsou následně přenášeny přes provozní kanály TDMA rozhraní vzduchu. Specifikace jako 3GPP TS 26.093 definují bitově přesnou implementaci kodeku, testovací sekvence a požadavky na kompatibilitu, čímž zajišťují konzistentní kvalitu hlasu napříč zařízeními různých výrobců.

## K čemu slouží

TDMA-EFR byl vytvořen, aby řešil potřebu výrazně lepší kvality hlasu v digitálních [TDMA](/mobilnisite/slovnik/tdma/) sítích (IS-136), které původně používaly starší, méně kvalitní hlasové kodeky. Hlavním problémem bylo, že zatímco digitální TDMA poskytovalo lepší spektrální účinnost a zabezpečení než analogové systémy, kvalita hlasu u starších plnorychlostních kodeků byla často vnímána jako horší než u analogového systému AMPS nebo pevné sítě. To byla konkurenční nevýhoda.

Motivací bylo vyvinout kodek, který by mohl poskytovat řeč 'jako v pevné síti' nebo 'toll quality' v rámci omezeného rozpočtu přenosové rychlosti digitálního mobilního kanálu. Technologie [ACELP](/mobilnisite/slovnik/acelp/), která se osvědčovala v jiných standardech (jako GSM EFR), byla přizpůsobena pro severoamerický TDMA trh. TDMA-EFR vyřešil problém kvality použitím pokročilejších vyhledávacích procedur typu analysis-by-synthesis a sofistikovaných kvantovacích metod, díky čemuž je komprimovaná řeč přirozenější a odolnější vůči bitovým chybám. Jeho vznik byl hnán snahou zvýšit spokojenost zákazníků a efektivně konkurovat jiným vyvíjejícím se digitálním technologiím, jako je CDMA, které také nabízely služby vysoké kvality hlasu.

## Klíčové vlastnosti

- Založen na algoritmu pro kódování řeči ACELP (Algebraic Code Excited Linear Prediction)
- Pracuje s 20ms hlasovými rámci při čisté přenosové rychlosti 7,4 kbit/s
- Poskytuje vylepšenou kvalitu hlasu blížící se kvalitě pevné sítě (toll quality)
- Obsahuje robustní kanálové kódování pro ochranu proti chybám na rádiových spojích
- Definován standardem TIA IS-641 a přijat pro interoperabilitu 3GPP
- Poskytuje standardizovanou testovací sekvenci pro ověření implementací

## Související pojmy

- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [GSM-EFR – GSM Enhanced Full Rate Speech Codec](/mobilnisite/slovnik/gsm-efr/)

## Definující specifikace

- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS

---

📖 **Anglický originál a plná specifikace:** [TDMA-EFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdma-efr/)
