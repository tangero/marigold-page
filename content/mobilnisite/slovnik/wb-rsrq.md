---
slug: "wb-rsrq"
url: "/mobilnisite/slovnik/wb-rsrq/"
type: "slovnik"
title: "WB-RSRQ – Wide Band Reference Signal Received Quality"
date: 2025-01-01
abbr: "WB-RSRQ"
fullName: "Wide Band Reference Signal Received Quality"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/wb-rsrq/"
summary: "WB-RSRQ je měření na straně UE pro LTE a NR, které posuzuje kvalitu širokopásmových referenčních signálů vzhledem k celkovému rušení a šumu. Je klíčové pro správu rádiových prostředků, rozhodování o p"
---

WB-RSRQ je měření na straně UE v LTE a NR, které vyhodnocuje kvalitu širokopásmových referenčních signálů vzhledem k celkovému rušení a šumu. Používá se pro správu rádiových prostředků a rozhodování o mobilitě.

## Popis

Wide Band Reference Signal Received Quality (WB-RSRQ) je klíčové měření vrstvy 3 definované ve specifikacích 3GPP pro uživatelské zařízení (UE) v systémech LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Jedná se o rozšíření tradičního měření [RSRQ](/mobilnisite/slovnik/rsrq/) (Reference Signal Received Quality), navržené k vyhodnocení kvality přijímaných referenčních signálů v širší šířce pásma. Měření se vypočítá jako poměr širokopásmového [RSRP](/mobilnisite/slovnik/rsrp/) (Reference Signal Received Power) k širokopásmovému [RSSI](/mobilnisite/slovnik/rssi/) (Received Signal Strength Indicator), konkrétně N krát RSRP děleno RSSI, kde N je počet bloků prostředků ([RB](/mobilnisite/slovnik/rb/)), přes které se RSSI měří. Tím se získá metrika podobná poměru signálu k rušení a šumu ([SINR](/mobilnisite/slovnik/sinr/)), která odráží kvalitu referenčních signálů v širším frekvenčním rozsahu.

Z architektonického hlediska WB-RSRQ provádí fyzická vrstva UE a hlásí vyšším vrstvám ([RRC](/mobilnisite/slovnik/rrc/)) pro použití v procedurách mobility a správy rádiových prostředků. Síť konfiguruje měření prostřednictvím signalizace RRC, specifikuje parametry jako šířka pásma měření, kritéria hlášení (periodická nebo spouštěná událostí) a filtrační koeficienty. UE kontinuálně měří výkon buňkově specifických referenčních signálů ([CRS](/mobilnisite/slovnik/crs/) v LTE) nebo bloků synchronizačního signálu/CSI-RS (v NR) v rámci nakonfigurované šířky pásma pro výpočet RSRP, zatímco současně měří celkový přijímaný výkon (včetně výkonu obsluhující buňky, ko-kanálového rušení a tepelného šumu) ve stejném pásmu pro výpočet RSSI.

Hlavní úloha WB-RSRQ v síti spočívá ve vylepšení rozhodování o mobilitě a vyvažování zátěže, zejména v heterogenních sítích (HetNets) s malými buňkami. Na rozdíl od úzkopásmového RSRQ, které může odrážet kvalitu pouze na podmnožině bloků prostředků, poskytuje WB-RSRQ více průměrový a reprezentativní pohled na kvalitu kanálu napříč celou šířkou pásma nosné. To je obzvláště důležité pro širokopásmové nosné (např. 20 MHz, 100 MHz), kde se podmínky rušení mohou výrazně lišit v závislosti na frekvenci. Měření se používá při událostech jako A3 (sousední buňka se stane o offset lepší než obsluhující) pro předání hovoru a při převýběru buňky pro mobilitu v klidovém režimu. Pomáhá síti identifikovat buňky s lepší celkovou rádiovou kvalitou, což vede ke zlepšení propustnosti pro uživatele a snížení počtu spadlých hovorů.

