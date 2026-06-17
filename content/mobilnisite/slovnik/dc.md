---
slug: "dc"
url: "/mobilnisite/slovnik/dc/"
type: "slovnik"
title: "DC – Dual Connectivity"
date: 2026-01-01
abbr: "DC"
fullName: "Dual Connectivity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dc/"
summary: "Dual Connectivity (DC) je funkce 3GPP umožňující uživatelskému zařízení (UE) současné připojení ke dvěma různým síťovým uzlům, typicky k hlavnímu uzlu (MN) a sekundárnímu uzlu (SN). Agreguje rádiové p"
---

DC je funkce 3GPP, při které se zařízení současně připojuje ke dvěma síťovým uzlům, aby agregovalo jejich rádiové prostředky pro vyšší datový propust, lepší mobilitu a vyváženější vytížení v sítích 4G/5G.

## Popis

Dual Connectivity (DC) je základní funkce správy rádiových prostředků ve standardech 3GPP, která umožňuje jednomu uživatelskému zařízení (UE) udržovat souběžná spojení se dvěma různými síťovými uzly, označovanými jako hlavní uzel ([MN](/mobilnisite/slovnik/mn/)) a sekundární uzel (SN). Tyto uzly mohou patřit ke stejné nebo různým rádiovým přístupovým technologiím (RAT), jako je LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). UE je konfigurováno se dvěma samostatnými protokolovými zásobníky, jedním pro každý uzel, což umožňuje simultánní přenos a příjem dat po obou rádiových spojích. MN poskytuje spojení řídicí roviny k jádru sítě (např. přes S1-MME nebo NG-C) a spravuje celkový kontext UE včetně zřizování, modifikace a uvolňování sekundárního spojení. SN poskytuje dodatečné rádiové prostředky pro uživatelskou rovinu, čímž zvyšuje kapacitu. Data mohou být rozdělována na různých vrstvách protokolu (např. PDCP, RLC) v závislosti na variantě architektury DC (např. nosič [MCG](/mobilnisite/slovnik/mcg/), nosič SCG, rozdělený nosič).

Architektura je definována rolemi zapojených uzlů. V LTE DC (zavedeno jako LTE-NR Dual Connectivity neboli [EN-DC](/mobilnisite/slovnik/en-dc/)) typicky [eNB](/mobilnisite/slovnik/enb/) funguje jako MN (MeNB) a gNB jako SN (SgNB). V 5G NR DC (NR-NR DC neboli [NE-DC](/mobilnisite/slovnik/ne-dc/)) jsou role definovány jako MN (např. gNB) a SN (další gNB). Uzly jsou vzájemně propojeny standardizovanými rozhraními: rozhraním X2 pro uzly založené na LTE a rozhraním Xn pro uzly založené na NR. Tato rozhraní přenášejí signalizaci řídicí roviny (např. procedury přidání/modifikace/uvolnění SN) a data uživatelské roviny pro nosiče ukončené v SN. UE udržuje dvě skupiny buněk: hlavní skupinu buněk (MCG) asociovanou s MN a sekundární skupinu buněk (SCG) asociovanou se SN. Každá skupina se skládá z primární buňky (PCell nebo PSCell) a volitelně jedné nebo více sekundárních buněk (SCell).

Z provozního hlediska DC zahrnuje složitou koordinaci. MN rozhoduje o přidání SN na základě měřicích hlášení od UE a vlastních podmínek zatížení. Iniciuje proceduru přidání SN přes rozhraní X2/Xn a přenese potřebný kontext UE. SN následně provede vlastní řízení přístupu a v případě úspěchu nakonfiguruje pro UE prostředky. MN poskytne konečnou konfiguraci UE prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), která může zahrnovat i sekundární konfiguraci RRC od SN (v případě NR DC). Pro uživatelskou rovinu mohou být data směrována různými způsoby. V konfiguraci rozděleného nosiče vrstva PDCP v MN zpracovává duplikaci paketů, jejich řazení a může směrovat pakety buď do vlastní vrstvy RLC (pro větev MCG), nebo do vrstvy RLC SN (pro větev SCG) přes rozhraní X2/Xn-U. To vyžaduje těsnou synchronizaci a řízení toku mezi uzly, aby se minimalizovala zpoždění způsobená přeřazováním paketů na přijímací straně.

