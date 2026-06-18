---
slug: "ii-nni"
url: "/mobilnisite/slovnik/ii-nni/"
type: "slovnik"
title: "II-NNI – Inter-IMS Network to Network Interface"
date: 2025-01-01
abbr: "II-NNI"
fullName: "Inter-IMS Network to Network Interface"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ii-nni/"
summary: "Standardizovaný referenční bod mezi dvěma sítěmi IP Multimedia Subsystem (IMS) od různých operátorů nebo administrativních domén. Umožňuje zabezpečené, funkčně bohaté propojení pro služby založené na"
---

II-NNI je standardizované rozhraní mezi sítěmi IMS dvou různých operátorů, které umožňuje zabezpečené propojení pro služby jako VoLTE a RCS.

## Popis

Inter-IMS Network to Network Interface (II-NNI) je klíčový standardizovaný referenční bod v architektuře IMS dle 3GPP. Definuje rozhraní mezi jádrovými sítěmi IMS dvou různých poskytovatelů služeb nebo administrativních domén. Primárním účelem II-NNI je usnadnit propojení sítí IMS za účelem podpory koncových služeb IMS mezi účastníky patřícími k různým operátorům. Technicky II-NNI není jediný fyzický spoj, ale logické rozhraní zahrnující sadu protokolů a procedur. Základním protokolem používaným přes II-NNI je Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)), rozšířený o hlavičky a parametry specifické pro 3GPP (jak definováno v TS 24.229) pro řízení relací. Vedle SIP toto rozhraní využívá Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) pro vyjednávání médií a Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) pro přenos médií. Klíčovou architektonickou komponentou je Interconnection Border Control Function ([IBCF](/mobilnisite/slovnik/ibcf/)), která funguje jako hraniční uzel na okraji každé sítě IMS. IBCF plní zásadní funkce, jako je skrytí topologie, překlad síťových adres/portů ([NAPT](/mobilnisite/slovnik/napt/)), filtrování a adaptace zpráv SIP a spolupráce mezi IPv4 a IPv6. Transition Gateway (TrGW), často umístěný společně s IBCF, zpracovává funkce v rovině médií, jako je přenos médií a v případě potřeby transkódování. II-NNI umožňuje navazování peer-to-peer relací (hlas, video, zasílání zpráv), optimalizaci registrační cesty a výměnu informací souvisejících se službami mezi sítěmi při zachování bezpečnosti, řízení politik a odděleného účtování.

## K čemu slouží

II-NNI bylo vytvořeno k vyřešení základního problému propojení mezi operátory pro pokročilé multimediální služby založené na IP, které poskytuje IMS. Před jeho standardizací mohli operátoři nasadit IMS jako izolovaný ostrov ve své vlastní síti, ale nabízet služby jako VoLTE nebo videohovory účastníkům v jiných sítích vyžadovalo proprietární brány nebo návrat k legacy okruhově přepínaným sítím. Motivací bylo umožnit bezproblémový zážitek ze služeb plně v IP napříč hranicemi operátorů, což je zásadní pro široké přijetí uživateli. Řeší omezení nestandardizovaného propojení, které vede k problémům s interoperabilitou, omezené bohatosti služeb a složitému správě sítí. Definováním standardizovaného rozhraní umožnil 3GPP operátorům přímo propojit jejich jádra IMS při zachování plné funkční sady služeb IMS (např. [HD](/mobilnisite/slovnik/hd/) hlasové kodeky, video, doplňkové služby) end-to-end. Toto byl klíčový krok ve vývoji od okruhově přepínané telefonie ke komunikaci plně v IP, který podpořil přechod odvětví k Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)) a zajistil, že IMS může plnit svou roli globální služební platformy.

## Klíčové vlastnosti

- Standardizované propojení založené na SIP a souvisejících protokolech IMS
- Využívá Interconnection Border Control Function (IBCF) jako hraniční prvek
- Podporuje skrytí topologie a bezpečnostní funkce mezi sítěmi operátorů
- Umožňuje kontinuitu služeb IMS end-to-end pro hlas, video a zasílání zpráv
- Usnadňuje meziodvětvové řízení politik, účtování a roamingové dohody
- Poskytuje mechanismy pro spolupráci IPv4/IPv6 a překonávání NAT

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [IBCF – Interconnection Border Control Functions](/mobilnisite/slovnik/ibcf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.865** (Rel-8) — Inter-IMS Network to Network Interface

---

📖 **Anglický originál a plná specifikace:** [II-NNI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ii-nni/)
