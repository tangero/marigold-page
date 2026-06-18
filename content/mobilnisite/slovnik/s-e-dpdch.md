---
slug: "s-e-dpdch"
url: "/mobilnisite/slovnik/s-e-dpdch/"
type: "slovnik"
title: "S-E-DPDCH – Secondary Dedicated Physical Data Channel for Enhanced Dedicated Channel"
date: 2025-01-01
abbr: "S-E-DPDCH"
fullName: "Secondary Dedicated Physical Data Channel for Enhanced Dedicated Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-e-dpdch/"
summary: "Sekundární fyzický kanál pro uplink v UMTS/HSPA používaný pro přenos uživatelských dat vylepšeného vyhrazeného kanálu (E-DCH). Funguje spolu s primárním E-DPDCH a zvyšuje přenosové rychlosti v uplinku"
---

S-E-DPDCH je sekundární fyzický kanál pro uplink v UMTS/HSPA, který přenáší uživatelská data vylepšeného vyhrazeného kanálu (Enhanced Dedicated Channel) spolu s primárním kanálem za účelem zvýšení přenosové rychlosti v uplinku.

## Popis

S-E-DPDCH (Secondary Dedicated Physical Data Channel for [E-DCH](/mobilnisite/slovnik/e-dch/)) je základní komponenta fyzické vrstvy ve specifikaci UMTS Terrestrial Radio Access ([UTRA](/mobilnisite/slovnik/utra/)), konkrétně pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Funguje jako součást Enhanced Uplink (EUL), známého také jako High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)). Primární funkcí kanálu je přenos datové části transportního kanálu E-DCH. Na rozdíl od vyhrazených kanálů pro přenos dat z dřívějších verzí standardu byly E-DCH a s ním spojené fyzické kanály, jako je S-E-DPDCH, zavedeny pro podporu paketově orientovaných, naplánovaných přenosů v uplinku s výrazně sníženou latencí a vyššími špičkovými datovými rychlostmi.

Z architektonického hlediska je S-E-DPDCH vždy konfigurován spolu s primárním [E-DPDCH](/mobilnisite/slovnik/e-dpdch/). Uživatelskému zařízení (UE) může být přiděleno více S-E-DPDCH v závislosti na jeho schopnostech a rozhodnutí síťového plánovače. Klíčovým rozlišovacím prvkem je rozprostírací faktor ([SF](/mobilnisite/slovnik/sf/)) a použitý kanalizační kód. S-E-DPDCH typicky používají pevný, nižší rozprostírací faktor (SF=2), který poskytuje vysokou hrubou přenosovou rychlost na kód. Síťový Node B, prostřednictvím řídicího rádiového řadiče pro E-DCH (Serving E-RNC), řídí přidělování těchto sekundárních kanálů pomocí absolutních příkazů (absolute grants) a relativních příkazů (relative grants) vysílaných na kanálech [E-AGCH](/mobilnisite/slovnik/e-agch/) a [E-RGCH](/mobilnisite/slovnik/e-rgch/). To umožňuje dynamické přizpůsobení kapacity na základě poptávky po přenosu v uplinku, rádiových podmínek a výkonové rezervy UE.

Provoz kanálu je úzce spojen s procesy Hybrid Automatic Repeat Request (HARQ). Bloky dat jsou přenášeny přes E-DPDCH(y) a přijímány Node B, který zasílá potvrzení (ACK/NACK) na kanálu E-HICH. Použití více S-E-DPDCH umožňuje vyšší datové rychlosti prostřednictvím kódového multiplexu. Například UE podporující konfiguraci 2xSF2+2xSF4 může současně používat dva S-E-DPDCH s SF2 a dva s SF4. Zpracování na fyzické vrstvě zahrnuje kanálové kódování (Turbo kódování), segmentaci fyzického kanálu, prokládání a modulaci (BPSK pro SF>=4, 4PAM pro SF=2), jak je definováno ve specifikacích 25.212 a 25.213. Řízení výkonu pro S-E-DPDCH je odvozeno od přidruženého DPCCH pomocí faktoru zesílení (βed) signalizovaného sítí.

