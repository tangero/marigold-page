---
slug: "fdt"
url: "/mobilnisite/slovnik/fdt/"
type: "slovnik"
title: "FDT – FLUTE File Delivery Table"
date: 2025-01-01
abbr: "FDT"
fullName: "FLUTE File Delivery Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fdt/"
summary: "FDT je strukturovaná tabulka metadat používaná v protokolu FLUTE (File Delivery over Unidirectional Transport) k popisu souborů doručovaných v broadcastové nebo multicastové relaci. Poskytuje základní"
---

FDT je strukturovaná tabulka metadat používaná v protokolu FLUTE k popisu souborů v broadcastové relaci. Poskytuje informace, jako je umístění a velikost, pro spolehlivé doručování přes sítě MBMS.

## Popis

[FLUTE](/mobilnisite/slovnik/flute/) File Delivery Table (FDT) je klíčová součást protokolu FLUTE, standardizovaná [IETF](/mobilnisite/slovnik/ietf/) a přijatá v rámci 3GPP pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její vývojovou fázi (eMBMS). Jedná se o strukturu založenou na XML, která slouží jako manifest nebo katalog souborů v rámci FLUTE relace. Samotná FDT je přenášena jako speciální soubor v rámci relace, identifikovaný specifickým Transport Object Identifier (TOI). Obsahuje řadu prvků FDT Instance, z nichž každý poskytuje snímek souborů dostupných v daném časovém okamžiku. Každá položka souboru v rámci FDT Instance zahrnuje povinné atributy jako TOI, Content-Location (URI), Content-Length a Content-Type, spolu s volitelnými atributy, jako je délka přenosu, čas vypršení platnosti a parametry kódování obsahu (např. pro [FEC](/mobilnisite/slovnik/fec/)).

Hlavní provozní úlohou FDT je poskytnout přijímačům potřebná metadata pro správnou identifikaci, vyžádání (v případě opravných toků), znovusestavení a zpracování doručených souborových objektů. V jednosměrném broadcastovém scénáři jsou soubory opakovaně vysílány v karuselech. FDT je také karuselována, přičemž nové instance jsou publikovány pro přidání, úpravu nebo odstranění položek souborů. Přijímač se naladí na relaci, získá aktuální FDT a použije ji k mapování příchozích datových paketů (identifikovaných jejich TOI a čísly zdrojového bloku) na správný soubor a k určení, kdy byl kompletní soubor přijat. Pro spolehlivé doručování FDT zahrnuje informace pro dekódování Forward Error Correction (FEC), specifikující FEC encoding ID a instance ID použité pro každý soubor.

Z architektonického hlediska se FDT nachází v aplikační vrstvě zásobníku protokolu FLUTE. [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre) v síti 3GPP generuje a spravuje FDT pro danou MBMS relaci. Struktura a sémantika FDT jsou definovány jako rozšiřitelné, což umožňuje zahrnutí metadat specifických pro relaci nebo aplikaci v samostatných jmenných prostorech. To umožňuje pokročilé služby, jako jsou dynamické aktualizace playlistů pro streamování nebo informace pro podmíněný přístup. Její standardizovaný formát zajišťuje interoperabilitu mezi různým síťovým zařízením a uživatelskými terminály a tvoří nezbytný spojovací prvek, který propojuje doručování datových paketů na transportní vrstvě s konzumací kompletních souborů na aplikační vrstvě.

## K čemu slouží

FDT byla vytvořena k řešení základního problému doručování diskrétních, identifikovatelných souborů přes jednosměrné, best-effort IP multicastové nebo broadcastové kanály. Před protokolem [FLUTE](/mobilnisite/slovnik/flute/) a FDT používaly broadcastové systémy často proprietární metody zapouzdření, což ztěžovalo rozsáhlé a interoperabilní doručování souborů. FDT poskytuje standardizovaný, flexibilní a efektivní mechanismus pro oznámení a popis souborového obsahu v rámci relace. To umožňuje přijímačům, které se mohou k relaci připojit kdykoli, okamžitě zjistit, jaké soubory jsou doručovány a jak je zpracovat, aniž by se spoléhaly na signalizaci mimo přenosovou cestu nebo předem nakonfigurované znalosti.

Její vývoj byl motivován vzestupem [MBMS](/mobilnisite/slovnik/mbms/) v 3GPP, jehož cílem bylo umožnit efektivní point-to-multipoint služby, jako je mobilní TV, aktualizace softwaru a skupinová komunikace. Tyto služby vyžadovaly spolehlivý mechanismus doručování souborů, který by mohl škálovat na miliony zařízení. FDT řeší omezení jednoduchých datových karuselů tím, že poskytuje bohatá metadata, podporuje pokročilé funkce, jako je [FEC](/mobilnisite/slovnik/fec/) pro spolehlivost, kompresi obsahu a dynamické aktualizace. Abstrahuje složitost podkladového transportu, což umožňuje vývojářům aplikací soustředit se na tvorbu obsahu, zatímco protokol FLUTE, řízený FDT, zvládá logistiku doručování, znovusestavení a ověření.

## Klíčové vlastnosti

- Struktura metadat založená na XML pro popis atributů souborů
- Podporuje dynamické aktualizace relace prostřednictvím karuselovaných instancí FDT
- Obsahuje povinné identifikátory souborů (TOI, Content-Location, velikost, typ)
- Nese informace o schématu Forward Error Correction (FEC) pro každý soubor
- Umožňuje rozšiřitelnost prostřednictvím jmenných prostorů XML pro data specifická pro aplikaci
- Umožňuje efektivní činnost přijímače mapováním transportních paketů na aplikační soubory

## Související pojmy

- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.827** (Rel-12) — IMS-based Streaming & Download Delivery Enhancements
- **TS 26.848** (Rel-12) — Enhanced MBMS for DASH over broadcast/unicast
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.947** (Rel-19) — FEC Evaluation for MBMS Enhancement
- **TS 33.246** (Rel-19) — MBMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [FDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/fdt/)
