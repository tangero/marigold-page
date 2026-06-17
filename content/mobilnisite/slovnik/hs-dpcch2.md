---
slug: "hs-dpcch2"
url: "/mobilnisite/slovnik/hs-dpcch2/"
type: "slovnik"
title: "HS-DPCCH2 – Secondary High Speed Dedicated Physical Control Channel (Uplink)"
date: 2025-01-01
abbr: "HS-DPCCH2"
fullName: "Secondary High Speed Dedicated Physical Control Channel (Uplink)"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hs-dpcch2/"
summary: "HS-DPCCH2 je sekundární řídicí kanál v uplinku zavedený v pozdějších verzích HSPA pro UE konfigurovaná s více buňkami HS-DSCH (Multi-Cell HSPA). Poskytuje dodatečnou kapacitu pro zpětnou vazbu, když p"
---

HS-DPCCH2 je sekundární řídicí kanál v uplinku v HSPA, který poskytuje dodatečnou kapacitu pro zpětnou vazbu CQI a HARQ-ACK, když je UE konfigurováno s více downlinkovými obslužnými buňkami v Multi-Cell HSPA.

## Popis

Sekundární vysoce rychlý vyhrazený fyzický řídicí kanál (HS-DPCCH2) je rozšířením původního [HS-DPCCH](/mobilnisite/slovnik/hs-dpcch/), zavedeným ve 3GPP Release 17 jako součást pokračujícího vývoje [HSPA](/mobilnisite/slovnik/hspa/), konkrétně pro scénáře Multi-Cell HSPA (MC-HSPA). Jedná se o druhý paralelní fyzický řídicí kanál v uplinku, který může být UE nakonfigurováno k vysílání, když přijímá data na velkém počtu downlinkových buněk [HS-DSCH](/mobilnisite/slovnik/hs-dsch/) (sekundárních obslužných buněk). Primární HS-DPCCH má omezenou kapacitu pro bity zpětné vazby. Když roste počet nakonfigurovaných buněk, jediný HS-DPCCH nemůže přenést všechny potřebné informace indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) a [HARQ](/mobilnisite/slovnik/harq/) [ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/) pro každou buňku v požadovaném časovém rámci.

Podmínkou pro aktivaci HS-DPCCH2 je hodnota parametru [RRC](/mobilnisite/slovnik/rrc/) Secondary_Cell_Enabled. Konkrétně, když je Secondary_Cell_Enabled větší než 3 pro UE nekonfigurované v režimu MIMO 4Tx, nebo větší než 1 pro UE konfigurované v režimu MIMO 4Tx, je UE povinno použít HS-DPCCH2. Rozdíl v prahových hodnotách zohledňuje zvýšené zatížení zpětné vazby při použití MIMO (které vyžaduje indikaci předkódování - PCI). HS-DPCCH2 přenáší doplňkové informace zpětné vazby, čímž efektivně rozděluje celkové zatížení zpětné vazby mezi dva paralelní řídicí kanály.

Fyzicky je HS-DPCCH2 strukturován podobně jako původní HS-DPCCH a pracuje s 2ms podrámcem. Je také kódově multiplexován v uplinku. Síť nezávisle konfiguruje jeho kanalizační kód a výkonový offset vzhledem k DPCCH. Obsah přenášený na HS-DPCCH2 doplňuje obsah na HS-DPCCH; společně poskytují kompletní hlášení CQI a HARQ-ACK pro všechny aktivované sekundární obslužné buňky. Přesné mapování, zpětná vazba které buňky jde na který kanál, je definováno ve specifikacích, aby Node B mohlo správně interpretovat kombinované informace.

Z pohledu provozu sítě zavedení HS-DPCCH2 umožňuje Node B spravovat vyšší úroveň agregace downlinkových nosných (např. 8-nosné HSPA) bez kompromisů v aktuálnosti nebo podrobnosti zpětné vazby. Tím je zachována účinnost rychlého plánování, přizpůsobení spojení a procesů HARQ napříč všemi agregovanými nosnými. Jedná se o vylepšení kapacity řídicí roviny v uplinku, které přímo umožňuje agresivnější navyšování kapacity downlinku v pozdějších releasech HSPA.

## K čemu slouží

HS-DPCCH2 byl vytvořen k řešení kapacitního omezení v signalizaci řídicí roviny v uplinku pro pokročilá nasazení Multi-Cell HSPA. Jak se HSPA vyvíjelo po Release 8, funkce jako více-nosné HSDPA umožnily agregaci rostoucího počtu downlinkových nosných (např. 4-nosné, 8-nosné) pro jednu UE. Dále byly zavedeny pokročilé anténní techniky jako 4x4 MIMO, které vyžadují dodatečné bity zpětné vazby (PCI). Původní HS-DPCCH, navržený v Release 5, měl pevnou strukturu a omezenou bitovou kapacitu.

S mnoha sekundárními buňkami a/nebo MIMO může množství dat CQI a HARQ-ACK, které je třeba hlásit každý podrámec, překročit to, co lze spolehlivě přenést na jediném kanálu HS-DPCCH, aniž by se významně zvýšil jeho výkon (což by způsobilo interference v uplinku) nebo snížila frekvence zpětné vazby (což by zhoršilo výkon plánovače). Problémem bylo, že řídicí kanál v uplinku se stal limitujícím faktorem pro další zisky z agregace downlinku.

Řešením, standardizovaným v Release 17, bylo zavedení sekundárního kanálu HS-DPCCH2. Ten poskytuje paralelní přenosovou cestu pro řídicí informace, efektivně zdvojnásobuje kapacitu zpětné vazby v uplinku, když je to potřeba. Umožňuje síti konfigurovat velmi vysoké úrovně agregace downlinku (a složité MIMO) při zachování nízkolatentní, vysokofrekvenční smyčky zpětné vazby, která je charakteristickým znakem efektivity HSPA. HS-DPCCH2 tedy řeší konkrétní problém škálovatelnosti v řídicí rovině a zajišťuje, že HSPA může i v pozdějších vývojových fázích nadále využívat agregaci nosných pro růst kapacity.

## Klíčové vlastnosti

- Sekundární fyzický řídicí kanál v uplinku pro HSPA, používaný v konfiguracích Multi-Cell HSPA (MC-HSPA).
- Aktivuje se, když počet povolených sekundárních buněk (Secondary_Cell_Enabled) překročí práh (3 pro ne-4Tx MIMO, 1 pro 4Tx MIMO).
- Přenáší doplňkové informace CQI a HARQ-ACK pro sekundární obslužné buňky, čímž doplňuje primární HS-DPCCH.
- Používá strukturu 2ms podrámce a je kódově multiplexován v uplinku s nezávisle konfigurovaným výkonovým offsetem.
- Umožňuje podporu agregace downlinkových nosných vyššího řádu (např. 8-nosné HSDPA) bez komprese nebo zpoždění zpětné vazby.
- Definován v aktualizovaných specifikacích fyzické vrstvy (25.212, 25.213, 25.214) pro Release 17.

## Související pojmy

- [HS-DPCCH – High Speed Dedicated Physical Control Channel (Uplink)](/mobilnisite/slovnik/hs-dpcch/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [HS-DPCCH2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-dpcch2/)
