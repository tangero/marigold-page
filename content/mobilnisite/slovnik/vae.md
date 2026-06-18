---
slug: "vae"
url: "/mobilnisite/slovnik/vae/"
type: "slovnik"
title: "VAE – V2X Application Enabler"
date: 2026-01-01
abbr: "VAE"
fullName: "V2X Application Enabler"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vae/"
summary: "Vrstva aplikačních služeb v rámci 3GPP, která poskytuje standardizovaný rámec pro aplikace komunikace mezi vozidlem a vším (V2X). Abstrahuje složitost podkladových sítí a nabízí vývojářům aplikací spo"
---

VAE je vrstva aplikačních služeb (service capability layer) v rámci 3GPP, která poskytuje standardizovaný rámec pro aplikace V2X tím, že abstrahuje síťovou složitost a nabízí společné funkce, jako je distribuce zpráv a zabezpečení.

## Popis

[V2X](/mobilnisite/slovnik/v2x/) Application Enabler (VAE) je architektura aplikační vrstvy definovaná 3GPP, primárně specifikovaná v TS 23.286. Funguje jako mezivrstva mezi aplikacemi specifickými pro V2X (např. varování před kolizí, jízda v koloně, zvyšování dopravní efektivity) a podkladovými komunikačními službami 3GPP, které mohou být založeny na rozhraních PC5 (sidelink) nebo Uu (buněčný přístup). VAE poskytuje sadu společných aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)) a aplikačních služeb, které zjednodušují vývoj aplikací tím, že skrývají složitost komunikačního zásobníku, výběru sítě a manipulace se zprávami.

Z architektonického hlediska se VAE nachází na V2X aplikačním serveru (uvnitř sítě) a/nebo uvnitř vozidlové koncové stanice (VUE). Mezi její klíčové komponenty patří funkce VAE [SCEF](/mobilnisite/slovnik/scef/) (Service Capability Exposure Function) nebo VAE aplikační server, které zpřístupňují služby aplikacím. Mezi základní funkce patří manipulace se zprávami V2X, která zahrnuje příjem, ověření a distribuci zpráv, jako jsou zprávy o kooperativním povědomí ([CAM](/mobilnisite/slovnik/cam/)) a decentralizované výstražné zprávy o stavu prostředí ([DENM](/mobilnisite/slovnik/denm/)). Spravuje životní cyklus těchto zpráv včetně kontroly jejich relevance na základě času, geografické polohy a typu události. Dále VAE poskytuje správu skupin pro jízdu v koloně nebo dynamické shluky vozidel, oznamování a vyhledávání služeb, aby bylo možné služby V2X nalézt a přihlásit se k jejich odběru, a podporu zabezpečení na aplikační vrstvě, včetně koncově-koncového ověřování zpráv a ochrany jejich integrity.

Princip fungování: Aplikace V2X, například služba Intersection Movement Assist, komunikuje s vrstvou VAE prostřednictvím standardizovaných API namísto přímého rozhraní s vrstvou [AS](/mobilnisite/slovnik/as/) nebo přístupovou vrstvou. Aplikace požádá VAE o vysílání konkrétního typu zprávy s určitými parametry (cílová oblast, priorita). VAE následně zpracuje převod tohoto požadavku na příslušné primitiva nižších vrstev, vybere správný přenos (např. vysílání přes PC5, unicast přes Uu na V2X aplikační server pro širší distribuci), použije potřebné politiky QoS a spravuje plánování zpráv. Na straně příjmu VAE filtruje příchozí zprávy na základě profilů odběru a relevance a předává pouze relevantní data registrovaným aplikacím. Tato abstrakce je klíčová pro zajištění interoperability a umožňuje aplikacím fungovat konzistentně napříč různými regiony, síťovými nasazeními a modely vozidel.

## K čemu slouží

VAE byla vytvořena za účelem řešení fragmentace a složitosti při vývoji a nasazování aplikací [V2X](/mobilnisite/slovnik/v2x/). Původní standardy V2X (např. od [ETSI](/mobilnisite/slovnik/etsi/) ITS) definovaly aplikační protokoly, ale ponechaly mezeru v tom, jak tyto aplikace bezproblémově využívají sítě 3GPP, zejména s příchodem LTE-V2X a NR-V2X, které nabízejí jak přímou (sidelink), tak síťovou komunikaci. Bez společné aplikační vrstvy by každý výrobce vozidel (OEM) nebo vývojář aplikací musel vytvářet proprietární middleware pro správu komunikace, vyhledávání služeb a zabezpečení, což by vedlo k neinteroperabilním řešením a pomalému přijetí trhem.

Motivace vycházela z potřeby standardizovaného 'middlewaru' v rámci ekosystému 3GPP, který by překlenul propast mezi obecnými síťovými schopnostmi 3GPP a specifickými, často bezpečnostně kritickými požadavky aplikací V2X. Řeší omezení čistě přístupově orientovaného pohledu tím, že poskytuje síťové služby s ohledem na aplikace. Tím, že nabízí jednotnou sadu služeb, VAE snižuje vstupní bariéru pro vývojáře aplikací, kteří se mohou soustředit na aplikační logiku namísto komunikačního zásobníku. Také umožňuje síťovým operátorům zpřístupňovat a zpeněžovat pokročilé síťové funkce (jako jsou služby polohy s edge computingem) pro vertikálu V2X kontrolovaným způsobem. Její vytvoření v Rel-15 bylo v souladu s dozráním LTE-V2X a potřebou připravit aplikační vrstvu pro pokročilé případy užití plánované pro 5G NR-V2X.

## Klíčové vlastnosti

- Abstrakce podkladového přenosu (Uu, PC5) pro výměnu zpráv V2X
- Služba manipulace se zprávami V2X pro distribuci a správu životního cyklu zpráv CAM/DENM
- Správa geografického rozsahu a relevance přijatých zpráv
- Oznámení, vyhledávání a správa odběru služeb V2X
- Podpora správy skupin na aplikační vrstvě (např. pro jízdu v koloně)
- Zpřístupnění služeb specifických pro V2X (např. QoS, poloha) aplikacím prostřednictvím API

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [CAM – Cooperative Awareness Message](/mobilnisite/slovnik/cam/)
- [DENM – Decentralized Environmental Notification Message](/mobilnisite/slovnik/denm/)

## Definující specifikace

- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.486** (Rel-19) — V2X Application Enabler (VAE) Protocol Spec
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 29.486** (Rel-19) — V2X Application Enabler (VAE) Services

---

📖 **Anglický originál a plná specifikace:** [VAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/vae/)
