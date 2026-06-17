---
slug: "dsac"
url: "/mobilnisite/slovnik/dsac/"
type: "slovnik"
title: "DSAC – Domain Specific Access Restriction"
date: 2025-01-01
abbr: "DSAC"
fullName: "Domain Specific Access Restriction"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dsac/"
summary: "Síťově řízený mechanismus, který omezuje přístup uživatelského zařízení (UE) ke konkrétním službám nebo doménám, jako je IMS nebo tísňové služby, zatímco ostatní povoluje. Umožňuje operátorům řídit sí"
---

DSAC je síťově řízený mechanismus, který omezuje přístup uživatelského zařízení (UE) ke konkrétním službám nebo doménám za účelem řízení zahlcení a zajištění dostupnosti kritických služeb.

## Popis

Domain Specific Access Restriction (DSAC) je funkcionalita jádra sítě definovaná v architektuře 3GPP, která primárně funguje v rámci Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v Evolved Packet Core (EPC) a funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G Core (5GC). Jejím základním úkolem je aplikovat detailní, na doménách založené politiky řízení přístupu pro UE. Síť vyhodnocuje registraci nebo servisní požadavek UE vůči souboru operátorem definovaných omezení. Tato omezení nejsou plošným zamítnutím síťového přístupu, ale cílí na konkrétní servisní domény, nejvýznamněji IP Multimedia Subsystem (IMS) pro hlasové a multimediální služby. Je-li pro UE aktivní omezení, uzel jádra sítě (MME/AMF) zamítne požadavky na vytvoření přenosových kanálů (bearerů) nebo PDU (Protocol Data Unit) relací spojených s blokovanou doménou, často s konkrétním příčinným kódem (cause code), který UE informuje o doménově specifickém omezení.

Mechanismus funguje ve spojení s daty o účastníkovi a síťovými politikami. Omezení mohou být dynamicky aplikována na základě faktorů, jako je síťové zatížení, úroveň předplatného nebo regulatorní požadavky. Například během období extrémního zahlcení může operátor použít DSAC k dočasnému omezení přístupu k hlasovým službám založeným na IMS pro nízkoprioritní účastníky, aby zachoval prostředky pro tísňové služby nebo zákazníky vyšších tříd. UE po obdržení zamítnutí s příčinným kódem DSAC implementuje zpětný časovač (back-off timer), čímž se zabrání jeho okamžitému opětovnému pokusu o přístup k blokované doméně, a tím se sníží signalizační zátěž.

Kritickým architektonickým aspektem DSAC je jeho doménově specifická povaha. Neovlivňuje přístup k jiným doménám, jako je obecný přístup k internetu přes výchozí přenosový kanál. To umožňuje UE potenciálně zachovat datovou konektivitu pro nezbytné aplikace, zatímco mu je znemožněno iniciovat hovor VoLTE (Voice over LTE). Vynucování politiky je centralizováno v jádru sítě, což zajišťuje konzistentní aplikaci bez ohledu na technologii rádiového přístupu ([E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN). DSAC představuje sofistikovanější nástroj než dřívější, širší mechanismy omezení přístupu (Access Class Barring), a umožňuje inteligentní správu provozu a priorizaci služeb v moderních paketových sítích.

## K čemu slouží

DSAC byl zaveden pro řešení potřeby detailního, na služby zaměřeného řízení provozu a zahlcení ve všech-IP sítích, jako jsou LTE a 5G. Tradiční okruhově spínané sítě měly inherentní oddělení hlasu a dat, ale v paketově spínaných architekturách všechny služby soutěží o stejné paketové prostředky. Bez mechanismů jako je DSAC by síťové přetížení mohlo degradovat všechny služby stejně, včetně těch kritických, jako jsou tísňové hlasové hovory (eVoLTE).

Jeho vytvoření bylo motivováno migrací na telefonii založenou na IMS (VoLTE). Operátoři potřebovali nástroj pro samostatné řízení signalizační a mediální zátěže IMS nezávisle na datovém provozu typu best-effort. Předchozí přístupy, jako Access Class Barring (ACB), byly buňkově založené a aplikovaly se plošně na všechny pokusy o přístup, postrádaly schopnost ochránit konkrétní servisní doménu. DSAC to řeší tím, že umožňuje jádru sítě instruovat UE, aby se vyhýbala konkrétní servisní doméně (např. IMS), zatímco potenciálně povoluje jiné datové relace, což umožňuje chytřejší využití prostředků a zvýšenou spolehlivost služeb pro prioritní uživatele a služby.

## Klíčové vlastnosti

- Doménově specifické omezení (např. IMS, tísňové služby)
- Vynucování politiky založené v jádru sítě (MME/AMF)
- Dynamická aplikace na základě síťových podmínek nebo profilu účastníka
- Způsobí, že UE implementuje zpětný časovač (back-off timer) pro blokovanou doménu
- Umožňuje pokračovat v přístupu k neomezeným doménám (např. internetová data)
- Poskytuje specifické příčinné kódy (cause codes) pro interpretaci UE

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.806** (Rel-13) — Application Specific Congestion Control for Data
- **TS 23.898** (Rel-7) — 3GPP System Enhancements for Network Overload
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.704** (Rel-12) — Study on Enhanced Broadcast of System Information

---

📖 **Anglický originál a plná specifikace:** [DSAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsac/)
