---
slug: "sdt"
url: "/mobilnisite/slovnik/sdt/"
type: "slovnik"
title: "SDT – Service Description Table"
date: 2026-01-01
abbr: "SDT"
fullName: "Service Description Table"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdt/"
summary: "SDT je datová struktura v rozhlasových/vícekanálových službách, která poskytuje úplný seznam a popis dostupných služeb nebo obsahových komponent. Slouží jako průvodce pro přijímače, umožňuje jim objev"
---

SDT je datová struktura v rozhlasových/vícekanálových službách, která poskytuje úplný seznam a popis dostupných služeb, aby umožnila přijímačům objevovat, vybírat a dekódovat datové proudy.

## Popis

Service Description Table (SDT) je klíčová signalizační tabulka používaná v rámcích pro doručování rozhlasových a vícekanálových služeb 3GPP, jako je Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)). Jedná se o strukturovaný datový soubor, který poskytuje popisná metadata o službách dostupných v rámci rozhlasového datového proudu. SDT vypisuje každou službu, přiřazuje jí jedinečný identifikátor a poskytuje informace nezbytné pro přijímač k přístupu a interpretaci této služby, jako je název služby, typ služby a odkazy na další zásadní tabulky nebo komponenty.

Z architektonického hlediska je SDT generován poskytovatelem rozhlasové služby nebo sítí a je multiplexován do transportního proudu (např. [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) relace v MBMS) nebo doručován prostřednictvím aplikačního protokolu. Funguje ve spojení s dalšími tabulkami, jako je Program Map Table ([PMT](/mobilnisite/slovnik/pmt/)) nebo Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) v streamování založeném na [DASH](/mobilnisite/slovnik/dash/). Mezi klíčové komponenty záznamu SDT patří service_id, service_descriptors (které mohou obsahovat textové názvy, informace o poskytovateli a klasifikaci typu služby) a odkazy na další deskriptory, které mohou indikovat umístění dat elektronického průvodce službami ([ESG](/mobilnisite/slovnik/esg/)) nebo komponentních proudů. Přijímač analyzuje SDT, aby vytvořil pro uživatele prezentovatelný seznam dostupných služeb.

Jeho úlohou je sloužit jako primární mechanismus pro objevování služeb v rámci rozhlasové/vícekanálové relace. Bez SDT by přijímač viděl pouze surový datový proud bez znalosti toho, jaké služby (např. TV kanál, rozhlasová stanice, relace pro doručování souborů) obsahuje, nebo jak je dekódovat. Je proto zásadní pro interakci s uživatelem, umožňuje přepínání kanálů, výběr služeb a zajišťuje, že přijímač nakonfiguruje správné dekodéry pro audio, video nebo datové komponenty spojené s vybranou službou.

## K čemu slouží

SDT byl vytvořen k řešení problému objevování a identifikace služeb v IP-based rozhlasových a vícekanálových systémech. V tradičním digitálním televizním vysílání (jako DVB) tuto úlohu plní podobné tabulky (např. DVB-SI). Když 3GPP vyvíjelo MBMS pro doručování multimédií přes mobilní sítě, byla potřeba standardizovaná, efektivní metoda pro popis služeb v rámci IP vícekanálového toku, což motivovalo přijetí a adaptaci konceptu SDT.

Základní problém, který řeší, je informování uživatelského zařízení o tom, 'co je k dispozici' v oblasti rozhlasové služby. Před jeho standardizací by proprietární nebo neinteroperabilní metody bránily rozšířenému přijetí rozhlasových služeb, protože přijímač každého výrobce by mohl potřebovat vlastní logiku k nalezení služeb. SDT poskytuje univerzální, dobře definovaný formát, který zajišťuje, že jakýkoli kompatibilní přijímač dokáže objevit všechny služby nabízené jakýmkoli operátorem sítě.

Překonává omezení čistého IP multicastu, kde se přijímač může připojit k vícekanálové skupině, ale nemá žádné inherentní informace o povaze obsahu nebo o tom, jak jej prezentovat. SDT přidává tato zásadní metadata služební vrstvy, čímž činí rozhlasové služby uživatelsky přívětivými a interoperabilními. Jeho vývoj napříč vydáními odráží rozšíření případů užití rozhlasu od služeb MBMS/TV až po zahrnutí veřejného varování, automobilového průmyslu a 5G broadcastu, což vyžaduje sofistikovanější popisy služeb a integraci se streamovacími protokoly, jako je DASH.

## Klíčové vlastnosti

- Poskytuje úplný seznam všech služeb v rozhlasové/vícekanálové relaci
- Obsahuje popisná metadata, jako jsou názvy služeb a informace o poskytovateli
- Přiřazuje službu jejím komponentním proudům (audio, video, data)
- Odkazuje na další zásadní signalizační tabulky nebo elektronické průvodce službami (ESG)
- Používá standardizovanou strukturu tabulky pro zaručenou interoperabilitu
- Podporuje dynamické aktualizace, které odrážejí změny v dostupných službách

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.887** (Rel-12) — Architectural enhancements for MTC and mobile data
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [SDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdt/)
