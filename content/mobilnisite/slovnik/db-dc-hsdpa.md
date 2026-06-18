---
slug: "db-dc-hsdpa"
url: "/mobilnisite/slovnik/db-dc-hsdpa/"
type: "slovnik"
title: "DB-DC-HSDPA – Dual Band Dual Cell High Speed Downlink Packet Access"
date: 2025-01-01
abbr: "DB-DC-HSDPA"
fullName: "Dual Band Dual Cell High Speed Downlink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/db-dc-hsdpa/"
summary: "DB-DC-HSDPA je vylepšení 3GPP, které umožňuje uživatelskému zařízení (UE) současně přijímat datový tok ve směru dolní linky na dvou nosných ze dvou různých kmitočtových pásem. Významně zvyšuje špičkov"
---

DB-DC-HSDPA je vylepšení 3GPP pro sítě HSPA, při kterém přijímá uživatelské zařízení (UE) datový tok ve směru dolní linky současně na dvou nosných z různých kmitočtových pásem, čímž se zvyšuje špičková přenosová rychlost a spektrální účinnost.

## Popis

DB-DC-HSDPA je technologie agregace nosných v rámci vývoje [HSPA](/mobilnisite/slovnik/hspa/) (High Speed Packet Access) v UMTS. Umožňuje nakonfigurovat uživatelské zařízení (UE) se dvěma nosnými pro dolní linku, označovanými jako 'hlavní (anchor) nosná' a 'vedlejší (secondary) nosná', přičemž tyto nosné pracují ve dvou odlišných kmitočtových pásmech (např. Pásmo I (2100 MHz) a Pásmo [VIII](/mobilnisite/slovnik/viii/) (900 MHz)). Jedná se o specifický případ Dual Cell [HSDPA](/mobilnisite/slovnik/hsdpa/) ([DC-HSDPA](/mobilnisite/slovnik/dc-hsdpa/)), který typicky agreguje nosné v rámci stejného pásma. UE přijímá a dekóduje samostatné transportní bloky na každé nosné současně, čímž se efektivně zdvojnásobuje teoretická špičková přenosová rychlost ve srovnání s jednonosným HSDPA, za předpokladu podobných modulačních a kódových schémat na každé nosné.

Architektura zahrnuje úpravy jak na straně Node B, tak na straně UE. Node B musí podporovat vysílání na nosných napříč dvěma určenými pásmy a musí zvládnout plánování a [HARQ](/mobilnisite/slovnik/harq/) procesy nezávisle pro každou nosnou. UE musí disponovat dvojicí přijímačů schopných současně pracovat na dvou různých pásmech, včetně potřebných schopností [RF](/mobilnisite/slovnik/rf/) předkoncového stupně a základního pásma. Řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) spravuje konfiguraci, aktivaci a deaktivaci vedlejší nosné pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/) a koordinuje s Node B přes rozhraní Iub.

Z pohledu protokolů je vrstva MAC rozšířena pro podporu více HARQ entit, jedné pro každou obsluhovanou buňku. Zpracování na fyzické vrstvě zůstává na úrovni jednotlivých nosných, přičemž každá nosná má svou vlastní sadu kanálů HS-PDSCH (High-Speed Physical Downlink Shared Channels) a přidružených řídicích kanálů (HS-SCCH). Synchronizace a časové sladění mezi oběma nosnými jsou kritické, zejména protože mohou pocházet ze stejného nebo různých sektorů Node B; specifikace definují požadavky na maximální rozdíly ve vysílacím časování, aby byla zajištěna proveditelnost přijímače UE.

Její úlohou v síti je poskytnout výrazné zvýšení výkonu ve směru dolní linky bez nutnosti úplné migrace na LTE. Umožňuje operátorům využít fragmentovaná spektrální aktiva napříč různými pásmy, sdružovat zdroje a poskytovat tak vyšší propustnost pro uživatele a lepší vyrovnávání zatížení. Představuje nákladově efektivní cestu upgradu pro sítě HSPA, která prodlužuje jejich konkurenceschopnost vůči vyvíjejícím se technologiím 4G.

## K čemu slouží

DB-DC-HSDPA bylo zavedeno, aby řešilo rostoucí poptávku po vyšších rychlostech mobilních dat v rámci ekosystému 3G UMTS, zejména předtím, než se nasazení LTE rozšířilo. Hlavní motivací bylo překonání omezení jednonosného HSDPA, které naráželo na praktické limity spektrální účinnosti. Zatímco DC-HSDPA v rámci stejného pásma zdvojnásobovalo šířku pásma, mnoho operátorů vlastnilo spektrální licence v nesouvislých blocích napříč různými kmitočtovými pásmy. DB-DC-HSDPA bylo vytvořeno, aby tuto realitu využilo, a umožnilo agregaci nosných z těchto různorodých pásem k dosažení vyšších přenosových rychlostí.

Řešilo problém neefektivního využití fragmentovaných spektrálních aktiv. Bez DB-DC-HSDPA by nosné v různých pásmech obsluhovaly uživatele nezávisle, bez možnosti spojit svou kapacitu pro jednu uživatelskou relaci. Tato technologie umožňuje operátorovi použít například své pásmo 2100 MHz pro kapacitu a své nízkofrekvenční pásmo 900 MHz pro pokrytí a prostupnost signálu, agregovat je a dát tak uživatelům v oblastech s dobrým pokrytím kombinovanou rychlost obou. Tím se zlepšuje celkový uživatelský zážitek a účinnost sítě.

Historicky následovalo po zavedení jednonosného HSDPA a následně DC-HSDPA. Vývoj k dvoupásmovému provozu byl přirozeným dalším krokem k maximalizaci využitelnosti veškerého dostupného WCDMA spektra, zejména když operátoři přebudovávali GSM pásma pro UMTS. Poskytlo významný skok ve výkonu, který pomohl sítím HSPA+ zůstat konkurenceschopnými, a podporovalo špičkové přenosové rychlosti teoreticky až 42 Mbps (s 64QAM a MIMO) nebo 84 Mbps při kombinaci dvoupásmového, dvounosného a 2x2 MIMO konfigurací.

## Klíčové vlastnosti

- Současný příjem ve směru dolní linky na dvou nosných v různých kmitočtových pásmech
- Zdvojnásobení špičkové propustnosti pro uživatele ve srovnání s jednonosným HSDPA
- Využití fragmentovaného spektra operátora napříč více pásmy
- Nezávislé HARQ procesy a plánování pro každou nosnou
- Zpětná kompatibilita s jednonosnými a jednopásmovými DC-HSDPA zařízeními UE
- Vyžaduje UE s dvojicí přijímačů podporujících konkrétní kombinaci pásem

## Související pojmy

- [DC-HSDPA – Dual Cell High Speed Downlink Packet Access](/mobilnisite/slovnik/dc-hsdpa/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.327** (Rel-19) — Multi-carrier HSDPA UE requirements
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements

---

📖 **Anglický originál a plná specifikace:** [DB-DC-HSDPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/db-dc-hsdpa/)
