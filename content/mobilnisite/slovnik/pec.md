---
slug: "pec"
url: "/mobilnisite/slovnik/pec/"
type: "slovnik"
title: "PEC – Post Event Charging"
date: 2025-01-01
abbr: "PEC"
fullName: "Post Event Charging"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pec/"
summary: "Post Event Charging (PEC) je architektura účtování v 5G, kde se záznamy o účtovaných datech (CDR) generují a zpracovávají až po ukončení servisní relace nebo události. Je navržena pro služby s nízkou"
---

PEC je architektura účtování v 5G, kde se záznamy o účtovaných datech (CDR) generují a zpracovávají až po úplném ukončení servisní relace nebo události.

## Popis

Post Event Charging (PEC) je paradigma účtování zavedené ve specifikaci 3GPP Release 16 jako součást systému 5G. Představuje posun od tradičního online ([OCS](/mobilnisite/slovnik/ocs/)) a offline účtování, kde k interakcím účtování dochází během relace. V PEC síť během poskytování služby s účtovacím systémem v reálném čase neinteraguje. Namísto toho jsou data o využití shromažďována lokálně síťovou funkcí (např. [SMF](/mobilnisite/slovnik/smf/), [PCF](/mobilnisite/slovnik/pcf/)) obsluhující uživatele. Po dokončení relace dat služby nebo konkrétní servisní události tato síťová funkce vygeneruje záznam o účtovaných datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo podobnou hlášku o využití. Tento záznam je následně předán účtovací funkci ([CHF](/mobilnisite/slovnik/chf/)) pro ocenění a účtování způsobem následného zpracování. Architektura spoléhá na předem stanovené politiky a kvoty dohodnuté mezi sítí a CHF před zahájením služby. Tyto politiky definují účtovací pravidla, jako jsou paušální sazby, poplatky za událost nebo objemové prahové hodnoty, které síťová funkce aplikuje lokálně. Mezi klíčové komponenty patří PCF pro řízení politik, SMF pro správu relací a generování CDR a CHF, která zastává roli fakturační domény. PEC je řízena především v rámci architektury založené na službách ([SBI](/mobilnisite/slovnik/sbi/)) 5G Core, využívá služeb Nchf založených na [HTTP](/mobilnisite/slovnik/http/)/2. Tato metoda snižuje signalizační zátěž a latenci, protože odstraňuje potřebu kontrol kreditu a aktualizací kvot v reálném čase během relace, což je ideální pro komunikaci typu stroj-stroj a další služby, kde okamžité autorizační účtování není kritické.

## K čemu slouží

PEC byla vyvinuta za účelem řešení omezení stávajících online účtovacích systémů ([OCS](/mobilnisite/slovnik/ocs/)) při zpracování masivního množství transakcí s nízkou cenou a nízkou latencí očekávaných v 5G, zejména pro scénáře internetu věcí (IoT) a hromadné komunikace typu stroj-stroj (mMTC). Tradiční online účtování vyžaduje dialog v reálném čase mezi síťovými funkcemi a OCS pro správu kvot a řízení kreditu, což přináší signalizační režii a latenci, která může být nepřekonatelnou překážkou pro služby zahrnující miliardy malých, častých událostí. Offline účtování, přestože se vyhýbá interakci v reálném čase, stále zahrnuje generování podrobných záznamů během relace a nemusí být dostatečně flexibilní pro nové obchodní modely. PEC to řeší oddělením účtování od toku služby v reálném čase. Operátorům umožňuje efektivně implementovat jednoduché, na událostech založené účtovací modely (např. za zařízení, za transakci nebo paušální). Motivací je potřeba škálovatelného a nákladově efektivního účtování pro 5G vertikály, jako je průmyslový IoT, kde zařízení generují obrovské množství malých datových transakcí. Zpracováním poplatků následně na základě předem dohodnutých politik PEC snižuje zahlcení síťové signalizace, snižuje provozní náklady a umožňuje nové strategie monetizace pro služby s vysokým objemem a nízkou hodnotou.

## Klíčové vlastnosti

- Zpracování dat účtování po dokončení servisní relace/události
- Snižuje signalizaci s účtovacím systémem v reálném čase
- Využívá předem stanovené účtovací politiky a pravidla
- Generuje záznamy o účtovaných datech (CDR) po ukončení relace
- Optimalizováno pro služby IoT/mMTC s vysokým objemem a nízkou latencí
- Funguje v rámci architektury 5G založené na službách (SBA)

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CHF – Charging Function](/mobilnisite/slovnik/chf/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- **TS 28.203** (Rel-18) — Charging management
- **TS 28.204** (Rel-18) — Charging management
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.274** (Rel-19) — SMS Charging Management Specification
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [PEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pec/)
