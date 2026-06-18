---
slug: "evm"
url: "/mobilnisite/slovnik/evm/"
type: "slovnik"
title: "EVM – Error Vector Magnitude"
date: 2025-01-01
abbr: "EVM"
fullName: "Error Vector Magnitude"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/evm/"
summary: "Kritická metrika pro měření přesnosti modulace a kvality vysílaného rádiového signálu. Kvantifikuje rozdíl mezi ideálním referenčním signálem a skutečně vysílaným signálem a přímo ovlivňuje datovou pr"
---

EVM je metrika, která měří přesnost modulace tím, že kvantifikuje rozdíl mezi ideálním referenčním signálem a skutečně vysílaným signálem, což ovlivňuje datovou propustnost a spolehlivost spojení.

## Popis

Error Vector Magnitude (EVM, velikost chybového vektoru) je základním měřítkem výkonnosti fyzické vrstvy digitálních rádiových vysílačů, zejména v systémech s ortogonálním frekvenčním multiplexem ([OFDM](/mobilnisite/slovnik/ofdm/)) a jednoduchým nosičem používaných ve standardech 3GPP. Je definována jako střední kvadratická ([RMS](/mobilnisite/slovnik/rms/)) hodnota chybového vektoru – vektorového rozdílu v rovině I/Q (in-fáze/kvadratura) mezi ideálním bodem konstelace (definovaným modulačním schématem, např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM) a skutečně změřeným bodem přijatého symbolu po aplikaci časových, frekvenčních a fázových korekcí. Výsledek je typicky normalizován vůči výkonu ideálního signálu a vyjádřen v procentech nebo v dB.

Proces měření zahrnuje zachycení vysílaného signálu, synchronizaci s ním a co největší vyrovnání vlivů kanálu, aby byly izolovány zkreslení vysílače. U vícekanálových systémů, jako je OFDM, se EVM měří na každé podnosné a často se agreguje jako RMS průměr přes určenou množinu podnosných a symbolů v rámci měřicí periody. Mezi klíčové zdroje EVM patří nedokonalosti vysílače, jako je fázový šum z lokálního oscilátoru, nelineární zkreslení z výkonového zesilovače (způsobující spektrální rozrůstání a kompresi), nerovnováha I/Q (nesoulad ve zesílení a fázi mezi drahami I a Q) a zbytkový posun nosné frekvence. Každá z těchto vad způsobuje rozptyl nebo rotaci bodů konstelace, čímž zvyšuje EVM.

Ve specifikacích 3GPP (např. TS 36.104 pro LTE, TS 38.104 pro NR) je EVM klíčovým požadavkem na vysílač specifikovaným pro každý podporovaný modulační řád v rádiových testech shody základnové stanice ([BS](/mobilnisite/slovnik/bs/)) a uživatelského zařízení (UE). Jsou definovány přísné limity EVM, aby bylo zajištěno, že vysílaný signál je dostatečně přesný pro demodulaci dat přijímačem s nízkou blokovou chybovostí ([BLER](/mobilnisite/slovnik/bler/)). Pro vyšší modulační řády, jako je 256QAM nebo 1024QAM, které zabalí více bitů na symbol a mají menší rozhodovací oblasti mezi body konstelace, je povolená EVM mnohem přísnější (např. 3,5 % pro 256QAM v NR) ve srovnání s nižšími modulačními řády, jako je QPSK (např. 17,5 %). To z EVM činí přímý faktor umožňující vysokou spektrální účinnost. Specifikace podrobně popisují přesný měřicí postup, včetně použitého referenčního signálu (např. vyhrazené piloty nebo [DM-RS](/mobilnisite/slovnik/dm-rs/)), měřicí šířky pásma a vyloučení určitých časových/frekvenčních zdrojů.

## K čemu slouží

EVM slouží jako komplexní jediná hodnota kvality pro kvantifikaci celkové modulační kvality digitálního vysílače a nahrazuje starší, méně přesné metriky, jako je poměr signálu k šumu (SNR), pro hodnocení linearity a čistoty složitě modulovaných signálů. Jak se mobilní systémy vyvíjely od 2G GMSK k vysokým řádům QAM ve 3G/4G/5G, potřeba přesného měření nedokonalostí vysílače se stala kritickou, protože tyto nedokonalosti přímo omezují dosažitelné datové rychlosti a výkon na okraji buňky. Bez přísné kontroly EVM by vyšší modulační řády selhaly, což by nutilo adaptaci spojení přepnout na robustnější, ale méně účinná schémata, a tím snížit kapacitu sítě.

Primární problém, který EVM řeší, je poskytnutí výrobcům zařízení a síťovým operátorům standardizované, opakovatelné metody pro ověření, že rádiový vysílač splňuje minimální výkon potřebný pro spolehlivou komunikaci. Silně koreluje s metrikami výkonnosti na systémové úrovni, jako je propustnost a BLER. Specifikací maximálních hodnot EVM v testech shody zajišťuje 3GPP interoperabilitu – UE od jednoho výrobce může úspěšně demodulovat signály od základnové stanice jiného výrobce, a to i za neideálních podmínek. To bylo zvláště důležité pro celosvětový úspěch LTE a NR.

Historicky, jak každá nová generace zaváděla vyšší šířky pásma a složitější modulaci, zdroje degradace EVM se stávaly náročnějšími na zvládnutí. Vytvoření podrobných specifikací EVM motivovalo pokrok v návrhu vysokofrekvenčních (RF) komponent, jako jsou vylepšené techniky linearizace výkonového zesilovače (např. digitální predistorse), oscilátory s nižším fázovým šumem a lepší kalibrace I/Q modulátorů. EVM tedy není jen měřením, ale hybatelem inovací v RF technologii, který umožňuje vysokorychlostní datové služby definující moderní mobilní broadband.

## Klíčové vlastnosti

- Kvantifikuje přesnost modulace jako RMS chybu mezi ideálními a změřenými body konstelace
- Normalizovaná metrika vyjádřená v procentech nebo dB umožňující srovnání napříč úrovněmi výkonu
- Klíčový parametr v rádiových testech shody 3GPP pro základnové stanice a UE pro každé modulační schéma
- Měření se provádí na každé podnosné v systémech OFDM a průměruje se přes určené zdroje
- Těsně spojena s podporovaným modulačním řádem a celkovou spektrální účinností
- Diagnostikuje konkrétní nedokonalosti vysílače: fázový šum, nelinearita výkonového zesilovače, nerovnováha I/Q

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- … a dalších 45 specifikací

---

📖 **Anglický originál a plná specifikace:** [EVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/evm/)
