---
slug: "im-bcsm"
url: "/mobilnisite/slovnik/im-bcsm/"
type: "slovnik"
title: "IM-BCSM – IP Multimedia Basic Call State Model"
date: 2025-01-01
abbr: "IM-BCSM"
fullName: "IP Multimedia Basic Call State Model"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/im-bcsm/"
summary: "IP Multimedia Basic Call State Model (IM-BCSM) je model konečného automatu používaný v IP Multimedia Subsystem (IMS) k popisu stavů a přechodů multimediální relace. Poskytuje standardizovaný rámec pro"
---

IM-BCSM je model konečného automatu používaný v IMS k popisu stavů a přechodů multimediální relace pro standardizované řízení hovorů založené na SIP a pro vykonávání servisní logiky.

## Popis

IP Multimedia Basic Call State Model (IM-BCSM) je konceptuální model definovaný 3GPP pro znázornění životního cyklu IP multimediální relace v architektuře IMS. Je založen na konečném automatu ([FSM](/mobilnisite/slovnik/fsm/)), který popisuje možné stavy, v nichž se hovor nebo relace může nacházet, spolu s událostmi, které spouštějí přechody mezi těmito stavy. IM-BCSM je primárně používán funkcí Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) a aplikačními servery ([AS](/mobilnisite/slovnik/as/)) pro správu logiky řízení relací a konzistentní vykonávání služeb v celé síti.

Model se skládá ze dvou hlavních částí: Originating IM-BCSM (O-IM-BCSM) a Terminating IM-BCSM (T-IM-BCSM). O-IM-BCSM modeluje relaci z pohledu volajícího účastníka a zahrnuje stavy od zahájení relace po její vytvoření nebo ukončení. T-IM-BCSM modeluje relaci z pohledu volaného účastníka a zpracovává stavy od příchodu relace po její přijetí nebo uvolnění. Každá část obsahuje body ve volání (PICs), které reprezentují konkrétní stavy, a detekční body (DPs), kde události mohou spustit interakce se servisní logikou. Například stavy zahrnují 'Null', 'Authorize_Origination_Attempt', 'Collect_Information', 'Analyze_Information', 'Routing' a 'Alerting'. Detekční body umožňují vyvolání servisní logiky, jako je kontrola zákazu volání nebo aplikace pravidel pro přesměrování hovorů.

IM-BCSM funguje tak, že zpracovává signalizační zprávy SIP odpovídající událostem v modelu stavů. Když je přijata SIP zpráva INVITE, CSCF ji namapuje na odpovídající stavový přechod IM-BCSM, například z 'Null' do 'Authorize_Origination_Attempt'. V každém detekčním bodě může CSCF interagovat s aplikačním serverem, aby provedl servisní logiku, což může ovlivnit tok relace – například přesměrování hovoru nebo aplikaci specifického zacházení. Tento strukturovaný přístup zajišťuje jednotné zpracování multimediálních relací, což umožňuje interoperabilitu mezi síťovými prvky a konzistentní chování služeb. Role modelu je kritická pro implementaci standardizovaných doplňkových služeb a vlastních aplikací v IMS a poskytuje jasný rámec pro vývojáře a síťové operátory k návrhu a nasazení funkcí řízení hovorů.

## K čemu slouží

IM-BCSM byl vyvinut pro řešení potřeby standardizovaného modelu stavu hovoru v IP multimediálních sítích, který zajišťuje konzistentní a interoperabilní řízení relací. Před jeho zavedením zpracování hovorů v raných IP multimediálních systémech postrádalo jednotný model, což vedlo k proprietárním implementacím a obtížím při integraci služeb. S vývojem IMS vzrostl požadavek na společný rámec pro zvládnutí složitosti relací založených na SIP a pro umožnění pokročilých telefonních služeb.

Vytvoření IM-BCSM bylo motivováno úspěchem modelu Basic Call State Model ([BCSM](/mobilnisite/slovnik/bcsm/)) používaného v tradičních inteligentních sítích ([IN](/mobilnisite/slovnik/in/)) pro přepojování okruhů. Přizpůsobením tohoto konceptu pro doménu IP multimédií poskytl 3GPP vývojářům služeb a operátorům známý model, což usnadnilo migraci služeb IN do IMS. IM-BCSM řeší problémy související s nejednoznačností řízení hovorů, spouštěním služeb a interakcí funkcí, což umožňuje bezproblémovou implementaci služeb, jako je čekání na hovor, držení hovoru nebo konference s více účastníky. Podporuje vývoj směrem k plně IP sítím tím, že poskytuje robustní základ pro vykonávání servisní logiky, který je nezbytný pro komerční nasazení hlasových a multimediálních služeb založených na IMS.

## Klíčové vlastnosti

- Model konečného automatu pro správu životního cyklu IP multimediální relace
- Rozdělen na část pro volajícího (O-IM-BCSM) a volaného (T-IM-BCSM)
- Definuje body ve volání (PICs) pro stavy relace a detekční body (DPs) pro spouštěče služeb
- Umožňuje konzistentní řízení hovorů a vykonávání servisní logiky v IMS sítích
- Podporuje implementaci doplňkových služeb, jako je přesměrování hovorů a zákazy volání
- Vychází z principů BCSM z inteligentních sítí a je přizpůsoben pro relace založené na SIP

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [IM-BCSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/im-bcsm/)
