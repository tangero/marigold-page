---
slug: "lpp"
url: "/mobilnisite/slovnik/lpp/"
type: "slovnik"
title: "LPP – LTE Positioning Protocol"
date: 2026-01-01
abbr: "LPP"
fullName: "LTE Positioning Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lpp/"
summary: "LPP je bodový protokol využívaný mezi lokalizačním serverem (např. E-SMLC) a cílovým zařízením (UE) ke zjištění jeho zeměpisné polohy. Podporuje více metod určování polohy, jako je OTDOA, A-GNSS a E-C"
---

LPP je bodový protokol mezi lokalizačním serverem a mobilním zařízením sloužící ke zjištění zeměpisné polohy zařízení a podporující více metod přesného určování polohy.

## Popis

LTE Positioning Protocol (LPP) je klíčový protokol aplikační vrstvy v architektuře řídicí roviny 3GPP, speciálně navržený pro přenos lokalizačních informací. Funguje mezi lokalizačním serverem ([LS](/mobilnisite/slovnik/ls/)), jako je Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5GC, a cílovým uživatelským zařízením (UE). LPP je přenášen přes rozhraní LTE-Uu a SLg prostřednictvím [NAS](/mobilnisite/slovnik/nas/) transportu, což zajišťuje bezpečné a spolehlivé doručení lokalizačních příkazů a měření. Protokol je vnitřně schopný rozpoznat možnosti; LPP relace obvykle začíná tím, že server dotazuje UE na podporované metody určování polohy (např. Observed Time Difference of Arrival - [OTDOA](/mobilnisite/slovnik/otdoa/), Assisted Global Navigation Satellite System - [A-GNSS](/mobilnisite/slovnik/a-gnss/), Enhanced Cell ID - [E-CID](/mobilnisite/slovnik/e-cid/)) a související schopnosti, což serveru umožňuje vybrat nejvhodnější techniku pro požadovanou přesnost a prostředí.

LPP zprávy jsou strukturovány do několika typů procedur. Hlavními procedurami jsou: Přenos schopností, kdy UE informuje server o svých podporovaných lokalizačních metodách; Přenos asistenčních dat, kdy server může poskytnout UE data (jako jsou efemeridy [GNSS](/mobilnisite/slovnik/gnss/) nebo informace o referenční buňce pro OTDOA) pro zlepšení rychlosti a přesnosti určení polohy; a Přenos lokalizačních informací, který může být iniciován sítí (server vyžaduje měření nebo odhad polohy) nebo UE (UE poskytne svou polohu). Pro OTDOA server poskytuje asistenční data obsahující seznam sousedních buněk a konfiguraci jejich lokalizačních referenčních signálů (PRS). UE následně změří rozdíl času příchodu referenčního signálu (RSTD) mezi těmito buňkami a nahlasí jej zpět přes LPP, aby server mohl vypočítat polohu.

V systému 5G zůstává LPP hlavním lokalizačním protokolem, nyní mezi UE a LMF. Jeho architektura byla rozšířena o podporu nových lokalizačních referenčních signálů 5G NR (PRS pro DL-TDOA, SRS pro UL-TDOA) a technik jako Multi-RTT (Round Trip Time). LPP zprávy jsou přenášeny přes rozhraní NG řídicí roviny (NG-C) prostřednictvím 5G NAS. Protokol podporuje jak lokalizaci v reálném čase pro služby jako tísňová volání, tak odložené nebo periodické určování polohy pro sledovací aplikace. Jeho návrh je modulární a rozšiřitelný, což umožňuje přidávat nové metody určování polohy a typy měření v následujících vydáních 3GPP bez nutnosti zásadních změn základního protokolu, a zajišťuje tak jeho budoucí použitelnost jako základu pro lokalizační služby založené na celulárních sítích.

## K čemu slouží

LPP byl vytvořen, aby poskytl standardizovanou, efektivní a přesnou metodu pro určování polohy zařízení v LTE sítích, což řeší regulatorní požadavky jako Enhanced 911 (E911) a umožňuje komerční služby založené na poloze (LBS). Před LPP spoléhaly lokalizační služby v sítích 2G/3G na méně přesné metody, jako je Cell-ID, nebo používaly proprietární protokoly, což vedlo k fragmentaci a nekonzistentnímu výkonu. Vývoj LTE poskytl příležitost k návrhu jednotného lokalizačního protokolu na bázi IP od základů.

Protokol byl motivován potřebou vysoké přesnosti, nízké latence a minimálního dopadu na životnost baterie UE. Řeší problém koordinace složitých lokalizačních měření (vyžadujících přesné časování a informace o signálu) mezi sítí a potenciálně miliony zařízení. Podporou přenosu asistenčních dat umožňuje LPP UE rychleji zachytávat signály GNSS (A-GNSS) nebo provádět OTDOA měření přesněji, což výrazně zlepšuje výkon ve srovnání s autonomními metodami. Jeho vytvoření umožnilo široké spektrum aplikací nad rámec tísňových služeb, včetně navigace krok za krokem, sledování majetku, geofencingu a optimalizace sítě na základě polohy, což učinilo přesnou lokalizaci klíčovou schopností moderních celulárních sítí.

## Klíčové vlastnosti

- Podpora více metod určování polohy (OTDOA, A-GNSS, E-CID, senzorových, WLAN, BT)
- Vyjednávání schopností mezi UE a lokalizačním serverem
- Přenos lokalizačních asistenčních dat pro zlepšení výkonu UE
- Podpora režimů určování polohy založených na UE i asistovaných UE
- Přenos přes NAS, což zajišťuje zabezpečení a spolehlivost řídicí roviny
- Rozšiřitelný návrh pro začlenění nových metod, jako je 5G NR Multi-RTT a AoA

## Související pojmy

- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.586** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 24.572** (Rel-19) — 5G LCS User Plane Protocol Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [LPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lpp/)
