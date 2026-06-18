---
slug: "npss"
url: "/mobilnisite/slovnik/npss/"
type: "slovnik"
title: "NPSS – Narrowband Primary Synchronization Signal"
date: 2025-01-01
abbr: "NPSS"
fullName: "Narrowband Primary Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/npss/"
summary: "NPSS je synchronizační signál v downlinku pro zařízení NB-IoT. Umožňuje zařízení detekovat buňku NB-IoT, dosáhnout časové a frekvenční synchronizace a identifikovat skupinu identit fyzické vrstvy buňk"
---

NPSS je první synchronizační signál v downlinku, který zařízení NB-IoT vyhledává, aby detekovalo buňku, dosáhlo časové a frekvenční synchronizace a identifikovalo skupinu identit fyzické vrstvy buňky.

## Popis

Úzkopásmový primární synchronizační signál (NPSS) je základní signál fyzické vrstvy v rádiové přístupové technologii Narrowband Internet of Things (NB-IoT). Vysílá jej základnová stanice ([eNB](/mobilnisite/slovnik/enb/) pro NB-IoT založené na LTE, gNB pro NB-IoT založené na NR) v downlinku. NPSS je speciálně navržen tak, aby zabíral velmi úzkou šířku pásma nosné NB-IoT, která činí přesně 180 kHz (což odpovídá jednomu fyzickému zdrojovému bloku LTE). Jeho hlavní úlohou je umožnit počáteční vyhledání buňky a synchronizaci pro uživatelské zařízení (UE) NB-IoT. Když je zařízení NB-IoT zapnuto nebo vstoupí do nové oblasti, skenuje podporovaná frekvenční pásma, aby detekovalo přítomnost NPSS, což signalizuje funkční buňku NB-IoT.

Technicky je NPSS vysílán v subrámu #5 každého rádiového rámce (trvání 10 ms) na nosné NB-IoT. V kmitočtové oblasti zabírá 11 sousedních subnosičů v rámci šířky pásma 180 kHz. Samotný signál je vytvořen z Zadoff-Chuovy sekvence délky 11, která má konstantní amplitudu a vlastnosti nulové autokorelace, což ji činí snadno detekovatelnou i v podmínkách velmi nízkého poměru signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)). Tato odolnost je klíčová pro cíle rozšíření pokrytí NB-IoT, které počítají s až o 20 dB vyšším rozpočtem spoje než u staršího LTE. UE provádí korelační proces mezi přijímaným signálem a známými sekvencemi NPSS, aby identifikovalo přesné časování symbolu a začátek subrámce. Tento proces poskytuje synchronizaci časování symbolů a hrubou frekvenční synchronizaci, čímž koriguje velké frekvenční odchylky způsobené oscilátory nízkonákladových zařízení.

Po detekci NPSS pokračuje UE v detekci úzkopásmového sekundárního synchronizačního signálu ([NSSS](/mobilnisite/slovnik/nsss/)), který je vysílán v subrámu #9. Společně NPSS a NSSS umožňují UE určit 504 unikátních identit fyzické vrstvy buňky ([PCI](/mobilnisite/slovnik/pci/)) buňky NB-IoT. NPSS je společný pro všechny buňky (sám neobsahuje informaci o identitě buňky), zatímco sekvence NSSS se liší. Synchronizovaný čas z NPSS je také nezbytný pro správný příjem úzkopásmového fyzického vysílacího kanálu (NPBCH) a následných bloků systémových informací, které obsahují klíčové parametry pro přístup k buňce. Návrh NPSS s jeho jednoduchou strukturou a opakovaným vysíláním minimalizuje složitost UE a spotřebu energie během fáze počátečního vyhledávání buňky, což jsou prvořadé požadavky pro nízkonákladová, bateriově napájená IoT zařízení.

## K čemu slouží

NPSS byl vytvořen jako základní součást nového rozhraní NB-IoT standardizovaného ve 3GPP Release 13. Před NB-IoT používala zařízení LTE pro vyhledání buňky primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)) a sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)). Tyto synchronizační signály LTE však byly navrženy pro systémové šířky pásma 1,4 MHz a větší a nebyly optimalizovány pro extrémní pokrytí, ultranízký výkon a ultranízkou složitost požadovanou pro hromadný IoT. Stávající PSS/SSS z LTE by byly v šířce pásma 180 kHz a scénářích hlubokého pokrytí předpokládaných pro NB-IoT neefektivní nebo dokonce nedetekovatelné.

Účelem NPSS je vyřešit základní problém počátečního zachycení buňky za přísných omezení NB-IoT. Musel poskytovat robustní časovou a frekvenční synchronizaci pro zařízení, která mohou být umístěna ve sklepích nebo venkovských oblastech s velmi slabým signálem, a zároveň využívat minimální výpočetní výkon zařízení k zachování životnosti baterie. Návrhová rozhodnutí – jako použití jedné pevné Zadoff-Chuovy sekvence, její vysílání v známém subrámu a obsazení téměř celé šířky pásma nosné – byla všechna řízena těmito požadavky. NPSS umožňuje zařízení NB-IoT rychle a spolehlivě najít síť, což je nezbytný první krok pro jakoukoli komunikaci. Jeho zavedení bylo klíčovým faktorem úspěchu NB-IoT jako specializované celulární IoT technologie, neboť poskytuje synchronizační mechanismus šitý na míru komunikaci typu stroj-stroj, namísto adaptace mechanismu navrženého pro širokopásmové služby orientované na člověka.

## Klíčové vlastnosti

- Vysílán v subrámu #5 každého 10ms rádiového rámce v NB-IoT
- Používá Zadoff-Chuovu sekvenci délky 11 pro robustní detekci
- Zabírá 11 sousedních subnosičů v rámci šířky pásma NB-IoT 180 kHz
- Poskytuje UE synchronizaci časování symbolů a hrubou frekvenční synchronizaci
- Společný signál pro všechny buňky NB-IoT (nepřenáší identitu buňky)
- Optimalizován pro detekci v extrémních podmínkách pokrytí až do 164 dB MCL

## Související pojmy

- [NSSS – Narrowband Secondary Synchronization Signal](/mobilnisite/slovnik/nsss/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)

## Definující specifikace

- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NPSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/npss/)
