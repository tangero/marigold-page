---
slug: "pscch"
url: "/mobilnisite/slovnik/pscch/"
type: "slovnik"
title: "PSCCH – Physical Sidelink Control Channel"
date: 2025-01-01
abbr: "PSCCH"
fullName: "Physical Sidelink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pscch/"
summary: "Fyzický kanál v postranním spoji LTE a NR, který vysílající UE používá k zasílání řídicích informací nezbytných pro příjem přidruženého datového kanálu (PSSCH). Nese plánovací přiřazení včetně přiděle"
---

PSCCH je fyzický kanál v postranním spoji LTE a NR, na kterém vysílající UE zasílá řídicí informace, jako jsou plánovací přiřazení, nezbytné pro příjem přidruženého datového kanálu (PSSCH).

## Popis

Physical Sidelink Control Channel (PSCCH) je klíčový řídicí kanál v postranním spoji ([SL](/mobilnisite/slovnik/sl/)) rozhraní 3GPP, který pracuje na fyzické vrstvě. Jeho hlavní funkcí je přenášet Sidelink Control Information ([SCI](/mobilnisite/slovnik/sci/)), konkrétně plánovací přiřazení ([SA](/mobilnisite/slovnik/sa/)), z vysílajícího uživatelského zařízení (UE) k jednomu nebo více přijímajícím UE. SCI přenášené na PSCCH poskytuje nezbytné dekódovací informace pro přidružený datový přenos na Physical Sidelink Shared Channel ([PSSCH](/mobilnisite/slovnik/pssch/)). Tyto informace zahrnují detailní přidělení zdrojů (časových a frekvenčních) pro PSSCH, schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)), skupinové cílové ID, informace o časovém předstihu a další parametry související s procesem [HARQ](/mobilnisite/slovnik/harq/) a opakovanými přenosy.

Z architektonického hlediska jsou PSCCH a PSSCH v rámci podrámce nebo slotu postranního spoje těsně propojeny časovým dělením. V postranním spoji LTE (Režim 3 a Režim 4) PSCCH typicky zabírá první symboly podrámce, po nichž následuje PSSCH ve zbývajících symbolech stejného podrámce. Vysílající UE vybírá zdroje pro PSCCH (a tím implicitně i pro přidružený PSSCH) buď na základě povolení od sítě (Režim 3), nebo prostřednictvím distribuovaného algoritmu autonomního výběru založeného na snímání (Režim 4). Samotný PSCCH je vysílán pomocí specifického vzoru demodulačního referenčního signálu ([DM-RS](/mobilnisite/slovnik/dm-rs/)), aby přijímající UE mohlo provést odhad kanálu pro koherentní demodulaci.

V postranním spoji NR (zavedeném ve verzi 16) je návrh PSCCH flexibilnější, aby vyhověl širokému spektru numerologií, šířek pásma a případů použití (např. [V2X](/mobilnisite/slovnik/v2x/), veřejná bezpečnost, komerční D2D). Postranní spoj NR definuje dvě fáze SCI: SCI Formát 0-1, který je přenášen na PSCCH, a SCI Formát 0-2, který může být přenášen přímo na PSSCH. SCI první fáze na PSCCH obsahuje informace, které UE bezpodmínečně potřebuje, aby vědělo, zda se má pokusit dekódovat PSSCH (např. priorita, rezervace zdrojů, přiřazení frekvenčních zdrojů). Podrobné MCS, HARQ informace a ID zdroje/cíle jsou pak přenášeny ve SCI druhé fáze na PSSCH. Tento dvoufázový přístup zlepšuje efektivitu a flexibilitu. PSCCH v NR může být konfigurován v rámci vyhrazených fondů zdrojů a jeho vysílání může být založeno na výsledcích snímání (podobně jako v LTE Režim 4) nebo na síťovém plánování (Režim 1).

## K čemu slouží

PSCCH byl zaveden, aby umožnil plánovanou a efektivní přímou komunikaci mezi zařízeními v postranním spoji. Bez vyhrazeného řídicího kanálu by byla komunikace postranním spojem chaotická a neefektivní. Zařízení by neměla způsob, jak oznamovat svá nadcházející datová vysílání nebo popisovat, jak by tato data měla být přijímána. PSCCH tento problém řeší tím, že poskytuje strukturovaný mechanismus signalizace v pásmu, který umožňuje vysílajícímu UE informovat blízká UE o parametrech svého následujícího datového přenosu.

Jeho vytvoření bylo motivováno potřebou spolehlivé, škálovatelné a rušení řízené komunikace zařízení-zařízení. V raných ad-hoc komunikačních schématech (jako některá předstandardní řešení V2X nebo veřejné bezpečnosti) byly řídicí informace buď přenášeny spolu s daty, nebo odesílány naslepo, což vedlo k vysoké pravděpodobnosti kolizí a špatnému využití zdrojů. PSCCH, zejména v kombinaci s procedurami snímání (jako v LTE Režim 4 a NR Režim 2), umožňuje UE naslouchat kanálu před vysíláním, vybírat zdroje, které jsou pravděpodobně volné, a oznamovat jejich využití ostatním. To dramaticky snižuje rušení a umožňuje předvídatelnou latenci – což je klíčové pro bezpečnostní zprávy V2X a komunikaci veřejné bezpečnosti. Je to mechanismus, který mění prostý broadcast na řízený přímý spoj s kontrolou zdrojů.

## Klíčové vlastnosti

- Přenáší Sidelink Control Information (SCI) / Plánovací přiřazení
- Označuje časově-frekvenční zdroje pro přidružený PSSCH
- Komunikuje schéma modulace a kódování (MCS) pro dekódování dat
- Podporuje skupinové (groupcast) a všesměrové (broadcast) adresování cílů
- Integruje se s autonomním výběrem zdrojů založeným na snímání (Režim 2/4)
- Umožňuje koordinaci HARQ zpětné vazby pro skupinový přenos (groupcast)

## Související pojmy

- [PSSCH – Physical Sidelink Shared Channel](/mobilnisite/slovnik/pssch/)
- [PSBCH – Physical Sidelink Broadcast Channel](/mobilnisite/slovnik/psbch/)
- [SCI – Subscriber Controlled Input / Send Charging Information](/mobilnisite/slovnik/sci/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.785** (Rel-14) — LTE Sidelink V2V Services Study
- **TS 36.786** (Rel-14) — TR on V2X Services based on LTE sidelink
- **TS 36.787** (Rel-15) — V2X New Band Combinations for LTE
- **TS 36.788** (Rel-15) — V2X Phase 2 Technical Report for LTE
- **TS 36.877** (Rel-12) — LTE Device to Device Proximity Services
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pscch/)
