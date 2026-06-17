---
slug: "8c-hsdpa"
url: "/mobilnisite/slovnik/8c-hsdpa/"
type: "slovnik"
title: "8C-HSDPA – Eight-Carrier High-Speed Downlink Packet Access"
date: 2025-01-01
abbr: "8C-HSDPA"
fullName: "Eight-Carrier High-Speed Downlink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/8c-hsdpa/"
summary: "8C-HSDPA je technologie agregace více nosných pro sítě WCDMA/HSPA, která umožňuje simultánní přenos přes 5 až 8 downlinkových nosných. Výrazně zvyšuje špičkové přenosové rychlosti a spektrální účinnos"
---

8C-HSDPA je nejvyšší úroveň agregace nosných HSPA, která umožňuje simultánní přenos přes osm downlinkových nosných pro výrazné zvýšení špičkové přenosové rychlosti a spektrální účinnosti v sítích WCDMA.

## Popis

Eight-Carrier [HSDPA](/mobilnisite/slovnik/hsdpa/) je pokročilá technologie agregace více nosných v rámci vývojového rámce [HSPA](/mobilnisite/slovnik/hspa/), která umožňuje uživatelskému zařízení (UE) přijímat data současně na až osmi downlinkových nosných. Každá nosná pracuje ve standardní šířce pásma WCDMA 5 MHz a po agregaci tyto nosné poskytují podstatně zvýšené špičkové přenosové rychlosti a lepší spektrální účinnost. Technologie navazuje na předchozí konfigurace více-nosného HSDPA (2C, 3C, 4C) rozšířením schopnosti agregace na podporu 5 až 8 komponentních nosných, přičemž přesný počet je konfigurovatelný na základě nasazení sítě a schopností UE.

Architektura 8C-HSDPA zahrnuje více synchronizovaných nosných ve stejném kmitočtovém pásmu nebo napříč různými pásmy, přičemž jedna nosná je určena jako kotvící (anchor) nebo primární nosná, která přenáší základní řídicí signalizaci. Sekundární nosné poskytují dodatečnou šířku pásma pro přenos dat. NodeB koordinuje přenos přes všechny aktivní nosné, zatímco UE musí podporovat potřebné RF a základnové pásmo (baseband) pro příjem a kombinaci signálů z více nosných současně. Klíčová vylepšení fyzické vrstvy zahrnují pokročilé přijímací algoritmy, vylepšené odhadování kanálu a sofistikované techniky ekvalizace pro zvládnutí zvýšené složitosti příjmu z více nosných.

Z pohledu protokolů si 8C-HSDPA zachovává zpětnou kompatibilitu s dřívějšími releasy HSPA a zároveň zavádí vylepšení protokolu MAC-hs pro správu plánování napříč více nosnými. Technologie používá plánování napříč nosnými (cross-carrier scheduling), kde kotvící nosná nese plánovací informace pro všechny komponentní nosné, čímž se snižuje režie řídicích kanálů. Fyzická vrstva využívá více [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/) (High-Speed Physical Downlink Shared Channels) napříč agregovanými nosnými, přičemž každá nosná podporuje až 15 kanalizačních kódů. Teoretická špičková přenosová rychlost pro 8C-HSDPA dosahuje až 336 Mbps při použití modulace [64QAM](/mobilnisite/slovnik/64qam/) a [MIMO](/mobilnisite/slovnik/mimo/) na každé nosné, ačkoli praktické implementace obvykle dosahují nižších rychlostí v závislosti na podmínkách kanálu a implementačních omezeních.

Při nasazení sítě je třeba u 8C-HSDPA pečlivě plánovat kmitočty nosných, požadavky na synchronizaci a přidělování výkonu napříč nosnými. Technologie vyžaduje UE s pokročilými RF schopnostmi pro zvládnutí zvýšené šířky pásma a potenciálních intermodulačních produktů. Z pohledu sítě umožňuje 8C-HSDPA operátorům lépe využít fragmentovaná spektrální aktiva agregací nesousedících nosných, což představuje nákladově efektivní alternativu k nasazení nových technologií radiového přístupu a zároveň poskytuje koncovým uživatelům konkurenceschopné přenosové rychlosti.

## K čemu slouží

8C-HSDPA byl vyvinut pro řešení rostoucí poptávky po vyšších přenosových rychlostech v sítích WCDMA/[HSPA](/mobilnisite/slovnik/hspa/) v důsledku exponenciálního nárůstu spotřeby mobilních dat. S rozšířením chytrých telefonů a datově náročných aplikací potřebovali operátoři způsoby, jak vylepšit své stávající 3G sítě bez nutnosti úplné migrace na LTE. Tato technologie představuje vyvrcholení snah o vývoj HSPA, posouváním hranic toho, čeho lze dosáhnout v rámci WCDMA pomocí pokročilých technik agregace nosných.

Předchozí releasy HSPA představily 2C, 3C a [4C-HSDPA](/mobilnisite/slovnik/4c-hsdpa/), ale tyto konfigurace se staly nedostatečnými, protože očekávání uživatelů ohledně přenosových rychlostí stále rostla. 8C-HSDPA to řešil zdvojnásobením maximálního počtu agregovaných nosných ve srovnání s 4C-HSDPA, čímž se efektivně zdvojnásobily potenciální špičkové přenosové rychlosti. To bylo obzvláště důležité pro operátory s významnými investicemi do infrastruktury WCDMA, kteří chtěli maximalizovat návratnost svých investic a zároveň konkurovat vznikajícím sítím LTE.

Technologie také řešila problém fragmentace spektra, což operátorům umožnilo agregovat nosné napříč různými kmitočtovými pásmy (jako 850 MHz, 900 MHz, 1900 MHz a 2100 MHz) a vytvářet tak širší efektivní šířky pásma. To bylo zvláště cenné na trzích, kde operátoři vlastnili nesousedící spektrální alokace, které nebylo možné efektivně využít s jednoduchými jedno-nosnými technologiemi. Umožněním agregace až 8 nosných poskytla 8C-HSDPA migrační cestu pro sítě HSPA k dosažení přenosových rychlostí konkurenceschopných s LTE při zachování zpětné kompatibility se stávající populací UE.

## Klíčové vlastnosti

- Agregace 5 až 8 downlinkových nosných pro zvýšení šířky pásma
- Teoretické špičkové přenosové rychlosti až 336 Mbps s 64QAM a MIMO
- Podpora jak sousedící, tak nesousedící agregace nosných
- Zpětná kompatibilita s dřívějšími konfiguracemi více-nosného HSPA
- Plánování napříč nosnými (cross-carrier scheduling) pro snížení režie řídicích kanálů
- Vylepšené přijímací algoritmy pro lepší výkon s více nosnými

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [DC-HSDPA – Dual Cell High Speed Downlink Packet Access](/mobilnisite/slovnik/dc-hsdpa/)
- [4C-HSDPA – Four-Carrier High-Speed Downlink Packet Access](/mobilnisite/slovnik/4c-hsdpa/)

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.327** (Rel-19) — Multi-carrier HSDPA UE requirements

---

📖 **Anglický originál a plná specifikace:** [8C-HSDPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/8c-hsdpa/)
