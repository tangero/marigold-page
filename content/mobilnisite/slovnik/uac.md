---
slug: "uac"
url: "/mobilnisite/slovnik/uac/"
type: "slovnik"
title: "UAC – Unified Access Control"
date: 2025-01-01
abbr: "UAC"
fullName: "Unified Access Control"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uac/"
summary: "Mechanismus, který spravuje pokusy o přístup uživatelského zařízení (UE) k rádiové síti během zahlcení nebo nouzových situací. Používá třídění přístupu podle přístupových tříd (ACB), řízení přístupu s"
---

UAC je mechanismus, který spravuje pokusy o přístup UE během zahlcení nebo nouzových stavů. Používá třídění přístupu podle přístupových tříd (Access Class Barring), řízení přístupu specifické pro služby (Service Specific Access Control) a rozšířené třídění přístupu (Extended Access Barring) k upřednostnění konkrétních uživatelů nebo služeb pro stabilitu sítě.

## Popis

Unified Access Control (UAC) je komplexní rámec ve specifikacích 3GPP, který řídí, jak je uživatelskému zařízení (UE) povoleno nebo zakázáno zahájit přístup k rádiové síti (např. pro uskutečnění hovoru, odeslání dat nebo signalizaci). Jedná se o klíčovou funkci správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), kterou provádí rádiová přístupová síť (RAN) ve spolupráci s jádrem sítě. UAC využívá sadu parametrů pro třídění přístupu, které jsou vysílány v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)) a které musí UE vyhodnotit před jakýmkoli pokusem o přístup, jako je navázání [RRC](/mobilnisite/slovnik/rrc/) spojení. UE tato pravidla aplikuje lokálně, čímž zabraňuje záplavě pokusů o přístup, která by mohla způsobit kolaps zahlcené nebo se zotavující sítě.

Tento rámec sjednocuje několik dříve samostatných mechanismů třídění přístupu. Základními komponentami jsou třídění přístupu podle přístupových tříd (ACB), které třídí přístup UE na základě náhodně přiřazené přístupové třídy (0-9, s 10-15 pro vyšší prioritu); řízení přístupu specifické pro služby ([SSAC](/mobilnisite/slovnik/ssac/)), které uplatňuje specifické faktory třídění pro hlasové a videoslužby multimediální telefonie ([MTSI](/mobilnisite/slovnik/mtsi/)); a rozšířené třídění přístupu ([EAB](/mobilnisite/slovnik/eab/)), které cílí na UE nakonfigurovaná pro nízkou prioritu přístupu (např. zařízení strojového typu). Pro 5G NR byl tento rámec rozšířen o Unified Access Control for NR (UAC-NR), který zavedl řízení založené na přístupové identitě a přístupové kategorii, čímž poskytuje vyšší granularitu. UE určí svou příslušnou přístupovou identitu (např. jako uživatel služby s prioritou multimédií) a přístupovou kategorii zamýšlené služby (např. nouzová, tolerantní k zpoždění, signalizace iniciovaná mobilním zařízením) a poté zkontroluje odpovídající informace o třídění přístupu vysílané sítí.

Když síť zažívá vysoké zatížení, katastrofu nebo poruchu, může operátor sítě dynamicky aktualizovat parametry UAC vysílané v SIB. Například může zakázat přístup všem běžným uživatelům (přístupová třída 0-9) a zároveň povolit přístup k síti záchranným složkám (přístupová třída 14) a personálu sítě (přístupová třída 15). UE provádí pravděpodobnostní kontrolu pomocí vysílaného faktoru třídění a času třídění; pokud je přístup zamítnut, musí před dalším pokusem vyčkat. Tento decentralizovaný řídicí mechanismus je vysoce efektivní, protože zabraňuje zahlcení přístupové sítě zamítnutými požadavky a šetří signalizační prostředky pro povolené přístupy. UAC je proto nezbytný pro udržení dostupnosti sítě, implementaci diferenciace služeb a zajištění prioritního přístupu pro veřejnou bezpečnost a nouzovou komunikaci.

## K čemu slouží

UAC byl vytvořen k řešení kritického problému kolapsu rádiové přístupové sítě v důsledku zahlcení, zejména během hromadných událostí, nouzových stavů nebo poruch sítě. Před zavedením sjednocených mechanismů byly kontroly třídění přístupu roztříštěnější a méně podrobné. UAC poskytuje standardizovaný, sjednocený rámec, který umožňuje operátorům sítí dynamicky řídit příliv pokusů o přístup na základě priority uživatele, typu služby a charakteristik zařízení, čímž chrání stabilitu sítě a zajišťuje dostupnost prostředků pro nejdůležitější komunikaci.

Vývoj směrem k UAC byl motivován potřebou sofistikovanější správy provozu s nástupem neustále připojených chytrých telefonů a masivního nasazení IoT. Jednoduché třídění přístupu podle přístupových tříd z 2G/3G bylo nedostatečné. [SSAC](/mobilnisite/slovnik/ssac/) řešilo specifickou potřebu ochrany hlasových služeb přes LTE (VoLTE) během zahlcení. [EAB](/mobilnisite/slovnik/eab/) bylo zavedeno pro správu potenciální signalizační bouře z milionů zařízení MTC s nízkou prioritou. UAC tyto mechanismy sjednotil pod jediný koncepční rámec, čímž zjednodušil správu sítě a implementaci v UE. Řeší omezení reaktivního řízení zahlcení tím, že poskytuje proaktivní, na vysílání založené kontroly, které jsou aplikovány u zdroje (tj. v UE).

V 5G se účel rozšířil o podporu širšího spektra kategorií definovaných službami, což je v souladu s dělením sítě (network slicing) a různorodými požadavky na QoS. Nový model založený na přístupových identitách a kategoriích umožňuje síti implementovat velmi přesné politiky, jako je povolení přístupu pro konkrétní síťový řez při současném zamítnutí ostatních, nebo upřednostnění provozu pro automatizaci továren před aktualizacemi senzorů. To zajišťuje, že 5G může spolehlivě podporovat jak služby s klíčovým významem, tak služby masivního IoT na sdílené infrastruktuře.

## Klíčové vlastnosti

- Sjednocuje více mechanismů třídění přístupu: ACB, SSAC, EAB a v 5G UAC-NR.
- Řízení orientované na UE založené na parametrech vysílaných v systémových informacích.
- Používá pravděpodobnostní třídění přístupu s faktorem třídění a časem třídění pro rozložení opakovaných pokusů.
- Podporuje prioritní přístup pro specifické přístupové identity (např. záchranné složky, služby s prioritou multimédií).
- Umožňuje služebně specifické třídění přístupu prostřednictvím přístupových kategorií (např. nouzová, tolerantní k zpoždění).
- Klíčový pro odolnost sítě během zahlcení, katastrof a pro správu přístupu masivního IoT.

## Definující specifikace

- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures

---

📖 **Anglický originál a plná specifikace:** [UAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/uac/)
