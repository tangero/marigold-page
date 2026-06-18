---
slug: "lmmse"
url: "/mobilnisite/slovnik/lmmse/"
type: "slovnik"
title: "LMMSE – Linear Minimum Mean Squared Error"
date: 2025-01-01
abbr: "LMMSE"
fullName: "Linear Minimum Mean Squared Error"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lmmse/"
summary: "Statistický algoritmus pro zpracování signálu používaný v bezdrátových přijímačích k odhadu vysílaných symbolů minimalizací střední kvadratické chyby mezi skutečným a odhadovaným signálem. Je klíčový"
---

LMMSE je statistický algoritmus pro zpracování signálu používaný v bezdrátových přijímačích k odhadu vysílaných symbolů minimalizací střední kvadratické chyby, což zmírňuje interferenci a šum za účelem zlepšení spolehlivosti spoje a datových rychlostí.

## Popis

Linear Minimum Mean Squared Error (LMMSE) je základní technika odhadu a ekvalizace používaná na fyzické vrstvě 3GPP bezdrátových systémů, včetně LTE a NR. Funguje jako lineární filtr aplikovaný na vektor přijatého signálu. Základním principem je výpočet odhadu vysílaného signálového vektoru, který minimalizuje očekávanou hodnotu kvadrátu chyby mezi skutečným vysílaným signálem a odhadovaným signálem, s omezením, že odhadovač je lineární funkcí pozorování. To vyžaduje znalost nebo odhad informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), kovarianční matice šumu a případně kovarianční matice signálu. Váhy LMMSE filtru jsou vypočteny tak, aby optimálně vyvažovaly kompromis mezi inverzí kanálu pro obnovení signálu a potlačením zesíleného šumu, což je kritická slabina jednodušších technik, jako je ekvalizace Zero-Forcing ([ZF](/mobilnisite/slovnik/zf/)).

V praktických přijímacích architekturách, například pro [PDSCH](/mobilnisite/slovnik/pdsch/) (Physical Downlink Shared Channel), je algoritmus LMMSE implementován v rámci řetězce základního pásma. Po [OFDM](/mobilnisite/slovnik/ofdm/) demodulaci je přijatý signál ve frekvenční doméně pro každou podnosnou reprezentován jako Y = HX + N, kde H je matice kanálu, X je vektor vysílaných symbolů a N je aditivní šum. LMMSE odhad Ć je vypočten jako Ć = W * Y, kde matice filtru W je odvozena jako W = R_xx H^H (H R_xx H^H + R_nn)^{-1}. Zde je R_xx kovarianční matice vysílaného signálu (často předpokládaná jako jednotková matice škálovaná výkonem signálu), H^H je Hermitovsky transponovaná matice kanálu a R_nn je kovarianční matice šumu. Tato formulace explicitně zohledňuje výkon šumu, což ji činí robustní v podmínkách nízkého poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)).

Role LMMSE je klíčová v detekci Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)), kde se používá k oddělení prostorově multiplexovaných datových proudů. Jeho výpočetní složitost je vyšší než u ZF, ale poskytuje lepší výkon, zejména ve scénářích omezených interferencí. V plánování sítí a ověřování výkonu, jak je popsáno ve specifikacích jako 36.829, slouží LMMSE jako referenční model přijímače pro vyhodnocování pokrytí a propustnosti. Jeho implementace se nachází v přijímačích uživatelského zařízení (UE) a základnových stanic (gNB/[eNB](/mobilnisite/slovnik/enb/)) a je klíčovým prvkem pro dosažení vysokých cílů spektrální účinnosti moderních celulárních standardů. Pokročilé varianty a aproximace LMMSE jsou také studovány za účelem snížení výpočetní náročnosti pro praktickou implementaci.

## K čemu slouží

Odhadovač LMMSE byl zaveden, aby řešil základní výzvu spolehlivé detekce dat v přítomnosti zkreslení kanálu, šumu a interference. Dřívější, jednodušší lineární přijímače, jako je přizpůsobený filtr nebo ekvalizace Zero-Forcing, měly významné nedostatky: přizpůsobený filtr je optimální pouze pro jediný proud v bílém šumu, ale při interferenci funguje špatně, zatímco [ZF](/mobilnisite/slovnik/zf/) ekvalizace dokonale invertuje kanál, ale katastrofálně zesiluje šum, což vede ke špatnému výkonu při nízkém SNR. Bezdrátový kanál v celulárních systémech je inherentně časově proměnný a frekvenčně selektivní a s přijetím MIMO se mezistopová interference stala hlavním omezením.

LMMSE poskytuje matematicky rigorózní rámec pro optimalizaci výkonu přijímače minimalizací průměrné odhadové chyby. Řeší kritický technický kompromis mezi obnovením signálu a zesílením šumu. Jeho vytvoření bylo motivováno potřebou robustního, teoreticky podloženého detekčního algoritmu, který by mohl být standardizován jako výkonnostní referenční bod a implementován v praktických přijímačích, aby splňoval stále rostoucí požadavky na datovou rychlost a spolehlivost spoje. V kontextu 3GPP standardizace umožňuje definice referenčních přijímacích algoritmů, jako je LMMSE, konzistentní a spravedlivé vyhodnocování výkonu různých nasazení sítí a schopností UE, čímž zajišťuje interoperabilitu a předvídatelnou kvalitu služeb.

## Klíčové vlastnosti

- Minimalizuje střední kvadratickou chybu mezi skutečným a odhadovaným signálovým vektorem
- Explicitně zohledňuje jak účinky kanálu, tak statistiku šumu v návrhu filtru
- Poskytuje lepší výkon než Zero-Forcing, zejména v podmínkách nízkého SNR
- Základní pro detekci MIMO a oddělení prostorových proudů
- Slouží jako standardní referenční model pro ověřování výkonu sítě v 3GPP
- Vyvažuje potlačení mezisymbolové interference s potlačením šumu

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.963** (Rel-19) — Feasibility Study on UMTS/HSDPA UE Interference Cancellation
- **TS 36.829** (Rel-11) — Feasibility Study on LTE UE Interference Cancellation

---

📖 **Anglický originál a plná specifikace:** [LMMSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmmse/)
