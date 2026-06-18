---
slug: "mano"
url: "/mobilnisite/slovnik/mano/"
type: "slovnik"
title: "MANO – Management and Orchestration"
date: 2026-01-01
abbr: "MANO"
fullName: "Management and Orchestration"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mano/"
summary: "Rámec pro automatizaci správy životního cyklu síťových služeb a virtualizovaných síťových funkcí (VNF) v cloud-nativním prostředí. Zajišťuje nasazení, škálování, hojení a ukončování prostředků napříč"
---

MANO je architektonický rámec pro automatizaci správy životního cyklu síťových služeb a virtualizovaných síťových funkcí, který zajišťuje jejich nasazení, škálování, hojení a ukončování v cloud-nativním prostředí.

## Popis

Management and Orchestration (MANO) je klíčový architektonický rámec definovaný organizacemi 3GPP a [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/) pro automatizaci kompletního životního cyklu síťových služeb složených z Virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) a Fyzických síťových funkcí ([PNF](/mobilnisite/slovnik/pnf/)). Je mozkem konceptu Network Functions Virtualization (NFV), který umožňuje operátorům agilně a efektivně nasazovat a spravovat softwarové síťové služby. Rámec MANO se skládá ze tří hlavních funkčních bloků: NFV Orchestrator ([NFVO](/mobilnisite/slovnik/nfvo/)), VNF Manager ([VNFM](/mobilnisite/slovnik/vnfm/)) a Virtualized Infrastructure Manager ([VIM](/mobilnisite/slovnik/vim/)). Tyto komponenty spolupracují na převodu požadavků na vysoké úrovni služeb na konkrétní příkazy pro výpočetní, úložné a síťové prostředky.

NFV Orchestrator (NFVO) je zodpovědný za správu životního cyklu síťových služeb ([NS](/mobilnisite/slovnik/ns/)). Přijímá požadavky na nasazení služeb, často popsané v šabloně pro specifikaci topologie a orchestraci (jako je TOSCA), a koordinuje vytváření, škálování, aktualizaci a ukončování příslušných VNF. NFVO spravuje katalog služeb, ověřuje dostupnost prostředků a řeší závislosti mezi VNF. VNF Manager (VNFM) dohlíží na životní cyklus jednotlivých instancí VNF, jako je instalace softwaru, konfigurace, škálování a hojení. Každá VNF může mít vlastní vyhrazený VNFM, nebo může být spravována generickým VNFM, který obsluhuje více VNF. Virtualized Infrastructure Manager (VIM) řídí NFV infrastrukturu (NFVI), která zahrnuje hypervizory, kontejnery, fyzické servery a sítě. Mezi oblíbené VIM patří OpenStack a Kubernetes. VIM přiděluje a monitoruje virtuální prostředky (vCPU, vRAM, vStorage) podle pokynů od NFVO/VNFM.

MANO funguje prostřednictvím řady referenčních bodů (rozhraní), jako jsou Os-Ma-nfvo (mezi OSS/BSS a NFVO), Or-Vnfm (mezi NFVO a VNFM) a Vi-Vnfm (mezi VNFM a VIM). Proces začíná, když operátor nebo zákazník požádá o novou síťovou službu prostřednictvím Operations Support System (OSS). NFVO požadavek ověří, zkontroluje dostupnost prostředků přes VIM a následně dá pokyn VNFM k vytvoření požadovaných VNF. VNFM následně spolupracuje s VIM na zřízení virtuálních strojů nebo kontejnerů, načtení softwarových obrazů VNF a konfiguraci sítě. Po celou dobu životnosti služby MANO sleduje výkon a poruchy a spouští automatické škálování nebo hojení podle definovaných politik. Tato automatizace je zásadní pro podporu dynamických služeb, jako je síťové dělení (network slicing), kde je třeba na požádání vytvářet a upravovat izolované logické sítě pro různé klienty nebo případy užití.

## K čemu slouží

MANO bylo vytvořeno k řešení provozních komplikací zavedených virtualizací sítí. Tradiční telekomunikační sítě se spoléhaly na proprietární hardwarová zařízení, která byla ručně zřizována a spravována, což vedlo k dlouhým cyklům nasazení (měsíce) a vysokým kapitálovým i provozním nákladům. Přechod na softwarové VNF běžící na běžně dostupném hardwaru (COTS) sliboval větší agilitu a úsporu nákladů, ale vyžadoval nový paradigma správy. Bez automatizace by správa stovek virtuálních instancí nebyla ve velkém měřítku možná. MANO poskytuje potřebnou orchestrační vrstvu k plnému využití výhod NFV.

Rámec řeší klíčové výzvy, jako je agilita služeb, optimalizace prostředků a interoperabilita více dodavatelů. Umožňuje operátorům rychle uvádět nové služby, pružně škálovat prostředky podle poptávky a snižovat manuální chyby prostřednictvím automatizace. Historicky měla každá síťová funkce svůj vlastní systém správy prvků (EMS), což vytvářelo izolované celky. MANO zavádí standardizovaný jednotný přístup ke správě celého řetězce služeb. Jeho vývoj byl motivován potřebou podpory nových technologií, jako je 5G, které vyžadují síťové dělení, edge computing a služby s ultra-nízkou latencí, jež si žádají dynamickou programovatelnou infrastrukturu. MANO je tedy základním kamenem pro transformaci telekomunikačních sítí na flexibilní cloud-nativní platformy.

## Klíčové vlastnosti

- Kompletní automatizace životního cyklu síťových služeb a VNF
- Modulární architektura s komponentami NFVO, VNFM a VIM
- Podpora orchestrace napříč více doménami a od více dodavatelů
- Integrace s OSS/BSS a správou politik
- Schopnosti automatického škálování, hojení a monitorování výkonu
- Standardizované šablony (např. deskriptory založené na TOSCA) pro definici služeb

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.794** (Rel-19) — Study on Zero Trust Security Enablers for 5G
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security

---

📖 **Anglický originál a plná specifikace:** [MANO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mano/)
