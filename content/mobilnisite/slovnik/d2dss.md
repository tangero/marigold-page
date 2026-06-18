---
slug: "d2dss"
url: "/mobilnisite/slovnik/d2dss/"
type: "slovnik"
title: "D2DSS – Device-to-Device Synchronization Signal"
date: 2018-01-01
abbr: "D2DSS"
fullName: "Device-to-Device Synchronization Signal"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/d2dss/"
summary: "D2DSS je synchronizační signál vysílaný zařízeními v LTE Proximity Services (ProSe) pro umožnění přímé komunikace mezi zařízeními. Umožňuje uživatelskému zařízení (UE) synchronizovat časování a frekve"
---

D2DSS je synchronizační signál vysílaný zařízeními v LTE ProSe, který umožňuje přímou komunikaci tím, že umožňuje uživatelskému zařízení synchronizovat časování a frekvenci se sousedními zařízeními.

## Popis

Device-to-Device Synchronization Signal (D2DSS) je klíčový signál fyzické vrstvy definovaný v rámci LTE pro Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a později rozšířený pro [V2X](/mobilnisite/slovnik/v2x/). Jeho primární funkcí je vytvořit a udržovat synchronizaci mezi uživatelskými zařízeními (UE) pracujícími v režimu přímé komunikace, známém jako sidelink. Na rozdíl od tradiční buněčné komunikace, kde se UE synchronizují s primárními a sekundárními synchronizačními signály eNodeB ([PSS](/mobilnisite/slovnik/pss/)/[SSS](/mobilnisite/slovnik/sss/)), umožňuje D2DSS zařízením stát se synchronizačními zdroji pro jiná zařízení a vytvářet tak decentralizovanou synchronizační hierarchii. To je nezbytné pro scénáře, kde není pokrytí sítí, je nespolehlivé, nebo kde je přímá komunikace preferována z důvodu latence nebo efektivity.

Z architektonického hlediska D2DSS funguje uvnitř fyzické vrstvy sidelink, konkrétně na rozhraní PC5. Zařízení schopné vysílat D2DSS může fungovat v jedné ze dvou rolí: zařízení v pokrytí, které je synchronizováno se sítí (eNodeB) a může tuto synchronizaci přenášet, nebo zařízení mimo pokrytí, které může generovat vlastní synchronizační referenci na základě interních kritérií nebo synchronizace přijaté z jiného zdroje D2DSS. Struktura signálu je odvozena od, ale odlišná od, LTE PSS/SSS specifických pro buňku, aby se předešlo záměně se síťovými signály. Skládá se z sekvencí, které přenášejí časové informace a identitu synchronizace sidelink na fyzické vrstvě.

Fungování D2DSS zahrnuje proces výběru synchronizačního zdroje a vysílání signálu. UE monitoruje D2DSS od potenciálních synchronizačních zdrojů, kterými mohou být eNodeB (v pokrytí) nebo jiná UE (v nebo mimo pokrytí). Na základě předkonfigurovaných pravidel a změřené kvality signálu (např. Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/))) si UE vybere nejlepší dostupnou synchronizační referenci. Pokud je určena (např. sítí nebo jako jediné schopné zařízení ve skupině), bude UE periodicky vysílat D2DSS na předdefinovaných zdrojích v rámci subrámců synchronizace sidelink. Toto vysílání zahrnuje samotný D2DSS a přidružený Physical Sidelink Broadcast Channel ([PSBCH](/mobilnisite/slovnik/psbch/)), který nese základní systémové informace, jako je indikátor stavu pokrytí (v/mimo) a podrobné časové informace. Přijímající UE používají D2DSS k dosažení časové a frekvenční synchronizace, což jim umožňuje správně dekódovat následné řídicí a datové kanály sidelink ([PSCCH](/mobilnisite/slovnik/pscch/), [PSSCH](/mobilnisite/slovnik/pssch/)) pro zjišťování a komunikaci.

Klíčové komponenty mechanismu D2DSS zahrnují typy synchronizačních zdrojů (síť, UE), generování sekvence D2DSS, přidružený PSBCH a schéma přidělování zdrojů pro vysílání. Výkon a spolehlivost přímé komunikace závisí na robustním vysílání a příjmu D2DSS, neboť tento signál podporuje celé časování fyzické vrstvy sidelink. Jeho role se významně rozšířila s V2X v pozdějších vydáních, kde je vysokorychlostní a vysoce spolehlivá synchronizace mezi vozidly, chodci a infrastrukturou klíčová pro bezpečnostní aplikace.

## K čemu slouží

D2DSS byl vytvořen, aby vyřešil základní problém zavedení synchronizace pro přímou komunikaci mezi zařízeními (D2D) v sítích LTE, což byla schopnost nepodporovaná ve standardech před Release 12. Tradiční buněčné sítě jsou centrálně synchronizovány základnovou stanicí (eNodeB). Pro přímou komunikaci, zejména ve scénářích veřejné bezpečnosti, kde mohou záchranáři působit v oblastech s poškozenou nebo žádnou síťovou infrastrukturou, potřebují UE metodu, jak se vzájemně synchronizovat nezávisle. Bez společného časového a frekvenčního referenčního bodu je efektivní demodulace signálů s ortogonálním frekvenčním multiplexem (OFDM) nemožná, což vede k neúspěšné komunikaci. D2DSS poskytuje tento zásadní referenční bod a umožňuje tak základní vrstvu pro ProSe.

Motivace vycházela z rostoucí poptávky po službách založených na blízkosti, včetně komerčních aplikací, jako jsou sociální sítě, a kritické komunikace pro veřejnou bezpečnost. Před Release 12 by jakákoli forma přímé komunikace UE-UE vyžadovala ne-3GPP technologie (např. Wi-Fi Direct), kterým chybí integrace s buněčnými sítěmi pro řízení, zabezpečení a mobilitu. D2DSS jako součást standardizovaného LTE sidelink umožňuje síťově řízenou nebo autonomní přímou komunikaci v licencovaném spektru, což nabízí lepší pokrytí, správu rušení a integraci se službami jádra sítě ve srovnání s ad-hoc řešeními.

Dále D2DSS řešil omezení vyžadující trvalé síťové pokrytí pro synchronizaci. Tím, že umožňuje UE fungovat jako synchronizační zdroje, umožňuje komunikaci ve scénářích s částečným pokrytím a mimo pokrytí. To byl klíčový požadavek organizací veřejné bezpečnosti. Vytvoření D2DSS tak odemklo nové případy užití a vytvořilo technický základ pro pozdější vývoj směrem ke komunikaci V2X založené na LTE v Release 14 a novějších, kde je synchronizace mezi vysokorychlostními vozidly prvořadá.

## Klíčové vlastnosti

- Umožňuje časovou a frekvenční synchronizaci pro komunikaci přes LTE sidelink (rozhraní PC5)
- Podporuje jak režim provozu v pokrytí (synchronizováno se sítí), tak mimo pokrytí (synchronizováno s UE)
- Definuje hierarchii synchronizačních zdrojů a procedury jejich výběru pro UE
- Vysílá se společně s PSBCH pro přenos základních systémových informací sidelink
- Používá sekvence odlišné od buněčných PSS/SSS, aby se předešlo rušení a nesprávné identifikaci
- Tvoří synchronizační základ pro zjišťování a přímou komunikaci v ProSe

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [PSBCH – Physical Sidelink Broadcast Channel](/mobilnisite/slovnik/psbch/)

## Definující specifikace

- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.843** (Rel-12) — D2D Proximity Services Feasibility Study
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services

---

📖 **Anglický originál a plná specifikace:** [D2DSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/d2dss/)
