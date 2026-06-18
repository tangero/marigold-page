---
slug: "uas"
url: "/mobilnisite/slovnik/uas/"
type: "slovnik"
title: "UAS – NF Uncrewed Aerial System Network Function"
date: 2026-01-01
abbr: "UAS"
fullName: "NF Uncrewed Aerial System Network Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uas/"
summary: "Síťová funkce 3GPP, která poskytuje vystavení schopností služeb, autorizaci a správu provozu pro bezpilotní systémy (drony). Umožňuje zabezpečené, řízené a spolehlivé mobilní připojení pro provoz dron"
---

UAS je síťová funkce 3GPP, která poskytuje vystavení služeb, autorizaci a správu provozu, aby umožnila zabezpečené mobilní připojení pro bezpilotní systémy (drony).

## Popis

[NF](/mobilnisite/slovnik/nf/) Uncrewed Aerial System Network Function (UAS NF) je prvek základní sítě zavedený 3GPP pro podporu bezpilotních systémů (UAS), běžně známých jako drony, přes sítě 3GPP (4G LTE a 5G). Je součástí architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) v 5G jádru sítě a funguje jako specializovaná síťová funkce (NF), která komunikuje s dalšími síťovými funkcemi jádra, jako je Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Primární rolí UAS NF je autorizovat operace UAS, spravovat předplatné služeb UAS a zprostředkovávat komunikaci mezi poskytovatelem služby UAS ([USS](/mobilnisite/slovnik/uss/)), operátorem UAS a sítí 3GPP.

Architektonicky UAS NF funguje jako centrální řídicí bod. Autentizuje a autorizuje UAS (který se skládá z bezpilotního prostředku - [UAV](/mobilnisite/slovnik/uav/) - a jeho dálkového ovladače) předtím, než mu povolí přístup k síťovým službám pro spojení příkazů a řízení ([C2](/mobilnisite/slovnik/c2/)) a přenos dat užitečného zatížení. Má rozhraní k systému USS/UTM (UAS Traffic Management), což je externí poskytovatel služeb spravující vzdušný prostor a schvalování letů. UAS NF předává žádosti o autorizaci letu od operátora UAS (prostřednictvím UE) k USS a vynucuje přijatá autorizační rozhodnutí. Také podporuje hlášení polohy UAV k USS pro povědomí o vzdušném prostoru a může prostřednictvím PCF uplatňovat specifické politiky QoS pro provoz UAS.

Klíčovými součástmi rámce služby UAS jsou samotná UAS NF, profil předplatného služby UAS uložený v UDM a servisní rozhraní (např. Nuu, Nudm, Nnef). UAS NF funguje tak, že nejprve ověří identitu a předplatné UAS. Pro letovou operaci přijme žádost o autorizaci letu UAS, případně včetně plánované trasy letu. Tuto žádost přepošle autorizovanému USS. Po obdržení schválení může UAS NF nařídit síti vytvoření vyhrazených QoS toků pro spojení C2 se zárukami vysoké spolehlivosti a nízké latence. Také podporuje průběžné nebo spouštěné hlášení polohy během letu. Toto komplexní řízení umožňuje operace za hranicí přímé viditelnosti (BVLOS) tím, že poskytuje zabezpečené, sledované a sítí řízené komunikační spojení.

## K čemu slouží

UAS NF byla vytvořena, aby řešila rostoucí potřebu bezpečné, škálovatelné a regulované integrace dronů do národního vzdušného prostoru s využitím všudypřítomných mobilních sítí. Před její specifikací používaly drony přímé rádiové spoje bod-bod (např. Wi-Fi) s omezeným dosahem, bez vnitřní autorizace založené na síti a bez integrace se systémy řízení letového provozu. To představovalo bezpečnostní, zabezpečovací a škálovatelnostní výzvy pro komerční aplikace dronů. Síť 3GPP poskytuje široké pokrytí, robustní zabezpečení, podporu mobility a vysokou kapacitu, což z ní činí ideálního kandidáta pro připojení UAS.

Motivace pro standardizaci UAS NF vycházela z celosvětových regulatorních snah (např. FAA, EASA), které vyžadují dálkovou identifikaci, geografická omezení a řízení provozu pro drony. 3GPP zahájilo práci na definici síťové podpory pro UAS, aby umožnilo kompatibilní komerční služby. UAS NF řeší problém, jak může mobilní síť autentizovat dron jako legitimního uživatele, autorizovat jeho konkrétní let a poskytnout nezbytnou kvalitu služeb a služby sledování polohy požadované regulátory a poskytovateli služeb UAS.

Řeší omezení ad-hoc připojení tím, že poskytuje standardizovaný, zabezpečený rámec. Tento rámec umožňuje jedinému operátoru dronů spravovat flotilu napříč širokými geografickými oblastmi s využitím stávající mobilní infrastruktury, umožňuje plynulý předávání služeb mezi buňkami během letu a zajišťuje, že kritická spojení C2 jsou chráněna a prioritizována. Vytvoření UAS NF v 3GPP Release 15 a její vylepšení v pozdějších vydáních představují klíčový krok k umožnění pokročilých služeb dronů, jako je doručování balíků, inspekce infrastruktury a letecké sledování ve velkém měřítku.

## Klíčové vlastnosti

- Autorizuje operace UAS a spravuje předplatné služeb UAS.
- Spolupracuje s externími systémy UAS Service Supplier (USS) / UTM.
- Podporuje zabezpečenou identifikaci a autentizaci UAS (Remote ID).
- Umožňuje hlášení polohy a sledování UAV k USS.
- Usnadňuje vytváření spojení pro příkazy a řízení (C2) se zárukou QoS.
- Integruje se s architekturou 5G Core založenou na službách (SBA).

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 22.125** (Rel-19) — UAS Requirements via 3GPP System
- **TS 22.825** (Rel-16) — UAS Remote Identification and Tracking over 3GPP
- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.754** (Rel-17) — Study on UAS Connectivity, ID & Tracking
- **TR 23.755** (Rel-17) — Study on app layer support for UAS
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 27.007** (Rel-19) — AT Command Set for UE
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [UAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/uas/)
