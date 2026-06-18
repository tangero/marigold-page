---
slug: "vnfc"
url: "/mobilnisite/slovnik/vnfc/"
type: "slovnik"
title: "VNFC – Virtualized Network Function Component"
date: 2025-01-01
abbr: "VNFC"
fullName: "Virtualized Network Function Component"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vnfc/"
summary: "Virtualized Network Function Component (VNFC) je modulární softwarová komponenta, která implementuje část virtualizované síťové funkce (VNF). Jedná se o nejmenší nasaditelnou jednotku v rámci VNF, což"
---

VNFC je nejmenší nasaditelná softwarová komponenta, která implementuje část virtualizované síťové funkce, a umožňuje tak flexibilní škálování a správu životního cyklu.

## Popis

Virtualized Network Function Component (VNFC) je klíčový koncept v architektonickém rámci [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/), který přijal a specifikoval 3GPP pro správu virtualizovaných síťových funkcí. Představuje samostatný, nasaditelný softwarový modul, který zapouzdřuje specifickou podmnožinu funkcionality větší virtualizované síťové funkce ([VNF](/mobilnisite/slovnik/vnf/)). VNF se typicky skládá z více propojených VNFC, z nichž každá je odpovědná za odlišný úkol, jako je zpracování signálu, správa relací nebo přeposílání paketů. Tato dekompozice je v souladu s cloud-nativními principy, kde jsou aplikace budovány jako sada volně provázaných, nezávisle nasaditelných služeb.

VNFC jsou instancovány jako virtuální stroje ([VM](/mobilnisite/slovnik/vm/)) nebo kontejnery na virtualizované infrastruktuře, konkrétně v rámci Network Functions Virtualization Infrastructure ([NFVI](/mobilnisite/slovnik/nfvi/)). Každá VNFC má své vlastní požadavky na zdroje ([CPU](/mobilnisite/slovnik/cpu/), paměť, úložiště) a spojuje se s ostatními VNFC prostřednictvím virtuálních spojů, aby vytvořila kompletní VNF. VNFC Descriptor (VNFC D) je šablona pro nasazení, která tyto požadavky definuje, včetně softwarových obrazů, úrovní instancování a závislostí. Tento deskriptor je součástí širšího VNF Descriptor používaného orchestračními systémy.

Z provozní perspektivy jsou VNFC primárními jednotkami pro škálování a ozdravné akce. VNF Manager ([VNFM](/mobilnisite/slovnik/vnfm/)) může škálovat VNF horizontálně přidáváním nebo odebíráním instancí konkrétního typu VNFC, nebo vertikálně úpravou zdrojů přidělených instanci VNFC. Podobně, pokud VNFC selže, může VNFM zahájit ozdravný postup k ukončení vadné instance a vytvoření nové. Tato jemně odstupňovaná kontrola umožňuje efektivní využití zdrojů a vysokou dostupnost služeb, což je klíčové pro telekomunikační sítě.

Role VNFC zasahuje do oblasti zajištění služeb a správy výkonu. Protože lze každou komponentu monitorovat nezávisle, získávají operátoři detailní přehled o výkonu a stavu svých síťových služeb. Metriky jako propustnost, latence a míra chyb lze sbírat na úrovni VNFC, což umožňuje přesnou analýzu hlavní příčiny a cílenou optimalizaci. Toto řízení na úrovni komponent představuje významný pokrok oproti monolitickým síťovým zařízením a připravuje cestu pro plně automatizované, intent-based síťové operace.

## K čemu slouží

Koncept VNFC byl vytvořen, aby řešil omezení monolitických, hardwarových síťových zařízení. Tradiční síťové funkce byly implementovány jako integrované jednotky proprietárního softwaru a hardwaru, což je činilo rigidními, nákladnými na škálování a pomalými na upgrade. Posun směrem k Network Functions Virtualization ([NFV](/mobilnisite/slovnik/nfv/)) měl za cíl oddělit software od hardwaru, ale rané virtualizované funkce často zůstávaly jako velké, monolitické softwarové obrazy, což omezovalo agilitu slibovanou virtualizací.

Zavedení VNFC umožňuje granularnější a flexibilnější architekturu. Rozdělením VNF na menší funkční komponenty mohou operátoři škálovat a aktualizovat části síťové funkce nezávisle. Například ve virtualizovaném Evolved Packet Core (vEPC) lze komponentu správy relací (VNFC) horizontálně škálovat během špičky, aniž by se musela škálovat i komponenta brány paketů, což vede k efektivnějšímu využití zdrojů. Tato komponentizace je odrazovým můstkem k cloud-nativním síťovým funkcím budovaným pomocí mikroslužeb, které nabízejí ještě větší odolnost a schopnosti kontinuálního nasazování.

VNFC jsou v konečném důsledku základním prvkem pro dosažení hlavních výhod NFV: snížení kapitálových a provozních výdajů, zrychlení inovací služeb a zlepšení provozní agility. Umožňují síťovým operátorům spravovat své zdroje se stejnou efektivitou a automatizací jako poskytovatelé cloudových služeb, což je nezbytné pro konkurenceschopnost na trhu, který vyžaduje rychlé nasazení nových služeb, jako je 5G network slicing a edge computing.

## Klíčové vlastnosti

- Modulární softwarová komponenta implementující podmnožinu funkcionality VNF
- Nejmenší nezávisle nasaditelná a spravovatelná jednotka v rámci VNF
- Definována VNFC Deskriptorem specifikujícím požadavky na zdroje a závislosti
- Instancována jako virtuální stroj nebo kontejner na NFVI
- Primární jednotka pro horizontální/vertikální škálování a akce obnovy po poruše
- Umožňuje jemně odstupňované monitorování výkonu a zajištění služeb

## Související pojmy

- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)
- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [VNFM – Virtualized Network Function Manager](/mobilnisite/slovnik/vnfm/)
- [NFVI – Network Functions Virtualization Infrastructure](/mobilnisite/slovnik/nfvi/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TS 28.516** (Rel-19) — Fault Management for Virtualized Mobile Networks
- **TS 28.520** (Rel-19) — PM for Virtualized Mobile Networks
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products

---

📖 **Anglický originál a plná specifikace:** [VNFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vnfc/)
