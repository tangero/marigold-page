---
slug: "imei-tac-2"
url: "/mobilnisite/slovnik/imei-tac-2/"
type: "slovnik"
title: "IMEI/TAC – International Mobile Equipment Identity Type Allocation Code"
date: 2026-01-01
abbr: "IMEI/TAC"
fullName: "International Mobile Equipment Identity Type Allocation Code"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/imei-tac-2/"
summary: "IMEI/TAC je úvodní osmiciferný segment plného IMEI, který jednoznačně identifikuje model a výrobce mobilního zařízení. Je klíčový pro schvalování typu zařízení, řízení přístupu k síti a regulatorní sh"
---

IMEI/TAC je úvodní osmiciferný segment plného IMEI, který jednoznačně identifikuje model a výrobce mobilního zařízení pro schvalování typu, řízení přístupu k síti a regulatorní shodu.

## Popis

International Mobile Equipment Identity Type Allocation Code ([IMEI](/mobilnisite/slovnik/imei/)/TAC) je globálně jedinečný identifikátor přidělený mobilnímu zařízení. Tvoří prvních osm číslic z celkového patnáctimístného IMEI. Samotný TAC přiděluje asociace GSM ([GSMA](/mobilnisite/slovnik/gsma/)) nebo její určené orgány výrobcům zařízení. Struktura je standardizovaná: první dvě číslice jsou identifikátor přidělující organizace (Reporting Body Identifier), který označuje skupinu schválenou GSMA, jež TAC přidělila, a následujících šest číslic je vlastní kód přidělení typu (Type Allocation Code), který jednoznačně identifikuje model a původ. Tento kód je trvale uložen v hardwaru zařízení, typicky v nevolatilní paměti, a je přenášen do sítě během úvodních procedur registrace a připojení.

V síťových operacích používá IMEI/TAC jádrová síť, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G, jak je podrobně popsáno ve specifikacích 3GPP 23.401 a 23.501. Když se uživatelské zařízení (UE) pokouší připojit k síti, poskytne svou identitu [IMSI](/mobilnisite/slovnik/imsi/) a své IMEI. Síť může z IMEI extrahovat TAC. Tento TAC je pak použit pro dotazy na registr identit zařízení ([EIR](/mobilnisite/slovnik/eir/)). EIR je databáze obsahující seznamy identifikátorů zařízení, typicky kategorizované jako bílý (schválený), šedý (monitorovaný) nebo černý (blokovaný). Síť konzultuje EIR, aby zjistila, zda je konkrétní typ nebo model zařízení oprávněn přistupovat k síťovým službám.

Role IMEI/TAC přesahuje jednoduché řízení přístupu. Je zásadní pro správu zařízení, prevenci podvodů a regulatorní shodu. Operátoři jej používají ke sledování typů zařízení ve své síti, což napomáhá plánování kapacity, přizpůsobování služeb a zajištění kompatibility se síťovými funkcemi. Z bezpečnostního hlediska pomáhá identifikovat a blokovat zařízení nahlášená jako odcizená nebo zařízení typu, o kterém je známo, že je zranitelný nebo nevyhovuje standardům. V kontextu 5G a síťového dělení (network slicing) může být TAC parametrem pro rozhodování o politikách, potenciálně ovlivňujícím, ke kterému síťovému řezu je zařízení na základě svých schopností povoleno přistupovat. TAC je statický, na hardwaru založený identifikátor, který poskytuje spolehlivý základ pro tyto síťové funkce, nezávisle na SIM kartě nebo předplatném uživatele.

## K čemu slouží

[IMEI](/mobilnisite/slovnik/imei/)/TAC byl vytvořen, aby poskytl standardizovanou, globálně jedinečnou metodu pro identifikaci typu a původu mobilního zařízení. Před jeho standardizací byla identifikace modelů zařízení napříč různými sítěmi a výrobci nekonzistentní, což bránilo interoperabilitě, správě podvodů a regulatornímu dohledu. TAC řeší problém nejednoznačnosti modelu zařízení a umožňuje sítím, regulátorům a průmyslovým orgánům přesně kategorizovat a spravovat širokou škálu mobilních zařízení vstupujících na trh.

Jeho zavedení řeší kritické potřeby v oblasti síťové bezpečnosti a provozu. Z bezpečnostního hlediska umožňuje implementaci registrů identit zařízení ([EIR](/mobilnisite/slovnik/eir/)), které jsou nezbytné pro blokování odcizených telefonů a zabránění používání padělaných nebo neschválených zařízení, která by mohla poškodit integritu sítě nebo bezpečnost uživatelů. Z provozního hlediska umožňuje operátorům mobilních sítí profilovat populaci zařízení ve své síti. Toto profilování je klíčové pro řešení problémů specifických pro zařízení, plánování zavádění nových služeb (jako VoLTE nebo 5G NR) a zajištění, že síťové zdroje jsou kompatibilní se schopnostmi připojených zařízení. TAC poskytuje jasnou vazbu mezi fyzickým zařízením a jeho certifikovanými technickými specifikacemi.

Vývoj směrem k 5G (od verze Rel-16) posílil jeho účel v rámci složitější, na službách založené architektury. V systémech 5G, s rozšířením zařízení internetu věcí (IoT) a různorodých případů užití, se přesná identifikace zařízení stává ještě kritičtější pro vynucování politik, výběr řezů a bezpečnost. TAC zůstává základním prvkem pro tyto pokročilé funkce, zajišťujíc zpětnou kompatibilitu a konzistentní identifikátor napříč generacemi mobilních technologií.

## Klíčové vlastnosti

- Globálně jedinečný osmiciferný kód identifikující model a výrobce zařízení
- Tvoří úvodní segment plného patnáctimístného IMEI
- Přidělený GSMA nebo jejími určenými přidělujícími organizacemi
- Používaný pro dotazy na EIR (Equipment Identity Register) a řízení přístupu k síti
- Umožňuje správu populace zařízení a sledování schvalování typu
- Hardwarově uložený, neměnitelný identifikátor pro spolehlivé profilování zařízení

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [IMEISV – International Mobile station Equipment Identity and Software Version number](/mobilnisite/slovnik/imeisv/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2

---

📖 **Anglický originál a plná specifikace:** [IMEI/TAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/imei-tac-2/)
