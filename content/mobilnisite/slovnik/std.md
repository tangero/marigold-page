---
slug: "std"
url: "/mobilnisite/slovnik/std/"
type: "slovnik"
title: "STD – Selective Transmit Diversity"
date: 2025-01-01
abbr: "STD"
fullName: "Selective Transmit Diversity"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/std/"
summary: "Selective Transmit Diversity (STD) je technika přenosu v downlinku, kdy síť vybere nejlepší buňku ze sady pro vysílání k UE, namísto vysílání ze všech buněk současně. Zlepšuje kvalitu downlink signálu"
---

STD je technika přenosu v downlinku, při níž síť vybere jedinou nejlepší buňku ze sady pro vysílání k uživatelskému zařízení, čímž zlepšuje kvalitu signálu a snižuje interferenci.

## Popis

Selective Transmit Diversity (STD) je síťová diverzitní technika používaná v downlinku buněčných systémů, definovaná zejména v UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) a později zvažovaná v kontextu 5G NR. Jejím základním principem je zlepšení kvality přijímaného downlink signálu na uživatelském zařízení (UE) selektivním vysíláním z buňky nebo Node B, která poskytuje nejlepší rádiové podmínky v daném okamžiku, namísto použití měkčích forem diverzity, jako je vysílací diverzita z více bodů současně. Síť tento výběr provádí dynamicky na základě hlášení o měření poskytovaných UE.

Architektonicky STD funguje v rámci řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS nebo centrální jednotky v pozdějších architekturách. UE průběžně měří kvalitu (např. [CPICH](/mobilnisite/slovnik/cpich/) [Ec](/mobilnisite/slovnik/ece-c/)/No v UMTS) signálů z buněk ve svém aktivním souboru – tedy souboru buněk aktivně zapojených do spojení při měkkém/měkčím předávání hovoru. Tato měření jsou hlášena síti prostřednictvím zpráv Measurement Report. Algoritmy RNC pak tyto zprávy analyzují. Namísto udržování současného vysílání ze všech buněk v aktivním souboru (jako u standardního měkkého předání hovoru) algoritmus STD vybere jedinou 'nejlepší' buňku, která se stane primární vysílající buňkou pro downlinkový vyhrazený fyzický kanál ([DPCH](/mobilnisite/slovnik/dpch/)). Ostatní buňky v aktivním souboru mohou vysílání ukončit nebo vysílat na velmi nízký výkon, přičemž primárně udržují uplink pro diverzitní příjem.

Klíčový technický mechanismus zahrnuje zaslání 'indexu kombinace řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/) Combination Index)' nevybraným buňkám s pokynem, aby přestaly vysílat downlinkový DPCH. Výběr není statický; může se rychle měnit (řádově v stovkách milisekund) na základě útlumového prostředí a mobility UE. To vyžaduje těsnou koordinaci a signalizaci mezi RNC a Node B. Výhody jsou dvojí: za prvé se zlepšuje poměr signálu k interferenci ([SIR](/mobilnisite/slovnik/sir/)) v downlinku pro UE tím, že se eliminuje interference, která by pocházela od ostatních buněk vysílajících stejný signál, ale s mírně odlišnými zpožděními (což může být destruktivní). Za druhé se snižuje celkový vysílací výkon v downlinku v síti, čímž se snižuje celková úroveň interference a zvyšuje kapacita systému.

Ve vývoji směrem k 5G se podobné koncepty znovu objevují ve formě dynamického výběru bodu (Dynamic Point Selection, DPS) v rámci schémat koordinovaného vícebodového přenosu/příjmu (Coordinated Multi-Point, CoMP). Zatímco konkrétní termín 'STD' je ve specifikacích NR méně běžný, základní princip dynamického výběru optimálního přenosového/přijímacího bodu (Transmission Reception Point, [TRP](/mobilnisite/slovnik/trp/)) ze spolupracující sady je přímým vývojem, který využívá pokročilejší informace o stavu kanálu a rychlejší přenosovou síť. Role STD byla primárně zvýšení kapacity a kvality sítí UMTS založených na WCDMA, což poskytlo nákladově efektivní vylepšení před rozšířeným nasazením systémů založených na MIMO a OFDMA.

## K čemu slouží

Selective Transmit Diversity byl vyvinut k řešení specifických omezení rozhraní WCDMA v UMTS, zejména problémů s kapacitou downlinku v oblastech měkkého předávání hovoru. Při standardním měkkém předávání hovoru si UE v překryvné oblasti více buněk udržuje současná spojení s nimi. Zatímco to poskytuje zisk makrodiverzity v uplinku (zlepšení příjmu v síti), v downlinku vytváří problém. Stejná data jsou vysílána z více buněk, což se v důsledku povahy WCDMA jeví jako více signálů přicházejících k UE. Pokud nejsou dokonale synchronizovány, mohou tyto signály vzájemně interferovat, čímž se zhoršuje downlinkový SIR. Tento jev je znám jako zvýšení interference v downlinku při měkkém předávání hovoru.

STD byl zaveden, aby získal zpět tuto ztracenou výkonnost downlinku. Selektivním vysíláním pouze z nejlepší buňky eliminuje tuto vnitro-spojovací interferenci. To byl významný motivátor, protože zvýšení kapacity downlinku bylo klíčové pro podporu vznikajících datových služeb v UMTS. Řešilo to problém bez nutnosti dodatečného hardwaru na Node B; šlo primárně o softwarový upgrade algoritmů RNC. Historický kontext řadí STD vedle dalších vylepšení, jako je vyvažování výkonu downlinkového vyhrazeného fyzického kanálu (DL DPCH) a pokročilé přijímače.

Dále STD pomáhalo snížit celkovou spotřebu energie rádiové přístupové sítě. Vysílání z více buněk zvyšuje celkový vyzářený výkon, což zvyšuje provozní náklady a zvyšuje základní úroveň interference pro ostatní uživatele. Selektivním vypínáním nevhodných vysílačů STD zlepšovalo energetickou účinnost sítě. Jeho vytvoření bylo motivováno potřebou vytěžit maximální výkon z existujících nasazení UMTS před přechodem na HSPA a LTE, které používaly odlišné schéma mnohonásobného přístupu (OFDMA/SC-FDMA) a techniky MIMO, které inherentně řídily interferenci a diverzitu odlišným způsobem.

## Klíčové vlastnosti

- Dynamicky vybírá jedinou nejlepší buňku z aktivního souboru pro downlinkový přenos k UE
- Snižuje downlinkovou intraceliovou interferenci v oblastech měkkého předávání hovoru
- Zlepšuje poměr signálu k interferenci (SIR) v downlinku a celkovou kapacitu
- Implementováno jako síťový algoritmus v RNC (UMTS) na základě hlášení o měření od UE
- Snižuje celkový vysílací výkon sítě, čímž zlepšuje energetickou účinnost
- Doplňuje příjem s makrodiverzitou v uplinku, kde více buněk přijímá signál UE

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR

---

📖 **Anglický originál a plná specifikace:** [STD na 3GPP Explorer](https://3gpp-explorer.com/glossary/std/)
