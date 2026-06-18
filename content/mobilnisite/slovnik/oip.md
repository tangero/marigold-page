---
slug: "oip"
url: "/mobilnisite/slovnik/oip/"
type: "slovnik"
title: "OIP – Originating Identification Presentation"
date: 2026-01-01
abbr: "OIP"
fullName: "Originating Identification Presentation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oip/"
summary: "Originating Identification Presentation (OIP) je doplňková služba, která umožňuje prezentaci identity volajícího straně (CLI) volané. Jedná se o základní funkci telefonie umožňující zobrazení čísla vo"
---

OIP je doplňková služba, která předkládá identitu volajícího straně volané, čímž umožňuje službu zobrazení čísla volajícího (caller ID) v přepojovaných okruzích i paketových sítích 3GPP.

## Popis

Originating Identification Presentation (OIP) je klasická doplňková služba telefonie standardizovaná v 3GPP, která umožňuje prezentaci identifikačních informací volajícího straně volané. Služba doručuje identitu volající linky ([CLI](/mobilnisite/slovnik/cli/)), která typicky zahrnuje telefonní číslo volajícího ([MSISDN](/mobilnisite/slovnik/msisdn/)) a případně dodatečné informace jako jméno, do koncové sítě a uživatelského zařízení. Služba funguje v rámci signalizace řízení hovoru, primárně v [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) pro hovory přepojované okruhy a v rámci zpráv Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro VoIP hovory založené na IMS. Při hovoru ověří výchozí síť předplatné volajícího pro OIP a, je-li to povoleno, zahrne CLI do počáteční adresní zprávy ([IAM](/mobilnisite/slovnik/iam/)) nebo SIP INVITE. Koncová síť následně zkontroluje předplatné volané strany pro komplementární službu Originating Identification Restriction ([OIR](/mobilnisite/slovnik/oir/)), aby zjistila, zda je prezentace blokována. Pokud není blokována, jsou informace doručeny na terminál volané strany k zobrazení. Architektura zahrnuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server (HSS) pro ukládání dat o službách účastníka, Mobile Switching Centers (MSC) nebo Call Session Control Functions (CSCF) vykonávající servisní logiku a User Equipment zobrazující informace. Služba je nedílnou součástí uživatelského zážitku, prevence podvodů a třídění hovorů.

## K čemu slouží

OIP byla vytvořena k naplnění základní telekomunikační potřeby, aby volaná strana věděla, kdo volá, ještě před přijetím hovoru. Tím se řeší otázky soukromí, bezpečnosti a pohodlí, což uživatelům umožňuje třídit hovory. Historicky to byla definující vlastnost digitální telefonie (ISDN) oproti analogovým systémům. Její standardizace v 3GPP zajišťuje interoperabilitu v globálních mobilních sítích a poskytuje konzistentní zážitek ze služby zobrazení čísla volajícího. Řeší problém anonymních nebo nežádoucích hovorů tím, že ve výchozím nastavení prezentuje identitu volajícího, zatímco její protějšek (OIR) poskytuje volajícím mechanismus pro ochranu soukromí. Vývoj v rámci vydání 3GPP tuto službu udržoval během přechodu od přepojování okruhů k VoIP založenému na IMS, čímž byla zajištěna kontinuita služby a funkční parita napříč generacemi sítí.

## Klíčové vlastnosti

- Prezentace identity volající linky (CLI)
- Spolupráce se službou Originating Identification Restriction (OIR)
- Podpora v doménách CS i IMS
- Řízení služby na základě předplatného
- Doručování prostřednictvím signalizace řízení hovoru (ISUP, SIP)
- Zahrnuje základní zobrazení čísla a volitelně jména

## Související pojmy

- [OIR – Originating Identification presentation Restriction](/mobilnisite/slovnik/oir/)
- [CLI – Common Language Infrastructure](/mobilnisite/slovnik/cli/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
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
- … a dalších 30 specifikací

---

📖 **Anglický originál a plná specifikace:** [OIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/oip/)
