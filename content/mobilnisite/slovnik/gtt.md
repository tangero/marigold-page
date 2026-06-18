---
slug: "gtt"
url: "/mobilnisite/slovnik/gtt/"
type: "slovnik"
title: "GTT – Global Text Telephony"
date: 2025-01-01
abbr: "GTT"
fullName: "Global Text Telephony"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gtt/"
summary: "Global Text Telephony (GTT) je funkce 3GPP umožňující konverzaci pomocí textu v reálném čase v rámci jakékoli konverzační služby 3GPP, například hlasového volání. Poskytuje dostupnou komunikační metod"
---

GTT je funkce 3GPP, která umožňuje konverzaci pomocí textu v reálném čase v rámci služeb, jako jsou hlasová volání, a poskytuje tak dostupnou komunikační metodu pro uživatele se sluchovým nebo řečovým postižením.

## Popis

Global Text Telephony (GTT) je standardizovaná služba v rámci specifikací 3GPP navržená pro podporu komunikace pomocí textu v reálném čase ([RTT](/mobilnisite/slovnik/rtt/)) jako nedílné součásti konverzačních multimediálních služeb, jako je telefonie založená na IP Multimedia Subsystem (IMS). Funguje tak, že v rámci relace vytváří textový mediální proud vedle nebo namísto hlasového mediálního proudu, což umožňuje přenos znaků v okamžiku jejich psaní a poskytuje tak bezprostřední konverzační zážitek. Architektura využívá stávající IMS core a paketové ([PS](/mobilnisite/slovnik/ps/)) přenosy, se specifickými aplikačními servery a schopnostmi uživatelského zařízení (UE) pro vyjednávání, navázání a správu textové relace. Mezi klíčové funkční komponenty patří GTT Application Server (GTT [AS](/mobilnisite/slovnik/as/)) v doméně IMS, který zajišťuje servisní logiku, a UE, které musí podporovat potřebné kodeky a řídicí protokoly relace, jako jsou [SIP](/mobilnisite/slovnik/sip/) a [RTP](/mobilnisite/slovnik/rtp/) pro přenos textu.

Technicky se relace GTT navazují pomocí metody SIP INVITE s nabídkami Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)), které indikují podporu pro textové mediální linky, typicky s využitím kodeků jako je textový protokol [ITU-T](/mobilnisite/slovnik/itu-t/) T.140 zapouzdřený v RTP. Síť zajišťuje Quality of Service (QoS) pro textový proud, často mu přiděluje vyhrazený přenos s příslušnými hodnotami QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)), aby byla garantována nízká latence a spolehlivé doručení, což je pro interakci v reálném čase zásadní. Propojení se staršími systémy textové telefonie, jako je Text over IP (ToIP) nebo tradiční služby teletypewriter (TTY) přes sítě s přepojováním okruhů, je klíčovým aspektem, který je zajišťován prostřednictvím interworking functions (IWFs) překládajících mezi různými formáty přenosu textu a signalizačními protokoly.

Role GTT v síti přesahuje základní dostupnost; je součástí prostředku Conversational Services, který zajišťuje, že text je plnohodnotným typem média v multimediální telefonii. Tato integrace umožňuje kombinované hlasové a textové relace, kde uživatelé mohou přepínat mezi oběma modalitami nebo je používat současně. Služba je definována v mnoha specifikacích 3GPP pokrývajících servisní požadavky (řada 22), architekturu (řada 23), kodeky (řada 26) a signalizaci (řada 29), což zajišťuje interoperabilitu mezi různými výrobci a síťovými nasazeními. Její implementace je povinná pro splnění některých regulatorních požadavků na dostupnost v různých regionech, což z ní činí klíčovou komponentu pro síťové operátory k dosažení shody a poskytování inkluzivních komunikačních služeb.

## K čemu slouží

GTT bylo vytvořeno pro uspokojení potřeby standardizované komunikace pomocí textu v reálném čase v sítích 3GPP, primárně pro službu uživatelům s postižením, jako jsou neslyšící, nedoslýchaví nebo osoby s řečovým postižením. Před jeho zavedením byla textová komunikace v mobilních sítích většinou omezena na neréžimové SMS nebo proprietární implementace textové telefonie, kterým chyběla interoperabilita a bezproblémová integrace s hlasovými službami. Motivace vycházela z regulatorních tlaků, jako je americký Twenty-First Century Communications and Video Accessibility Act (CVAA) a evropské směrnice o dostupnosti, které nařizovaly, aby telekomunikační služby byly dostupné všem uživatelům.

Historicky existovala textová telefonie ve formě TTY zařízení přes analogové telefonní linky, ale přechod na digitální sítě a sítě s přepojováním paketů, jako jsou GSM a UMTS, vytvořil problémy s kompatibilitou. Rané verze 3GPP měly omezenou podporu textu, často vyžadující návrat k režimům přenosu dat s přepojováním okruhů. GTT, zavedené ve verzi 4 jako součást evoluce IMS, poskytlo nativní řešení založené na IP, které integruje text jako základní typ média v rámci konverzační multimediální domény. Tím byly vyřešeny limity fragmentovaných, nestandardizovaných přístupů definováním jednotné architektury, signalizace a specifikací kodeků, což umožnilo doručování textu v reálném čase se stejnými očekáváními spolehlivosti a kvality jako u hlasu.

Tato technologie řeší problém inkluzivní komunikace tím, že zajišťuje, aby text nebyl až druhořadou záležitostí, ale základní servisní komponentou. Umožňuje síťovým operátorům nasadit jediný, do budoucna připravený systém, který bezproblémově podporuje jak hlas, tak text, což snižuje složitost a náklady ve srovnání s údržbou oddělených řešení dostupnosti. Dále GTT usnadňuje přístup k nouzovým službám (např. text-to-911) a zlepšuje komunikaci v hlučném prostředí, čímž prospívá širší uživatelské základně i mimo osoby s postižením, a tím se slučuje s cílem 3GPP poskytovat univerzální službu.

## Klíčové vlastnosti

- Přenos znaků v reálném čase během konverzačních relací
- Integrace s architekturou multimediální telefonie (MMTel) založenou na IMS
- Podpora simultánních hlasových a textových mediálních proudů v rámci jedné relace
- Propojení se staršími systémy textové telefonie TTY a s přepojováním okruhů
- Standardizované použití textového protokolu ITU-T T.140 přes transport RTP
- Správa QoS pro doručování textu s nízkou latencí prostřednictvím vyhrazených přenosů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [TTY – Text Telephone or TeletYpewriter](/mobilnisite/slovnik/tty/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture

---

📖 **Anglický originál a plná specifikace:** [GTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/gtt/)
