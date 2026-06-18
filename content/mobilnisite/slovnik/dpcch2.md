---
slug: "dpcch2"
url: "/mobilnisite/slovnik/dpcch2/"
type: "slovnik"
title: "DPCCH2 – Dedicated Physical Control Channel 2"
date: 2025-01-01
abbr: "DPCCH2"
fullName: "Dedicated Physical Control Channel 2"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dpcch2/"
summary: "Sekundární vyhrazený řídicí kanál pro uplink zavedený pro vylepšení Dual Connectivity a agregace nosných v pozdějších vydáních 3GPP. Přenáší řídicí informace pro sekundární skupinu buněk, což umožňuje"
---

DPCCH2 je sekundární vyhrazený řídicí kanál pro uplink v režimu Dual Connectivity a agregace nosných, který přenáší řídicí informace pro sekundární skupinu buněk a umožňuje současný přenos řídicích informací pro více nosných.

## Popis

Dedicated Physical Control Channel 2 (DPCCH2) je rozšířením původního konceptu [DPCCH](/mobilnisite/slovnik/dpcch/), zavedeným ve vydání 3GPP Release 12 pro podporu pokročilých schopností UE, především Dual Connectivity ([DC](/mobilnisite/slovnik/dc/)) a vylepšené agregace nosných pro uplink. Zatímco primární DPCCH je asociován s hlavní skupinou buněk ([MCG](/mobilnisite/slovnik/mcg/)), DPCCH2 je asociován se sekundární skupinou buněk ([SCG](/mobilnisite/slovnik/scg/)). Jeho funkce je analogická DPCCH, ale slouží pro sekundární sadu obsluhujících buněk, což UE umožňuje vysílat potřebné řídicí informace fyzické vrstvy pro uplink SCG.

Ve scénáři Dual Connectivity je UE současně připojeno ke dvěma eNodeB (nebo k hlavnímu [eNB](/mobilnisite/slovnik/enb/) a sekundárnímu eNB). MCG poskytuje primární spojení včetně primární buňky (PCell), zatímco SCG poskytuje jednu nebo více sekundárních buněk (SCell). DPCCH2 přenáší řídicí informace pro přenosy [PUCCH](/mobilnisite/slovnik/pucch/) a [PUSCH](/mobilnisite/slovnik/pusch/) odpovídající primární SCell (PSCell) SCG. To zahrnuje pilotní bity pro odhad kanálu, [HARQ](/mobilnisite/slovnik/harq/) ACK/NACK pro downlinkové přenosy na SCG, hlášení informace o stavu kanálu (CSI) pro buňky SCG a žádosti o plánování (SR). Přenosové parametry pro DPCCH2, jako je řízení výkonu, jsou řízeny nezávisle na parametrech primárního DPCCH, ačkoli jsou koordinovány UE.

Zavedení DPCCH2 vyžadovalo vylepšení zpracování fyzické vrstvy a řízení přístupu k médiu (MAC) v UE. UE musí být schopno generovat a vysílat dva samostatné proudy řídicích informací pro uplink, každý synchronizovaný s časovým předstihem příslušné skupiny buněk. To umožňuje efektivnější využití rádiových prostředků napříč více nosnými a základnovými stanicemi, což vede k vyšším špičkovým přenosovým rychlostem a lepšímu vyvažování zátěže. Specifikace pro DPCCH2 jsou podrobně popsány ve stejných dokumentech fyzické vrstvy (např. TS 25.211, 25.214) jako původní DPCCH, s dodatečnými ustanoveními a postupy pro práci s dvouskupinovou konfigurací buněk. Představuje klíčový prvek umožňující agregaci kapacity z nespolokalizovaných základnových stanic, což je významný krok nad rámec jednoduché agregace nosných na jednom místě.

## K čemu slouží

DPCCH2 byl vytvořen, aby překonal omezení spočívající v existenci pouze jediného řídicího kanálu pro uplink ve scénářích zahrnujících více nezávislých přenosových bodů. Se zavedením Dual Connectivity ve vydání Release 12 mohlo UE přijímat data ze dvou samostatných eNodeB, ale potřebovalo mechanismus pro efektivní odesílání řídicí zpětné vazby (jako HARQ-ACK a CSI) pro sekundární skupinu buněk. Spoléhání se pouze na primární DPCCH by vytvořilo úzké hrdlo a zvýšilo latenci pro zpětnou vazbu SCG.

Jeho účelem je umožnit nezávislé a paralelní řídicí signalizování pro uplink pro více skupin buněk. To řeší problém zahlcení řídicího kanálu a zpoždění zpětné vazby při agregaci nosných z různých základnových stanic, což je běžné v heterogenních síťových nasazeních s makro a malými buňkami. Poskytnutím vyhrazeného řídicího kanálu pro SCG zajišťuje DPCCH2, že pokročilé funkce, jako je koordinovaný příjem z více bodů (CoMP) a efektivní agregace nosných přes neideální backhaul, mohou být realizovány bez kompromisů ve spolehlivosti nebo včasnosti řídicí smyčky. Šlo o nezbytný vývoj pro podporu zvýšené složitosti a výkonnostních cílů LTE-Advanced Pro a cestu k 5G.

## Klíčové vlastnosti

- Poskytuje řídicí signalizaci pro uplink pro sekundární skupinu buněk (SCG) v režimu Dual Connectivity.
- Přenáší řídicí informace pro PSCell SCG, včetně HARQ-ACK, CSI a SR.
- Umožňuje nezávislé řízení výkonu a časování pro sekundární skupinu buněk.
- Umožňuje současný přenos řídicích informací pro MCG a SCG.
- Nezbytný pro agregaci nosných s vysokou propustností napříč nespolokalizovanými lokalitami.
- Definován ve specifikacích fyzické vrstvy s rozšířeními pro vícebodovou konektivitu.

## Související pojmy

- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DPCCH2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpcch2/)
