---
slug: "eisrefsens"
url: "/mobilnisite/slovnik/eisrefsens/"
type: "slovnik"
title: "EISREFSENS – OTA Reference Sensitivity"
date: 2025-01-01
abbr: "EISREFSENS"
fullName: "OTA Reference Sensitivity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eisrefsens/"
summary: "Specifické měření citlivosti přijímače přes vzduch (OTA) definované pro základnové stanice 5G NR (gNB). Představuje minimální úroveň přijímaného výkonu na anténním portu potřebnou k dosažení definovan"
---

EISREFSENS je minimální úroveň přijímaného výkonu na anténním portu základnové stanice 5G potřebná k dosažení definované propustnosti, což zajišťuje spolehlivou detekci vzestupného signálu od uživatelského zařízení.

## Popis

EISREFSENS, neboli [OTA](/mobilnisite/slovnik/ota/) referenční citlivost, je klíčový ukazatel výkonu definovaný ve specifikacích 3GPP pro hodnocení citlivosti přijímačů základnových stanic 5G New Radio (NR) v testovacím prostředí přes vzduch. Jedná se o specifickou aplikaci širšího konceptu Ekvivalentní izotropní citlivosti ([EIS](/mobilnisite/slovnik/eis/)), přizpůsobenou pro zařízení základnových stanic. Metrika kvantifikuje minimální úroveň výkonu, vyjádřenou v dBm, která musí dopadat na anténní pole gNB, aby bylo dosaženo stanovené referenční propustnosti (typicky 95 % maximální propustnosti) pro definovaný referenční měřicí kanál. Toto měření zahrnuje vlivy vyzařovacího diagramu antény základnové stanice, jejího zisku a případných charakteristik beamforming za testovacích podmínek.

Měřicí postup, detailně popsaný ve specifikacích jako 38.141, zahrnuje umístění testovaného gNB do bezodrazové komory. Testovací UE nebo kalibrovaný rádiový zdroj vysílá standardizovaný vzestupný signál. Výkon přijímaný anténou gNB je přesně řízen a měřen. Testovací systém následně vyhodnocuje chybovost bloků ([BLER](/mobilnisite/slovnik/bler/)) nebo propustnost přijímaného signálu. Iterativním upravováním vysílacího výkonu je identifikována minimální úroveň výkonu potřebná k dosažení cílové propustnosti. Tato hodnota je EISREFSENS. Test se provádí pro konkrétní provozní pásma NR, šířky pásma a numerologie (rozestupy podnosných), a často pro různé směry paprsku, pokud gNB využívá beamforming.

EISREFSENS je klíčový pro ověření, že základnová stanice může efektivně přijímat signály od uživatelského zařízení, zejména od těch na okraji buňky, kde je přijímaný výkon nízký. Přímo ovlivňuje poloměr pokrytí vzestupného spoje buňky. Nižší (lepší) hodnota EISREFSENS znamená, že gNB dokáže detekovat slabší signály, což umožňuje širší pokrytí nebo lepší výkon ve scénářích omezených interferencí. Standardizace tohoto OTA měření zajišťuje, že přijímače základnových stanic od různých výrobců splňují minimální výkonnostní standardy, což přispívá ke konzistentní kvalitě sítě a umožňuje přesné plánování rádiové sítě. Dopňuje měření citlivosti na konektoru tím, že poskytuje validaci na systémové úrovni zahrnující anténní subsystém.

## K čemu slouží

EISREFSENS byl zaveden ve 3GPP Release 15 spolu s prvními specifikacemi 5G NR, aby řešil jedinečné výzvy testování přijímačů základnových stanic v éře 5G. Předchozí generace se více spoléhaly na měření na konektoru u anténních portů, která se stala méně reprezentativní pro systémy s aktivními anténami ([AAS](/mobilnisite/slovnik/aas/)) a masivní [MIMO](/mobilnisite/slovnik/mimo/) pole, kde jsou anténa a rádiová část hluboce integrovány. Měření na konektoru nemohla zachytit vliv beamforming, vazby mezi anténami nebo celkového vyzařovacího diagramu.

Účelem definice EISREFSENS bylo vytvořit standardizovanou, realistickou metodu pro ověření citlivosti přijímače základnové stanice v provozním kontextu. Řeší problém zajištění správné funkce celého přijímacího řetězce – od zářičů přes [RF](/mobilnisite/slovnik/rf/) a digitální beamforming jednotky. To je obzvláště důležité pro 5G sítě využívající vyšší frekvence (jako mmWave) s větším útlumem na dráze, které se spoléhají na beamforming pro udržení rozpočtu spoje. Zavedením povinných testů [OTA](/mobilnisite/slovnik/ota/) referenční citlivosti 3GPP zajišťuje, že základnové stanice nasazené v terénu budou spolehlivě přijímat vzestupné přenosy, což je základní pro pokrytí sítě, její kapacitu a uživatelský zážitek. Poskytuje síťovým operátorům garantovaný výkonnostní metrik pro účely nákupu a nasazení.

## Klíčové vlastnosti

- Metrika OTA citlivosti specificky pro přijímače základnových stanic 5G NR (gNB)
- Zahrnuje efekty integrovaných anténních polí a beamforming
- Definována pro specifické referenční měřicí kanály a cíle propustnosti (např. 95 % maxima)
- Testována napříč kmitočtovými rozsahy NR (FR1 a FR2) a různými šířkami pásma
- Zásadní pro validaci pokrytí vzestupného spoje a výkonu na okraji buňky
- Standardizovaná metodologie umožňuje spravedlivé srovnání mezi různými výrobci gNB a návrhy AAS

## Definující specifikace

- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.817** — 3GPP TR 38.817

---

📖 **Anglický originál a plná specifikace:** [EISREFSENS na 3GPP Explorer](https://3gpp-explorer.com/glossary/eisrefsens/)
