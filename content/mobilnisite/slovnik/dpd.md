---
slug: "dpd"
url: "/mobilnisite/slovnik/dpd/"
type: "slovnik"
title: "DPD – Digital Pre-Distortion"
date: 2025-01-01
abbr: "DPD"
fullName: "Digital Pre-Distortion"
category: "Physical Layer"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/dpd/"
summary: "Digital Pre-Distortion (DPD, digitální předzkreslení) je technika zpracování signálu aplikovaná ve vysílači za účelem linearizace výstupu výkonového zesilovače (PA). Kompenzuje nelineární zkreslení za"
---

DPD (digitální předzkreslení) je technika zpracování signálu v vysílači, která linearizuje výkonový zesilovač kompenzací jeho nelineárních zkreslení, čímž zlepšuje věrnost signálu a spektrální účinnost.

## Popis

Digital Pre-Distortion (digitální předzkreslení) je sofistikovaná linearizační technika implementovaná v digitální základní pásmové části vysílače. Funguje tak, že na digitální vstupní signál aplikuje inverzní nelineární funkci, než je tento signál převeden na analogový a přiveden do výkonového zesilovače. Základním principem je předzkreslení signálu tak, aby kombinovaný účinek funkce DPD a inherentní nelinearity zesilovače PA vedl k lineárnímu, zesílenému výstupu. To vyžaduje přesné modelování nelineárních charakteristik zesilovače PA, kterého se typicky dosahuje pomocí adaptivních algoritmů, které průběžně odhadují chování zesilovače PA na základě zpětné vazby z jeho výstupu.

Architektura systému DPD zahrnuje několik klíčových komponent: procesor digitálního signálu ([DSP](/mobilnisite/slovnik/dsp/)) implementující algoritmus předzkreslení, zpětnovazební přijímací cestu a blok identifikace modelu. Zpětnovazební cesta odebírá část zesíleného výstupu z PA, převádí jej dolů a digitalizuje. Tento digitalizovaný výstupní signál je porovnáván s původním vstupním signálem v bloku identifikace modelu, který aktualizuje parametry modelu předzkreslení. Mezi běžné modely patří modely paměťových polynomů a Volterrovy řady, které zohledňují jak statickou nelinearitu, tak paměťové efekty způsobené tepelnou dynamikou a variacemi impedance v zesilovači PA.

Úloha DPD v síti je primárně v rádiové přístupové síti (RAN), konkrétně ve vysílacím řetězci základnové stanice (eNodeB/gNodeB). Linearizací zesilovače PA umožňuje DPD, aby zesilovač pracoval blíže svému saturačnímu bodu (vyšší účinnost), aniž by generoval nadměrné mimopásmové emise nebo zkreslení v pásmu. To přímo zlepšuje velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) vysílaného signálu, což je klíčové pro modulační schémata vyššího řádu, jako je 256-QAM nebo 1024-QAM používaná v 4G a 5G. Dále pomáhá vysílači splňovat regulační spektrální masky, čímž zabraňuje rušení sousedních kanálů a umožňuje efektivnější využití spektra.

## K čemu slouží

Primárním účelem Digital Pre-Distortion je překonání základního kompromisu mezi účinností a linearitou výkonového zesilovače. Výkonové zesilovače jsou nejúčinnější při provozu blízko saturace, ale tato oblast je vysoce nelineární, což způsobuje zkreslení signálu a spektrální zpětný růst, který ruší sousední kanály. Před rozšířeným přijetím DPD musely systémy 'ustupovat' s provozem zesilovače PA do lineárnější, ale méně účinné oblasti, což plýtvalo značným množstvím stejnosměrného výkonu a zvyšovalo provozní náklady, zejména ve výkonných základnových stanicích.

Jeho vznik byl motivován vývojem směrem ke komplexním modulačním schématům a širším šířkám pásma v 3G a zejména v 4G LTE. Tyto pokročilé signály mají vysoký poměr špičkového a průměrného výkonu (PAPR) a jsou extrémně citlivé na nelineární zkreslení. DPD se stala nezbytnou technologií pro umožnění těchto spektrálně účinných modulací bez obětování účinnosti zesilovače. Řešila omezení předchozích analogových linearizačních technik, jako je předstupeňová nebo zpětnovazební linearizace, které byly složité, úzkopásmové a méně přizpůsobivé.

Historicky jeho standardizace v 3GPP odráží jeho důležitost pro výkon sítě a koexistenci. Specifikace jako 33.320 a 38.877 se zabývají jeho aplikací a testováním, což zajišťuje konzistentní implementaci pro síťové vybavení. DPD je klíčovým prvkem pro husté využití spektra a vysokou datovou propustnost vyžadovanou moderními buněčnými standardy, což z ní činí základní technologii pro efektivní infrastrukturu RAN.

## Klíčové vlastnosti

- Linearizuje výstup výkonového zesilovače (PA) za účelem snížení spektrálního zpětného růstu a zkreslení v pásmu
- Umožňuje provoz zesilovače PA s vyšší účinností (blíže saturaci), čímž snižuje spotřebu energie
- Využívá adaptivní algoritmy založené na zpětné vazbě z výstupu PA pro korekci modelu v reálném čase
- Podporuje širokopásmové signály a kompenzuje kromě statické nelinearity i paměťové efekty
- Kritické pro podporu modulace QAM vyššího řádu (např. 256QAM, 1024QAM) s nízkým EVM
- Pomáhá zajistit soulad s přísnými regulačními spektrálními emisními maskami (např. ACLR)

## Související pojmy

- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [CFR – Code of Federal Regulations](/mobilnisite/slovnik/cfr/)

## Definující specifikace

- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [DPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpd/)
