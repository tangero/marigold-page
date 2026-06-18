---
slug: "db-dc-hsupa"
url: "/mobilnisite/slovnik/db-dc-hsupa/"
type: "slovnik"
title: "DB-DC-HSUPA – Dual Band Dual Cell High Speed Uplink Packet Access"
date: 2025-01-01
abbr: "DB-DC-HSUPA"
fullName: "Dual Band Dual Cell High Speed Uplink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/db-dc-hsupa/"
summary: "DB-DC-HSUPA je vylepšení 3GPP UMTS, které umožňuje uživatelskému zařízení (UE) vysílat uplink data současně pomocí dvou nosných agregovaných ze dvou různých kmitočtových pásem. Výrazně zvyšuje rychlos"
---

DB-DC-HSUPA je vylepšení 3GPP UMTS, které umožňuje zařízení vysílat uplink data současně pomocí dvou agregovaných nosných ze dvou různých kmitočtových pásem, čímž zvyšuje rychlost a efektivitu uplinku.

## Popis

DB-DC-HSUPA je technologie agregace nosných v rámci rádiového přístupového sítě UMTS/[HSPA](/mobilnisite/slovnik/hspa/), konkrétně vylepšující směr uplink ([UL](/mobilnisite/slovnik/ul/)). Navazuje na základní [HSUPA](/mobilnisite/slovnik/hsupa/) (High Speed Uplink Packet Access) a starší [DC-HSUPA](/mobilnisite/slovnik/dc-hsupa/) (Dual Cell HSUPA, která agreguje dvě nosné v rámci stejného kmitočtového pásma). Klíčovým architektonickým pokrokem DB-DC-HSUPA je její schopnost nakonfigurovat UE se dvěma uplink nosnými, které se nacházejí ve dvou různých provozních pásmech UMTS (např. Pásmo I na 2100 MHz a Pásmo [VIII](/mobilnisite/slovnik/viii/) na 900 MHz). To vyžaduje, aby UE podporovalo možnost dvojího vysílání napříč těmito pásmy. Síť, konkrétně Node B a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)), musí spravovat plánování a řízení výkonu pro obě uplink nosné nezávisle, ačkoli jsou pro stejného uživatele koordinovány. Primární obsluhující buňka poskytuje řídicí signalizaci, zatímco sekundární buňka je přidána pro dodatečnou uplink šířku pásma.

Z pohledu protokolu UE naváže rádiové spojení na primární nosné v primárním pásmu. Po úspěšné konfiguraci ze strany RNC prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) je aktivována sekundární uplink nosná v jiném pásmu. UE poté vysílá transportní bloky Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)) souběžně na obou nosných. Vrstva Medium Access Control (MAC) na straně UE a Node B zajišťuje multiplexování a plánování dat přes obě nosné. Node B přijímá signály prostřednictvím samostatných rádiových cest a antén naladěných na příslušná pásma, zpracovává je nezávisle a přeposílá data k RNC pro případné sloučení.

Úlohou této technologie je maximalizovat využití fragmentovaných spektrálních zdrojů, které může operátor vlastnit napříč více pásmy. Agregací nosných z nesouvislých spektrálních bloků vytváří pro uživatele širší efektivní uplink kanál. To je řízeno výhradně v rámci UTRAN (UMTS Terrestrial Radio Access Network) bez zapojení core sítě pro samotnou agregaci. Mezi klíčové technické komponenty, které to umožňují, patří vícekmitočtové RF přední části a návrh výkonového zesilovače UE, možnosti vícekmitočtového přijímače Node B a vylepšení protokolů RRC a MAC pro podporu správy, měření a procedur aktivace/deaktivace nosných v různých pásmech.

## K čemu slouží

DB-DC-HSUPA bylo zavedeno, aby řešilo rostoucí poptávku po vyšších rychlostech uplink dat a lepší uplink kapacitě v sítích UMTS/HSPA, poháněnou nárůstem uživatelského obsahu, videokonferencí a cloudové synchronizace. Před jeho zavedením byla vylepšení uplinku omezena na jednoduchou HSUPA nebo DC-HSUPA, která byla omezena na agregaci dvou nosných v rámci stejného kmitočtového pásma. To bylo omezení pro operátory, kteří neměli dostatek souvislého spektra v jednom pásmu pro efektivní nasazení DC-HSUPA.

Technologie vyřešila problém nevyužitých, fragmentovaných spektrálních rezerv. Mnoho operátorů vlastní spektrální licence ve více pásmech (např. základní pásmo 2100 MHz pro pokrytí měst a nižší pásmo jako 900 MHz pro širší pokrytí). DB-DC-HSUPA jim umožňuje využívat tyto rozdílné zdroje současně ke zvýšení výkonu uplinku. Přímo řeší asymetrii v dřívějším zaměření HSPA, které zaznamenalo dramatičtější vylepšení downlinku s technologiemi jako DC-HSDPA a později MC-HSDPA. Tím, že umožnila agregaci uplinku v různých pásmech, poskytla vyváženější uživatelský zážitek, snížila latenci pro interaktivní aplikace a zlepšila celkovou efektivitu sítě lepším využitím všech dostupných spektrálních zdrojů.

## Klíčové vlastnosti

- Současný uplink přenos na dvou nosných v různých kmitočtových pásmech
- Vyžaduje podporu UE pro dvojí vysílání a vícekmitočtový RF provoz
- Nezávislé plánování a řízení výkonu pro každou agregovanou uplink nosnou
- Vylepšení signalizace RRC pro aktivaci sekundární nosné v jiném pásmu
- Zvýšené špičkové rychlosti uplink dat efektivním zdvojnásobením uplink šířky pásma
- Zlepšená spektrální efektivita uplinku a kapacita rádiové přístupové sítě

## Související pojmy

- [DC-HSUPA – Dual Cell High Speed Uplink Packet Access](/mobilnisite/slovnik/dc-hsupa/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [DC-HSDPA – Dual Cell High Speed Downlink Packet Access](/mobilnisite/slovnik/dc-hsdpa/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [DB-DC-HSUPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/db-dc-hsupa/)
