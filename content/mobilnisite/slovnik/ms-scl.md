---
slug: "ms-scl"
url: "/mobilnisite/slovnik/ms-scl/"
type: "slovnik"
title: "MS-SCL – Mobile Station – Supported Codec List"
date: 2025-01-01
abbr: "MS-SCL"
fullName: "Mobile Station – Supported Codec List"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ms-scl/"
summary: "MS-SCL (Mobile Station – Supported Codec List) je schopnost uživatelského zařízení (UE) přenášená do sítě, která podrobně popisuje audio a řečové kodeky, které zařízení podporuje. Je klíčová pro efekt"
---

MS-SCL je schopnost uživatelského zařízení (UE) přenášená do sítě, která podrobně popisuje audio a řečové kodeky, které mobilní zařízení podporuje pro efektivní sestavení hovoru a kompatibilní výběr média.

## Popis

Mobile Station – Supported Codec List (MS-SCL) je strukturovaný informační prvek definovaný 3GPP, který zapouzdřuje schopnosti kodeků uživatelského zařízení (UE). Je to kritická součást mechanismu výměny schopností mezi UE a jádrem sítě, konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v okruhově spínaných ([CS](/mobilnisite/slovnik/cs/)) doménách nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IMS doménách. MS-SCL je přenášen UE do sítě, typicky během registrace nebo jako součást signalizace pro sestavení hovoru. Technicky se jedná o seznam výčtu podporovaných řečových a audio kodeků (např. [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/), G.711) spolu s jejich přidruženými konfiguračními parametry, jako jsou podporované přenosové rychlosti, typy rámců a režimy kanálů. Síťový prvek (např. MSC Server) tuto informaci používá během procedury sestavování hovoru. Při směrování hovoru k nebo z UE síť provede proces vyjednávání kodeků. Porovná MS-SCL volajícího UE se schopnostmi cílového UE (nebo síťového prostředku), aby vybral optimální, vzájemně podporovaný kodek. Tento výběr si klade za cíl maximalizovat kvalitu hlasu při minimalizaci využití šířky pásma a vyhnutí se potřebě překódování uvnitř sítě, což může zhoršit kvalitu a přidat zpoždění. MS-SCL je přenášen v konkrétních signalizačních zprávách, jako jsou zprávy Register, Setup nebo Progress v CS řízení hovoru, nebo v rámci [SIP](/mobilnisite/slovnik/sip/) zpráv jako INVITE a 200 OK v IMS. Jeho role je zásadní pro interoperabilitu a kvalitu služeb v mobilních hlasových službách, zajišťuje, že dva koncové body mohou komunikovat pomocí nejkvalitnějšího dostupného společného kodeku, což je obzvláště důležité pro služby jako VoLTE (Voice over LTE) a VoNR (Voice over NR).

## K čemu slouží

MS-SCL existuje k vyřešení základního problému interoperability kodeků v heterogenních mobilních sítích. V raných celulárních systémech byla podpora kodeků omezená a často pevná, ale jak se sítě vyvíjely s GSM, UMTS a LTE, byla zavedena řada nových, efektivnějších kodeků (jako [AMR](/mobilnisite/slovnik/amr/), AMR-WB a EVS). Bez standardizovaného způsobu komunikace podporovaných kodeků zařízení by síť musela předpokládat nejnižšího společného jmenovatele nebo vynutit překódování, obojí suboptimální. Historickým motivem bylo umožnit efektivní sestavení hlasového hovoru a optimální výběr kvality hlasu. Před standardizovanými seznamy schopností byla interoperabilita náročná a pokročilé funkce kodeků nemohly být spolehlivě využity. MS-SCL, zavedený ve verzi 8 jako součást pokračujícího vývoje signalizace CS jádra sítě, poskytl formální, rozšiřitelný kontejner pro tuto informaci o schopnostech. Řešil omezení ad-hoc nebo proprietární signalizace schopností, zajišťuje interoperabilitu mezi více dodavateli pro UE a síťová zařízení. Umožněním přesného vyjednávání kodeků umožňuje sítím využívat novější, šířku pásma efektivní a kvalitnější kodeky, čímž zlepšuje spektrální účinnost a uživatelský zážitek, zejména při migraci služeb na paketově spínaný hlas přes IMS.

## Klíčové vlastnosti

- Strukturovaný seznam identifikátorů podporovaných řečových a audio kodeků (např. pro AMR, EVS)
- Zahrnuje specifické konfigurační parametry kodeků, jako jsou přenosové rychlosti a režimy
- Přenášen v signalizaci z UE do sítě (např. v CS řízení hovoru nebo SIP zprávách)
- Umožňuje síťový výběr optimálního kodeku během sestavování hovoru
- Snižuje potřebu překódování v síťové cestě, čímž zachovává kvalitu hlasu
- Rozšiřitelný pro zahrnutí nových kodeků definovaných v pozdějších vydáních 3GPP

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 43.903** (Rel-19) — Feasibility Study for A-interface over IP

---

📖 **Anglický originál a plná specifikace:** [MS-SCL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ms-scl/)
