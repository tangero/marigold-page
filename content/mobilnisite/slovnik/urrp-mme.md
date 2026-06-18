---
slug: "urrp-mme"
url: "/mobilnisite/slovnik/urrp-mme/"
type: "slovnik"
title: "URRP-MME – User Reachability Request Parameter for MME"
date: 2025-01-01
abbr: "URRP-MME"
fullName: "User Reachability Request Parameter for MME"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/urrp-mme/"
summary: "Parametr v 4G EPC používaný SGW k vyžádání, aby MME provedlo procedury dosažitelnosti UE. Spouští paging pro lokalizaci nečinného UE při příchodu dat ve směru downlink, čímž iniciuje proceduru síťově"
---

URRP-MME je parametr v 4G Evolved Packet Core, který SGW používá k vyžádání, aby MME provedlo paging nečinného UE a iniciovalo jeho opětovné připojení pro doručení dat ve směru downlink.

## Popis

User Reachability Request [Parameter](/mobilnisite/slovnik/parameter/) for [MME](/mobilnisite/slovnik/mme/) (URRP-MME) je signalizační prvek používaný v 4G Evolved Packet Core (EPC) na rozhraní S11 mezi Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Mobility Management Entity (MME). Jeho účelem je umožnit SGW vyžádat si od MME provedení procedur k dosažitelnosti UE, když SGW přijme data ve směru downlink pro EPS bearer UE, které je ve stavu ECM-IDLE. SGW, které buffruje downlinkové pakety, zahrnuje URRP-MME ve zprávě Downlink Data Notification ([DDN](/mobilnisite/slovnik/ddn/)) odeslané MME.

Po přijetí DDN s URRP-MME MME iniciuje proceduru síťově iniciovaného service request. To zahrnuje, že MME nejprve odešle zprávu Paging všem eNodeB v registrované Tracking Area UE, aby jej lokalizovalo. Jakmile UE odpoví Service Request, MME koordinuje s eNodeB a SGW opětovnou aktivaci EPS bearerů, převádí UE zpět do stavu ECM-CONNECTED a navazuje tunel [S1-U](/mobilnisite/slovnik/s1-u/) pro uživatelskou rovinu. Poté MME odešle SGW potvrzení Downlink Data Notification Acknowledge, načež SGW může přeposlat buffrovaná data. Parametr může také nést informace, jako je EPS Bearer ID, na který data čekají, což umožňuje MME upřednostnit určité bearery.

Architektonicky je URRP-MME klíčovou součástí návrhu úspory energie a správy mobility v EPC. Umožňuje síti zachovat kontinuitu IP relací, zatímco UE mohou přecházet do energeticky úsporného stavu idle. SGW funguje jako kotva mobility a spouštěč datové cesty, zatímco MME zajišťuje vlastní paging a správu signalizačního spojení. Toto jasné funkční rozdělení je charakteristickým rysem návrhu EPC. Procedura zajišťuje, že paging je prováděn pouze v případě potřeby (tj. při příchodu dat ve směru downlink), čímž optimalizuje rádiové a signalizační prostředky jádra sítě. Mechanismus se také používá pro další síťově iniciované procedury, jako je žádost o připojení k [PDN](/mobilnisite/slovnik/pdn/) nebo modifikace beareru iniciovaná [PCRF](/mobilnisite/slovnik/pcrf/).

## K čemu slouží

URRP-MME byl definován v počátečních specifikacích LTE/EPC (Release 8) k vyřešení základního problému doručování dat ve směru downlink mobilnímu UE, které je v energeticky úsporném stavu idle. Předchozí mobilní systémy měly podobné koncepty, ale plochá IP architektura LTE a striktní oddělení uživatelské roviny ([SGW](/mobilnisite/slovnik/sgw/)) a řídicí roviny (MME) vyžadovaly standardizovaný a efektivní signalizační mechanismus mezi nimi. URRP-MME formalizuje tento spouštěč ve zprávě DDN.

Řeší omezení spočívající v neexistenci trvalého spojení uživatelské roviny k nečinnému UE. Bez tohoto mechanismu by síť musela buď udržovat UE trvale připojená (plýtvání baterií a rádiovými prostředky), nebo by nebyla schopna doručit data, čímž by přerušila neustálé IP připojení (always-on). URRP-MME umožňuje paradigma 'vždy dosažitelné' pro IP služby, což bylo klíčové pro přijetí LTE u aplikací na chytrých telefonech spoléhajících na push notifikace (e-mail, messaging atd.).

Dále poskytuje řízenou bránu pro síťově iniciované akce. Nad rámec pouhého příchodu dat umožňuje mechanismus URRP-MME jádru sítě (např. prostřednictvím PCRF) iniciovat převedení UE do stavu connected z důvodů řízených politikou, například k založení dedikovaného beareru pro novou službu. Tím bylo vyřešeno, jak může síť proaktivně spravovat prostředky bearerů UE na základě externích požadavků služeb nebo měnících se profilů předplatného, což umožnilo pokročilé modely QoS a účtování v LTE.

## Klíčové vlastnosti

- Standardizovaný parametr ve zprávě Downlink Data Notification (DDN) na rozhraní S11 (GTPv2-C)
- Spouští v MME proceduru síťově iniciovaného service request, včetně pagingu
- Používá se, když SGW přijme data ve směru downlink pro UE ve stavu ECM-IDLE
- Umožňuje efektivní obnovení tunelů S1-U uživatelské roviny a EPS bearerů
- Podporuje notifikaci specifickou pro bearer prostřednictvím zahrnutého EPS Bearer ID
- Základní prvek modelu úspory energie v EPS, umožňující UE spát, zatímco zůstávají dosažitelná

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN

---

📖 **Anglický originál a plná specifikace:** [URRP-MME na 3GPP Explorer](https://3gpp-explorer.com/glossary/urrp-mme/)
