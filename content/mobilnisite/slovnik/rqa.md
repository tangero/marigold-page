---
slug: "rqa"
url: "/mobilnisite/slovnik/rqa/"
type: "slovnik"
title: "RQA – Reflective QoS Attribute"
date: 2026-01-01
abbr: "RQA"
fullName: "Reflective QoS Attribute"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rqa/"
summary: "Atribut QoS používaný v 5G pro povolení Reflexivní QoS. Je přenášen ve zprávě PDU Session Establishment Accept ze SMF do UE. Signalizuje, že tok QoS podléhá reflexivní kvalitě služeb, což umožňuje UE"
---

RQA je atribut kvality služeb signalizovaný ve zprávě PDU Session Establishment Accept, který označuje, že tok QoS podléhá reflexivní kvalitě služeb, což umožňuje UE odvodit pravidla pro uplink z downlinkového provozu.

## Popis

Reflective QoS Attribute (RQA) je základní parametr v rámci architektury kvality služeb (QoS) 5G, který je specificky navržen pro podporu mechanismu Reflexivní QoS. Je definován jako atribut QoS přidružený k toku QoS. RQA je zřizován funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) a je odeslán do uživatelského zařízení (UE) ve zprávě [PDU](/mobilnisite/slovnik/pdu/) Session Establishment Accept (nebo v následné zprávě PDU Session Modification) jako součást pravidla (pravidel) QoS pro konkrétní tok QoS. Přítomnost RQA pro daný tok QoS explicitně instruuje UE, že tento tok je nakonfigurován pro provoz v režimu Reflexivní QoS.

Z architektonického hlediska je RQA prvek řídicí roviny, který sídlí v profilu QoS spravovaném SMF. Když SMF určí, že tok QoS má využívat Reflexivní QoS – často pro aplikace se symetrickými požadavky na uplink a downlink, jako je VoIP (Voice over IP) nebo služby reálného času – zahrne RQA do pravidla QoS odeslaného do UE přes funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). Charakteristiky 5G QoS ([5QI](/mobilnisite/slovnik/5qi/)) pro daný tok jsou na straně UE již známy, ale RQA poskytuje konkrétní autorizaci pro aplikaci procesu reflexivního odvozování.

Jeho funkce je vnitřně propojena s Reflective QoS Indication ([RQI](/mobilnisite/slovnik/rqi/)). Když downlinkový paket pro tok QoS označený RQA dorazí do UE, může [UPF](/mobilnisite/slovnik/upf/) (User Plane Function) nebo gNB nastavit bit RQI v zapouzdřovací hlavičce paketu (např. v [GTP-U](/mobilnisite/slovnik/gtp-u/) extension header nebo v poli [QFI](/mobilnisite/slovnik/qfi/)). Uživatelská rovina UE tento paket označený RQI detekuje. Přítomnost RQI v uživatelské rovině v kombinaci s předchozí autorizací signalizovanou RQA v řídicí rovině spustí v UE vytvoření nebo aktualizaci pravidla uplinkové QoS. Toto pravidlo zrcadlí charakteristiky QoS (jako 5QI, ARP, session-AMBR) downlinkového toku, čímž efektivně odvozuje uplinkovou politiku z pozorovaného downlinkového provozu bez nutnosti průběžné signalizace v jádru sítě.

Jeho role v síti spočívá v umožnění efektivního, dynamického a na aplikaci zaměřeného řízení QoS. Snižuje signalizační režii mezi UE a jádrem sítě (konkrétně SMF) automatizací nastavení symetrických toků QoS. To je klíčové pro podporu služeb s nízkou latencí a síťového dělení (network slicing), kde je vyžadována rychlá adaptace na potřeby aplikace. RQA funguje jako základní povolovací listina, zatímco RQI poskytuje spouštěč v reálném čase; společně tak tvoří uzavřený regulační okruh pro reflexivní řízení QoS v uživatelské rovině.

## K čemu slouží

RQA bylo vytvořeno za účelem řešení neefektivit tradičních, čistě síťově zřizovaných modelů QoS při zpracování dynamických, symetrických vzorců provozu. Před 5G byla uplinková pravidla QoS typicky stanovována explicitně prostřednictvím signalizace řídicí roviny ze sítě (např. pravidla PCC z PCRF/PCF). Pro aplikace jako konverzační video nebo hraní her, kde se požadavky na uplink a downlink objevují současně se zahájením relace, by toto mohlo zavádět zpoždění při nastavování a generovat významnou signalizační zátěž, zejména při častém přidávání nebo modifikaci toků.

Motivace pro RQA a širší koncept Reflexivní QoS vychází z potřeby rychlejší a škálovatelnější aktivace QoS. Systém 5G si klade za cíl podporovat masivní počet zařízení a rozmanité požadavky služeb, včetně těch definovaných pro Ultra-Reliable Low-Latency Communication (URLLC). Explicitní signalizace pro každý symetrický tok by se stala úzkým hrdlem. Reflexivní QoS, autorizovaná pomocí RQA, umožňuje UE jednat autonomně na základě podnětů ze sítě (RQI), což dramaticky snižuje latenci při nastavování toků a snižuje zatížení řídicí roviny.

Historicky byla QoS plně pod kontrolou sítě. Zavedení RQA ve specifikaci 3GPP Release 15 představuje posun paradigmatu směrem k modelu s distribuovanější inteligencí. Poskytuje UE omezenou, síťově autorizovanou rozhodovací schopnost pro QoS. Tím řeší problém rychlé reakce na požadavky aplikací a je klíčovým prvkem pro síťové dělení (network slicing), kde různé řezy mohou používat různé strategie QoS, včetně reflexivních metod pro zvýšení efektivity.

## Klíčové vlastnosti

- Autorizuje tok QoS pro provoz v režimu Reflexivní QoS.
- Je zřizován SMF a doručen do UE prostřednictvím NAS signalizace.
- Je přidružen ke konkrétnímu pravidlu QoS v rámci PDU relace.
- Funguje v součinnosti se značkou RQI v uživatelské rovině.
- Snižuje potřebu explicitní signalizace mezi SMF a UE pro nastavení symetrických toků.
- Umožňuje UE autonomně odvozovat pravidla uplinkové QoS.

## Související pojmy

- [RQI – Reflective QoS Indication](/mobilnisite/slovnik/rqi/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [RQA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rqa/)
