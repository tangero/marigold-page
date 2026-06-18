---
slug: "o-im-bcsm"
url: "/mobilnisite/slovnik/o-im-bcsm/"
type: "slovnik"
title: "O-IM-BCSM – Originating IP Multimedia Basic Call State Model"
date: 2025-01-01
abbr: "O-IM-BCSM"
fullName: "Originating IP Multimedia Basic Call State Model"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/o-im-bcsm/"
summary: "Model konečného automatu používaný v IMS k definování a řízení sledu událostí pro zahajovanou IP multimediální relaci, jako je například hovor nebo videosezení založené na SIP. Poskytuje rámec pro int"
---

O-IM-BCSM je model konečného automatu v IMS, který definuje posloupnost událostí pro zahajovanou (originating) IP multimediální relaci a poskytuje rámec pro aplikační logiku služeb CAMEL za účelem řízení zpracování hovoru.

## Popis

O-IM-BCSM je základní komponentou v architektuře IP Multimedia Subsystem (IMS) podle 3GPP, konkrétně navrženou pro řídicí rovinu. Jedná se o formalizovaný model, který reprezentuje životní cyklus zahajované IP multimediální relace z pohledu síťové entity řídící tuto relaci, typicky [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving Call Session Control Function). Model je strukturován jako konečný automat ([FSM](/mobilnisite/slovnik/fsm/)) skládající se z řady bodů ve volání (Points In Call, [PIC](/mobilnisite/slovnik/pic/)) a detekčních bodů (Detection Points, [DP](/mobilnisite/slovnik/dp/)). PIC reprezentují stabilní stavy v procesu sestavení, změny nebo ukončení hovoru, například 'Authorize_Origination_Attempt' nebo 'O_Alerting'. DP jsou konkrétní události nebo okamžiky v rámci těchto stavů, kde může být standardní zpracování přerušeno, aby mohla být spuštěna externí aplikační logika poskytovaná prostředím služeb [CAMEL](/mobilnisite/slovnik/camel/) (CAMEL Service Environment, [CSE](/mobilnisite/slovnik/cse/)). Když je DP aktivován (armed), S-CSCF pozastaví své standardní zpracování a odešle oznámení do CSE, které pak může S-CSCF instruovat, jak pokračovat – například pokračovat, ukončit hovor nebo upravit parametry relace.

O-IM-BCSM spolupracuje s [T-IM-BCSM](/mobilnisite/slovnik/t-im-bcsm/) (Terminating [IM-BCSM](/mobilnisite/slovnik/im-bcsm/)) a poskytuje tak kompletní pohled na dialog. Jeho činnost je spuštěna, když uživatelské zařízení (UE) iniciuje SIP relaci, například požadavkem INVITE. S-CSCF, vystupující jako zahajující (originating) konečný automat, posouvá hovor přes definované PIC. Klíčová interakce nastává na aktivovaných DP, které jsou konfigurovány na základě O-IM-CSI (Originating IP Multimedia CAMEL Subscription Information) účastníka. Tato data, stažená z HSS, sdělují S-CSCF, na kterých DP má zapojit službu CAMEL. Aplikační logika sídlící v gsmSCF pak může aplikovat komplexní služby, jako je překlad čísel, kontrola volání, předplacené účtování nebo interakce s interaktivní hlasovou odpovědí, ještě než hovor dorazí k cíli.

Z architektonického hlediska je O-IM-BCSM definován v aplikační logice řízení služeb S-CSCF. Rozhraní k CAMEL Application Part (CAP) zprostředkovává rozhraní IMS Service Control (ISC) pro komunikaci s gsmSCF. Jeho role je klíčová pro migraci tradičních služeb inteligentní sítě (Intelligent Network, IN) z okruhově přepínané domény do domény paketově přepínané IMS, což zajišťuje kontinuitu služeb a umožňuje nové, na IP založené služby. Poskytnutím standardizovaného stavového modelu zajišťuje interoperabilitu mezi síťovými zařízeními od různých dodavatelů a umožňuje konzistentní provádění služeb definovaných operátorem v celé síti.

## K čemu slouží

O-IM-BCSM byl vytvořen, aby překlenul propast mezi tradiční inteligencí okruhově přepínané telefonie a novým IP multimediálním světem IMS. Před zavedením IMS byly pokročilé telefonní služby (jako předplacené, bezplatné linky nebo virtuální privátní sítě) poskytovány v okruhově přepínaných sítích GSM a UMTS za použití protokolu CAMEL (Customised Applications for Mobile network Enhanced Logic) a modelů základního stavu hovoru (Basic Call State Models, BCSM) pro Mobile Switching Centre (MSC). Se zavedením IMS v 3GPP Release 5 byl potřeba nový řídicí paradigma založený na SIP, ale operátoři potřebovali způsob, jak přenést své stávající, ziskové služby IN a prostředí pro tvorbu služeb do této nové architektury.

O-IM-BCSM tento problém řeší tím, že poskytuje analogický stavový model pro relace založené na SIP. Umožňuje opětovné využití stávající aplikační logiky služeb CAMEL a obchodních pravidel, které často představují pro operátory značnou investici, v doméně IMS s minimálními úpravami. To umožnilo hladký přechod na plně IP sítě. Dále vytvořil standardizovaný rámec pro spouštění nových, na IMS specifických služeb, čímž poskytl operátorům kontrolu a flexibilitu potřebnou k vytváření a nasazování pokročilých multimediálních služeb, které jsou řízené sítí, nikoli pouze založené na funkčnosti koncového zařízení. Jeho vytvoření bylo motivováno potřebou transparentnosti služeb, síťové kontroly a jasné migrační cesty pro služby inteligentní sítě, což bylo pro přijetí technologie IMS operátory zásadní.

## Klíčové vlastnosti

- Definuje konečný automat pro řízení zahajovaných (originating) SIP relací
- Integruje aplikační logiku služeb CAMEL do zpracování hovorů v IMS
- Využívá body ve volání (Points In Call, PIC) k reprezentaci stabilních stavů hovoru
- Používá detekční body (Detection Points, DP) pro vyvolání aplikační logiky služeb
- Spolupracuje s T-IM-BCSM pro kompletní modelování hovoru
- Umožňuje síťové služby, jako je předplacené účtování a kontrola volání pro multimediální relace

## Související pojmy

- [T-IM-BCSM – Terminating IP Multimedia Basic Call State Model](/mobilnisite/slovnik/t-im-bcsm/)
- [O-IM-CSI – Originating IP Multimedia CAMEL Subscription Information](/mobilnisite/slovnik/o-im-csi/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [O-IM-BCSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-im-bcsm/)
