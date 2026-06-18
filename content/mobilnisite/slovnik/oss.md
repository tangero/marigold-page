---
slug: "oss"
url: "/mobilnisite/slovnik/oss/"
type: "slovnik"
title: "OSS – Operations and Supervisory System"
date: 2025-01-01
abbr: "OSS"
fullName: "Operations and Supervisory System"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/oss/"
summary: "Systém pro správu provozu sítě, závad, konfigurace, účtování, výkonu a zabezpečení (FCAPS). Umožňuje poskytovatelům služeb monitorovat, řídit a optimalizovat síťové prvky a služby, čímž zajišťuje spol"
---

OSS (Operations and Supervisory System) je systém pro správu provozu sítě, který umožňuje poskytovatelům služeb monitorovat, řídit a optimalizovat síťové prvky a služby.

## Popis

Operations and Supervisory System (OSS) je komplexní sada aplikací a platforem tvořících provozní páteř telekomunikační sítě. Je zodpovědný za správu síťových prvků (NEs) a jimi poskytovaných služeb v souladu s modelem FCAPS (Fault, Configuration, Accounting, Performance, Security). Architektonicky se OSS typicky nachází ve vrstvě správy sítě a komunikuje se síťovými prvky prostřednictvím standardizovaných rozhraní, jako je Itf-N (Interface-Northbound), nebo využívá protokoly jako [SNMP](/mobilnisite/slovnik/snmp/), [CORBA](/mobilnisite/slovnik/corba/) či NETCONF/YANG v modernějších implementacích. Shromažďuje data ze sítě, zpracovává je a prezentuje je operátorům sítě prostřednictvím rozhraní pro správu, což umožňuje centralizované řízení.

Jádro OSS tvoří několik klíčových subsystémů. Systém správy závad (Fault Management) nepřetržitě monitoruje síť na výskyt alarmů a událostí, provádí analýzu hlavní příčiny a spouští nápravné akce nebo záznamy o poruše. Správa konfigurace (Configuration Management) se zabývá zřizováním a správou životního cyklu síťových prostředků, včetně aktualizací softwaru a změn parametrů. Správa výkonu (Performance Management) shromažďuje a analyzuje klíčové ukazatele výkonu (KPIs) a metriky kvality služby (QoS) pro posouzení stavu a kapacity sítě. Správa účtování (Accounting Management) sleduje využití prostředků pro účely fakturace a účtování, zatímco správa zabezpečení (Security Management) vynucuje bezpečnostní politiky, monitoruje hrozby a spravuje přístupová oprávnění.

V ekosystému 3GPP OSS komunikuje s různými síťovými doménami, včetně jádra sítě (CN) a rádiové přístupové sítě (RAN). Spravuje entity jako Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G a jejich protějšky v 5G ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)). Pro RAN spravuje NodeB, eNodeB a gNB. OSS hraje klíčovou roli v zajišťování služeb (service assurance), umožňuje operátorům dodržovat smlouvy o úrovni služeb (SLAs), plánovat rozšíření sítě a automatizovat rutinní provozní úlohy, čímž snižuje provozní výdaje (OPEX) a minimalizuje prostoje.

## K čemu slouží

OSS byl vytvořen pro řešení rostoucí složitosti telekomunikačních sítí, které se staly nezvladatelnými pomocí ruční správy prvek po prvku. Před standardizovaným OSS se operátoři spoléhali na proprietární, na dodavatele specifické nástroje pro správu, což vedlo k provozním izolacím, vysokým nákladům na integraci a neefektivním procesům. Rozmach síťových technologií (2G, 3G, 4G, 5G) a rostoucí poptávka po různorodých službách si vyžádaly jednotný, standardizovaný přístup k provozu sítě.

3GPP standardizovalo OSS, aby poskytlo společný rámec pro správu sítí s více dodavateli a technologiemi. Tato standardizace řeší kritické problémy, jako je interoperabilita mezi systémy správy a síťovými prvky od různých dodavatelů. Umožňuje automatizované zřizování služeb, centralizované monitorování závad a komplexní analýzu výkonu v celé síti. Motivací bylo snížit provozní náklady, zlepšit kvalitu a spolehlivost služeb a urychlit nasazování nových služeb tím, že operátorům poskytne nástroje pro efektivní správu jejich stále složitějších a škálovatelných síťových infrastruktur.

## Klíčové vlastnosti

- Komplexní správa podle modelu FCAPS (závady, konfigurace, účtování, výkon, zabezpečení)
- Standardizovaná severní (Itf-N) a jižní rozhraní pro interoperabilitu mezi různými dodavateli
- Automatizované zřizování služeb a správa životního cyklu
- Monitorování výkonu a analýza KPI v reálném čase i historických dat
- Integrovaná správa závad s korelací alarmů a analýzou hlavní příčiny
- Podpora správy více technologií v jedné síti (2G/3G/4G/5G, pevné sítě)

## Související pojmy

- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.816** (Rel-8) — UMTS Management Reuse for E-UTRAN/EPC
- **TS 32.826** (Rel-10) — Study on Energy Savings Management in LTE/SAE Networks
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [OSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/oss/)
