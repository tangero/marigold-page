---
slug: "kpas"
url: "/mobilnisite/slovnik/kpas/"
type: "slovnik"
title: "KPAS – Korean Public Alert System"
date: 2026-01-01
abbr: "KPAS"
fullName: "Korean Public Alert System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/kpas/"
summary: "Varovný systém definovaný 3GPP pro doručování zpráv o veřejné bezpečnosti mobilním uživatelům v Jižní Koreji. Využívá službu Cell Broadcast Service (CBS) k vysílání geograficky cílených nouzových zprá"
---

KPAS je korejský systém veřejného varování definovaný 3GPP, který využívá službu Cell Broadcast Service k doručování geograficky cílených nouzových zpráv, jako jsou varování před přírodními katastrofami, na všechna kompatibilní mobilní zařízení v postižených buňkách.

## Popis

Korean Public Alert System (KPAS) je konkrétní implementace a profil rámců Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)) a Earthquake and Tsunami Warning System (ETWS) od 3GPP, přizpůsobená tak, aby splňovala regulatorní požadavky na veřejné varování v Jižní Koreji. Funguje jako síťová vysílací služba pro mobilní zařízení, kde jsou varovné zprávy vloženy do síťového jádra a poté současně rozeslány na všechna uživatelská zařízení (UE) v jedné nebo více určených oblastech pro vysílání v buňkách. Architektura zahrnuje Cell Broadcast Center ([CBC](/mobilnisite/slovnik/cbc/)), které přijímá výstrahy od vládního poskytovatele varování, formátuje je podle specifikací 3GPP a předává je příslušným základnovým stanicím (eNodeB v LTE, gNB v NR) přes rozhraní CBC-RAN (např. SBC-AP).

Jak KPAS funguje: Začíná generováním výstrahy autorizovaným vládním subjektem. Tato výstraha, obsahující text zprávy a cílové geografické oblasti, je odeslána do CBC síťového operátora. CBC mapuje geografickou oblast na seznam Cell ID a vytvoří Cell Broadcast Message. Tato zpráva obsahuje specifické identifikátory zpráv a sériová čísla definovaná pro KPAS, aby se odlišila od ostatních CBS zpráv. CBC poté tuto zprávu odešle základnovým stanicím obsluhujícím cílové buňky pomocí příslušného protokolu Radio Access Network (RAN). Základnové stanice vysílají zprávu přes rozhraní vzduch pomocí systémových informačních bloků (např. SIB12 v LTE, SIB12 v NR) na vyhrazeném logickém kanálu ([CTCH](/mobilnisite/slovnik/ctch/)). Kompatibilní UE, která tato vysílání průběžně monitorují, zprávu přijmou a dekódují a zobrazí ji uživateli s vysokou prioritou, často doprovázenou specifickým zvukem a vibracemi.

Klíčové komponenty KPAS zahrnují Warning Provider (korejské vládní agentury), Cell Broadcast Center (CBC), Core Network ([MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/) pro směrování řídicí roviny), RAN (eNodeB/gNB) a UE s podporou KPAS. Role systému je poskytnout rychlou, spolehlivou a nekongestní metodu hromadného varování, protože využívá vysílací kanál nezávislý na point-to-point provozu. Technické specifikace zajišťují integritu zprávy, zabraňují podvržení a umožňují aktualizace a zrušení zpráv. Zprávy KPAS jsou definovány specifickými kódy a formáty ve specifikacích 3GPP, aby byla zajištěna interoperabilita mezi různými síťovými operátory a výrobci mobilních zařízení v Koreji, což z něj činí kritickou službu národní veřejné bezpečnosti.

## K čemu slouží

KPAS byl vytvořen k naplnění národního regulatorního mandátu v Jižní Koreji pro spolehlivý a okamžitý systém veřejného varování prostřednictvím mobilních sítí. Primární problém, který řeší, je potřeba rychle informovat celou populaci nebo geograficky cílenou její část o bezprostředních hrozbách, jako jsou zemětřesení, tsunami, tajfuny, civilní nouzové situace nebo upozornění na únos dětí (AMBER alerty). Tradiční metody varování jako sirény, TV nebo rádio mají omezení v dosahu, okamžitosti a přesnosti cílení. Systémy varování založené na SMS mohou během mimořádných událostí způsobovat zahlcení sítě a zpoždění.

Motivací pro standardizaci KPAS v rámci 3GPP bylo zajistit konzistentní a interoperabilní technickou implementaci napříč všemi korejskými mobilními operátory s využitím stávajících mechanismů 3GPP [CBS](/mobilnisite/slovnik/cbs/)/ETWS. Před takovou standardizací mohly proprietární nebo neinteroperabilní systémy vést k fragmentovanému pokrytí a nekonzistentní uživatelské zkušenosti. Přijetím a profilováním standardů 3GPP KPAS zajišťuje, že jakýkoli kompatibilní mobilní telefon, bez ohledu na výrobce nebo operátora, může tyto kritické výstrahy přijímat a zobrazovat. Odstraňuje tak omezení předchozích ad-hoc přístupů tím, že poskytuje standardizovaný, sítí řízený vysílací mechanismus, který není ovlivněn zatížením provozu, a zajišťuje doručení výstrah během sekund na všechna zařízení v cílové zóně, včetně těch, která nejsou právě zapojena do hovoru nebo datové relace.

## Klíčové vlastnosti

- Geograficky cílené vysílání nouzových výstrah na všechna UE v buňce
- Využívá službu Cell Broadcast Service (CBS) a rámec ETWS
- Definuje jedinečné identifikátory zpráv a formáty pro korejská varování
- Vysokoprioritní zobrazení na UE s charakteristickými zvukovými/vizuálními signály
- Síťové vysílání se vyhne zahlcení signalizace
- Podporuje procedury aktualizace a zrušení zpráv

## Související pojmy

- [CBS – Cell Broadcast Service](/mobilnisite/slovnik/cbs/)

## Definující specifikace

- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [KPAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/kpas/)
