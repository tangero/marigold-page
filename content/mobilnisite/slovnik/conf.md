---
slug: "conf"
url: "/mobilnisite/slovnik/conf/"
type: "slovnik"
title: "CONF – CONFerence calling"
date: 2025-01-01
abbr: "CONF"
fullName: "CONFerence calling"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/conf/"
summary: "CONF je doplňková služba umožňující více účastníkům současně se účastnit hlasové nebo multimediální komunikační relace. Umožňuje uživatelům zřizovat, spravovat a účastnit se konferenčních hovorů a pod"
---

CONF je doplňková služba umožňující více účastníkům současně se účastnit hlasové nebo multimediální komunikační relace pro konferenční hovory.

## Popis

CONF (CONFerence calling, konferenční hovor) je standardizovaná doplňková služba v sítích 3GPP, která umožňuje více uživatelům současně se účastnit jedné komunikační relace. Služba funguje v rámci architektury IP Multimedia Subsystem (IMS) a využívá protokol Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro zřizování, úpravu a ukončování relací. Konferenční hovor může iniciovat uživatel (v roli kontroléra konference), který pozve další účastníky, nebo se účastníci mohou připojit k naplánovaným konferencím pomocí specifických přístupových údajů. Služba podporuje různé typy konferencí včetně ad-hoc (okamžitě zřízených), plánovaných (předem domluvených) a vysílacích (jednosměrné šíření).

Technická implementace CONF zahrnuje koordinaci několika síťových prvků. Conference [AS](/mobilnisite/slovnik/as/) (Application Server) slouží jako centrální řídicí bod, který spravuje seznam účastníků, mixování médií a zásady konference. Když uživatel zahájí konferenční hovor, jeho UE (User Equipment) odešle požadavek SIP INVITE na Conference AS, který následně naváže individuální SIP dialogy s každým účastníkem. Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) zajišťuje vlastní zpracování médií, včetně mixování audia pro hlasové konference a případně skládání videa pro multimediální konference. Služba podporuje jak plně duplexní komunikaci (všichni účastníci mohou současně mluvit a naslouchat), tak režimy řízené předsedou, kde kontrolér konference spravuje oprávnění účastníků.

Mezi klíčové architektonické komponenty patří Conference Focus (logická funkce uvnitř Conference AS, která udržuje stav konference), Conference Notification Service (zajišťuje oznámení účastníkům) a Conference Policy Server (spravuje autorizaci a zásady). Služba je integrována s dalšími komponentami IMS včetně Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) pro směrování relací a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro získávání dat o účastnících a jejich služebních profilů. CONF podporuje různé typy médií včetně hlasu, videa a textu v reálném čase, přičemž mechanismy kvality služby (QoS) zajišťují odpovídající doručování médií.

Služba funguje prostřednictvím standardizovaných procedur definovaných v řadě specifikací 3GPP. Zřizování konference sleduje specifické signalizační toky zahrnující metody SIP REFER pro pozvání účastníků, SIP SUBSCRIBE/NOTIFY pro aktualizace stavu konference a SIP re-INVITE pro změny během hovoru. Účastníci se mohou ke konferencím připojit prostřednictvím přímého pozvání, vytočením [URI](/mobilnisite/slovnik/uri/) konference nebo použitím přístupových kódů konference. Služba zahrnuje funkce jako správa seznamu účastníků (přidávání, odebírání, ztlumení účastníků, povýšení na předsedu), uzamčení/odemčení konference a možnosti záznamu. Bezpečnostní mechanismy zajišťují, že konference mohou vytvářet nebo se k nim připojovat pouze autorizovaní uživatelé, přičemž autentizace je prováděna standardními postupy IMS.

## K čemu slouží

CONF byl vyvinut pro uspokojení rostoucí potřeby efektivní skupinové komunikace v mobilních sítích, zejména pro firemní a kolaborativní aplikace. Před standardizovanými službami konferenčních hovorů byli uživatelé odkázáni na implementace specifické pro operátora nebo řešení třetích stran, kterým chyběla interoperabilita a konzistentní uživatelský zážitek. Služba umožňuje efektivní víceúčastnickou komunikaci bez nutnosti, aby byli účastníci na stejném fyzickém místě, čímž podporuje moderní pracovní postupy a společenské interakce.

Vytvoření CONF v 3GPP Release 7 se časově shodovalo s dozráním architektury IMS, která poskytla potřebnou infrastrukturu pro pokročilé multimediální služby. Předchozí řešení konferenčních hovorů v přepojování okruhů byla omezená z hlediska škálovatelnosti, sady funkcí a integrace s dalšími službami. CONF využívá sítě s přepojováním paketů a protokol [SIP](/mobilnisite/slovnik/sip/) k poskytnutí flexibilnějších a funkčně bohatších konferenčních schopností, které lze škálovat na větší počet účastníků a podporovat multimediální obsah přesahující pouze hlas.

Služba řeší několik praktických problémů: umožňuje efektivní obchodní schůzky geograficky rozptýlených týmů, podporuje aplikace distančního vzdělávání, usnadňuje rodinnou a sociální skupinovou komunikaci a poskytuje možnosti koordinace při mimořádných událostech. Standardizací konferenčních hovorů napříč sítěmi 3GPP zajišťuje interoperabilitu mezi různými operátory a zařízeními, vytváří konzistentní uživatelský zážitek a zároveň umožňuje poskytovatelům služeb nabízet přidané komunikační funkce.

## Klíčové vlastnosti

- Zřizování víceúčastnické relace pomocí signalizace SIP
- Podpora typů konferencí: ad-hoc, plánované a vysílací
- Schopnosti mixování médií prostřednictvím MRF (Media Resource Function)
- Správa účastníků (přidání, odebrání, ztlumení, povýšení na předsedu)
- Mechanismy oznamování a odebírání stavu konference
- Integrace s architekturou IMS a dalšími doplňkovými službami

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.505** (Rel-8) — Protocol Description of the Conference Service
- **TS 24.605** (Rel-19) — 3GPP CONF Service Protocol Specification
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 24.611** (Rel-19) — Anonymous Communication Rejection & Barring
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service
- **TS 29.827** (Rel-16) — Policy and Charging for Volume Based Charging

---

📖 **Anglický originál a plná specifikace:** [CONF na 3GPP Explorer](https://3gpp-explorer.com/glossary/conf/)
