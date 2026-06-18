---
slug: "tssf"
url: "/mobilnisite/slovnik/tssf/"
type: "slovnik"
title: "TSSF – Traffic Steering Support Function"
date: 2025-01-01
abbr: "TSSF"
fullName: "Traffic Steering Support Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tssf/"
summary: "Síťová funkce, která pomáhá směrovat uživatelský provoz na příslušné síťové řezy nebo typy přístupu na základě politik. Je klíčová pro umožnění efektivního síťového řezání a správy provozu v 5G, zajiš"
---

TSSF je síťová funkce, která směruje uživatelský provoz na příslušné síťové řezy nebo typy přístupu na základě politik, což umožňuje efektivní správu provozu a optimální poskytování služeb v 5G.

## Popis

Traffic Steering Support Function (TSSF) je funkce jádra sítě zavedená ve specifikaci 3GPP Release 13, původně pro architekturu Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)), a později adaptovaná pro 5G Core (5GC). Jejím hlavním úkolem je interpretovat a vynucovat politiky směrování provozu, které určují, jak mají být směrovány datové toky uživatele. Tyto politiky jsou typicky poskytovány funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a jsou založeny na faktorech, jako jsou data o předplatném, požadavky aplikací, stav sítě a politiky výběru řezu. TSSF funguje jako bod vynucování politik, převádí pravidla směrování na vysoké úrovni na konkrétní instrukce pro jiné síťové funkce, jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)).

Z architektonického hlediska může být TSSF implementována jako samostatná funkce nebo integrována v jiných funkcích řídicí roviny. Rozhraní ke klíčovým prvkům 5GC zajišťuje prostřednictvím standardizovaných referenčních bodů, například N7 k PCF pro příjem politik a N11 k AMF pro mobilitu a kontext relace. Když je zřízena nebo modifikována relace Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)), může se SMF dotázat TSSF, aby určila příslušný Data Network Name ([DNN](/mobilnisite/slovnik/dnn/)), Network Slice Selection Assistance Information ([NSSAI](/mobilnisite/slovnik/nssai/)) nebo typ přístupu (např. 3GPP, non-3GPP). TSSF vyhodnocuje pravidla politik vůči aktuálnímu kontextu relace, profilu účastníka a lokální konfiguraci, aby učinila rozhodnutí o směrování.

Interně se TSSF skládá z úložiště pravidel politik, engine pro porovnávání pravidel a rozhraní pro komunikaci s jinými síťovými funkcemi. Zpracovává pravidla Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), která obsahují informace pro směrování provozu, jako jsou deskriptory výběru trasy. Tyto deskriptory mohou specifikovat priority pro různé instance řezů nebo přístupové technologie. Proces rozhodování TSSF je dynamický, umožňuje úpravy v reálném čase na základě zatížení sítě, mobility uživatele nebo změn požadavků služby. Tato schopnost je zásadní pro realizaci vize 5G síťového řezání, kde je na sdílené fyzické infrastruktuře vytvořeno více logických sítí s odlišnými charakteristikami.

V provozu hraje TSSF klíčovou roli v zajištění služeb od konce do konce. Například pro službu Ultra-Reliable Low-Latency Communication (URLLC) může TSSF směrovat provoz na řez optimalizovaný pro nízkou latenci, případně s využitím specifické konfigurace rádiové přístupové sítě (RAN). Naopak pro aplikaci massive Internet of Things (mIoT) může provoz nasměrovat na řez navržený pro vysokou hustotu připojení a energetickou účinnost. Centralizací logiky směrování provozu TSSF zjednodušuje správu sítě, zvyšuje konzistenci politik a umožňuje automatizované, inteligentní rozdělování provozu v heterogenních síťových prostředích.

## K čemu slouží

TSSF byla vytvořena, aby řešila rostoucí složitost správy provozu v moderních mobilních sítích, zejména s nástupem 5G a síťového řezání. Před jejím zavedením bylo směrování provozu často řešeno ad-hoc prostřednictvím statických konfigurací v síťových prvcích, jako je Gateway GPRS Support Node (GGSN) nebo Packet Data Network Gateway (PGW). Tento přístup postrádal dynamiku a granularitu potřebnou pro podporu různorodých 5G služeb s přísnými a různorodými požadavky na latenci, šířku pásma a spolehlivost. Omezení předchozích systémů se stala zřejmými, když operátoři usilovali o poskytování diferencovaných služeb, jako je enhanced mobile broadband (eMBB), kritické komunikace a IoT, na společné infrastruktuře.

Hlavní motivací pro vývoj TSSF bylo poskytnout standardizovaný, politikami řízený mechanismus pro inteligentní směrování provozu. Řeší problém, jak automaticky a efektivně nasměrovat datové toky uživatele na nejvhodnější síťové prostředky na základě podmínek v reálném čase a smluv o úrovni služeb (SLA). To je nezbytné pro síťové řezání, které je základním kamenem 5G a umožňuje vytváření více virtuálních sítí na jedné fyzické platformě. Bez specializované funkce, jako je TSSF, by implementace a správa směrování provozu specifického pro řez byla těžkopádná, náchylná k chybám a obtížně škálovatelná.

Historicky se koncept vyvinul z dřívějších rámců pro řízení politik definovaných v 3GPP, jako je architektura Policy and Charging Control (PCC). Release 13 původně specifikovalo TSSF v kontextu SCEF pro optimalizace Cellular IoT (CIoT), se zaměřením na směrování ne-IP dat. S přechodem na Service-Based Architecture (SBA) v Release 15 byla její role rozšířena a integrována do 5GC pro správu směrování všech typů PDU relací napříč řezy a typy přístupu. TSSF tak představuje vyzrání řízení politik, vyvíjející se od jednoduchého vynucování tarifování a kvality služeb (QoS) k zahrnutí sofistikované, kontextově-aware orchestrace provozu, která je klíčová pro poskytování slibované flexibility a účinnosti 5G sítí.

## Klíčové vlastnosti

- Směrování provozu na základě politik pro síťové řezy a typy přístupu
- Integrace s funkcí 5G Policy Control Function (PCF) přes rozhraní N7
- Podpora dynamických rozhodnutí o směrování na základě kontextu relace v reálném čase
- Umožňuje efektivní využití prostředků a směrování specifické pro službu
- Usnadňuje automatický výběr a správu síťových řezů
- Poskytuje standardizovanou funkci pro konzistentní orchestrace provozu v 5GC

## Související pojmy

- [NSSAI – Network Slice Selection Assistance Information](/mobilnisite/slovnik/nssai/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 29.155** (Rel-19) — REST-based St Reference Point Protocol
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [TSSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tssf/)
