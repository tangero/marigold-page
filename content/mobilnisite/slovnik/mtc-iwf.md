---
slug: "mtc-iwf"
url: "/mobilnisite/slovnik/mtc-iwf/"
type: "slovnik"
title: "MTC-IWF – Machine Type Communications - InterWorking Function"
date: 2025-01-01
abbr: "MTC-IWF"
fullName: "Machine Type Communications - InterWorking Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mtc-iwf/"
summary: "MTC-IWF je funkce jádra sítě, která slouží jako zabezpečená brána mezi externími servery MTC a sítí 3GPP. Autorizuje servisní požadavky, překládá protokoly a přeposílá zprávy pro spuštění zařízení smě"
---

MTC-IWF je funkce jádra sítě, která funguje jako zabezpečená brána mezi externími servery MTC a sítí 3GPP, autorizuje požadavky, překládá protokoly a přeposílá spouštěče zařízení.

## Popis

Funkce pro propojení komunikace typu stroj (Machine Type Communications InterWorking Function, MTC-IWF) je klíčový zabezpečovací a propojovací uzel zavedený do architektury jádra sítě 3GPP, který umožňuje řízenou a zabezpečenou komunikaci mezi externími servery komunikace typu stroj ([MTC](/mobilnisite/slovnik/mtc/)) a mobilní sítí. Funguje jako jednotný kontaktní bod v doméně operátora pro všechny externí poskytovatele služeb MTC. Z architektonického hlediska se MTC-IWF nachází v domácí veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) a komunikuje s externími servery MTC přes referenční bod Tsp, který typicky používá protokoly založené na IP, jako je Diameter nebo RESTful [API](/mobilnisite/slovnik/api/). Uvnitř sítě komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) přes rozhraní S6m (založené na Diameter) a s [SMS](/mobilnisite/slovnik/sms/) Service Center ([SMS-SC](/mobilnisite/slovnik/sms-sc/)) přes rozhraní T4. Její primární operační role spočívá v obsluze požadavků na 'Spuštění zařízení' (Device Trigger). Když server MTC potřebuje zahájit komunikaci s neaktivním zařízením MTC, odešle požadavek na spuštění do MTC-IWF. MTC-IWF nejprve autentizuje a autorizuje server na základě předplatitelských dat. Poté se dotáže HSS, aby zjistila stav dosažitelnosti zařízení a nejvhodnější mechanismus doručení, což je často právě přes SMS jako přenos pro spouštěč. MTC-IWF spouštěč odpovídajícím způsobem naformátuje a přepošle jej do SMS-SC pro doručení zařízení. Tento proces umožňuje síti probudit zařízení v režimu úspory energie ([PSM](/mobilnisite/slovnik/psm/)) nebo jinak nepřipojené k IP. Kromě spouštění MTC-IWF také provádí překlad protokolů mezi externími aplikačními protokoly a interními signalizačními protokoly 3GPP, poskytuje účtovací data a vynucuje politiky, aby zabránila zneužití sítě ze strany externích subjektů.

## K čemu slouží

MTC-IWF byla vytvořena, aby vyřešila kritickou bezpečnostní a architektonickou mezeru v raných nasazeních MTC: jak umožnit externím serverům MTC třetích stran bezpečně komunikovat se zařízeními uvnitř důvěryhodné sítě operátora, aniž by byly přímo vystaveny rozhraní jádra sítě. Před jejím zavedením neexistovala standardizovaná, bezpečná metoda, jak by mohl externí server zahájit komunikaci se zařízením, zejména s takovým, které bylo neaktivní nebo v hlubokém spánkovém režimu. To omezovalo možnost implementace efektivních služeb IoT založených na principu push. MTC-IWF poskytuje řízenou bránu, která řeší několik klíčových problémů: brání neoprávněnému přístupu k předplatitelským datům a síťovým zdrojům, abstrahuje složitou interní topologii sítě a protokoly před externími servery a poskytuje centralizovaný bod pro vynucování politik, auditování a účtování související se službami MTC. Její vytvoření ve verzi 11 (Release 11) bylo motivováno potřebou umožnit škálovatelné, komerční služby MTC, kde by mohlo více externích poskytovatelů služeb spolehlivě a bezpečně dosáhnout na svá zařízení, což je základním požadavkem pro obchodní model IoT, kde jsou síťový operátor a poskytovatel aplikace často oddělené subjekty.

## Klíčové vlastnosti

- Slouží jako jednotná, zabezpečená brána pro externí servery MTC pro rozhraní se sítí 3GPP
- Provádí autentizaci, autorizaci a účtování (AAA) pro požadavky serverů MTC
- Zpracovává a přeposílá požadavky na spuštění zařízení (Device Trigger) k probuzení neaktivních zařízení MTC
- Komunikuje s HSS/HLR za účelem kontroly stavu zařízení a předplatného pro funkce MTC
- Překládá mezi externími aplikačními protokoly (např. přes Tsp) a interními signalizačními protokoly 3GPP (např. Diameter přes S6m)
- Poskytuje řízení přetížení směrem k externím serverům za účelem ochrany jádra sítě

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SMS-SC – Short Message Service - Service Centre](/mobilnisite/slovnik/sms-sc/)

## Definující specifikace

- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 29.336** (Rel-19) — HSS Diameter Interfaces for PDN Interworking
- **TS 29.337** (Rel-19) — Diameter T4 Interface for MTC Device Triggering
- **TS 33.187** (Rel-19) — Security for Machine-Type Communications Enhancements

---

📖 **Anglický originál a plná specifikace:** [MTC-IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtc-iwf/)
