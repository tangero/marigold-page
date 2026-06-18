---
slug: "vps"
url: "/mobilnisite/slovnik/vps/"
type: "slovnik"
title: "VPS – Visual Positioning System"
date: 2025-01-01
abbr: "VPS"
fullName: "Visual Positioning System"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vps/"
summary: "Systém, který využívá vizuální data, například snímky nebo video z kamery zařízení, k určení přesné polohy a orientace zařízení. Vylepšuje služby založené na poloze, zejména v prostředích bez GPS sign"
---

VPS je systém, který využívá vizuální data z kamery zařízení k určení jeho přesné polohy a orientace, čímž vylepšuje služby jako je polohování v interiérech a navigace v rozšířené realitě.

## Popis

Visual Positioning System (VPS) je služební schopnost v sítích 3GPP navržená k poskytování vysoce přesného polohování prostřednictvím využití vizuálních informací z uživatelského zařízení (UE). Na rozdíl od tradičních metod spoléhajících pouze na rádiové signály (např. [GNSS](/mobilnisite/slovnik/gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/)) VPS analyzuje vizuální prvky ze záznamu kamery zařízení. Základní architektura zahrnuje UE, které pořizuje snímky nebo video, extrahuje vizuální prvky (jako klíčové body a deskriptory) a odesílá tato data na síťový polohovací server, často prostřednictvím Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) nebo vyhrazeného VPS serveru. Server tyto prvky porovnává s předem vytvořenou vizuální mapou nebo databází georeferencovaných vizuálních orientačních bodů. Porovnáním pozorovaných prvků se známými polohami v databázi server vypočítá přesnou 3D polohu UE (zeměpisná šířka, délka, nadmořská výška) a orientaci (odchylka, náklon, rotace), a tento odhad následně vrátí UE nebo žádající aplikaci.

Klíčové komponenty zahrnují UE s kamerou a zpracovatelskými schopnostmi, databázi vizuální mapy (která může být cloudová nebo distribuovaná) a polohovací server, který provádí porovnávací algoritmy. VPS server může také sloučit výsledek vizuálního polohování s dalšími senzorickými vstupy z UE, jako jsou data z inerciální měřicí jednotky ([IMU](/mobilnisite/slovnik/imu/)), otisky Wi-Fi nebo měření z buněčné sítě, aby zvýšil přesnost, robustnost a kontinuitu, zejména v obdobích špatného sledování vizuálních prvků. Systém typicky funguje ve spojení s LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo NR Positioning Protocol (NRPPa) pro signalizační výměnu mezi UE a sítí.

Úlohou VPS je doplnit a vylepšit celkový rámec polohování 3GPP definovaný v specifikacích jako 23.273. Řeší scénáře, kde je polohování založené na rádiových signálech nedostatečné, například v hustých městských kaňonech nebo vnitřních prostředích, kde jsou satelitní signály slabé nebo blokované. Služba umožňuje novou třídu aplikací vyžadujících přesnost na úrovni centimetrů až metrů a odhad polohy se šesti stupni volnosti (6DoF), což je klíčové pro imerzivní rozšířenou realitu ([AR](/mobilnisite/slovnik/ar/)), přesnou navigaci v interiérech a služby reagující na kontext. Integrace do standardů 3GPP zajišťuje, že VPS může být nasazena jako spravovaná, škálovatelná služba s definovanou kvalitou služby, zabezpečením a kontrolami soukromí.

## K čemu slouží

VPS byl vytvořen, aby vyřešil základní omezení stávajících polohovacích technologií založených na rádiových frekvencích v prostředích se špatným pokrytím satelitním nebo buněčným signálem, zejména v interiérech a v hustých městských oblastech. Tradiční metody jako [GPS](/mobilnisite/slovnik/gps/), [A-GNSS](/mobilnisite/slovnik/a-gnss/) a OTDOA v takových scénářích často selhávají nebo poskytují nedostatečnou přesnost (desítky metrů), což brání vývoji přesných služeb založených na poloze. Rozšíření chytrých telefonů s kvalitními kamerami a pokročilou výpočetní silou představovalo příležitost využít vizuální data jako bohatý zdroj polohovacích informací, což motivovalo jeho standardizaci pro zajištění interoperability a rozsáhlého nasazení.

Historický kontext zahrnuje rostoucí poptávku po aplikacích rozšířené reality, přesné navigaci v interiérech (např. na letištích, v nákupních centrech, muzeích) a průmyslové automatizaci, které všechny vyžadují přesný odhad polohy. Před VPS se řešení spoléhala na proprietární technologie, majáčky nebo otiskování, kterým chyběla standardizace a škálovatelnost. Integrací VPS do ekosystému 3GPP, počínaje ranými studiemi v R99 a konkrétnější prací v pozdějších vydáních, bylo cílem poskytnout jednotnou, síťově asistovanou polohovací službu, která využívá všudypřítomnost mobilních kamer. Tím se řeší omezení předchozích přístupů tím, že nabízí řešení fungující tam, kde jsou RF signály slabé, poskytuje data o orientaci a může být hladce integrováno s dalšími buněčnými službami pro konzistentní uživatelský zážitek.

## Klíčové vlastnosti

- Pro polohování využívá porovnávání vizuálních prvků s georeferencovanou databází
- Poskytuje odhad polohy se šesti stupni volnosti (6DoF) (pozice a orientace)
- Funguje v prostředích bez GPS signálu, jako jsou interiéry a městské kaňony
- Síťově asistovaná architektura s polohovacím serverem a daty vizuální mapy
- Sloučení s dalšími senzorovými daty (IMU, Wi-Fi, buněčná síť) pro zvýšenou robustnost
- Standardizovaná signalizace prostřednictvím LPP/NRPPa pro interoperabilitu

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [VPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vps/)
