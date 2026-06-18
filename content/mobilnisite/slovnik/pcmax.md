---
slug: "pcmax"
url: "/mobilnisite/slovnik/pcmax/"
type: "slovnik"
title: "PCMAX – Configured Maximum UE Output Power"
date: 2025-01-01
abbr: "PCMAX"
fullName: "Configured Maximum UE Output Power"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pcmax/"
summary: "Maximální úroveň vysílacího výkonu, kterou je User Equipment (UE) oprávněno nebo nakonfigurováno použít na konkrétní nosné nebo v pásmu. Jde o klíčový parametr pro řízení výkonu v uplinku, zajišťující"
---

PCMAX je konfigurovaná maximální úroveň vysílacího výkonu, kterou je User Equipment oprávněno použít na konkrétní nosné nebo v pásmu. Je klíčový pro řízení výkonu v uplinku, splnění regulatorních požadavků, prevenci rušení a správu výkonu.

## Popis

PCMAX je základní parametr ve vysílacím řetězci UE pro uplink, definovaný v 3GPP specifikacích pro NR (New Radio) a vyvinutý pro LTE na nosnou a pásmo. Představuje horní limit pro konfigurovaný výstupní výkon UE. Skutečná hodnota PCMAX není jediné pevné číslo, ale je určena kombinací regulatorních požadavků, konfigurace sítě a vlastních schopností UE. Funguje v definovaném rozsahu od PCMAX_L do PCMAX_H, kde PCMAX_L je dolní mez a PCMAX_H horní mez. Konečně nakonfigurovaný PCMAX musí spadat do tohoto rozsahu.

Stanovení PCMAX zahrnuje několik vstupů. Za prvé, regulatorní limity definují absolutní maximální povolený výkon v konkrétním frekvenčním pásmu, aby se zabránilo škodlivému rušení. Za druhé, síť (gNB v NR, [eNB](/mobilnisite/slovnik/enb/) v LTE) může UE signalizovat parametr maximálního povoleného výkonu prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), jako je informační element P-Max v [SIB1](/mobilnisite/slovnik/sib1/) (System Information Block 1) nebo v dedikované konfiguraci. Za třetí, UE má svou vlastní schopnost definovanou třídou výkonu (např. Třída výkonu 3 pro mnoho handsets, definující nominální maximální výkon jako 23 dBm). UE vypočítá přípustný rozsah PCMAX (PCMAX_L, PCMAX_H) na základě těchto vstupů, aplikuje vzorce definované ve specifikacích jako TS 38.101-1 pro NR, které zohledňují maximální redukci výkonu ([MPR](/mobilnisite/slovnik/mpr/)) a dodatečnou maximální redukci výkonu ([A-MPR](/mobilnisite/slovnik/a-mpr/)), potřebné kvůli faktorům jako modulace vyššího řádu, přenos v široké šířce pásma nebo specifické regionální regulatorní požadavky.

Během provozu algoritmus řízení výkonu v uplinku UE používá PCMAX jako pevný strop. Algoritmus vypočítá požadovaný vysílací výkon na základě měření útlumu na trase, cílového přijímaného výkonu v základnové stanici, modulačního a kódovacího schématu ([MCS](/mobilnisite/slovnik/mcs/)) a počtu přidělených bloků zdrojů. Konečný vysílací výkon P je nastaven jako minimum z vypočítaného požadovaného výkonu a PCMAX. Tím je zajištěno, že UE nikdy nepřekročí svůj konfigurovaný maximum. Role PCMAX je klíčová pro správu rušivého prostředí v uplinku v buňce. Vhodným konfigurováním PCMAX může síť řídit poloměr pokrytí v uplinku a spravovat rušení sousedním buňkám, zejména v hustých nasazeních nebo na okrajích buněk.

