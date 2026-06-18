---
slug: "pd2dss"
url: "/mobilnisite/slovnik/pd2dss/"
type: "slovnik"
title: "PD2DSS – Primary D2D Synchronization Signal"
date: 2018-01-01
abbr: "PD2DSS"
fullName: "Primary D2D Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pd2dss/"
summary: "Primární synchronizační signál pro komunikaci typu zařízení-zařízení (D2D) v LTE. Vysílá jej uživatelské zařízení (UE), aby umožnilo ostatním blízkým zařízením dosáhnout počáteční časové a frekvenční"
---

PD2DSS je primární synchronizační signál pro komunikaci typu zařízení-zařízení (Device-to-Device) v LTE, vysílaný uživatelským zařízením (UE), který umožňuje blízkým zařízením dosáhnout počáteční časové a frekvenční synchronizace pro přímé zjišťování a komunikaci.

## Popis

Primární [D2D](/mobilnisite/slovnik/d2d/) synchronizační signál (PD2DSS) je jedním ze dvou synchronizačních signálů definovaných pro postranní spojení (sidelink, [SL](/mobilnisite/slovnik/sl/)) v LTE, druhým je sekundární D2D synchronizační signál ([SD2DSS](/mobilnisite/slovnik/sd2dss/)). Je to základní signál fyzické vrstvy používaný pro komunikaci typu zařízení-zařízení (Device-to-Device), zejména v rámci služeb založených na blízkosti (Proximity Services, [ProSe](/mobilnisite/slovnik/prose/)). PD2DSS vysílá uživatelské zařízení (UE), které funguje jako synchronizační zdroj. Jeho hlavní funkcí je poskytnout počáteční hrubou časovou a frekvenční synchronizaci pro přijímající UE. To umožňuje zjišťujícím UE sladit své přijímače v čase a frekvenci s vysílajícím UE, což je nezbytný první krok před pokusem o dekódování jakýchkoli datových nebo řídicích kanálů, jako je přidružený kanál [PD2DSCH](/mobilnisite/slovnik/pd2dsch/).

Z hlediska architektury je PD2DSS navržen tak, aby byl robustní a snadno detekovatelný. Je založen na sekvenci Zadoff-Chu ([ZC](/mobilnisite/slovnik/zc/)), podobně jako primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)) používaný v downlinku pro buněčnou synchronizaci s eNodeB. Aby se však předešlo záměně a rušení, používají se pro D2D jiné kořenové indexy a délky sekvencí. PD2DSS se vysílá ve specifických podrámcích v rámci nakonfigurovaného fondu zdrojů pro synchronizační signály postranního spoje. Vysílající UE vysílá PD2DSS spolu s SD2DSS (který poskytuje dodatečné informace, jako je identita postranního spoje) a PD2DSCH v synchronizovaném bloku. Tato kombinace umožňuje přijímajícímu UE určit 504 jedinečných identit pro synchronizaci postranního spoje.

Operační postup zahrnuje skenování UE pro signály PD2DSS. Po detekci provede korelaci, aby zjistilo časový posun a odhadlo posun nosné frekvence. Jakmile je PD2DSS detekován a dosaženo hrubé synchronizace, UE pokračuje v detekci SD2DSS, aby identifikovalo konkrétní ID synchronizačního zdroje a dosáhlo jemnějšího časování. Nakonec dekóduje PD2DSCH, aby získalo hlavní informační blok postranního spoje (SL-MIB). PD2DSS je zásadní pro vytvoření společného časového referenčního bodu mezi skupinou UE, což umožňuje technologie jako relaying mezi UE a sítí a přímou komunikaci ve scénářích veřejné bezpečnosti, kde mohou zařízení vytvářet více-skokové řetězce, přičemž každý skok se znovu synchronizuje pomocí PD2DSS od partnerského zařízení.

## K čemu slouží

PD2DSS byl vytvořen k řešení problému počáteční synchronizace mezi uživatelskými zařízeními (UE) v nepřítomnosti buněčné sítě (eNodeB). V tradičním LTE se UE synchronizují s [PSS](/mobilnisite/slovnik/pss/)/SSS eNodeB. Pro přímou D2D komunikaci, zejména pro případy použití veřejné bezpečnosti, kde může být síťová infrastruktura poškozena nebo nedostupná, byl vyžadován alternativní synchronizační mechanismus. PD2DSS poskytuje tento synchronizační maják pocházející od UE.

Historický kontext souvisí s prací 3GPP Rel-12 na službách založených na blízkosti (ProSe). Klíčovým požadavkem byla podpora komunikace pro záchranné složky 'mimo síť'. PD2DSS spolu s SD2DSS tvoří pár D2D synchronizačních signálů, který napodobuje funkci PSS/SSS, ale pro rozhraní postranního spoje. Řeší omezení, kdy se zařízení nemohou koordinovat v čase a frekvenci, což by vedlo k neefektivní komunikaci náchylné ke kolizím. Tím, že umožňuje UE stát se synchronizačními referencemi, umožňuje vytváření samoorganizujících se sítí, rozšiřuje pokrytí a je to umožňující signál fyzické vrstvy pro všechny následné postupy D2D zjišťování a komunikace. Jeho návrh zajišťuje, že může být odlišen od downlinkových signálů, aby se zabránilo chybné synchronizaci.

## Klíčové vlastnosti

- Poskytuje počáteční časovou a frekvenční synchronizaci pro D2D komunikaci / komunikaci přes postranní spojení (sidelink).
- Je založen na sekvenci Zadoff-Chu, odlišné od downlinkového PSS, aby se předešlo záměně.
- Vysílá jej uživatelské zařízení (UE) fungující jako synchronizační zdroj (synchronizované s eNB, jiným UE nebo GNSS).
- Je součástí bloku synchronizačních signálů, který zahrnuje SD2DSS a PD2DSCH.
- Umožňuje identifikaci jedné z 504 jedinečných identit pro synchronizaci postranního spoje (v kombinaci s SD2DSS).
- Je zásadní pro scénáře mimo pokrytí, s částečným pokrytím a pro relaying mezi UE a sítí.

## Související pojmy

- [SD2DSS – Secondary D2D Synchronization Signal](/mobilnisite/slovnik/sd2dss/)
- [PD2DSCH – Physical D2D Synchronization Channel](/mobilnisite/slovnik/pd2dsch/)
- [D2D – Device-to-Device](/mobilnisite/slovnik/d2d/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.843** (Rel-12) — D2D Proximity Services Feasibility Study
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services

---

📖 **Anglický originál a plná specifikace:** [PD2DSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pd2dss/)
