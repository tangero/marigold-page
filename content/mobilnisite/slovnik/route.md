---
slug: "route"
url: "/mobilnisite/slovnik/route/"
type: "slovnik"
title: "ROUTE – Real-time transport Object delivery over Unidirectional Transport"
date: 2025-01-01
abbr: "ROUTE"
fullName: "Real-time transport Object delivery over Unidirectional Transport"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/route/"
summary: "ROUTE je jednosměrný doručovací protokol pro přenos mediálních objektů, jako jsou segmenty MPEG-DASH, přes vysílací sítě, například eMBMS. Umožňuje efektivní, škálovatelné šíření lineárního a na vyžád"
---

ROUTE je jednosměrný transportní protokol pro efektivní doručování mediálních objektů, jako jsou segmenty MPEG-DASH, přes vysílací (broadcast) sítě za účelem umožnění škálovatelného multimediálního šíření.

## Popis

Real-time transport Object delivery over Unidirectional Transport (ROUTE) je protokol navržený pro efektivní a spolehlivé doručování diskrétních datových objektů přes jednosměrné IP multicast/broadcast sítě. Je specifikován v kontextu služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její evoluce (eMBMS) konsorcia 3GPP, zejména pro doručování mediálního obsahu pro služby jako LTE-based broadcast. ROUTE pracuje na aplikační vrstvě, typicky nad protokolem [UDP](/mobilnisite/slovnik/udp/) (User Datagram Protocol), a je navržen tak, aby spolupracoval s dalšími protokoly, jako je [FLUTE](/mobilnisite/slovnik/flute/) (File Delivery over Unidirectional Transport) a [MPEG](/mobilnisite/slovnik/mpeg/) Media Transport ([MMT](/mobilnisite/slovnik/mmt/)).

ROUTE je zásadně postaven pro doručování objektů, jako jsou mediální segmenty MPEG-DASH (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)), manifesty ([MPD](/mobilnisite/slovnik/mpd/)) a další přidružená metadata. Jeho architektura je orientovaná na relaci, přičemž ROUTE relace se skládá z jednoho nebo více zdrojových toků. Každý zdrojový tok přenáší objekty z konkrétního zdroje a tyto objekty jsou fragmentovány do zdrojových bloků, které jsou následně zapouzdřeny do ROUTE paketů pro přenos. Klíčovou součástí je stavební blok Layered Coding Transport ([LCT](/mobilnisite/slovnik/lct/)), převzatý z FLUTE, který poskytuje funkce řízení zahlcení a identifikace paketů. ROUTE také zahrnuje instanci protokolu Asynchronous Layered Coding (ALC) pro spolehlivé doručování za použití Forward Error Correction (FEC).

Princip fungování: Mediální server připraví segmenty DASH a jim odpovídající MPD. Ty jsou prezentovány jako objekty ROUTE odesílateli. Odesílatel přiřadí každý objekt ke zdrojovému toku, fragmentuje jej a může použít FEC kódování pro generování opravných symbolů. Výsledné zdrojové bloky (data a opravné symboly) jsou paketizovány do LCT paketů se specifickými hlavičkami obsahujícími identifikátory transportní relace (TSI) a identifikátory objektů. Tyto pakety jsou následně přenášeny přes jednosměrný vysílací kanál. Na straně přijímače ROUTE klient z přijatých paketů znovu sestaví objekty, přičemž využívá FEC pro obnovu ze ztráty paketů. Jakmile je objekt (např. video segment) kompletně přijat, je předán DASH klientovi pro přehrávání. Úlohou ROUTE je poskytnout vysoce efektivní, škálovatelný a spolehlivý transportní mechanismus pro doručování medií založených na souborech a segmentech přes vysílací sítě, což umožňuje služby jako živé TV a rozsáhlé šíření souborů.

## K čemu slouží

ROUTE byl vyvinut pro řešení rostoucí poptávky po efektivním hromadném šíření médií přes mobilní vysílací sítě, jako je eMBMS. Tradiční jednosměrný (unicast) streaming se stává neefektivním a nákladným při doručování oblíbených živých událostí nebo lineární TV tisícům současných uživatelů. Vysílání/multicast nabízí spektrálně efektivní řešení, ale vyžadoval moderní transportní protokol optimalizovaný pro současné mediální formáty, konkrétně MPEG-DASH, který se stal průmyslovým standardem pro adaptivní streamování.

Předchozí protokoly, jako FLUTE, byly navrženy pro spolehlivé doručování souborů, ale nebyly inherentně optimalizovány pro časově citlivé, kontinuální streamování segmentovaných médií. ROUTE byl vytvořen, aby tuto mezeru zaplnil. Řeší problém přenosu DASH segmentů a jejich manifestů včasným a synchronizovaným způsobem přes jednosměrný kanál. Jeho účelem je umožnit vysílacím společnostem a mobilním operátorům nasazovat škálovatelné služby lineární a na vyžádání poskytované TV a odlehčit tak přetíženým jednosměrným (unicast) sítím. Motivací byla potřeba standardizovaného, interoperabilního protokolu, který by mohl podporovat doručování živého i na vyžádání poskytovaného obsahu v rámci ekosystému 3GPP eMBMS, a tím usnadnit konvergenci vysílacích a širokopásmových služeb.

## Klíčové vlastnosti

- Optimalizován pro doručování mediálních segmentů a manifestů MPEG-DASH přes vysílání (broadcast)
- Využívá LCT (Layered Coding Transport) pro správu relací a řízení zahlcení
- Zahrnuje ALC (Asynchronous Layered Coding) a FEC pro spolehlivé doručování objektů bez zpětné vazby
- Podporuje zdrojové toky pro logické multiplexování objektů z různých zdrojů
- Umožňuje modely distribuce obsahu pro živé vysílání i obsah na vyžádání
- Navržen pro jednosměrné IP multicast/broadcast sítě, jako je eMBMS

## Související pojmy

- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [MMT – MPEG Media Transport](/mobilnisite/slovnik/mmt/)
- [LCT – Layered Coding Transport](/mobilnisite/slovnik/lct/)
- [ALC – Asynchronous Layered Coding](/mobilnisite/slovnik/alc/)

## Definující specifikace

- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [ROUTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/route/)
