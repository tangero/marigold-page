---
slug: "hms"
url: "/mobilnisite/slovnik/hms/"
type: "slovnik"
title: "HMS – Home Node B Management System"
date: 2025-01-01
abbr: "HMS"
fullName: "Home Node B Management System"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/hms/"
summary: "Systém pro správu Home Node B (HNB), což jsou femtobuňky instalované koncovými uživateli pro zajištění vnitřního pokrytí mobilní sítí. HMS umožňuje vzdálenou konfiguraci, monitorování a údržbu HNB a z"
---

HMS je systém pro správu femtobuněk typu Home Node B, který umožňuje jejich vzdálenou konfiguraci, monitorování a údržbu, aby bylo zajištěno jejich správné fungování v síti mobilního operátora.

## Popis

Home Node B Management System (HMS) je centralizovaná platforma pro správu určená k dohledu nad zařízeními Home Node B ([HNB](/mobilnisite/slovnik/hnb/)), známými také jako femtobuňky. HNB jsou malé, nízkovýkonné buňkové základnové stanice instalované koncovými uživateli pro zlepšení vnitřního pokrytí a kapacity. HMS poskytuje operátorům nástroje pro efektivní správu těchto distribuovaných zařízení, zajišťuje úkoly jako provizionování, softwarové aktualizace, monitorování výkonu a správu poruch. S HNB komunikuje prostřednictvím zabezpečených IP spojení, typicky za použití protokolu TR-069 nebo jiných správních protokolů, za účelem výměny konfiguračních dat a provozního stavu.

Z architektonického hlediska se HMS skládá z několika klíčových komponent: auto-konfiguračního serveru ([ACS](/mobilnisite/slovnik/acs/)), který zasílá nastavení HNB, modulu správy výkonu, který sbírá metriky jako síla signálu a úspěšnost hovorů, a zabezpečovací brány, která zajišťuje šifrovanou komunikaci. HMS se integruje s prvky základní sítě operátora, jako je HNB Gateway ([HNB-GW](/mobilnisite/slovnik/hnb-gw/)) a systémy pro podporu provozu ([OSS](/mobilnisite/slovnik/oss/)), aby umožnil plynulé poskytování služeb. Podporuje hromadné operace, což operátorům umožňuje spravovat tisíce HNB současně, což je klíčové pro rozsáhlá nasazení.

HMS hraje klíčovou roli při zajišťování toho, aby HNB dodržovaly síťové politiky a nezpůsobovaly rušení makro buňkám. Vynucuje řízení přístupu ověřováním identity HNB a jejich autorizací pro připojení k síti. Dále HMS usnadňuje vzdálené odstraňování problémů, čímž snižuje potřebu zásahů na místě a provozní náklady. Poskytnutím komplexních funkcí správy pomáhá HMS operátorům nákladově efektivně rozšiřovat pokrytí a kapacitu při zachování vysokých standardů kvality služeb a zabezpečení.

## K čemu slouží

HMS byl vyvinut k řešení výzev správy spojených s rozsáhlým nasazením Home Node B (femtobuněk) v sítích 3G a později 4G. Když operátoři podporovali koncové uživatele v instalaci [HNB](/mobilnisite/slovnik/hnb/) pro zlepšení vnitřního pokrytí, ruční konfigurace a monitorování těchto zařízení se stala nepraktickou. HMS poskytl automatizované, škálovatelné řešení pro vzdálenou správu, které řešilo problémy jako nekonzistentní konfigurace, bezpečnostní zranitelnosti a zhoršování výkonu.

Vytvoření HMS bylo motivováno potřebou integrovat zařízení instalovaná uživateli do sítí operátorů bez kompromitování integrity sítě. Předchozí přístupy postrádaly standardizované systémy správy, což vedlo k problémům s interoperabilitou a zvýšeným nákladům na podporu. HMS standardizoval postupy správy, což operátorům umožnilo efektivně zavádět služby femtobuněk při zajištění spolehlivého provozu a zabezpečení. Řešil omezení dřívější správy malých buněk tím, že nabídl centralizovanou kontrolu a bezproblémovou integraci s existující síťovou infrastrukturou.

## Klíčové vlastnosti

- Vzdálené provizionování a konfigurace Home Node B
- Automatizované softwarové a firmware aktualizace
- Monitorování výkonu a správa poruch
- Zabezpečená komunikace prostřednictvím šifrování a autentizace
- Hromadné operace pro škálovatelná nasazení femtobuněk
- Integrace s HNB Gateway a OSS operátora

## Definující specifikace

- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 31.104** (Rel-19) — HPSIM Application Specification
- **TS 32.571** (Rel-19) — HNB/HeNB Type 2 Interface Management Concepts
- **TS 32.572** (Rel-19) — HNB/HeNB Type 2 Interface Concepts & Requirements
- **TS 32.581** (Rel-19) — HNB OAM&P Concepts & Requirements
- **TS 32.582** (Rel-19) — HNB Management Information Model for Type 1 Interface
- **TS 32.583** (Rel-19) — HNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.584** (Rel-19) — HNB OAM&P XML Definitions for Type 1 Interface
- **TS 32.592** (Rel-19) — HeNB OAM&P Information Model
- **TS 32.593** (Rel-19) — HeNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.594** (Rel-19) — Data definitions for HeNB to HeMS Type 1 interface
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem

---

📖 **Anglický originál a plná specifikace:** [HMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hms/)
