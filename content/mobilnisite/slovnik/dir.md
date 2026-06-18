---
slug: "dir"
url: "/mobilnisite/slovnik/dir/"
type: "slovnik"
title: "DIR – Dominant-to-rest Interference Ratio"
date: 2025-01-01
abbr: "DIR"
fullName: "Dominant-to-rest Interference Ratio"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dir/"
summary: "DIR je klíčová metrika v 3GPP GERAN (GSM/EDGE RAN) sloužící k charakterizaci kvality rádiového kanálu měřením poměru výkonu nejsilnější rušivé složky ke kombinovanému výkonu všech ostatních rušivých s"
---

DIR je metrika 3GPP GERAN, která měří poměr výkonu nejsilnější rušivé signálové složky k celkovému výkonu všech ostatních rušivých složek, čímž charakterizuje kvalitu kanálu pro potlačení interference.

## Popis

Dominant-to-rest Interference Ratio (DIR) je parametr definovaný ve specifikacích 3GPP [GERAN](/mobilnisite/slovnik/geran/), konkrétně v TS 45.903. Kvantifikuje strukturu interference, kterou zažívá mobilní přijímač, tím, že rozlišuje mezi jedním dominantním rušičem a kolektivním 'zbytkem' interference. Metrika se vypočítá jako poměr (obvykle v dB) výkonu nejsilnějšího ko-kanálového nebo sousedního-kanálového rušiče (tzv. 'dominantního' rušiče) k celkovému výkonu všech ostatních rušivých signálů plus šumu. Toto rozlišení je architektonicky významné, protože mnoho pokročilých typů přijímačů, jako jsou ty využívající interference rejection combining ([IRC](/mobilnisite/slovnik/irc/)) nebo single-antenna interference cancellation ([SAIC](/mobilnisite/slovnik/saic/)), je navrženo tak, aby specificky zaměřily a potlačily jediného silného rušiče. Síť může odhadnout DIR na základě měření hlášených mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a použít tuto informaci k výběru nejvhodnějšího schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) a, což je klíčové, k rozhodnutí, zda nasadit pokročilou přijímací funkci, která může využít tento specifický profil interference.

Během provozu měření DIR ovlivňuje algoritmy adaptace spoje a řízení rádiových prostředků. Vysoká hodnota DIR indikuje, že prostředí interference je ovládáno jedním konkrétním zdrojem, což je příznivá podmínka pro přijímače s potlačením interference. V takovém případě může síť naplánovat přenosy s modulacemi vyššího řádu (jako [8-PSK](/mobilnisite/slovnik/8-psk/) nebo vyšší v [EDGE](/mobilnisite/slovnik/edge/)), protože přijímač může efektivně potlačit primárního rušiče. Naopak nízký DIR naznačuje rozptýlenější, šumu podobný scénář interference, kde by mohly být vhodnější klasické přijímače nebo jednoduché techniky diverzity. DIR tedy není jen měřením, ale řídicím parametrem, který umožňuje inteligentní výběr režimu přijímače, optimalizující kompromis mezi spektrální účinností a robustností.

Role DIR je klíčová pro zvýšení kapacity a výkonu sítí GSM/EDGE, zejména v hustých městských nasazeních, kde je frekvenční reuse agresivní a interference je hlavním limitujícím faktorem. Přesnou charakterizací interference se systém může posunout za hranici zacházení se všemi interferenčními složkami jako s aditivním bílým Gaussovským šumem ([AWGN](/mobilnisite/slovnik/awgn/)) a aplikovat cílená protiopatření. To umožňuje těsnější vzorce frekvenčního reusu, vyšší datové rychlosti na okraji buňky a celkové zlepšení kvality služeb. Parametr je typicky zpracováván v řadiči základnové stanice (BSC) a v základnové přijímací/vysílací stanici (BTS), přičemž MS poskytuje potřebná nezpracovaná měřicí data prostřednictvím standardizovaných reportovacích mechanismů.

## K čemu slouží

DIR byl zaveden, aby řešil základní limit kapacity v sítích GSM/EDGE: ko-kanálovou interferenci. Tradiční plánování sítě spoléhalo na statické vzorce frekvenčního reusu, aby udrželo interferenci na zvládnutelné úrovni, ale tento přístup plýtval spektrem. Účelem DIR je umožnit dynamické řízení interference poskytnutím přesné metriky, která informuje pokročilé přijímací algoritmy. Identifikací scénářů, kde převažuje jediný rušič, může síť odemknout potenciál technik potlačení interference, což umožňuje agresivnější frekvenční reuse a vyšší spektrální účinnost bez degradace kvality služby.

Historicky přijímače zacházely s interferencí jako s nediferencovanou hladinou šumu, což omezovalo výkon. Vývoj přijímačů schopných potlačit specifické rušiče, jako jsou ty využívající SAIC pro hlasové kanály, vytvořil potřebu metriky na straně sítě, aby se rozhodlo, kdy tyto schopnosti aktivovat. DIR tento problém řeší kvantifikací struktury interference. Jeho vytvoření bylo motivováno snahou průmyslu vytěžit maximální hodnotu z existujícího GSM spektra a infrastruktury, čímž se oddálila potřeba nákladných akvizic nového spektra nebo nasazení nových stanovišť. Představuje posun od statického, plánováním založeného vyhýbání se interferenci k dynamickému, přijímačem asistovanému zmírňování interference.

## Klíčové vlastnosti

- Kvantifikuje strukturu interference oddělením výkonu dominantního rušiče od agregátu ostatních rušičů
- Umožňuje inteligentní výběr pokročilých režimů přijímače (např. SAIC, IRC) v mobilní stanici
- Informuje algoritmy adaptace spoje o volbě optimálních schémat modulace a kódování
- Klíčový vstup pro rozhodnutí řízení rádiových prostředků, zejména ve scénářích s těsným reusem
- Definován specificky pro GSM/EDGE Radio Access Network (GERAN) ve specifikacích 3GPP
- Hlášen mobilní stanicí pro podporu síťových strategií zmírňování interference

## Související pojmy

- [DARP – Downlink Advanced Receiver Performance](/mobilnisite/slovnik/darp/)
- [SAIC – Single Antenna Interference Cancellation](/mobilnisite/slovnik/saic/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks

---

📖 **Anglický originál a plná specifikace:** [DIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dir/)
