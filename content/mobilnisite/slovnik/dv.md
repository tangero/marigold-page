---
slug: "dv"
url: "/mobilnisite/slovnik/dv/"
type: "slovnik"
title: "DV – Data Volume"
date: 2025-01-01
abbr: "DV"
fullName: "Data Volume"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dv/"
summary: "Kvantifikovatelná metrika reprezentující celkový objem uživatelských dat přenesených nebo přijatých přes síťové spojení v určitém kontextu, například v PDU Session, QoS Flow nebo reportovacím interval"
---

DV je kvantifikovatelná metrika reprezentující celkový objem uživatelských dat přenesených nebo přijatých přes síťové spojení v určitém kontextu.

## Popis

Data Volume (DV) je základní měřící parametr v systémech 3GPP označující agregovaný objem dat přenesených v uživatelské rovině. Měří se v oktetech (bytách) a počítá se odděleně pro směr uplink (od UE do síťe) a downlink (od síťe do UE). Kontext měření DV je přesně definován: může být spojen s konkrétní Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) Session, s dedikovaným QoS Flow v rámci session, s service data flow ([SDF](/mobilnisite/slovnik/sdf/)) identifikovaným pomocí packet filtrů, nebo i s celým subscriberem. Počítání provádí síťové funkce, které zpracovávají provoz v uživatelské rovině, primárně User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core a Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN)/Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC.

Technický proces zahrnuje, že counting node kontroluje pakety při jejich přenosu. Pro každý paket odpovídající definovanému měřícímu kontextu (například patřící do konkrétní PDU Session a QoS Flow) node inkrementuje odpovídající DV counter o počet oktetů v payloadu paketu (vyjma specifických headerů pro danou vrstvu, jako [GTP-U](/mobilnisite/slovnik/gtp-u/), [UDP](/mobilnisite/slovnik/udp/)/IP). Tyto countery jsou typicky udržovány v reálném časem. Informace o DV je pak využívána několika způsoby. Pro účtování může [SMF](/mobilnisite/slovnik/smf/) (nebo PGW-C v EPC) požadovat reporty od UPF (nebo PGW-U) obsahující využitý DV, který je pak formátován do Charging Data Records (CDR) pro offline účtování nebo použit pro online credit control. Pro řízení politik může Policy Control Function (PCF) nastavit usage monitoring thresholds; když DV dosáhne thresholdu, SMF je notifikována, aby případně triggerovala policy akce, jako snížení datových rychlostí.

DV reporting může být event-triggered (například při ukončení session, při dosažení kvóty) nebo periodický. Granularita měření DV je klíčový aspekt síťového managementu. Umožňuje volume-based charging tiers, fair usage policies a detailní analytiku síťových traffic patterns. V pokročilých deploymentech může DV být také korelována s slice-specific usage pro účtování a plánování kapacity v network slicing.

## K čemu slouží

Koncept Data Volume byl integrální od zavedení packet-switched služeb, ale jeho formalizace a granularní aplikace se rozvíjely s potřebou sofistikované service differentiation a monetizace. Rané GPRS/UMTS síťe používaly DV primárně pro jednoduché bulk charging. Avšak s příchodem flat-rate data plans, streaming služeb a IoT, operátorům bylo potřebné finer-grained visibility a control nad datovým využitím.

DV jako standardizovaná metrika, zejména zdůrazňovaná od 3GPP Release 16 v kontextech jako enhanced coverage a UAV support, řeší potřebu přesného, context-aware usage accounting. Řeší problém jak účtovat různé služby (například účtovat jinak mission-critical IoT data vs. mobile broadband) a jak enforce fair usage policies bez prostého blokování přístupu. Spojením DV s specifickými QoS Flow nebo síťovými slices umožňuje business modely pro 5G, jako network-as-a-service, kde billing může být based na objemu guaranteed-bit-rate traffic. Poskytuje kvantitativní základ pro policy and charging control (PCC) architekturu.

## Klíčové vlastnosti

- Měří se v oktetech, s oddělenými countery pro směry uplink a downlink.
- Počítá se v specifických kontextech: per PDU Session, per QoS Flow, per SDF nebo per UE.
- Primární měřící bod je user plane gateway (UPF v 5GC, PGW-U v EPC).
- Napájí Charging Data Records (CDR) pro offline charging a online credit control.
- Integruje se s Policy and Charging Control (PCC) pro usage monitoring a enforcement politik.
- Podporuje event-triggered a periodic reporting do control plane funkcí (SMF, PCF).

## Definující specifikace

- **TR 22.882** (Rel-19) — Study on Energy Efficiency as a Service Criteria
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks

---

📖 **Anglický originál a plná specifikace:** [DV na 3GPP Explorer](https://3gpp-explorer.com/glossary/dv/)
