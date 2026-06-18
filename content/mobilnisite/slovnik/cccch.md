---
slug: "cccch"
url: "/mobilnisite/slovnik/cccch/"
type: "slovnik"
title: "CCCCH – Compact Common Control Channel"
date: 2025-01-01
abbr: "CCCCH"
fullName: "Compact Common Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cccch/"
summary: "CCCCH je logický kanál v sítích GPRS/EDGE, který přenáší signalizaci společného řízení mezi sítí a mobilními zařízeními. Jde o kompaktní verzi kanálu CCCH optimalizovanou pro efektivní využívání prost"
---

CCCCH je kompaktní logický kanál v sítích GPRS/EDGE, který přenáší signalizaci společného řízení pro efektivní počáteční přístup k síti, paging a vysílání systémových informací.

## Popis

Compact Common Control Channel (CCCCH) je logický kanál definovaný v architektuře protokolů rozhraní [GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/), konkrétně v rámci vrstvy Radio Link Control/Medium Access Control ([RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/)) podle specifikace 3GPP TS 44.060. Jako logický kanál neodpovídá specifickému fyzickému prostředku, ale definuje typ přenášené informace po fyzických kanálech. CCCCH pracuje v uplink směru od mobilních stanic k síti a přenáší signalizaci společného řízení, která nevyžaduje vyhrazené prostředky.

Z architektonického hlediska se CCCCH nachází ve vrstvách nad fyzickou vrstvou a pod vrstvou RLC/MAC. Je mapován na konkrétní fyzické prostředky známé jako Packet Common Control Channels ([PCCCH](/mobilnisite/slovnik/pccch/)), pokud jsou dostupné, nebo na stávající kanály společného řízení ([CCCH](/mobilnisite/slovnik/ccch/)) v GSM, pokud PCCCH není zaveden. Kanál využívá proceduru náhodného přístupu založenou na mechanismu slotted Aloha, kdy mobilní stanice vysílají přístupové výbuchy obsahující jejich požadavky. Tyto výbuchy zahrnují klíčové informace, jako je identita mobilního zařízení, typ požadované služby a náhodné referenční číslo pro řešení kolizí.

CCCCH přenáší několik typů řídicích zpráv včetně zpráv Packet Channel Request, Packet Resource Request a Packet Paging Response. Kanál využívá soutěživý mechanismus přístupu, při kterém může více mobilních stanic současně zkoušet získat přístup k síti, což vyžaduje procedury detekce a řešení kolizí. Síť reaguje na přenosy po CCCCH alokací vyhrazených prostředků nebo poskytnutím potřebných řídicích informací prostřednictvím downlink kanálů. Tento kanál je obzvláště důležitý během počáteční fáze navazování paketové datové relace, kdy mobilní zařízení přechází z klidového do aktivního stavu.

Klíčové komponenty fungování CCCCH zahrnují strukturu přístupového výbuchu, mechanismy časového předstihu a procedury řízení výkonu. Kanál používá specifické tréninkové sekvence optimalizované pro detekci ve scénářích náhodného přístupu a zahrnuje mechanismy pro zvládání různých podmínek šíření. Operátoři mohou konfigurovat parametry CCCCH, jako jsou úrovně perzistence přístupu, maximální počet pokusů o opakovaný přenos a časovací parametry, aby optimalizovali výkon podle charakterů provozu a podmínek zatížení sítě.

## K čemu slouží

CCCCH byl vytvořen k řešení specifických požadavků paketově orientovaných datových služeb v sítích [GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/), které se výrazně lišily od tradičních služeb přepojování okruhů pro hlas. Před GPRS používaly sítě GSM pro veškerou signalizaci společného řízení kanál CCCH, ale tento přístup nebyl optimalizovaný pro přerušovanou, "bursty" povahu paketového datového provozu. Stávající mechanismy CCCH byly navrženy primárně pro zřizování hlasových hovorů a neefektivně zvládaly časté, malé datové přenosy charakteristické pro rané mobilní datové aplikace.

Primárním motivem pro zavedení CCCCH bylo poskytnutí efektivnějšího řídicího kanálu specificky přizpůsobeného pro datové služby. Tradiční procedury CCCH zahrnovaly poměrně dlouhé signalizační výměny, které vytvářely zbytečnou režii pro paketové datové relace. CCCCH zavedl optimalizace, jako jsou kratší formáty zpráv, rychlejší přístupové procedury a lepší zvládání soutěživých scénářů běžných v datových sítích. To bylo obzvláště důležité, když mobilní operátoři začali zavádět služby GPRS vedle stávajících GSM hlasových sítí, což vyžadovalo efektivní souběžné fungování obou typů služeb.

CCCCH vyřešil několik konkrétních problémů: snížil signalizační režii pro paketové datové relace, zlepšil úspěšnost přístupu při přetížených podmínkách a umožnil rychlejší přechod z klidového do aktivního stavu pro datové služby. Optimalizací řídicí signalizace pro přepojování paketů pomohl CCCCH učinit sítě GPRS/EDGE efektivnějšími a citlivějšími, čímž podpořil rostoucí poptávku po mobilních datových službách na konci 90. let a začátku 21. století. Návrh kanálu také usnadnil vývoj směrem k pokročilejším systémům paketových dat, které se nakonec staly sítěmi 3G a 4G.

## Klíčové vlastnosti

- Optimalizován pro procedury přístupu paketových dat
- Používá mechanismus náhodného přístupu typu slotted Aloha
- Přenáší zprávy Packet Channel Request a Resource Request
- Podporuje řešení kolizí pomocí náhodných referenčních čísel
- Je mapován na prostředky PCCCH nebo stávající GSM CCCH
- Používá přístupové výbuchy se specifickými tréninkovými sekvencemi

## Související pojmy

- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [PCCCH – Packet Common Control Channel](/mobilnisite/slovnik/pccch/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CCCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cccch/)
