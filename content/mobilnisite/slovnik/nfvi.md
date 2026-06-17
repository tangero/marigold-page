---
slug: "nfvi"
url: "/mobilnisite/slovnik/nfvi/"
type: "slovnik"
title: "NFVI – Network Functions Virtualization Infrastructure"
date: 2025-01-01
abbr: "NFVI"
fullName: "Network Functions Virtualization Infrastructure"
category: "Management"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nfvi/"
summary: "Podkladová hardwarová a softwarová platforma, která poskytuje virtualizované prostředky (výpočetní, úložné, síťové) pro provoz virtualizovaných síťových funkcí (VNFs). Je základem pro cloud-nativní na"
---

NFVI je hardwarová a softwarová platforma, která poskytuje virtualizované výpočetní, úložné a síťové prostředky potřebné pro provoz virtualizovaných síťových funkcí.

## Popis

Infrastruktura pro virtualizaci síťových funkcí (NFVI) je základní vrstvou pro virtualizované a cloud-nativní síťové architektury, jak je definována [ETSI](/mobilnisite/slovnik/etsi/) a přijata 3GPP. Zahrnuje souhrn všech hardwarových a softwarových komponent, které společně vytvářejí prostředí, ve kterém jsou virtualizované síťové funkce (VNFs) nasazovány, spravovány a provozovány. Koncepčně abstrahuje fyzické prostředky do fondu virtuálních prostředků, odděluje síťový software od proprietárního hardwaru. Tato abstrakce je klíčová pro umožnění elasticity, škálovatelnosti a automatizace slibované virtualizací sítí.

Architektura NFVI je typicky strukturována do tří domén: výpočetní domény, úložné domény a síťové domény. Výpočetní doména se skládá z komerčních serverů standardní řady ([COTS](/mobilnisite/slovnik/cots/)), které poskytují výpočetní výkon prostřednictvím virtuálních strojů (VMs) nebo kontejnerů. Úložná doména zahrnuje lokální i sdílené úložné systémy, virtualizované tak, aby poskytovaly VNFs blokové, objektové nebo souborové úložiště. Síťová doména zahrnuje fyzická síťová rozhraní, přepínače a směrovače spolu s jejich virtualizovanými protějšky, jako jsou virtuální přepínače (např. Open vSwitch) a virtuální sítě, které zajišťují konektivitu mezi VNFs a k externím sítím.

V softwarovém srdci NFVI leží virtualizační vrstva, nejčastěji hypervizor (pro nasazení založená na VMs) nebo kontejnerový runtime (pro nasazení založená na kontejnerech). Tato vrstva je zodpovědná za abstrakci fyzických prostředků, jejich rozdělení a prezentaci jako virtuálních prostředků VNFs. Spravuje životní cyklus těchto virtuálních prostředků, zajišťuje izolaci, zabezpečení a výkon pro každou VNF. Nad ní poskytuje správce virtuální infrastruktury (VIM), jako je OpenStack nebo Kubernetes, orchestraci a řídicí rovinu pro tyto virtuální prostředky. VIM řeší úkoly jako inventář prostředků, jejich alokaci, umístění a monitorování a komunikuje s vyššími systémy pro správu a orchestraci, jako je [NFVO](/mobilnisite/slovnik/nfvo/).

Role NFVI v ekosystému 3GPP spočívá v hostování funkcí jádra sítě (jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)) a dalších síťových aplikací. Poskytnutím standardizované, na dodavateli nezávislé platformy umožňuje operátorům nasazovat síťové funkce od různých dodavatelů na společné infrastruktuře, čímž ruší závislost na jediném dodavateli. Umožňuje rychlé nasazení služeb prostřednictvím automatizace, efektivní využití prostředků díky jejich sdružování a sdílení a škálovatelné operace, které mohou pružně růst nebo se zmenšovat podle poptávky. Výkon, spolehlivost a zabezpečení NFVI jsou proto prvořadé, protože přímo ovlivňují kvalitu služeb celé mobilní sítě.

## K čemu slouží

NFVI bylo vytvořeno, aby řešilo omezení tradičních telekomunikačních sítí postavených na proprietárních, integrovaných hardwarových zařízeních. Tyto starší systémy byly nákladné, pomalé při nasazování a upgradování a vedly k závislosti na dodavateli, což dusilo inovace a zvyšovalo provozní složitost. Primární motivací bylo využít [IT](/mobilnisite/slovnik/it/) virtualizační technologie a cloudové principy k transformaci telekomunikační infrastruktury, aby byla agilnější, nákladově efektivnější a škálovatelnější.

Historický kontext představuje celoprůmyslový posun směrem k virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)), který prosazuje ETSI. NFVI je realizací infrastrukturního pilíře vize NFV. Řeší problém závislosti na hardwaru tím, že abstrahuje síťové funkce do softwaru, který může běžet na standardních serverích, úložištích a přepínačích vyráběných ve velkých sériích. Tento posun umožňuje síťovým operátorům těžit z úspor z rozsahu a rychlého inovačního cyklu IT průmyslu.

Navíc NFVI umožňuje dynamickou orchestraci a automatizaci síťových služeb, což je nezbytné pro podporu moderních požadavků, jako je dělení sítě (network slicing), edge computing a služby 5G na vyžádání. Poskytuje základní agilitu potřebnou pro konkurenceschopnost s cloud-nativními poskytovateli služeb a pro efektivní správu masivního rozsahu a různorodých požadavků služeb 5G a dalších generací.

## Klíčové vlastnosti

- Abstrakce fyzických výpočetních, úložných a síťových prostředků
- Podpora úloh založených na virtuálních strojích (VMs) i na kontejnerech
- Integrace se správci virtuální infrastruktury (VIMs), jako je OpenStack/Kubernetes
- Umožňuje víceklientský provoz a izolaci mezi různými VNFs
- Poskytuje API pro automatizovanou správu životního cyklu prostředků
- Tvoří základ pro cloud-nativní nasazení síťových funkcí

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [NFVO – Network Functions Virtualization Orchestrator](/mobilnisite/slovnik/nfvo/)

## Definující specifikace

- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.520** (Rel-19) — PM for Virtualized Mobile Networks
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security
- **TR 33.927** (Rel-19) — Security Assurance for Virtualized Network Products

---

📖 **Anglický originál a plná specifikace:** [NFVI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nfvi/)
