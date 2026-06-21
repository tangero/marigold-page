---
slug: "chf"
url: "/mobilnisite/slovnik/chf/"
type: "slovnik"
title: "CHF – Charging Function"
date: 2026-01-01
abbr: "CHF"
fullName: "Charging Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/chf/"
summary: "Charging Function (CHF, Účtovací funkce) je základní komponenta jádra sítě v systémech 5G odpovědná za generování a správu záznamů o účtování (CDR) za využití sítě. Operátorům umožňuje implementovat f"
infografika: "/assets/slovnik/chf.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním CHF"
---

CHF je základní komponenta jádra sítě v systémech 5G odpovědná za generování a správu záznamů o účtování za využití sítě, což umožňuje flexibilní modely účtování pro služby jako hlas, data a síťové řezy.

## Popis

Charging Function (CHF, Účtovací funkce) je základní komponenta v architektuře 5G Core Network (5GC), konkrétně součást rámce účtování. Funguje jako producent účtovacích událostí a komunikuje s dalšími síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), prostřednictvím rozhraní služebního typu (např. Nchf). CHF je odpovědná za sběr informací o využití, aplikaci účtovacích politik a generování záznamů o účtování ([CDR](/mobilnisite/slovnik/cdr/)) nebo účtovacích událostí. Tyto záznamy jsou následně předávány funkci Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) pro dlouhodobé uložení a následné zpracování fakturačním systémem.

Architektonicky je CHF definována jako samostatná síťová funkce, kterou lze nasadit nezávisle a která podporuje režimy účtování offline i online. V režimu online účtování provádí kontrolu kreditu v reálném čase a přiděluje nebo zamítá služební jednotky na základě stavu účtu uživatele a pravidel politik. To zahrnuje přímou interakci se systémem správy zůstatků uživatele. Pro offline účtování shromažďuje data o využití po poskytnutí služby a koreluje události z více NF za účelem vytvoření konsolidovaných CDR. CHF podporuje konvergovaný účtovací systém, což znamená, že může prostřednictvím jednotného rámce zpracovávat účtování za jakýkoli typ služby (např. data, hlas, IoT, síťové řezy).

Klíčovými komponentami fungování CHF jsou Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)), která je logicky zabudována v jiných NF (např. SMF) za účelem detekce zpoplatnitelných událostí, a Charging Data Function (CDF) pro ukládání záznamů. Samotná CHF implementuje účtovací logiku, určuje doby tarifů, aplikuje rating a spravuje kvóty. Používá standardizované referenční body jako Nchf (pro služební komunikaci s ostatními NF) a Rf/Ga (pro případné použití starších rozhraní pro offline/online účtování). Její návrh je vysoce flexibilní a podporuje účtování založené na událostech, relacích a objemu dat, což je zásadní pro různorodou nabídku služeb 5G, jako jsou síťové řezy a edge computing.

Role CHF je klíčová pro monetizaci služeb 5G. Operátorům umožňuje implementovat sofistikované strategie účtování v reálném čase, jako je dynamické cenotvorba, účtování založené na QoS a fakturace specifická pro konkrétní síťový řez. Oddělením účtování od správy relací umožňuje 5G agilnější nasazování služeb a inovativní obchodní modely, včetně účtování služeb třetích stran. CHF zajišťuje, že veškeré využití síťových zdrojů je přesně měřeno, ohodnoceno a zaznamenáno, čímž vytváří základ pro zajištění výnosů a fakturaci zákazníkům v moderních telekomunikačních sítích.

## K čemu slouží

CHF byla zavedena ve specifikaci 3GPP Release 15 jako součást nové architektury 5G Core (5GC) za účelem překonání omezení předchozích účtovacích systémů v 4G EPC. V 4G bylo účtování pevně svázáno s konkrétními síťovými elementy, jako je [PGW](/mobilnisite/slovnik/pgw/) (prostřednictvím rozhraní Gy/Gz), což jej činilo nepružným a obtížně přizpůsobitelným novým službám. Architektura účtování 4G byla primárně navržena pro tradiční mobilní broadband a nedokázala uspokojivě řešit požadavky na účtování v reálném čase s diferenciací služeb, které vyžadují IoT, síťové řezy a edge služby.

Hlavní motivací pro vytvoření dedikované CHF bylo umožnění konvergovaného, služebního účtovacího rámce, který by dokázal podporovat různorodé use case slibované 5G. Toto oddělení umožňuje aplikovat účtovací logiku nezávisle na podkladové síťové topologii nebo stavu relace, což usnadňuje inovace. Řeší problém monolitických účtovacích systémů tím, že poskytuje modulární, cloud-nativní [NF](/mobilnisite/slovnik/nf/), která může dynamicky škálovat a integrovat se s moderními IT systémy prostřednictvím API.

Historicky se účtování vyvinulo z jednoduchých záznamů o hovorech v sítích s přepojováním okruhů ke složitějšímu datovému účtování v sítích s přepojováním paketů. CHF představuje další krok, navržený pro softwarově definované, službami orientované jádro sítě. Řeší potřebu účtování v reálném čase pro služby na vyžádání, podporu síťových řezů, kde každý řez může mít jiný model účtování, a schopnost účtovat služby a aplikace třetích stran přímo prostřednictvím sítě. To umožňuje nové zdroje příjmů a obchodní modely nezbytné pro ekonomickou životaschopnost 5G.

## Klíčové vlastnosti

- Konvergované účtování pro všechny typy služeb (data, hlas, IoT, síťové řezy)
- Podpora režimů účtování Online (OCS) i Offline (OFCS)
- Architektura založená na službách (SBA) s rozhraním Nchf
- Řízení kreditu a správa kvót v reálném čase
- Flexibilní účtovací triggery a korelace událostí
- Integrace s řízením politik pro vynucování účtovacích pravidel

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- **TS 28.203** (Rel-18) — Charging management
- **TS 28.204** (Rel-18) — Charging management
- **TR 28.815** (Rel-17) — Charging Study for Edge Computing
- **TR 28.816** (Rel-17) — Charging for 5G Cellular IoT
- **TR 28.822** (Rel-17) — Charging for 5G LAN Services Study
- **TR 28.827** (Rel-18) — Technical Report on 5G Charging for Roaming Scenarios
- **TR 28.840** (Rel-18) — Technical Report
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [CHF na 3GPP Explorer](https://3gpp-explorer.com/glossary/chf/)
