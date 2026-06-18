---
slug: "dc-hsdpa"
url: "/mobilnisite/slovnik/dc-hsdpa/"
type: "slovnik"
title: "DC-HSDPA – Dual Cell High Speed Downlink Packet Access"
date: 2025-01-01
abbr: "DC-HSDPA"
fullName: "Dual Cell High Speed Downlink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dc-hsdpa/"
summary: "DC-HSDPA je vylepšení podle 3GPP, které umožňuje UE přijímat data současně na dvou sousedních 5 MHz nosných frekvencích v downlinku, čímž se efektivně zdvojnásobí špičková datová rychlost a spektrální"
---

DC-HSDPA je vylepšení HSPA podle 3GPP, které umožňuje uživatelskému zařízení přijímat data současně na dvou downlinkových nosných, čímž se v porovnání s jednokanálovým HSDPA zdvojnásobí špičková datová rychlost.

## Popis

DC-HSDPA funguje agregací dvou sousedních 5 MHz [WCDMA](/mobilnisite/slovnik/wcdma/) nosných ve stejném kmitočtovém pásmu, což umožňuje jednomu uživatelskému zařízení (UE) přijímat data souběžně na obou nosných. Toto je implementováno v Node B (základnové stanici) a v UE, přičemž síť koordinuje plánování a přenos přes obě nosné. Primární nosná zpracovává veškerou řídicí signalizaci, včetně [HS-SCCH](/mobilnisite/slovnik/hs-scch/) (High Speed Shared Control Channel) pro downlinková plánovací přiřazení a [HS-DPCCH](/mobilnisite/slovnik/hs-dpcch/) (High Speed Dedicated Physical Control Channel) pro uplinková potvrzení a zpětnou vazbu o kvalitě kanálu. Sekundární nosná se používá primárně pro dodatečný datový přenos, přičemž plánování řídí Node B na základě stavu kanálu a schopností UE.

Z pohledu protokolů zavádí DC-HSDPA vylepšení na vrstvě [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control). UE má jedinou MAC entitu, která spravuje dva transportní kanály [HS-DSCH](/mobilnisite/slovnik/hs-dsch/) (High Speed Downlink Shared Channel), jeden na každé nosné. Plánovač Node B může dynamicky přidělovat data přes obě nosné, čímž optimalizuje využití zdrojů. Zpracování fyzické vrstvy zůstává z velké části na úrovni jednotlivých nosných, s odděleným kódováním, modulací ([QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/) nebo [64QAM](/mobilnisite/slovnik/64qam/)) a hybridními ARQ procesy pro každou nosnou. UE musí podporovat duální přijímače a schopnost demodulovat obě nosné současně, což zvyšuje složitost, ale umožňuje významné zisky v propustnosti.

Mezi klíčové síťové komponenty patří Node B, který musí být vybaven hardwarem a softwarem podporujícím dvě nosné, a RNC (Radio Network Controller), který zpracovává konfiguraci nosných, správu mobility a přidělování zdrojů pro UE podporující DC-HSDPA. RNC konfiguruje sekundární nosnou prostřednictvím signalizace RRC (Radio Resource Control), typicky jako doplňkový downlink. DC-HSDPA lze kombinovat s dalšími vylepšeními HSPA, jako je MIMO (Multiple Input Multiple Output) a vyšší řád modulace (64QAM), pro další zvýšení výkonu, což vede k teoretickým špičkovým datovým rychlostem až 42 Mbps v Rel-8 s 2x2 MIMO a 64QAM.

Technologie hraje klíčovou roli ve zvyšování kapacity 3G sítí a uživatelských datových rychlostí, zejména ve scénářích s omezeným spektrem. Umožňuje operátorům efektivněji využívat stávající WCDMA spektrum spojením nosných, čímž oddaluje potřebu okamžité migrace na LTE. DC-HSDPA je zpětně kompatibilní, což znamená, že UE nepodporující DC mohou stále pracovat na jedné z nosných, což zajišťuje hladké soužití. Položila základy pro pokročilejší techniky agregace nosných v LTE a 5G NR a stanovila principy vícekanálového provozu v mobilních sítích.

## K čemu slouží

DC-HSDPA byl vyvinut pro řešení rostoucí poptávky po vyšších datových rychlostech a lepší spektrální účinnosti v 3G sítích, poháněné rozšířením chytrých telefonů a využíváním mobilního internetu na konci let 2000. Jednokanálové HSDPA, zavedené v Rel-5, dosáhlo praktických limitů se špičkovými rychlostmi kolem 14,4 Mbps (s MIMO a 64QAM), ale vyžadovalo významné podmínky SNR. Operátoři hledali způsoby, jak zvýšit výkon bez nutnosti nových kmitočtových pásem nebo kompletní přestavby sítě na LTE. DC-HSDPA poskytlo nákladově efektivní cestu upgradu využitím stávajících přidělených spárovaných spekter, často již dostupných v souvislých blocích.

Technologie vyřešila problém omezené špičkové uživatelské propustnosti a kapacity buňky v přetížených městských prostředích. Agregací dvou nosných efektivně zdvojnásobila dostupnou šířku pásma na uživatele, čímž zlepšila propustnost a snížila latenci pro datově náročné aplikace. To bylo obzvláště cenné pro operátory, kteří ještě nenasadili LTE nebo chtěli maximalizovat své investice do 3G. DC-HSDPA také zlepšilo vyrovnávání zatížení tím, že umožnilo distribuci provozu přes nosné, čímž zvýšilo celkovou efektivitu sítě a uživatelský komfort během špiček.

Historicky bylo DC-HSDPA součástí evoluce HSPA+, která překlenula mezeru mezi raným HSPA a LTE. Řešilo omezení jednokanálového provozu, jako je závislost na vyšším řádu modulace a MIMO za ideálních rádiových podmínek, tím, že poskytlo spolehlivější zvýšení propustnosti prostřednictvím agregace šířky pásma. Tento koncept později ovlivnil agregaci nosných v LTE, demonstroval životaschopnost vícekanálového provozu v komerčních sítích a připravil cestu pro složitější scénáře agregace ve 4G a 5G.

## Klíčové vlastnosti

- Současný příjem na dvou sousedních 5 MHz WCDMA nosných
- Zdvojnásobení špičkové datové rychlosti až na 42 Mbps s MIMO a 64QAM
- Jedna MAC entita spravující duální transportní kanály HS-DSCH
- Primární nosná pro řídicí signalizaci, sekundární pro data
- Zpětná kompatibilita s UE nepodporujícími DC-HSDPA
- Dynamické plánování a vyrovnávání zatížení přes nosné

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements

---

📖 **Anglický originál a plná specifikace:** [DC-HSDPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dc-hsdpa/)