Mezi klíčové komponenty zapojené do WB-RSRQ patří řetězec RF přijímače UE, jednotky základního pásma pro měření signálu a protokol RRC pro konfiguraci a hlášení. Měření je standardizováno, aby byla zajištěna konzistence napříč různými implementacemi UE a síťovými zařízeními. V NR lze WB-RSRQ měřit na blocích SS/PBCH nebo prostředcích CSI-RS, což poskytuje flexibilitu pro různá scénáře nasazení. Přesnost a latence hlášení WB-RSRQ jsou kritické pro správu rádiových prostředků v reálném čase, což z něj činí základní aspekt výkonu rádiového rozhraní LTE a NR.

## K čemu slouží

WB-RSRQ bylo zavedeno v 3GPP Release 11, aby řešilo omezení tradičního úzkopásmového RSRQ v širokopásmových nasazeních LTE a vznikajících heterogenních sítích. Před WB-RSRQ se měření RSRQ typicky prováděla v úzkém pásmu (např. 6 bloků prostředků), což mohlo neodpovídat celkové kvalitě nosné, zejména ve scénářích s frekvenčně selektivním útlumem nebo rušením. Toto úzkopásmové měření mohlo vést k suboptimálním rozhodnutím o předání hovoru, kdy se buňka mohla jevit lepší na konkrétním subpásmu, ale v celé šířce pásma podávala špatný výkon, což vedlo ke zhoršenému uživatelskému zážitku po předání.

Motivace pro WB-RSRQ vycházela z rostoucích šířek pásma nosných v LTE-Advanced (až 20 MHz zpočátku a později agregovaných nosných) a nasazení malých buněk (piko, femto) vedle makro buněk. V takových HetNets jsou vzorce rušení složité a mohou se výrazně lišit v závislosti na frekvenci. Širokopásmové měření kvality poskytuje holističtější pohled, umožňuje lepší vyvažování zátěže, koordinaci rušení a robustnost mobility. Například v ko-kanálovém HetNetu může UE na okraji buňky zažívat vysoké rušení ze sousední makro buňky na některých blocích prostředků, ale ne na jiných; WB-RSRQ zachycuje tento průměrovaný efekt a navádí síť k předání UE do buňky s konzistentně lepší širokopásmovou kvalitou.

Dále WB-RSRQ podporuje vylepšené algoritmy správy rádiových prostředků v síti. Poskytnutím metriky kvality v celé šířce pásma napomáhá frekvenčně selektivnímu plánování, koordinaci mezibuněčného rušení (ICIC) a správě agregace nosných. Usnadňuje také provoz funkcí jako vylepšená koordinace mezibuněčného rušení (eICIC) a další vylepšená ICIC (FeICIC) v Release 10 a 11, kde je přesné širokopásmové hodnocení kvality klíčové pro výběr téměř prázdných podrámců (ABS) a rozšíření dosahu v malých buňkách. WB-RSRQ bylo tedy vytvořeno za účelem zlepšení výkonu sítě, uživatelské propustnosti a spolehlivosti mobility v pokročilých systémech LTE a NR.

## Klíčové vlastnosti

- Měří kvalitu referenčního signálu v široké šířce pásma (konfigurovatelné sítí)
- Vypočítáno jako N*RSRP/RSSI, kde N je počet RB v měřené šířce pásma
- Podporuje měření pro LTE (založená na CRS) i NR (založená na SSB/CSI-RS)
- Konfigurovatelné prostřednictvím signalizace RRC pro periodické nebo událostmi spouštěné hlášení
- Používá se pro rozhodování o předání hovoru, převýběr buňky a správu rádiových prostředků
- Poskytuje průměrovanou metriku kvality, čímž snižuje dopad frekvenčně selektivního rušení

## Související pojmy

- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [RSSI – Received Signal Strength Indication](/mobilnisite/slovnik/rssi/)

## Definující specifikace

- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD

---

📖 **Anglický originál a plná specifikace:** [WB-RSRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/wb-rsrq/)
