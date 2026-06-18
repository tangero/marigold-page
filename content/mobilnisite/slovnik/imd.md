---
slug: "imd"
url: "/mobilnisite/slovnik/imd/"
type: "slovnik"
title: "IMD – Intermodulation Distortion"
date: 2024-01-01
abbr: "IMD"
fullName: "Intermodulation Distortion"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/imd/"
summary: "Intermodulační zkreslení (IMD) je nelineární zkreslení signálu v rádiových vysílačích a přijímačích, při kterém se dva nebo více vysílaných signálů smíchají a vytvoří nežádoucí parazitní signály na no"
---

IMD je nelineární zkreslení signálu v rádiových vysílačích a přijímačích, při kterém se dva nebo více signálů smíchají a vytvoří nežádoucí parazitní signály na nových frekvencích.

## Popis

Intermodulační zkreslení (IMD) je forma nelineárního zkreslení, ke kterému dochází v rádiofrekvenčních ([RF](/mobilnisite/slovnik/rf/)) komponentách, jako jsou výkonové zesilovače ([PA](/mobilnisite/slovnik/pa/)), míchače a přijímače, při současné přítomnosti více signálů. Jde o základní zkreslení na fyzické vrstvě v bezdrátových komunikačních systémech. Když dva nebo více signálů na frekvencích f1 a f2 procházejí nelineárním zařízením, generují kromě původních signálů i nežádoucí parazitní signály na frekvencích, které jsou matematickými kombinacemi původních frekvencí, například 2f1 - f2 a 2f2 - f1 (produkty intermodulace třetího řádu, neboli IM3). Tyto parazitní emise mohou spadat do vlastního přijímacího pásma zařízení nebo do jiných přidělených frekvenčních pásem, čímž způsobují interferenci, která zhoršuje citlivost přijímače a celkový výkon systému.

Mechanismus IMD je zakořeněn v nelineární přenosové charakteristice aktivních RF komponent. Výstupní signál y(t) nelineárního systému lze modelovat jako mocninnou řadu vstupního signálu x(t): y(t) = a1*x(t) + a2*x(t)^2 + a3*x(t)^3 + ... . Lineární člen (a1*x(t)) představuje požadované zesílení. Členy vyšších řádů (a2, a3, ...) generují harmonické a intermodulační produkty. Když je x(t) součtem dvou sinusovek, člen a3*x(t)^3 je primárně zodpovědný za generování produktů intermodulace třetího řádu (IM3), které jsou často nejproblematičtější, protože jsou frekvenčně nejblíže požadovaným signálům a mohou mít značný výkon, pokud je nelinearita výrazná.

Ve specifikacích 3GPP je IMD podrobně charakterizováno a specifikováno prostřednictvím několika klíčových testů. Pro uživatelské zařízení (UE) je kritickým testem požadavek na intermodulaci vysílače UE, definovaný ve specifikacích jako 36.101 a 38.101. Tento test měří výkon nežádoucích IMD produktů generovaných ve vysílači UE při přítomnosti rušivého signálu od jiného UE nebo základnové stanice. UE musí potlačit tyto parazitní emise pod stanovenou masku, aby se zabránilo vzniku interference. Podobně se u základnových stanic (eNodeB/gNB) testují charakteristiky intermodulace přijímače, aby bylo zajištěno, že přijímač snese rušivé signály bez výrazného zhoršení své schopnosti přijímat požadovaný signál. Specifikace definují testovací konfigurace s konkrétními výkony, frekvencemi a typy modulace požadovaného a rušivého signálu, aby byl zajištěn konzistentní a spolehlivý výkon všech kompatibilních zařízení. Řízení IMD je obzvláště náročné u moderních rádiových systémů podporujících agregaci nosných ([CA](/mobilnisite/slovnik/ca/)), kde zařízení současně vysílá nebo přijímá na více komponentních nosných, což samo o sobě vytváří podmínky příznivé pro vznik intermodulace.

## K čemu slouží

IMD existuje jako základní fyzické omezení všech praktických [RF](/mobilnisite/slovnik/rf/) systémů kvůli inherentním nelinearitám elektronických součástek, jako jsou tranzistory používané v zesilovačích. Účelem specifikování požadavků na IMD v 3GPP není vynalézt tento jev, ale kontrolovat jeho dopad, aby byla zajištěna spolehlivá koexistence více rádiových systémů a služeb v přeplněném rádiovém spektru. Bez přísných limitů na parazitní emise generované IMD by vysílač mohl způsobit škodlivou interferenci vlastnímu přijímači (sebeinterference v systémech s duplexním dělením kmitočtů) nebo jiným uživatelům pracujícím v sousedních či dokonce nesousedních kanálech a pásmech.

Problém, který specifikace IMD řeší, je prevence systémové interference v celulárních sítích, což je klíčové pro udržení kapacity sítě, pokrytí a kvality služeb. Jak se sítě vyvíjely k používání širších šířek pásma, agregace nosných a složitějších vícepásmových/více-RAT zařízení, potenciál pro interferenci související s IMD významně vzrostl. Například při agregaci nosných může UE vysílající na dvou uplinkových nosných (např. Pásmo A a Pásmo B) generovat produkty intermodulace třetího řádu, které spadají do downlinkového přijímacího pásma zcela jiného Pásma C, což může potenciálně blokovat vlastní schopnost UE přijímat signály v tomto pásmu. Specifikace 3GPP definují přijatelné limity pro takové emise, aby k tomu nedocházelo.

Historicky, jak se celulární technologie vyvíjela od jednokanálového GSM přes širokopásmové [CDMA](/mobilnisite/slovnik/cdma/) až k [OFDMA](/mobilnisite/slovnik/ofdma/) založenému LTE a 5G NR, se požadavky na linearitu RF komponent zpřísňovaly. Motivací pro podrobné specifikace IMD ve vydáních jako Rel-12 a novějších bylo zavedení složitějších scénářů: souvislá a nesouvislá agregace nosných v rámci pásma, mezipásmová agregace nosných s velkými frekvenčními odstupy a koexistence LTE s jinými systémy ve sdíleném spektru. Tyto specifikace zajišťují, že zařízení od různých výrobců fungují předvídatelně a nestanou se zdrojem interference v celé síti, což je základním požadavkem pro úspěšné nasazení hustých mobilních sítí s vysokou kapacitou.

## Klíčové vlastnosti

- Generování nežádoucích parazitních signálů na součtových a rozdílových frekvencích více vstupních signálů (např. 2f1-f2).
- Primárně charakterizováno třetím interceptním bodem (IP3), což je parametr linearity.
- Specifikováno v 3GPP jak pro parazitní emise vysílače, tak pro desenzibilizaci přijímače.
- Kritický testovací případ pro certifikaci zařízení s agregací nosných a vícepásmových zařízení.
- Ovlivňuje výkon jak uživatelského zařízení (UE), tak základnové stanice (eNodeB/gNB).
- Řízeno prostřednictvím lineárního návrhu obvodů, snížení výkonu (back-off) a technik digitálního predistorsu.

## Související pojmy

- [ACL – Asynchronous Connection-Oriented Link](/mobilnisite/slovnik/acl/)
- [SEM – Spectrum Emissions Mask](/mobilnisite/slovnik/sem/)

## Definující specifikace

- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 36.833** — 3GPP TR 36.833
- **TS 36.852** — 3GPP TR 36.852
- **TS 36.853** — 3GPP TR 36.853
- **TR 37.829** (Rel-18) — Technical Report
- **TS 37.863** — 3GPP TR 37.863
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [IMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/imd/)
