---
slug: "sfo"
url: "/mobilnisite/slovnik/sfo/"
type: "slovnik"
title: "SFO – Sampling Frequency Offset"
date: 2026-01-01
abbr: "SFO"
fullName: "Sampling Frequency Offset"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sfo/"
summary: "Chyba časového posunu mezi vysílačem a přijímačem způsobená nesouladem vzorkovacích kmitočtů hodin analogově-digitálních/digitálně-analogových převodníků. Vede k akumulované fázové rotaci, intersymbol"
---

SFO je chyba časového posunu mezi vysílačem a přijímačem způsobená nesouladem jejich vzorkovacích kmitočtů, což vede k fázové rotaci a zhoršení výkonu, není-li kompenzována.

## Popis

Sampling Frequency Offset (SFO) je kritická porucha v přijímačích digitální komunikace, včetně buněčných systémů 3GPP. Vzniká, když vzorkovací kmitočet hodin v analogově-digitálním převodníku ([ADC](/mobilnisite/slovnik/adc/)) přijímače není dokonale synchronizován se vzorkovacím kmitočtem hodin (a tedy i s rychlostí symbolů) v digitálně-analogovém převodníku ([DAC](/mobilnisite/slovnik/dac/)) vysílače. Tento nesoulad, často způsobený nepřesnostmi a driftem krystalového oscilátoru, vede k tomu, že přijímač vzorkuje přicházející průběh spojitého času v mírně nesprávných okamžicích. Hlavním účinkem je časově proměnná chyba časování, která se lineárně akumuluje v čase. V diskrétně-časovém základně-pásmovém modelu se SFO projevuje jako progresivní fázová rotace napříč podnosnými v systémech s ortogonálním frekvenčním multiplexem ([OFDM](/mobilnisite/slovnik/ofdm/)), jako jsou LTE a NR. Fázová rotace pro danou podnosnou je úměrná indexu podnosné a akumulovanému vzorkovacímu posunu. Není-li korigována, ničí ortogonalitu mezi podnosnými, což vede k mezikanálovému rušení ([ICI](/mobilnisite/slovnik/ici/)). V časové oblasti způsobuje pomalý drift optimálního vzorkovacího okamžiku, který se může posunout do sousedních symbolů a způsobit intersymbolové rušení ([ISI](/mobilnisite/slovnik/isi/)). Algoritmy přijímače musí SFO průběžně odhadovat a korigovat. To se často provádí pomocí známých referenčních signálů (např. Cell-Specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Phase-Tracking Reference Signals ([PT-RS](/mobilnisite/slovnik/pt-rs/)) v NR). Odhad typicky zahrnuje měření fázového rozdílu referenčního signálu mezi dvěma OFDM symboly. Zjištěná chyba je vložena do řídicí smyčky časování (např. digitální PLL), která upravuje vzorkovací hodiny ADC pomocí napětím řízeného oscilátoru ([VCO](/mobilnisite/slovnik/vco/)) nebo, častěji v softwarově definovaných rádiích, aplikuje na vzorkovaný signál digitální převzorkovací/interpolační filtr pro korekci časového driftu. Kompenzace je klíčová pro udržení nízké blokové chybovosti (BLER), zejména u modulací vyššího řádu (např. 256QAM, 1024QAM) a širokých šířek pásma.

## K čemu slouží

Mechanismy pro odhad a kompenzaci SFO byly formálně specifikovány ve 3GPP Release 19 pro NR, aby vyhověly přísným požadavkům na výkon pokročilých nasazení 5G. Přestože se vždy jednalo o praktický problém přijímače, jeho explicitní ošetření ve specifikacích, jako jsou 38.191 (User Equipment (UE) radio transmission and reception) a 38.194 (Base Station (BS) radio transmission and reception), bylo motivováno několika faktory. Použití vyšších kmitočtových pásem (mmWave) se širšími kanálovými šířkami pásma (až 400 MHz) činí systém citlivějším na časové chyby; malá chyba hodin v ppm má za následek větší absolutní kmitočtový drift. Nasazení nízkonákladových IoT zařízení a zařízení se sníženou kapacitou (RedCap) s méně stabilními lokálními oscilátory zvyšuje pravděpodobnost významného SFO. Dále pokročilé funkce jako Integrated Access and Backhaul (IAB) a opakovače, specifikované v 38.769, zahrnují kaskádované uzly, kde se mohou chyby vzorkovacích hodin šířit a akumulovat. Bez robustního zvládání SFO by tyto faktory zhoršily propustnost, zvýšily latenci a snížily pokrytí. Standardizace zajišťuje konzistentní výkonnostní měřítka pro základnové stanice a UE, což umožňuje interoperabilitu i se součástmi s různou přesností hodin. Řeší omezení dřívějších systémů, kde byla korekce SFO z velké části otázkou implementace, tím, že poskytuje standardizovaný rámec pro požadavky a testovací postupy.

## Klíčové vlastnosti

- Způsobeno nesouladem vzorkovacího kmitočtu hodin mezi vysílačem a přijímačem
- Vede k akumulující se chybě časování a rotaci fáze závislé na podnosné v OFDM
- Způsobuje mezikanálové rušení (ICI) a intersymbolové rušení (ISI), není-li korigováno
- Odhadováno pomocí referenčních signálů (např. PT-RS v NR) prostřednictvím měření fázového rozdílu
- Kompenzováno pomocí řídicích smyček časování nebo digitálních převzorkovacích filtrů
- Kritické pro výkon v širokopásmových mmWave a při nasazeních s nízkonákladovými oscilátory

## Související pojmy

- [CFO – Carrier Frequency Offset](/mobilnisite/slovnik/cfo/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [PT-RS – Phase Tracking Reference Signal](/mobilnisite/slovnik/pt-rs/)

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [SFO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfo/)
