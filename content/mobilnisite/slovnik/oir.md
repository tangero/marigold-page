---
slug: "oir"
url: "/mobilnisite/slovnik/oir/"
type: "slovnik"
title: "OIR – Originating Identification presentation Restriction"
date: 2026-01-01
abbr: "OIR"
fullName: "Originating Identification presentation Restriction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oir/"
summary: "Doplňková služba, která volající straně umožňuje omezit zobrazení své identifikace (např. telefonního čísla) volané straně. Jde o klíčovou funkci zajišťující soukromí v telekomunikačních sítích, která"
---

OIR je doplňková služba, která volající straně umožňuje omezit zobrazení své identifikace, například telefonního čísla, volané straně.

## Popis

Originating Identification presentation Restriction (OIR) je doplňková služba standardizovaná organizací 3GPP, která volající straně poskytuje možnost zabránit prezentaci svých identifikačních údajů (typicky čísla volajícího nebo [SIP](/mobilnisite/slovnik/sip/) [URI](/mobilnisite/slovnik/uri/)) volané straně. Služba funguje v rámci vrstev řízení hovorů a správy relací sítě, kde zachycuje a upravuje signalizační zprávy nesoucí identifikaci volajícího. Když uživatel OIR aktivuje (ať už pro jednotlivý hovor pomocí předvolby, nebo jako trvalou službu předplatného), síť aplikuje logiku k odstranění identifikace z odchozí signalizace nebo ji označí jako 'prezentace omezena'. Toto je vynucováno na řídicích uzlech výchozí sítě, jako je [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) v okruhově spínaných sítích nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving Call Session Control Function) v sítích IMS (IP Multimedia Subsystem). Služba komunikuje s [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) nebo [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) za účelem ověření předplatitelských dat a autorizace služby. V architektuře IMS je OIR implementována jako služba na straně volajícího v rámci S-CSCF, využívá Initial Filter Criteria (iFC) ke spuštění příslušného aplikačního serveru, pokud je potřeba pro pokročilejší logiku. Omezení může být v konkrétních případech potlačeno, například u tísňových hovorů nebo hovorů na určitá autorizovaná čísla, podle síťové politiky a regulatorních požadavků. Síť volané strany může také aplikovat doplňkové služby, jako je Connected Line Identification Presentation ([COLP](/mobilnisite/slovnik/colp/)), nebo generovat indikátory ochrany soukromí na základě přijatého stavu omezení.

## K čemu slouží

OIR byla vytvořena jako odpověď na rostoucí obavy uživatelů o soukromí a umožňuje jednotlivcům kontrolovat zveřejňování svých osobních kontaktních údajů. Před zavedením takových služeb byla identifikace volajícího typicky vždy prezentována, což mohlo vést k nežádoucímu kontaktu, obtěžování nebo narušení soukromí. Služba řeší problém nedobrovolného zveřejňování informací v telefonii a dává předplatitelům autonomii nad svou identitou. Její zavedení bylo motivováno regulatorními požadavky v mnoha regionech, které nařizují poskytovat možnosti ochrany soukromí pro uživatele telekomunikačních služeb. Umožňuje také obchodní aplikace, například umožňuje zaměstnancům uskutečňovat pracovní hovory bez prozrazení osobního mobilního čísla. Služba poskytuje standardizovaný mechanismus napříč různými generacemi sítí (okruhově spínané a paketově spínané/IMS), což zajišťuje konzistentní funkčnost ochrany soukromí při vývoji sítí.

## Klíčové vlastnosti

- Umožňuje volajícím uživatelům omezit prezentaci svého CLI (Calling Line Identity) nebo SIP URI.
- Lze aktivovat pro jednotlivý hovor pomocí předvolby (např. *67) nebo jako trvalá služba předplatného.
- Integrována do architektur řízení hovorů jak pro okruhově spínané (CS), tak pro IMS sítě.
- Komunikuje s předplatitelskými databázemi (HLR/HSS) pro autorizaci služby.
- Lze potlačit pro tísňová volání a další prioritní hovory podle síťové politiky.
- Generuje příslušné indikátory ochrany soukromí ve signalizaci (např. parametr 'prezentace omezena').

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [COLP – Connected Line identification Presentation](/mobilnisite/slovnik/colp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.408** (Rel-7) — TIP/TIR Services Protocol Specification
- **TS 24.410** (Rel-8) — Protocol Description of HOLD Services
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- … a dalších 29 specifikací

---

📖 **Anglický originál a plná specifikace:** [OIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/oir/)
