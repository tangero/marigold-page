---
slug: "sor-af"
url: "/mobilnisite/slovnik/sor-af/"
type: "slovnik"
title: "SOR-AF – Steering Of Roaming Application Function"
date: 2025-01-01
abbr: "SOR-AF"
fullName: "Steering Of Roaming Application Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sor-af/"
summary: "SOR-AF je síťová funkce v rámci architektury založené na službách (SBA) 5G, která poskytuje informace pro přesměrování roamingu (Steering of Roaming) do UDM. Umožňuje mobilním operátorům ovlivnit, kte"
---

SOR-AF je funkce 5G sítě, která poskytuje informace pro přesměrování roamingu (Steering of Roaming) a umožňuje operátorům ovlivnit, kterou síť si zařízení roamujícího účastníka vybere.

## Popis

Funkce SOR-AF (Steering of Roaming Application Function) je standardizovaná síťová funkce zavedená ve specifikaci 3GPP Release 16 jako součást architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G jádra. Funguje jako poskytovatel služeb [NEF](/mobilnisite/slovnik/nef/) (Network Exposure Function) nebo může mít přímé rozhraní založené na službách s funkcí [UDM](/mobilnisite/slovnik/udm/) (Unified Data Management). Primární rolí SOR-AF je generovat a dodávat informace pro přesměrování roamingu ([SOR](/mobilnisite/slovnik/sor/)), které zahrnují seznamy preferovaných veřejných pozemních mobilních sítí ([PLMN](/mobilnisite/slovnik/plmn/)) pro účastníka. Tyto informace jsou bezpečně přeneseny a uloženy v UDM.

Z architektonického hlediska SOR-AF komunikuje s UDM prostřednictvím rozhraní založeného na službách Nudm, konkrétně využívá službu Nudm_SDM (Subscription Data Management). Pokud je potřeba data pro přesměrování roamingu účastníka zřídit nebo aktualizovat, SOR-AF vyvolá na UDM servisní operaci Nudm_SDM_Update. UDM pak tyto SOR informace uloží jako součást profilu účastníka. SOR data jsou strukturována tak, aby obsahovala transparentní data (určená pro UE) a případně zabezpečený paket, který je pro UE šifrovaný a chráněný integritou pomocí klíčů odvozených od autentizačních údajů účastníka.

Když se uživatelské zařízení (UE) registruje ve navštívené síti, UDM zahrne relevantní SOR informace do dat předplatného odeslaných funkci [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) během registrační procedury. AMF následně tyto SOR informace přepošle UE prostřednictvím signalizace [NAS](/mobilnisite/slovnik/nas/). Po přijetí SOR dat je UE vyhodnotí, typicky když je v režimu nečinnosti, a může zahájit proceduru výběru PLMN, aby se připojilo k síti ze seznamu preferovaných sítí poskytnutého domovským operátorem. Tento mechanismus umožňuje domovskému operátorovi dynamicky přesměrovávat roamující účastníky na partnerské sítě s lepšími komerčními dohodami nebo kvalitou služeb, aniž by to vyžadovalo manuální zásah na UE.

## K čemu slouží

SOR-AF byla vytvořena, aby poskytla standardizovanou, bezpečnou a dynamickou metodu pro domovské síťové operátory k přesměrování jejich odchozích roamujících účastníků na preferované partnerské sítě. Před její standardizací bylo přesměrování roamingu často implementováno proprietárními, nestandardizovanými prostředky, jako jsou aktualizace přes vzduch ([OTA](/mobilnisite/slovnik/ota/)) prostřednictvím SIM karty nebo aplikací v zařízení, které mohly být méně bezpečné, méně spolehlivé a neintegrované se systémy pro poskytování služeb v jádru sítě. Absence síťového standardu ztěžovala zajištění včasných aktualizací a konzistentní uplatňování politik přesměrování napříč všemi zařízeními účastníků.

Motivace vychází z komerční a technické potřeby operátorů efektivně spravovat roamingový provoz. Tím, že operátor přesměruje účastníky na konkrétní navštívené veřejné pozemní mobilní sítě (VPLMN), může ovládat náklady na základě roamingových dohod, zlepšit uživatelský komfort účastníka směrováním na sítě s lepším pokrytím nebo možnostmi služeb a vyrovnávat zatížení mezi více roamingovými partnery. Integrace do architektury SBA 5G umožňuje automatizované, na politikách založené přesměrování, které je součástí základního profilu účastníka, a nabízí tak sofistikovanější správu provozu v reálném čase ve srovnání se staršími metodami.

## Klíčové vlastnosti

- Standardizované rozhraní založené na službách (Nudm) pro integraci s UDM v 5G jádru.
- Generuje zabezpečené informace pro přesměrování roamingu (SOR) obsahující seznamy preferovaných PLMN.
- Podporuje jak transparentní data pro UE, tak zabezpečený paket pro ochranu integrity.
- Umožňuje dynamickou aktualizaci roamingových preferencí bez nutnosti rekonfigurace UE.
- Integruje se s bezpečnostní autentizací účastníka pro chráněnou komunikaci k UE.
- Usnadňuje optimalizovaný roaming na základě komerčních dohod a stavu sítě.

## Související pojmy

- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 29.544** (Rel-19) — Nspaf Service Based Interface (SP-AF) Stage 3
- **TS 29.550** (Rel-19) — 5G Steering of Roaming Service Based Interface

---

📖 **Anglický originál a plná specifikace:** [SOR-AF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sor-af/)
