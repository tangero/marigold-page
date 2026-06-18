---
slug: "ms-mtsi"
url: "/mobilnisite/slovnik/ms-mtsi/"
type: "slovnik"
title: "MS-MTSI – Multi-Stream MTSI"
date: 2025-01-01
abbr: "MS-MTSI"
fullName: "Multi-Stream MTSI"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ms-mtsi/"
summary: "Multi-Stream MTSI (MS-MTSI) je služební prvek 3GPP pro konverzační video služby s více proudy přes IMS. Umožňuje klientovi odesílat a přijímat více synchronizovaných video proudů, což umožňuje pokroči"
---

MS-MTSI je služební prvek 3GPP pro konverzační video s více proudy přes IMS, který umožňuje klientovi odesílat a přijímat více synchronizovaných video proudů pro podporu imerzivní komunikace.

## Popis

Multi-Stream [MTSI](/mobilnisite/slovnik/mtsi/) (MS-MTSI) je standardizovaná služební schopnost od 3GPP pro službu multimediální telefonie pro IMS (MTSI). Zásadně rozšiřuje tradiční model bod-bod video telefonie tím, že umožňuje navázání, synchronizaci a správu více souběžných mediálních proudů v rámci jediné IMS relace. Toho je dosaženo prostřednictvím specifických signalizačních rozšíření a protokolů pro zpracování médií definovaných pro IMS jádro. Architektura zahrnuje vylepšení jak MTSI klienta, tak IMS síťových prvků pro podporu vyjednávání a doručování více mediálních proudů. Klient během navazování relace pomocí rozšíření Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) indikuje svou schopnost podporovat MS-MTSI. Síť, včetně Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Application Server ([AS](/mobilnisite/slovnik/as/)), musí být těchto schopností vědoma, aby mohla více proudů správně směrovat a uplatňovat na ně politiky. Klíčovým technickým aspektem je synchronizační mechanismus, který zajišťuje, že více video proudů (např. z různých kamerových úhlů na sportovní akci nebo z různých částí 360stupňového záznamu) je příjemci prezentováno s časově sladěním, což vytváří souvislý a imerzivní zážitek. To je typicky řízeno pomocí rozšíření [RTP](/mobilnisite/slovnik/rtp/) Control Protocol ([RTCP](/mobilnisite/slovnik/rtcp/)) a skupin synchronizačních zdrojů ([SSRC](/mobilnisite/slovnik/ssrc/)) definovaných v přidružených RTP relacích. MS-MTSI také definuje mechanismy pro dynamickou adaptaci, kdy mohou být jednotlivé proudy během aktivní relace přidávány nebo odebírány na základě síťových podmínek nebo interakce uživatele, což poskytuje flexibilitu. Jeho role v síti je jako vrstva služeb s přidanou hodnotou nad základní IMS infrastrukturou, což umožňuje poskytovatelům služeb nabízet vizuální komunikační služby nové generace.

## K čemu slouží

MS-MTSI byl vytvořen, aby řešil omezení tradiční video telefonie s jedním proudem, která nemohla podporovat nové scénáře imerzivní a multi-perspektivní komunikace. Motivace vycházela z rostoucí poptávky spotřebitelů a podniků po bohatších komunikačních zážitcích, jako jsou volání ve virtuální realitě ([VR](/mobilnisite/slovnik/vr/)), vzdálená spolupráce s více kamerovými přenosy a interaktivní sdílení 360stupňového videa. Před MS-MTSI vyžadovala implementace takových služeb proprietární, neinteroperabilní řešení nebo složité obejítí, jako je navazování více paralelních IMS relací, což bylo neefektivní a obtížně synchronizovatelné. Historický kontext představuje vývoj samotného MTSI, které v dřívějších vydáních poskytovalo robustní základ pro hlas a video přes LTE/5G, ale bylo zásadně navrženo pro jediný audio a jediný video proud na relaci. MS-MTSI, zavedený ve vydání 15, přímo řešil toto architektonické omezení standardizací rámce v rámci IMS ekosystému. Tato standardizace zajišťuje interoperabilitu mezi klienty a síťovým vybavením různých dodavatelů, snižuje implementační složitost pro poskytovatele služeb a otevírá nový trh pro imerzivní telekomunikační služby, které využívají vysokou šířku pásma a nízkou latenci sítí 4G a 5G.

## Klíčové vlastnosti

- Podpora vyjednávání více souběžných video RTP proudů v rámci jediné IMS relace
- Mechanismy pro synchronizaci médií mezi proudy pomocí RTCP a rozšíření hlaviček RTP
- Dynamická modifikace relace pro přidání, odebrání nebo nahrazení jednotlivých mediálních proudů během hovoru
- Zpětná kompatibilita se staršími MTSI klienty s jedním proudem prostřednictvím vyjednávání schopností
- Podpora různých typů proudů (např. hlavní pohled, pomocné pohledy, mapy hloubky) pro pokročilé vykreslování
- Integrace s IMS řízením politik pro správu QoS a přidělování šířky pásma na jednotlivé proudy

## Související pojmy

- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling

---

📖 **Anglický originál a plná specifikace:** [MS-MTSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ms-mtsi/)
