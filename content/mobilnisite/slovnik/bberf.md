---
slug: "bberf"
url: "/mobilnisite/slovnik/bberf/"
type: "slovnik"
title: "BBERF – Bearer Binding and Event Reporting Function"
date: 2025-01-01
abbr: "BBERF"
fullName: "Bearer Binding and Event Reporting Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bberf/"
summary: "BBERF je logická funkce ve vyvinutém paketovém jádře (EPC), která váže služební datové toky na přenosové kanály a hlásí události funkci PCRF. Umožňuje dynamické řízení QoS a vynucování politik v příst"
---

BBERF (funkce pro vazbu přenosových kanálů a hlášení událostí) je logická funkce ve vyvinutém paketovém jádře, která váže služební datové toky na přenosové kanály a hlásí události funkci PCRF za účelem dynamického řízení kvality služeb (QoS) a vynucování politik v přístupových sítích mimo 3GPP.

## Popis

Bearer Binding and Event Reporting Function (BBERF) je klíčovou součástí architektury řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) podle 3GPP, konkrétně navrženou pro přístupové sítě mimo 3GPP, jako jsou Wi-Fi, WiMAX a pevné širokopásmové sítě. Jako logická funkce sídlí BBERF v přístupové bráně sítí mimo 3GPP a slouží jako bod pro vynucování politik, který komunikuje s [PCRF](/mobilnisite/slovnik/pcrf/) přes referenční bod Gxx. Jeho primární odpovědností je mapovat služební datové toky identifikované PCRF na odpovídající přenosové kanály nebo tunely v přístupové síti, čímž zajišťuje správnou aplikaci QoS politik na uživatelský provoz.

Architektonicky BBERF funguje jako zprostředkovatel mezi PCRF a systémem správy přenosových kanálů přístupové sítě. Když uživatel naváže připojení prostřednictvím přístupové sítě mimo 3GPP, poskytne PCRF prostřednictvím rozhraní Gxx BBERF pravidla PCC obsahující parametry QoS a informace o účtování. BBERF pak tato pravidla PCC přeloží na příkazy specifické pro přístupovou síť a podle potřeby vytváří, upravuje nebo ruší přenosové kanály. Tento překlad je klíčový, protože různé přístupové technologie mají odlišné modely přenosových kanálů a možnosti QoS – BBERF tyto rozdíly abstrahuje a poskytuje PCRF jednotné rozhraní.

Fungování BBERF zahrnuje několik klíčových procesů: vazbu kanálu, hlášení událostí a vynucování politik. Při vazbě kanálu BBERF zkoumá příchozí pravidla PCC a rozhodne, který existující přenosový kanál by měl přenášet každý služební datový tok na základě požadavků QoS. Pokud vhodný kanál neexistuje, spustí vytvoření nového kanálu s odpovídajícími charakteristikami QoS. Hlášení událostí umožňuje BBERF informovat PCRF o významných událostech v přístupové síti, jako jsou selhání při vytváření kanálu, změny parametrů QoS nebo přechody mezi přístupovými technologiemi. Tyto zprávy umožňují PCRF činit informovaná rozhodnutí o politikách a udržovat kontinuitu relace.

Tato funkce také hraje zásadní roli v mobilních scénářích zahrnujících přechody mezi sítěmi 3GPP a sítěmi mimo 3GPP. Během takových přechodů BBERF koordinuje s PCRF, aby zajistil plynulý přenos QoS politik mezi přístupovými technologiemi. Tato schopnost je zvláště důležitá pro udržení kvality služby při vertikálních přechodech, kdy se uživatelé pohybují mezi mobilními a Wi-Fi sítěmi bez přerušení služby. Mechanismus hlášení událostí BBERF poskytuje PCRF informace o stavu přístupové sítě v reálném čase, což umožňuje dynamické úpravy politik na základě aktuálních možností sítě a polohy uživatele.

