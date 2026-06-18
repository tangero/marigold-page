---
slug: "m-rnti"
url: "/mobilnisite/slovnik/m-rnti/"
type: "slovnik"
title: "M-RNTI – MBMS Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "M-RNTI"
fullName: "MBMS Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/m-rnti/"
summary: "Dočasný identifikátor používaný na LTE radiovém rozhraní pro adresování uživatelských zařízení (UE) při přenosech služby Multimedia Broadcast Multicast Service (MBMS). Umožňuje efektivní skupinové plá"
---

M-RNTI je dočasný identifikátor používaný na LTE radiovém rozhraní pro adresování uživatelských zařízení (UE) při přenosech MBMS, který umožňuje skupinové plánování a signalizaci řídicích zpráv pro broadcastový/multicastový provoz.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Radio Network Temporary Identifier (M-RNTI) je klíčový identifikátor vrstvy 1 a vrstvy 2 v architektuře LTE Radio Access Network ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) pro podporu služby Multimedia Broadcast Multicast Service (MBMS). Funguje na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) a používá jej eNodeB k adresování skupiny UE, která má zájem přijímat konkrétní službu MBMS. Na rozdíl od UE-specifického [C-RNTI](/mobilnisite/slovnik/c-rnti/) je M-RNTI společný identifikátor sdílený všemi UE v oblasti Multicast-Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)) naladěnými na danou službu. Technicky je M-RNTI 16bitová hodnota a její konkrétní bitová posloupnost je definována v technických specifikacích pro plánování související s MBMS. Když eNodeB potřebuje vysílat MBMS data na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), nejprve pošle na PDCCH zprávu Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)). Tato DCI je zakódována (scramblována) pomocí M-RNTI. UE monitorující PDCCH dekódují řídicí kanály pomocí různých hodnot [RNTI](/mobilnisite/slovnik/rnti/). Po úspěšném dekódování DCI zprávy, jejíž CRC je zakódováno M-RNTI, které je dané UE nakonfigurováno monitorovat, UE pozná, že následné přidělení zdrojů na PDSCH obsahuje MBMS data určená pro jeho skupinu. M-RNTI je úzce spojeno s logickými kanály MBMS (MCCH a MTCH). Systémová informace nebo MCCH informuje UE o tom, které M-RNTI odpovídá které službě MBMS (identifikované pomocí Temporary Mobile Group Identity, TMGI). Tento mechanismus umožňuje efektivní point-to-multipoint plánování bez nutnosti individuálního adresování, čímž šetří zdroje řídicího kanálu. Jeho role je zásadní pro přidělování zdrojů a procedury fyzické vrstvy, které umožňují škálovatelné doručování broadcastového a multicastového obsahu přes LTE.

## K čemu slouží

M-RNTI bylo zavedeno, aby vyřešilo problém efektivního řízení radiových zdrojů pro broadcastové a multicastové služby v LTE. Tradiční unicastová komunikace používá pro každé UE jedinečné C-RNTI, což je neefektivní pro doručování stejného obsahu stovkám nebo tisícům zařízení. Účelem M-RNTI je poskytnout jedinou, skupinově orientovanou adresu pro radiové rozhraní. To umožňuje eNodeB provést jedno plánovací přiřazení na PDCCH, které platí pro všechna UE přijímající službu MBMS, což dramaticky snižuje režii řídicího kanálu. Řeší tak klíčovou výzvu škálovatelné skupinové komunikace v celulárních sítích. Historicky existovaly dedikované mechanismy pro broadcast (jako Cell Broadcast Service), ale MBMS si kladlo za cíl poskytnout integrovanější a spektrálně efektivnější možnost multimediálního broadcastu. Vytvoření M-RNTI spolu s architekturou MBSFN bylo motivováno snahou podporovat služby jako mobilní TV, skupinovou komunikaci pro veřejnou bezpečnost a distribuci softwaru/aktualizací obrovskému počtu zařízení, aniž by se síť zahlcovala redundantními unicastovými toky. Umožňuje síti zacházet se skupinou účastníků jako s jedinou entitou pro účely přidělování downlinkových zdrojů.

## Klíčové vlastnosti

- 16bitový dočasný identifikátor radiové sítě používaný pro MBMS
- Společný identifikátor sdílený všemi UE přijímajícími konkrétní službu MBMS v oblasti MBSFN
- Používá se ke scramblování CRC zpráv DCI na PDCCH pro skupinové plánování
- Umožňuje efektivní point-to-multipoint přidělování zdrojů na PDSCH
- Spojeno s logickými kanály MBMS (MCCH a MTCH)
- Klíčová komponenta pro snížení režie řídicí signalizace při broadcastových/multicastových přenosech

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)

## Definující specifikace

- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [M-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-rnti/)
