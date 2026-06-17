---
slug: "ces"
url: "/mobilnisite/slovnik/ces/"
type: "slovnik"
title: "CES – Cloud Enabler Server"
date: 2026-01-01
abbr: "CES"
fullName: "Cloud Enabler Server"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ces/"
summary: "Cloud Enabler Server (CES) je management entity definovaný ve 3GPP pro umožnění a správu cloud-nativních síťových funkcí a aplikací. Poskytuje standardizovaný rámec pro správu životního cyklu, orchest"
---

CES je management entity 3GPP, která umožňuje a spravuje cloud-nativní síťové funkce tím, že poskytuje standardizovaný rámec pro správu životního cyklu, orchestraci a vystavování schopností v cloudových sítích 5G a vyšších generací.

## Popis

Cloud Enabler Server (CES) je klíčová architektonická komponenta zavedená ve 3GPP Release 18 v rámci architektury 5G systému (5GS) a jeho evoluce. Funguje jako řídicí funkce, konkrétně navržená k překlenutí propasti mezi tradičními systémy pro správu sítí a cloud-nativními distribuovanými výpočetními prostředími. CES poskytuje sadu standardizovaných northbound aplikačních rozhraní ([API](/mobilnisite/slovnik/api/)) a southbound rozhraní pro usnadnění automatizovaného nasazení, konfigurace, škálování a ukončování síťových funkcí a aplikací zabalených jako kontejnery nebo virtuální stroje. Její primární úlohou je abstrahovat heterogenitu podkladové cloudové infrastruktury (např. od různých dodavatelů nebo napříč více datovými centry) a poskytovat jednotnou řídicí rovinu vyšším orchestračním systémům, jako je Network Function Virtualization Orchestrator ([NFVO](/mobilnisite/slovnik/nfvo/)) nebo framework Service Management and Orchestration (SMO).

Architektonicky je CES definován tak, aby komunikoval s několika klíčovými entitami. Na své northbound straně vystavuje služby správy spotřebitelům, jako je Management Data Analytics Function ([MDAF](/mobilnisite/slovnik/mdaf/)), Network Data Analytics Function (NWDAF) nebo poskytovatelé služeb třetích stran. Tato rozhraní, standardizovaná např. ve specifikacích 29.558, umožňují zřizování výpočetních, úložných a síťových prostředků, stejně jako vytváření instancí a správu životního cyklu úloh. Na své southbound straně komunikuje CES se systémy pro správu cloudové infrastruktury (CIMS), které mohou být založeny na platformách jako Kubernetes nebo OpenStack, aby provedla skutečné přidělení prostředků a plánování úloh na fyzické nebo virtualizované infrastruktuře. CES samotný může obsahovat dílčí funkce pro správu inventáře, vymáhání politik, správu chyb a monitorování výkonu a správu bezpečnostních přihlašovacích údajů pro spravované úlohy.

Z provozní perspektivy CES pracuje tak, že přijímá záměrové požadavky od spotřebitele služby správy. Například požadavek může specifikovat potřebu nasadit instanci User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) na konkrétní edge lokalitě s určitými zárukami výpočetního výkonu, latence a šířky pásma. CES přeloží tento vysokolehlý záměr do konkrétních akcí. Konzultuje své motory inventáře a politik, aby vybral vhodný hostitelský bod přítomnosti cloudové infrastruktury (např. centrální ústřednu nebo edge datové centrum). Poté komunikuje s místním CIMS v daném místě, aby rezervoval prostředky, stáhl potřebné kontejnerové image, nakonfiguroval síťování (potenciálně za účasti Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro síťové politiky) a konečně spustil úlohu. Během celého životního cyklu úlohy CES sleduje její stav a výkon, sbírá metriky a události, které může hlásit zpět spotřebiteli nebo použít k aktivaci automatického škálování nebo ozdravných akcí.

