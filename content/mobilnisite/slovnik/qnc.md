---
slug: "qnc"
url: "/mobilnisite/slovnik/qnc/"
type: "slovnik"
title: "QNC – QoS Notification Control"
date: 2025-01-01
abbr: "QNC"
fullName: "QoS Notification Control"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/qnc/"
summary: "QoS Notification Control (QNC) je schopnost 5G core sítě, která síti umožňuje upozornit uživatelské zařízení (UE) na změny jeho autorizovaných parametrů QoS. Umožňuje dynamickou adaptaci QoS, jako je"
---

QNC je schopnost 5G core sítě, která uživatelskému zařízení (UE) oznamuje změny jeho autorizovaných parametrů QoS, aby umožnila dynamickou adaptaci, například úpravu garantovaných přenosových rychlostí.

## Popis

QoS Notification Control (QNC) je mechanismus definovaný v rámci 5G systému (5GS), který umožňuje síti informovat uživatelské zařízení (UE) o změnách jeho autorizovaných parametrů kvality služby (QoS) pro existující [PDU](/mobilnisite/slovnik/pdu/) (Protocol Data Unit) session nebo QoS Flow. Na rozdíl od statického přidělování QoS umožňuje QNC dynamické úpravy po zavedení session. Toto oznámení je klíčové pro sladění představy UE o dostupných zdrojích s aktuálními rozhodnutími síťové politiky nebo provozním stavem sítě.

Proceduru QNC primárně řídí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Když se PCF rozhodne, že je vyžadována změna autorizovaných parametrů QoS – z důvodů jako aktualizace politik, přetížení sítě, řízení specifické pro síťový řez (slice) nebo požadavek aplikace – odešle aktualizaci politiky Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). SMF, která je zodpovědná za správu PDU session, pak zahájí proces oznámení směrem k UE. To zahrnuje komunikaci SMF s Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a nakonec s Radio Access Network (RAN) za účelem doručení zprávy s oznámením o QoS na UE.

Po přijetí oznámení se očekává, že UE odpovídajícím způsobem přizpůsobí své chování v uplink provozu. Například pokud je autorizovaná přenosová rychlost pro QoS Flow snížena, mělo by UE omezit svou přenosovou rychlost na novou hodnotu. Oznámení typicky obsahuje aktualizované parametry QoS, jako je 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)), Aggregate Bit Rate ([ABR](/mobilnisite/slovnik/abr/)), Guaranteed Flow Bit Rate (GFBR) nebo Maximum Flow Bit Rate ([MFBR](/mobilnisite/slovnik/mfbr/)). QNC funguje v rámci UE policy frameworku a liší se od zřizování QoS pravidel; nezavádí nová pravidla, ale upravuje autorizaci spojenou s existujícími pravidly nebo toky. Tento mechanismus je nedílnou součástí dosažení QoS řízení v uzavřené smyčce, kde síť může reagovat téměř v reálném čase na měnící se podmínky a udržovat smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), zejména ve složitých prostředích, jako je síťové dělení (network slicing).

## K čemu slouží

QNC bylo zavedeno v 5G (Rel-15) jako řešení omezení statického QoS řízení, které převládalo v předchozích generacích. V 4G/LTE byly parametry QoS z velké části nastaveny během zřizování přenosového kanálu (bearer) a mohly být změněny pouze prostřednictvím složitých procedur jeho modifikace, které nebyly optimalizovány pro rychlé změny řízené politikami. Příchod 5G přinesl rozmanité požadavky služeb, síťové dělení (network slicing) a dynamické řízení politik, což si vyžádalo agilnější metodu komunikace změn QoS koncovému zařízení.

Hlavním problémem, který QNC řeší, je synchronizace stavu QoS mezi síťovým bodem rozhodování politik (PCF) a UE. Bez QNC by UE mohlo pokračovat v přenosu rychlostí, kterou síť již nemůže podporovat kvůli přetížení, změně prioritizace řezu (slice) nebo změně uživatelského tarifu, což by vedlo ke ztrátám paketů, neefektivitě nebo porušení SLA. QNC umožňuje efektivní využití síťových zdrojů tím, že síti dovoluje okamžitě snížit (nebo příležitostně zvýšit) QoS autorizace. To je obzvláště důležité pro síťové dělení (network slicing), kde jsou zdroje sdíleny a musí být přidělovány pružně, a pro kontinuitu služeb, když se uživatel přesouvá mezi různými instancemi řezů nebo když se v průběhu session změní požadavky aplikace. Poskytuje detailní kontrolu potřebnou pro pokročilé případy užití 5G, jako je průmyslový IoT, ultra-spolehlivá komunikace s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB).

## Klíčové vlastnosti

- Umožňuje síti iniciované oznámení UE o aktualizovaných autorizovaných parametrech QoS
- Je spouštěno Policy Control Function (PCF) na základě dynamických rozhodnutí politik
- Je doručováno přes SMF, AMF a RAN k UE pomocí existujících signalizačních cest
- Umožňuje dynamickou úpravu parametrů jako 5QI, GFBR, MFBR a agregovaných přenosových rychlostí (Aggregate Bit Rates)
- Podporuje efektivní správu zdrojů pro síťové dělení (network slicing) a řízení přetížení
- Integruje se s 5G UE policy frameworkem pro ucelené řízení chování zařízení

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [QNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/qnc/)
