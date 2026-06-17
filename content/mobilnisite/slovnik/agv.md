---
slug: "agv"
url: "/mobilnisite/slovnik/agv/"
type: "slovnik"
title: "AGV – Automated Guided Vehicles"
date: 2025-01-01
abbr: "AGV"
fullName: "Automated Guided Vehicles"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/agv/"
summary: "Automated Guided Vehicles (AGV) jsou bezobslužné mobilní roboty používané v průmyslové automatizaci pro manipulaci s materiálem a logistiku. V kontextu 3GPP představují klíčový případ užití pro 5G a d"
---

AGV je bezobslužný mobilní robot používaný v průmyslové automatizaci, který představuje klíčový případ užití 5G vyžadující ultra-spolehlivou komunikaci s nízkou latencí a přesné určování polohy pro manipulaci s materiálem v chytrých továrnách.

## Popis

Automated Guided Vehicles (AGV) jsou autonomní, programovatelná vozidla, která přepravují materiál, komponenty nebo hotové výrobky v řízeném prostředí, jako je výrobní hala, sklad nebo logistické centrum, bez nutnosti lidského obsluhy. V kontextu norem 3GPP nejsou AGV konkrétním protokolem nebo síťovým prvkem, ale představují zásadní případ užití průmyslového internetu věcí (IIoT), který pohání požadavky na buněčné systémy 5G a 6G. Normalizační práce definuje požadavky na komunikaci a služby nezbytné pro spolehlivou a bezpečnou podporu flotil AGV přes bezdrátové sítě.

Z pohledu síťové architektury zahrnuje podpora AGV spolupráci více komponent systému 3GPP. Samotné AGV funguje jako uživatelské zařízení (UE) s rozšířenými schopnostmi. Připojuje se přes rozhraní 5G New Radio (NR) ke gNB v rádiové přístupové síti (RAN). Jádrová síť, konkrétně 5G Core (5GC), musí podporovat kritické funkce, jako je Ultra-Reliable Low-Latency Communication (URLLC), prostřednictvím své architektury založené na službách. Mezi klíčové síťové funkce zapojené do podpory patří Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) pro registraci a mobilitu, Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro správu PDU relací přenášejících řídicí a senzorová data AGV a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která zajišťuje přeposílání dat s nízkou latencí a vysokou spolehlivostí. Pro pokročilou koordinaci může Application Function ([AF](/mobilnisite/slovnik/af/)) interagovat se systémem pro správu flotily AGV umístěným v lokální edge výpočetní platformě (Multi-access Edge Computing - [MEC](/mobilnisite/slovnik/mec/)) za účelem minimalizace latence.

Technické fungování se točí kolem splnění přísných klíčových výkonnostních ukazatelů ([KPI](/mobilnisite/slovnik/kpi/)). Provoz AGV závisí na nepřetržité výměně dat v reálném čase. To zahrnuje telemetrická data (poloha, rychlost, stav baterie) odesílaná z AGV do centrálního řídicího systému a příkazová data (navigační instrukce, úpravy rychlosti, nouzová zastavení) odesílaná z řídicího systému na AGV. Specifikace 3GPP, jako je TR 22.804, definují požadavky, jako je koncová latence až 1-10 milisekund, spolehlivost až 99,9999 % a dostupnost až 99,99 % pro kritické řídicí smyčky. Dále je nezbytné přesné určování polohy. 3GPP vylepšilo techniky určování polohy v NR, včetně měření času zpátečního průchodu (RTT) přes více buněk, určení úhlu příchodu (AoA) a určování polohy asistovaného přes sidelink, aby dosáhlo přesnosti na úrovni pod metr nebo dokonce centimetrů pro navigaci AGV a vyhýbání se kolizím.

