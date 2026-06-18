---
slug: "tsdt"
url: "/mobilnisite/slovnik/tsdt/"
type: "slovnik"
title: "TSDT – Transport Stream Description Table"
date: 2025-01-01
abbr: "TSDT"
fullName: "Transport Stream Description Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tsdt/"
summary: "Transport Stream Description Table (TSDT) je metadatová struktura definovaná 3GPP pro popis multimediálních vysílacích a skupinových služeb (MBMS). Poskytuje základní informace o transportním proudu,"
---

TSDT je metadatová struktura definovaná 3GPP pro MBMS, která poskytuje základní informace o transportním proudu, jako jsou seznamy služeb a podrobnosti o komponentách, aby umožnila efektivní doručování a příjem vysílaného obsahu přes mobilní sítě.

## Popis

Transport Stream Description Table (TSDT) je klíčovou součástí architektury služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) dle 3GPP, konkrétně definovanou pro doručování vysílaného a skupinového obsahu. Funguje jako kontejner metadat, který popisuje strukturu a složení digitálního transportního proudu přenášejícího jednu či více multimediálních služeb. TSDT je přenášena v rámci nosiče MBMS a klientská zařízení, jako je User Equipment (UE), ji využívají k efektivnímu objevování a přístupu k dostupným vysílacím službám. Jejím hlavním úkolem je poskytovat na transportní vrstvě funkci podobnou průvodci službami, což umožňuje UE analyzovat proud a identifikovat jednotlivé komponenty služby (např. audio, video, časované titulky) bez nutnosti předchozí signalizace mimo přenosový pásmo.

Z architektonického hlediska TSDT generuje a vkládá do transportního proudu Broadcast Multicast Service Centre ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťová entita odpovědná za poskytování a doručování služeb MBMS. Tato tabulka dodržuje specifickou syntaxi a sémantiku definovanou v 3GPP TS 26.917, což zajišťuje interoperabilitu mezi síťovým zařízením a přijímacími zařízeními. Typicky obsahuje deskriptory, které uvádějí služby v rámci proudu, mapují identifikátory služeb na konkrétní Packet Identifiers ([PID](/mobilnisite/slovnik/pid/)) elementárních proudů a poskytují informace o komponentách služeb, jako jsou jejich typy médií a kódovací formáty. To umožňuje UE, která se naladí na vysílací frekvenci nebo nosič MBMS, rychle dekódovat TSDT, pochopit, jaké služby jsou dostupné, a vybrat požadované audio/video komponenty pro dekódování a prezentaci.

Fungování TSDT je nedílnou součástí uživatelské služby MBMS 'Streaming Delivery'. Když UE aktivuje příjem MBMS, nejprve získá parametry fyzické a transportní vrstvy. Po úspěšné demodulaci a dekódování paketů transportního proudu UE vyhledává sekce obsahující TSDT. Tabulka je přenášena periodicky, aby umožnila novým zařízením připojit se k vysílací relaci kdykoli. Analýzou TSDT si UE vytvoří interní mapu nabídky služeb. Například se dozví, že PID 101 nese video komponentu pro 'Službu A' kódovanou pomocí H.264/[AVC](/mobilnisite/slovnik/avc/), PID 102 nese odpovídající audio [AAC](/mobilnisite/slovnik/aac/) a PID 103 nese přidružené stopy titulků. Tato samo popisující povaha transportního proudu zjednodušuje návrh přijímače a umožňuje bezproblémový uživatelský zážitek, kdy lze seznamy kanálů dynamicky naplňovat přímo z vysílaného signálu.

## K čemu slouží

TSDT byla vytvořena k řešení specifických výzev spojených s doručováním televizních a rozhlasových vysílacích služeb přes paketově přepínané mobilní sítě v rámci architektury 3GPP [MBMS](/mobilnisite/slovnik/mbms/). Před MBMS byly multimediální obsahy pro mobilní zařízení primárně doručovány přes jednobodová spojení, což je neefektivní pro oblíbené živé události, protože duplikuje stejný datový proud tisícům jednotlivých uživatelů a spotřebovává nadměrnou síťovou kapacitu. MBMS zavedlo efektivní doručování typu bod–více bodů, ale to vyžadovalo mechanismus, aby přijímače mohly efektivně objevovat a dekódovat multiplexované služby v rámci sdíleného vysílacího nosiče. TSDT tento problém objevování řeší.

Historicky v tradičních digitálních vysílacích systémech, jako je [DVB](/mobilnisite/slovnik/dvb/), podobné tabulky (např. Program Association Table a Program Map Table) plní základní funkci popisu multiplexu transportního proudu. 3GPP TSDT plní analogický účel, ale je přizpůsobena IP prostředí MBMS pro mobilní sítě. Její vytvoření bylo motivováno potřebou standardizovaného mechanismu popisu služeb v pásmu. Bez něj by UE vyžadovala předem nakonfigurované informace nebo samostatné jednobodové datové spojení pro dotaz na průvodce službami, než by mohla dekódovat vysílání, což by komplikovalo uživatelský zážitek, zvyšovalo latenci při přepínání služeb a snižovalo efektivitu a autonomii modelu vysílacího doručování. TSDT umožňuje 'vždy zapnutý' vysílací zážitek, kdy je obsah a jeho popis doručován společně.

## Klíčové vlastnosti

- Objevování služeb v pásmu uvnitř transportního proudu MBMS
- Popisuje strukturu multiplexu a mapuje služby na Packet Identifiers (PID)
- Uvádí komponenty služeb (audio, video, text) a jejich kódovací formáty
- Periodicky přenášena pro dynamické získávání služeb přijímači
- Generována Broadcast Multicast Service Centre (BM-SC)
- Dodržuje standardizovanou syntaxi dle 3GPP TS 26.917 pro interoperabilitu

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [TSDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsdt/)
