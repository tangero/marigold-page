---
slug: "rac"
url: "/mobilnisite/slovnik/rac/"
type: "slovnik"
title: "RAC – Radio Admission Control"
date: 2025-01-01
abbr: "RAC"
fullName: "Radio Admission Control"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rac/"
summary: "Radio Admission Control (RAC, řízení přístupu k rádiovým prostředkům) je klíčová funkce správy rádiových prostředků (RRM) v rádiové přístupové síti (RAN), která rozhoduje, zda povolit nebo zamítnout ž"
---

RAC (řízení přístupu k rádiovým prostředkům) je funkce správy rádiových prostředků, která rozhoduje, zda povolit novou žádost o rádiový přenosový kanál, aby ochránila stabilitu sítě a předešla přetížení.

## Popis

Radio Admission Control (RAC, řízení přístupu k rádiovým prostředkům) je kritický rozhodovací algoritmus umístěný v síťovém řadiči rádiové přístupové sítě ([RNC](/mobilnisite/slovnik/rnc/) v UMTS, [eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR). Funguje jako vrátný pro žádosti o zřízení nových rádiových přenosových kanálů, které jsou typicky vyvolány požadavkem jádrové sítě na nastavení rádiového přístupového kanálu ([RAB](/mobilnisite/slovnik/rab/)) nebo žádostí UE o signalizační spojení. Když taková žádost dorazí, funkce RAC vyhodnotí, zda má rádiová síť dostatek dostupných prostředků pro podporu nového kanálu při současném zachování dohodnuté kvality služeb (QoS) pro všechny stávající aktivní kanály.

Algoritmus RAC funguje tak, že porovnává požadavky na prostředky požadovaného kanálu s aktuálním vytížením a kapacitou příslušné buňky nebo sektoru. Klíčové vstupy zahrnují parametry QoS nového požadavku (např. garantovaný přenosový výkon, úroveň priority, rozpočet zpoždění paketů) a měření aktuálního vytížení buňky v reálném čase. Toto vytížení lze měřit v různých dimenzích: úrovně rušení v uplinku/downlinku (zásadní v UMTS [WCDMA](/mobilnisite/slovnik/wcdma/)), využití bloků fyzických prostředků ([PRB](/mobilnisite/slovnik/prb/)) v LTE/NR, vytížení hardwarového zpracování nebo dostupná šířka pásma přenosové sítě. Algoritmus používá přednastavené prahové hodnoty a politiky pro své rozhodování. Například může zablokovat nový kanál pro video s vysokým přenosovým výkonem, pokud je rušení v buňce již blízko limitu stability, ale povolit kanál s nízkou prioritou pro přenos na pozadí.

Pokud je žádost povolena, funkce RAC rezervuje potřebné prostředky (v logickém smyslu) a umožní pokračovat následným procedurám nastavení rádiového přenosového kanálu. Pokud je zamítnuta, je žádost odmítnuta a jádrová síť nebo UE je o tom informována, což často vede k indikaci „síť je obsazena“ pro uživatele. RAC je úzce propojeno s dalšími funkcemi [RRM](/mobilnisite/slovnik/rrm/), jako je řízení zahlcení a plánování paketů. Zatímco RAC činí počáteční rozhodnutí o přístupu, řízení zahlcení nepřetržitě monitoruje buňku a může podniknout nápravná opatření (jako degradaci některých kanálů), pokud po povolení překročí vytížení bezpečné limity. RAC je tedy proaktivním opatřením k udržení stability sítě a kvality služeb, což je obzvláště důležité pro služby s přísnými zárukami, jako je Voice over LTE (VoLTE) nebo hry v reálném čase.

## K čemu slouží

RAC existuje, aby zajistil dlouhodobou stabilitu a předvídatelný výkon celulární sítě, což je sdílený zdroj s inherentně omezenou kapacitou. Bez řízení přístupu by síť mohla přijmout více uživatelů a relací, než je schopna fyzicky obsloužit, což by vedlo ke scénáři „tragédie obecní pastviny“, kde nadměrné rušení nebo konkurence o prostředky degraduje kvalitu pro všechny připojené uživatele, což může způsobit rozsáhlá přerušení hovorů nebo nepoužitelné datové rychlosti.

Tento problém byl obzvláště akutní v systémech omezených rušením, jako je UMTS [WCDMA](/mobilnisite/slovnik/wcdma/), kde každé nové spojení zvyšuje celkovou hladinu šumu a ovlivňuje všechny ostatní. RAC byl zaveden jako základní funkce [RRM](/mobilnisite/slovnik/rrm/) již od nejranějších standardů 3G, aby takovému kolapsu zabránil. Umožňuje síťovým operátorům prosazovat politiky plánování kapacity a upřednostňovat určité služby nebo účastníky. Například hovor záchranných služeb nebo prémiového účastníka může být povolen, i když je buňka blízko kapacity, zatímco žádost o datový přenos typu best-effort může být zablokována. Vývoj od homogenních hlasových sítí k heterogenním multislužebním sítím s více RAT pouze zvýšil důležitost RAC. Je klíčovým prvkem pro diferenciaci služeb a síťové segmenty (network slicing), protože musí rozumět a vynucovat odlišné požadavky na prostředky pro uplink senzoru masivního IoT oproti průmyslovému řídicímu spojení s ultra-spolehlivou nízkou latencí (URLLC).

## Klíčové vlastnosti

- Funkce vrátného, která přijímá nebo zamítá žádosti o zřízení nových rádiových přenosových kanálů.
- Rozhodování založené na požadovaném profilu QoS a měřeních vytížení buňky v reálném čase (rušení, využití prostředků).
- Používá konfigurovatelné přístupové politiky a prahové hodnoty k ochraně stability sítě.
- Působí proaktivně, aby předešlo zahlcení dříve, než k němu dojde.
- Integrální součást správy rádiových prostředků (RRM) v řadiči RAN (RNC/eNB/gNB).
- Nezbytný pro udržení záruk QoS pro již připuštěné uživatele a služby.

## Související pojmy

- [RAB – Radio Access Bearer](/mobilnisite/slovnik/rab/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [RAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rac/)
