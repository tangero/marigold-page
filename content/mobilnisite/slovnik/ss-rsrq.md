---
slug: "ss-rsrq"
url: "/mobilnisite/slovnik/ss-rsrq/"
type: "slovnik"
title: "SS-RSRQ – Synchronization Signal Reference Signal Received Quality"
date: 2025-01-01
abbr: "SS-RSRQ"
fullName: "Synchronization Signal Reference Signal Received Quality"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ss-rsrq/"
summary: "SS-RSRQ je měření v 5G NR, které udává kvalitu přijímaného synchronizačního signálu. Vypočítává se jako poměr SS-RSRP k celkové spektrální hustotě přijímaného výkonu. Poskytuje ukazatel signálu vůči š"
---

SS-RSRQ je měření rádiového signálu v 5G NR, které udává kvalitu synchronizačního signálu. Vypočítává se jako poměr SS-RSRP k celkovému přijímanému výkonu a poskytuje metrika signálu vůči šumu a interferenci pro převýběr buňky a předávání spojení.

## Popis

SS-RSRQ (Synchronization Signal Reference Signal Received Quality) je odvozené měření pro správu rádiových prostředků v 5G NR, které kvantifikuje kvalitu přijímaného bloku synchronizačního signálu. Je definováno jako poměr N * [SS-RSRP](/mobilnisite/slovnik/ss-rsrp/) / (NR carrier [RSSI](/mobilnisite/slovnik/rssi/)), kde N je počet zdrojových bloků ([RB](/mobilnisite/slovnik/rb/)) šířky pásma měření indikátoru síly přijímaného signálu (RSSI) nosné NR. RSSI představuje celkový širokopásmový přijímaný výkon v určené šířce měřicího pásma, včetně signálů obslužných i neobslužných buněk na stejném kanálu, interference z přilehlých kanálů a tepelného šumu. SS-RSRQ tedy poskytuje míru toho, jak výrazně se výkon požadovaného [SS](/mobilnisite/slovnik/ss/) signálu (SS-RSRP) vyčleňuje z celkové interference a šumu v kanálu.

Z architektonického hlediska probíhá výpočet SS-RSRQ ve fyzické vrstvě UE a funkcích správy rádiových prostředků vrstvy 3. UE nejprve změří SS-RSRP pro konkrétní SSB, jak je popsáno v jeho vlastní definici. Současně nebo v konfigurovaném měřicím období UE změří celkové RSSI ve stejné šířce pásma nosné, která byla použita pro měření SS-RSRP. Měření RSSI zahrnuje vzorkování celkového výkonu v celé konfigurované šířce měřicího pásma. Poměr je následně vypočítán, typicky vedoucí k záporné hodnotě v dB, protože SS-RSRP (část celkového výkonu) je děleno celkovým RSSI. Tato vypočtená hodnota SS-RSRQ je filtrována, aby se vyhladily krátkodobé fluktuace.

Role SS-RSRQ v síti je doplňková k SS-RSRP. Zatímco SS-RSRP udává absolutní sílu signálu, SS-RSRQ udává jeho 'čistotu' neboli kvalitu. To je obzvláště důležité v hustých síťových nasazeních, jako jsou městské makro buňky nebo vnitřní small buňky, kde může být interference ze sousedních buněk významná. Během převýběru buňky v idle módu používá UE kritéria, která mohou zahrnovat jak SS-RSRP, tak SS-RSRQ (parametry jako Qqualmeas a Qqualmin), aby vybrala nejlepší buňku, nikoli pouze nejsilnější. Pro mobilitu v connected módu může síť nakonfigurovat události předání spojení (např. událost A5), které se spouštějí na základě prahových hodnot SS-RSRQ, což umožňuje předání spojení z buňky s přijatelnou silou signálu, ale špatnou kvalitou (vysoká interference), do buňky s lepší kvalitou. Jde o klíčový vstup pro algoritmy vyvažování zátěže a koordinace interference prováděné RAN.

## K čemu slouží

SS-RSRQ bylo zavedeno ve 3GPP Release 15 spolu se [SS-RSRP](/mobilnisite/slovnik/ss-rsrp/), aby poskytlo standardizovanou míru kvality signálu v 5G NR. V LTE plnil podobný účel [RSRQ](/mobilnisite/slovnik/rsrq/), vypočítávaný jako N * [RSRP](/mobilnisite/slovnik/rsrp/) / ([E-UTRA](/mobilnisite/slovnik/e-utra/) carrier RSSI). Motivací pro definici RSRQ založeného na SS v NR byl stejný architektonický posun, který motivoval SS-RSRP: odklon od vždy zapnutého CRS. Protože primárními signály pro počáteční přístup a mobilitu se staly periodicky vysílané SSB, muselo být i měření kvality založeno na těchto signálech, aby byla zachována konzistence a přesnost.

SS-RSRQ řeší kritický problém hodnocení interference v celulárních sítích. Buňka může mít silné SS-RSRP, ale pokud je okolní interference (z jiných buněk nebo šum) také velmi vysoká, může být skutečná kvalita komunikačního spojení špatná, což vede k nízké propustnosti a vysoké chybovosti. Spoléhání se pouze na sílu signálu (SS-RSRP) při rozhodování o mobilitě může způsobit, že se UE připojí k nebo předá spojení do silně interferované buňky. SS-RSRQ poskytuje potřebný další rozměr pro inteligentnější rozhodování. Řeší omezení pouhé metriky výkonu tím, že zahrnuje úroveň interference a šumu, což umožňuje síti a UE rozlišit mezi skutečně dobrou buňkou a buňkou silnou, ale přetíženou. To je obzvláště klíčové pro úspěch 5G sítí, které cílí na ultra-hustá nasazení a vysokou spektrální účinnost, kde je správa interference prvořadá.

## Klíčové vlastnosti

- Odvozená metrika vypočítávaná jako (N * SS-RSRP) / NR carrier RSSI
- Poskytuje ukazatel kvality signálu zohledňující interferenci a šum
- Používá se při hodnocení buněk pro převýběr (S-kritérium) spolu s SS-RSRP
- Lze konfigurovat jako spouštěč událostí předání spojení ve stavu RRC_CONNECTED
- Nezbytné pro strategie vyvažování zátěže sítě a zmírňování interference
- Šířka pásma pro měření RSSI je konfigurovatelná sítí

## Související pojmy

- [SS-RSRP – Synchronization Signal based Reference Signal Received Power](/mobilnisite/slovnik/ss-rsrp/)
- [SS-SINR – SS Signal-to-Interference-plus-Noise Ratio](/mobilnisite/slovnik/ss-sinr/)
- [RSSI – Received Signal Strength Indication](/mobilnisite/slovnik/rssi/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement

---

📖 **Anglický originál a plná specifikace:** [SS-RSRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss-rsrq/)
