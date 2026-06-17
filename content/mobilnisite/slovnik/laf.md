---
slug: "laf"
url: "/mobilnisite/slovnik/laf/"
type: "slovnik"
title: "LAF – Location Application Function"
date: 2025-01-01
abbr: "LAF"
fullName: "Location Application Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/laf/"
summary: "Síťová funkce v architektuře založené na službách (SBA) sítě 5G, která poskytuje služby určování polohy externím aplikacím. Slouží jako rozhraní pro aplikace k vyžádání polohy uživatelských zařízení ("
---

LAF je funkce sítě 5G, která poskytuje rozhraní pro externí aplikace k vyžádání polohy uživatelského zařízení (UE) a podporuje služby jako tísňová volání, zákonný odposlech a komerční služby založené na poloze.

## Popis

Location Application Function (LAF) je síťová funkce definovaná v architektuře založené na službách (SBA) jádra sítě 5G. Nachází se ve vrstvě pro vystavení služeb a slouží jako hlavní rozhraní pro autorizované externí aplikační funkce ([AF](/mobilnisite/slovnik/af/)) nebo servery třetích stran k vyžádání informací o poloze uživatelských zařízení (UE). LAF poskytuje standardizované, zabezpečené [API](/mobilnisite/slovnik/api/) (často založené na [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/)), přes které mohou aplikace podávat požadavky na určení polohy, například na jednorázové okamžité určení polohy nebo na periodické či spouštěné hlášení polohy. Je klíčovou součástí architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) a překládá požadavky aplikační úrovně na síťově specifické procedury.

Z architektonického hlediska LAF spolupracuje s dalšími funkcemi jádra sítě k vyřízení požadavků na polohu. Jejím hlavním protějškem je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), což je tradiční uzel jádra sítě pro služby určování polohy. V síti 5G LAF typicky komunikuje s GMLC pomocí standardizovaného rozhraní Le nebo jeho ekvivalentu založeného na službách (např. rozhraní Nlg). LAF může také spolupracovat s funkcí Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) kvůli vynucování politik, autentizaci a autorizaci požadavku externí aplikace. LAF se zabývá aspekty jako ověření předplatného aplikace, kontrola předpisů na ochranu soukromí (např. souhlas uživatele přes GMLC) a správa relace požadavku na polohu.

Jak to funguje, zahrnuje posloupnost kroků. Nejprve externí AF odešle požadavek na polohu na API LAF a specifikuje parametry jako identifikátor cílového UE (např. [MSISDN](/mobilnisite/slovnik/msisdn/), externí identifikátor), požadovanou QoS (např. přesnost, doba odezvy) a typ služby (např. okamžitá, odložená). LAF autentizuje AF a autorizuje požadavek. Poté požadavek přepošle na GMLC. GMLC spolupracuje s obsluhujícím AMF daného UE a nakonec s funkcemi pro určování polohy v přístupové síti (např. pomocí LTE Positioning Protocol (LPP) přes AMF a NG-RAN), aby získal odhad polohy. Výsledná data o poloze (např. zeměpisné souřadnice) jsou směrovány zpět přes GMLC na LAF, která je naformátuje a doručí žádající externí AF.

Klíčové součásti LAF zahrnují její rozhraní založené na službách (např. Nlaf), její logiku pro správu relací požadavků a její integraci s NEF pro zabezpečení vystavení. Role LAF spočívá v abstrakci složitostí podkladových síťových technologií určování polohy (např. GNSS, OTDOA, E-CID) před aplikací a poskytování jednoduchého, webově přívětivého API. To umožňuje širokou škálu služeb včetně určení polohy tísňového volajícího (E911/E112), účtování na základě polohy, správy vozových parků a personalizovaných služeb. Hraje klíčovou roli při zpřístupnění schopností sítě 5G, konkrétně přesné polohy, aplikačnímu ekosystému bezpečným způsobem.

## K čemu slouží

LAF byla vytvořena za účelem modernizace a standardizace způsobu, jakým externí aplikace přistupují k síťovým službám určování polohy. V architekturách před 5G byly služby určování polohy pro aplikace často poskytovány prostřednictvím proprietárních nebo zastaralých rozhraní k GMLC, která mohla být složitá a postrádat flexibilitu vyžadovanou moderními cloud-nativními aplikacemi. Rozšíření IoT a pokročilých služeb založených na poloze si vyžádalo agilnější přístup řízený API.

Zavedení LAF v architektuře SBA sítě 5G to řeší tím, že poskytuje vyhrazenou funkci založenou na službách pro vystavení služeb určování polohy aplikacím. Řeší problém těsného provázání aplikací se síťově specifickými protokoly. Nabídkou RESTful nebo HTTP/2 založeného API umožňuje vývojářům aplikací snadno integrovat možnosti určování polohy bez hluboké znalosti telekomunikačních protokolů. Dále centralizuje autentizaci, autorizaci a řízení politik pro požadavky na polohu prostřednictvím integrace s NEF, čímž zvyšuje zabezpečení a dodržování předpisů na ochranu soukromí. Tento vývoj podporuje vizi 5G o programovatelnosti sítě a vystavení služeb, což umožňuje nové obchodní modely a efektivní podporu kritických služeb, jako jsou vylepšené tísňové služby.

## Klíčové vlastnosti

- Poskytuje standardizované API (např. RESTful/HTTP2) pro externí aplikace k vyžádání polohy uživatelského zařízení (UE)
- Integruje se s Gateway Mobile Location Centre (GMLC) k provedení procedur určování polohy
- Podporuje různé typy požadavků na polohu: okamžité, periodické a spouštěné
- Vynucuje autentizaci a autorizaci aplikací a politiky ochrany soukromí (často prostřednictvím NEF)
- Abstrahuje podkladové síťové technologie určování polohy před aplikacemi
- Umožňuje tísňové služby, zákonný odposlech a komerční aplikace služeb založených na poloze (LBS)

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/laf/)
