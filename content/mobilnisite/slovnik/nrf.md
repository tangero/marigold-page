---
slug: "nrf"
url: "/mobilnisite/slovnik/nrf/"
type: "slovnik"
title: "NRF – Network Resource Fulfilment"
date: 2026-01-01
abbr: "NRF"
fullName: "Network Resource Fulfilment"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nrf/"
summary: "Řídicí funkce 3GPP odpovědná za automatické zřizování, aktivaci a konfiguraci síťových prostředků a služeb. Je klíčovou součástí architektury řízení a orchestrace (MANO) a umožňuje efektivní životní c"
---

NRF je řídicí funkce 3GPP odpovědná za automatické zřizování, aktivaci a konfiguraci síťových prostředků a služeb v rámci MANO architektury.

## Popis

Network Resource Fulfilment (NRF) je klíčová řídicí funkce v rámci systému řízení 3GPP, konkrétně definovaná v architektuře řízení a orchestrace ([MANO](/mobilnisite/slovnik/mano/)) pro sítě 5G. Operuje ve vrstvách síťového řízení ([NM](/mobilnisite/slovnik/nm/)) a řízení prvků ([EM](/mobilnisite/slovnik/em/)) a komunikuje se síťovými funkcemi (NFs) a fyzickými/virtuálními prostředky. Funkce NRF je zodpovědná za provádění pracovních postupů nezbytných k realizaci instance služby nebo síťového řezu na základě požadavku na zřízení. To zahrnuje překlad požadavků na služby na vysoké úrovni (např. od Communication Service Management Function - CSMF) do podrobných a proveditelných konfiguračních příkazů pro podpůrné síťové prostředky, včetně výpočetních kapacit, úložišť, sítí a virtualizovaných (VNF) nebo kontejnerizovaných ([CNF](/mobilnisite/slovnik/cnf/)) síťových funkcí.

Z architektonického hlediska NRF spolupracuje s dalšími řídicími funkcemi, jako je Network Slice Subnet Management Function (NSSMF) a Network Function Management Function (NFMF). Když je potřeba vytvořit instanci síťového řezu, NSSMF dekomponuje požadavky na řez a vyvolá NRF, aby zajistil prostředky pro každou dílčí podsíť. NRF komunikuje se správci prostředků specifických pro daný typ (např. Virtualized Infrastructure Manager - VIM, WAN Infrastructure Manager - WIM) a správci [NF](/mobilnisite/slovnik/nf/) s cílem alokovat prostředky, instanciovat software, konfigurovat parametry a navázat konektivitu. Řídí se definovaným postupem zřizování, který může zahrnovat fáze validace, rezervace, aktivace, testování a zprovoznění. Proces je do značné míry závislý na deskriptorech a šablonách, jako jsou Network Service Descriptors (NSD) a Virtual Network Function Descriptors (VNFD), které definují požadavky na prostředky a skripty pro životní cyklus.

Jak to funguje, zahrnuje sekvenci orchestračních kroků. Po přijetí požadavku na zřízení NRF nejprve provede kontrolu přijatelnosti a dostupnosti prostředků proti inventáři. Poté spustí správce prostředků k alokaci potřebných virtuálních strojů, kontejnerů, svazků úložiště a síťových propojení. U síťových funkcí instruuje NFMF k vytvoření instance VNF/CNF s použitím příslušného balíčku z katalogu. NRF koordinuje konfiguraci těchto prostředků, zajišťuje nastavení IP adres, směrovacích politik, bezpečnostních skupin a parametrů specifických pro funkci podle plánu služby. Monitoruje proces zřizování a řeší případné chyby pomocí postupů návratu. Jakmile jsou všechny prostředky zřízeny a nakonfigurovány, NRF aktualizuje síťový inventář a upozorní volající řídicí funkci, že služba nebo řez jsou připraveny k provozu. Tato automatizace je klíčová pro podporu dynamického, na požádání poskytovaného síťového řezování a nasazování služeb.

## K čemu slouží

Funkce Network Resource Fulfilment byla zavedena k řešení značné provozní složitosti moderních telekomunikačních sítí, zejména s nástupem 5G, síťového řezování a cloud-nativních principů. Tradiční zřizování sítě bylo z velké části manuální, řízené příkazovým řádkem a pomalé, což znemožňovalo uspokojit požadavky na rychlou inovaci služeb, elasticitu a přizpůsobené řezy pro vertikální odvětví. NRF automatizuje tento životní cyklus zřizování a řeší tak problém škálování síťových operací v softwarově definovaném a virtualizovaném prostředí.

Historicky byla každá síťová komponenta konfigurována nezávisle. Přechod k virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a softwarově definovaným sítím (SDN) vytvořil disintegrovanou, flexibilní infrastrukturu, ale také problém s jejím řízením. NRF jako součást sladěného řídicího rámce 3GPP (navazujícího na koncepty [ETSI](/mobilnisite/slovnik/etsi/) NFV [MANO](/mobilnisite/slovnik/mano/)) poskytuje standardizované, na dodavateli nezávislé rozhraní a proces pro automatizaci komplexního zřizování kompozitních síťových služeb. Odstraňuje omezení izolovaných řídicích systémů pro konkrétní prvky, které nedokázaly koordinovat napříč výpočetními, síťovými a aplikačními vrstvami.

Vytvoření NRF bylo motivováno obchodní potřebou správy služeb a řezů bez manuálního zásahu. Operátoři potřebují schopnost nasadit nový řez pro podnikového zákazníka v řádu minut, nikoli měsíců. NRF to umožňuje tím, že poskytuje automatizovaný workflow engine, který překládá zákaznicky orientovanou objednávku služby v technickou realitu. Je zásadní pro dosažení vize 5G 'network-as-a-service', která umožňuje operátorům efektivně využívat své sdružené prostředky a rychle reagovat na tržní příležitosti při současném snížení provozních nákladů a lidských chyb.

## Klíčové vlastnosti

- Orchestruje automatické zřizování a aktivaci virtuálních/fyzických síťových prostředků
- Provádí postupy zřizování na základě plánů síťových služeb nebo řezů (NSD)
- Koordinuje se správci infrastruktury (VIM/WIM) a správci síťových funkcí (NFMF)
- Podporuje akce správy životního cyklu: vytváření instancí, škálování, ukončování, aktualizace
- Provádí kontrolu přijatelnosti prostředků a udržuje synchronizaci s inventářem prostředků
- Umožňuje uzavřenou smyčku řízení tím, že poskytuje data o zřizování funkcím správy kvality provozu

## Související pojmy

- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 26.532** (Rel-19) — 5G Data Collection and Reporting API Specification
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TR 28.840** (Rel-18) — Technical Report
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [NRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrf/)
