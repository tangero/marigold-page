---
slug: "aaa"
url: "/mobilnisite/slovnik/aaa/"
type: "slovnik"
title: "AAA – Authentication, Authorization, and Accounting"
date: 2026-01-01
abbr: "AAA"
fullName: "Authentication, Authorization, and Accounting"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aaa/"
summary: "AAA je bezpečnostní rámec pro řízení přístupu uživatelů k síťovým službám a sledování využití zdrojů. Provádí ověření identity uživatele, povolení příslušných akcí a evidenci spotřeby služeb pro účtov"
---

AAA je bezpečnostní rámec, který řídí přístup uživatelů k síťovým službám prostřednictvím ověření identity (autentizace), povolení příslušných akcí (autorizace) a evidence využití zdrojů pro účely účtování a auditu.

## Popis

Autentizace, autorizace a účtování (AAA) je komplexní bezpečnostní a řídicí rámec definovaný 3GPP pro řízení přístupu k síťovým zdrojům, vynucování politik a zaznamenávání dat o využití. V architektuře 3GPP jsou funkce AAA primárně implementovány v jádru sítě (Core Network) a často komunikují se serverem [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) nebo [UDM](/mobilnisite/slovnik/udm/) (Unified Data Management) pro ověření přihlašovacích údajů a dat uživatelského profilu. Koncept rámce je nezávislý na protokolu, ale jeho realizace běžně využívá protokol Diameter (specifikovaný v 3GPP TS 29.229 a souvisejících specifikacích) pro komunikaci mezi síťovými funkcemi, například mezi PCRF (Policy and Charging Rules Function) a [OCS](/mobilnisite/slovnik/ocs/) (Online Charging System).

Proces začíná autentizací, při které uživatel nebo zařízení prokáže svou identitu síti, typicky předložením přihlašovacích údajů (jako [IMSI](/mobilnisite/slovnik/imsi/) a sdílený tajný klíč), které jsou ověřeny proti datům uloženým v HSS/UDM. Tento krok zajišťuje, že entita je tím, za koho se vydává. Po úspěšné autentizaci následuje autorizace, která určuje, ke kterým službám, přenosovým rychlostem nebo síťovým zdrojům je uživatel oprávněn přistupovat na základě svého předplatného, aktuálních síťových politik a smluvních podmínek. Toto vynucují síťové prvky, jako je [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function).

Nakonec účtování zahrnuje sběr dat o spotřebě zdrojů pro účely fakturace, analýzy trendů nebo plánování kapacity. To lze provádět v reálném čase (online charging) nebo jako dávkový proces po skončení relace (offline charging). Rámec AAA je hluboce integrován s architekturou 3GPP PCC (Policy and Charging Control), kde se autorizační a účtovací politiky dynamicky uplatňují a aktualizují během uživatelské relace. Jeho role je klíčová nejen pro základní přístup, ale také pro umožnění sofistikované diferenciace služeb, zabezpečeného síťového řezání (network slicing) a flexibilních obchodních modelů, jako je sponzorovaný přenos dat.

## K čemu slouží

Rámec AAA byl vytvořen k řešení základních požadavků komerčních telekomunikačních sítí: zajistit, aby ke službám měli přístup pouze legitimní, platící účastníci, aby využívali pouze služby, na které mají nárok, a aby bylo možné jejich využití přesně měřit a účtovat. Před standardizovaným AAA měly rané mobilní sítě jednodušší a méně škálovatelné mechanismy pro řízení přístupu a účtování. Formalizace AAA v 3GPP, počínaje Release 4, poskytla strukturovaný, interoperabilní a škálovatelný model, který mohl podpořit přechod od okruhově přepínaných hlasových služeb k paketově přepínaným datovým službám a komplexnímu portfoliu služeb 3G a novějších generací.

K jeho vytvoření vedla potřeba jednotné bezpečnostní a řídicí vrstvy, která by mohla fungovat napříč různými přístupovými technologiemi (např. [GPRS](/mobilnisite/slovnik/gprs/), propojení s WLAN, 5G NR) a typy služeb. Řeší problém fragmentovaného řízení přístupu tím, že poskytuje centralizovaný bod pro ověření přihlašovacích údajů a rozhodování o politikách. Dále umožňuje pokročilé obchodní operace díky podpoře flexibilních účtovacích modelů (předplacené, postpaid, objemové, časové) a detailních auditních záznamů, které jsou nezbytné pro dodržování regulatorních požadavků a prevenci podvodů. V podstatě je AAA základním kamenem, který mění surové přenosové médium na zabezpečenou, zpoplatnitelnou a spravovatelnou komerční službu.

## Klíčové vlastnosti

- Centralizovaná autentizace uživatelů proti přihlašovacím údajům v HSS/UDM
- Dynamická autorizace na základě profilů účastníků a síťových politik
- Účtování a charging v reálném čase (online) a dávkové (offline)
- Integrace s architekturou Policy and Charging Control (PCC)
- Podpora bezpečnosti nezávislé na typu přístupu (3GPP i non-3GPP přístup)
- Umožňuje detailní reportování využití pro účtování a analytiku

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 22.258** (Rel-7) — All-IP Network Service Requirements
- **TR 22.935** (Rel-13) — LCS Feasibility Study for 3GPP-WLAN Interworking
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 28.204** (Rel-18) — Charging management
- **TS 28.402** (Rel-19) — EPC and non-3GPP Interworking Performance Measurements
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [AAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aaa/)
