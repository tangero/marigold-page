---
slug: "uus"
url: "/mobilnisite/slovnik/uus/"
type: "slovnik"
title: "UUS – User-to-User Signalling Supplementary Service"
date: 2025-01-01
abbr: "UUS"
fullName: "User-to-User Signalling Supplementary Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uus/"
summary: "Doplňková služba v sítích 3GPP, která umožňuje účastníkům vyměňovat omezená uživatelem definovaná data během sestavování hovoru nebo za aktivního hovoru. Umožňuje aplikace, jako je odesílání identity"
---

UUS (User-to-User Signalling) je doplňková služba, která umožňuje účastníkům vyměňovat omezená uživatelem definovaná data, jako je identita volajícího nebo krátké zprávy, uvnitř signalizace volání během jeho sestavování nebo během aktivního hovoru.

## Popis

Doplňková služba signalizace mezi uživateli (User-to-User Signalling, UUS) je služba přepojování okruhů standardizovaná 3GPP, která usnadňuje přenos malého množství uživateli generovaných informací mezi dvěma účastníky. Tento přenos probíhá transparentně sítí pomocí signalizační cesty, konkrétně uvnitř zpráv [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo [DSS1](/mobilnisite/slovnik/dss1/) (Digital Subscriber Signalling System No. 1), nikoli prostřednictvím hlasového přenosového kanálu. Služba je architektonicky integrována do řídicích funkcí hovoru v jádru sítě, nachází se v Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) pro mobilní sítě nebo v ekvivalentních ústřednách ve fixních sítích. Funguje tak, že volající nebo volaná strana může zahrnout informační prvek UUS do zpráv pro sestavení hovoru (jako SETUP, ALERTING, CONNECT) nebo během aktivní fáze hovoru prostřednictvím zpráv FACILITY.

Služba se dále dělí na tři samostatné služby: [UUS1](/mobilnisite/slovnik/uus1/), [UUS2](/mobilnisite/slovnik/uus2/) a [UUS3](/mobilnisite/slovnik/uus3/), ke kterým se může účastník přihlásit a které může používat nezávisle. Úlohou sítě je především tento uživatelská data transparentně přenášet, provádět základní kontroly předplatného služby a délkových omezení, ale neinterpretovat obsah. Data jsou typicky omezena na 128 oktetů (pro UUS1 a UUS2 v režimu asociovaném s hovorem) a mohou být použita pro různé aplikace definované uživatelem nebo vyššími vrstvami, jako je přenos čísla telefonní karty, krátké textové poznámky nebo servisního kódu. Signalizace je přenášena buď asociovaně s hovorem, kdy jsou data UUS vložena do řídicích zpráv hovoru, nebo neasociovaně s hovorem pomocí samostatných signalizačních zpráv nezávislých na stavu hovoru, ačkoli druhá varianta je méně běžně implementována.

Z pohledu protokolu UUS využívá stávající řídicí protokoly hovoru. V mobilní jádrové síti využívá [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) pro interakce řízení služeb s HLR a CAP (CAMEL Application Part) pro interakce v inteligentní síti, je-li to potřeba. Na rozhraní uživatel-síť (UNI) používá protokoly jako DSS1. Její implementace vyžaduje podporu jak od koncového zařízení (UE) pro generování a zobrazení informací, tak od sítě pro jejich přenos. Ačkoli je tato služba spojována především s okruhově spínanými doménami 2G (GSM) a 3G (UMTS), její principy ovlivnily pozdější koncepty signalizace v pásmu, i když ve srovnání se službou SMS se dočkala omezeného rozšíření mezi běžnými uživateli.

## K čemu slouží

UUS byla vytvořena, aby uspokojila potřebu jednoduchého přenosu uživatelem definovaných dat s nízkou latencí v souvislosti s hlasovým hovorem, bez nutnosti samostatného datového kanálu nebo služby jako SMS. V rané éře digitální telefonie ISDN a GSM rostla poptávka po přidaných službách, které by mohly vylepšit základní hlasové hovory. Před UUS vyžadovala výměna malého množství dat během sestavování nebo průběhu hovoru buď verbální komunikaci, samostatný datový hovor, nebo později SMS, která fungovala na jiném signalizačním kanálu s principem ulož a předej a znamenala zpoždění. UUS tento problém vyřešila přidružením dat k signalizační cestě hovoru v reálném čase.

Historický kontext vychází z ISDN, kde byl v signalizaci Q.931 definován informační prvek 'User-to-User Information'. 3GPP jej přijala a standardizovala jako doplňkovou službu pro GSM a UMTS, aby zachovala funkční paritu s fixními sítěmi ISDN a umožnila nové možnosti služeb. Cílem bylo usnadnit aplikace, jako je zabezpečená identita volajícího (nad rámec CLI), přenos čísel účtů pro automatizované systémy nebo jednoduchá výměna textu během pokusu o hovor. Jejímu rozšíření však bránila omezená podpora terminálů, nástup všudypřítomné SMS a později IP-based messaging, což ji omezilo především na specializované podnikové aplikace a aplikace pro interoperabilitu sítí.

## Klíčové vlastnosti

- Umožňuje přenos uživatelem definovaných dat (až 128 oktetů) uvnitř signalizace řízení hovoru
- Funguje transparentně přes síť bez interpretace obsahu
- Nabízí tři nezávislé typy služeb (UUS1, UUS2, UUS3) s různými body spuštění
- Podporuje jak režim signalizace asociované s hovorem (během sestavování/aktivního hovoru), tak neasociované s hovorem
- Implementována jako doplňková služba 3GPP vyžadující předplatné a zřízení v síti
- Pro přenos a řízení využívá stávající protokoly ISUP, MAP a DSS1

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.087** (Rel-19) — User-to-User Signalling (UUS) Supplementary Service
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 23.097** (Rel-19) — Multiple Subscriber Profile (MSP) Phase 2
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.087** (Rel-19) — User-to-User Signalling (UUS) Stage 3
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [UUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/uus/)
