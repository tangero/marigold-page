---
slug: "sari"
url: "/mobilnisite/slovnik/sari/"
type: "slovnik"
title: "SARI – Service Area Restriction Information"
date: 2025-01-01
abbr: "SARI"
fullName: "Service Area Restriction Information"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sari/"
summary: "Sada dat používaná 5G Core Network pro řízení, kde je uživatelskému zařízení (UE) povoleno získávat službu. Definuje povolené a nepovolené sledovací oblasti (tracking areas), čímž brání přístupu v ome"
---

SARI je datová sada 3GPP, která definuje povolené a nepovolené sledovací oblasti (tracking areas) za účelem řízení, kde je uživatelskému zařízení (User Equipment) povoleno získávat službu.

## Popis

Service Area Restriction Information (SARI) je parametr politiky (policy) specifický pro účastníka nebo relaci v 5G systému (5GS). Spravuje jej funkce Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) jako součást předplatitelských dat uživatele a je poskytována funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) během procedur registrace a zřizování relace. SARI obsahuje dva primární seznamy: Povolenou oblast (Allowed Area) a Nepovolenou oblast (Non-Allowed Area), z nichž každý je složen z identifikátorů sledovacích oblastí (Tracking Area Identities, TAIs). AMF tyto informace používá k vynucení pohybových omezení tím, že povoluje nebo zamítá registrace, žádosti o službu a předání spojení (handover) na základě aktuální nebo cílové polohy UE.

Z architektonického hlediska je SARI šířeno klíčovými 5G rozhraními. UDM jej zahrnuje do odpovědí služby Nudm_SubscriberDataManagement směrem k AMF. AMF následně vyhodnocuje aktuální [TAI](/mobilnisite/slovnik/tai/) UE vůči SARI. Pokud se UE nachází v Nepovolené oblasti, může AMF zamítnout registraci s příslušným kódem příčiny (cause code), čímž službu efektivně zablokuje. Pro probíhající relaci, pokud se UE přesune do Nepovolené oblasti, může AMF iniciovat síťově iniciované odregistrování (network-initiated deregistration) nebo upravit [PDU](/mobilnisite/slovnik/pdu/) relaci. Tato politika může být také uplatněna na úrovni síťového řezu (Network Slice), což umožňuje různá omezení služební oblasti pro různé řezy přiřazené stejnému UE.

Jak to funguje, zahrnuje přesnou koordinaci mezi procedurami aktualizace polohy UE a vynucováním politiky AMF. Když UE provede Registrační žádost (Registration Request) nebo Periodickou aktualizaci registrace (Periodic Registration Update), AMF obdrží aktuální TAI UE. Načte SARI účastníka (pokud již není v mezipaměti) a provede kontrolu. 'Povolená oblast' (Allowed Area) má přednost; pokud je TAI přítomen v seznamech Povolené i Nepovolené oblasti, je považován za povolený. Tato detailní kontrola umožňuje operátorům definovat komplexní služební pokrytí, například povolit službu pouze v konkrétním městě (Povolená oblast) nebo všude kromě citlivého místa (Nepovolená oblast). SARI je klíčovým nástrojem pro implementaci regulatorních nařízení (např. žádná služba v zabezpečených vládních zařízeních), komerčních dohod (geograficky ohraničené služby) a efektivní izolaci síťových řezů.

## K čemu slouží

SARI bylo zavedeno v 5G, aby poskytlo flexibilnější a výkonnější mechanismus pro geografické řízení služeb, než jaký byl dostupný v předchozích generacích, jako je 4G EPC. Dřívější systémy používaly koncepty jako Zakázané sledovací oblasti (Forbidden Tracking Areas) nebo ekvivalentní omezení založená na poloze, ale často byla méně detailní a nebyly tak plynule integrovány se správou předplatitelských dat a politikami síťového krájení. Vzestup 5G případů užití, jako jsou privátní sítě, síťové krájení pro vertikální odvětví a přísné regulatorní požadavky, vytvořil potřebu přesného, dynamického a na řezy citlivého řízení služební oblasti.

Primární problém, který SARI řeší, je potřeba diferencovaného řízení přístupu na základě geografie. Například továrna zavádějící privátní 5G síň potřebuje zajistit, aby její řez pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) byl přístupný pouze v areálu továrny. Podobně regulátor může vyžadovat, aby byla mobilní služba deaktivována ve věznicích nebo vojenských zónách. SARI poskytuje standardizovaný mechanismus k vynucení těchto politik na úrovni síťového jádra, čímž zabraňuje neoprávněnému přístupu nebo úniku služby mimo definované hranice.

Jeho vytvoření bylo motivováno architektonickým posunem 5G směrem k cloud-nativním, službám založeným rozhraním a explicitní podporou síťového krájení. SARI je klíčovým prvkem umožňujícím izolaci řezů, což různým řezům umožňuje mít nezávislé geografické pokrytí. Také podporuje dynamické aktualizace; operátor může upravit SARI uživatele v [UDM](/mobilnisite/slovnik/udm/) a změna může být zaslána obsluhující [AMF](/mobilnisite/slovnik/amf/), což umožňuje změny služebních oblastí v reálném čase z bezpečnostních nebo provozních důvodů, což bylo v předchozích architekturách obtížnější.

## Klíčové vlastnosti

- Definuje seznamy Povolených a Nepovolených sledovacích oblastí (Tracking Areas) pro detailní kontrolu
- Vynucováno AMF během procedur registrace a mobility
- Integrováno s předplatitelskými daty v UDM
- Podporuje uplatnění na úrovni instance síťového řezu (Network Slice)
- Umožňuje síťově iniciované odregistrování při porušení
- Schopnost dynamické aktualizace prostřednictvím řízení politik (policy control)

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [SARI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sari/)
