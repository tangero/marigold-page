---
slug: "irc"
url: "/mobilnisite/slovnik/irc/"
type: "slovnik"
title: "IRC – Interference Rejection Combining"
date: 2025-01-01
abbr: "IRC"
fullName: "Interference Rejection Combining"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/irc/"
summary: "Technika zpracování signálu v přijímači LTE a NR, která zlepšuje kvalitu signálu kombinací více anténních signálů za účelem potlačení ko-kanálového rušení. Zvyšuje propustnost na okraji buňky a celkov"
---

IRC je technika zpracování signálu v přijímači LTE a NR, která zlepšuje kvalitu signálu kombinací více anténních signálů za účelem potlačení ko-kanálového rušení, čímž zvyšuje propustnost na okraji buňky a kapacitu sítě.

## Popis

Interference Rejection Combining (IRC) je pokročilý přijímací algoritmus implementovaný v uživatelském zařízení (UE) nebo základnové stanici (eNodeB/gNB) pro boj s ko-kanálovým rušením, které je hlavním omezujícím faktorem výkonu v celulárních sítích. Na rozdíl od tradičního Maximum Ratio Combining ([MRC](/mobilnisite/slovnik/mrc/)), které maximalizuje výkon požadovaného signálu, ale zachází s rušením jako s nekorelovaným šumem, IRC explicitně odhaduje prostorové charakteristiky rušení. Toho dosahuje výpočtem kovarianční matice přijatého rušení-plus-šumu napříč více přijímacími anténami. Tato matice zachycuje korelaci rušivých signálů mezi anténními prvky. Přijímač následně aplikuje vektor kombinačních vah, který je odvozen nejen z kanálu požadovaného signálu, ale také nepřímo úměrný této kovarianční matici rušení. Matematicky jsou váhy navrženy tak, aby maximalizovaly poměr signálu k rušení-plus-šumu ([SINR](/mobilnisite/slovnik/sinr/)), čímž efektivně vytvářejí prostorový filtr, který potlačuje směry, ze kterých přichází silné rušení.

Architektura pro IRC je integrována do řetězce přijímače fyzické vrstvy, následuje po [RF](/mobilnisite/slovnik/rf/) předzesilovači a analogově-digitálním převodu. Klíčové komponenty zahrnují odhadovač kanálu, který poskytuje informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) pro požadovaný signál, a odhadovač rušení, který průběžně monitoruje a aktualizuje kovarianční matici rušení. Tento odhad se typicky provádí na referenčních symbolech, jako jsou Cell-specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Demodulation Reference Signals ([DM-RS](/mobilnisite/slovnik/dm-rs/)) v NR, které jsou přijímači známé. Výpočetní jádro řeší optimální kombinační váhy, často za použití algoritmů založených na kritériu Minimum Mean Square Error ([MMSE](/mobilnisite/slovnik/mmse/)). Kombinovaný signál je poté předán do fází demodulace a dekódování. IRC pracuje na bázi jednotlivých subnosných nebo bloků zdrojů (resource block) v systémech [OFDMA](/mobilnisite/slovnik/ofdma/), což umožňuje jemně odstupňované potlačení rušení napříč frekvenční doménou.

Role IRC v síti je klíčová pro správu rušení jak v homogenních nasazeních makro buněk, tak v heterogenních sítích (HetNets) s malými buňkami. V LTE je to klíčová funkce pro pokročilá UE (např. kategorie 6 a výše) pro zlepšení výkonu na downlinku. V 5G NR jsou principy IRC základem pro sofistikovanější víceanténní techniky, jako je pokročilé zmírňování rušení v Massive MIMO a operace Coordinated Multi-Point (CoMP). Jde o vylepšení na straně přijímače, což znamená, že zlepšuje výkon bez nutnosti koordinace mezi vysílajícími buňkami, a je tak nákladově efektivním řešením pro přírůstkové zisky kapacity sítě. Tato technika je nezbytná pro naplnění slibů 5G o vysoké spolehlivosti a vysoké přenosové rychlosti, zejména v ultra-hustých městských scénářích, kde je rušení dominantním omezením.

## K čemu slouží

IRC bylo vytvořeno, aby řešilo základní výzvu ko-kanálového rušení v celulárních sítích využívajících frekvenční reužití. Jak se sítě vyvíjely směrem k vyšší spektrální účinnosti agresivním opakovaným používáním stejných frekvenčních pásem v sousedních buňkách, stalo se rušení ze sousedních základnových stanic a od jiných uživatelů hlavním omezením přenosových rychlostí, zejména pro uživatele na okrajích buněk. Tradiční přijímače jako MRC byly navrženy pro prostředí omezená šumem a v těchto podmínkách omezených rušením si vedly špatně, což vedlo ke špatnému uživatelskému zážitku a nerovnoměrnému pokrytí sítě.

Motivace pro standardizaci IRC v 3GPP, počínaje Release 8, byla využít rostoucí nasazování více přijímacích antén v UE (MIMO technologie) pro účel, který přesahuje prostorovou diverzitu nebo multiplexování: aktivní potlačení rušení. To poskytlo významný výkonnostní přínos bez nutnosti změn v síťovém přenosovém schématu nebo vyžadování složitých protokolů mezibuněčné koordinace. Vyřešilo problém 'utrpení na okraji buňky' tím, že umožnilo přijímači digitálně odfiltrovat dominantní rušiče, čímž se zvýšil efektivní SINR a umožnilo se spolehlivě používat modulace a kódovací schémata vyššího řádu.

Historicky, před IRC, sítě spoléhaly na statické frekvenční plánování, koordinaci rušení (ICIC) nebo snížení faktorů reuše – vše za cenu obětování celkové spektrální účinnosti. IRC představovalo posun směrem k inteligentnímu, adaptivnímu zpracování v přijímači, které dokáže dynamicky bojovat s rušením. Jeho zavedení bylo klíčovým krokem v přechodu sítí z omezených šumem na efektivně spravované z hlediska rušení, což připravilo cestu pro husté, vysokokapacitní sítě vyžadované pro služby 4G a 5G.

## Klíčové vlastnosti

- Prostorové potlačení rušení využívající více přijímacích antén
- Výpočet kovarianční matice rušení-plus-šumu
- Aplikace optimálních kombinačních vah založených na MMSE
- Zpracování na úrovni jednotlivých subnosných nebo bloků zdrojů (resource block) v OFDMA
- Funguje na známých referenčních signálech (např. CRS, DM-RS) pro odhad
- Vylepšení implementovatelné v UE bez povinných změn na straně sítě

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)

## Definující specifikace

- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.859** (Rel-13) — Study on Downlink Multiuser Superposition Transmission
- **TS 36.866** (Rel-12) — Study on Network Assisted Interference Cancellation
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [IRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/irc/)
