---
slug: "c-tpdu"
url: "/mobilnisite/slovnik/c-tpdu/"
type: "slovnik"
title: "C-TPDU – Command Transport Protocol Data Unit"
date: 2025-01-01
abbr: "C-TPDU"
fullName: "Command Transport Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/c-tpdu/"
summary: "C-TPDU je protokolová datová jednotka používaná pro řídicí signalizaci v rámci transportní vrstvy sítí 3GPP. Přenáší příkazy pro navázání, uvolnění a správu spojení mezi síťovými entitami a zajišťuje"
---

C-TPDU je protokolová datová jednotka transportní vrstvy v sítích 3GPP, která přenáší řídicí příkazy pro navázání, uvolnění a správu spojení mezi síťovými entitami.

## Popis

Command Transport Protocol Data Unit (C-TPDU) je základním prvkem v protokolech transportní vrstvy definovaných 3GPP, konkrétně pro řídicí rovinu. Funguje jako strukturovaný formát zprávy pro přenos příkazů a souvisejících parametrů mezi partnerskými entitami, například mezi radiovou síťovou kontrolní jednotkou ([RNC](/mobilnisite/slovnik/rnc/)) a podpůrným uzlem [GPRS](/mobilnisite/slovnik/gprs/) ([SGSN](/mobilnisite/slovnik/sgsn/)) v UMTS nebo podobnými koncovými body řídicí roviny ve vyvinutých architekturách. C-TPDU není samostatný protokol, ale specifický typ [PDU](/mobilnisite/slovnik/pdu/) používaný v rámci širších transportních protokolů, jako je [SCCP](/mobilnisite/slovnik/sccp/) (Signaling Connection Control Part) nebo jiné adaptační vrstvy, pro správu signalizačních spojení.

Z architektonického hlediska je C-TPDU vloženo do datové části rámce transportní vrstvy. Skládá se z hlavičky a pole informačních prvků s proměnnou délkou. Hlavička obsahuje pole jako identifikátor typu PDU (odlišující jej od datových [TPDU](/mobilnisite/slovnik/tpdu/), I-TPDU atd.), referenční čísla spojení a řídicí příznaky. Informační prvky nesou specifické parametry příkazu, které mohou zahrnovat kódy příčin, hodnoty časovačů, adresy a další data potřebná k provedení příkazu, jako je zahájení spojení nebo nahlášení chybového stavu.

Jeho činnost je klíčová pro spojově orientovanou signalizaci. Například pro navázání signalizačního spojení pro relaci mobilního zařízení je od iniciující entity odeslána C-TPDU typu 'Connection Request' ([CR](/mobilnisite/slovnik/cr/)). Přijímající entita odpoví C-TPDU 'Connection Confirm' ([CC](/mobilnisite/slovnik/cc/)) pro potvrzení nebo 'Connection Refuse' (CREF) pro odmítnutí. Podobně C-TPDU jako 'Released' (RLSD) a 'Release Complete' (RLC) řídí řádné uvolnění spojení. Tato výměna příkazů zajišťuje spolehlivé přidělení, údržbu a uvolnění prostředků řídicí roviny a poskytuje stabilní základ pro signalizační protokoly vyšších vrstev, jako je RANAP (Radio Access Network Application Part) nebo BSSAP (Base Station System Application Part).

V širším síťovém kontextu umožňují C-TPDU spolehlivý přenos zpráv signalizační aplikační vrstvy. Spravují signalizační spoje, které přenášejí kritické informace pro správu mobility, řízení hovorů a správu relací. Bez spolehlivé výměny příkazů zprostředkované C-TPDU by řídicí rovina postrádala robustní mechanismus pro navázání potřebných transportních asociací, což by vedlo k možným signalizačním selháním a zhoršení síťové služby. Jejich návrh zahrnuje mechanismy detekce a obnovy chyb, často prostřednictvím sekvenčních čísel a postupů potvrzování v rámci výměny TPDU, což zajišťuje integritu signalizačního transportu.

## K čemu slouží

C-TPDU bylo vytvořeno za účelem poskytnutí standardizovaného, spolehlivého mechanismu pro správu signalizačních transportních spojení v telekomunikačních sítích, konkrétně pro řešení potřeby robustní řídicí roviny v digitálních celulárních systémech, jako jsou GSM a UMTS. Před jeho formalizací ve standardech 3GPP používaly rané signalizační systémy často jednodušší nebo proprietární metody pro řízení spojení, což mohlo vést k problémům s interoperabilitou a omezené spolehlivosti v komplexních síťových prostředích s více dodavateli. C-TPDU jako součást vrstevnatých transportních protokolů (např. založených na principech OSI) zavedlo jasné oddělení mezi správou spojení (řešenou C-TPDU) a přenosem dat (řešeným D-TPDU), čímž se zlepšila modularita a izolace chyb.

Primární problém, který řeší, je navázání, údržba a uvolnění signalizačních spojení, která přenášejí protokoly aplikační vrstvy. V mobilních sítích jsou tato spojení klíčová pro procedury jako předávání spojení, paging a zřizování relací. Bez spolehlivého příkazového protokolu by tyto procedury mohly selhat kvůli problémům na transportní vrstvě. C-TPDU poskytuje definovanou sadu příkazů s explicitními parametry, což zajišťuje konzistentní interpretaci stavů spojení všemi síťovými entitami. To bylo obzvláště důležité s vývojem sítí od přepojování okruhů pro hlas k podpoře přepojování paketů pro data (GPRS, EDGE), což vyžadovalo dynamičtější a častější správu signalizačních spojení.

K jeho vytvoření vedla potřeba mezinárodní standardizace pro zajištění globální interoperability pro roamování a nasazení s více dodavateli. Přijetím spojově orientované transportní služby s explicitními příkazovými PDU se 3GPP sjednotilo se zavedenými telekomunikačními signalizačními architekturami (jako je SS7), což umožnilo bezproblémovou integraci se stávajícími základními sítěmi. Mechanismus C-TPDU řešil omezení nespojových nebo méně strukturovaných přístupů tím, že poskytoval řízení signalizačních spojů přímo v přenosu, což umožňuje efektivní správu prostředků a obnovu po chybách, což je nezbytné pro vysokou dostupnost očekávanou ve veřejných pozemních mobilních sítích.

## Klíčové vlastnosti

- Standardizovaná sada příkazů pro řízení spojení (např. CR, CC, RLC, RLSD)
- Řízení transportních spojů přímo v přenosu (in-band signaling)
- Podpora spojově orientovaných signalizačních služeb
- Přenáší parametry jako kódy příčin a reference spojení
- Umožňuje spolehlivé navázání a uvolnění signalizačních asociací
- Integruje se s aplikačními protokoly vyšších vrstev (RANAP, BSSAP)

## Související pojmy

- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [C-TPDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-tpdu/)
