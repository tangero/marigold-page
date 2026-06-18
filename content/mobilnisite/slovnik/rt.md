---
slug: "rt"
url: "/mobilnisite/slovnik/rt/"
type: "slovnik"
title: "RT – Real Time"
date: 2025-01-01
abbr: "RT"
fullName: "Real Time"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rt/"
summary: "V 3GPP označuje RT služby s přísnými požadavky na zpoždění a časování, jako jsou hlasové a video hovory, kde musí být data doručena v omezeném čase. Jde o základní třídu QoS, která odlišuje interaktiv"
---

RT je základní třída QoS pro služby s přísnými požadavky na zpoždění, jako jsou hlasové a video hovory, kde musí být data doručena v omezeném čase.

## Popis

V rámci architektury 3GPP není 'Real Time' (RT, tj. v reálném čase) jediným protokolem nebo rozhraním, ale základní charakteristikou kvality služeb (QoS) a klasifikací služby. Definuje kategorii provozu, u níž je hodnota informace kriticky závislá na včasnosti doručení. Celkové přenosové zpoždění (end-to-end) musí být omezené a předvídatelné, aby bylo pro aplikaci přijatelné. To je v kontrastu s provozem Non-Real Time ([NRT](/mobilnisite/slovnik/nrt/)) nebo provozem na pozadí, kde může být propustnost nebo míra chyb důležitější než striktní zpoždění. Klasifikace RT prostupuje více síťovými vrstvami a specifikacemi a ovlivňuje návrh protokolů, rezervaci zdrojů a plánovací algoritmy.

Jak jsou požadavky RT implementovány, zahrnuje několik klíčových komponent napříč rádiovou přístupovou sítí (RAN) a jádrem sítě (CN). V CN je pro službu, jako je Voice over IP (VoIP), zapojen IP Multimedia Subsystem (IMS) a architektura Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Pravidla PCC, definovaná funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), určují, že přenosový kanál (bearer) pro VoIP hovor musí být zřízen s hodnotou QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) asociovanou s konverzačním hlasem (např. QCI 1), která má striktní záruky pro prioritu, rozpočet zpoždění paketů a míru ztráty paketů chybami. Tento QoS profil je pak vynucován bránou Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a obslužnou bránou (serving gateway). V RAN diktuje povaha v reálném čase fungování [MAC](/mobilnisite/slovnik/mac/) a fyzické vrstvy. Například v UMTS je Radio Access Bearer ([RAB](/mobilnisite/slovnik/rab/)) pro hlasový hovor nakonfigurován se specifickými atributy, jako je garantovaná přenosová rychlost, přenosové zpoždění a priorita zpracování provozu. Plánovač Node B musí upřednostňovat rádiové zdroje pro tyto RT přenosové kanály před daty NRT, aby splnil rozpočet zpoždění.

Jeho role je naprosto klíčová pro základní funkci mobilních sítí: umožnění interaktivní komunikace. Celý návrh rozhraní pro přenos vzduchem, od rámcové struktury v GSM ([TDMA](/mobilnisite/slovnik/tdma/) časové sloty) po Transmission Time Intervals (TTI) v UMTS/LTE a mini-sloty v 5G NR, je optimalizován pro podporu služeb RT s nízkou latencí. Plánovací algoritmy v základnové stanici (eNodeB/gNB) neustále činí rozhodnutí na úrovni milisekund, aby přidělily bloky fyzických zdrojů (PRBs) uživatelským zařízením (UE) s aktivními RT relacemi. Mechanismy řízení přístupu (admission control) také využívají požadavky služeb RT k rozhodnutí, zda lze přijmout nový hovor bez zhoršení výkonu stávajících hovorů. Dále jsou procedury mobility, jako je předávání hovoru (handover), optimalizovány pro služby RT, často využívají rychlejší, sítí řízená předání, aby se zabránilo přerušení hovoru, na rozdíl od více měřením řízených předání možných u datových služeb typu best-effort.

## K čemu slouží

Koncept klasifikace služeb Real Time existuje, aby řešil základní výzvu podpory zpoždění citlivé lidské komunikace, primárně hlasu, přes sdílené, paketově přepínané sítě. Raná mobilní telefonie (GSM) byla inherentně okruhově přepínaná, vyčleňující fyzický kanál (časový slot) na dobu trvání hovoru, což přirozeně zaručovalo časování. S evolucí směrem k paketově přepínaným sítím v UMTS a zejména LTE/5G se veškerý provoz, včetně hlasu, stal paketizovanými daty. To zavedlo problém s kolísáním zpoždění (jitter) a proměnlivým zpožděním kvůli statistickému multiplexování a frontám. Třída QoS RT byla vytvořena, aby zajistila, že tyto hlasové/video pakety dostanou přednostní zacházení po celé síťové cestě, napodobující záruky okruhově přepínaného kanálu.

Historicky učinil přechod na plně IP sítě (AIPN) v 3GPP Release 5 a novějších explicitní mechanismy QoS nezbytnými. Bez nich by mohly být hlasové pakety zpožděny za velkými stahováními souborů, což by znemožnilo konverzaci. Klasifikace RT spolu s přidruženými parametry QoS (jako QCI, ARP, GBR) poskytuje standardizovaný rámec pro sítě, aby rozlišovaly tento kritický provoz. Řeší problém degradace služeb v konvergované síti a umožňuje operátorům nabízet tradiční telefonní služby (přes VoLTE, VoNR) s provozovatelskou (carrier-grade) spolehlivostí přes infrastrukturu založenou na IP. To umožnilo ukončení provozu starších okruhově přepínaných jader při zachování, a dokonce zlepšení, uživatelského zážitku pro komunikaci v reálném čase.

## Klíčové vlastnosti

- Definuje provoz s požadavky na omezené celkové zpoždění (end-to-end)
- Mapuje se na specifické identifikátory tříd QoS (QCIs) pro zřizování přenosových kanálů
- Ovlivňuje plánování v RAN a prioritní algoritmy
- Spouští specifické politiky řízení přístupu a rezervace zdrojů
- Nezbytná pro konverzační hlas (VoLTE/VoNR) a živé video streamování
- Vyžaduje optimalizované řízení mobility (např. bezproblémové předání hovoru)

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [RT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rt/)
