---
slug: "pdtq"
url: "/mobilnisite/slovnik/pdtq/"
type: "slovnik"
title: "PDTQ – Planned Data Transfer with QoS requirements"
date: 2026-01-01
abbr: "PDTQ"
fullName: "Planned Data Transfer with QoS requirements"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdtq/"
summary: "Servisní funkce umožňující plánování přenosů dat se zaručenou kvalitou služeb (QoS) pro aplikace jako jsou aktualizace softwaru nebo přednačítání obsahu. Umožňuje síti předem naplánovat alokaci prostř"
---

PDTQ je servisní funkce pro plánování přenosů dat se zaručenou kvalitou služeb (QoS), která umožňuje síti předem naplánovat alokaci prostředků pro aplikace jako jsou aktualizace softwaru.

## Popis

Planned Data Transfer with QoS requirements (PDTQ) je servisní schopnost zavedená ve specifikaci 3GPP Release 18, definovaná v rámci architektury 5G System (5GS). Umožňuje Application Function ([AF](/mobilnisite/slovnik/af/)) požádat síť o naplánování budoucího přenosu dat pro User Equipment (UE) se specifickými zárukami QoS. Základní mechanismus spočívá v tom, že AF odešle žádost k Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) prostřednictvím Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), která specifikuje požadovaný objem dat, cílové časové okno, parametry QoS (jako [5QI](/mobilnisite/slovnik/5qi/), Guaranteed Flow Bit Rate, Maximum Flow Bit Rate) a cílový Data Network Name ([DNN](/mobilnisite/slovnik/dnn/)). PCF následně tuto žádost autorizuje a převede ji na pravidla politiky pro Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). SMF je zodpovědná za zřízení nebo modifikaci příslušné Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) Session pro splnění plánovaného přenosu a koordinuje s User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a Access and Mobility Management Function (AMF), aby zajistila, že UE bude dosažitelné a prostředky budou v Radio Access Network (RAN) alokovány v naplánovaný čas.

Architektonicky PDTQ využívá stávající rozhraní 5G založená na službách, především Nnef (mezi NEF a AF) a Npcf (mezi NEF a PCF). PCF využívá službu Npcf_SMPolicyControl k poskytnutí autorizované politiky SMF. Klíčovou součástí je spouštěč žádosti o řízení politiky 'Planned Data Transfer', který instruuje SMF, aby se připravila na budoucí aktivitu session. SMF může předem zřídit QoS Flows a upozornit RAN prostřednictvím AMF na nadcházející přenos dat, což umožňuje pokročilé plánování rádiových prostředků. Tato proaktivní orchestrace odlišuje PDTQ od reaktivních mechanismů QoS.

Úlohou PDTQ v síti je optimalizace využití prostředků a zlepšení uživatelského zážitku pro ne-reálné aplikace s hromadnými daty. Přesunem předvídatelných přenosů velkých objemů dat do období mimo špičku nebo období nízkého vytížení sítě přispívá k vyhlazování provozu a vyvažování zátěže. Zajišťuje, že aplikace jako aktualizace operačních systémů, stahování velkých souborů nebo přednačítání mediálního obsahu jsou dokončeny spolehlivě a ve stanoveném časovém rámci, aniž by konkurovaly službám citlivým na latenci, jako je hlas nebo streamování videa. To z něj činí základní prvek pro efektivní network slicing a diferencované nabídky služeb.

## K čemu slouží

PDTQ bylo vytvořeno, aby řešilo rostoucí poptávku po efektivním a předvídatelném zpracování provozu dat na pozadí v sítích 5G. Před jeho zavedením si přenosy dat na pozadí (např. aktualizace softwaru, zálohy v cloudu) konkurovaly o prostředky s aplikacemi uživatelů na popředí na bázi best-effort, což často vedlo k nepředvídatelným časům dokončení, potenciálnímu vybíjení baterie UE kvůli opakovaným pokusům o opětovné přenosy a přetížení během špičky. Operátoři sítí neměli standardizovaný mechanismus pro plánování a zaručení QoS pro takové plánované přenosy, což omezovalo jejich schopnost proaktivně spravovat zatížení sítě.

Historický kontext vychází z vývoje chytrých zařízení a IoT, která generují významné množství dat, jejichž přenos lze odložit. Motivací pro PDTQ bylo poskytnout standardizované rozhraní pro poskytovatele over-the-top (OTT) aplikací a podnikové služby, aby mohli vyjednávat garantované sloty pro doručení dat s mobilní sítí. Tím se řeší problém neefektivního zpracování dat na 'pozadí', které se transformuje na 'plánovanou' službu řízenou sítí. Řeší omezení předchozích přístupů, jako jsou základní QoS Class Identifiers (QCIs/5QIs) aplikované reaktivně, které nemohly zohlednit budoucí plánování založené na čase, a proprietární řešení postrádající interoperabilitu.

V konečném důsledku PDTQ umožňuje nové obchodní modely a smlouvy o úrovni služeb (SLA) pro plánované doručování dat. Umožňuje operátorům nabízet prémiové služby 'zaručeného doručení' poskytovatelům obsahu a podnikům, čímž zlepšuje efektivitu sítě prostřednictvím tvarování provozu a vytváří nové zdroje příjmů. Je to klíčový krok k tomu, aby se síť 5G stala inteligentnější a programovatelnější platformou pro rozmanité datové služby.

## Klíčové vlastnosti

- Plánování přenosů dat na časovém základě se spouštěcími a ukončovacími časovači
- Podpora garantovaných parametrů QoS (5QI, GBR, MFBR) pro plánovaný přenos
- Integrace s rámcem pro řízení politik v 5G (PCF, SMF) pro autorizaci a vynucování
- Rozhraní zprostředkované Network Exposure Function (NEF) pro žádosti Application Function (AF)
- Podpora okamžitého i odloženého poskytování politik SMF
- Mechanismy pro správu dosažitelnosti UE a oznámení o plánované session

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.543** (Rel-19) — 5G Data Transfer Policy Control Services Stage 3

---

📖 **Anglický originál a plná specifikace:** [PDTQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdtq/)
