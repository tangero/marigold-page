---
slug: "agi"
url: "/mobilnisite/slovnik/agi/"
type: "slovnik"
title: "AGI – Antenna Gain Imbalance"
date: 2025-01-01
abbr: "AGI"
fullName: "Antenna Gain Imbalance"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/agi/"
summary: "Antenna Gain Imbalance (AGI) označuje rozdíl ve zisku mezi více anténami v rádiovém systému, zejména v konfiguracích s diverzitním příjmem nebo MIMO. Jde o kritický parametr ovlivňující výkon systému,"
---

AGI (Antenna Gain Imbalance) je rozdíl ve zisku mezi více anténami v rádiovém systému, což je klíčový parametr pro výkon při diverzitním příjmu, MIMO a beamforming.

## Popis

Antenna Gain Imbalance (AGI) je základní parametr v technice vysokých kmitočtů, který kvantifikuje rozdíl ve zisku mezi více anténami v rámci rádiového systému. V praktických nasazeních vykazují i antény stejného modelu a specifikace mírné odchylky ve zisku kvůli výrobním tolerancím, rozdílům v instalaci, vlivům prostředí a stárnutí komponent. AGI konkrétně měří tyto odchylky v decibelech (dB) a představuje maximální přípustný rozdíl mezi anténami s nejvyšším a nejnižším ziskem v konfiguraci s více anténami.

V systémech s diverzitním příjmem, které jsou základem moderních mobilních sítí, AGI přímo ovlivňuje účinnost kombinování signálů z více antén. Když mají antény výrazně odlišné zisky, může být slabší signálová cesta dominována šumem spíše než aby přispívala užitečnou signálovou energií, což snižuje zisk z diverzity, který by měl být teoreticky dosažen. Tato nerovnováha ovlivňuje jak přijímací, tak vysílací cesty, ačkoli je obvykle kritičtější na straně příjmu, kde jsou úrovně signálu nižší a šum má větší dopad. Nerovnováha se projevuje jako snížení efektivního poměru signál-šum (SNR) a může způsobit nesprávné vážení v algoritmech pro kombinování signálů.

Pro systémy Multiple Input Multiple Output ([MIMO](/mobilnisite/slovnik/mimo/)), které tvoří páteř technologií 4G LTE a 5G NR, má AGI ještě hlubší důsledky. MIMO spoléhá na techniky prostorového multiplexování a beamforming, které předpokládají relativně vyvážené charakteristiky antén. Významné nerovnováhy ve zisku mezi anténními prvky narušují kanálovou matici, snižují ortogonalitu mezi prostorovými proudy a zvyšují interferenci mezi proudy. Tato degradace přímo vede ke snížení propustnosti, nižší spektrální účinnosti a narušení spolehlivosti spoje. V aplikacích beamforming způsobuje AGI zkreslení vyzařovacího diagramu, zvýšení úrovní bočních laloků a chyby směrování, které snižují účinnost směrového vysílání.

Specifikace 3GPP řeší AGI prostřednictvím standardizovaných požadavků a testovacích postupů. Tyto specifikace definují maximální přípustné hodnoty AGI pro různé scénáře nasazení, čímž zajišťují interoperabilitu mezi zařízeními od různých dodavatelů. Operátoři sítí typicky implementují monitorování AGI prostřednictvím periodických měření během údržbových oken nebo vestavěných testovacích schopností moderních rádiových zařízení. Kompenzační techniky zahrnují postupy kalibrace antén, digitální úpravu zisku v základnovém pásmu a adaptivní algoritmy, které zohledňují naměřené nerovnováhy ve zpracovatelských řetězcích signálu. Správa AGI je obzvláště kritická v nasazeních massive MIMO s velkými anténními poli, kde se malé nerovnováhy na jednotlivých prvcích mohou kumulovat do významného snížení výkonu na systémové úrovni.

## K čemu slouží

Koncept Antenna Gain Imbalance existuje proto, aby řešil praktickou realitu, že dokonalé sladění antén je v reálných nasazeních nemožné. V ideálních teoretických modelech se předpokládá, že více antén v systému má identické charakteristiky, ale výrobní odchylky, rozdíly v instalaci a faktory prostředí vytvářejí nevyhnutelné nerovnováhy. Bez kvantifikace a správy těchto nerovnováh by výkon rádiového systému výrazně zaostával za teoretickými předpověďmi, což by vedlo k nespolehlivému výkonu sítě a nespokojeným uživatelům.

Historicky, jak se mobilní sítě vyvíjely od systémů s jednou anténou k diverzitnímu příjmu a následně k technologiím [MIMO](/mobilnisite/slovnik/mimo/), se dopad anténních nerovnováh stával stále kritičtějším. Rané mobilní systémy mohly tolerovat relativně velké AGI, protože používaly jednodušší modulační schémata a nižší datové rychlosti. S zavedením modulací vyššího řádu (jako 64-QAM a 256-QAM v LTE a 5G) a technik prostorového multiplexování se však citlivost na nerovnováhy ve zisku dramaticky zvýšila. Průmysl potřeboval standardizované přístupy k specifikaci, měření a kompenzaci AGI, aby zajistil, že pokročilé rádiové technologie mohou poskytnout své slibované výkonnostní výhody v praktických nasazeních.

Specifikace AGI řeší několik klíčových problémů: zajišťují interoperabilitu mezi síťovým zařízením od různých dodavatelů, poskytují jasné požadavky pro výrobce antén, umožňují přesné předpovědi systémového výkonu a stanovují metodiky testování pro nasazení a údržbu sítě. Definováním přijatelných limitů AGI pomáhají standardy 3GPP operátorům sítí vyvážit požadavky na výkon s praktickými omezeními nasazení a nákladovými hledisky. To je obzvláště důležité pro systémy massive MIMO v 5G, kde desítky nebo stovky anténních prvků musí spolupracovat koherentně, aby dosáhly slibovaného zlepšení kapacity a pokrytí.

## Klíčové vlastnosti

- Kvantifikuje rozdíly ve zisku mezi více anténami v rádiovém systému
- Měří se v decibelech (dB) jako maximální přípustná odchylka
- Kritický parametr pro výkon systému s diverzitním příjmem
- Přímo ovlivňuje účinnost prostorového multiplexování a beamforming v MIMO
- Předmět standardizace 3GPP pro zajištění interoperability
- Vyžaduje monitorování a kompenzaci v moderních rádiových systémech

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [AGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/agi/)
