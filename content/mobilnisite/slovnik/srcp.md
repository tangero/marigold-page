---
slug: "srcp"
url: "/mobilnisite/slovnik/srcp/"
type: "slovnik"
title: "SRCP – Speech Remote Control Protocol"
date: 2025-01-01
abbr: "SRCP"
fullName: "Speech Remote Control Protocol"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srcp/"
summary: "SRCP je protokol umožňující dálkové ovládání zařízení pomocí hlasových příkazů přes telekomunikační síť. Umožňuje uživatelům bezruční interakci se službami a zařízeními, což zvyšuje dostupnost a pohod"
---

SRCP je protokol umožňující dálkové ovládání zařízení pomocí hlasových příkazů přes telekomunikační síť, což umožňuje bezruční interakci se službami, jako je hlasové vytáčení.

## Popis

Speech Remote Control Protocol (SRCP) je protokol aplikační vrstvy standardizovaný 3GPP, který usnadňuje hlasové dálkové ovládání síťových služeb a uživatelských zařízení. Funguje na principu definování strukturovaného dialogu mezi uživatelským zařízením a aplikačním serverem v síti. Uživatel vydá mluvené příkazy, které jsou zachyceny mikrofonem zařízení. Tyto zvukové signály jsou pak paketizovány a přeneseny přes síť k vyhrazenému SRCP aplikačnímu serveru. Tento server hostuje stroje pro rozpoznávání řeči, které převádějí zvuk na proveditelné příkazy. Server následně tyto příkazy zpracuje, což může zahrnovat rozhraní k dalším síťovým službám (jako je řízení hovorů nebo zasílání zpráv) nebo ovládání lokálních funkcí zařízení, a odešle odpovídající odpovědi zpět uživateli, často ve formě syntetizované řeči nebo datových aktualizací.

Z architektonického hlediska je SRCP typicky implementován jako součást platformy pro přidané služby ([VAS](/mobilnisite/slovnik/vas/)) uvnitř jádra sítě, často s rozhraním k IP Multimedia Subsystem (IMS) pro řízení relace. Mezi klíčové komponenty patří SRCP klient na uživatelském zařízení (UE), který zajišťuje zachycení zvuku a signalizaci protokolu; SRCP aplikační server ([AS](/mobilnisite/slovnik/as/)), který provádí rozpoznávání řeči a vykonává servisní logiku; a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která může být použita pro úlohy zpracování řeči, jako je konverze kodeků nebo přehrávání hlášení. Protokol definuje specifické zprávy pro zahájení relace hlasového ovládání, odesílání zvukových paketů a předávání výsledků rozpoznání nebo chyb.

Úlohou SRCP je poskytnout standardizovanou metodu hlasového ovládání nezávislou na síti, která odděluje složitost rozpoznávání řeči od koncového zařízení. To umožňuje využití výkonnějších, aktualizovatelných rozpoznávacích strojů v síti a zajišťuje konzistentní uživatelský zážitek napříč různými typy koncových zařízení. Protokol spolupracuje s podkladovými transportními a relakovými protokoly (jako je [RTP](/mobilnisite/slovnik/rtp/) pro média a [SIP](/mobilnisite/slovnik/sip/) pro řízení relace) za účelem vytvoření spolehlivého kanálu pro hlasový dialog. Specifikace protokolu podrobně popisují syntaxi a sémantiku řídicích zpráv, což zajišťuje interoperabilitu mezi zařízeními různých výrobců a napříč servisními platformami různých síťových operátorů.

## K čemu slouží

SRCP byl vytvořen za účelem standardizace hlasem ovládaných služeb v mobilních sítích, aby vyhověl rostoucí poptávce po bezručních a dostupných uživatelských rozhraních. Před jeho standardizací byly funkce hlasového ovládání často proprietární, implementace specifické pro dané zařízení, kterým chyběla interoperabilita a které omezovaly dostupnost služeb. Tato roztříštěnost bránila širokému nasazení pokročilých hlasových služeb ze strany síťových operátorů. SRCP poskytl jednotný rámec, který operátorům umožnil nasadit síťové služby hlasového ovládání, které mohly konzistentně fungovat napříč širokým spektrem účastnických zařízení.

Motivace vycházela z touhy zvýšit uživatelský komfort, zlepšit dostupnost pro uživatele se zdravotním postižením a vytvořit nové služby generující příjmy pro operátory. Přesunutím zpracování rozpoznávání řeči do sítě umožnil SRCP využití sofistikovanějších, serverových rozpoznávacích algoritmů, které bylo možné aktualizovat bez nutnosti nového softwaru v koncovém zařízení. Tím byla vyřešena omezená výpočetní kapacita a úložný prostor na raných mobilních zařízeních, která byla nevhodná pro složité úlohy rozpoznávání řeči s bohatou slovní zásobou. Také umožnil centralizovanou správu hlasových gramatik a uživatelských profilů, což usnadnilo personalizované hlasové služby.

Historicky se zavedení SRCP v 3GPP Release 2 časově shodovalo s raným vývojem služeb 3G, kde se pozornost začala soustředit na multimediální a interaktivní datové služby. Jeho cílem bylo využít lepší přenosovou kapacitu a trvalé připojení paketových sítí k poskytování rychlých a spolehlivých služeb hlasových příkazů. Protokol odstranil omezení starších interaktivních hlasových odpovědí ([IVR](/mobilnisite/slovnik/ivr/)) založených na [DTMF](/mobilnisite/slovnik/dtmf/) (Dual-Tone Multi-Frequency), které byly těžkopádné a omezené na číselný vstup, tím, že umožnil přirozenou interakci řečí pro ovládání širšího spektra síťových a zařízeních funkcí.

## Klíčové vlastnosti

- Síťové rozpoznávání řeči, které odlehčuje zpracování od uživatelského zařízení
- Standardizovaný protokol pro interoperabilitu mezi zařízeními a síťovými platformami
- Podpora strukturovaných hlasových dialogů a gramatik příkazů
- Integrace s IMS a dalšími architekturami služeb jádra sítě
- Schopnost ovládat jak síťové služby, tak lokální funkce zařízení
- Mechanismy pro zpracování chyb a hlášení míry spolehlivosti rozpoznání

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework

---

📖 **Anglický originál a plná specifikace:** [SRCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/srcp/)
