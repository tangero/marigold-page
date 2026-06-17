---
slug: "li"
url: "/mobilnisite/slovnik/li/"
type: "slovnik"
title: "LI – Lawful Interception"
date: 2026-01-01
abbr: "LI"
fullName: "Lawful Interception"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/li/"
summary: "Standardizovaný bezpečnostní a regulatorní rámec, který umožňuje oprávněným orgánům činným v trestním řízení odposlouchávat komunikaci a související data v telekomunikačních sítích. Jedná se o klíčový"
---

LI je standardizovaný rámec 3GPP, který umožňuje oprávněným orgánům činným v trestním řízení zákonně odposlouchávat komunikaci a data v mobilních sítích, a zajistit tak provozovatelům soulad s regulatorními a soukromí chránícími požadavky.

## Popis

Lawful Interception (LI) je komplexní, standardizovaná architektura a soubor rozhraní definovaných 3GPP, která umožňuje síťovým operátorům ([NO](/mobilnisite/slovnik/no/)) a poskytovatelům internetových služeb ([ISP](/mobilnisite/slovnik/isp/)) poskytovat zákonně autorizovaný odposlech telekomunikačního provozu a souvisejících informací orgánům činným v trestním řízení ([LEA](/mobilnisite/slovnik/lea/)). Nejde o jedinou komponentu, ale o systém zahrnující více síťových funkcí, rozhraní (známá jako Handover Interfaces - [HI](/mobilnisite/slovnik/hi/)) a přísné oddělení mezi provozními funkcemi sítě a funkcemi odposlechu. Systém LI je navržen tak, aby byl aktivován pouze po předložení platného soudního příkazu a funguje utajeně, bez upozornění cílového účastníka (Intercept Subject).

Architektonicky je systém 3GPP LI rozdělen do tří hlavních funkčních skupin: Intercepting Control Element ([ICE](/mobilnisite/slovnik/ice/)), Mediation Function ([MF](/mobilnisite/slovnik/mf/)) a Law Enforcement Monitoring Facility ([LEMF](/mobilnisite/slovnik/lemf/)). ICE je vestavěno v síťových uzlech, které zpracovávají komunikaci cíle, jako jsou [MME](/mobilnisite/slovnik/mme/), SGW, PGW, SMF, UPF v 5G, nebo MSC, SGSN, GGSN v dřívějších generacích. Jeho rolí je duplikovat a přesměrovat kopii Intercept Related Information (IRI) – která zahrnuje signalizační data hovoru, informace o poloze a data o využití služeb – a Content of Communication (CC) – skutečné hlasové, video nebo uživatelské datové pakety – směrem k MF. MF, často samostatné mediační zařízení, normalizuje, formátuje a doručuje tato odposlechnutá data do jedné nebo více LEMF prostřednictvím standardizovaných Handover Interfaces (HI1, HI2, HI3). HI1 slouží pro správu příkazů k odposlechu, HI2 doručuje IRI a HI3 doručuje CC.

Jak to funguje: Proces začíná, když LEMA (Law Enforcement Monitoring Agency) zašle zákonné pověření (soudní příkaz) síťovému operátorovi. Administrativní systém operátora nakonfiguruje příslušné ICE v síti tak, aby identifikovaly provoz pro určený cíl (pomocí identifikátorů jako IMSI, MSISDN nebo IP adresa). Po aktivaci ICE provádí hlubokou inspekci paketů a monitorování signalizace, aby zachytila veškeré IRI a CC spojené s cílem. Tato data jsou poté odeslána do MF, která zajistí jejich formátování podle standardů jako ETSI ES 201 671 nebo 3GPP TS 33.108 a bezpečné doručení do LEMF. Systém je navržen pro vysokou spolehlivost, zabezpečení (pro prevenci neoprávněného přístupu) a škálovatelnost, aby zvládl více simultánních odposlechů bez dopadu na kvalitu služeb pro ostatní účastníky. Jeho rolí je poskytnout zákonně konformní, auditovatelný a technicky robustní mechanismus pro sledování, což je povinný požadavek pro telekomunikační operátory ve většině jurisdikcí.

## K čemu slouží

Lawful Interception existuje, aby vyvážil dvě základní společenské potřeby: právo jednotlivce na soukromí a povinnost státu vyšetřovat trestnou činnost a zajistit národní bezpečnost. Před standardizací byly odposlechové schopnosti proprietární a často nekompatibilní, což orgánům činným v trestním řízení ztěžovalo práci napříč různými síťovými operátory a jurisdikcemi. Tento nedostatek standardizace mohl také vést k právním výzvám ohledně přípustnosti odposlechnutých důkazů. Standardizace LI v 3GPP, která začala naplno od Release 4, byla hnací silou regulatorních požadavků vlád po celém světě, které nařizovaly, že veřejné komunikační sítě musí mít vestavěné schopnosti pro podporu autorizovaného odposlechu.

Primární problémy, které řeší, jsou poskytnutí konzistentní, spolehlivé a právně obhajitelné metody pro odposlech moderní digitální komunikace a zajištění, že takové mocné schopnosti jsou implementovány se silnými zárukami proti zneužití. Řeší technickou výzvu odposlechu paketově přepínaných dat (kromě okruhově přepínaného hlasu), která se stala převažující s GPRS, UMTS a pozdějšími technologiemi. Standardizovaná architektura zajišťuje, že odposlech může být proveden bez ohledu na podkladovou síťovou technologii (2G, 3G, 4G, 5G, IMS) nebo použité zařízení dodavatele, což usnadňuje interoperabilitu pro orgány činné v trestním řízení. Definuje také přísné bezpečnostní požadavky na Handover Interfaces a mediační funkci, aby chránila integritu a důvěrnost jak procesu odposlechu, tak odposlechnutých dat.

Historicky byl jeho vývoj úzce spjat s novými síťovými architekturami a službami. Každé nové vydání systému 3GPP zavádělo specifikace LI pro nové síťové entity a služby, jako je IP Multimedia Subsystem (IMS) v Release 5, LTE/EPC v Release 8 a 5G System v Release 15. Tento kontinuální vývoj zajišťuje, že schopnosti LI drží krok s technologickým pokrokem, jako je VoLTE, network slicing a edge computing, a zabraňuje tak existenci 'slepých míst pro zákonný odposlech', která by mohla být zneužita. Tento rámec je nezbytný pro síťové operátory, aby splnili své licenční povinnosti a vyhnuli se sankcím, a zároveň poskytuje LEA nástroje potřebné pro efektivní vyšetřování v digitálním věku.

## Klíčové vlastnosti

- Standardizovaná architektura s Intercepting Control Element (ICE), Mediation Function (MF) a Law Enforcement Monitoring Facility (LEMF)
- Tři definovaná Handover Interfaces (HI1, HI2, HI3) pro bezpečné doručení příkazů, informací souvisejících s odposlechem (IRI) a obsahu komunikace (CC)
- Utajený provoz zajišťující, že odposlouchávaný subjekt nemá o sledování vědomí
- Podpora odposlechu jak okruhově přepínané, tak paketově přepínané komunikace napříč všemi generacemi 3GPP (2G až 5G) a IMS
- Silné bezpečnostní mechanismy na ochranu odposlechové infrastruktury a dat před neoprávněným přístupem
- Škálovatelný design pro zvládnutí více simultánních odposlechů bez degradace výkonu sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TR 23.919** (Rel-19) — 3GPP Direct Tunnel Deployment Guidelines
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [LI na 3GPP Explorer](https://3gpp-explorer.com/glossary/li/)
