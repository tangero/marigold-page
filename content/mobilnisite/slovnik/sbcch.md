---
slug: "sbcch"
url: "/mobilnisite/slovnik/sbcch/"
type: "slovnik"
title: "SBCCH – Sidelink Broadcast Control Channel"
date: 2025-01-01
abbr: "SBCCH"
fullName: "Sidelink Broadcast Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbcch/"
summary: "SBCCH je logický kanál v LTE a NR postranní (sidelink) komunikaci mezi zařízeními (device-to-device) používaný k vysílání systémových informací a řídicích zpráv přímo mezi uživatelskými zařízeními bez"
---

SBCCH je postranní (sidelink) vysílací řídicí kanál používaný v LTE a NR komunikaci mezi zařízeními (device-to-device) k vysílání systémových informací a řídicích zpráv přímo mezi uživatelskými zařízeními bez síťové infrastruktury.

## Popis

Sidelink Broadcast Control Channel (SBCCH) je logický kanál definovaný ve specifikacích rozhraní postranního spoje (PC5) 3GPP pro LTE (počínaje Rel-12) a NR. Funguje v řídicí rovině komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)) nebo komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)). Jako vysílací kanál je jeho hlavní funkcí přenášet základní systémové informace z vysílajícího UE k jednomu nebo více přijímajícím UE v jeho blízkosti. Tyto informace jsou klíčové pro to, aby si UE mohla vzájemně detekovat, synchronizovat se a správně interpretovat zdroje a parametry používané pro následnou postranní komunikaci. SBCCH je mapován na přenosový kanál Sidelink Broadcast Channel ([SL-BCH](/mobilnisite/slovnik/sl-bch/)), který je následně mapován na konkrétní fyzické zdroje (např. [PSSCH](/mobilnisite/slovnik/pssch/) v NR).

Obsah vysílaný na SBCCH je znám jako Sidelink Master Information Block (SL-MIB) a Sidelink System Information Blocks (SL-SIBs). Tyto informace zahrnují parametry jako přímé číslo rámce, šířku pásma systému, konfiguraci fondů zdrojů pro postranní spoj, synchronizační reference a informace o schopnostech vysílajícího UE nebo dostupnosti služeb. UE, která má sloužit jako synchronizační zdroj nebo poskytovat služby prostřednictvím postranního spoje, bude tyto zprávy SBCCH periodicky vysílat. Sousední UE monitorují přenosy SBCCH, aby získaly nezbytnou konfiguraci pro účast v síti postranního spoje, provedly výběr zdrojů a navázaly komunikaci.

Z architektonického hlediska je SBCCH klíčovou součástí protokolového zásobníku postranního spoje, který sídlí ve vrstvě Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) v transparentním režimu a ve vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Umožňuje decentralizovaný provoz sítě, což je zásadní pro scénáře, kde je pokrytí mobilní sítě nepřítomné, nespolehlivé nebo přetížené. Například v komunikacích pro veřejnou bezpečnost mohou první respondenti použít SBCCH k vytvoření přímých komunikačních skupin. V NR V2X podporuje SBCCH pokročilé případy užití, jako je formování vozových kolon a sdílení senzorů, tím, že zajišťuje společnou představu všech vozidel ve skupině o rádiových zdrojích a časování, což usnadňuje spolehlivou a nízkolatenční přímou komunikaci.

## K čemu slouží

SBCCH byl vytvořen, aby řešil základní výzvu organizace přímé komunikace mezi zařízeními standardizovaným a efektivním způsobem. Před jeho zavedením ve verzi 12 (pro LTE [D2D](/mobilnisite/slovnik/d2d/) [ProSe](/mobilnisite/slovnik/prose/)) přímé komunikaci mezi zařízeními chyběl standardizovaný řídicí mechanismus pro koordinaci zdrojů a šíření systémových informací vysílacím způsobem. Raná proprietární řešení D2D nebo ad-hoc sítě často trpěly kolizemi, neefektivním využitím zdrojů a dlouhou dobou navazování spojení. SBCCH poskytuje strukturovaný, na síti nezávislý způsob, jak mohou UE oznamovat svou přítomnost a 'pravidla zapojení' pro postranní spoj, což umožňuje škálovatelné a interoperabilní služby založené na blízkosti.

Hnací silou za SBCCH byla potřeba spolehlivé přímé komunikace pro veřejnou bezpečnost a komerční služby založené na blízkosti. Orgány veřejné bezpečnosti potřebovaly, aby zařízení mohla komunikovat přímo při výpadcích sítě. Vytvoření SBCCH spolu s širším rámcem postranního spoje umožnilo UE samoorganizovat se vysíláním kritických řídicích informací, což umožnilo detekci, synchronizaci a přidělování zdrojů bez centrální síťové koordinace. Tato schopnost byla později rozšířena a vylepšena pro vozovou komunikaci (V2X) ve verzích 14 a vyšších, kde je nízkolatenční vysílání řídicích informací klíčové pro bezpečnostní zprávy a kooperativní manévry při jízdě.

## Klíčové vlastnosti

- Vysílá systémové informace postranního spoje (SL-MIB/SL-SIBs) pro D2D/V2X
- Umožňuje synchronizaci UE a konfiguraci fondů zdrojů v postranním spoji
- Funguje bez síťové infrastruktury (nezávisle na pokrytí)
- Mapován na přenosový kanál SL-BCH v protokolovém zásobníku postranního spoje
- Podporuje jak LTE postranní spoj (PC5), tak NR postranní spoj
- Nezbytný pro veřejnou bezpečnost, detekci zařízení a skupinovou komunikaci V2X

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [SL-BCH – Sidelink Broadcast Channel](/mobilnisite/slovnik/sl-bch/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [SBCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbcch/)
