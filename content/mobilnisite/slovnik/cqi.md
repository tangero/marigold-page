---
slug: "cqi"
url: "/mobilnisite/slovnik/cqi/"
type: "slovnik"
title: "CQI – Channel Quality Indicator"
date: 2025-01-01
abbr: "CQI"
fullName: "Channel Quality Indicator"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cqi/"
summary: "CQI je klíčové měření hlášené UE síti, které indikuje kvalitu downlinkového rádiového kanálu. Používá se pro adaptivní modulaci a kódování (AMC) a rozhodnutí o plánování, což přímo ovlivňuje datovou p"
---

CQI je měření hlášené uživatelským zařízením, které indikuje kvalitu downlinkového kanálu, což síti umožňuje provádět adaptivní rozhodnutí o modulaci, kódování a plánování pro optimalizaci propustnosti a efektivity.

## Popis

Channel Quality Indicator (CQI) je kritický zpětnovazební mechanismus v rádiových přístupových sítích 3GPP, primárně pro downlink. Jedná se o kvantovanou reprezentaci vnímaných podmínek kanálu ze strany uživatelského zařízení (UE). UE kontinuálně měří downlinkové referenční signály, jako je Common Pilot Channel ([CPICH](/mobilnisite/slovnik/cpich/)) v UMTS nebo Channel State Information Reference Signals ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) v LTE a NR, aby odhadlo kvalitu kanálu. Tento odhad typicky zvažuje poměr přijímaného signálu k interferenci a šumu (SINR). UE pak tento odhadnutý SINR mapuje na předdefinovaný CQI index. Každý index odpovídá konkrétní kombinaci modulačního schématu (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM, 1024QAM) a míry kódování kanálu, kterou může UE podporovat s pravděpodobností chyby přenosového bloku nepřesahující 10%. Toto mapování je standardizováno, ale může být ovlivněno implementací a schopnostmi UE.

Z architektonického hlediska je hlášení CQI integrováno do procedur fyzické vrstvy a [MAC](/mobilnisite/slovnik/mac/) vrstvy. UE přenáší CQI report do sítě (eNodeB v LTE, gNB v NR) prostřednictvím uplinkových řídicích kanálů, jako je Physical Uplink Control Channel (PUCCH) nebo Physical Uplink Shared Channel (PUSCH). Hlášení může být periodické, spouštěné v nakonfigurovaných intervalech, nebo aperiodické, dynamicky spouštěné sítí prostřednictvím Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)). Plánovač sítě využívá přijaté CQI spolu s dalšími faktory, jako je stav vyrovnávací paměti a požadavky QoS, k činění dynamických rozhodnutí o plánování. Pro naplánované UE vybere vhodný modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)), velikost přenosového bloku a fyzické bloky zdrojů (PRB) pro downlinkový přenos. Tento proces, známý jako adaptace spojení, zajišťuje maximalizaci datového toku při zachování přijatelné míry chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)) pro aktuální rádiové podmínky.

Role CQI přesahuje rámec jednoduché adaptace spojení. Je základním vstupem pro pokročilé víceanténní techniky. Při operacích Multiple-Input Multiple-Output (MIMO) je hlášení CQI často spojeno se zpětnou vazbou Precoding Matrix Indicator (PMI) a Rank Indicator (RI), což je souhrnně označováno jako Channel State Information (CSI). Pro beamforming může být CQI hlášeno pro každý paprsek, což síti pomáhá vybrat optimální paprsek pro přenos. Při agregaci nosných je CQI hlášeno pro každou komponentní nosnou, což umožňuje plánování napříč nosnými a vyrovnávání zatížení. Přesnost a aktuálnost CQI reportů je proto prvořadá; zastaralé nebo nepřesné CQI může vést k suboptimálnímu výběru MCS, což způsobí buď nadměrné retransmise (pokud je příliš agresivní), nebo plýtvání spektrálními zdroji (pokud je příliš konzervativní). Design CQI tabulek, režimů hlášení a zpětnovazebních mechanismů se napříč releasy 3GPP výrazně vyvinul, aby podpořil vyšší datové toky, nová kmitočtová pásma a složitější anténní konfigurace.

## K čemu slouží

CQI bylo zavedeno, aby vyřešilo základní problém časově proměnlivého a kmitočtově selektivního útlumu v bezdrátových kanálech. Rané bezdrátové systémy často používaly pevnou modulaci a kódování, což bylo neefektivní – buď příliš robustní pro dobré podmínky (plýtvání kapacitou), nebo příliš křehké pro špatné podmínky (vysoká chybovost). Účelem CQI je umožnit adaptivní modulaci a kódování (AMC), což je klíčový princip moderních paketově orientovaných buněčných systémů jako HSPA, LTE a NR. Poskytnutím síti zpětné vazby o podmínkách downlinkového kanálu téměř v reálném čase může systém dynamicky přizpůsobit přenosové parametry okamžité kvalitě rádiového spoje. Tím se maximalizuje datová propustnost pro každého uživatele při zachování spolehlivosti, což dramaticky zlepšuje celkovou spektrální účinnost a kapacitu buňky.

Historicky, před sofistikovanou CQI zpětnou vazbou, systémy jako GSM používaly adaptaci spojení založenou na hrubých měřeních, která byla pomalejší a méně podrobná. Zavedení CQI v 3GPP Release 5 s HSDPA představovalo posun k rychlému, na kanálu založenému plánování v NodeB (základnové stanici), což znamenalo odklon od centralizovaného plánování v RNC. Tím se řešilo omezení pomalé reakční doby na změny kanálu. Zpětná vazba CQI umožňuje plánovači využít diverzitu více uživatelů tím, že preferenčně plánuje uživatele v jejich nejlepších kanálových podmínkách. Motivací pro jeho kontinuální vývoj je potřeba vyšších datových toků, podpora širších šířek pásma a implementace pokročilých víceanténních technologií (MIMO, beamforming). Každý nový release přináší vylepšení CQI hlášení za účelem snížení režie, zlepšení přesnosti pro nové scénáře (jako ultra-spolehlivá komunikace s nízkou latencí) a podpory operací ve vyšších kmitočtových pásmech s odlišnými charakteristikami šíření.

## Klíčové vlastnosti

- Kvantovaná zpětná vazba mapující odhadnutý SINR na podporované modulační a kódovací schéma (MCS)
- Umožňuje síťovému plánovači dynamickou adaptaci spojení (Adaptive Modulation and Coding - AMC)
- Podporuje více režimů hlášení: periodické (PUCCH) a aperiodické (PUSCH)
- Integrální součást hlášení Channel State Information (CSI) pro operace MIMO a beamformingu
- Hlášeno pro každou komponentní nosnou ve scénářích agregace nosných
- Používá standardizované tabulky definující CQI indexy, modulační řád, míru kódování a spektrální účinnost

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [CQI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cqi/)
