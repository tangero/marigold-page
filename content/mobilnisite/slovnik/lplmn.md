---
slug: "lplmn"
url: "/mobilnisite/slovnik/lplmn/"
type: "slovnik"
title: "LPLMN – Local Public Land Mobile Network"
date: 2025-01-01
abbr: "LPLMN"
fullName: "Local Public Land Mobile Network"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lplmn/"
summary: "LPLMN je identifikátor sítě představující domácího nebo primárního síťového operátora uživatele v konkrétní geografické oblasti. Je klíčový pro identifikaci účastníka, roamingové dohody a procedury vý"
---

LPLMN je identifikátor sítě domácího nebo primárního mobilního operátora uživatele v konkrétní oblasti, používaný pro identifikaci účastníka, roaming a výběr sítě za účelem připojení k jeho domovské síti.

## Popis

Local Public Land Mobile Network (LPLMN) je základní identifikátor v architektuře systému 3GPP, definovaný jako PLMN, u kterého má uživatel své předplatné. Jedná se o jedinečný identifikátor, typicky složený z Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), který globálně odlišuje síť jednoho operátora od druhého. LPLMN je uložen na uživatelově modulu USIM (Universal Subscriber Identity Module) a používá jej uživatelské zařízení (UE) i síť pro klíčové procedury, jako je počáteční registrace, správa mobility a autorizace služeb. UE neustále monitoruje přítomnost své LPLMN, aby upřednostnilo připojení ke své domovské síti, což je zásadní pro zajištění kvality služeb, přesnosti účtování a přístupu k předplaceným službám bez roamingových poplatků.

Architektonicky je koncept LPLMN integrován do předplatitelských dat v jádře sítě, kde sídlí v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v 4G nebo v Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) v 5G. Když se UE pokouší připojit k síti, odešle svou International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), která inherentně obsahuje kód PLMN. Navštívená síť to použije k identifikaci domovské sítě uživatele (LPLMN) a k navázání spojení s příslušným HSS/UDM pro autentizaci a autorizaci. LPLMN je klíčovým parametrem v seznamu ekvivalentních PLMN ([EPLMN](/mobilnisite/slovnik/eplmn/)) v UE, což jsou sítě považované za rovnocenné domovské síti z hlediska kontinuity služeb, ale samotná LPLMN má nejvyšší prioritu v algoritmu výběru sítě v UE.

Jeho role se rozprostírá napříč protokolovým zásobníkem a síťovými rozhraními. V protokolech Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) se LPLMN používá při aktualizacích sledovací oblasti a aktualizacích směrovací oblasti. Na rádiovém rozhraní je vysílán v blocích systémových informací (SIB) každou buňkou. UE porovnává vysílaný PLMN s uloženou LPLMN (a seznamem EPLMN), aby mohlo rozhodovat o výběru a převýběru buňky. Pro síťové operátory tvoří LPLMN základ roamingových dohod; když se UE nachází ve Visited PLMN (VPLMN), VPLMN identifikuje LPLMN, aby správně směrovala účtovací a autentizační zprávy. LPLMN tedy není jen statický identifikátor, ale dynamický ukotvovací bod pro síťovou identitu účastníka, který umožňuje plynulou mobilitu, poskytování služeb a interoperabilitu mezi operátory v globálním měřítku.

## K čemu slouží

LPLMN byl zaveden, aby poskytl standardizovanou, jednoznačnou metodu pro identifikaci domácího síťového operátora účastníka v rámci globálního telekomunikačního ekosystému. Před standardizovanou identifikací PLMN byla interoperabilita mezi různými národními a regionálními sítěmi obtížná, což bránilo rozvoji plynulého mezinárodního roamingu. LPLMN řeší základní problém identity účastníka a sítě v prostředí s více operátory a umožňuje automatické zjišťování, výběr a připojení k síti.

Jeho vytvoření bylo motivováno potřebou spolehlivého mechanismu pro podporu mobility účastníků. Umožňuje mobilnímu zařízení automaticky najít a upřednostnit svou domovskou síť, což zajišťuje uživatelům konzistentní službu a zabraňuje zbytečnému připojení k roamingovému partnerovi, které by mohlo znamenat dodatečné poplatky nebo horší službu. Dále poskytuje technický základ pro funkce jádra sítě, jako je autentizace, kde síť potřebuje vědět, na který [HSS](/mobilnisite/slovnik/hss/)/UDM se má dotázat ohledně přihlašovacích údajů účastníka. Vložením této identity do USIM a standardizací jejího použití napříč všemi technologiemi 3GPP (od GSM/UMTS přes LTE až po 5G NR) zajišťuje LPLMN zpětnou kompatibilitu a konzistentní uživatelský zážitek s vývojem technologií.

## Klíčové vlastnosti

- Jedinečný globální identifikátor složený z MCC a MNC
- Trvale uložen na uživatelově USIM
- Nejvyšší priorita v algoritmu výběru sítě v UE
- Ukotvovací bod pro předplatitelská data v HSS/UDM
- Základní pro uzavírání roamingových dohod mezi operátory
- Vysílán v systémových informacích buňky pro identifikaci UE

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [EPLMN – Equivalent PLMN](/mobilnisite/slovnik/eplmn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [LPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/lplmn/)