Role DC v síti je mnohostranná. Primárně jde o nástroj pro zvýšení kapacity, který agreguje spektrum a rádiové prostředky ze dvou přenosových bodů, aby dosáhl špičkových datových rychlostí přesahujících možnosti jediného uzlu. Je také klíčovým vylepšením mobility; udržováním stabilního kotvícího spojení (MCG) umožňuje plynulejší předávání SCG, čímž snižuje riziko selhání rádiového spoje při pohybu mezi buňkami. Dále umožňuje efektivní vyvažování zátěže mezi různými síťovými vrstvami (např. makro a small buňkami) nebo různými kmitočtovými pásmy. V 5G je DC základem pro pokročilejší schémata více-násobného připojení a je nezbytné pro využití nestand-alone (NSA) architektur, kde kotva LTE poskytuje robustní pokrytí a řízení, zatímco spojení NR zajišťuje vysokou propustnost.

## K čemu slouží

Dual Connectivity byl vytvořen, aby řešil rostoucí poptávku po vyšších uživatelských datových rychlostech a robustnějším mobilním zážitku, které nemohlo být uspokojeno jediným připojením k jedné síťové buňce. Před DC umožňovalo agregaci nosných ([CA](/mobilnisite/slovnik/ca/)) agregovat komponentní nosné z jediné základnové stanice, to však bylo omezeno geografickým pokrytím a kapacitou tohoto jediného uzlu. DC toto omezení překonává tím, že umožňuje agregaci napříč geograficky oddělenými uzly, čímž efektivně sdružuje prostředky makro buňky a small buňky. To bylo obzvláště důležité pro nasazení heterogenních sítí (HetNet), kde jsou small buňky nasazovány pro zvýšení kapacity v oblastech s vysokou koncentrací uživatelů, ale vyžadují stabilní vrstvu makro buněk pro řízení a pokrytí.

Historicky se tento koncept vyvinul z dřívějších technik koordinace více bodů. Jeho formální zavedení v 3GPP Release 12 (pro LTE-LTE DC) bylo hnací silou potřeby zlepšení propustnosti na uživatele a výkonu mobility v hustých sítích. Klíčový problém, který řešil, byl 'ping-pong' efekt v nasazeních small buněk, kde častá předávání mohla degradovat výkon. Ukotvením řídicí roviny na makro buňce (MN) a přidáním small buňky jako SN pro data poskytlo DC stabilní spojení a zároveň dynamicky přidávalo a odebíralo kapacitu. To také zlepšilo energetickou účinnost sítě tím, že umožnilo aktivovat SN pouze v případě potřeby pro vysoký datový provoz.

Motivace zesílila s příchodem 5G. Počáteční nasazení 5G používala nestand-alone (NSA) architekturu, která zásadně závisela na LTE-NR Dual Connectivity (EN-DC), aby poskytla 5G datovou přípojku (přes NR gNB jako SN) při zachování LTE eNB jako řídicí kotvy. To umožnilo rychlé zavedení služeb 5G s využitím stávajících LTE jader sítě. Dále, jak se sítě 5G vyvíjely do stand-alone (SA) režimu, se NR-NR DC (a později více-RAT DC) stalo nezbytným pro agregaci různých kmitočtových rozsahů NR (např. FR1 a FR2/mmWave) za účelem kombinace pokrytí a kapacity, což zajišťuje konzistentní vysoký výkon i v případě, že jeden spoj (jako mmWave) je náchylný k překážkám.

## Klíčové vlastnosti

- Současné připojení k hlavnímu uzlu a sekundárnímu uzlu
- Agregace uživatelské roviny pro zvýšení špičkové datové rychlosti
- Ukotvení řídicí roviny na hlavním uzlu pro robustnost
- Podpora více kombinací RAT (např. LTE-LTE, LTE-NR, NR-NR)
- Flexibilní typy nosičů (MCG, SCG a rozdělený nosič) pro optimalizaci směrování dat
- Vylepšená mobilita a vyvažování zátěže napříč síťovými vrstvami

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.392** (Rel-19) — MMTel Application Enablement
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.392** (Rel-19) — MMTel Data Channel Application Profile Management
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.707** (Rel-14) — Multi-Carrier Enhancements for UMTS Study
- … a dalších 92 specifikací

---

📖 **Anglický originál a plná specifikace:** [DC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dc/)
