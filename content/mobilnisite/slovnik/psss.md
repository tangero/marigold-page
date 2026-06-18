---
slug: "psss"
url: "/mobilnisite/slovnik/psss/"
type: "slovnik"
title: "PSSS – Primary Sidelink Synchronization Signal"
date: 2025-01-01
abbr: "PSSS"
fullName: "Primary Sidelink Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psss/"
summary: "Fyzický vrstvový signál používaný pro počáteční časovou a frekvenční synchronizaci v LTE a NR sidelink (device-to-device) komunikaci. Umožňuje uživatelským zařízením (UE) se vzájemně přímo detekovat a"
---

PSSS je synchronizační signál fyzické vrstvy používaný pro počáteční časovou a frekvenční synchronizaci mezi zařízeními v LTE a NR sidelink komunikaci, což umožňuje přímou detekci zařízení a synchronizaci.

## Popis

Primární sidelink synchronizační signál (PSSS) je základní signál fyzické vrstvy definovaný pro LTE sidelink rozhraní, zavedený ve 3GPP Release 12. Funguje na rozhraní PC5, což je přímý komunikační spoj mezi uživatelskými zařízeními (UE) bez průchodu síťovou infrastrukturou. PSSS společně se sekundárním sidelink synchronizačním signálem ([SSSS](/mobilnisite/slovnik/ssss/)) tvoří blok sidelink synchronizačních signálů. Jeho primární funkcí je poskytnout počáteční synchronizaci časování symbolů a nosné frekvence pro přijímající UE, které se snaží detekovat a dekódovat sidelink přenosy od vysílajícího UE. To je klíčové pro vytvoření společné časové reference v decentralizovaném, ad-hoc síťovém prostředí, kde zařízení nemusí mít společný síťový časový zdroj jako eNodeB.

Technicky je PSSS Zadoff-Chu sekvence vysílaná na specifických zdrojových prvcích v rámci subframu. Sekvence je charakterizována kořenovým indexem, který pomáhá rozlišit synchronizační zdroje. V LTE sidelink designu pro veřejnou bezpečnost a [V2X](/mobilnisite/slovnik/v2x/) jsou pro PSSS definovány dva specifické kořenové indexy, což umožňuje UE rozlišit mezi synchronizačními zdroji v dosahu pokrytí (synchronizovanými s eNodeB) a mimo dosah pokrytí (synchronizovanými s jiným UE nebo zdrojem [GNSS](/mobilnisite/slovnik/gnss/)). Detekce PSSS umožňuje přijímajícímu UE určit časování hranice sidelink subframu a provést hrubou korekci frekvenčního posunu. Tento proces je prvním krokem před dekódováním přidruženého SSSS a fyzického sidelink broadcast kanálu ([PSBCH](/mobilnisite/slovnik/psbch/)), který nese základní systémové informace, jako je šířka pásma sidelink systému a indikátor stavu pokrytí.

Role PSSS je ústřední pro hierarchii sidelink synchronizace. UE může být synchronizačním zdrojem, vysílajícím PSSS/SSSS, nebo synchronizačním cílem, který tyto signály vyhledává. Architektura podporuje vícenásobnou (multi-hop) synchronizaci, kde se UE může synchronizovat s jiným UE, které samo může být synchronizováno s eNodeB nebo globálním navigačním satelitním systémem (GNSS). To umožňuje spolehlivou přímou komunikaci ve scénářích s částečným nebo žádným síťovým pokrytím. Design signálu zajišťuje robustní detekci i v prostředích s vysokým Dopplerovským rozptylem, typických pro vozidlovou (V2X) komunikaci. Jeho specifikace jsou podrobně popsány v řadě 3GPP technických specifikací, především v sérii 36 pro LTE a odkazovány v 38.889 pro studie sidelink založené na NR, které popisují jeho generování, mapování na zdrojové elementy a přidružené procedury.

## K čemu slouží

PSSS byl vytvořen, aby umožnil přímou komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), což je základním kamenem pro 3GPP Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a později pro Cellular Vehicle-to-Everything (C2V) služby. Před jeho zavedením byla veškerá buněčná komunikace striktně síťově centrická a vyžadovala, aby UE komunikovala přes základnovou stanici (eNodeB), i když byla fyzicky blízko. Tato architektura byla pro místní komunikaci neefektivní, zaváděla latenci a zcela selhávala ve scénářích bez síťového pokrytí, jako jsou oblasti postižené katastrofami nebo odlehlé lokality. Motivací pro sidelink a jeho synchronizační signály, jako je PSSS, byly požadavky veřejné bezpečnosti a rostoucí potřeba [V2X](/mobilnisite/slovnik/v2x/) komunikace, kde přímé spoje s nízkou latencí a vysokou spolehlivostí mezi vozidly nebo mezi vozidly a chodci jsou klíčové pro bezpečnostní aplikace.

Vytvoření PSSS řešilo základní výzvu vytvoření společné časové a frekvenční reference v decentralizovaném, peer-to-peer rádiovém prostředí. Tradiční buněčné systémy spoléhají na downlink synchronizační signály ([PSS](/mobilnisite/slovnik/pss/)/SSS) vysílané pevnou infrastrukturní základnovou stanicí. Pro sidelink není zaručen žádný pevný vysílač. PSSS poskytuje standardizovanou metodu, aby se jakékoli UE mohlo stát synchronizačním zdrojem, což umožňuje jiným zařízením jej detekovat a sladit své přijímače. Tím se řeší problém počátečního přístupu a koexistence v dynamické topologii, kde zařízení mohou často vstupovat do komunikačního dosahu a opouštět jej. Umožnilo to komerční a veřejně-bezpečnostní nasazení LTE přímé komunikace, čímž vznikla alternativa v licencovaném spektru k ad-hoc technologiím jako Wi-Fi Direct.

## Klíčové vlastnosti

- Poskytuje počáteční synchronizaci časování symbolů pro sidelink přijímače
- Umožňuje hrubou korekci posunu nosné frekvence
- Používá Zadoff-Chu sekvence pro robustní detekční výkon
- Rozlišuje mezi synchronizačními zdroji v dosahu a mimo dosah pokrytí pomocí kořenových indexů
- Vysílán jako součást bloku sidelink synchronizačních signálů (SLSS)
- Základní pro stanovení časování sidelink subframu a rádiového framu

## Související pojmy

- [SSSS – Secondary Sidelink Synchronization Signal](/mobilnisite/slovnik/ssss/)
- [PSBCH – Physical Sidelink Broadcast Channel](/mobilnisite/slovnik/psbch/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PSSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/psss/)
