---
slug: "tpmi"
url: "/mobilnisite/slovnik/tpmi/"
type: "slovnik"
title: "TPMI – Transmitted Precoding Matrix Indicator"
date: 2025-01-01
abbr: "TPMI"
fullName: "Transmitted Precoding Matrix Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tpmi/"
summary: "Index signalizovaný gNB směrem k UE v 5G NR (a eNB v LTE), který označuje konkrétní prekódovací matici aplikovanou na downlinkový přenos dat. Je klíčovou součástí MIMO se zpětnou vazbou, která umožňuj"
---

TPMI je index signalizovaný sítí zařízení, který označuje konkrétní prekódovací matici aplikovanou na downlinkový přenos, což umožňuje správnou demodulaci v MIMO se zpětnou vazbou.

## Popis

Transmitted Precoding Matrix Indicator (TPMI) je kritický prvek řídicí informace pro downlink v [MIMO](/mobilnisite/slovnik/mimo/) operacích LTE a 5G NR. Je přenášen ze sítě ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) k uživatelskému zařízení (UE) jako součást Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). Hodnota TPMI je index, který odkazuje na konkrétní prekódovací matici nebo vektor v rámci předem definovaného kodebooku známého vysílači i přijímači. Tento kodebook obsahuje sadu možných lineárních transformací (matic), které lze aplikovat na mapování vrstev na porty pro vysílací beamforming a prostorové multiplexování. Když síť naplánuje downlinkový přenos pro UE, vybere prekódovací matici na základě zpětné vazby UE o stavu kanálu (Channel State Information, [CSI](/mobilnisite/slovnik/csi/)) (která obsahuje doporučení Precoding Matrix Indicator, [PMI](/mobilnisite/slovnik/pmi/)) a dalších plánovacích algoritmů. Index aplikované matice je pak sdělen prostřednictvím TPMI.

Po přijetí DCI obsahujícího TPMI použije UE tento index k vyhledání odpovídající prekódovací matice W ve svém lokálním kodebooku. UE pak tuto znalost aplikuje ve svém přijímacím řetězci. Konkrétně použije matici W k vytvoření hypotéz o efektivním kanálu pozorovaném na přijímači, což je součin skutečného fyzického MIMO kanálu H a prekódovací matice W (tj. H_eff = H * W). To umožňuje UE provést přesný odhad kanálu pro demodulační referenční signály ([DM-RS](/mobilnisite/slovnik/dm-rs/) v NR, UE-RS v LTE), které jsou prekódovány stejnou maticí jako data. Následně může UE koherentně demodulovat data na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)). TPMI je nezbytný pro prostorové multiplexování se zpětnou vazbou, zejména pro prekódování založené na kodebooku, protože odstraňuje jakoukoli nejednoznačnost mezi tím, co UE doporučilo (prostřednictvím PMI), a tím, co gNB skutečně vyslalo.

Z hlediska architektury je TPMI součástí dynamické smyčky adaptace spoje zajišťované fyzickou vrstvou. Proces zahrnuje: 1) UE změří downlinkový kanál a nahlásí doporučené PMI a Rank Indicator (RI) přes PUCCH nebo PUSCH. 2) Plánovač gNB zváží toto doporučení spolu s víceuživatelským rušením a vytížením provozu, aby vybral finální prekódovací matici a řád přenosu. 3) gNB signalizuje zvolenou matici prostřednictvím TPMI (a řád přenosu) v DCI. 4) UE dekóduje DCI, získá TPMI a podle toho nakonfiguruje svůj přijímač. Tento mechanismus umožňuje rychlou adaptaci prekódovací strategie na úrovni subrámce tak, aby odpovídala časově proměnným podmínkám kanálu, maximalizuje propustnost a spolehlivost. V 5G NR se signalizace TPMI používá také pro uplinkový přenos založený na kodebooku, kde gNB instruuje UE, kterou prekódovací matici má použít pro svůj přenos na PUSCH, což ukazuje její obousměrnou roli.

## K čemu slouží

TPMI byl zaveden, aby umožnil efektivní a jednoznačnou implementaci prekódování se zpětnou vazbou založeného na kodebooku pro MIMO v LTE (od Release 8 dále) a později byl přenesen do 5G NR. Před standardizovaným MIMO se zpětnou vazbou systémy spoléhaly na otevřenou smyčku diverzity nebo vyžadovaly složité techniky slepé detekce na přijímači, aby určily aplikované prekódování. Primární problém, který TPMI řeší, je signalizace volby prekódování vysílače směrem k přijímači s nízkou režií. Bez tohoto explicitního indikátoru by UE neznalo přesný prostorový filtr aplikovaný na jeho data, což by vedlo k výraznému zhoršení výkonu při demodulaci, protože efektivní kanál by byl neznámý.

Jeho vytvoření bylo motivováno snahou dosáhnout vyšší spektrální účinnosti prostřednictvím víceanténních technik. Tím, že síť může informovat UE o přesné prekódovací matici, může UE provádět optimální zpracování na přijímači, jako je detekce Minimum Mean Square Error (MMSE) nebo Maximum Likelihood (ML), přizpůsobené efektivnímu kanálu. To maximalizuje poměr signálu k šumu a rušení (SINR) na vrstvu. TPMI spolu se zpětnou vazbou PMI tvoří těsnou zpětnovazební smyčku, která přizpůsobuje beamformingový diagram aktuálnímu stavu kanálu, zaměřuje energii na zamýšlené UE a minimalizuje rušení ostatním. To je zásadní pro dosažení zisků kapacity slibovaných technologií MIMO. V 5G NR se jeho účel rozšířil na podporu flexibilnějších anténních konfigurací, massive MIMO a uplinkového MIMO, což odráží vývoj směrem k dynamičtějšímu a konfigurovatelnějšímu prostorovému zpracování.

## Klíčové vlastnosti

- Index signalizující aplikovanou prekódovací matici ze standardizovaného kodebooku
- Přenášen v rámci Downlink Control Information (DCI) na PDCCH
- Umožňuje koherentní demodulaci prekódovaného PDSCH definováním efektivního kanálu
- Funguje v součinnosti se zpětnou vazbou CSI (PMI/RI) od UE
- Podporuje dynamickou adaptaci prekódovací strategie na úrovni subrámce
- Používá se pro prekódování založené na kodebooku jak pro downlink, tak pro uplink (v NR)

## Související pojmy

- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [TPMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpmi/)