Dále je PCMAX zásadní pro správu výkonu a tepelné řešení UE. Vysílání na vysoký výkon rychle vybíjí baterii a generuje teplo. Síť může snížit konfigurovaný PCMAX pro UE blízko středu buňky, což jim umožní šetřit výkon bez dopadu na kvalitu spojení. Hraje také klíčovou roli ve scénářích agregace nosných ([CA](/mobilnisite/slovnik/ca/)) a duální konektivity ([DC](/mobilnisite/slovnik/dc/)). UE má celkový limit výkonu napříč všemi vysílacími řetězci. Proto je PCMAX definován pro každou komponentní nosnou (CC) a UE musí provádět sdílení výkonu, aby byl zajištěn součet výkonů napříč aktivními CC nepřekročil celkovou kapacitu výkonu UE, přičemž výkon každé CC je omezen jejím odpovídajícím PCMAX. Tato složitá správa výkonu je podrobně specifikována v TS 38.101 a testovací postupy v TS 38.521.

## K čemu slouží

PCMAX existuje k řešení několika vzájemně souvisejících problémů v návrhu uplinku v celulárních sítích: regulatorní shoda, správa rušení, energetická účinnost UE a optimalizace výkonu sítě. Bez dobře definovaného a konfigurovatelného limitu maximálního výkonu by UE mohly vysílat na svém absolutním hardwarovém maximu, což by mohlo porušit regulatorní masky spektrálních emisí, způsobit nadměrné rušení jiným uživatelům ve stejném nebo sousedním pásmu a vytvořit nerovnoměrné rušivé prostředí v uplinku, které je pro síť obtížně říditelné.

Historicky se řízení výkonu zaměřovalo na to, aby UE vysílala právě takovým výkonem, aby na základnové stanici dosáhlo cíle kvality, ale jednoduchý hardwarový strop byl nedostačující. Zavedení složitějších přenosových schémat s proměnnou šířkou pásma a modulacemi vyššího řádu (jako 256QAM v LTE a 1024QAM v NR) znamenalo, že výkonový zesilovač UE musel pracovat s vyšší linearitou, což často vyžadovalo snížení maximálního výstupního výkonu, aby se předešlo spektrálnímu nárůstu a emisím mimo pásmo. To je zachyceno koncepty MPR/A-MPR spojenými s PCMAX. Dále, jak se sítě vyvíjely k využívání agregace nosných a více technologií radiového přístupu současně, se konfigurovatelné maximum na nosnou stalo nezbytným pro správu celkového vyzařovaného výkonu UE napříč všemi aktivními vysílači.

Jeho vytvoření a formalizace ve specifikacích 3GPP, zejména od Rel-15 dále pro NR, bylo motivováno potřebou flexibilního a přesného rámce. Tento rámec umožňuje síti inteligentně řídit výkonovou obálku UE v uplinku. Síť může nastavit PCMAX na základě scénářů nasazení (např. nižší v small cells), polohy UE, vytížení sítě a podmínek rušení. To umožňuje optimalizovanou kapacitu systému a pokrytí, přičemž je zajištěno, že UE pracují v bezpečných tepelných a bateriových limitech. Poskytuje potřebný nástroj pro síťové operátory k vyvážení mezi dosažením vysokých přenosových rychlostí v uplinku pro uživatele na okraji buňky a zachováním celkové stability a efektivity sítě.

## Klíčové vlastnosti

- Definuje horní limit pro vysílací výkon UE na konkrétní nosné nebo v pásmu.
- Stanovuje se jako rozsah (PCMAX_L až PCMAX_H) zohledňující regulatorní limity, konfiguraci sítě (P-Max) a třídu výkonu UE.
- Zahrnuje Maximální Redukci Výkonu (MPR) a Dodatečnou MPR (A-MPR) pro signály s vysokým poměrem špičkového a průměrného výkonu (PAPR).
- Slouží jako konečné omezení ve výpočtu řízení výkonu v uplinku (P = min(vypočítaný výkon, PCMAX)).
- Zásadní pro správu rušení v uplinku a pokrytí buňky v síti.
- Klíčový pro sdílení a správu výkonu UE ve scénářích Agregace Nosných (CA) a Duální Konektivity (DC).

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.793** (Rel-19) — Simultaneous Rx/Tx Band Combinations TR
- **TS 38.887** (Rel-16) — NR Band n259 Specification (39.5-43.5 GHz)

---

📖 **Anglický originál a plná specifikace:** [PCMAX na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcmax/)
