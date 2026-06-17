---
slug: "hsp"
url: "/mobilnisite/slovnik/hsp/"
type: "slovnik"
title: "HSP – High Speed Protocol"
date: 2025-01-01
abbr: "HSP"
fullName: "High Speed Protocol"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hsp/"
summary: "Bezpečnostní protokol definovaný v 3GPP pro zabezpečení přenosů vysokorychlostních dat, zejména pro zákonný odposlech (Lawful Interception, LI) a podobné aplikace. Zajišťuje integritu, důvěrnost a spo"
---

HSP je bezpečnostní protokol 3GPP zajišťující integritu, důvěrnost a spolehlivé doručení odposlechnutých dat, například pro zákonný odposlech (Lawful Interception), mezi síťovými funkcemi a sběrnými systémy.

## Popis

Protokol High Speed Protocol (HSP) je standardizovaný protokol v rámci bezpečnostní architektury 3GPP, specifikovaný primárně v TS 33.224. Je navržen tak, aby umožňoval zabezpečený, spolehlivý a vysoce výkonný přenos odposlechnutého komunikačního obsahu a s ním souvisejících informací o odposlechu (Intercept-Related Information, [IRI](/mobilnisite/slovnik/iri/)) ze síťových prvků, jako je Packet Data Network Gateway (PGW) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), k mediační nebo sběrné funkci pro zákonný odposlech (Lawful Interception, [LI](/mobilnisite/slovnik/li/)). Protokol funguje nad TCP/IP a je konstruován pro zpracování velkých objemů dat s minimální latencí a vysokou propustností, což je klíčové pro scénáře odposlechu v reálném čase v moderních sítích s vysokou šířkou pásma.

Z architektonického hlediska HSP definuje model klient-server, kde síťový prvek generující data z odposlechu funguje jako klient HSP a zařízení orgánu činného v trestním řízení (Law Enforcement Monitoring Facility, [LEMF](/mobilnisite/slovnik/lemf/)) nebo mediační zařízení funguje jako server HSP. Protokol specifikuje formáty zpráv, procedury navázání relace a mechanismy pro řízení toku a obnovu po chybě. Podporuje přenos jak obsahu komunikace (Content of Communication, [CC](/mobilnisite/slovnik/cc/)), což jsou vlastní uživatelská data (např. hlasové pakety, IP toky), tak informací souvisejících s odposlechem (Intercept-Related Information, IRI), což jsou metadata o komunikaci (např. podrobnosti o volání, poloha). Ty jsou doručovány na samostatných logických kanálech v rámci relace HSP, aby umožňovaly diferencované zacházení a stanovení priorit.

Klíčové komponenty zásobníku protokolu HSP zahrnují vrstvu správy spojení pro navazování a udržování zabezpečených TCP spojení, vrstvu formátování zpráv pro strukturování užitečného zatížení IRI a CC podle standardů 3GPP a bezpečnostní vrstvu, která vyžaduje použití TLS (Transport Layer Security) pro zajištění důvěrnosti a integrity přenášených odposlechnutých dat. Jeho role je klíčová pro soulad s právními požadavky na telekomunikační dohled, neboť zajišťuje, že odposlechnutá data jsou přesně, kompletně a bezpečně doručena ze sítě operátora k oprávněnému orgánu činnému v trestním řízení, aniž by to ovlivnilo výkon nebo integritu komerčních síťových služeb.

## K čemu slouží

HSP byl vytvořen, aby řešil specifické výzvy zákonného odposlechu (Lawful Interception, [LI](/mobilnisite/slovnik/li/)) v rozvíjejících se paketových sítích 3GPP. Předchozí metody pro doručování odposlechnutých dat byly často závislé na dodavateli, postrádaly standardizované mechanismy pro vysokovýkonný přenos a nedokázaly držet krok s rostoucími datovými rychlostmi nabízenými technologiemi jako [HSPA](/mobilnisite/slovnik/hspa/) a LTE. Rozšíření služeb s vysokou šířkou pásma, jako je streamování videa a stahování velkých souborů, si vyžádalo standardizovaný protokol schopný zvládnout vysokoobjemové datové toky v reálném čase od síťových uzlů k systémům pro sběr odposlechů, aniž by se stal úzkým hrdlem.

Protokol řeší problém zabezpečeného a spolehlivého hromadného doručování dat pro účely odposlechu. Poskytuje společné rozhraní, které zajišťuje interoperabilitu mezi zařízeními od různých dodavatelů sítí a systémů pro orgány činné v trestním řízení, což je klíčový regulační požadavek v mnoha jurisdikcích. Specifikací robustního přenosového mechanismu s vestavěným zabezpečením (TLS), řízením toku a zpracováním chyb HSP zajišťuje integritu a úplnost řetězce důkazů, což je prvořadé pro jejich přípustnost před soudem. Jeho vytvoření bylo motivováno potřebou modernizovat schopnosti odposlechu v souladu s architekturou 3GPP založenou výhradně na IP, což znamená posun od zastaralých modelů odposlechu v okruhově přepínaných sítích ke škálovatelnému, paketově orientovanému rámci vhodnému pro éru vysokorychlostního internetu.

## Klíčové vlastnosti

- Standardizovaný přenos dat pro zákonný odposlech (IRI a CC)
- Architektura klient-server nad TCP/IP
- Povinné použití TLS pro důvěrnost a integritu
- Podpora doručování dat s vysokou propustností a nízkou latencí
- Samostatné logické kanály pro informace související s odposlechem (IRI) a obsah komunikace (CC)
- Definované procedury pro správu relací, řízení toku a obnovu po chybě

## Definující specifikace

- **TS 33.224** (Rel-19) — Generic Push Layer (GPL) Specification

---

📖 **Anglický originál a plná specifikace:** [HSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsp/)
