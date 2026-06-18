---
slug: "pt-rs"
url: "/mobilnisite/slovnik/pt-rs/"
type: "slovnik"
title: "PT-RS – Phase Tracking Reference Signal"
date: 2025-01-01
abbr: "PT-RS"
fullName: "Phase Tracking Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pt-rs/"
summary: "Referenční signál zavedený v 5G NR pro odhad a kompenzaci fázového šumu ve vysokofrekvenčních pásmech a pokročilých anténních systémech. Je klíčový pro udržení koherentní demodulace a dosažení vysoké"
---

PT-RS je referenční signál 5G NR, který odhaduje a kompenzuje fázový šum ve vysokofrekvenčních pásmech za účelem zachování koherentní demodulace a vysoké spektrální účinnosti.

## Popis

Phase Tracking Reference Signal (PT-RS) je referenční signál fyzické vrstvy definovaný v rádiovém rozhraní 5G New Radio (NR) od 3GPP Release 15. Jeho primární funkcí je umožnit přijímači odhadnout a sledovat rychlé fázové variace, známé jako fázový šum, které mohou výrazně degradovat výkon modulačních schémat vyššího řádu, jako je 256-QAM nebo 1024-QAM. Fázový šum se stává dominantním znehodnocením na vyšších nosných frekvencích (např. v mmWave pásmech nad 24 GHz) a v systémech využívajících výkonné zesilovače nebo složité víceanténní ([MIMO](/mobilnisite/slovnik/mimo/)) konfigurace. PT-RS poskytuje známou pilotní sekvenci, která je vložena do časově-frekvenční mřížky [OFDM](/mobilnisite/slovnik/ofdm/), což umožňuje přijímači změřit fázové zkreslení, kterému jsou vystaveny datové symboly, a aplikovat korekci.

Z architektonického hlediska je PT-RS uživatelsky specifický referenční signál (UE-specific), což znamená, že jeho konfigurace – včetně hustoty v čase a frekvenci, jeho skramblovací sekvence a mapování na prvky prostředků – je dynamicky plánována gNodeB pro každé uživatelské zařízení (UE) na základě faktorů, jako je plánované modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)), nosná frekvence a nahlášené schopnosti UE. Signál může být vysílán jak v downlinku (z gNB do UE), tak v uplinku (z UE do gNB). V downlinku pomáhá příjmu UE; v uplinku pomáhá gNB demodulovat signály od UE, které zažívají významný fázový šum. PT-RS je těsně integrován s dalšími referenčními signály, jako je Demodulation Reference Signal ([DM-RS](/mobilnisite/slovnik/dm-rs/)) pro odhad kanálu a Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) pro sondování kanálu.

Během provozu gNB konfiguruje parametry PT-RS prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a dynamicky jej aktivuje prostřednictvím Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). PT-RS je typicky řídký, s konfigurovatelnou hustotou (např. jeden PT-RS symbol každé 2, 4 nebo více OFDM symbolů v čase a jeden PT-RS subnosný na blok prostředků ve frekvenci), aby byla vyvážena režie vůči přesnosti sledování. Přijímač používá lineární interpolaci nebo pokročilejší filtrování napříč těmito referenčními body k vytvoření spojitého odhadu fázové chyby v celé plánované šířce pásma a po celou dobu trvání. Tento odhad je pak použit k derotaci přijatých datových symbolů, čímž se koriguje společná fázová chyba (CPE) a potenciálně i složky mezinosné interference (ICI) fázového šumu.

Jeho role v síti je zásadní pro využití plného potenciálu vylepšeného mobilního širokopásmového připojení (eMBB) a komunikace s ultra-spolehlivým nízkým zpožděním (URLLC) v 5G NR. Tím, že zmírňuje fázový šum, PT-RS zajišťuje robustní výkon spoje, umožňuje použití modulací vyššího řádu pro vyšší datové rychlosti a udržuje nízkou blokovou chybovost (BLER) pro spolehlivost. Je klíčovým prvkem pro provoz ve frekvenčním rozsahu 2 (FR2), podporujícím cíle vysoké propustnosti a konektivity sítí 5G-Advanced.

## K čemu slouží

PT-RS byl vytvořen k řešení zásadní výzvy na fyzické vrstvě, která se stala akutní s evolucí směrem k 5G: znehodnocení fázovým šumem. Předchozí generace mobilních sítí (LTE a starší) fungovaly primárně na frekvencích pod 6 GHz, kde byl fázový šum z oscilátorů relativně nízký a dal se zvládnout inherentní robustností modulací nižšího řádu nebo byl vyprůměrován jinými referenčními signály, jako je Cell-Specific Reference Signal (CRS). Expanze 5G do milimetrového pásma (mmWave), od 24,25 GHz až do 52,6 GHz a výše, však zavedla výrazně vyšší fázový šum kvůli fyzice vysokofrekvenčních lokálních oscilátorů. Navíc použití pokročilých víceanténních technik (massive MIMO) a širších šířek pásma učinilo systém citlivějším na tyto rychlé, náhodné fázové fluktuace.

Omezení předchozích přístupů byla zřejmá. Spoléhání se pouze na DM-RS pro sledování fáze bylo nedostatečné, protože DM-RS je primárně navržen pro odhad kanálu (amplituda a fáze kanálu) a není v čase dostatečně hustý, aby sledoval rychlé variace fázového šumu, zejména pro dlouhé bloky symbolů. Bez vyhrazeného sledování fáze by modulace vyššího řádu (např. 1024-QAM) trpěly katastrofálním nárůstem chybovosti, což by negovalo zisky ve spektrální účinnosti. PT-RS to řeší tím, že poskytuje vyhrazený, konfigurovatelný pilotní signál optimalizovaný pro sledování specifické charakteristiky fázového šumu – společné fázové chyby napříč všemi subnosnými a frekvenčně závislé složky. Jeho zavedení bylo motivováno potřebou odemknout vysoké datové rychlosti a spolehlivou konektivitu slibovanou 5G v jeho nových frekvenčních doménách, a zajistit tak, aby pokroky ve spektru a anténní technologii nebyly limitovány tímto základním fyzikálním znehodnocením.

## Klíčové vlastnosti

- Uživatelsky specifická konfigurace (UE-specific) a dynamická aktivace prostřednictvím plánování DCI
- Konfigurovatelná hustota v čase a frekvenci pro kompromis mezi režií a přesností sledování
- Podpora jak downlinku (pro příjem UE), tak uplinku (pro příjem gNB)
- Umožňuje kompenzaci společné fázové chyby (CPE) a mezinosné interference (ICI)
- Kritický pro podporu modulací vyššího řádu (až do 1024-QAM) ve vysokofrekvenčních pásmech
- Integrovaný s rámcovou strukturou 5G NR a mřížkou prostředků

## Související pojmy

- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [PT-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pt-rs/)
