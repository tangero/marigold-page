---
slug: "ifs"
url: "/mobilnisite/slovnik/ifs/"
type: "slovnik"
title: "IFS – Information Field Sizes"
date: 2025-01-01
abbr: "IFS"
fullName: "Information Field Sizes"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifs/"
summary: "Standardizované definice maximálních bitových délek datových polí v rámci protokolových zpráv a informačních elementů 3GPP. Zajišťují interoperabilitu mezi síťovými prvky a uživatelskými zařízeními de"
---

IFS je standardizovaná definice maximálních bitových délek pro datová pole v rámci protokolových zpráv 3GPP, která zajišťuje interoperabilitu definováním přesných struktur pro kódování a dekódování.

## Popis

Information Field Sizes (IFS) jsou základní specifikace v rámci 3GPP, které definují přesné bitové délky různých polí používaných v telekomunikačních protokolech. Tyto velikosti jsou detailně dokumentovány v technických specifikacích, jako je TS 21.905 (Vocabulary for 3GPP Specifications), a jsou aplikovány napříč více protokolovými vrstvami, včetně Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a signalizačních protokolů jádra sítě, jako jsou Diameter a [MAP](/mobilnisite/slovnik/map/). Každý IFS určuje maximální počet bitů nebo oktetů přidělených pro konkrétní informaci, jako je identifikátor, čítač, adresa nebo parametr. Například IFS může specifikovat, že Temporary Mobile Subscriber Identity (TMSI) má délku 32 bitů nebo že parametr QoS je reprezentován 16 bity. Tato přesná definice je klíčová pro procesy kódování a dekódování v Abstract Syntax Notation One (ASN.1), zajišťující, že odesílatel zakóduje zprávu v rámci definovaných velikostních omezení a příjemce může příchozí bitový proud správně zpracovat.

Z architektonického hlediska jsou IFS zabudovány do fáze návrhu protokolu a jsou reflektovány v definicích modulů ASN.1, které jsou základem signalizace 3GPP. Když je konstruována protokolová datová jednotka (PDU), každé pole je vyplněno podle svého IFS, s případným doplněním (padding) nebo zkrácením, aby byla splněna požadovaná velikost. K tomu dochází v protokolových entitách specifických pro danou vrstvu uvnitř síťových uzlů (např. [MME](/mobilnisite/slovnik/mme/), [AMF](/mobilnisite/slovnik/amf/), gNB) a uživatelského zařízení (UE). Konzistence vynucovaná IFS zaručuje, že zpráva vygenerovaná UE od jednoho výrobce může být přesně interpretována síťovým prvkem od jiného, což umožňuje interoperabilitu mezi více dodavateli. Dále IFS ovlivňují alokaci paměti v softwarových implementacích a hardwarových vyrovnávacích pamětech, protože vývojáři předem alokují struktury na základě těchto definovaných velikostí.

Role IFS přesahuje základní interoperabilitu a ovlivňuje také efektivitu sítě a její vývoj. Pevné velikosti polí umožňují optimalizované parsovací algoritmy a rychlejší zpracování, což je zásadní pro splnění cílů nízké latence v 5G. Poskytují také rámec pro zpětnou a dopřednou kompatibilitu; když nová funkce vyžaduje rozšířené pole, může být IFS aktualizován v pozdější verzi specifikace, často s pravidly pro zpracování staršími entitami (např. ignorování neznámých rozšíření). IFS jsou rovněž nedílnou součástí bezpečnostních mechanismů, protože definují délku kryptografických prvků, jako jsou autentizační tokeny. Stručně řečeno, IFS jsou základními 'stavebními předpisy' pro protokolové zprávy 3GPP, které zajišťují, že každý bit v rozsáhlém ekosystému mobilní komunikace je přesně definován a správně interpretován všemi kompatibilními entitami.

## K čemu slouží

Koncept Information Field Sizes existuje, aby vyřešil základní problém interoperability v komplexních globálních telekomunikačních systémech s více dodavateli. V počátcích standardů digitální buněčné komunikace, bez striktně definovaných velikostí polí, mohli různí výrobci zařízení implementovat odlišné interpretace protokolových zpráv, což vedlo k selhání spojení, poškození dat a výpadkům služeb. Vytvoření standardizovaných IFS v rámci specifikací 3GPP poskytlo jednoznačnou smlouvu mezi všemi síťovými prvky a uživatelskými zařízeními, která zajišťuje, že zpráva naformátovaná jednou entitou bude zpracovatelná jinou, bez ohledu na dodavatele.

IFS řeší potřebu efektivního a spolehlivého kódování dat. Specifikací maximálních velikostí umožňují implementátorům navrhovat vyrovnávací paměti pevné délky a optimalizované rutiny pro kódování/dekódování, což zvyšuje rychlost zpracování a snižuje paměťovou náročnost. To je obzvláště kritické pro signalizaci v reálném čase při správě mobility a zakládání relací. Dále IFS poskytují stabilní základ pro vývoj protokolů. Jak jsou přidávány nové služby a schopnosti (např. při přechodu z 3G na 4G a 5G), mohou být IFS rozšířeny nebo mohou být definována nová pole kontrolovaným způsobem, při zachování zpětné kompatibility. Starší zařízení mohou ignorovat nová, delší pole, kterým nerozumí, zatímco nová zařízení mohou využívat rozšířené informace, a to vše v rámci strukturovaného rámce, který zabraňuje kolapsu systému.

## Klíčové vlastnosti

- Definuje maximální bitovou/oktetovou délku pro informační elementy protokolu
- Zajišťuje interoperabilitu mezi více dodavateli v ekosystému 3GPP
- Základ pro pravidla kódování a dekódování ASN.1
- Umožňuje optimalizovanou alokaci paměti a zpracování v síťovém softwaru
- Podporuje vývoj protokolů s mechanismy zpětné kompatibility
- Aplikováno napříč signalizačními vrstvami NAS, RRC a jádra sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [IFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifs/)
