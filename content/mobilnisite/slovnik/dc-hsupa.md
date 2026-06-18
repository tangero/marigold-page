---
slug: "dc-hsupa"
url: "/mobilnisite/slovnik/dc-hsupa/"
type: "slovnik"
title: "DC-HSUPA – Dual Cell High Speed Uplink Packet Access"
date: 2025-01-01
abbr: "DC-HSUPA"
fullName: "Dual Cell High Speed Uplink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dc-hsupa/"
summary: "DC-HSUPA je vylepšení standardu 3GPP, které umožňuje uživatelskému zařízení (UE) přenášet uplinková data současně na dvou sousedních 5MHz nosných ve stejném kmitočtovém pásmu. Oproti jednonosné HSUPA"
---

DC-HSUPA je vylepšení standardu 3GPP, které umožňuje zařízení přenášet uplinková data současně na dvou sousedních nosných, čímž zdvojnásobuje špičkovou přenosovou rychlost v uplinku a zlepšuje výkon pro aplikace náročné na odesílání dat v sítích 3G.

## Popis

Dual Cell High Speed Uplink Packet Access (DC-HSUPA) je technologie agregace nosných zavedená ve specifikaci 3GPP Release 9 pro sítě [WCDMA](/mobilnisite/slovnik/wcdma/)/[HSPA](/mobilnisite/slovnik/hspa/). Umožňuje uživatelskému zařízení (UE) současně využívat dvě sousední 5MHz nosné ve stejném provozním pásmu pro přenos v uplinku. Architektura staví na existujícím [HSUPA](/mobilnisite/slovnik/hsupa/) rámci, kde každá nosná má svůj vlastní transportní kanál Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)) s nezávislými procesy Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)), řízením výkonu a plánováním. NodeB plánuje prostředky na obou nosných nezávisle a UE vysílá samostatné transportní bloky na každé nosné, čímž efektivně zdvojnásobuje dostupnou šířku pásma pro uplink.

Technická implementace vyžaduje, aby UE podporovalo schopnost duálního vysílače, což umožňuje současný přenos na dvou sousedních nosných. To zahrnuje složitější návrh [RF](/mobilnisite/slovnik/rf/) front-endu a vyšší nároky na výkonový zesilovač ve srovnání s provozem na jedné nosné. Dvě nosné jsou typicky konfigurovány jako primární nosná (serving cell) a sekundární nosná, přičemž primární nosná zpracovává veškerou řídicí signalizaci včetně signalizace [RRC](/mobilnisite/slovnik/rrc/), zatímco obě nosné přenášejí uživatelská data. Vrstva MAC na straně UE i NodeB zajišťuje multiplexování a demultiplexování dat přes obě nosné a pro každou nosnou udržuje samostatné HARQ entity.

Klíčové komponenty DC-HSUPA zahrnují UE schopné práce s dvěma nosnými, NodeB podporující plánování pro dvě nosné a RNC konfigurující tento dvounosný provoz. Zpracování na fyzické vrstvě zůstává pro každou nosnou podobné jako u jednonosné HSUPA, s odděleným kanálovým kódováním, prokládáním a modulací (QPSK nebo 16QAM) pro každou nosnou. UE vysílá pomocí dvou samostatných scrambling kódů, jednoho pro každou nosnou, a NodeB je přijímá a zpracovává nezávisle, než jsou data na vyšších vrstvách zkombinována. Řízení výkonu funguje nezávisle pro každou nosnou, přičemž UE spravuje celkový vysílací výkon přes obě nosné tak, aby zůstal v rámci maximálních výkonových limitů.

Úlohou DC-HSUPA v síti bylo poskytnout operátorům UMTS/HSPA nákladově efektivní cestu upgradu pro zlepšení výkonu v uplinku bez nutnosti získání nového spektra nebo kompletně nové infrastruktury. Agregací dvou existujících nosných mohli operátoři efektivně zdvojnásobit uplinkovou kapacitu pro schopná zařízení, čímž zlepšili výkon pro aplikace náročné na odesílání dat, jako je sdílení videa, zálohování do cloudu a komunikace v reálném čase. Tato technologie fungovala spolu s dalšími vylepšeními HSPA+, jako je MIMO a modulace vyššího řádu, aby prodloužila konkurenceschopnou životnost sítí 3G vůči nastupující technologii LTE.

## K čemu slouží

DC-HSUPA byla vyvinuta, aby řešila rostoucí nerovnováhu mezi schopnostmi downlinku a uplinku v sítích 3G. Zatímco HSPA významně zlepšilo rychlosti v downlinku pomocí technologií jako HSDPA a později Dual Cell HSDPA, uplink zůstal úzkým místem pro symetrické aplikace a obsah generovaný uživateli. Rozšíření chytrých telefonů s kamerami a aplikací pro sociální sítě vytvořilo poptávku po lepším výkonu v uplinku, který jednonosná HSUPA nemohla efektivně podporovat.

Předchozí přístupy ke zlepšení výkonu v uplinku zahrnovaly zvýšení řádu modulace (z QPSK na 16QAM) a vylepšení plánovacích algoritmů, ale ty přinášely pouze omezené zisky. Základním omezením byla šířka kanálu WCDMA 5 MHz. DC-HSUPA toto vyřešila tím, že umožnila agregaci dvou nosných, čímž efektivně vytvořila 10MHz uplinkový kanál při zachování zpětné kompatibility s existujícími jednonosnými zařízeními. Tento přístup byl spektrálně efektivnější než nasazení kompletně nové technologie a umožnil operátorům využít jejich stávající spektrální držby.

Historický kontext vývoje DC-HSUPA představoval konkurenční tlak ze strany nastupující technologie LTE, která slibovala výrazně vyšší datové rychlosti. 3GPP potřebovala poskytnout operátorům UMTS/HSPA evoluční cesty, aby zůstali konkurenceschopní. DC-HSUPA spolu s dalšími funkcemi HSPA+ prodloužila užitečnou životnost investic do infrastruktury 3G a zároveň uživatelům poskytla výrazně lepší mobilní broadbandový zážitek. Konkrétně řešila potřeby aplikací jako videokonference, nahrávání velkých souborů a hraní her v reálném čase, které vyžadují symetrickou šířku pásma.

## Klíčové vlastnosti

- Současný přenos na dvou sousedních 5MHz nosných
- Zdvojnásobuje špičkové datové rychlosti v uplinku oproti jednonosné HSUPA
- Nezávislé HARQ procesy a plánování pro každou nosnou
- Zpětná kompatibilita s jednonosnými HSUPA zařízeními (UE)
- Vyžaduje schopnost duálního vysílače v UE
- Nezávislé řízení výkonu a scrambling kódy pro každou nosnou

## Související pojmy

- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [DC-HSDPA – Dual Cell High Speed Downlink Packet Access](/mobilnisite/slovnik/dc-hsdpa/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA

---

📖 **Anglický originál a plná specifikace:** [DC-HSUPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dc-hsupa/)
