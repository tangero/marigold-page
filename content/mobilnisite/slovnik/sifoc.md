---
slug: "sifoc"
url: "/mobilnisite/slovnik/sifoc/"
type: "slovnik"
title: "SIFOC – Send Information For Outgoing Call"
date: 2025-01-01
abbr: "SIFOC"
fullName: "Send Information For Outgoing Call"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sifoc/"
summary: "Doplňková služba v sítích GSM/UMTS, která umožňuje uživateli během zahájení hovoru odeslat dodatečné informace (např. číslo telefonní karty). Umožňuje pokročilé účtování a autentizaci pro odchozí hovo"
---

SIFOC je doplňková služba v sítích GSM/UMTS, která umožňuje uživateli odeslat během zahájení odchozího hovoru dodatečné informace pro pokročilé účtování a autentizaci.

## Popis

Send Information For Outgoing Call (SIFOC) je doplňková služba definovaná ve specifikacích 3GPP pro sítě GSM a UMTS. Funguje jako součást rámce pro řízení hovorů a interakci služeb a umožňuje volající straně poskytnout síti během fáze navazování odchozího hovoru doplňkové informace. Tyto informace se typicky používají pro účely autentizace, účtování nebo směrování nad rámec standardně vytočených číslic. Službu vyvolá uživatelské zařízení (UE) nebo mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) odesláním specifických signalizačních zpráv obsahujících informační prvek SIFOC do sítě. Síť, konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), tyto informace zpracuje. Může komunikovat s dalšími síťovými entitami, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo body řízení služeb (např. pro [CAMEL](/mobilnisite/slovnik/camel/)), aby informace ověřila a uplatnila příslušnou servisní logiku, jako je alternativní účtování nebo směrování hovoru na základě poskytnutých dat. Z architektonického hlediska je SIFOC integrována do protokolů pro řízení hovorů (např. v TS 24.008) a spoléhá na stávající signalizační infrastrukturu (např. [MAP](/mobilnisite/slovnik/map/), [ISUP](/mobilnisite/slovnik/isup/)). Informace jsou přenášeny sítí transparentně, dokud nedosáhnou entity zodpovědné za provedení služby. Její role je klíčová pro umožnění nadstandardních služeb, které vyžadují dodatečný vstup od uživatele při zahájení hovoru, a překlenuje tak propast mezi základní telefonní službou a službami inteligentní sítě.

## K čemu slouží

SIFOC byla vytvořena pro podporu služeb telefonních karet a dalších telefonních aplikací, kde volající potřebuje poskytnout autentizační nebo fakturační informace oddělené od vytočeného čísla. Před jejím zavedením takové služby často vyžadovaly složitý vstup pomocí [DTMF](/mobilnisite/slovnik/dtmf/) (dvoutónové vícefrekvenční signalizace) po navázání hovoru, což bylo nepohodlné a nejisté. SIFOC umožňuje odeslat tyto informace bezpečně v rámci počáteční signalizace při zahájení hovoru, čímž zlepšuje uživatelský zážitek a umožňuje síťovou autentizaci. Řeší omezení základního zahájení hovoru, které přenáší pouze cílové číslo, tím, že poskytuje standardizovaný mechanismus pro dodatečná data. To bylo zvláště důležité pro operátory GSM nabízející předplacené nebo podnikové služby, protože to usnadňovalo integraci s platformami inteligentní sítě pro účtování a řízení služeb v reálném čase. Tato funkce se objevila v raných vydáních GSM za účelem zvýšení flexibility služeb a byla zachována v následných vydáních 3GPP kvůli zpětné kompatibilitě a pokračující podpoře starších služeb.

## Klíčové vlastnosti

- Umožňuje přenos dodatečných uživatelských informací během signalizace zahájení hovoru
- Podporuje služby telefonních karet a autentizace
- Integruje se s CAMEL pro řízení služeb inteligentní sítě
- Používá standardizované informační prvky v zprávách pro řízení hovorů
- Zpracovávána MSC/VLR pro provedení servisní logiky
- Zachovává zpětnou kompatibilitu napříč vydáními 3GPP

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2

---

📖 **Anglický originál a plná specifikace:** [SIFOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sifoc/)
