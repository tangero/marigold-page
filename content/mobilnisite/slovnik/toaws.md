---
slug: "toaws"
url: "/mobilnisite/slovnik/toaws/"
type: "slovnik"
title: "TOAWS – Time Of Arrival Window Startpoint"
date: 2025-01-01
abbr: "TOAWS"
fullName: "Time Of Arrival Window Startpoint"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/toaws/"
summary: "Time Of Arrival Window Startpoint (TOAWS, počáteční bod časového okna příchodu) definuje počáteční hranici časového okna používaného k vyhledání uplinkového signálu konkrétního uživatelského zařízení"
---

TOAWS je parametr, který definuje počáteční hranici časového okna, ve kterém jednotka pro měření polohy (LMU) vyhledává uplinkový signál konkrétního uživatelského zařízení, aby umožnila určení polohy metodou Uplink TDOA.

## Popis

Time Of Arrival Window Startpoint (TOAWS, počáteční bod časového okna příchodu) je síťově řízený časovací parametr klíčový pro fungování určování polohy metodou Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)). Určuje nejčasnější okamžik, ve kterém by jednotka pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)) měla začít vyhledávat uplinkový přenos cílového uživatelského zařízení (UE). Společně s parametrem Time Of Arrival Window Endpoint ([TOAWE](/mobilnisite/slovnik/toawe/), koncový bod časového okna příchodu) vytváří TOAWS ohraničený časový 'průzor', který zaměřuje úsilí LMU v oblasti zpracování signálu. Uzlový bod pro určování polohy vypočítá očekávaný čas příchodu na základě přibližně známých poloh UE a LMU. TOAWS je nastaven na čas těsně před tuto očekávanou hodnotu, aby zohlednil zápornou chybu v počátečním odhadu polohy a nejistoty šíření signálu.

V praxi, když uzlový bod pro určování polohy ([E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, [LMF](/mobilnisite/slovnik/lmf/) v 5G) vyžádá měření UTDOA, odešle příslušným LMU příkaz. Tento příkaz obsahuje parametry identifikující cílové UE (např. jeho dočasný identifikátor buňkové rádiové sítě - [C-RNTI](/mobilnisite/slovnik/c-rnti/) a plánovací informace) a kritické parametry okna: TOAWS a TOAWE. Po přijetí LMU nakonfiguruje svůj procesor digitálního signálu tak, aby přesně v čase určeném TOAWS začal korelovat přijímaný širokopásmový rádiový signál s očekávaným profilem uplinkového signálu UE (jako je Sounding Reference Signal nebo demodulační referenční signály kanálu Physical Uplink Shared Channel). Korelační proces pokračuje, dokud není dosaženo času TOAWE.

Tento mechanismus je zásadní pro výkon. Tím, že vyhledávání začíná na vypočítaném TOAWS, se LMU vyhne zpracování irelevantních dřívějších časových segmentů, čímž šetří výpočetní zdroje a snižuje celkovou dobu potřebnou k získání platného měření [TOA](/mobilnisite/slovnik/toa/). Přesnost nastavení TOAWS přímo ovlivňuje pravděpodobnost detekce; pokud je nastaven příliš pozdě, skutečný příchod signálu může být zmeškán. Proto uzlový bod pro určování polohy využívá parametry kvality služby a odhady nejistot k dynamickému přizpůsobení počátečního bodu okna pro každý požadavek na měření, čímž zajišťuje robustní provoz napříč různými síťovými geometriemi a rychlostmi UE.

## K čemu slouží

TOAWS byl vyvinut, aby umožnil praktické a efektivní vyhledávání uplinkového signálu v víceuživatelském širokopásmovém buněčném prostředí. Jádrem problému, který řeší, je problém neohraničeného vyhledávání. [LMU](/mobilnisite/slovnik/lmu/) přijímající signály z celého sektoru buňky musí izolovat přenos jednoho konkrétního UE. Bez naváděcího počátečního bodu by přijímač musel provádět nepřetržitou, plně časovou korelaci, což je pro služby určování polohy v reálném čase nepřijatelně složité a pomalé, zejména při obsluze více souběžných požadavků na určení polohy.

Jeho vytvoření bylo motivováno potřebou učinit síťové, na UE nezávislé určování polohy proveditelným pro splnění přísných požadavků na přesnost lokalizace nouzových volání. Metody založené na downlinku vyžadují spolupráci a schopnosti ze strany UE, ale UTDOA (používající TOAWS/TOAWE) umožňuje síti lokalizovat jakékoli zařízení, které vysílá, včetně jednoduchých IoT senzorů a starších telefonů. Parametr TOAWS poskytuje nezbytné 'iniciační' informace pro zahájení cíleného vyhledávání, čímž transformuje neřešitelný kontinuální úkol na zvládnutelný, ohraničený úkol.

TOAWS navíc podporuje optimalizaci síťových zdrojů. Přesným řízením okamžiku, kdy LMU začne své zpracování pro konkrétní úkol, může síť lépe plánovat a multiplexovat požadavky na měření napříč fondem LMU, čímž zlepšuje celkovou kapacitu systému určování polohy. To umožňuje, aby jedna LMU obsluhovala mnoho buněk a četné požadavky na určení polohy, aniž by byla přetížena zpracovatelskou zátěží.

## Klíčové vlastnosti

- Definuje počáteční hranici časového vyhledávacího okna pro detekci uplinkového signálu
- Kritický parametr pro zahájení korelačního procesu v LMU pro UTDOA
- Dynamicky vypočítáván uzlovým bodem pro určování polohy na základě odhadované polohy UE
- Signalizován z uzlového bodu pro určování polohy (E-SMLC/LMF) do LMU prostřednictvím řídicích protokolů
- Zajišťuje, že LMU neplýtvá zpracovatelskými zdroji na irelevantní časová období
- Přímo ovlivňuje pravděpodobnost detekce a latenci určení polohy metodou UTDOA

## Související pojmy

- [TOAWE – Time Of Arrival Window Endpoint](/mobilnisite/slovnik/toawe/)
- [UTDOA – Uplink Time Difference of Arrival](/mobilnisite/slovnik/utdoa/)
- [LMU – Location Measurement Unit](/mobilnisite/slovnik/lmu/)

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms

---

📖 **Anglický originál a plná specifikace:** [TOAWS na 3GPP Explorer](https://3gpp-explorer.com/glossary/toaws/)
