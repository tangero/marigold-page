---
slug: "nzp"
url: "/mobilnisite/slovnik/nzp/"
type: "slovnik"
title: "NZP – Non-Zero Power CSI-RS"
date: 2025-01-01
abbr: "NZP"
fullName: "Non-Zero Power CSI-RS"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nzp/"
summary: "Typ referenčního signálu pro informace o stavu kanálu (CSI-RS) vysílaný s nenulovým výkonem, používaný pro měření a odhad kanálu v NR a LTE-Advanced. Umožňuje UE měřit kvalitu kanálu, charakteristiky"
---

NZP je typ referenčního signálu pro informace o stavu kanálu (CSI-RS) vysílaný s nenulovým výkonem, používaný pro měření a odhad kanálu za účelem umožnění reportování kvality, beamů a interference.

## Popis

Non-Zero Power [CSI-RS](/mobilnisite/slovnik/csi-rs/) (NZP CSI-RS) je downlinkový referenční signál v 5G NR (a vylepšený v LTE-Advanced od Rel-10) používaný pro získávání informací o stavu kanálu. Na rozdíl od své protějškové varianty Zero-Power CSI-RS ([ZP](/mobilnisite/slovnik/zp/) CSI-RS), která slouží jako utlumený zdroj pro měření interference, je NZP CSI-RS aktivně vysílán gNodeB. Skládá se ze specifických sekvencí mapovaných na předem určené zdrojové prvky v časově-frekvenční mřížce fyzického zdrojového bloku. UE měří přijatý výkon, fázi a kvalitu těchto známých referenčních symbolů, aby odhadlo downlinkový rádiový kanál mezi každým vysílacím anténním portem (nebo beamem) a každou ze svých přijímacích antén.

Z architektonického hlediska jsou zdroje NZP CSI-RS konfigurovány gNodeB prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), což poskytuje vysokou flexibilitu. Mezi parametry patří periodicita a offset v časové doméně, hustota a umístění ve frekvenční doméně, počet anténních portů (který může být 1, 2, 4, 8, 12, 16, 24 nebo 32) a scramblingová identita. Signál může být vysílán jako široký beam nebo, což je kritičtější, jako beamformovaný referenční signál, kdy je vysílán prostřednictvím specifického analogového beamu v daném období burstu SSB. To je zásadní pro procedury správy beamů, jako je beam sweeping, měření a reportování. UE používá tato měření k výpočtu klíčových metrik, jako je indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), indikátor předkódovací matice ([PMI](/mobilnisite/slovnik/pmi/)), indikátor hodnosti ([RI](/mobilnisite/slovnik/ri/)) a indikátor vrstvy ([LI](/mobilnisite/slovnik/li/)), které jsou zpětně hlášeny gNodeB v [CSI](/mobilnisite/slovnik/csi/) reportech.

Jeho role přesahuje základní odhad kvality kanálu. V systémech s massive MIMO a beamformingem je NZP CSI-RS primárním nástrojem pro doladění beamů. gNodeB může nakonfigurovat více sad zdrojů NZP CSI-RS pro měření UE, které odpovídají různým kandidátním beamům. UE reportuje nejsilnější beamy, což síti umožňuje vybrat optimální konfiguraci přenosu. Dále je NZP CSI-RS používán jako sledovací referenční signál (TRS) pro jemné časové a frekvenční sledování a pro měření mobility (nahrazující nebo doplňující CRS v NR). Je také klíčový v operacích s více TRP (Transmission Reception Point) a koordinovaným multipointem (CoMP), kde UE měří NZP CSI-RS z více geograficky oddělených bodů, což umožňuje sdružený přenos nebo dynamický výběr bodu.

## K čemu slouží

NZP CSI-RS byl vyvinut, aby poskytoval flexibilní, efektivní a škálovatelný mechanismus pro odhad downlinkového kanálu v pokročilých anténních systémech. V raném LTE (Rel-8/9) byl pro demodulaci i měření kanálu používán společný referenční signál (CRS). CRS však byl vždy vysílán v celém přenosovém pásmu a ze všech anténních portů, což způsobovalo významnou režii a omezovalo flexibilitu beamformingu, protože byl specifický pro buňku. Přechod k dedikovaným, UE-specifickým referenčním signálům pro demodulaci (DM-RS) vytvořil potřebu samostatného, konfigurovatelného referenčního signálu čistě pro sondování kanálu.

Zavedení CSI-RS v LTE Rel-10, s jeho variantou Non-Zero Power, tyto limity odstranilo. Umožnilo řídké, konfigurovatelné vysílání v čase a frekvenci, což drasticky snížilo režii. Co je důležitější, bylo odděleno od identity buňky a mohlo být předkódováno, což umožnilo měření kanálu specifického pro beam. To bylo zásadní pro adopci uzavřené smyčky prostorového multiplexování a multi-user MIMO. Primární problém, který řešil, byl přesný odhad vícerozměrného MIMO kanálu bez neúnosné režie referenčních signálů, což byl požadavek, který se stal ještě kritičtějším s massive MIMO systémy plánovanými pro 5G NR.

V 5G NR byl účel NZP CSI-RS rozšířen a upřesněn. NR opustilo vždy zapnutý CRS, čímž se CSI-RS stalo jediným referenčním signálem pro měření kanálu. Jeho návrh byl optimalizován pro velmi velké anténní soustavy (až 32 portů explicitně definovaných, s podporou pro více), široká přenosová pásma a flexibilní numerologii. Bylo těsně integrováno s beam-centric designem NR a slouží jako klíčový signál fyzické vrstvy pro správu beamů, což je zásadní pro provoz ve vysokofrekvenčních mmWave pásmech. NZP CSI-RS se tak vyvinulo z nástroje pro zpětnou vazbu kanálu v ústřední komponentu pro získávání, sledování a doladění beamů, čímž řeší výzvu správy směrových spojů v mobilním prostředí.

## Klíčové vlastnosti

- Flexibilní konfigurace periody, šířky pásma, hustoty a anténních portů prostřednictvím RRC
- Podpora až 32 anténních portů pro odhad kanálu v massive MIMO
- Může být beamformován a použit pro procedury správy beamů (např. beam sweeping, reportování)
- Používá se pro odvození CSI reportů (CQI, PMI, RI, LI)
- Funguje jako sledovací referenční signál (TRS) pro jemné časové/frekvenční sledování
- Umožňuje měření pro mobilitu (např. L1-RSRP) a scénáře s více TRP/CoMP

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [TRS – Total Radiated Sensitivity](/mobilnisite/slovnik/trs/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [NZP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nzp/)