Její role v síti je klíčová pro umožnění pravých cloud-nativních principů v telekomunikacích. Poskytnutím standardizované, automatizované a na infrastruktuře nezávislé vrstvy správy CES snižuje závislost na dodavateli, urychluje nasazení služeb z týdnů na minuty a umožňuje efektivní využití prostředků prostřednictvím elastického škálování. Je základním enablerem pro síťové slicing, kde každý slice může vyžadovat jedinečnou sadu funkcí nasazených na vyžádání napříč sdílenou cloudovou infrastrukturou. Dále podporuje vizi distribuovaných výpočtů od jádra cloudu až po vzdálený edge, což umožňuje optimální umístění aplikací a síťových funkcí pro splnění přísných požadavků na latenci a šířku pásma u případů užití jako průmyslový IoT, rozšířená realita a autonomní vozidla.

## K čemu slouží

Cloud Enabler Server byl vytvořen, aby řešil významné provozní výzvy vznikající při přechodu mobilních sítí na cloud-nativní architektury. Před jeho standardizací byla správa virtualizovaných síťových funkcí (VNF) a cloud-nativních síťových funkcí ([CNF](/mobilnisite/slovnik/cnf/)) často řešena prostřednictvím proprietárních rozhraní a skriptů vázaných na konkrétní cloudové platformy (např. implementace OpenStack nebo Kubernetes konkrétního dodavatele). To vedlo k fragmentaci, vysokým integračním nákladům a neschopnosti automatizovat nasazení služeb napříč více dodavatelskými a multi-cloudovými prostředími. Absence společné abstraktní vrstvy správy bránila obratnosti slibované virtualizací síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a software-defined sítěmi, což operátorům ztěžovalo rychlé uvádění nových služeb nebo dynamické škálování prostředků v reakci na poptávku.

Historicky byla architektura správy 3GPP, soustředěná kolem Network Management System (NMS) a Element Management System (EMS), navržena pro fyzické síťové prvky s relativně statickými konfiguracemi. Dynamická, efemérní povaha kontejnerizovaných úloh v mikroslužbami založeném jádru 5G vyžadovala nový paradigma. CES byl motivován potřebou rozšířit managementový framework 3GPP tak, aby nativně podporoval cloudovou infrastrukturu. Řeší problém, jak jednotně spravovat životní cyklus softwarových úloh, které jsou základní pro systém 5G – jako je Access and Mobility Management Function (AMF), Session Management Function (SMF) a UPF – když jsou nasazeny nikoli jako monolitická zařízení, ale jako kolekce mikroslužeb, které lze nezávisle škálovat a aktualizovat.

Kromě toho vzestup edge computingu a síťového slicingu vytvořil další složitost. Nasazení instance síťového slicingu vyžaduje koordinované vytvoření více funkcí napříč potenciálně geograficky rozptýlenými cloudovými prostředky. Bez standardizované entity jako CES, která by fungovala jako jediný bod kontroly pro zřizování cloudových prostředků a správu úloh, by orchestrace slicingu byla nesmírně složitá a neinteroperabilní. CES tedy existuje, aby poskytla potřebnou spojnici mezi vrstvou orchestrace služeb/sítě a různorodou vrstvou cloudové infrastruktury, a umožnila tak automatizované, politikami řízené a efektivní naplnění vize 5G pro flexibilní a na službách založenou síťovou architekturu.

## Klíčové vlastnosti

- Standardizovaná northbound API pro správu životního cyklu úloh (zřizování, škálování, ukončování)
- Abstrakce heterogenní cloudové infrastruktury (např. různých distribucí Kubernetes, OpenStack) prostřednictvím southbound adaptérů
- Integrace s managementovými frameworky 3GPP jako Service Management and Orchestration (SMO) a Management Data Analytics Services (MDAS)
- Podpora záměrového managementu a automatického přidělování prostředků řízeného politikami
- Schopnosti pro správu inventáře, monitoring a správu chyb cloudových prostředků a hostovaných úloh
- Enabler pro automatizované nasazení a správu síťových slicingů napříč distribuovanými edge uzly cloudu

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [CNF – Conjunctive Normal Form](/mobilnisite/slovnik/cnf/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.558** (Rel-19) — Enabling Edge Applications

---

📖 **Anglický originál a plná specifikace:** [CES na 3GPP Explorer](https://3gpp-explorer.com/glossary/ces/)
