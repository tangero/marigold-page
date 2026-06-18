---
slug: "pidf-lo"
url: "/mobilnisite/slovnik/pidf-lo/"
type: "slovnik"
title: "PIDF-LO – Presence Information Data Format Location Object"
date: 2025-01-01
abbr: "PIDF-LO"
fullName: "Presence Information Data Format Location Object"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pidf-lo/"
summary: "PIDF-LO je XML formát standardizovaný IETF a přijatý 3GPP pro kódování a přenos informací o poloze uživatele v rámci služeb presence. Umožňuje aplikace využívající polohu tím, že poskytuje standardizo"
---

PIDF-LO je XML formát standardizovaný IETF a přijatý 3GPP pro kódování a přenos informací o poloze uživatele v rámci služeb presence za účelem umožnění aplikací využívajících polohu.

## Popis

Objekt polohy ve formátu informací o přítomnosti (PIDF-LO) je specifické využití formátu [PIDF](/mobilnisite/slovnik/pidf/) (Presence Information Data Format) od [IETF](/mobilnisite/slovnik/ietf/), definovaného v [RFC](/mobilnisite/slovnik/rfc/) 4119, rozšířeného o přenos informací o poloze. V rámci architektur 3GPP, především IP multimedia subsystému (IMS), slouží PIDF-LO jako standardizovaná datová struktura pro výměnu údajů o poloze uživatele mezi síťovými entitami a aplikačními servery. Jedná se o [XML](/mobilnisite/slovnik/xml/) dokument, který zapouzdřuje informace o poloze, jež mohou být vyjádřeny buď geografickými souřadnicemi (např. zeměpisná šířka, délka, nadmořská výška na základě Geography Markup Language, GML), nebo formátem občanské adresy (např. stát, město, ulice).

Dokument PIDF-LO je přenášen v rámci zpráv [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), jako jsou PUBLISH, NOTIFY nebo INVITE, což umožňuje, aby informace o poloze byly nedílnou součástí procedur presence a navazování relací. Klíčovou architektonickou komponentou využívající PIDF-LO je Location Server (např. Gateway Mobile Location Centre, [GMLC](/mobilnisite/slovnik/gmlc/), nebo vyhrazený Location Information Server, [LIS](/mobilnisite/slovnik/lis/)). Tento server je zodpovědný za získání polohy uživatele (např. z RAN prostřednictvím metod určování polohy v řídicí nebo uživatelské rovině), její formátování do dokumentu PIDF-LO a poskytnutí autorizovaným žadatelům, jako je IMS Application Server ([AS](/mobilnisite/slovnik/as/)) pro tísňové služby nebo Service Capability Exposure Function (SCEF/NEF).

Formát zahrnuje klíčová metadata, jako je časové razítko udávající čas určení polohy, identifikátor lokalizované entity (např. SIP URI nebo tel URI), a prvky popisující metodu použitou k získání polohy a její odhadovanou přesnost. Tato bohatá metadata umožňují spotřební aplikacím posoudit aktuálnost a spolehlivost polohových dat. Role PIDF-LO je zásadní pro směrování tísňových hovorů, kde se používá k předání polohy volajícího na tísňové operační středisko (PSAP), a pro komerční služby založené na poloze poskytované prostřednictvím IMS. Jeho standardizace zajišťuje interoperabilitu mezi síťovými prvky a aplikačními servery různých výrobců, což je klíčové pro rozsáhlé mobilní sítě s více dodavateli.

## K čemu slouží

PIDF-LO byl vytvořen k vyřešení kritického problému standardizace způsobu reprezentace a přenosu informací o poloze v sítích založených na IP, konkrétně v rámci architektury IMS od 3GPP. Před jeho přijetím proprietární nebo aplikačně specifické formáty polohových dat bránily interoperabilitě mezi síťovými prvky od různých výrobců a mezi sítěmi různých operátorů. To byl významný problém pro nezbytné služby, jako je tísňové volání (E112/E911), kde je spolehlivé a všeobecně srozumitelné předání polohy regulatorním požadavkem i nutností pro záchranu života.

Motivace pro přijetí PIDF-LO pramenila ze sbližování telekomunikačních a internetových technologií. Když 3GPP definovalo IMS pro poskytování multimediálních služeb přes IP, využilo existující protokoly IETF, jako je SIP, pro řízení relací a přítomnost. PIDF byl standardem IETF pro informace o přítomnosti. Jeho rozšíření o polohový objekt (PIDF-LO) poskytlo přirozený, XML založený a rozšiřitelný formát, který se mohl bezproblémově integrovat s architekturou IMS založenou na SIP. To umožnilo, aby se poloha stala plnohodnotnou součástí služeb presence, což umožnilo nejen tísňové služby, ale také novou generaci standardizovaných, sítí poskytovaných aplikací založených na poloze.

PIDF-LO navíc řeší potřebu společného jazyka mezi nativními systémy pro určování polohy v buněčných sítích (např. určování polohy v řídicí rovině) a aplikacemi na aplikační vrstvě založené na IP. Slouží jako překladová vrstva, která abstrahuje složitá, technologicky specifická měření polohy do dodavatele neutrálního, pro aplikace vhodného formátu. Tato abstrakce zjednodušuje vývoj a nasazování služeb, podporuje inovace v oblasti služeb založených na poloze a zároveň zajišťuje soulad s politikami ochrany soukromí a bezpečnosti pro nakládání s osobními identifikačními informacemi o poloze.

## Klíčové vlastnosti

- Standardizované XML schéma pro kódování geografických (GML) a občanských údajů o poloze
- Přenos v rámci SIP zpráv (např. PUBLISH, NOTIFY) pro integraci se službami IMS
- Zahrnuje metadata: časové razítko, identifikátor entity, metodu určení polohy a přesnost/nejistotu
- Podporuje modely poskytování polohy podle hodnoty (plná data v zprávě) a podle reference (ukazatel URI)
- Umožňuje kontrolu ochrany soukromí a politik prostřednictvím pravidel použití a autorizačních mechanismů
- Základ pro tísňové služby 3GPP (např. odvození NAI, ESRD/ESRK pro směrování)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [PIDF-LO na 3GPP Explorer](https://3gpp-explorer.com/glossary/pidf-lo/)
