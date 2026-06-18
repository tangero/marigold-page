---
slug: "sinr"
url: "/mobilnisite/slovnik/sinr/"
type: "slovnik"
title: "SINR – Signal to Interference plus Noise Ratio"
date: 2025-01-01
abbr: "SINR"
fullName: "Signal to Interference plus Noise Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sinr/"
summary: "SINR je klíčová metrika představující kvalitu přijímaného rádiového signálu. Je to poměr výkonu požadovaného signálu k součtu výkonu interference (z jiných buněk/uživatelů) a výkonu šumu pozadí. SINR"
---

SINR je poměr výkonu požadovaného signálu ke kombinovanému výkonu interference z jiných buněk nebo uživatelů a šumu pozadí, který určuje kvalitu signálu a dosažitelnou přenosovou rychlost v buněčné síti.

## Popis

Signal to Interference plus Noise Ratio (SINR) je základní a klíčová metrika výkonu v bezdrátových komunikacích, která kvantifikuje kvalitu přijímaného signálu v konkrétním časovém okamžiku a místě. Matematicky je vyjádřena jako SINR = P_S / (P_I + P_N), kde P_S je výkon požadovaného signálu, P_I je celkový výkon interferenčních signálů (např. ze sousedních buněk používajících stejnou frekvenci) a P_N je výkon aditivního šumu pozadí (tepelný šum). Na rozdíl od [SNR](/mobilnisite/slovnik/snr/) (Signal-to-Noise Ratio), které zohledňuje pouze šum, SINR bere v potaz praktickou realitu buněčných sítí: interference je často dominantním limitujícím faktorem, zejména v hustých nasazeních.

SINR měří přijímač, typicky uživatelské zařízení (UE) v downlinku nebo základnová stanice (gNB/[eNB](/mobilnisite/slovnik/enb/)) v uplinku. Proces měření zahrnuje odhad výkonu referenčních signálů (např. Cell-Specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Synchronization Signal Blocks (SSB)/Channel State Information Reference Signals ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) v NR) pro požadovaný signál. Současně přijímač odhaduje celkový výkon v rámci šířky přenosového pásma, který zahrnuje požadovaný signál, interferenci a šum. Odečtením odhadnutého výkonu požadovaného signálu od celkového výkonu se získá odhad výkonu interference a šumu. Tato měření jsou hlášena síti jako Channel State Information ([CSI](/mobilnisite/slovnik/csi/)), což je zásadní pro adaptivní přidělování prostředků.

Role SINR je ústřední pro několik funkcí správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)). Je to hlavní determinant zvoleného modulačního a kódového schématu ([MCS](/mobilnisite/slovnik/mcs/)) pro přenos. Vysoká hodnota SINR umožňuje použití modulace vyššího řádu (např. 256QAM, 1024QAM) a nízké kódové redundance, což přináší vysoké přenosové rychlosti. Nízká hodnota SINR vyžaduje robustní modulaci nižšího řádu (např. [QPSK](/mobilnisite/slovnik/qpsk/)) a silné kanálové kódování. Dále měření SINR řídí rozhodnutí o předávání spojení, algoritmy řízení výkonu a techniky koordinace interference jako Enhanced Inter-Cell Interference Coordination (eICIC) nebo Coordinated Multipoint (CoMP). V 5G NR jsou odhady SINR pro různé paprsky zásadní pro správu a výběr paprsků. SINR je v konečném důsledku klíčovým článkem spojujícím fyzikální rádiové podmínky s kvalitou služby vnímanou uživatelem a celkovou kapacitou sítě.

## K čemu slouží

SINR existuje jako komplexní metrika pro přesné vyhodnocení použitelnosti rádiového spoje v buněčných systémech omezených interferencí. Rané bezdrátové systémy byly často omezené šumem, takže SNR byla dostačující metrikou. Jak se však buněčné sítě vyvíjely s frekvenční reutilizací pro maximalizaci kapacity, se ko-kanálová interference stala hlavním omezením výkonu. SNR tuto realitu nedokázalo zachytit, což vedlo k nepřesné adaptaci spojení a špatnému přidělování prostředků. SINR byl zaveden, aby poskytl věrné měřítko 'čistoty signálu' za přítomnosti jak šumu, tak dominantních interferenčních signálů od jiných vysílačů.

Jeho vznik byl motivován potřebou inteligentního provozu sítě. Přesným měřením SINR může síť činit informovaná rozhodnutí pro optimalizaci výkonu. Například umožňuje adaptivní modulaci a kódování, které maximalizuje propustnost pro každého uživatele na základě jeho okamžitých kanálových podmínek. Je také klíčovým vstupem pro strategie řízení interference; identifikací buněk nebo uživatelů se špatným SINR může síť spustit procedury pro zmírnění interference. Historicky se pozornost na SINR zesílila s přechodem na systémy založené na OFDMA, jako jsou LTE a NR, kde je intracelulární interference minimální, což činí intercelulární interferenci hlavním problémem. SINR poskytuje detailní data v reálném čase potřebná pro funkce samoorganizujících se sítí (SON) a hustá heterogenní nasazení, která charakterizují moderní 4G a 5G sítě.

## Klíčové vlastnosti

- Definuje kvalitu rádiového spoje zohledněním požadovaného signálu, interference a šumu
- Přímo určuje dosažitelné modulační a kódové schéma (MCS) a přenosovou rychlost
- Používá se jako klíčový vstup pro hlášení informace o stavu kanálu (CSI)
- Řídí kritické funkce správy rádiových prostředků (RRM), jako je předání spojení a řízení výkonu
- Zásadní pro techniky řízení a koordinace interference
- Měřen na referenčních signálech (např. CRS, CSI-RS, SSB) specifických pro danou technologii

## Související pojmy

- [SNR – Spending Status Notification Request](/mobilnisite/slovnik/snr/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TS 36.884** (Rel-13) — MMSE-IRC Receiver Performance for LTE BS
- **TS 36.894** (Rel-13) — Study on LTE Measurement Gap Enhancement
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [SINR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sinr/)
