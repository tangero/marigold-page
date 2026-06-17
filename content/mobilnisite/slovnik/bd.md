---
slug: "bd"
url: "/mobilnisite/slovnik/bd/"
type: "slovnik"
title: "BD – Baseline DNS Action Information Template"
date: 2026-01-01
abbr: "BD"
fullName: "Baseline DNS Action Information Template"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bd/"
summary: "Standardizovaná šablona pro informace o DNS (Domain Name System) akcích používaná v rámci správy sítí a řízení politik 3GPP. Definuje základní strukturu pro předávání pokynů a parametrů souvisejících"
---

BD je standardizovaná šablona pro informace o DNS akcích, která definuje základní strukturu pro předávání pokynů a parametrů souvisejících se službou DNS v rámci správy sítí a řízení politik 3GPP.

## Popis

Šablona základních informací o [DNS](/mobilnisite/slovnik/dns/) akcích (BD) je strukturovaný datový model definovaný ve specifikacích 3GPP, především v rámci rámců pro provoz, administraci a údržbu (OAM) a řízení politik a účtování (PCC). Slouží jako standardizovaný formát pro zakódování informací souvisejících s DNS akcemi – jako jsou dotazy, odpovědi, přesměrování nebo pokyny k filtrování – které je třeba komunikovat mezi systémy správy sítě, policy servery a síťovými funkcemi. Šablona je navržena jako rozšiřitelná a interoperabilní, aby zařízení a software různých výrobců mohly DNS politiky jednotně interpretovat a provádět. Její architektura je typicky vyjádřena v XML nebo jiných datových modelovacích jazycích s definovanými prvky pro typy akcí, cílové domény, IP adresy, hodnoty TTL (Time to Live) a pravidla přednosti.

V provozu se šablona BD používá v rámci rozhraní správy, jako je referenční bod Np (mezi PCRF a [AF](/mobilnisite/slovnik/af/)), nebo v rámci OAM systémů pro provisioning DNS politik. Například funkce pro pravidla řízení politik a účtování (PCRF) může použít BD k tomu, aby instruovala funkci detekce provozu (TDF) nebo uživatelskou rovinu k aplikaci specifického zacházení se službou DNS – například k blokování přístupu k určitým doménám nebo k přesměrování DNS dotazů na bezpečný resolver. Klíčové součásti šablony zahrnují identifikátory akce (např. 'allow', 'deny', 'redirect'), parametry specifikující zahrnuté DNS záznamy nebo názvy domén a volitelná metadata, jako jsou období platnosti nebo požadavky na logování. Tento strukturovaný přístup umožňuje jemně odstupňovanou kontrolu nad DNS provozem, což je nezbytné pro implementaci rodičovských kontrol, bezpečnostních politik podniků nebo strategií optimalizace sítě.

Role BD v síti je klíčová pro umožnění dynamického a automatizovaného vynucování DNS politik bez manuálního zásahu. Integruje se s širším ekosystémem politik 3GPP, včetně architektury PCC definované v TS 23.203, aby podpořila rozhodování o službách v reálném čase na základě profilů účastníků, stavu sítě nebo požadavků aplikací. Poskytnutím základní šablony 3GPP zajišťuje, že DNS akce mohou být konzistentně aplikovány napříč nasazeními více výrobců, což snižuje složitost integrace a zvyšuje spolehlivost sítě. Šablona navíc podporuje škálovatelnost tím, že umožňuje síťovým operátorům definovat znovupoužitelná pravidla politik aplikovatelná na velké báze účastníků, což usnadňuje efektivní správu služeb souvisejících se službou DNS v prostředí vyvíjejících se technologií 5G a IoT.

## K čemu slouží

BD byla vytvořena, aby řešila potřebu standardizované správy [DNS](/mobilnisite/slovnik/dns/) politik v sítích 3GPP, zejména když se služby staly více závislé na dynamickém a na aplikaci citlivém zacházení s provozem. Před jejím zavedením byly DNS akce často implementovány proprietárními nebo ad-hoc metodami, což vedlo k problémům s interoperabilitou mezi různými síťovými prvky a systémy správy. Tento nedostatek standardizace ztěžoval nasazení konzistentních DNS politik – jako je filtrování obsahu, rodičovské kontroly nebo směrování provozu – napříč heterogenními síťovými prostředími, což brzdilo agilitu služeb a zvyšovalo provozní náklady.

Motivováno rostoucím významem DNS pro poskytování služeb a bezpečnost zavedlo 3GPP BD ve vydání 8 jako součást vylepšení rámců PCC a OAM. Řeší problém fragmentovaného vynucování DNS politik tím, že poskytuje společnou šablonu použitelnou napříč různými rozhraními, jako jsou například rozhraní mezi PCRF, [AF](/mobilnisite/slovnik/af/) a TDF. To operátorům umožňuje implementovat centralizované řízení politik pro DNS akce a zajistit, aby účastníci dostávali jednotný servisní zážitek bez ohledu na podkladové síťové vybavení. Historicky to bylo hnáno expanzí mobilního širokopásmového připojení a potřebou sofistikovanějších schopností správy provozu přesahujících základní účtování a QoS.

BD navíc usnadňuje automatizované síťové operace tím, že umožňuje dynamické provisionování a aktualizaci DNS politik na základě podmínek v reálném čase, jako je zahlcení sítě nebo bezpečnostní hrozby. Řeší omezení dřívějších přístupů, které spoléhaly na statické konfigurace nebo manuální zásahy, které byly neefektivní a náchylné k chybám. Vložením informací o DNS akcích do standardizované šablony umožnilo 3GPP robustnější a škálovatelnější řešení pro správu DNS v kontextu vyvíjejících se technologií, jako je 5G, síťové dělení (network slicing) a IoT, kde je flexibilní a spolehlivé zacházení se službou DNS klíčové pro funkčnost a bezpečnost služeb.

## Klíčové vlastnosti

- Standardizovaná struktura šablony založená na XML pro informace o DNS akcích
- Podpora více typů DNS akcí včetně povolení (allow), zamítnutí (deny) a přesměrování (redirect)
- Integrace s architekturou řízení politik a účtování (PCC) 3GPP
- Rozšiřitelné parametry pro názvy domén, IP adresy a hodnoty TTL
- Umožňuje dynamické provisionování a vynucování politik v reálném čase
- Usnadňuje interoperabilitu napříč síťovým vybavením více výrobců

## Související pojmy

- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 29.556** (Rel-19) — EASDF Service Based Interface Protocol
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.252** (Rel-12) — 3GPP WLAN Interworking Charging
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [BD na 3GPP Explorer](https://3gpp-explorer.com/glossary/bd/)
