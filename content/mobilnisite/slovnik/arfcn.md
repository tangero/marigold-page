---
slug: "arfcn"
url: "/mobilnisite/slovnik/arfcn/"
type: "slovnik"
title: "ARFCN – Absolute Radio Frequency Channel Number"
date: 2025-01-01
abbr: "ARFCN"
fullName: "Absolute Radio Frequency Channel Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/arfcn/"
summary: "ARFCN je jedinečný číselný identifikátor přiřazený každému rádiovému frekvenčnímu kanálu v mobilních sítích. Poskytuje standardizovanou metodu pro odkazování na konkrétní kmitočty nosných, což umožňuj"
---

ARFCN je jedinečný číselný identifikátor pro každý rádiový frekvenční kanál v mobilních sítích, který poskytuje standardizovanou metodu pro odkazování na konkrétní kmitočty nosných napříč generacemi od GSM po 5G-NR.

## Popis

Absolutní číslo rádiového frekvenčního kanálu (ARFCN) slouží jako základní adresovací mechanismus pro rádiové frekvenční zdroje v 3GPP mobilních systémech. Funguje jako schéma číslování kanálů, které se mapuje na konkrétní středové kmitočty v určených kmitočtových pásmech. Každé ARFCN odpovídá konkrétnímu kmitočtu nosné, přičemž mapování je definováno matematickými vzorci, které se liší v závislosti na technologii rádiového přístupu (GSM, UMTS, LTE nebo NR) a používaném kmitočtovém pásmu. Toto systematické číslování umožňuje síťovým zařízením a uživatelským terminálům jednoznačně identifikovat a naladit se na konkrétní rádiové kanály bez nutnosti přímé specifikace kmitočtu v hertzech.

Systém ARFCN funguje tak, že vytváří lineární vztah mezi čísly kanálů a skutečnými rádiovými kmitočty. Pro systémy GSM vzorec typicky následuje F = F_low + 0,2 × (N - N_off), kde F je kmitočet nosné v MHz, F_low je dolní okrajová frekvence pásma, N je ARFCN a N_off je offset. V LTE a 5G-NR složitější vzorce zohledňují různé šířky pásma kanálů a rastrové offsety. Síť vysílá hodnoty ARFCN v blocích systémových informací, měřicích konfiguracích a příkazech k předání hovoru, což umožňuje zařízením identifikovat, které kmitočty mají monitorovat, měřit nebo na kterých se mají připojit. Základnové stanice používají ARFCN pro konfiguraci svých vysílacích kmitočtů a pro koordinaci využití kmitočtů se sousedními buňkami.

Klíčové součásti systému ARFCN zahrnují vzorce pro číslování kanálů definované ve specifikacích 3GPP pro každé kmitočtové pásmo, rastr kanálů (minimální kmitočtový krok mezi sousedními ARFCN) a parametry specifické pro pásmo, jako jsou offsety pro uplink/downlink u systémů [FDD](/mobilnisite/slovnik/fdd/). ARFCN plní více kritických rolí: slouží jako kmitočtový referenční bod pro počáteční vyhledávání a výběr buňky, umožňuje přesné řízení rádiových zdrojů, usnadňuje mezifrekvenční měření a měření mezi různými [RAT](/mobilnisite/slovnik/rat/) a podporuje mobilní procedury, jako jsou předání hovoru. Operátoři sítí používají plánování ARFCN pro přidělování kmitočtů buňkám při vyhýbání se interferencím a zařízení používají dekódování ARFCN k identifikaci dostupných sítí při roamingu.

V moderních 5G sítích se ARFCN vyvinulo do systému [NR-ARFCN](/mobilnisite/slovnik/nr-arfcn/) s globálním kmitočtovým rastrem 5 kHz, 15 kHz nebo 60 kHz v závislosti na kmitočtovém rozsahu. To umožňuje 5G podporovat širší šířky pásma a flexibilnější uspořádání spektra při zachování zpětné kompatibility s dřívějšími systémy. Koncept ARFCN zůstává nezbytný pro kmitočtovou synchronizaci, konfiguraci agregace nosných a nastavení duální konektivity, kde se zařízení současně připojují k nosným LTE a NR identifikovaným jejich příslušnými ARFCN.

## K čemu slouží

ARFCN bylo vytvořeno, aby vyřešilo základní problém identifikace a správy kmitočtů v mobilních sítích. Před standardizovaným číslováním kanálů používali různí výrobci a operátoři různé metody pro odkazování na kmitočty, což vedlo k problémům s kompatibilitou, zejména pro roamující zařízení a více-dodavatelské sítě. Systém ARFCN poskytuje univerzální jazyk pro specifikaci kmitočtů, který funguje napříč různými dodavateli zařízení, síťovými operátory a geografickými regiony.

Historický kontext vývoje ARFCN začíná standardizací GSM v 80. letech 20. století, kdy se s globální expanzí mobilních sítí stala zřejmou potřeba jednoduché a efektivní metody pro identifikaci [RF](/mobilnisite/slovnik/rf/) kanálů. Rané mobilní systémy používaly přímou specifikaci kmitočtů, která byla pro konfiguraci těžkopádná a náchylná k chybám. ARFCN tyto limity řešilo vytvořením abstraktní vrstvy, kde síťové elementy mohly odkazovat na kmitočty pomocí jednoduchých celých čísel namísto přesných hodnot v hertzech. Tato abstrakce zjednodušila plánování sítě, implementaci zařízení a provozní procedury.

ARFCN řeší několik praktických problémů: umožňuje efektivní signalizaci (malé celočíselné hodnoty vyžadují pro přenos méně bitů než hodnoty kmitočtů), podporuje nezávislost na kmitočtovém pásmu (stejná hodnota ARFCN se může mapovat na různé skutečné kmitočty v různých pásmech) a usnadňuje standardizaci hlášení měření. Jak se mobilní technologie vyvíjela přes UMTS, LTE a 5G, koncept ARFCN se ukázal být přizpůsobivý novým požadavkům, jako je agregace nosných, kde více ARFCN identifikuje komponentní nosné, a scénáře sdílení sítí, kde různí operátoři používají stejnou fyzickou infrastrukturu, ale různé logické ARFCN pro své spektrální zdroje.

## Klíčové vlastnosti

- Jedinečný číselný identifikátor pro každý RF kanál
- Technologicky specifické mapovací vzorce (GSM, UMTS, LTE, NR)
- Parametry a kmitočtové offsety závislé na pásmu
- Podporuje oba duplexní režimy FDD i TDD
- Umožňuje přesnou kmitočtovou synchronizaci a naladění
- Usnadňuje mezifrekvenční měření a měření mezi různými RAT

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [UARFCN – UTRA Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/uarfcn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements
- **TR 38.852** (Rel-17) — 1900MHz NR band for European Rail Mobile Radio
- **TR 38.853** (Rel-17) — 900MHz NR Band for European Rail Mobile Radio
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [ARFCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/arfcn/)
