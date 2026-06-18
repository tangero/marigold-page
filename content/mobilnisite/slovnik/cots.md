---
slug: "cots"
url: "/mobilnisite/slovnik/cots/"
type: "slovnik"
title: "COTS – Commercial Off-The-Shelf"
date: 2026-01-01
abbr: "COTS"
fullName: "Commercial Off-The-Shelf"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cots/"
summary: "COTS odkazuje na komerčně dostupné hotové hardwarové a softwarové produkty, které jsou k dispozici k okamžitému nákupu, na rozdíl od řešení vyvíjených na míru. V kontextu 3GPP umožňuje operátorům nasa"
---

COTS (Commercial Off-The-Shelf) označuje využití komerčně dostupných, hotových hardwarových a softwarových produktů, což operátorům umožňuje nasazovat virtualizované síťové funkce na standardních serverech za účelem snížení nákladů a rychlejšího uvedení do provozu.

## Popis

Commercial Off-The-Shelf (COTS) ve standardech 3GPP označuje využití standardizovaných, komerčně dostupných hardwarových a softwarových komponent, které lze zakoupit od dodavatelů bez nutnosti vlastního vývoje. Tento přístup zásadně transformuje architekturu telekomunikačních sítí tím, že umožňuje běh síťových funkcí na hardwaru pro všeobecné použití namísto proprietárního specializovaného zařízení. Specifikace 3GPP poskytují rámce a požadavky pro implementaci telekomunikačních funkcí na platformách COTS, zajišťují interoperabilitu, zabezpečení a výkon a zároveň využívají pokroky v komerční výpočetní technice.

Z architektonického hlediska implementace COTS v sítích 3GPP zahrnuje několik klíčových komponent: standardní servery na bázi x86 nebo ARM, komerční hypervizory nebo kontejnerové platformy, komerční operační systémy a standardizovaná rozhraní. Tyto komponenty spolupracují prostřednictvím virtualizačních vrstev, které abstrahují podkladový hardware, což umožňuje nasazení síťových funkcí jako virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) nebo cloud-nativních síťových funkcí ([CNF](/mobilnisite/slovnik/cnf/)). Specifikace 3GPP definují, jak tyto virtualizované funkce vzájemně interagují a jak komunikují s fyzickou infrastrukturou, aby byly splněny požadavky na výkon, spolehlivost a zabezpečení i při použití nespecializovaného hardwaru.

Při provozu fungují síťové funkce založené na COTS prostřednictvím softwarově definovaných architektur, kde jsou řídicí a datové roviny odděleny a implementovány jako softwarové aplikace. Hardware poskytuje výpočetní, úložné a síťové prostředky prostřednictvím standardizovaných rozhraní, zatímco síťové funkce běží jako softwarové instance, které lze dynamicky vytvářet, škálovat a migrovat. To vyžaduje sofistikované systémy orchestrace a správy, které dokážou přidělovat prostředky, monitorovat výkon a zajišťovat kontinuitu služeb. Rámec 3GPP pro správu a orchestraci ([MANO](/mobilnisite/slovnik/mano/)) spolu se specifikacemi jako 28.500 poskytují potřebná rozhraní a postupy pro správu nasazení založených na COTS.

Role COTS v sítích 3GPP zasahuje do více domén, včetně jádra sítě, kde funkce jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a [UPF](/mobilnisite/slovnik/upf/) mohou běžet na hardwaru COTS; rádiového přístupového sítě, kde jsou virtualizované funkce RAN stále častěji nasazovány na komerčních serverech; a systémů správy. Tento přístup umožňuje operátorům využít úspor z rozsahu komerčního výpočetního průmyslu, rychle nasazovat nové služby prostřednictvím softwarových aktualizací namísto výměny hardwaru a vytvářet flexibilnější a škálovatelnější síťové architektury. Specifikace zajišťují, že i při použití komerčního hardwaru lze zachovat telekomunikační úroveň spolehlivosti a výkonu prostřednictvím redundance, vyrovnávání zátěže a mechanismů kvality služeb implementovaných na softwarové vrstvě.

## K čemu slouží

Adopce COTS v sítích 3GPP řeší několik kritických výzev v telekomunikační infrastruktuře. Historicky se telekomunikační sítě spoléhaly na proprietární, vertikálně integrovaná hardwarová a softwarová řešení od specializovaných dodavatelů, což vedlo k vysokým kapitálovým výdajům, dlouhým cyklům nasazení, závislosti na jediném dodavateli a omezené flexibilitě. Každá síťová funkce vyžadovala vyhrazený hardware, který byl nákladný na vývoj, údržbu a upgrade. Odvětví uznalo, že tento model je neudržitelný, protože datový provoz exponenciálně rostl a nové služby vyžadovaly agilnější možnosti nasazení.

Primární motivací pro adopci COTS bylo využít rychlé inovace a nákladové efektivity komerčního výpočetního průmyslu. Použitím standardních serverů, úložišť a síťových zařízení dostupných od více dodavatelů mohli operátoři snížit náklady prostřednictvím konkurence a úspor z rozsahu. Tento přístup také umožnil rychlejší nasazování nových funkcí a služeb prostřednictvím softwarových aktualizací namísto výměny hardwaru. Nástup technologií cloud computingu, virtualizace a softwarově definovaných sítí poskytl technický základ pro implementaci telekomunikačních funkcí na komerčním hardwaru při zachování požadovaného výkonu a spolehlivosti.

COTS řeší omezení tradičního telekomunikačního zařízení tím, že umožňuje virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)), která odděluje síťové funkce od vyhrazeného hardwaru. To operátorům umožňuje konsolidovat více funkcí na sdílené infrastruktuře, zlepšit využití prostředků prostřednictvím dynamického přidělování a vytvářet flexibilnější síťové architektury, které se mohou pružně škálovat podle poptávky. Standardy 3GPP zajišťují, že implementace založené na COTS splňují telekomunikační požadavky na latenci, propustnost, dostupnost a zabezpečení, což umožňuje přechod od proprietárních systémů k otevřeným, softwarově definovaným sítím při zachování kvality služeb a provozní efektivity.

## Klíčové vlastnosti

- Umožňuje nasazení síťových funkcí na standardních komerčních serverech
- Podporuje virtualizaci prostřednictvím hypervizorů a kontejnerových platforem
- Usnadňuje virtualizaci síťových funkcí (NFV) a cloud-nativní architektury
- Snižuje kapitálové výdaje využitím běžného hardwaru
- Urychluje nasazení služeb prostřednictvím softwarových aktualizací
- Umožňuje pružné škálování a optimalizaci prostředků prostřednictvím softwarového řízení

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)
- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)

## Definující specifikace

- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 32.331** (Rel-19) — Notification Log IRP Requirements
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [COTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cots/)
