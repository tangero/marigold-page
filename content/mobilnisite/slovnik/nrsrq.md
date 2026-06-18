---
slug: "nrsrq"
url: "/mobilnisite/slovnik/nrsrq/"
type: "slovnik"
title: "NRSRQ – Narrowband Reference Signal Received Quality"
date: 2025-01-01
abbr: "NRSRQ"
fullName: "Narrowband Reference Signal Received Quality"
category: "Physical Layer"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nrsrq/"
summary: "NRSRQ je klíčové měření kvality rádiového signálu pro zařízení NB-IoT a LTE-M, které kvantifikuje poměr přijatého výkonu referenčního signálu k celkovému přijatému výkonu (včetně rušení a šumu). Je zá"
---

NRSRQ je poměr přijatého výkonu úzkopásmového referenčního signálu k celkovému přijatému výkonu, používaný pro výběr buňky a adaptaci spojení v sítích NB-IoT a LTE-M.

## Popis

Narrowband Reference Signal Received Quality (NRSRQ, kvalita přijatého úzkopásmového referenčního signálu) je kritické měření na vrstvě 1 definované ve specifikacích 3GPP pro Narrowband Internet of Things (NB-IoT) a LTE for Machine-Type Communications (LTE-M). Je to bezrozměrný poměr, typicky vyjádřený v decibelech (dB), který představuje kvalitu přijatých referenčních signálů z buňky. Konkrétně se NRSRQ vypočítá jako N-násobek poměru Narrowband Reference Signal Received Power ([NRSRP](/mobilnisite/slovnik/nrsrp/)) k Received Signal Strength Indicator ([RSSI](/mobilnisite/slovnik/rssi/)) celé nosné, kde N je počet bloků zdrojů použitých při měření RSSI. Matematicky NRSRQ = N * (NRSRP / RSSI). Toto měření poskytuje metriku podobnou poměru signálu k rušení a šumu ([SINR](/mobilnisite/slovnik/sinr/)), která je klíčová pro vyhodnocení kvality rádiového spoje za přítomnosti soukanálového rušení a šumu, což je přesnější ukazatel potenciální propustnosti než samotný přijatý výkon.

Architektura pro měření NRSRQ je zabudována v uživatelském zařízení (UE), konkrétně ve funkcích fyzické vrstvy (vrstva 1) a měřicí vrstvy (vrstva 3). Přijímač UE nepřetržitě sleduje úzkopásmové referenční signály ([NRS](/mobilnisite/slovnik/nrs/)) vysílané základnovou stanicí ([eNB](/mobilnisite/slovnik/enb/) pro LTE, gNB pro NR). Tyto referenční signály jsou předdefinované sekvence vložené do specifických prvků zdrojů v rámci sestupných rádiových rámců. UE měří výkon těchto známých sekvencí pro výpočet NRSRP. Současně měří celkový přijatý výkon (RSSI) v určené šířce pásma. Zpracování těchto surových měření pro odvození NRSRQ typicky zajišťuje firmwar modemu UE podle vzorců a konfigurací hlášení diktovaných standardy 3GPP a síťovou signalizací [RRC](/mobilnisite/slovnik/rrc/).

NRSRQ hraje zásadní roli v několika postupech správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)). Pro UE v nečinném režimu je primárním vstupem pro algoritmy výběru a převýběru buňky, což zajišťuje, že se zařízení připojí k buňce s nejkvalitnějším spojením, nikoli pouze s nejsilnějším signálem. V připojeném režimu jsou měření NRSRQ hlášena síti prostřednictvím hlášení o měřeních. Vrstva řízení rádiových zdrojů (RRC) sítě používá tato hlášení k přijímání klíčových rozhodnutí, jako je zahájení předání spojení, kdy je UE převedeno na sousední buňku s lepší kvalitou, a adaptace spojení, kde je modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) upraveno na základě nahlášené kvality kanálu pro optimalizaci spolehlivosti a účinnosti přenosu dat. Pro zařízení IoT s omezeným příkonem je přesné měření NRSRQ zásadní pro udržení připojení při minimalizaci spotřeby energie prostřednictvím efektivních strategií mobility a přenosu.

## K čemu slouží

NRSRQ bylo zavedeno pro řešení specifických potřeb technologií Low-Power Wide-Area Network (LPWAN) standardizovaných 3GPP, konkrétně NB-IoT a LTE-M. Před těmito technologiemi tradiční zařízení LTE používala Reference Signal Received Quality (RSRQ). Nicméně NB-IoT pracuje s mnohem užší šířkou pásma (180 kHz) ve srovnání se standardním LTE (které může mít 1,4 MHz až 20 MHz). Stávající měření RSRQ, navržené pro širší šířky pásma, nebylo optimální ani přímo použitelné pro přesné posouzení kvality signálu v tomto omezeném spektru. Úzkopásmový provoz představuje jedinečné charakteristiky rušení a výzvy pro měření.

Vytvoření NRSRQ bylo motivováno požadavkem na metriku kvality přizpůsobenou struktuře fyzické vrstvy NB-IoT. Řeší problém přesného posouzení použitelnosti rádiového spoje pro zařízení IoT, která často pracují na okraji buňky, v hlubokých vnitřních prostorách nebo v prostředích s vysokým rušením. Jednoduché měření výkonu (jako NRSRP) je nedostatečné, protože nezohledňuje rušení nebo šum, což jsou významné limitující faktory spolehlivosti dat. Poskytnutím poměru výkonu požadovaného signálu k celkovému přijatému výkonu dává NRSRQ síťovým algoritmům mnohem jasnější představu o tom, zda spojení může podporovat spolehlivou komunikaci, což umožňuje lepší správu mobility a přidělování zdrojů pro masivní nasazení IoT.

Historicky bylo zavedení NRSRQ v 3GPP Release 14 součástí širších vylepšení NB-IoT. Vyplnilo kritickou mezeru v rámci RRM pro IoT, což umožnilo těmto sítím dosáhnout cílů výkonu a spolehlivosti. Bez vyhrazené úzkopásmové metriky kvality by sítě musely spoléhat na improvizované nebo méně přesné metody, což by mohlo vést ke zvýšenému počtu přerušených spojení, neúspěšným předáním spojení a suboptimálním datovým rychlostem pro aplikace IoT, což by podkopalo hodnotový návrh celulárního IoT.

## Klíčové vlastnosti

- Bezrozměrný poměr NRSRP k celkovému RSSI, vyjádřený v dB.
- Specificky definován pro úzkopásmový provoz (180 kHz) v NB-IoT a LTE-M.
- Používá se jako primární vstup pro postupy výběru a převýběru buňky.
- Kritický pro postupy RRM v připojeném režimu, jako je předání spojení a adaptace spojení.
- Hlášen UE síti prostřednictvím zpráv RRC Measurement Report.
- Poskytuje metriku podobnou SINR, která indikuje kvalitu kanálu za přítomnosti rušení.

## Související pojmy

- [NRSRP – Narrowband Reference Signal Received Power](/mobilnisite/slovnik/nrsrp/)
- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)

## Definující specifikace

- **TS 32.857** (Rel-15) — Management of LTE IoT RAN Features
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [NRSRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrsrq/)
