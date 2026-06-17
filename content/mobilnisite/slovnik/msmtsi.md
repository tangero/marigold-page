---
slug: "msmtsi"
url: "/mobilnisite/slovnik/msmtsi/"
type: "slovnik"
title: "MSMTSI – Multi-Stream Multimedia Telephony Service for IMS"
date: 2025-01-01
abbr: "MSMTSI"
fullName: "Multi-Stream Multimedia Telephony Service for IMS"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msmtsi/"
summary: "Standardizovaná služba založená na IMS pro pokročilou multimediální telefonii, podporující více synchronizovaných mediálních toků, jako je video, audio a sdílení obsahu v rámci jediné relace. Umožňuje"
---

MSMTSI je standardizovaná telefonní služba založená na IMS, která v rámci jediné relace podporuje více synchronizovaných mediálních toků, jako je video, audio a sdílení obsahu, pro bohatou komunikaci.

## Popis

Multi-Stream Multimedia Telephony Service for IMS (MSMTSI) je komplexní specifikace služby definovaná 3GPP pro poskytování pokročilé telefonie přes sítě IP Multimedia Subsystem (IMS). Rozšiřuje základní Voice over LTE (VoLTE) o podporu více synchronizovaných mediálních komponent v rámci jedné SIP relace. Architektonicky spoléhá na IMS core (CSCFs), Telephony Application Server (TAS) a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) pro řízení a zpracování médií. Služba používá Session Description Protocol (SDP) pro komplexní mediální vyjednávání, což koncovým bodům umožňuje dynamicky během hovoru nabízet, přidávat, odebírat a upravovat více mediálních toků. Například typická relace MSMTSI může zahrnovat primární audio tok pro řeč, primární video tok z uživatelské kamery a sekundární video tok pro sdílení obrazovky nebo prezentaci, vše synchronizované a spravované jako souvislý hovor. Klíčovými zapojenými protokoly jsou SIP pro řízení relace a RTCP pro synchronizaci mediálních toků a zpětnou vazbu o kvalitě. Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)) může být použit pro pokročilé služby, jako je mixování mediálních toků nebo poskytování tónů a oznámení. MSMTSI definuje podrobné procedury pro navázání, modifikaci (např. přidání video toku během hovoru) a ukončení relace, čímž zajišťuje interoperabilitu mezi zařízeními a sítěmi od různých výrobců. Specifikuje také mechanismy kvality služeb (QoS), využívající architekturu Policy and Charging Control (PCC) k zajištění přidělení odpovídajících přenosových prostředků pro každý typ mediálního toku, což garantuje vysoce kvalitní uživatelský zážitek.

## K čemu slouží

MSMTSI bylo vytvořeno za účelem standardizace a obohacení multimediální telefonie za hranice jednoduchých hlasových a základních videohovorů. Před jeho specifikací byly multimediální služby často proprietární, což vedlo k fragmentaci a nedostatku interoperability mezi různými operátory a zařízeními. Problém, který řeší, je potřeba operátorské, standardizované služby schopné podporovat komplexní, vícekanálovou komunikaci, jako jsou videohovory se sdílením obsahu, které jsou klíčové pro obchodní spolupráci a vylepšené služby pro spotřebitele. Jeho vývoj byl motivován konvergencí telekomunikačních a [IT](/mobilnisite/slovnik/it/) služeb a snahou nabídnout funkčně bohatou, interoperabilní komunikaci jako konkurenceschopnou alternativu k over-the-top ([OTT](/mobilnisite/slovnik/ott/)) aplikacím. Díky založení na IMS umožňuje MSMTSI operátorům nabízet pokročilé, zpoplatnitelné služby se zaručenou kvalitou, integrované s dalšími IMS službami, jako je přítomnost a zasílání zpráv. Poskytuje technický základ pro komerční služby Rich Communication Services (RCS) a budoucí imerzivní komunikační zážitky.

## Klíčové vlastnosti

- Podporuje více synchronizovaných mediálních toků (audio, video, obsah) v jedné relaci
- Umožňuje dynamickou modifikaci relace (např. přidání videa nebo sdílení obrazovky během hovoru)
- Založeno na IMS a SIP pro standardizované, interoperabilní řízení služby
- Definuje procedury pro mediální vyjednávání, synchronizaci a správu QoS
- Integruje se s PCC pro zaručené přidělení přenosových prostředků na každý tok
- Poskytuje základ pro pokročilé obchodní a spotřebitelské telefonní služby

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.980** (Rel-19) — Multi-stream Multiparty Conferencing Media Handling

---

📖 **Anglický originál a plná specifikace:** [MSMTSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/msmtsi/)
