---
slug: "ipig"
url: "/mobilnisite/slovnik/ipig/"
type: "slovnik"
title: "IPIG – In-Progress Imminent Peril Group"
date: 2025-01-01
abbr: "IPIG"
fullName: "In-Progress Imminent Peril Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ipig/"
summary: "Stav služby v MCPTT pro aktivní skupinový hovor zahájený za podmínek bezprostředního ohrožení. Řídí nouzovou komunikaci pro předdefinovanou skupinu, zajišťuje prioritní síťové prostředky a koordinovan"
---

IPIG je stav služby v MCPTT pro aktivní skupinový hovor zahájený za podmínek bezprostředního ohrožení (imminent peril) za účelem řízení nouzové komunikace pro předdefinovanou skupinu.

## Popis

In-Progress Imminent Peril Group (IPIG) je specializovaný stav služby v rámci architektury 3GPP Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně pro skupinové hovory Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Označuje skupinový hovor, který byl úspěšně navázán a je aktuálně aktivní, přičemž jeho počáteční sestavení bylo spuštěno nouzovým prohlášením typu 'imminent peril' (bezprostřední ohrožení) od uživatele. Bezprostřední ohrožení označuje situaci zahrnující bezprostřední hrozbu pro život nebo zdraví. Architektura zahrnuje klienta MCPTT, aplikační server MCPTT a systém správy skupin. Server MCPTT hraje klíčovou roli při vytváření a správě relace IPIG. Identifikuje hovor jako skupinový hovor typu imminent peril na základě počáteční žádosti, uplatňuje specifické zásady pro nouzové skupinové hovory a dynamicky spravuje skupinovou relaci. Mezi klíčové komponenty patří procesor skupinových hovorů, funkce varování před bezprostředním ohrožením a integrace s prioritními mechanismy v podkladovém jádru 3GPP (např. [GCSE](/mobilnisite/slovnik/gcse/)_LTE pro podpůrné funkce skupinové komunikace). Jeho úlohou je umožnit rychlou, jednosměrnou (one-to-many) nouzovou komunikaci pro týmy čelící kritickému incidentu. Stav 'In-Progress' je významný pro chování sítě a klienta; ovlivňuje zásady řízení práva k mluvení (floor control), povinné režimy naslouchání pro členy skupiny a uplatnění nejvyšší možné úrovně QoS a přednostního přerušení (pre-emption) napříč rádiovou přístupovou sítí (RAN) a jádrem sítě. Server může také vyvolat aktualizaci polohy všech účastníků a udržovat trvalou relaci, dokud autorizovaný uživatel nezruší stav bezprostředního ohrožení.

## K čemu slouží

Koncept IPIG byl vyvinut, aby řešil kritickou potřebu okamžité a spolehlivé skupinové komunikace během nouzových situací v oblasti veřejné bezpečnosti a operací s klíčovým posláním (mission-critical). Tradiční skupinové hovory v mobilních sítích postrádaly označení naléhavosti a garance prostředků potřebné pro koordinované reakce na bezprostřední hrozby. IPIG řeší problém povýšení běžného skupinového hovoru na nouzovou relaci s nejvyšší prioritou, která si vynucuje síťové prostředky. Byl motivován operačními postupy záchranných složek, kde varování celého týmu před situací bezprostředního ohrožení života vyžaduje nezaměnitelný komunikační kanál s vysokou prioritou. Před standardizací v 3GPP Release 13 byly podobné funkce závislé na konkrétních dodavatelích nebo se spoléhaly na úzkopásmové PMR systémy. Standardizace IPIG v rámci [MCPTT](/mobilnisite/slovnik/mcptt/) zajišťuje, že různé složky a země mohou vzájemně spolupracovat během společných operací a že síť pro tyto hovory poskytuje deterministický výkon, čímž překonává omezení typu 'best-effort' dřívějších komerčních služeb skupinové komunikace přes LTE.

## Klíčové vlastnosti

- Představuje aktivní relaci skupinového hovoru MCPTT zahájenou za podmínek bezprostředního ohrožení.
- Vynucuje nejvyšší úroveň síťové priority a přednostního přerušení (pre-emption) pro všechny zúčastněné UE.
- Uplatňuje specifické řízení práva k mluvení (floor control) a povinné chování naslouchání pro členy skupiny.
- Integruje se s mechanismy varování před bezprostředním ohrožením pro urgentní upozornění celé skupiny.
- Spravován aplikačním serverem MCPTT s definovanou autorizací pro zahájení a ukončení.
- Využívá podpůrné funkce GCSE_LTE v jádru sítě pro efektivní doručování skupinové komunikace.

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [IPIG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipig/)
