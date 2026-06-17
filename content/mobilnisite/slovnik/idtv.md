---
slug: "idtv"
url: "/mobilnisite/slovnik/idtv/"
type: "slovnik"
title: "IDTV – Integrated Digital Television (receiver)"
date: 2025-01-01
abbr: "IDTV"
fullName: "Integrated Digital Television (receiver)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/idtv/"
summary: "Digitální televizní přijímač, který integruje širokopásmový modem podle 3GPP, což mu umožňuje přijímat televizní služby prostřednictvím mobilních širokopásmových sítí (např. LTE, 5G NR) vedle nebo mís"
---

IDTV je digitální televizní přijímač s integrovaným širokopásmovým modemem podle 3GPP, který umožňuje příjem televize prostřednictvím mobilních sítí, jako je LTE nebo 5G NR, vedle nebo místo tradičních vysílacích kanálů.

## Popis

Přijímač integrované digitální televize (IDTV) v kontextu 3GPP označuje televizní přijímač nebo set-top box, který jako nedílnou součást své hardwarové a softwarové architektury obsahuje mobilní širokopásmový přijímač definovaný 3GPP (např. pro LTE nebo 5G New Radio). Toto konvergentní zařízení je navrženo pro příjem digitálních televizních a multimediálních služeb nejen prostřednictvím tradičních terestrických, kabelových nebo satelitních vysílacích tunerů, ale také prostřednictvím rozhraní mobilních sítí. Specifikace 3GPP, zejména pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její vyvinutou formu Further evolved MBMS (FeMBMS), definují protokoly a procedury pro doručování vysílacího a multicastového obsahu přes celulární sítě, které přijímač IDTV implementuje.

Z architektonického hlediska přijímač IDTV zahrnuje vedle svých schopností příjmu vysílání také modemovou zásobníkovou vrstvu 3GPP User Equipment (UE). To mu umožňuje připojit se k mobilní síti jako datové zařízení. Pro vysílací služby může přijímat MBMS/FeMBMS přenosy na vyhrazených oblastech multicast-broadcast single-frequency network ([MBSFN](/mobilnisite/slovnik/mbsfn/)) nebo v režimu single-cell point-to-multipoint (SC-PTM). Přijímač zpracovává všechny procedury nižších vrstev včetně synchronizace, demodulace a dekódování fyzického multicastového kanálu (PMCH). Na servisní vrstvě podporuje oznámení služby, její vyhledání a doručování audio, video a datových proudů, jak je definováno v 3GPP TS 26.346 pro MBMS a souvisejících specifikacích. Integrace umožňuje hybridní servisní modely, kde může být lineární televizní kanál doručován prostřednictvím efektivního vysílání, zatímco přidružený obsah na vyžádání, reklamy nebo interaktivní aplikace jsou načítány prostřednictvím unicastového spojení přes stejné rozhraní mobilní sítě.

Jak to funguje: přijímač IDTV prohledává dostupné mobilní sítě a služby MBMS. Registruje se v síti pro unicastové služby a přihlašuje se k přenosovým službám MBMS na základě uživatelského výběru nebo automatických servisních průvodců. Spravuje přidělování prostředků mezi vysílací a unicastové toky, případně využívaje stejnou rádiovou frekvenci v případě FeMBMS. Software přijímače zahrnuje mediální přehrávače, klienty [DRM](/mobilnisite/slovnik/drm/) a aplikační enginy schopné vykreslovat bohaté, interaktivní televizní zážitky, které plynule propojují vysílací a širokopásmový obsah, jak to předpokládají standardy jako HbbTV a [ATSC](/mobilnisite/slovnik/atsc/) 3.0 v kombinaci s doručováním podle 3GPP.

## K čemu slouží

Účelem definice přijímače integrované digitální televize (IDTV) ve standardech 3GPP je umožnit a standardizovat konvergenci vysílací televize a mobilních širokopásmových služeb v jediném zařízení. Řeší rostoucí poptávku po flexibilních, interaktivních a vysoce kvalitních video službách, které nejsou omezeny jednosměrnou povahou tradičního vysílání. Motivace vychází z potřeby efektivnějšího využití spektra, zlepšené odolnosti služeb a obohacení uživatelského zážitku.

Řeší několik klíčových problémů: Za prvé umožňuje vysílatelům a operátorům využívat infrastrukturu celulárních sítí (která je všudypřítomná) k poskytování televizních služeb, zejména v oblastech, kde je nasazení vyhrazených vysílacích věží nerentabilní. Za druhé umožňuje hybridní modely doručování, kde je oblíbený živý obsah efektivně vysílán mnoha uživatelům současně (šetří kapacitu sítě), zatímco personalizovaný obsah nebo obsah na vyžádání je doručován prostřednictvím unicastu. Tím se optimalizují celkové síťové zdroje. Za třetí poskytuje budoucí cestu pro televizní služby využívající pokročilé funkce mobilních sítí, jako je mobilita, obousměrná komunikace pro interaktivitu a bezproblémová integrace s internetovými službami. Vytvoření specifikací 3GPP pro přijímače IDTV bylo motivováno průmyslovými iniciativami ke sloučení vysílání a širokopásmového přístupu a poskytlo standardizovaný technický základ pro zařízení schopná přijímat služby jako LTE-based 5G Broadcast (FeMBMS), čímž se zajišťuje interoperabilita a podporuje rozvoj ekosystému pro televizi nové generace.

## Klíčové vlastnosti

- Integruje modem 3GPP (LTE/5G NR) pro širokopásmový přístup
- Podporuje příjem MBMS a FeMBMS pro vysílací/multicastovou TV
- Umožňuje hybridní doručování služeb kombinující vysílání a unicast
- Obsahuje standardizované mechanismy pro vyhledání a oznámení služby
- Schopen přijímat služby v režimech MBSFN nebo SC-PTM
- Umožňuje interaktivní televizní aplikace prostřednictvím obousměrné konektivity

## Související pojmy

- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [eNB – Evolved Node B](/mobilnisite/slovnik/enb/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [IDTV na 3GPP Explorer](https://3gpp-explorer.com/glossary/idtv/)
