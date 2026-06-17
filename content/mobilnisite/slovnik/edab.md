---
slug: "edab"
url: "/mobilnisite/slovnik/edab/"
type: "slovnik"
title: "EDAB – Extended Dual slot Access Burst"
date: 2025-01-01
abbr: "EDAB"
fullName: "Extended Dual slot Access Burst"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/edab/"
summary: "Vylepšený formát náhodného přístupového burstu v sítích GSM, který využívá dva po sobě jdoucí časové sloty namísto jednoho. Zvyšuje výkon a délku trvání signálu přístupového požadavku a výrazně tak zl"
---

EDAB je vylepšený formát náhodného přístupového burstu v GSM, který využívá dva po sobě následující časové sloty ke zvýšení výkonu signálu a jeho trvání, čímž zlepšuje pravděpodobnost úspěšného přístupu v náročných rádiových podmínkách.

## Popis

Extended Dual slot Access Burst (EDAB) je fyzická struktura burstu definovaná v GSM specifikacích pro náhodný přístupový kanál (RACH). Představuje vylepšení oproti standardnímu přístupovému burstu ([AB](/mobilnisite/slovnik/ab/)), který zabírá jediný časový slot. EDAB, jak již název napovídá, rozšiřuje přenos na dva po sobě následující časové sloty v rámci TDMA rámce. Toho dosáhne mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) vysíláním speciálně formátovaného burstu, který pokrývá tyto dva sloty. Struktura burstu zahrnuje rozšířenou tréninkovou sekvenci a ochranné periody přizpůsobené pro dvouslotovou délku, jak je podrobně popsáno ve specifikacích jako 45.001 a 45.003.

Provozně, když je GSM buňka nakonfigurována na podporu EDAB (což je indikováno vysílanými systémovými informacemi), může MS při pokusu o přístup k síti – například k provedení aktualizace polohy nebo zahájení hovoru – tento formát burstu použít, pokud odhadne špatné rádiové podmínky. MS spočítá potřebný vysílací výkon a časový předstih. Pokud je útlum na trase velmi vysoký a překračuje prahovou hodnotu, při které by standardní AB nemusel být spolehlivě dekódován základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)), může se MS rozhodnout vyslat EDAB. Použití dvou slotů poskytuje přibližně dvojnásobnou energii při stejném špičkovém výkonu nebo umožňuje robustnější modulační vzor, čímž se zvyšuje poměr signálu k šumu na přijímači.

Z hlediska architektury má EDAB dopad jak na MS, tak na BTS. Fyzická vrstva MS musí být schopna generovat tento delší formát burstu, včetně odpovídající modulace a náběhu výkonu napříč dvěma sloty. Přijímač BTS musí být vybaven pro detekci a synchronizaci těchto rozšířených burstů na RACH. Dekódovací algoritmy v BTS jsou navrženy tak, aby korelovaly delší tréninkovou sekvenci, která poskytuje lepší odolnost vůči vícenásobnému útlumu a interferenci. Úspěšná detekce EDAB uděluje MS přístup k síti, po kterém pokračuje standardní signalizační procedurou. Primární rolí EDAB je rozšířit efektivní poloměr pokrytí GSM buňky, zejména pro signalizaci řídicí roviny, a zajistit, aby se uživatelé na okraji buňky nebo v obtížných prostorových podmínkách mohli stále připojit k síti a žádat o služby.

## K čemu slouží

Extended Dual slot Access Burst byl vyvinut k řešení kritického problému selhání náhodného přístupu v GSM sítích s velkými buňkami a v prostředích se silným útlumem signálu. Před zavedením EDAB měl standardní přístupový burst omezený účet zisků a ztrát linky. Ve velmi rozlehlých buňkách (např. venkovské oblasti) nebo v hlubokých vnitřních lokalitách (např. sklepy) mohl signál z [MS](/mobilnisite/slovnik/ms/) dorazit k [BTS](/mobilnisite/slovnik/bts/) příliš slabý na to, aby byl spolehlivě detekován přes šum a interferenci na RACH. To vedlo k neúspěšným pokusům o přístup, opakovaným pokusům, zvýšené interferenci a v konečném důsledku k odmítnutí služeb pro uživatele v oblastech se špatným pokrytím.

Zavedený ve vydání 14 jako součást evoluce GSM pro IoT a rozšíření pokrytí byl EDAB motivován potřebou podporovat zařízení pro komunikaci mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)), která jsou často nasazována v náročných rádiových podmínkách a vyžadují extrémně spolehlivé připojení k síti. Tradičním přístupem ke zlepšení pokrytí bylo zvýšení vysílacího výkonu BTS nebo nasazení více stanovišť, což je nákladné. EDAB poskytl nákladově efektivní řešení tím, že posílil přístupový signál ve směru uplink ze strany zařízení, čímž efektivně zvýšil účet zisků a ztrát linky pro počáteční přístupovou proceduru, aniž by vyžadoval změny hardwaru na každé BTS (pouze na těch, které tuto funkci potřebují).

Řeší základní asymetrii v účtech zisků a ztrát linky v buněčných sítích, kde downlink (BTS k MS) je obvykle silnější než uplink (MS k BTS). Vyčleněním více času (dva sloty) pro přístupový pokus může MS integrovat do signálu více energie, což zvyšuje pravděpodobnost, že překročí detekční práh BTS. To bylo obzvláště důležité pro zajištění úspěšnosti řídkých, ale kritických signalizačních událostí, jako jsou periodické aktualizace polohy od IoT senzorů. EDAB tak rozšiřuje praktické pokrytí GSM buňky pro řídicí signalizaci, zlepšuje dostupnost a spolehlivost, což je klíčový požadavek pro masivní nasazení IoT a robustní komerční hlasové služby.

## Klíčové vlastnosti

- Překlenuje dva po sobě následující TDMA časové sloty pro zvýšení délky přenosu
- Zlepšuje účet zisků a ztrát linky ve směru uplink pro proceduru náhodného přístupu
- Používá rozšířenou tréninkovou sekvenci pro lepší synchronizaci v šumu
- Konfigurovatelný sítí prostřednictvím vysílaných systémových informací
- Používán MS na základě odhadovaných podmínek útlumu na trase
- Zlepšuje míru úspěšnosti přístupu ve velkých buňkách a scénářích se špatným pokrytím

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.018** (Rel-19) — GSM Radio Resource Management Procedures
- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.002** (Rel-19) — GSM/EDGE Radio Physical Layer Specification
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [EDAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/edab/)