Role AGV v ekosystému 3GPP spočívá v ověření a posouvání hranic buněčné technologie pro vertikální průmyslová odvětví. Slouží jako měřítko pro průmyslový internet věcí (IIoT) a 'továrnu budoucnosti'. Podpora AGV demonstruje schopnost sítě nahradit tradiční průmyslové kabelové sítě (jako PROFINET nebo EtherCAT) bezdrátovou konektivitou, což nabízí větší flexibilitu v uspořádání továrny a umožňuje dynamické výrobní linky. Práce zahrnuje nejen fyzickou a spojovou vrstvu, ale také aspekty vyšších vrstev, jako je integrace Time-Sensitive Networking (TSN) pro deterministickou komunikaci, automatizace sítě pro rychlou rekonfiguraci tras AGV a vylepšené bezpečnostní mechanismy pro ochranu před kyberneticko-fyzickými útoky v průmyslovém prostředí.

## K čemu slouží

Účelem standardizace podpory pro Automated Guided Vehicles (AGV) v rámci 3GPP je umožnit buněčným sítím, konkrétně 5G a dalším generacím, aby sloužily jako jednotná bezdrátová komunikační infrastruktura pro pokročilou průmyslovou automatizaci. Před érou 5G průmyslová AGV obvykle spoléhala na nebuněčné technologie, jako je Wi-Fi, infračervené navádění, magnetická páska nebo proprietární bezdrátové systémy. Tato řešení často trpěla omezeními v spolehlivosti, škálovatelnosti, výkonu při předávání spojení a pokrytí, zejména ve velkých, složitých nebo kovových prostředích běžných v továrnách. Nemohla garantovat přísné požadavky na latenci a spolehlivost vyžadované pro bezpečnostně kritické řízení pohybu a koordinaci v reálném čase mezi více AGV.

Motivace 3GPP pro řešení AGV vychází ze strategické iniciativy rozšíření 5G na nové vertikální trhy mimo vylepšené mobilní širokopásmové připojení. Průmyslový sektor s jeho tlakem na Průmysl 4.0 a chytré výrobní procesy představoval významnou příležitost. AGV jsou základem flexibilní, automatizované logistiky. Definováním přesných požadavků na služby (např. v TR 22.804) a vývojem potřebných technologií v RAN a jádrové síti si 3GPP klade za cíl poskytnout standardizovanou, vysoce výkonnou a bezpečnou bezdrátovou alternativu. Tím se řeší problém fragmentace infrastruktury a umožňuje se výrobcům rychle nasazovat a přemisťovat flotily AGV, aniž by je omezovaly fyzické naváděcí dráhy nebo nespolehlivé bezdrátové spoje.

Historicky byl vznik URLLC jako klíčového pilíře 5G výrazně ovlivněn případy užití, jako jsou AGV a dálkové ovládání. Omezení předchozích generací buněčných sítí (4G LTE) z hlediska latence (typicky >20 ms) a hustoty spojení je činila nevhodnými pro tak náročné aplikace. Účelem pracovní položky týkající se AGV je tedy konkrétně specifikovat, co znamená 'ultra-spolehlivá' a 'nízká latence' v praktickém průmyslovém scénáři, a vést vývoj funkcí NR – jako jsou mini-sloty, grant-free uplink, redundantní přenosové cesty a vylepšené plánování – které společně splňují tyto ambiciózní cíle. Překlenuje tak propast mezi obecnými síťovými schopnostmi a konkrétními, bezpečnostně kritickými průmyslovými aplikacemi.

## Klíčové vlastnosti

- Požadavek na ultra-spolehlivou komunikaci s nízkou latencí (URLLC) se spolehlivostí 99,9999 % a latencí <10 ms
- Závislost na službách určování polohy s vysokou přesností (na úrovni pod metr až centimetrů) pro navigaci a vyhýbání se kolizím
- Podpora koordinovaných operací flotil více AGV vyžadujících komunikaci mezi zařízeními (sidelink)
- Integrace s Time-Sensitive Networking (TSN) pro deterministickou výměnu dat přes systémy 5G
- Schopnost řízené mobility sítí a plynulého předávání spojení v hustém průmyslovém prostředí
- Vylepšené bezpečnostní mechanismy pro ochranu kritických řídicích příkazů a senzorových dat

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 38.859** (Rel-18) — Technical Report
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [AGV na 3GPP Explorer](https://3gpp-explorer.com/glossary/agv/)
