---
slug: "mmt"
url: "/mobilnisite/slovnik/mmt/"
type: "slovnik"
title: "MMT – MPEG Media Transport"
date: 2025-01-01
abbr: "MMT"
fullName: "MPEG Media Transport"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmt/"
summary: "MMT je standard MPEG pro balení a doručování multimediálního obsahu přes IP sítě. Je navržen pro efektivní streamování a vysílání kvalitního videa a audia a podporuje funkce jako multiplexování, synch"
---

MMT je standard MPEG pro balení a doručování multimediálního obsahu přes IP sítě, navržený pro efektivní streamování a vysílání kvalitního videa a audia s funkcemi jako multiplexování a synchronizace.

## Popis

[MPEG](/mobilnisite/slovnik/mpeg/) Media Transport (MMT) je mezinárodní standard [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) (ISO/IEC 23008-1) vyvinutý skupinou MPEG pro doručování kódovaných mediálních dat přes paketové sítě. Definuje sadu protokolů a formátů pro zapouzdření, doručování a synchronizaci multimediálního obsahu včetně videa, audia a přidružených metadat. MMT je navržen jako nezávislý na síti, efektivně funguje v heterogenních sítích jako jsou vysílací, širokopásmové a mobilní sítě, což jej činí vhodným pro konvergované služby. Architektura se skládá z několika klíčových logických entit: MMT Package, což je logická kolekce mediálního obsahu a jeho prezentačních informací; MMT Signaling Message, používaná pro navázání relace a popis médií; a MMT Protocol ([MMTP](/mobilnisite/slovnik/mmtp/)), což je doručovací protokol pro přenos MMT Packages. MMT funguje tak, že zapouzdřuje mediální data do MMT Payload Units ([MPU](/mobilnisite/slovnik/mpu/)) a následně do MMT Protocol Data Units (MMTP PDU) pro přenos. Tyto PDU jsou přenášeny přes transportní protokoly jako UDP/IP. MMT podporuje funkce jako multiplexování více mediálních komponent do jediného toku, časování a synchronizaci pomocí Composition Information ([CI](/mobilnisite/slovnik/ci/)) a Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)) pro odolnost vůči chybám. V kontextu 3GPP je MMT odkazováno pro aplikace doručování médií, zejména ve specifikacích týkajících se multimediálních služeb a streamování. Poskytuje standardizovanou metodu pro balení a streamování médií, kterou mohou služby 3GPP využít pro efektivní distribuci obsahu. Návrh MMT umožňuje adaptivní streamovací scénáře, kde lze obsah dynamicky přizpůsobovat na základě síťových podmínek, čímž se zlepšuje uživatelský zážitek. Protokol také podporuje integraci se systémy Digital Rights Management ([DRM](/mobilnisite/slovnik/drm/)) pro zabezpečené doručování obsahu. Celkově slouží MMT jako robustní rámec pro přenos médií nové generace, usnadňující kvalitní, synchronizované a spolehlivé multimediální zážitky napříč různými přenosovými sítěmi.

## K čemu slouží

MMT bylo vytvořeno, aby řešilo omezení předchozích protokolů pro přenos médií, jako je MPEG-2 Transport Stream (TS), které byly primárně navrženy pro vysílací prostředí a méně vhodné pro IP-bázi interaktivní služby. Rozšíření vysokorychlostních mobilních sítí (např. LTE, 5G) a poptávka po bohatých multimediálních zážitcích si vyžádaly flexibilnější a efektivnější přenosový mechanismus. MMT si klade za cíl poskytnout jednotné řešení pro doručování médií přes paketové sítě, podporující jak streamovací, tak stahovací scénáře, a zároveň umožňující pokročilé funkce jako hybridní vysílání a širokopásmové doručování. Historicky se doručování médií přes IP spoléhalo na protokoly jako RTP/RTCP pro streamování a HTTP pro adaptivní streamování (např. DASH). Ty však často postrádaly nativní podporu pro efektivní multiplexování, synchronizaci a obnovu po chybách v heterogenních síťových podmínkách. MMT bylo vyvinuto, aby tuto mezeru zaplnilo, a nabízí standardizovaný, integrovaný přístup, který zjednodušuje implementaci a zlepšuje výkon. Je motivováno zejména potřebou podporovat video Ultra-High Definition (UHD), imerzivní audio a interaktivní služby, které vyžadují nízkou latenci, vysokou spolehlivost a přesnou synchronizaci. Poskytnutím společného rámce MMT usnadňuje interoperabilitu mezi různými zařízeními a sítěmi, snižuje složitost pro poskytovatele služeb a zlepšuje zážitek koncového uživatele.

## Klíčové vlastnosti

- Efektivní balení multimediálního obsahu do MMT Packages
- Podpora multiplexování více mediálních komponent (video, audio, titulky) do jediného datového toku
- Mechanismy časování a synchronizace využívající Composition Information (CI) a časová metadata
- Funkce odolnosti vůči chybám včetně Forward Error Correction (FEC) a podpory pro opakovaný přenos
- Návrh nezávislý na síti, vhodný pro vysílací, širokopásmové a mobilní sítě
- Integrace s adaptivním streamováním a dynamické přizpůsobení síťovým podmínkám

## Související pojmy

- [MMTP – MPEG Media Transport Protocol](/mobilnisite/slovnik/mmtp/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MPEG – Moving Pictures Experts Group](/mobilnisite/slovnik/mpeg/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [MMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmt/)
