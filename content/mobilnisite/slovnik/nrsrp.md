---
slug: "nrsrp"
url: "/mobilnisite/slovnik/nrsrp/"
type: "slovnik"
title: "NRSRP – Narrowband Reference Signal Received Power"
date: 2025-01-01
abbr: "NRSRP"
fullName: "Narrowband Reference Signal Received Power"
category: "Physical Layer"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nrsrp/"
summary: "Narrowband Reference Signal Received Power (NRSRP) je měření na fyzické vrstvě v LTE-M a NB-IoT, které kvantifikuje přijímaný výkon úzkopásmových referenčních signálů. Používá se pro výběr buňky, před"
---

NRSRP je měření na fyzické vrstvě v LTE-M a NB-IoT, které kvantifikuje přijímaný výkon úzkopásmových referenčních signálů pro výběr buňky, předávání hovoru (handover) a odhad pokrytí.

## Popis

Narrowband Reference Signal Received Power (NRSRP) je klíčové rádiové měření specifické pro technologie Narrowband Internet of Things (NB-IoT) a LTE-M (Cat-M1) v rámci standardů 3GPP LTE a 5G NR. Představuje lineární průměrný výkon přijímaný uživatelským zařízením (UE) na zdrojových prvcích, které nesou úzkopásmové referenční signály ([NRS](/mobilnisite/slovnik/nrs/)) ve stanovené měřicí šířce pásma, typicky 180 kHz pro NB-IoT. NRSRP je odvozeno z referenčních signálů na downlinku vysílaných základnovou stanicí (eNodeB v LTE, gNB v NR), které jsou určeny pro odhad kanálu a synchronizaci. Proces měření zahrnuje demodulaci těchto referenčních signálů uživatelským zařízením, které jsou rozloženy v čase a frekvenci napříč úzkopásmovým nosičem, a výpočet přijímaného výkonu v jednotkách dBm. Tato hodnota je klíčová pro vyhodnocení síly signálu v nízkopříkonových širokoplošných scénářích, kde IoT zařízení často pracují v náročných rádiových podmínkách, jako jsou hluboko uvnitř budov nebo venkovské oblasti. NRSRP používá uživatelské zařízení pro procedury výběru a převýběru buňky, aby určilo nejvhodnější buňku pro připojení na základě kvality signálu. Také informuje o rozhodnutích pro předání hovoru a mechanismech řízení výkonu, čímž zajišťuje spolehlivé připojení při minimalizaci spotřeby baterie. Měření je hlášeno síti prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), což síti umožňuje optimalizovat přidělování prostředků a pokrytí. Ve srovnání s měřeními v širším pásmu, jako je [RSRP](/mobilnisite/slovnik/rsrp/) v klasickém LTE, je NRSRP uzpůsobeno pro úzkopásmový provoz a poskytuje přesné hodnocení v prostředích s omezenou šířkou pásma, což je zásadní pro nasazení IoT.

## K čemu slouží

Účelem Narrowband Reference Signal Received Power (NRSRP) je řešit specifické požadavky IoT zařízení v celulárních sítích, zejména pro technologie NB-IoT a LTE-M zavedené ve 3GPP Release 13 a novějších. Tradiční měření LTE, jako je [RSRP](/mobilnisite/slovnik/rsrp/), byla navržena pro širší šířky pásma (např. 1,4 MHz až 20 MHz) a vyšší přenosové rychlosti, což je neefektivní pro IoT zařízení, která upřednostňují nízkou spotřebu energie, rozšířené pokrytí a provoz v úzkých šířkách pásma (např. 180 kHz). NRSRP bylo vytvořeno, aby poskytlo přesné měření síly signálu optimalizované pro tyto úzkopásmové nosiče, což umožňuje přesné vyhodnocení buňky v prostředích s omezeným spektrem a náročnými podmínkami šíření. Řeší problémy, jako je spolehlivý výběr buňky v režimech s rozšířeným pokrytím (např. až 20 dB dodatečného zisku pro NB-IoT), kde zařízení potřebují detekovat velmi slabé signály. Motivace vychází z rozšíření aplikací masivního IoT, jako jsou chytré měřiče, senzory a sledovací zařízení, které vyžadují dlouhou životnost baterie a robustní připojení v oblastech se slabým signálem. Zavedením NRSRP umožnilo 3GPP efektivní správu rádiových prostředků pro IoT, podporující funkce jako rozšířený přerušovaný příjem (eDRX) a režim úspory energie ([PSM](/mobilnisite/slovnik/psm/)), což v konečném důsledku usnadňuje škálovatelná a energeticky účinná nasazení IoT.

## Klíčové vlastnosti

- Měří přijímaný výkon úzkopásmových referenčních signálů v šířce pásma 180 kHz.
- Používá se pro výběr buňky, převýběr buňky a předání hovoru v NB-IoT a LTE-M.
- Podporuje režimy rozšíření pokrytí až se ziskem 20 dB.
- Umožňuje přesné vyhodnocení signálu v nízkopříkonových širokoplošných scénářích.
- Integrováno se signalizací RRC pro hlášení síti a optimalizaci.
- Uzpůsobeno pro IoT zařízení s omezenou šířkou pásma a omezeními baterie.

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)

## Definující specifikace

- **TS 32.857** (Rel-15) — Management of LTE IoT RAN Features
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [NRSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrsrp/)