Jeho role je klíčová ve vývoji HSPA, protože umožňuje dosažení teoretických maxim špičkových přenosových rychlostí v uplinku (např. 11,5 Mbps v Rel-7 s konfigurací 2xSF2+2xSF4). Představuje posun od výkonově řízeného uplinku s přepojováním okruhů k naplánovanému, kódově multiplexovanému uplinku pro pakety řízenému HARQ, což je základní koncept, který se později vyvinul v LTE a 5G NR.

## K čemu slouží

S-E-DPDCH byl vytvořen, aby překonal závažná omezení původního uplinku UMTS Release 99, který byl založen na jediném vyhrazeném fyzickém datovém kanálu (DPDCH) s proměnným rozprostíracím faktorem. Tento přístup byl neefektivní pro přerušovaná paketová data, protože se nemohl rychle přizpůsobit měnícím se objemům dat, což vedlo ke špatnému využití prostředků a omezeným špičkovým přenosovým rychlostem (typicky limitovaným na 384 kbps). Motivací pro Enhanced Uplink (E-DCH) v Rel-5/6 bylo zavést plánování paketů v Node B (snížení latence z ~100 ms na ~10 ms) a podpořit vyšší datové rychlosti.

Zavedení S-E-DPDCH v pozdějších verzích, zejména jako součást dalších vylepšení HSPA, bylo hnací silou potřeby ještě více zvýšit špičkové datové rychlosti v uplinku. Samotný primární E-DPDCH s omezenou sadou rozprostíracích faktorů představoval úzké hrdlo. Definováním sekundárních kanálů s pevným, nízkým rozprostíracím faktorem (jako SF2) standard umožnil agregaci více fyzických kódových kanálů s vysokou kapacitou. Tím se vyřešil problém, jak zvýšit propustnost bez nutnosti nadměrně široké šířky pásma nebo nových modulačních schémat v počáteční fázi. Umožnilo to stávajícím UE s vylepšenými schopnostmi využívat více dostupného kódového stromu za příznivých rádiových podmínek, což přímo vedlo k lepší uživatelské zkušenosti s aplikacemi náročnými na uplink, jako je nahrávání videa a přenos velkých souborů.

Historicky tato evoluce probíhala paralelně s vylepšeními HSDPA pro downlink, ale řešila jedinečnou výzvu uplinku, který je inherentně limitován vysílacím výkonem UE. Použitím více paralelních kódů (S-E-DPDCH) namísto pouhého zvýšení výkonu na jediném kódu mohl systém dosáhnout vyšších datových rychlostí při stejném výkonovém rozpočtu, protože celkový výkon je sdílen mezi kanály. Toto bylo spektrálně i výkonově efektivnější řešení než přístup před zavedením E-DCH.

## Klíčové vlastnosti

- Poskytuje dodatečné fyzické prostředky pro přenos dat E-DCH.
- Používá pevný rozprostírací faktor 2 (SF2) pro vysokou spektrální účinnost.
- Lze konfigurovat v násobcích spolu s primárním E-DPDCH na základě schopností UE.
- Výkon je řízen vzhledem k DPCCH pomocí signalizovaného faktoru zesílení βed.
- Umožňuje vyšší špičkové datové rychlosti v uplinku prostřednictvím kódového multiplexu.
- Dynamicky přidělován a odebírán plánovačem Node B prostřednictvím E-AGCH/E-RGCH.

## Související pojmy

- [E-DPDCH – E-DCH Dedicated Physical Data Channel](/mobilnisite/slovnik/e-dpdch/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [E-RGCH – E-DCH Relative Grant Channel](/mobilnisite/slovnik/e-rgch/)
- [E-HICH – EDCH HARQ Acknowledgement Indicator Channel](/mobilnisite/slovnik/e-hich/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [S-E-DPDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-e-dpdch/)
