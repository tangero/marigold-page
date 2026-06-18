---
slug: "iab-mt"
url: "/mobilnisite/slovnik/iab-mt/"
type: "slovnik"
title: "IAB-MT – Integrated Access and Backhaul Mobile Termination"
date: 2025-01-01
abbr: "IAB-MT"
fullName: "Integrated Access and Backhaul Mobile Termination"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iab-mt/"
summary: "Funkce mobilního zakončení (Mobile Termination) v rámci IAB uzlu, která mu umožňuje bezdrátově se připojit k nadřazenému uzlu stejným způsobem jako uživatelské zařízení (UE). Je klíčovou součástí pro"
---

IAB-MT je funkce mobilního zakončení (Mobile Termination) v rámci IAB uzlu, která mu umožňuje bezdrátově se připojit k nadřazenému uzlu, podobně jako uživatelské zařízení, pro účely vlastního přenosu (self-backhauling) v 5G sítích.

## Popis

IAB-MT (Integrated Access and Backhaul Mobile Termination) je základní komponenta architektury [IAB](/mobilnisite/slovnik/iab/) definované 3GPP a zavedené ve vydání Release 16. Představuje stranu „uživatelského zařízení“ IAB uzlu. Funkčně je IAB-MT logickou entitou, která navazuje a udržuje bezdrátové připojení k nadřazenému uzlu, kterým může být jiný IAB uzel nebo dárce gNB (gNB-DU). Toto připojení tvoří bezdrátový přenosový (backhaul) spoj, přenášející signalizaci řídicí roviny i data uživatelské roviny jak pro samotný IAB uzel, tak pro všechny podřízené uzly nebo UEs, které obsluhuje. IAB-MT funguje podle standardních specifikací rozhraní NR Uu, což znamená, že používá stejnou fyzickou vrstvu (jak je definováno v 38.211), protokoly vrstvy 2 a procedury [RRC](/mobilnisite/slovnik/rrc/) (jak v 38.331) jako konvenční 5G UE. Toto konstrukční řešení maximalizuje opětovné využití stávající funkčnosti UE a zajišťuje spolehlivé, standardizované připojení pro přenosovou část.

Architektonicky se IAB uzel skládá ze dvou hlavních funkčních částí: IAB-MT a [IAB-DU](/mobilnisite/slovnik/iab-du/) (Distributed Unit). IAB-MT je zodpovědná za bezdrátový přenosový uplink, zatímco IAB-DU poskytuje funkčnost přístupové sítě pro obsluhu koncových uživatelských UEs nebo podřízených IAB uzlů prostřednictvím rozhraní NR Uu. IAB-MT a IAB-DU v rámci stejného uzlu jsou koordinovány adaptační vrstvou specifickou pro IAB a jsou spravovány centrální IAB-donor [CU](/mobilnisite/slovnik/cu/) (Centralized Unit). Tato rozdělená architektura umožňuje efektivní alokaci zdrojů a správu topologie. Provoz IAB-MT je těsně integrován s plánováním IAB-DU za účelem správy časového ([TDM](/mobilnisite/slovnik/tdm/)) nebo prostorového multiplexování mezi přenosovými a přístupovými spoji, čímž se předchází vlastnímu rušení a optimalizuje se spektrální účinnost.

Role IAB-MT je klíčová pro umožnění sítí s vlastním přenosem. Umožňuje operátorovi nasadit síťový uzel tam, kde optická vlákna nejsou dostupná nebo jsou příliš nákladná, tím, že se uzel sám „bezdrátově připojí“ do sítě. IAB-MT podporuje agregaci nosných, duální konektivitu a provoz v kmitočtových pásmech FR1 i FR2, jak je specifikováno v příslušných specifikacích [RF](/mobilnisite/slovnik/rf/) výkonu (38.174, 38.176). Její výkon přímo ovlivňuje kapacitu a latenci více-skokového přenosového řetězce. Mezi klíčové procedury zahrnující IAB-MT patří počáteční přístup a navázání spojení s nadřazeným uzlem, rekonfigurace RRC pro mobilitu (např. změna nadřazené buňky) a zpracování směrovacích identifikátorů adaptační vrstvy pro přenos ([BAP](/mobilnisite/slovnik/bap/)) pro správné směrování paketů topologií IAB.

## K čemu slouží

IAB-MT byla vytvořena, aby vyřešila problém nasazení hustých 5G sítí, zejména v milimetrových pásmech (mmWave), kde je šíření signálu omezené a instalace optických vláken je pro každou lokalitu buňky neúměrně nákladná. Tradiční sítě vyžadují optické připojení ke každé základnové stanici pro přenosovou část, což je hlavní překážkou pro rychlé a nákladově efektivní nasazení. Účelem IAB-MT je přeměnit síťový uzel na přenosový uzel (relay), což mu umožní připojit se k jádru sítě bezdrátově prostřednictvím více-skokové sítě podobných uzlů. To operátorům umožňuje rozšířit pokrytí a kapacitu do nových oblastí – jako jsou městské kaňony, vnitřní prostory nebo dočasná místa konání akcí – na základě počátečního ukotvení připojeného optickými vlákny (dárce).

Historicky podobné koncepty existovaly v LTE (Relay Nodes), ale nebyly plně integrovány do architektury RAN. Architektura 5G [IAB](/mobilnisite/slovnik/iab/) s IAB-MT jako klíčovou součástí je nativní, flexibilnější a škálovatelnější řešení. Řeší problém zahušťování sítě tím, že odděluje potřebu optických vláken od potřeby rádiového pokrytí. IAB-MT konkrétně řeší problém, jak se přenosový uzel integruje do sítě jako rovnocenný prvek. Tím, že se chová jako standardní UE pro své připojení směrem vzhůru, využívá všechny stávající mechanismy mobility, zabezpečení a správy rádiových zdrojů 5G NR, čímž zajišťuje robustní a řiditelné přenosové spoje. Toto řešení bylo motivováno snahou průmyslu o agilnější a snadněji nasaditelné sítě pro 5G a další generace.

## Klíčové vlastnosti

- Funguje jako standardní NR UE pro přenosové připojení využívající rozhraní Uu
- Umožňuje bezdrátový vlastní přenos (self-backhauling), čímž snižuje závislost na infrastruktuře z optických vláken
- Podporuje provoz v kmitočtových pásmech FR1 (pod 6 GHz) i FR2 (mmWave)
- Integruje se s IAB-DU v rámci stejného uzlu pro koordinovaný provoz s TDM/SDM
- Využívá protokol adaptační vrstvy pro přenos (BAP) pro směrování v topologiích s více skoky
- Podporuje procedury mobility, jako je změna nadřazeného uzlu, pro robustnost topologie

## Související pojmy

- [IAB-DU – IAB Distributed Unit](/mobilnisite/slovnik/iab-du/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.420** (Rel-19) — Introduction to Xn interface specifications
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background

---

📖 **Anglický originál a plná specifikace:** [IAB-MT na 3GPP Explorer](https://3gpp-explorer.com/glossary/iab-mt/)
