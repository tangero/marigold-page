---
slug: "tch-afs"
url: "/mobilnisite/slovnik/tch-afs/"
type: "slovnik"
title: "TCH/AFS – Traffic Channel for Adaptive Multi-Rate Full Rate Speech"
date: 2025-01-01
abbr: "TCH/AFS"
fullName: "Traffic Channel for Adaptive Multi-Rate Full Rate Speech"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tch-afs/"
summary: "Kanál pro přenos hovorů v GSM využívající plně rychlostní kodek Adaptive Multi-Rate (AMR). Dynamicky přizpůsobuje rychlosti řečového a kanálového kódování na základě rádiových podmínek, čímž optimaliz"
---

TCH/AFS je kanál pro přenos hovorů v GSM, který využívá plně rychlostní kodek Adaptive Multi-Rate (AMR) k dynamickému přizpůsobení rychlosti řečového a kanálového kódování na základě rádiových podmínek, čímž optimalizuje kvalitu hlasu a odolnost proti chybám.

## Popis

[TCH](/mobilnisite/slovnik/tch/)/[AFS](/mobilnisite/slovnik/afs/) (Traffic Channel employing [AMR](/mobilnisite/slovnik/amr/) Full rate Speech) je logický kanál v GSM, který využívá řečový kodek Adaptive Multi-Rate (AMR) v jeho plně rychlostním režimu. Na rozdíl od kanálu [TCH-FS](/mobilnisite/slovnik/tch-fs/) s pevnou rychlostí obsahuje TCH/AFS zásadní vylepšení: adaptabilitu. Kodek AMR definuje více režimů řečového kódování (např. 12,2; 10,2; 7,95; 7,40; 6,70; 5,90; 5,15; 4,75 kbps) a více schémat kanálového kódování. Kanál TCH/AFS funguje tak, že dynamicky vybírá nejvhodnější kombinaci rychlosti řečových bitů a ochrany kanálovým kódováním na základě měření kvality rádiového spoje v reálném čase. Tento výběr, známý jako Link Adaptation nebo Codec Mode Adaptation, provádí Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)).

Technicky kanál zabírá jeden plný fyzický timeslot v rámci [TDMA](/mobilnisite/slovnik/tdma/), podobně jako TCH-FS. Užitečné zatížení v rámci tohoto timeslotu je však variabilní. Když jsou rádiové podmínky dobré, systém zvolí režim s vysokou rychlostí řečových bitů (jako 12,2 kbps) s méně robustním kanálovým kódováním, čímž maximalizuje kvalitu hlasu. Když se podmínky zhorší (např. nízký signál, vysoký interference), systém přepne do režimu s nižší rychlostí řečových bitů, čímž uvolní bity v rámci stejného hrubého bitového rozpočtu pro použití výkonnějšího Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)). Tím se zvýší odolnost proti chybám a udrží se kontinuita hovoru za cenu mírně nižší zvukové kvality. Tato adaptace může během hovoru probíhat periodicky. Struktura kanálu stále sleduje multiframe a přenáší řečová data a přidruženou signalizaci [SACCH](/mobilnisite/slovnik/sacch/).

Z architektonického hlediska vyžaduje TCH/AFS podporu v mobilní stanici, BTS, BSC a TRAU. BSC funguje jako adaptační kontrolér, který na základě měřicích reportů z mobilní stanice a BTS řídí změny režimu kodeku. TRAU musí být schopné transkódovat mezi různými rychlostmi AMR. Úlohou TCH/AFS je poskytnout lepší uživatelský zážitek a efektivnější provoz sítě ve srovnání s kanály s pevnou rychlostí. Optimalizuje základní kompromis v bezdrátové komunikaci: mezi zdrojovým kódováním (kvalita řeči) a kanálovým kódováním (ochrana proti chybám). Přizpůsobením se podmínkám poskytuje nejlepší možnou kvalitu hlasu, kterou rádiový spoj v daném okamžiku podporuje, snižuje pravděpodobnost přerušení hovoru v oblastech se špatným pokrytím a může dokonce zlepšit celkovou kapacitu sítě tím, že umožní hovorům pokračovat v podmínkách, ve kterých by kanál s pevnou rychlostí selhal.

## K čemu slouží

TCH/AFS byl vytvořen, aby překonal omezení řečových kanálů s pevnou rychlostí (TCH-FS a TCH-HS), které se nemohly přizpůsobovat měnícím se rádiovým podmínkám. Hlavní problém, který řešil, byla povaha dřívějších kodeků typu 'vše nebo nic': při špatných podmínkách by hovor s pevnou plnou rychlostí trpěl vážným zhoršením kvality nebo by spadl, zatímco hovor s pevnou poloviční rychlostí by mohl nabízet špatnou kvalitu, i když byl rádiový spoj výborný. Technologie AMR, a tím i kanál TCH/AFS, do tohoto procesu vnesly inteligenci.

Historickým motivem bylo dosažení vyšší kvality hlasu a robustnosti sítě, jak sítě GSM dospívaly a uživatelé očekávali konzistentnější službu. 3GPP standardizovala AMR, aby poskytla adaptabilní řečový kodek připravený na budoucnost. Implementace kanálu TCH/AFS umožnila nasazení tohoto kodeku v rámci existující struktury GSM kanálů. Řešila klíčové omezení statické alokace zdrojů tím, že učinila hlasovou službu odolnou a citlivou na kvalitu. To bylo zvláště důležité pro zlepšení služby v okrajových částech buněk a v interiérech, což přímo ovlivnilo spokojenost zákazníků a metriky výkonu sítě. Představovalo to posun od síťově orientovaného, fixního plánování zdrojů k více uživatelsky orientovanému, adaptivnímu modelu poskytování hlasových služeb.

## Klíčové vlastnosti

- Využívá řečový kodek Adaptive Multi-Rate (AMR) v plně rychlostní konfiguraci
- Dynamické Link Adaptation mezi více rychlostmi řečového a kanálového kódování
- Optimalizuje kvalitu hlasu za dobrých podmínek a odolnost hovoru za špatných podmínek
- Zabírá jeden fyzický timeslot s adaptivním obsahem užitečného zatížení
- Codec Mode Adaptation je řízen BSC na základě rádiových měření
- Poskytuje zpětnou kompatibilitu a spolupráci s legacy kanály s pevnou rychlostí

## Související pojmy

- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)
- [TCH/AHS – Traffic Channel / Adaptive Multi-Rate Half Rate Speech](/mobilnisite/slovnik/tch-ahs/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [TCH/AFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-afs/)
