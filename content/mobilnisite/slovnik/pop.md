---
slug: "pop"
url: "/mobilnisite/slovnik/pop/"
type: "slovnik"
title: "POP – Participating Operator"
date: 2026-01-01
abbr: "POP"
fullName: "Participating Operator"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pop/"
summary: "Operátor, který se účastní služby více operátorů, dohody o sdílení sítě nebo federace. Je klíčovou entitou ve specifikacích správy a účtování 3GPP pro definici rolí, odpovědností a zúčtování mezi part"
---

POP (účastnický operátor) je operátor účastnící se služby více operátorů, dohody o sdílení sítě nebo federace, který definuje role a umožňuje zúčtování mezi partnerskými operátory ve specifikacích 3GPP.

## Popis

Účastnický operátor (POP) je základní obchodní a provozní role definovaná v rámci rámců správy a účtování 3GPP. Odkazuje na operátora telekomunikační sítě, který se aktivně podílí na společné nabídce služeb, dohodě o sdílení sítě nebo federaci s jedním či více dalšími operátory. POP není jen pasivním partnerem, ale entitou s definovanými právy, povinnostmi a rozhraními v ekosystému více operátorů. Tento koncept je klíčový pro scénáře, jako je roamování, hostitelství mobilního virtuálního operátora sítě ([MVNO](/mobilnisite/slovnik/mvno/)), federace služeb (např. pro IoT nebo 5G slicing napříč operátory) a různé formy sdílení infrastruktury včetně MORAN (Multi-Operator Radio Access Network) a [MOCN](/mobilnisite/slovnik/mocn/) (Multi-Operator Core Network).

V rámci architektury 3GPP je POP reprezentován v systémech správy (např. správa sítě, správa prvků) a účtovacích systémech. Specifikace jako TS 28.541 (5G Management) a TS 32.130 (Charging) podrobně popisují, jak je POP identifikován, ověřován a autorizován. Každý POP má v kontextu dohody jedinečný identifikátor. Rozhraní správy umožňují POP zobrazovat a spravovat svůj podíl na zdrojích, přijímat výkonnostní reporty a být informován o poruchách ovlivňujících jeho služby. V účtování je POP ústřední entitou v procesech zúčtování; generují se podrobné účtovací záznamy pro sledování využití zdrojů připadajících na každého POP, což umožňuje přesné fakturace a sdílení výnosů mezi partnery.

Technická implementace zahrnuje specifické referenční body a informační modely. Například ve scénáři síťového slicingu napříč více operátory by každý operátor vystupující jako POP vystavil subdoménu správy sliců. Koordinační entita (kterou může být jeden z POP nebo třetí strana) používá standardizovaná rozhraní ke složení end-to-end slicu z prostředků každého POP. Bezpečnostní specifikace (např. TS 33.310) definují, jak se mezi POP vytváří důvěra, často s využitím federativního rámce, kde kořenová certifikační autorita vydává certifikáty každému účastnickému operátorovi.

## K čemu slouží

Koncept účastnického operátora byl formalizován, aby podpořil složitá obchodní a technická partnerství vyžadovaná v moderní telekomunikaci. Jak se služby vyvíjely za hranice jednoduchého bilaterálního roamingu, operátoři začali vstupovat do hlubokého sdílení sítí za účelem snížení nákladů na nasazení a do federací služeb, aby nabídli bezproblémová mezihraniční řešení pro IoT nebo podniky. Tyto spolupráce vyžadovaly jasnou, standardizovanou definici role každého operátora, aby umožnily automatizované poskytování, správu a zúčtování.

Před touto formalizací se uspořádání více operátorů často řešila pomocí vlastních bilaterálních dohod a manuálních procesů, které nebyly škálovatelné. Model POP to řeší tím, že poskytuje standardizovaného 'aktéra' v rámci systémové architektury 3GPP. To umožňuje automatizaci klíčových procesů: POP může být automaticky udělen přístup do systému správy pro monitorování jeho slicu, záznamy o účtovacích datech mohou být automaticky označeny správným identifikátorem POP pro zúčtování a bezpečnostní přihlašovací údaje mohou být automaticky ověřeny. Tato standardizace snižuje bariéru pro vytváření partnerství, urychluje nasazení služeb a snižuje provozní náklady, což je zásadní pro úspěch 5G síťového slicingu a rozsáhlých nasazení IoT, která ze své podstaty překračují hranice operátorů.

## Klíčové vlastnosti

- Definuje roli operátora v dohodách a federacích více operátorů
- Má jedinečný identifikátor v systémech správy a účtování
- Umožňuje automatizované poskytování zdrojů a správu služeb napříč operátory
- Je klíčový pro zúčtování mezi operátory a sdílení výnosů
- Integruje se s bezpečnostními rámci 3GPP pro federovanou důvěru
- Podporuje různé modely, jako je sdílení sítě, roamování a federace sliců

## Související pojmy

- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)

## Definující specifikace

- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TR 28.813** (Rel-17) — Study on New Energy Efficiency Aspects for 5G
- **TR 28.825** (Rel-17) — 5G Network Sharing Management Study
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management

---

📖 **Anglický originál a plná specifikace:** [POP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pop/)
