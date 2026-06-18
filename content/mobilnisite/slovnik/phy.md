---
slug: "phy"
url: "/mobilnisite/slovnik/phy/"
type: "slovnik"
title: "PHY – Physical Layer"
date: 2025-01-01
abbr: "PHY"
fullName: "Physical Layer"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/phy/"
summary: "Fyzická vrstva (PHY) je nejnižší vrstva (vrstva 1) v protokolovém zásobníku 3GPP, odpovědná za skutečný přenos a příjem rádiových signálů přes rozhraní vzdušného rozhraní. Zpracovává modulaci, kódován"
---

PHY je nejnižší vrstva v protokolovém zásobníku 3GPP, odpovědná za vysílání a příjem rádiových signálů prostřednictvím zpracování modulace, kódování a multiplexování přes rozhraní vzdušného rozhraní.

## Popis

Fyzická vrstva (PHY), označovaná jako vrstva 1 v modelu [OSI](/mobilnisite/slovnik/osi/) a protokolovém modelu 3GPP, je základem pro veškerou komunikaci přes vzdušné rozhraní v mobilních sítích. Její architektura je úzce spojena s konkrétní technologií rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)), jako je [UTRA](/mobilnisite/slovnik/utra/) (UMTS), [E-UTRA](/mobilnisite/slovnik/e-utra/) (LTE) nebo NR (5G). PHY se nachází jak v uživatelském zařízení (UE), tak v základnové stanici (Node B, eNodeB, gNB). Poskytuje přenosové kanály vyšší vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) nad ní, což jsou logické kanály mapované na konkrétní fyzické prostředky.

Fungování PHY zahrnuje vícestupňový proces pro vysílání i příjem. Na straně vysílače přijímá přenosové bloky z vrstvy MAC. Tyto bloky procházejí několika zpracovatelskými fázemi: připojením cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) pro detekci chyb, kanálovým kódováním (např. Turbo kódy, [LDPC](/mobilnisite/slovnik/ldpc/)) pro opravu chyb, přizpůsobením rychlosti a prokládáním. Zakódované bity jsou poté mapovány na modulační symboly (pomocí schémat jako [QPSK](/mobilnisite/slovnik/qpsk/), 16QAM, 256QAM). Tyto symboly jsou multiplexovány na fyzické prvky prostředků (jako jsou podnosné OFDM a symboly v LTE/NR) prostřednictvím procesů jako je scramblování, mapování modulace a předkódování. Nakonec je signál převeden do časové domény (přes IFFT v OFDM), přidán cyklický prefix a signál je zesílen a vyslán přes vysokofrekvenční (RF) front-end.

Klíčové součásti PHY zahrnují moduly kódování a modulace, modulátor schématu vícenásobného přístupu (např. OFDMA pro downlink, SC-FDMA pro uplink LTE), RF transceiver a funkce synchronizace a odhadu kanálu. Pro příjem provádí inverzní operace: RF příjem, synchronizace, odstranění cyklického prefixu, FFT, odhad kanálu a ekvalizace, demodulace, deprokládání, přizpůsobení rychlosti, dekódování kanálu a kontrola CRC. Jejím úkolem je spolehlivě doručit datové bity přes proměnlivý rádiový kanál a zvládat poruchy jako šum, interference, útlum a Dopplerův jev. Také provádí procedury fyzické vrstvy, jako je vyhledávání buňky, náhodný přístup, řízení výkonu, formování svazku (v NR) a měření (RSRP, RSRQ) pro rozhodnutí o mobilitě na vyšších vrstvách.

## K čemu slouží

Fyzická vrstva existuje, aby řešila základní problém přenosu digitální informace přes analogové, sdílené a nepříznivé rádiové prostředí. Převádí logické komunikační požadavky z vyšších vrstev na skutečné elektromagnetické vlny, které se mohou šířit prostorem a být správně interpretovány přijímačem. Motivací pro její neustálý vývoj napříč releasy 3GPP je zvýšení spektrální účinnosti (bitů/sec/Hz), zlepšení pokrytí a spolehlivosti, snížení latence a podpora různorodých požadavků služeb (např. massive IoT, ultra-spolehlivá komunikace s nízkou latencí).

Historicky každá nová generace (3G, 4G, 5G) zavedla novou PHY, aby překonala omezení té předchozí. Například přechod z WCDMA (3G) na LTE založené na OFDMA (4G) byl motivován potřebou vyšších špičkových datových rychlostí, lepší spektrální účinnosti a flexibility v alokaci šířky pásma. PHY WCDMA čelila výzvám s vícecestným rušením a složitým návrhem přijímače při vysokých rychlostech, což OFDMA pomohlo zmírnit.

Vytvoření každého nového standardu PHY řeší specifické technologické a službami řízené mezery. PHY 5G NR byla vytvořena pro podporu mnohem širšího rozsahu frekvencí (od pásem pod 1 GHz po mmWave), extrémních šířek pásma a různorodých případů užití vyžadujících různou numerologii (rozestup podnosných). Řeší problémy předchozích vrstev zavedením flexibilní, samostatné struktury slotů pro nízkou latenci, pokročilého massive MIMO a formování svazku pro pokrytí mmWave a nových kanálových kódů (LDPC pro data, Polar kódy pro řízení) pro lepší výkon při vysokých datových rychlostech. Účelem PHY je tedy realizovat schopnosti rádiového rozhraní, které umožňují služby slibované každou generací.

## Klíčové vlastnosti

- Definuje modulační schémata (např. QPSK, 16/64/256QAM, π/2-BPSK) a kódování (Turbo, LDPC, Polar)
- Specifikuje metodu vícenásobného přístupu (WCDMA, OFDMA, SC-FDMA) a strukturu rámce
- Spravuje mapování fyzických prostředků (bloky prostředků, podnosné, symboly, sloty)
- Implementuje dopřednou korekci chyb (FEC) a hybridní automatické opakování požadavku (HARQ)
- Provádí rádiové procedury: synchronizaci, vyhledávání buňky, náhodný přístup, měření kanálu
- Podporuje pokročilé anténní techniky (MIMO, formování svazku, předkódování)

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [PHY na 3GPP Explorer](https://3gpp-explorer.com/glossary/phy/)