Z hlediska nasazení sítě je BBERF typicky implementován uvnitř důvěryhodné přístupové brány pro sítě mimo 3GPP (TNW-AGW) nebo vyvinuté brány paketových dat (ePDG) pro nedůvěryhodný přístup. Jeho integrace s těmito branami umožňuje centralizovanou správu politik při zachování distribuovaného vynucování na okraji sítě. Tato distribuovaná architektura vyvažuje škálovatelnost s rychlou odezvou a zajišťuje, že rozhodnutí o QoS lze rychle implementovat bez přetížení síťového jádra. Design BBERF odráží vizi 3GPP o konvergentní správě politik napříč heterogenními sítěmi a poskytuje základ pro konzistentní uživatelský zážitek bez ohledu na přístupovou technologii.

## K čemu slouží

BBERF byl představen v Release 8 3GPP jako součást architektury Evolved Packet System (EPS) k řešení rostoucí potřeby integrovaného řízení politik napříč heterogenními sítěmi. Před jeho zavedením měly sítě 3GPP dobře definované mechanismy [PCC](/mobilnisite/slovnik/pcc/) pro mobilní přístup prostřednictvím funkce [PCEF](/mobilnisite/slovnik/pcef/), ale přístupovým sítím mimo 3GPP chyběly standardizovaná rozhraní pro koordinaci politik se síťovým jádrem. Toto omezení způsobovalo nekonzistence v kvalitě služeb, když se uživatelé připojovali přes Wi-Fi nebo jiné alternativní přístupové technologie, protože QoS politiky nemohly být jednotně aplikovány na různé typy sítí.

Hlavní motivací pro vytvoření BBERF bylo rozšíření rámce PCC 3GPP na přístupové sítě mimo 3GPP, což operátorům umožňuje nabízet konzistentní kvalitu služeb a modely účtování bez ohledu na to, jak se uživatelé k síti připojí. Tato schopnost se stávala stále důležitější, když mobilní operátoři začali integrovat přesměrování provozu na Wi-Fi do své nabídky služeb a uživatelé očekávali plynulé přechody mezi mobilními a Wi-Fi sítěmi. Bez BBERF čelili operátoři výzvám při aplikaci stejných sofistikovaných QoS politik a pravidel účtování na přístup mimo 3GPP, což omezovalo jejich schopnost efektivně zpoplatňovat služby napříč všemi typy přístupu.

BBERF vyřešil několik klíčových problémů: poskytl standardizované rozhraní (Gxx) mezi sítěmi mimo 3GPP a [PCRF](/mobilnisite/slovnik/pcrf/), umožnil dynamickou správu přenosových kanálů pro služební toky v prostředích mimo 3GPP a usnadnil hlášení událostí z přístupových sítí k řadiči politik. Tyto schopnosti umožnily operátorům implementovat pokročilé služby, jako je streamování videa se zaručenou přenosovou rychlostí, prioritní hlasové služby a diferencované účtování napříč všemi přístupovými technologiemi. Díky abstrakci rozdílů mezi různými přístupovými technologiemi mimo 3GPP BBERF zjednodušil implementaci politik a snížil složitost integrace pro nasazení s více přístupovými sítěmi.

## Klíčové vlastnosti

- Vazba přenosových kanálů mezi pravidly PCC a přenosovými kanály specifickými pro přístupovou síť
- Hlášení událostí funkci PCRF přes rozhraní Gxx
- Vynucování QoS politik v přístupových sítích mimo 3GPP
- Podpora mobility mezi sítěmi 3GPP a sítěmi mimo 3GPP
- Dynamické vytváření/úprava/zrušení přenosových kanálů
- Integrace s důvěryhodnými a nedůvěryhodnými přístupovými bránami pro sítě mimo 3GPP

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 29.154** (Rel-19) — Nt Reference Point Protocol
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.804** (Rel-8) — CT3 Aspects of System Architecture Evolution
- **TS 29.810** (Rel-13) — Diameter Load Control Study
- **TS 29.816** (Rel-10) — PCRF Failure & Restoration Study
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC

---

📖 **Anglický originál a plná specifikace:** [BBERF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bberf/)
