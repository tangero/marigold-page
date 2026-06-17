---
slug: "cse"
url: "/mobilnisite/slovnik/cse/"
type: "slovnik"
title: "CSE – Camel Service Environment"
date: 2025-01-01
abbr: "CSE"
fullName: "Camel Service Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cse/"
summary: "CSE je standardizované provozní prostředí pro služby CAMEL (Customised Applications for Mobile network Enhanced Logic) v sítích GSM a UMTS. Umožňuje nasazení specifických, inteligentních síťových (IN)"
---

CSE je standardizované provozní prostředí pro služby CAMEL, které umožňuje nasazení specifických, inteligentních síťových služeb operátora, jako je předplacené účtování, v sítích GSM a UMTS.

## Popis

Camel Service Environment (CSE) je klíčová funkční entita v architektuře inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) 3GPP pro GSM a UMTS, konkrétně definovaná pro hostování a provádění servisní logiky [CAMEL](/mobilnisite/slovnik/camel/). CAMEL je sada standardů, která umožňuje síťovým operátorům definovat a nasazovat vlastní, přidané služby, které mohou následovat účastníka i při roamingu mimo jeho domácí síť. CSE je fyzická nebo logická platforma, na které tyto programy servisní logiky CAMEL (SLP) sídlí a jsou prováděny. Rozhraní s prvky základní sítě, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) a Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)), prostřednictvím protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) za účelem řízení hovorů a relací na základě přihlášené servisní logiky.

Architektonicky je CSE často implementována jako součást Service Control Point (SCP) v tradičním modelu IN. Obsahuje klíčové komponenty včetně CAMEL Service Logic Execution Environment (SLEE), což je běhové prostředí pro programy servisní logiky, a CAMEL Service Data Function, která spravuje data účastníka a služby. Když přihlášený uživatel zahájí hovor nebo datovou relaci, spouštěč v MSC nebo SGSN (gsmSCF neboli Service Switching Function) detekuje událost a pozastaví zpracování hovoru. Poté odešle zprávu CAP do CSE s žádostí o instrukce. CSE, provádějící příslušnou servisní logiku CAMEL, žádost analyzuje, aplikuje obchodní pravidla (např. kontrolu předplaceného zůstatku, aplikaci směrování VPN) a vrátí řídicí příkazy ústředně, aby povolila, upravila, přesměrovala nebo ukončila hovor.

Role CSE je klíčová pro umožnění služeb řízených sítí v reálném čase. Poskytuje standardizované, na dodavateli nezávislé prostředí, které zajišťuje, že servisní logika napsaná pro síť jednoho operátora může být přenesena a správně provedena na implementaci CSE jiného operátora, čímž podporuje interoperabilitu. Zvládá komplexní stavové interakce, spravuje dialogy s více síťovými ústřednami současně a komunikuje s externími systémy, jako jsou fakturační platformy nebo centra polohy. CSE v podstatě funguje jako mozek pro služby CAMEL, odděluje servisní inteligenci od základní přepínací funkčnosti, což umožňuje rychlé zavádění a přizpůsobení služeb bez nutnosti aktualizace každé síťové ústředny.

## K čemu slouží

CSE byla vytvořena, aby vyřešila základní omezení tradičních mobilních sítí, kde byla veškerá servisní logika pevně zabudována do jednotlivých ústředen ([MSC](/mobilnisite/slovnik/msc/)). To činilo vytváření a nasazování nových, specifických služeb operátora extrémně pomalým, nákladným a nepřenosným. Bylo téměř nemožné, aby vlastní služby účastníka (jako podnikové VPN nebo předplacený účet) fungovaly bezproblémově při roamingu v navštívené síti, protože ústředny této sítě neznaly servisní logiku domácího operátora.

Zavedení [CAMEL](/mobilnisite/slovnik/camel/) a jeho CSE bylo motivováno potřebou přístupu inteligentní sítě (IN) v mobilní doméně, inspirovaného pevnými standardy IN jako INAP. Cílem bylo oddělit servisní logiku od přepínacího hardwaru. Centralizací servisní inteligence v CSE/SCP mohli operátoři vyvíjet, testovat a nasazovat nové služby na jedné platformě, která pak prostřednictvím standardizovaného protokolu CAP řídila ústředny v celé síti. To dramaticky zkrátilo dobu uvedení nových, výnos generujících služeb na trh.

Historicky, před CAMEL, byly pokročilé služby proprietární a omezené. CSE poskytla standardizované prostředí, které umožnilo první vlnu sofistikovaných mobilních služeb, jako je účtování předplacených služeb v reálném čase, což bylo klíčové pro expanzi trhu, a virtuální privátní sítě pro podniky. Stanovila architektonický základ pro síťové řízení služeb, který se později vyvinul v IP Multimedia Subsystem (IMS) a další platformy pro poskytování služeb, a zajistila přenositelnost služeb a konzistentní uživatelský zážitek přes hranice sítí.

## Klíčové vlastnosti

- Standardizované provozní prostředí pro programy servisní logiky CAMEL (SLP)
- Komunikuje s uzly základní sítě (MSC, SGSN) pomocí protokolu CAMEL Application Part (CAP)
- Umožňuje provádění služeb řízených sítí v reálném čase pro roamující účastníky
- Podporuje stavové servisní dialogy a správu dat účastníka
- Umožňuje specifické služby operátora, jako je předplacené účtování, VPN a účtování na základě polohy
- Poskytuje přenositelnost služeb a interoperabilitu dodavatelů prostřednictvím standardizace 3GPP

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.073** (Rel-5) — Localised Service Area (SoLSA) Stage 2 Description
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 43.073** (Rel-19) — SoLSA (Support of Localised Service Area) - Stage 2

---

📖 **Anglický originál a plná specifikace:** [CSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cse/)
