---
slug: "ssss"
url: "/mobilnisite/slovnik/ssss/"
type: "slovnik"
title: "SSSS – Secondary Sidelink Synchronization Signal"
date: 2025-01-01
abbr: "SSSS"
fullName: "Secondary Sidelink Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssss/"
summary: "Synchronizační signál používaný v postranním spoji (sidelink) LTE a 5G NR pro komunikaci mezi zařízeními. Funguje společně s Primárním postranním synchronizačním signálem (PSSS) a umožňuje uživatelský"
---

SSSS je Sekundární postranní (sidelink) synchronizační signál používaný v LTE a 5G NR pro komunikaci mezi zařízeními (device-to-device), který společně s PSSS umožňuje přímé zjišťování (discovery) a synchronizaci mezi uživatelskými zařízeními.

## Popis

Sekundární postranní synchronizační signál (SSSS) je základní signál fyzické vrstvy definovaný pro komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), konkrétně v rámci postranního spoje ([SL](/mobilnisite/slovnik/sl/)) LTE a 5G NR. Jeho hlavní úlohou je umožnit časovou a frekvenční synchronizaci mezi uživatelskými zařízeními (UE) pracujícími v přímém komunikačním režimu, nezávisle na infrastruktuře mobilní sítě. SSSS je vždy vysílán společně s Primárním postranním synchronizačním signálem ([PSSS](/mobilnisite/slovnik/psss/)), čímž vytváří pár synchronizačních signálů. Tento pár vysílá UE fungující jako zdroj synchronizace, kterým může být eNodeB/gNodeB (v pokrytí sítí), jiné UE (mimo pokrytí) nebo globální navigační satelitní systém ([GNSS](/mobilnisite/slovnik/gnss/)). Příjem těchto signálů umožňuje sousedním UE dosáhnout hrubé synchronizace, odhadnout časování rádiového rámce postranního spoje a identifikovat typ zdroje synchronizace.

Z architektonického hlediska je SSSS mapován na specifické zdrojové prvky v rámci podrámce pro synchronizaci postranního spoje. V LTE jsou například PSSS a SSSS vysílány ve dvou po sobě jdoucích symbolech. SSSS nese klíčové informace zakódované ve své sekvenci. Konkrétně přenáší část identity synchronizace postranního spoje ([SLSS](/mobilnisite/slovnik/slss/) ID), která v kombinaci s informací z PSSS jednoznačně identifikuje zdroj synchronizace. Rozsah SLSS ID je rozdělen tak, aby indikoval, zda je zdroj uvnitř sítě nebo mimo síť. Dále je sekvence SSSS odvozena od Zadoff-Chuovy sekvence, vybrané pro své dobré autokorelační a zkřížené korelační vlastnosti, které jsou klíčové pro spolehlivou detekci v náročných rádiových podmínkách.

Z provozního hlediska musí UE, které chce zahájit nebo se připojit k relaci komunikace po postranním spoji, nejprve tyto synchronizační signály vyhledat. Po detekci páru PSSS/SSSS UE provede odhad časování a frekvenčního posunu. Dekódované SLSS ID informuje UE o charakteristikách zdroje synchronizace, což mu umožní odpovídajícím způsobem sladit své vysílací a přijímací časování. Tento proces je základním kamenem pro zřízení řídicích a datových kanálů postranního spoje (např. [PSCCH](/mobilnisite/slovnik/pscch/), [PSSCH](/mobilnisite/slovnik/pssch/)). SSSS tedy není pouze časovým referenčním bodem, ale také nositelem základních systémových informací pro ad-hoc síť postranního spoje, což umožňuje škálovatelné a efektivní zjišťování a komunikaci mezi blízkými zařízeními bez nutnosti neustálé závislosti na síťovém časování.

## K čemu slouží

SSSS byl zaveden, aby vyřešil základní výzvu zřízení synchronizace ve scénářích přímé komunikace mezi zařízeními, kde nemusí být přítomna nebo preferována základnová stanice mobilní sítě. Před službami komunikace na krátkou vzdálenost ([ProSe](/mobilnisite/slovnik/prose/)) v 3GPP byla komunikace mezi zařízeními výhradně síťově centrická a vyžadovala, aby veškerý provoz procházel přes eNodeB. Tato architektura zaváděla latenci a byla neefektivní pro místní komunikaci, jako je skupinová komunikace pro veřejnou bezpečnost nebo výstrahy mezi vozidly. Vytvoření vyhrazeného rozhraní pro postranní spoj si vyžádalo nový synchronizační mechanismus, protože UE již nemohla záviset pouze na signálech příjemného spoje z pevné infrastruktury.

Motivací pro SSSS společně s PSSS bylo umožnit autonomní synchronizaci v různých modelech nasazení: v pokrytí, částečném pokrytí a mimo pokrytí. V případech použití pro veřejnou bezpečnost a vozidlovou komunikaci (V2X) musí být komunikace odolná a možná i v případě poškození nebo nedostupnosti síťové infrastruktury. SSSS poskytuje prostředky pro UE k vytváření samoorganizujících se sítí. Řeší omezení předchozích mobilních systémů, kterým chyběla standardizovaná přímá synchronizační schopnost mezi zařízeními, a tím odemyká nové paradigmy služeb, jako je přímé zjišťování, přenosové operace a aplikace V2X s nízkou latencí, které jsou klíčové pro bezpečnost a provozní efektivitu.

## Klíčové vlastnosti

- Umožňuje časovou a frekvenční synchronizaci mezi zařízeními bez síťové infrastruktury.
- Nese část identity synchronizace postranního spoje (SLSS ID) k identifikaci typu synchronizačního zdroje.
- Založeno na Zadoff-Chuových sekvencích pro robustní detekci v prostředích s vysokou mobilitou a šumem.
- Vysílán ve fixním páru zdrojů s Primárním postranním synchronizačním signálem (PSSS).
- Podporuje více synchronizačních zdrojů včetně GNSS, eNB/gNB a dalších UE.
- Základní pro počáteční hledání buňky a získání časování rámce v komunikaci po postranním spoji.

## Související pojmy

- [PSSS – Primary Sidelink Synchronization Signal](/mobilnisite/slovnik/psss/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [SSSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssss/)
