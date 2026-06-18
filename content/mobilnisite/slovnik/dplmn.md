---
slug: "dplmn"
url: "/mobilnisite/slovnik/dplmn/"
type: "slovnik"
title: "DPLMN – Donor Public Land Mobile Network"
date: 2025-01-01
abbr: "DPLMN"
fullName: "Donor Public Land Mobile Network"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dplmn/"
summary: "Veřejná mobilní síť (PLMN), která poskytuje služby a zdroje jádra sítě lokální síti, jako je Home NodeB nebo malá buňka, ve scénářích jako sdílení sítě nebo nasazení femtobuněk. Umožňuje lokální síti"
---

DPLMN je veřejná mobilní síť (PLMN), která poskytuje služby a zdroje jádra sítě lokální síti, což jí umožňuje fungovat využitím infrastruktury dárce.

## Popis

Donor Public Land Mobile Network (DPLMN) je koncept definovaný ve specifikacích 3GPP, konkrétně v TS 43.052, v kontextu sdílení sítě a lokálních přístupových sítí, jako jsou systémy Home NodeB ([HNB](/mobilnisite/slovnik/hnb/)) nebo femtobuněk. DPLMN označuje [PLMN](/mobilnisite/slovnik/plmn/) (typicky provozovanou mobilním operátorem), která daruje nebo poskytuje funkce jádra sítě, včetně správy mobility, správy relací a autentizace účastníků, entitě lokální sítě. Tato lokální síť, často malá buňka nebo rezidenční brána, využívá zdroje DPLMN k připojení uživatelských zařízení k širším mobilním službám a funguje jako rozšíření dárcovské síťové infrastruktury.

Z architektonického hlediska DPLMN komunikuje s lokální sítí prostřednictvím standardizovaných referenčních bodů, jako je rozhraní Iuh pro HNBs, aby usnadnila komunikaci řídicí a uživatelské roviny. Prvky jádra sítě DPLMN, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G, zpracovávají procedury pro uživatele lokální sítě, včetně registrace, předávání hovorů a vynucování politik. Lokální síť se naopak spoléhá na DPLMN pro přístup ke službám, jako je hlas, data a IMS, a přitom může fungovat pod jinou identitou PLMN (např. Closed Subscriber Group) pro lokalizovanou správu.

Role DPLMN je klíčová pro umožnění modelů sdílení sítě, jako jsou sítě s jádrem pro více operátorů nebo nasazení neutrálního hostitele, kde spolupracuje více operátorů nebo infrastrukturu poskytuje třetí strana. Umožňuje lokální síti přesunout složité funkce jádra na dárce, čímž snižuje náklady a složitost. DPLMN také podporuje scénáře jako podnikové sítě nebo rozšíření pokrytí ve venkovských oblastech, kde může zavedená síť dárce-operatora zlepšit dostupnost a kvalitu služeb pro lokalizované oblasti.

## K čemu slouží

DPLMN byl zaveden pro podporu sdílení sítě a lokalizovaných přístupových řešení, aby uspokojil potřebu efektivního využití zdrojů a rozšíření pokrytí bez duplikace infrastruktury jádra sítě. Před jeho standardizací nasazení jako femtobuňky často vyžadovala vyhrazená jádra sítí nebo složité integrace, což omezovalo škálovatelnost a interoperabilitu. Koncept, formalizovaný ve vydání 8, umožnil operátorům darovat základní služby malým buňkám, což usnadnilo rezidenční a podniková nasazení využívající stávající sítě operátorů.

Klíčový problém, který DPLMN řeší, je umožnit lokálním sítím (např. HNBs) bezproblémově fungovat prostřednictvím zapůjčení funkcí jádra sítě od dárce [PLMN](/mobilnisite/slovnik/plmn/). Tím se snižují náklady na nasazení, zjednodušuje se správa a urychluje se zavádění služeb pro scénáře jako pokrytí v budovách nebo dohody o sdílení sítě. Podporuje také regulační a obchodní modely, kde více zúčastněných stran sdílí infrastrukturu, čímž se zvyšuje efektivita sítě a uživatelský zážitek v různých prostředích.

## Klíčové vlastnosti

- Poskytuje služby jádra sítě lokálním sítím, jako jsou Home NodeBs
- Umožňuje sdílení sítě a darování zdrojů mezi PLMNs
- Podporuje rozhraní jako Iuh pro připojení řídicí a uživatelské roviny
- Usnadňuje správu mobility a zpracování relací pro lokální uživatele
- Umožňuje lokalizovaným sítím fungovat v rámci autentizačních a politických rámců dárce
- Zlepšuje pokrytí a kapacitu v rezidenčních, podnikových nebo scénářích s neutrálním hostitelem

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [DPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/dplmn/)
