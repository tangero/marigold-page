---
slug: "fac"
url: "/mobilnisite/slovnik/fac/"
type: "slovnik"
title: "FAC – Fully Anechoic Chamber"
date: 2025-01-01
abbr: "FAC"
fullName: "Fully Anechoic Chamber"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fac/"
summary: "Stíněná místnost s absorbéry na všech plochách, která vytváří prostředí bez odrazů pro přesné testování antén a zařízení. Je nezbytná pro přesná vzduchem prováděná (OTA) měření vyzařovacího výkonu, kt"
---

FAC (Fully Anechoic Chamber, plně anechoická komora) je stíněná místnost s absorbéry na všech plochách, která vytváří prostředí bez odrazů pro přesné testování antén a zařízení vzduchem (Over-The-Air) za účelem splnění konformačních standardů 3GPP.

## Popis

Plně anechoická komora (FAC) je specializované elektromagnetické testovací prostředí navržené k simulaci stavu volného prostoru bez odrazů. Její konstrukce se skládá ze stíněného prostoru, typicky vyrobeného z vodivého kovu (jako ocel nebo hliník), který blokuje vnější rádiové rušení. Vnitřní stěny, strop a podlaha jsou obloženy pyramidálními nebo klínovými [RF](/mobilnisite/slovnik/rf/) absorbéry, vyrobenými z pěny s příměsí uhlíku nebo z feritových dlaždic. Tyto absorbéry minimalizují odrazy přeměnou dopadající elektromagnetické energie na teplo, čímž účinně vytvářejí anechoické podmínky až k určené nízké mezní frekvenci. Velikost komory je pečlivě navržena na základě požadovaného testovacího objemu, frekvenčního rozsahu a velikosti testovaného zařízení ([EUT](/mobilnisite/slovnik/eut/)), jako je uživatelské zařízení (UE) nebo anténa základnové stanice.

Hlavním provozním principem je vytvoření tiché zóny, což je objemová oblast uvnitř komory, kde je pole rovnoměrné a odrazy jsou pod požadovanou prahovou hodnotou (např. -40 dB). Toho je dosaženo přesným umístěním absorbérů, geometrií komory a někdy použitím dodatečných reflektorů nebo čoček. Při testování je EUT umístěno na pozicionovacím systému (často otočný stůl a stožár) uvnitř této tiché zóny. Měřící anténa, připojená k vektorovému analyzátoru sítí nebo komunikačnímu testeru, je umístěna v pevné vzdálenosti. Systém pak měří vyzařovací parametry, jako je celkový vyzářený výkon ([TRP](/mobilnisite/slovnik/trp/)), celková izotropní citlivost (TIS), charakteristiky vyzařovacích diagramů a nežádoucí emise.

V kontextu 3GPP je FAC klíčová pro konformační testování vzduchem ([OTA](/mobilnisite/slovnik/ota/)), jak je specifikováno v dokumentech jako 38.124 pro NR. Poskytuje řízené, opakovatelné prostředí k ověření, že zařízení splňují přísné požadavky na vyzařovací výkon pro technologie od 3G UMTS až po 5G NR a dále. Bez takové komory by byla měření zkreslena vícepaprsčitými odrazy z okolí a vnějším šumem, což by vedlo k nepřesným a neopakovatelným výsledkům. FAC je proto základním nástrojem v procesech výzkumu a vývoje, certifikace a zajištění kvality jakéhokoli bezdrátového zařízení, neboť zajišťuje jeho spolehlivý výkon v reálných sítích.

## K čemu slouží

FAC existuje, aby řešila základní problém přesného měření vyzařovacího výkonu antén a bezdrátových zařízení v řízeném laboratorním prostředí. Před rozšířeným používáním anechoických komor se testování antén často provádělo na otevřených testovacích místech ([OATS](/mobilnisite/slovnik/oats/)) nebo v odrazných místnostech, které byly náchylné k rušení z prostředí, povětrnostním podmínkám a vícepaprsčitým odrazům. Tato omezení činila měření nekonzistentními, neopakovatelnými a velmi závislými na konkrétním testovacím místě a denní době.

Vznik FAC byl motivován potřebou přesnosti a opakovatelnosti v rodícím se oboru bezdrátové komunikace. Jak se buněčné standardy vyvíjely od 2G k 5G, s rostoucími frekvencemi, širšími šířkami pásma a zaváděním složitých víceanténních systémů ([MIMO](/mobilnisite/slovnik/mimo/), beamforming), rostla poptávka po přesné charakterizaci prostorových vyzařovacích diagramů a celkového vyzářeného výkonu exponenciálně. FAC poskytuje izolované, odrazů prosté prostředí nezbytné k oddělení vlastního výkonu zařízení od vlivu testovacího prostředí. Tento požadavek se stal prvořadým pro konformační testování 3GPP a regulační certifikaci (např. orgány jako [FCC](/mobilnisite/slovnik/fcc/) a [ETSI](/mobilnisite/slovnik/etsi/)).

Historicky vývoj lepších materiálů pro RF absorbéry a technik návrhu komor umožnil FAC pracovat na vyšších frekvencích (až do milimetrových vln pro 5G NR) s většími tichými zónami. Tento vývoj přímo podporuje testování pokročilých anténních systémů a zajišťuje, že zařízení jako smartphony, IoT moduly a základnové stanice splňují přísná výkonnostní kritéria definovaná ve specifikacích 3GPP, čímž garantují kvalitu sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Elektromagnetické stínění blokující vnější RF rušení
- Vnitřek (stěny, strop, podlaha) obložený RF absorbéry pro minimalizaci odrazů
- Definovaná tichá zóna s nízkou úrovní odrazů pole (např. < -40 dB)
- Podpora metodik testování vzduchem (OTA)
- Integrace s přesnými pozicovacími systémy (otočné stoly, stožáry)
- Schopnost testovat v širokém frekvenčním rozsahu (např. od sub-6 GHz po mmWave)

## Související pojmy

- [OTA – Over The Air](/mobilnisite/slovnik/ota/)
- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 38.124** (Rel-19) — NR UE EMC Requirements

---

📖 **Anglický originál a plná specifikace:** [FAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fac/)
