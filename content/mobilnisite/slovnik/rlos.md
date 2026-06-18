---
slug: "rlos"
url: "/mobilnisite/slovnik/rlos/"
type: "slovnik"
title: "RLOS – Restricted Local Operator Services"
date: 2025-01-01
abbr: "RLOS"
fullName: "Restricted Local Operator Services"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rlos/"
summary: "Servisní funkce, která omezuje přístup uživatele pouze na lokální služby poskytované operátorem, jako jsou tísňová volání a operátorská podpora, a zároveň blokuje ostatní odchozí hovory. Je klíčová pr"
---

RLOS je servisní funkce, která omezuje uživatele pouze na lokální služby poskytované operátorem, jako jsou tísňová volání, a zároveň blokuje ostatní odchozí hovory. Používá se ve scénářích, jako je roamování nebo u tarifů s omezenými službami.

## Popis

Restricted Local Operator Services (RLOS) je mechanismus řízení služeb definovaný v architektuře 3GPP, který je primárně spravován Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a aplikován prostřednictvím frameworku Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Hlavní funkcí RLOS je uložit uživatelské relaci specifický servisní profil, který selektivně povoluje pouze předdefinovanou sadu služeb považovaných operátorem sítě za nezbytné nebo lokálně relevantní. Když je uživatel označen pro RLOS, HSS poskytne indikaci obslužným síťovým uzlům, jako je [MME](/mobilnisite/slovnik/mme/) v EPS nebo [AMF](/mobilnisite/slovnik/amf/) v 5GS. Tato indikace spustí vynucení odpovídající sady PCC pravidel, která jsou nakonfigurována tak, aby povolovala pouze určité šablony toků provozu ([TFT](/mobilnisite/slovnik/tft/)). Tyto povolené TFT typicky umožňují přístup k vlastní servisní síti operátora (např. pro zákaznickou podporu, doplnění kreditu nebo servisní portály) a k tísňovým službám (např. volání na 112, 911). Všechny ostatní pokusy o odchozí komunikaci, jako jsou běžné hlasové hovory nebo datové relace na veřejný internet, jsou blokovány funkcí Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) s [UPF](/mobilnisite/slovnik/upf/). Architektura je integrována s rozhraními Rx a Gx (nebo jejich ekvivalenty v 5GC) pro dynamickou aplikaci těchto politik. RLOS není samostatná síťová funkce, ale servisní logika implementovaná napříč prvky jádra sítě, která využívá stávající data o předplatiteli a mechanismy řízení politik k dosažení granulárního omezení služeb. Jejím úkolem je poskytnout operátorům flexibilní nástroj pro řízení dostupnosti služeb kontrolovaným způsobem v souladu s komerčními, regulačními nebo síťovými potřebami bez nutnosti úplného odpojení služeb.

## K čemu slouží

RLOS byl zaveden pro řešení specifických provozních a komerčních scénářů, kdy je třeba omezit předplatitele v uskutečňování obecných odchozích hovorů, ale musí mu být zachován přístup k minimální sadě služeb spravovaných operátorem. Primárním případem použití jsou příchozí roamující uživatelé, kteří nemají uzavřenou roamingovou smlouvu nebo jim došel kredit; namísto úplného odepření služeb může operátor aplikovat RLOS, aby uživateli umožnil kontaktovat zákaznickou podporu nebo si doplnit účet. Slouží také uživatelům s restriktivními tarify a zajišťuje, že mohou vždy kontaktovat tísňové služby a operátorskou podporu. Historicky, bez takové funkce, byly možnosti binární: buď plný přístup ke službám, nebo úplné zablokování služeb. RLOS poskytuje střední cestu, která zlepšuje zákaznický zážitek tím, že zachovává přístup k životně důležitým službám, a zároveň chrání operátora před potenciální ztrátou výnosů z nezaplaceného využití. Jeho vytvoření bylo motivováno potřebou sofistikovanějšího řízení služeb v rámci PCC architektury definované od Release 7 výše, což umožňuje dynamickou, politikami řízenou diferenciaci služeb nad rámec jednoduchých seznamů blokování.

## Klíčové vlastnosti

- Dynamické vynucování politik prostřednictvím PCC (Policy and Charging Control) architektury.
- Selektivní povolení provozu na servisní destinace definované operátorem a na tísňová čísla.
- Integrace s HSS/UDM pro indikaci servisního profilu specifického pro předplatitele.
- Aplikace v systémech 4G EPS (prostřednictvím MME, P-GW) i 5G 5GC (prostřednictvím AMF, SMF, UPF).
- Podpora scénářů, jako je roamování, řízení kreditu a předplatná s omezenými službami.
- Využívá standardizované šablony toků provozu (TFT) pro přesnou filtraci a řízení přenosu paketů.

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TR 23.715** (Rel-16) — Study on access to restricted local operator services
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.368** (Rel-19) — NAS Configuration Management Object
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.815** (Rel-16) — Security Study for PARLOS/RLOS
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [RLOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlos/)
