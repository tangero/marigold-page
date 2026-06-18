---
slug: "ss-rsrp"
url: "/mobilnisite/slovnik/ss-rsrp/"
type: "slovnik"
title: "SS-RSRP – Synchronization Signal based Reference Signal Received Power"
date: 2025-01-01
abbr: "SS-RSRP"
fullName: "Synchronization Signal based Reference Signal Received Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ss-rsrp/"
summary: "SS-RSRP je klíčové měření na fyzické vrstvě v 5G NR, které kvantifikuje úroveň přijímaného výkonu bloku synchronizačního signálu (SS) od buňky. Používá se v UE pro rozhodování o výběru buňky, převýběr"
---

SS-RSRP je měření v 5G NR, které kvantifikuje úroveň přijímaného výkonu bloku synchronizačního signálu buňky. Používá se v UE pro rozhodování o výběru buňky, převýběru buňky a předávání hovoru.

## Popis

SS-RSRP (Synchronization Signal based Reference Signal Received Power) je základní měření pro správu rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) definované ve standardech 3GPP New Radio (NR). Jedná se o lineární průměr výkonových příspěvků (ve wattech) prvků zdroje, které nesou sekundární synchronizační signály ([SSS](/mobilnisite/slovnik/sss/)) v rámci bloku synchronizačního signálu/fyzického vysílacího kanálu ([SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/)), běžně známého jako SSB. Měření provádí uživatelské zařízení (UE) na signálech v downlinku vysílaných gNodeB. SSB je klíčová signálová struktura, kterou buňka periodicky vysílá a která obsahuje primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)), sekundární synchronizační signál (SSS) a fyzický vysílací kanál (PBCH). Měření SS-RSRP se konkrétně zaměřuje na SSS, protože ten poskytuje stabilní a buňce specifický referenční bod. UE měří výkon těchto specifických prvků zdroje po provedení nezbytných procedur synchronizace a odhadu kanálu.

Architektura podporující SS-RSRP zahrnuje řetězec zpracování fyzické vrstvy v UE. Při zapnutí nebo během událostí mobility UE prohledává různé kmitočtová pásma a směry paprsků, aby našla SSB. Jakmile je SSB detekován a získáno jeho časování, UE izoluje prvky zdroje odpovídající SSS v rámci tohoto SSB. Výkon těchto [RE](/mobilnisite/slovnik/re/) se změří, typicky za použití filtrování pro vyhlazení rychlého úniku a vlivů rušení, což vede ke stabilní hodnotě [RSRP](/mobilnisite/slovnik/rsrp/) hlášené v dBm. Toto měření je pak nahlášeno vyšším vrstvám (vrstva 3) protokolového zásobníku UE a může být dále hlášeno síti prostřednictvím hlášení o měření (např. ve stavech [RRC](/mobilnisite/slovnik/rrc/)_IDLE, RRC_INACTIVE nebo RRC_CONNECTED) pro podporu rozhodování sítě.

SS-RSRP hraje ústřední roli v několika síťových funkcích. Je primární metrikou pro procedury výběru a převýběru buňky, kde UE porovnává SS-RSRP obsluhující buňky a sousedních buněk s předdefinovanými prahy (např. Squal, Srxlev). Pro předávání hovoru a správu paprsků se měření SS-RSRP různých SSB (které odpovídají různým paprskům v pásmu FR2) používají k určení nejlepší buňky nebo paprsku pro připojení. Síť konfiguruje měřicí objekty, konfigurace hlášení a spouštěcí události (jako události A3, A5) na základě SS-RSRP. Jeho přesnost a spolehlivost jsou prvořadé, protože chyby mohou vést k ping-pong předávání hovoru, přerušením hovoru nebo suboptimálnímu připojení k buňce, což přímo ovlivňuje uživatelský zážitek a výkon sítě.

## K čemu slouží

SS-RSRP bylo zavedeno ve 3GPP Release 15 jako součást standardizace 5G NR, aby poskytlo standardizovanou a přesnou metodu pro měření síly signálu v downlinku ze synchronizačních signálů. V předchozích generacích, jako je LTE, se RSRP měřilo na základě buňce specifických referenčních signálů (CRS). 5G NR však zavedlo flexibilnější a na paprsky orientovaný design, kde byl neustále vysílaný CRS odstraněn za účelem úspory režie a energie. Blok SS/PBCH se stal primárním signálem pro počáteční přístup a mobilitu. Bylo tedy nutné nové měření analogické RSRP, ale založené na bloku SS. SS-RSRP řeší problém poskytování konzistentní reference pro výkon signálu v síti, kde nejsou referenční signály vysílány nepřetržitě.

Vytvoření SS-RSRP bylo motivováno potřebou podporovat efektivní mobilitu v různých scénářích nasazení 5G, včetně vysokofrekvenčních pásem (mmWave) s formováním paprsků. V těchto scénářích se kvalita signálu může výrazně lišit mezi různými paprsky. Měření SS-RSRP na jednotlivé SSB (paprsky) umožňuje UE a síti identifikovat nejsilnější paprsek pro komunikaci. Řeší omezení RSRP založeného na CRS z LTE, které nebylo vhodné pro přerušované, paprskově přepínané vysílání SSB v NR. Definováním měření konkrétně na SSS zajišťuje buňce specifický a stabilní odhad výkonu, který je oddělen od možných výkyvů výkonu v jiných kanálech, což umožňuje spolehlivé monitorování rádiového spoje a rozhodování o mobilitě v ekosystému 5G.

## Klíčové vlastnosti

- Měření založené na sekundárním synchronizačním signálu (SSS) v rámci bloku SS/PBCH
- Hlášeno v dBm jako lineární průměr výkonových příspěvků
- Základní pro procedury výběru buňky, převýběru buňky a předávání hovoru v NR
- Podporuje správu paprsků tím, že poskytuje měření na jednotlivé SSB (na jednotlivé paprsky) v pásmu FR2
- Konfigurovatelné sítí prostřednictvím signalizace RRC pro měřicí mezery a kritéria hlášení
- Používá se spolu s dalšími měřeními, jako je SS-RSRQ a SS-SINR, pro komplexní hodnocení spoje

## Související pojmy

- [SS-RSRQ – Synchronization Signal Reference Signal Received Quality](/mobilnisite/slovnik/ss-rsrq/)
- [SS-SINR – SS Signal-to-Interference-plus-Noise Ratio](/mobilnisite/slovnik/ss-sinr/)
- [RRM – Radio Resource Management](/mobilnisite/slovnik/rrm/)

## Definující specifikace

- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [SS-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss-rsrp/)
