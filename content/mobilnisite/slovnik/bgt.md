---
slug: "bgt"
url: "/mobilnisite/slovnik/bgt/"
type: "slovnik"
title: "BGT – Block Guard Time"
date: 2025-01-01
abbr: "BGT"
fullName: "Block Guard Time"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bgt/"
summary: "Block Guard Time je časový ochranný interval vložený mezi po sobě jdoucí přenosové bloky v buňkových systémech založených na TDMA. Zabraňuje překryvu sousedních časových slotů, zajišťuje správné časov"
---

BGT je časový ochranný interval vložený mezi po sobě jdoucí přenosové bloky v systémech TDMA, který zabraňuje jejich překryvu a snižuje interferenci.

## Popis

Block Guard Time (BGT) je základní časový parametr v buňkových systémech s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) standardizovaných 3GPP. Představuje pečlivě vypočítaný časový interval vložený mezi po sobě jdoucí přenosové bloky nebo bursty v rámci struktury rádiového rámce. Tato ochranná perioda slouží jako nárazníková zóna, která kompenzuje časové nepřesnosti, zpoždění šíření a nedokonalosti synchronizace, které se přirozeně vyskytují v mobilních komunikačních prostředích.

Technická implementace BGT zahrnuje přesné časové výpočty založené na poloměru buňky, maximálním očekávaném zpoždění šíření a synchronizačních schopnostech terminálu. V systémech GSM/[EDGE](/mobilnisite/slovnik/edge/) je BGT implementován jako součást struktury burstu, přičemž jsou definovány konkrétní délky pro různé typy burstů (normální burst, přístupový burst, burst pro frekvenční korekci, synchronizační burst). Ochranný čas je typicky implementován jako perioda ticha při přenosu nebo se specifickými bitovými vzory, které usnadňují synchronizaci přijímače. Délka se liší v závislosti na konkrétní aplikaci, přičemž přístupové bursty vyžadují delší ochranné časy, aby vyhověly počátečním procedurám náhodného přístupu, kdy ještě nebyl stanoven časový předstih.

Z architektonického hlediska BGT funguje na fyzické vrstvě rozhraní mezi mobilní stanicí a základnovou stanicí. Mechanismus časového předstihu základnové stanice spolupracuje s BGT, aby zajistil správné časové zarovnání. Když se mobilní stanice poprvé připojuje k síti, vysílá na kanálu pro náhodný přístup s maximálním ochranným časem, aby vyhověla neznámému zpoždění šíření. Jakmile základnová stanice změří časový posun, poskytne mobilní stanici příkazy pro časový předstih, čímž efektivně sníží potřebný ochranný čas pro následné přenosy.

Role BGT přesahuje rámec jednoduché časové ochrany. Umožňuje efektivní frekvenční reužití tím, že umožňuje těsnější uspořádání časových slotů při zachování ochrany před interferencí. V hierarchických strukturách buněk s různými velikostmi mohou být parametry BGT upraveny tak, aby vyhověly různým požadavkům na zpoždění šíření. Ochranný čas také poskytuje rezervu pro drift hodin mezi přenosy a umožňuje plynulé procedury předávání hovoru mezi buňkami s různými časovými referencemi.

## K čemu slouží

BGT byl vytvořen, aby řešil základní časové výzvy v [TDMA](/mobilnisite/slovnik/tdma/) buňkových systémech, zejména v sítích GSM. V systémech s časovým dělením je přesné časování zásadní, protože více uživatelů sdílí stejný frekvenční kanál vysíláním v různých časových slotech. Bez správných ochranných intervalů by se signály ze sousedních časových slotů překrývaly kvůli zpoždění šíření, což by způsobovalo intersymbolovou interferenci, která zhoršuje kvalitu signálu a zvyšuje míru bitových chyb.

Před standardizovanou implementací ochranného času se rané mobilní systémy potýkaly s problémy časové synchronizace, zejména ve velkých buňkách, kde mohla být zpoždění šíření významná. Různé vzdálenosti mezi mobilními stanicemi a základnovými stanicemi znamenaly, že signály přicházely v různých časech a mohly přetékat do sousedních časových slotů. BGT poskytuje systematické řešení vytvořením ochranného nárazníku, který těmto časovým variacím vyhoví, a zároveň zachovává spektrální účinnost.

Tato technologie řeší problém udržení ortogonality v časové doméně při podpoře mobilních uživatelů v různých vzdálenostech od základnové stanice. Umožňuje základnové stanici správně demultiplexovat signály od různých uživatelů bez nutnosti složitého zpracování signálu k oddělení překrývajících se přenosů. Poskytnutím této časové rezervy umožňuje BGT praktickou implementaci TDMA v reálných mobilních prostředích s měnícími se podmínkami šíření a mobilitou uživatelů.

## Klíčové vlastnosti

- Zabraňuje interferenci mezi sloty v TDMA systémech
- Kompenzuje variace v zpoždění šíření
- Umožňuje počáteční náhodný přístup bez časového předstihu
- Podporuje hierarchické struktury buněk s různými velikostmi
- Usnadňuje předávání hovoru mezi buňkami s časovými rozdíly
- Poskytuje rezervu pro nepřesnosti synchronizace hodin

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [BGT na 3GPP Explorer](https://3gpp-explorer.com/glossary/bgt/)
