---
slug: "noa"
url: "/mobilnisite/slovnik/noa/"
type: "slovnik"
title: "NOA – Nature Of Address indicator"
date: 2025-01-01
abbr: "NOA"
fullName: "Nature Of Address indicator"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/noa/"
summary: "Parametr v signalizačních protokolech (jako ISUP, BICC, SIP), který klasifikuje typ adresy, například telefonního čísla. Rozlišuje mezi národními, mezinárodními, účastnickými nebo síťově specifickými"
---

NOA je signalizační parametr, který klasifikuje typ adresy, například národní nebo mezinárodní, aby umožnil správné směrování hovoru a obsluhu služeb.

## Popis

Indikátor povahy adresy (Nature Of Address – NOA) je základní pole v telekomunikačních signalizačních zprávách používané k interpretaci sémantiky a kontextu směrování adresy, typicky volaného čísla. Je přenášen v protokolech jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)), Bearer Independent Call Control (BICC) a Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)). NOA poskytuje nezbytná metadata o číslicích adresy, která síti říkají, jak je zpracovat. Například stejná číselná sekvence může představovat národní číslo, mezinárodní číslo (s předpokládanou úvodní '+') nebo síťově specifický služební kód a NOA je klíčem k rozlišení této nejednoznačnosti.

Technicky je NOA obvykle několik bitů nebo bajt uvnitř informačního prvku adresy. V ISUP je součástí parametrů Called Party Number a Calling Party Number. Mezi běžné hodnoty patří 'International Number' (mezinárodní číslo), 'National (Significant) Number' (národní (významné) číslo), 'Subscriber Number' (účastnické číslo), 'Abbreviated Number' (zkrácené číslo) a 'Network-Specific Number' (síťově specifické číslo). Když ústředna přijme zprávu o sestavení hovoru, prověří NOA parametru Called Party Number, aby určila postup směrování. Hodnota 'International' spustí zpracování kódu země, hodnota 'National' označuje, že číslo je v rámci národního číslovacího plánu, a 'Subscriber' číslo je považováno za místní číslo v rámci stejné sítě nebo oblasti.

NOA funguje ve spojení s indikátorem číslovacího plánu (Numbering Plan Indicator – [NPI](/mobilnisite/slovnik/npi/)), který specifikuje číslovací plán (např. E.164, E.212 pro [IMSI](/mobilnisite/slovnik/imsi/), privátní). Společně poskytují úplnou interpretaci číslic adresy. To je klíčové pro mezisíťové hovory, zejména mezi zeměmi s různými číslovacími konvencemi, a pro umožnění služeb, jako jsou bezplatná čísla, prémiová čísla a tísňová volání, které vyžadují specifické zacházení na základě povahy adresy.

## K čemu slouží

Indikátor NOA byl vytvořen k řešení problému nejednoznačné interpretace čísel v automatizovaných telefonních sítích. V raných ručních ústřednách kontext čísla chápal operátor. S automatickým přepojováním potřebovala síť strojově čitelný způsob, jak poznat, zda číslice představují místní, dálkové nebo mezinárodní volání, aby mohla aplikovat správnou směrovací logiku a účtování. Bez NOA by mohlo být číslo jako '441234567890' chybně směrováno jako národní číslo v jedné zemi, přestože je určeno jako mezinárodní číslo do UK (+44).

Řeší omezení spočívající pouze v analýze číslic (jako jsou předčíslí). Zatímco předčíslí (např. '00' pro mezinárodní volání) jsou uživatelsky volené konvence, NOA je vnitrosíťový, jednoznačný indikátor nastavovaný zdrojovým uzlem na základě vstupu účastníka a jeho předplatného. To je obzvláště důležité v integrovaných digitálních sítích ([ISDN](/mobilnisite/slovnik/isdn/)) a později v IP sítích (VoIP, IMS), kde je signalizace oddělena od uživatelské roviny. NOA zajišťuje konzistentní a spolehlivé směrování hovorů napříč sítěmi více dodavatelů a více operátorů a tvoří základní kámen globální telekomunikační interoperability.

## Klíčové vlastnosti

- Rozlišuje typ a rozsah telefonního čísla nebo adresy
- Umožňuje správná rozhodnutí o směrování pro národní, mezinárodní a služební čísla
- Používá se v klíčových signalizačních protokolech jako ISUP, BICC a SIP
- Funguje v součinnosti s indikátorem číslovacího plánu (NPI) pro úplnou interpretaci adresy
- Podporuje speciální služební čísla (např. tísňová, prémiová) prostřednictvím specifických hodnot NOA
- Umožňuje směrování a účtování hovorů mezi operátory a mezi standardy

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [NOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/noa/)
