---
slug: "nm"
url: "/mobilnisite/slovnik/nm/"
type: "slovnik"
title: "NM – Network Management"
date: 2025-01-01
abbr: "NM"
fullName: "Network Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nm/"
summary: "Network Management (NM) zahrnuje funkce, architekturu a rozhraní pro provoz, správu, údržbu a provisioning telekomunikační sítě. V rámci 3GPP definuje standardizované principy pro správu chyb, konfigu"
---

NM (Network Management) je standardizovaná sada funkcí, architektury a rozhraní pro provoz, správu, údržbu a provisioning telekomunikační sítě založená na principech FCAPS, která umožňuje efektivní správu více dodavatelských sítí.

## Popis

V kontextu 3GPP se Network Management (NM) vztahuje k ucelenému rámci standardizovaných funkcionalit a rozhraní používaných pro správu systémů definovaných 3GPP, včetně Core Network (CN), Radio Access Network (RAN) a User Equipment (UE). Není to jediné centrum, ale vrstvená architektura a soubor procesů definovaných v mnoha technických specifikacích (TS), primárně v řadě 28 (Management and Orchestration), řadě 32 (Telecommunication management) a dalších. Rámec NM je založen na modelu FCAPS (Fault, Configuration, Accounting, Performance, and Security Management) a vrstveném modelu Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)).

Architektura typicky zahrnuje několik logických vrstev: Network Element ([NE](/mobilnisite/slovnik/ne/)) layer, Element Management ([EM](/mobilnisite/slovnik/em/)) layer a Network Management (NM) layer. Vrstva NM poskytuje pohled na síť end-to-end a spravuje více podsítí nebo domén. Komunikuje se systémy Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)) pod ní pomocí standardizovaných rozhraní, nejvýznamněji Itf-N (Northbound Interface) definovaných pomocí protokolů založených na [XML](/mobilnisite/slovnik/xml/). Mezi klíčové funkce správy patří sledování výkonu (sběr čítačů a měření pro [KPI](/mobilnisite/slovnik/kpi/)), správu chyb (monitorování alarmů a analýza příčin), správu konfigurace (správa softwaru, provisioning) a lifecycle management síťových služeb a řezů.

NM funguje prostřednictvím sady standardizovaných modelů Information Service ([IS](/mobilnisite/slovnik/is/)), které definují spravované objekty, jejich atributy a notifikace, které mohou generovat. Manažery (NM systémy) a agenti (EM systémy nebo NE) si vyměňují informace pomocí protokolů jako [CORBA](/mobilnisite/slovnik/corba/)/IDL ve starších vydáních a později přecházejí k RESTful API a YANG datovým modelům (např. pro 5G network resource model). Specifikace detailně popisují vše od požadavků (řada 32.1xx) až po protokolově specifická mapování (řada 32.3xx a 32.6xx). Tato rozsáhlá standardizace zajišťuje, že operátor může integrovat systémy správy od různých dodavatelů pro správu heterogenní síťové infrastruktury.

## K čemu slouží

Primárním účelem standardizace Network Management v 3GPP je umožnit provozní proveditelnost mobilních sítí od více dodavatelů. Bez společných rozhraní a informačních modelů pro správu by každý dodavatel síťových prvků poskytoval proprietární systémy správy, což by nutilo operátory používat desítky různých nástrojů pro provoz svých sítí. To by bylo enormně nákladné, neefektivní a náchylné k chybám. Standardizované NM tento problém řeší definicí toho, jak jsou informace pro správu modelovány a komunikovány, což umožňuje integrované, vyšší úrovně operational support systems (OSS).

Historicky se standardizace správy vyvinula z rámce ITU-T TMN. 3GPP tyto principy pro mobilní sítě přijalo a rozšířilo počínaje 3G (Release 99/4). Počáteční zaměření bylo na správu jádra s přepojováním okruhů a rádiové sítě. Jak se sítě stávaly složitějšími se zavedením jader založených na IP (IMS, EPC), služeb s přepojováním paketů a později virtualizovaných síťových funkcí, musel se rámec NM dramaticky vyvíjet. Řeší omezení oddělené, na dodavateli uzamčené správy tím, že poskytuje společný jazyk a soubor interakcí pro monitorování chyb, zajištění výkonu, softwarové aktualizace a konfiguraci – což je klíčové pro udržení kvality služeb, snížení provozních nákladů (OPEX) a umožnění nových provozních paradigmat, jako jsou self-organizing networks (SON) a automatizovaný lifecycle management pro network slicing v 5G.

## Klíčové vlastnosti

- Standardizované funkce správy podle FCAPS (Fault, Configuration, Accounting, Performance, Security)
- Vrstvená architektura založená na TMN (vrstvy NE, EM, NM)
- Definovaná rozhraní northbound (Itf-N) a southbound pro interoperabilitu více dodavatelů
- Komplexní modely Information Service (IS) pro spravované objekty
- Podpora sběru měření výkonu, monitorování alarmů a správy softwaru
- Vývoj směrem k modelově řízené správě (např. pomocí YANG) a podpora lifecycle managementu pro network slicing

## Související pojmy

- [EM – Electromagnetic Emanations](/mobilnisite/slovnik/em/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 28.302** (Rel-19) — LSA Controller IRP Management Operations
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 28.820** (Rel-12) — Umbrella Operation Model for Fixed Mobile Convergence
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- … a dalších 75 specifikací

---

📖 **Anglický originál a plná specifikace:** [NM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nm/)
