---
slug: "nfv"
url: "/mobilnisite/slovnik/nfv/"
type: "slovnik"
title: "NFV – Network Functions Virtualization"
date: 2026-01-01
abbr: "NFV"
fullName: "Network Functions Virtualization"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nfv/"
summary: "Paradigma síťové architektury, které odděluje síťové funkce (jako firewally, load balancery nebo uzly EPC/5GC) od proprietárních hardwarových zařízení. Tyto funkce jsou implementovány jako softwarové"
---

NFV je paradigma síťové architektury, které odděluje síťové funkce od proprietárního hardwaru tím, že je implementuje jako softwarové instance na komerčních serverech, což umožňuje agilitu, škálovatelnost a snížení nákladů.

## Popis

Virtualizace síťových funkcí (NFV) je transformační architektonický rámec pro telekomunikační sítě, který nahrazuje vyhrazená proprietární hardwarová zařízení softwarovými virtualizovanými instancemi běžícími na standardizovaných serverech, přepínačích a úložištích velkých objemů. Síťová funkce ([NF](/mobilnisite/slovnik/nf/)), což je funkční blok v síťové infrastruktuře (např. Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) nebo firewall), je implementována jako virtuální síťová funkce ([VNF](/mobilnisite/slovnik/vnf/)). Tento softwarový VNF je nasazen na virtualizované infrastruktuře, typicky spravované hypervizorem nebo platformou pro orchestraci kontejnerů, jako je Kubernetes, která abstrahuje základní výpočetní, úložné a síťové prostředky.

Architektura NFV, jak je standardizována [ETSI](/mobilnisite/slovnik/etsi/) a přijata 3GPP, se skládá ze tří hlavních vrstev. Za prvé, infrastruktura NFV ([NFVI](/mobilnisite/slovnik/nfvi/)) poskytuje virtualizované prostředky – virtuální výpočetní výkon, virtuální úložiště a virtuální sítě – sdružené z fyzického hardwaru [COTS](/mobilnisite/slovnik/cots/). Za druhé, virtuální síťové funkce (VNF) jsou softwarové implementace síťových funkcí, které tyto virtuální prostředky spotřebovávají. Za třetí, framework pro správu a orchestraci NFV ([MANO](/mobilnisite/slovnik/mano/)) je mozkem celé operace. MANO zahrnuje správce virtualizované infrastruktury (VIM, např. OpenStack), který řídí NFVI; správce VNF (VNFM), který zajišťuje životní cyklus (instanciaci, škálování, ukončení) jednotlivých VNF; a orchestrátor NFV (NFVO), který orchestruje prostředky a služby napříč více VNF za účelem vytvoření koncových síťových služeb.

Jak to funguje, zahrnuje orchestraci těchto komponent. Když je vyžadována nová síťová služba (např. nasazení slicu pro nového podnikového zákazníka), NFVO obdrží požadavek a konzultuje katalog dostupných VNF a deskriptorů síťových služeb. Poté nařídí VIM přidělit potřebné virtuální prostředky (VM nebo kontejnery) z fondu NFVI. Následně dá pokyn příslušným VNFM, aby na těchto prostředcích instancovaly a nakonfigurovaly požadované VNF (např. UPF a AMF), a nakonec mezi nimi vytvoří virtuální síťové spoje. Celý tento proces je automatizovaný, což umožňuje rychlé nasazení služeb, elastické škálování na základě zatížení a efektivní využití prostředků. V 5G jádru (5GC) od 3GPP je koncept cloud-nativních síťových funkcí (CNF), často implementovaných jako kontejnery a v souladu s principy NFV, základním pilířem, díky čemuž je jádrová síť agilní a službově orientovaná.

## K čemu slouží

NFV bylo vytvořeno, aby řešilo kritickou neefektivitu tradičních telekomunikačních sítí, které byly postaveny na vertikálně integrovaných, proprietárních hardwarových zařízeních od jediného dodavatele. Tento model vedl k dlouhým inovačním cyklům (vývoj hardwaru trvá roky), vysokým kapitálovým a provozním nákladům (energie, prostor, chlazení pro mnoho zařízení) a silné závislosti na dodavateli. Hlavní problém, který NFV řeší, je tato nepružnost; operátorům ztěžuje rychlé uvedení nových služeb nebo efektivní škálování stávajících v reakci na tržní poptávku, jako je exploze dat způsobená smartphony a IoT.

Historická motivace pro NFV vznikla kolem roku 2012 z konsorcia telekomunikačních operátorů, které publikovalo white paper nastiňující tuto vizi. Inspirovali se agilitou a úsporami z rozsahu pozorovanými v IT cloudových datových centrech. Cílem bylo využít standardní IT virtualizační technologie ke konsolidaci mnoha typů síťových zařízení na průmyslové standardní servery, přepínače a úložiště, které mohou být umístěny v datových centrech, síťových uzlech nebo na hraně sítě. Tento posun sliboval snížení nákladů, zrychlení uvedení nových služeb na trh a podporu živějšího více-dodavatelského ekosystému. NFV přímo umožňuje klíčové koncepty 5G, jako je síťové dělení (network slicing) a edge computing, tím, že poskytuje potřebnou elasticitu infrastruktury a automatizaci pro instanciaci a správu logických sítí a funkcí na vyžádání.

## Klíčové vlastnosti

- Odděluje software (VNF/CNF) od hardwaru, běží na serverech COTS
- Využívá framework pro správu a orchestraci (MANO) pro automatizovanou správu životního cyklu
- Umožňuje elastické škálování (horizontální/vertikální) síťových funkcí na základě poptávky
- Podporuje řetězení služeb (service chaining) pro dynamické propojování VNF za účelem vytvoření komplexních síťových služeb
- Usnadňuje multi-tenancy a sdružování prostředků pro lepší využití infrastruktury
- Poskytuje základnu pro cloud-nativní, agilní síťové architektury, jako je 5G Core (5GC)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TS 32.103** (Rel-19) — 3GPP Management IRP Overview
- **TS 32.426** (Rel-19) — EPC Performance Measurements Specification
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [NFV na 3GPP Explorer](https://3gpp-explorer.com/glossary/nfv/)
