---
slug: "tpe"
url: "/mobilnisite/slovnik/tpe/"
type: "slovnik"
title: "TPE – Termination Point Encapsulation"
date: 2025-01-01
abbr: "TPE"
fullName: "Termination Point Encapsulation"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tpe/"
summary: "Termination Point Encapsulation (TPE) je koncept správy podle 3GPP pro abstrakci a reprezentaci koncových bodů logických nebo fyzických spojení v rámci modelu síťových zdrojů. Používá se v systémech p"
---

TPE je koncept správy podle 3GPP pro abstrakci a reprezentaci koncových bodů spojení v rámci modelu síťových zdrojů, používaný jednotně pro správu konfigurace, chyb a výkonu.

## Popis

Termination Point Encapsulation (TPE) je modelovací koncept definovaný v rámci architektury Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) podle 3GPP, konkrétně v kontextu Network Resource Model ([NRM](/mobilnisite/slovnik/nrm/)). Termination Point ([TP](/mobilnisite/slovnik/tp/)) představuje koncový bod logického nebo fyzického propojení, kde je poskytována konektivita, například port na přepínači, virtuální síťové rozhraní nebo konektor rádiové antény. TPE poskytuje standardizovaný způsob pro zapouzdření a popis těchto koncových bodů, včetně jejich atributů, schopností a vztahů k jiným spravovaným objektům.

Architektonicky je TPE realizován jako třída informačního objektu v rámci NRM, často děděná ze základní třídy Managed Function nebo Managed Element. Obsahuje atributy, které definují roli TP (např. zdroj nebo příjemce), jeho směrovost (vstup, výstup, obousměrný), asociovaný protokolový zásobník a jeho vazbu na fyzický hardware nebo virtualizované zdroje. U virtualizované síťové funkce ([VNF](/mobilnisite/slovnik/vnf/)) může TPE reprezentovat například virtuální síťovou kartu (vNIC) se specifickými vlastnostmi šířky pásma a latence. Systém správy, jako je Element Management System ([EMS](/mobilnisite/slovnik/ems/)) nebo Network Management System ([NMS](/mobilnisite/slovnik/nms/)), používá model TPE k objevování, konfiguraci, monitorování a řešení problémů s konektivitou.

Jak to funguje, zahrnuje integraci definic TPE do deskriptorů používaných pro onboarding síťových služeb a VNF, jako je VNF Descriptor (VNFD). Běží lifecycle management orchestrovaný [NFV](/mobilnisite/slovnik/nfv/) Orchestrátorem ([NFVO](/mobilnisite/slovnik/nfvo/)), vytváření instance VNF zahrnuje vytváření instancí jejích modelovaných koncových bodů a jejich propojení s dalšími TP v síti za účelem vytvoření servisních řetězců. TPE umožňuje jednotné rozhraní správy napříč heterogenním síťovým zařízením, ať už se jedná o fyzické síťové funkce (PNF) nebo VNF. Jeho role je klíčová pro automatizaci nasazování služeb a zajištění přesného splnění požadavků na konektivitu ve složitých, segmentovaných sítích.

## K čemu slouží

TPE bylo vytvořeno, aby řešilo výzvu správy koncových bodů konektivity v čím dál více softwarově definovaných a virtualizovaných sítích. Předchozí přístupy často používaly pro porty a rozhraní modely specifické pro dodavatele nebo zařízení, což činilo automatizované poskytování služeb a jejich zajištění napříč více dodavateli složitým a náchylným k chybám. TPE poskytuje společnou abstraktní vrstvu.

Problém, který řeší, je absence standardizovaného informačního modelu pro koncové body v rámci architektury správy podle 3GPP. S příchodem virtualizace síťových funkcí (NFV) a softwarově definovaných sítí (SDN) se sítě začaly skládat z dynamicky vytvářených funkcí s virtuálními propojeními. TPE jako součást standardizovaného NRM umožňuje systémům spráty tyto spoje jednotně chápat a ovládat, bez ohledu na to, zda je podřízená funkce fyzická nebo virtuální. To bylo motivováno potřebou agilního poskytování služeb a efektivního využívání zdrojů v sítích 5G a novějších, kde síťové segmentování vyžaduje přesnou kontrolu nad koncovými body konektivity pro každou instanci segmentu.

## Klíčové vlastnosti

- Standardizovaná abstrakce pro koncové body logických a fyzických spojení
- Definováno jako třída informačního objektu v rámci 3GPP Network Resource Model (NRM)
- Podporuje atributy pro roli, směr, protokol a vazbu na zdroje
- Zásadní pro modelování konektivity v deskriptorech VNF a síťových služeb
- Umožňuje automatizovanou konfiguraci a správu životního cyklu spojení
- Umožňuje jednotné monitorování chyb a výkonu koncových bodů

## Související pojmy

- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)

## Definující specifikace

- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model

---

📖 **Anglický originál a plná specifikace:** [TPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpe/)
