---
slug: "ulsup"
url: "/mobilnisite/slovnik/ulsup/"
type: "slovnik"
title: "ULSUP – Uplink Sharing from UE Perspective"
date: 2025-01-01
abbr: "ULSUP"
fullName: "Uplink Sharing from UE Perspective"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ulsup/"
summary: "ULSUP označuje schopnost a chování UE pro sdílení uplinkových zdrojů, zejména v Agregaci nosných (CA) a Duální konektivitě (DC). Definuje, jak UE spravuje a vysílá data na více uplinkových nosných sou"
---

ULSUP je schopnost a chování UE pro sdílení uplinkových zdrojů v rámci agregace nosných a duální konektivity, které definuje, jak zařízení spravuje a vysílá data na více uplinkových nosných současně za účelem optimalizace propustnosti a latence.

## Popis

Uplink Sharing from UE Perspective (ULSUP) je soubor schopností a procedur UE definovaných v mnoha specifikacích 3GPP, které řídí, jak uživatelské zařízení (UE) spravuje a využívá více uplinkových nosných pro přenos. Jedná se o klíčový aspekt pokročilých rádiových funkcí, jako je Agregace nosných ([CA](/mobilnisite/slovnik/ca/)) a Duální konektivita ([DC](/mobilnisite/slovnik/dc/)), kdy je UE nakonfigurováno s více než jednou uplinkovou nosnou, a to buď od stejné, nebo od různých základnových stanic (např. MeNB a SeNB v [EN-DC](/mobilnisite/slovnik/en-dc/)). ULSUP řeší praktická omezení UE, jako je limitovaný vysílací výkon a hardwarové možnosti, aby určil, jak jsou uplinková data a řídicí informace distribuovány napříč těmito nosnými.

Z architektonického hlediska je ULSUP řízeno signalizací schopností UE a síťovou konfigurací prostřednictvím zpráv [RRC](/mobilnisite/slovnik/rrc/). UE hlásí svou schopnost ULSUP síti, čímž například indikuje, zda podporuje simultánní vysílání na všech agregovaných uplinkových nosných, nebo zda má omezení (jako je sdílení výkonu nebo omezení multiplexování s časovým dělením). Na základě toho síť (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) nakonfiguruje UE konkrétními skupinami buněk (Cell Groups), primární buňkou (PCell), primární sekundární buňkou (PSCell) a sekundárními buňkami (SCell), z nichž každá má přidružené uplinkové zdroje. Vrstva Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v UE je pak zodpovědná za implementaci chování ULSUP v souladu s přijatou konfigurací a přidělenými plánovacími granty.

Jak to funguje, zahrnuje několik klíčových mechanismů. UE přijímá uplinkové granty (prostřednictvím [DCI](/mobilnisite/slovnik/dci/) formátů na [PDCCH](/mobilnisite/slovnik/pdcch/)) pro své nakonfigurované nosné. Pravidla ULSUP určují, jak je dostupný vysílací výkon UE přidělen mezi tyto granty, při dodržení maximálních limitů výkonu a pravidel priority (např. UCI na PUCCH má nejvyšší prioritu, následuje PRACH, poté PUSCH s daty SRB a poté PUSCH s daty DRB). Ve scénářích s duální konektivitou (např. NR-DC) ULSUP také definuje, jak se výkon sdílí mezi skupinami buněk hlavního uzlu (MN) a sekundárního uzlu (SN). UE provádí priorizaci logických kanálů (LCP) pro každou skupinu buněk, mapuje data na konkrétní MAC PDU pro přenos na přidělených zdrojích každé nosné.

Jeho úlohou je maximalizovat uplinkový výkon a zajistit spolehlivou signalizaci řízení. Efektivním sdílením uplinkových zdrojů umožňuje ULSUP vyšší špičkové datové rychlosti, nižší latenci pro kritická data a robustní přenos uplinkových řídicích informací (UCI), i když je aktivních více nosných. Zajišťuje, že UE pracuje v rámci svých RF a výkonových omezení, čímž předchází porušení, které by mohlo vést k chybám přenosu nebo nedodržení regulačních limitů emisí. Je nezbytný pro plné využití výhod agregace nosných a duální konektivity jak v LTE, tak v NR.

## K čemu slouží

ULSUP bylo vytvořeno za účelem definování standardizovaného chování UE pro uplinkový přenos ve scénářích s více nosnými a více konektivitami, čímž řeší problém nekoordinovaného a potenciálně neefektivního využití uplinkových zdrojů. Raná vydání LTE s jednoduchou nosnou měla přímočarou správu uplinku. Nicméně se zavedením Agregace nosných ve vydání 10 mohlo mít UE více downlinkových nosných, ale zpočátku pouze jednu uplinkovou nosnou (přidruženou k PCell). Pozdější vydání přidala uplinkovou CA, což vytvořilo potřebu pravidel, jak by mělo UE zpracovávat simultánní granty na více uplinkových nosných vzhledem ke svým konečným možnostem výkonového zesilovače a zpracování.

Primární problém, který ULSUP řeší, je optimální distribuce uplinkových dat a řídicích kanálů napříč dostupnými nosnými při respektování hardwarových omezení UE (maximální výstupní výkon, schopnost sdílení výkonu). Bez takových pravidel by se různá provedení UE chovala nekonzistentně, což by pro operátory činilo síťové plánování a optimalizaci výkonu extrémně obtížnými. ULSUP poskytuje předvídatelný rámec, který síti umožňuje efektivně plánovat zdroje na základě známých schopností UE.

Navíc s příchodem Duální konektivity (např. LTE-NR EN-DC) a pokročilejších kombinací CA se složitost zvýšila. ULSUP se vyvinulo tak, aby zvládalo sdílení výkonu mezi různými rádiovými přístupovými technologiemi (např. LTE a NR) a mezi skupinami buněk řízenými různými uzly. Tím je zajištěno, že kritická signalizace (jako HARQ-ACK na PUCCH) je vždy přenášena spolehlivě, i když to znamená omezení datového přenosu na jiné nosné, čímž se udržuje stabilita sítě a uživatelský zážitek v pokročilých scénářích nasazení.

## Klíčové vlastnosti

- Definuje pravidla pro sdílení a přidělování výkonu UE napříč více uplinkovými nosnými
- Specifikuje prioritu uplinkových kanálů (PUCCH, PRACH, PUSCH s SRB/DRB)
- Zahrnuje signalizaci schopností UE pro simultánní vysílání a třídy sdílení výkonu
- Řídí uplinkové chování v nastaveních Agregace nosných i Duální konektivity
- Spravuje priorizaci logických kanálů (LCP) a hlášení stavu vyrovnávací paměti pro každou skupinu buněk
- Zajišťuje dodržování požadavků na maximální redukci výkonu (MPR) a požadavků na RF expozici

## Související pojmy

- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)

## Definující specifikace

- **TS 37.716** — 3GPP TR 37.716
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.719** (Rel-19) — Rel-19 NR SUL Configurations and CA Band Combinations
- **TS 38.755** (Rel-19) — NR FR1 DL Fragmented Carriers Study
- **TS 38.793** (Rel-19) — Simultaneous Rx/Tx Band Combinations TR
- **TR 38.839** (Rel-17) — Simultaneous Rx/Tx band combinations
- **TR 38.881** (Rel-18) — Technical Report on Lower MSD for Inter-band CA/EN-DC/DC
- **TR 38.894** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [ULSUP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ulsup/)
