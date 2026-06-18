---
slug: "isim"
url: "/mobilnisite/slovnik/isim/"
type: "slovnik"
title: "ISIM – IMS Subscriber Identity Module"
date: 2026-01-01
abbr: "ISIM"
fullName: "IMS Subscriber Identity Module"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/isim/"
summary: "ISIM je specializovaná aplikace na UICC (čipové kartě), která bezpečně ukládá identitu a autentizační přihlašovací údaje účastníka pro IP Multimedia Subsystem (IMS). Umožňuje zabezpečený přístup k IMS"
---

ISIM je aplikace na UICC, která bezpečně ukládá identitu a přihlašovací údaje účastníka v IMS a umožňuje autentizaci a přístup ke službám, jako je VoLTE.

## Popis

IMS Subscriber Identity Module (ISIM) je specializovaná softwarová aplikace umístěná na Universal Integrated Circuit Card (UICC), běžně známé jako [SIM](/mobilnisite/slovnik/sim/) karta. Odlišuje se od klasické SIM aplikace používané pro přístup k mobilní síti ([CS](/mobilnisite/slovnik/cs/) doména) a od [USIM](/mobilnisite/slovnik/usim/) aplikace pro paketový přístup v sítích 3G/4G ([PS](/mobilnisite/slovnik/ps/) doména). Aplikace ISIM je vyhrazena výhradně pro IP Multimedia Subsystem (IMS), který poskytuje multimediální služby jako Voice over LTE (VoLTE), videohovory a instant messaging přes mobilní paketové jádro.

Z architektonického hlediska ISIM obsahuje sadu bezpečně uložených souborů a parametrů nezbytných pro registraci do IMS a využívání služeb. Nejzásadnější datovou položkou je IMS Private User Identity ([IMPI](/mobilnisite/slovnik/impi/)), jedinečný globální identifikátor účastníka v IMS doméně (často ve formátu [NAI](/mobilnisite/slovnik/nai/), např. user@domain.com). Ukládá také odpovídající IMS Public User Identity ([IMPU](/mobilnisite/slovnik/impu/)), což je adresa používaná pro komunikaci (např. [SIP](/mobilnisite/slovnik/sip/) URI). Dále ISIM uchovává dlouhodobé autentizační přihlašovací údaje: sdílený tajný klíč a související parametry autentizačního algoritmu. Tyto přihlašovací údaje se používají v proceduře IMS Authentication and Key Agreement (IMS AKA).

Když chce uživatel přistoupit k IMS službám, IMS klient v mobilním zařízení přečte potřebné identity z ISIM. Během registrace zařízení a síť provedou protokol IMS AKA. Zařízení použije tajný klíč z ISIM k výpočtu odpovědi na výzvu ze sítě. Tento proces autentizuje účastníka vůči IMS síti a vytváří zabezpečené relací klíče pro ochranu signalizace SIP. ISIM tedy funguje jako kořen důvěry pro přístup k IMS, obdobně jako USIM autentizuje uživatele vůči paketové síti jádra.

Aplikace ISIM spolupracuje s dalšími aplikacemi na stejné UICC. Zařízení může používat USIM pro přístup k LTE/5G síti (pro přenosovou konektivitu) a současně ISIM pro přístup k IMS službám přes tuto přenosovou cestu. Toto oddělení umožňuje nezávislou správu přihlašovacích údajů a služeb. Role ISIM je zásadní pro bezpečnost IMS a přenositelnost služeb, protože identita a přihlašovací údaje účastníka v IMS jsou fyzicky uloženy na přenosné, proti manipulaci odolné kartě.

## K čemu slouží

ISIM byl vytvořen, aby poskytl bezpečný, přenosný a standardizovaný identifikační modul specificky pro IMS, což je servisní architektura oddělená od tradičních přístupových mobilních sítí. Před zavedením ISIM rané implementace IMS často používaly softwarové přihlašovací údaje (uživatelské jméno/heslo uložené v zařízení) nebo se pokoušely odvodit IMS identity z mobilních identit (jako je IMSI). Tyto přístupy měly bezpečnostní slabiny (softwarové přihlašovací údaje jsou zranitelné) nebo omezenou flexibilitu (těsné propojení s mobilním tarifem).

Specializovaný modul byl nezbytný, protože autentizace v IMS (IMS AKA) se liší od autentizace v mobilní síti (používané SIM/USIM). IMS používá protokoly založené na SIP a vyžaduje identity ve formátu URI nebo NAI, nikoli MSISDN nebo IMSI. ISIM poskytuje zabezpečený hardwarový kontejner pro tyto nové formáty identit a související kryptografické klíče, čímž zajišťuje vysokou úroveň bezpečnosti srovnatelnou s přístupem k mobilní síti. Také umožňuje přenositelnost služeb; uživatel může přemístit svou UICC do nového zařízení a jeho IMS identita a služby jsou okamžitě dostupné.

Jeho zavedení ve verzi Release 5 časově souviselo s počáteční standardizací IMS. Vyřešil problém, jak bezpečně a spravovatelně poskytovat IMS předplatné koncovým uživatelům. Využitím stávající platformy UICC umožnil operátorům nabízet IMS služby pomocí známého, bezpečného distribučního mechanismu (SIM karty). ISIM vytvořil jasné oddělení přihlašovacích údajů, což umožňuje uživateli mít nezávislá předplatná pro mobilní přístup a IMS služby, i když je poskytuje stejný operátor.

## Klíčové vlastnosti

- Ukládá IMS Private User Identity (IMPI) a Public User Identity (IMPU)
- Obsahuje dlouhodobý tajný klíč pro IMS Authentication and Key Agreement (IMS AKA)
- Je implementována jako specializovaná aplikace na UICC (čipové kartě)
- Poskytuje hardwarově založenou ochranu pro IMS přihlašovací údaje, odolnou vůči manipulaci
- Umožňuje zabezpečenou registraci do IMS a přístup ke službám (např. VoLTE)
- Funguje nezávisle na aplikacích USIM/SIM na stejné UICC

## Související pojmy

- [IMPI – IP Multimedia CN subsystem Private Identity](/mobilnisite/slovnik/impi/)
- [IMPU – IP Multimedia Public User Identity](/mobilnisite/slovnik/impu/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TR 31.901** (Rel-14) — USIM/ISIM/USAT Feature Review Study
- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- **TS 32.182** (Rel-19) — UDC Common Baseline Information Model (CBIM)
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [ISIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/isim/)
