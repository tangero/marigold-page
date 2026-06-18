---
slug: "e-utra-epc"
url: "/mobilnisite/slovnik/e-utra-epc/"
type: "slovnik"
title: "E-UTRA/EPC – E-UTRA connected to Evolved Packet Core"
date: 2025-01-01
abbr: "E-UTRA/EPC"
fullName: "E-UTRA connected to Evolved Packet Core"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-utra-epc/"
summary: "Tradiční a základní architektura 4G LTE, ve které se LTE rádiová síť (E-UTRA) připojuje k 4G Evolved Packet Core (EPC). Toto je standardní konfigurace pro čisté LTE sítě, poskytující vysokorychlostní"
---

E-UTRA/EPC je základní architektura 4G LTE, ve které se LTE rádiová síť připojuje k 4G Evolved Packet Core a tvoří standardní konfiguraci pro čisté LTE sítě.

## Popis

[E-UTRA](/mobilnisite/slovnik/e-utra/)/EPC představuje standardní a původní systémovou architekturu pro 4G LTE sítě, ve které je rádiová síť Enhanced Universal Terrestrial Radio Access (E-UTRA) připojena k Evolved Packet Core (EPC). V této konfiguraci LTE základnová stanice, známá jako Evolved Node B ([eNB](/mobilnisite/slovnik/enb/)), komunikuje s EPC přes rozhraní S1. Rozhraní S1 je rozděleno na řídicí rovinu ([S1-MME](/mobilnisite/slovnik/s1-mme/)), která spojuje eNB s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro signalizaci, a na uživatelskou rovinu ([S1-U](/mobilnisite/slovnik/s1-u/)), která spojuje eNB se Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)) pro datový provoz. EPC, tvořené MME, S-GW, Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), spravuje mobilitu, správu relací, vynucování politik a propojení s externími paketovými datovými sítěmi (např. internetem). Když se User Equipment (UE) připojí k síti, provede s MME proceduru Attach, která autentizuje účastníka přes HSS a zřídí výchozí přenosový kanál přes S-GW a P-GW. Všechny datové pakety jsou tunelovány pomocí GPRS Tunneling Protocol (GTP) přes rozhraní S1-U a S5/S8. Tato architektura je plně IP a byla navržena pro efektivní paketově orientovanou komunikaci, podporující vysoké datové rychlosti, nízkou latenci a diferenciaci kvality služeb (QoS) pomocí vyhrazených přenosových kanálů. Tvoří páteř komerčních LTE sítí po celém světě a poskytuje konektivitu pro mobilní broadbandové služby. Systém E-UTRA/EPC je definován tak, aby fungoval samostatně, ale slouží také jako kotva pro vyvinuté systémové architektury, jako je E-UTRA/5GC.

## K čemu slouží

E-UTRA/EPC bylo vytvořeno za účelem vytvoření výkonné, plně IP mobilní síťové architektury, která by mohla překonat omezení předchozích systémů 3GPP. Předchozí 3G UMTS sítě používaly složitou hierarchickou architekturu s radiovým síťovým řadičem (RNC) a jádrovou sítí, která stále podporovala okruhově orientovaný přenos hlasu, což bylo pro rostoucí datový provoz neefektivní. Hlavními řešenými problémy byla vysoká latence, architektonická úzká místa na RNC a neschopnost nákladově efektivního škálování pro paketová data. Architektura E-UTRA/EPC byla motivována potřebou zjednodušeného plochého síťového návrhu, který snížil počet síťových prvků v datové cestě, a tím snížil latenci i provozní náklady. Byla od počátku navržena pro podporu pouze paketově orientovaného provozu, optimalizovaného pro internetový protokol a umožňujícího bezproblémovou mobilitu a kontinuitu služeb. Tato architektura umožnila mobilním operátorům uspokojit explozivní poptávku po mobilním broadbandu poháněném chytrými telefony a aplikacemi a poskytla výrazně lepší uživatelský zážitek než 3G. Stanovila standard pro 4G a stala se pracovním koněm pro globální mobilní konektivitu po více než desetiletí.

## Klíčové vlastnosti

- Plochá architektura s eNB připojeným přímo k EPC přes rozhraní S1
- Plně IP paketově orientovaná síť využívající GTP pro tunelování
- Oddělení řídicí roviny (S1-MME k MME) a uživatelské roviny (S1-U k S-GW)
- Podpora QoS prostřednictvím vyhrazených přenosových kanálů a QoS Class Identifiers (QCIs)
- Efektivní správa mobility v rámci LTE a při přechodech do/z 3G/2G sítí
- Základní architektura pro samostatný provoz LTE sítě

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [E-UTRA/EPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-utra-epc/)
