---
slug: "nwdaf"
url: "/mobilnisite/slovnik/nwdaf/"
type: "slovnik"
title: "NWDAF – Network Data Analytics Function"
date: 2026-01-01
abbr: "NWDAF"
fullName: "Network Data Analytics Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nwdaf/"
summary: "Funkce pro analýzu síťových dat (NWDAF) je analytický engine 5G Core sítě, který sbírá data od síťových funkcí a externích zdrojů za účelem poskytování analýz a predikcí. Umožňuje uzavřenou smyčku aut"
---

NWDAF je analytický engine 5G Core sítě, který sbírá data od síťových funkcí a externích zdrojů za účelem poskytování analýz a predikcí pro automatizaci a optimalizaci.

## Popis

Funkce pro analýzu síťových dat (NWDAF) je standardizovaná analytická funkce s podporou strojového učení v rámci architektury 5G Core sítě, zavedená ve specifikaci 3GPP Release 15. Slouží jako centralizovaný nebo distribuovaný analytický engine, který sbírá, koreluje a analyzuje data z různých síťových funkcí, aplikací a externích zdrojů za účelem generování analýz, predikcí a doporučení. Primární role NWDAF spočívá v poskytování daty řízené inteligence ostatním řídicím funkcím a funkcím managementu 5G Core, což umožňuje automatizovanou optimalizaci sítě, proaktivní zajištění služeb a vylepšený uživatelský zážitek. Architektonicky je definována jako funkce architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)), která zpřístupňuje analytické služby směrem k severu prostřednictvím standardizovaných [API](/mobilnisite/slovnik/api/), což umožňuje konzumentům, jako je funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), funkce výběru síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)) a systémy provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)), tyto analýzy vyžadovat.

NWDAF funguje prostřednictvím strukturovaného datového řetězce zahrnujícího sběr dat, analytické zpracování a distribuci výsledků. Sbírá data z více zdrojů kategorizovaných jako síťová data (např. od [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/) ohledně metrik relací, vzorců mobility, QoS), aplikační data (např. od aplikačních funkcí (AF) o požadavcích služby) a data managementu (např. od OAM o výkonu a chybách). Tato data mohou být přijímána prostřednictvím push nebo pull mechanismů využívajících standardizovaná rozhraní jako Nnwdaf_EventsSubscription. Interně NWDAF využívá analytické modely – které mohou být založené na pravidlech, statistické nebo modely strojového učení – ke zpracování dat. Tyto modely provádějí úkoly jako detekce anomálií, analýzu trendů, predikci síťového vytížení nebo mobility uživatelů a identifikaci problémů s výkonem řezů. Výsledky analýz, které zahrnují historické reporty, analýzy v reálném čase nebo budoucí predikce, jsou následně poskytovány konzumentům, aby ovlivnily rozhodnutí, jako je úprava QoS politik, spuštění rekonfigurace síťového řezu nebo optimalizace parametrů předávání.

Klíčové komponenty NWDAF zahrnují Analytickou logickou funkci (která hostuje analytické modely), Funkci koordinace sběru dat (která spravuje získávání dat ze zdrojů) a Funkci zpřístupnění analýz (která se stará o zpřístupnění API a správu odběrů). NWDAF podporuje jak analytické dotazy na vyžádání, tak odběrové kontinuální analytické reportování. Například PCF se může přihlásit k odběru analýz od NWDAF o očekávaném síťovém přetížení v určité oblasti, aby preventivně upravil pravidla politik, nebo OAM systém může vyžádat predikce využití zdrojů řezu pro plánování kapacity. NWDAF také usnadňuje trénink modelů a správu jejich životního cyklu, potenciálně využívajíc federované učení napříč více instancemi NWDAF. Jeho integrace s 5G Core je všeprostupující, ovlivňuje téměř všechny aspekty provozu sítě od správy mobility a správy relací po síťové řezy a edge computing, což z něj činí základní kámen vize autonomní sítě 5G.

## K čemu slouží

NWDAF byl vytvořen, aby řešil rostoucí složitost a dynamickou povahu 5G sítí, které podporují rozmanité služby s výrazně odlišnými požadavky – od vylepšeného mobilního širokopásmového připojení přes masivní IoT až po ultra-spolehlivou komunikaci s nízkou latencí. Tradiční správa sítě spoléhala na reaktivní, manuální zásahy založené na statických prahových hodnotách, které byly pro rozsah, agilitu a rozmanitost služeb 5G nedostatečné. NWDAF zavádí nativní, standardizovanou analytickou schopnost uvnitř 5G Core, aby umožnil daty řízené, proaktivní a automatizované síťové operace. Řeší problém izolovaných dat napříč síťovými funkcemi tím, že poskytuje centralizovaný analytický hub, který koreluje informace za účelem získání holistických analýz, čímž zlepšuje efektivitu sítě, využití zdrojů a kvalitu služby.

Historicky byly síťové analýzy prováděny externími OAM systémy nebo proprietárními řešeními, kterým chyběla těsná integrace s řídicí rovinou jádra sítě. To vedlo k opožděným reakcím, omezeným možnostem v reálném čase a neschopnosti přímo ovlivňovat chování sítě. S příchodem síťových řezů, edge computingu a architektury založené na službách v 5G se potřeba inteligentní, uzavřené smyčky automatizace stala kritickou. Release 15 specifikace 3GPP položil základy pro NWDAF jako součást nativní inteligence systému 5G, motivován požadavky operátorů na snížení provozních nákladů, zlepšení zákaznické zkušenosti a podporu nových vertikálních služeb. NWDAF umožňuje prediktivní údržbu, dynamické přidělování zdrojů a personalizované poskytování služeb prostřednictvím využití technik strojového učení a big data v telekomunikační doméně.

NWDAF dále řeší omezení předchozích přístupů tím, že poskytuje standardizovaný rámec pro analýzy, který zajišťuje interoperabilitu napříč dodavateli a síťovými funkcemi. Umožňuje síťovým operátorům nasazovat pokročilé analýzy bez nutnosti spoléhat se na fragmentovaná, dodavatelsky specifická řešení. Vložením analýz přímo do síťové architektury NWDAF usnadňuje rozhodování v reálném čase, jako je okamžité přizpůsobení se špičkám provozu nebo zmírnění přetížení dříve, než ovlivní uživatele. Jeho vznik byl také hnán vizí samoorganizujících se sítí (SON) vyvíjejících se směrem k plně autonomním sítím, kde NWDAF funguje jako 'mozek', který analyzuje data a spouští akce prostřednictvím systémů řízení politik a managementu. To transformuje 5G z platformy pro konektivitu na inteligentní, adaptivní infrastrukturu schopnou splnit přísné a různorodé požadavky budoucí digitální společnosti.

## Klíčové vlastnosti

- Centralizovaný sběr a korelace dat z více zdrojů sítě
- Podpora prediktivní analýzy využívající modely strojového učení (ML)
- Standardizovaná API založená na službách pro zpřístupnění analýz
- Odběrové a na vyžádání poskytované analytické reportování
- Integrace s řídicí rovinou 5G pro uzavřenou smyčku automatizace
- Podpora analýz a zajištění specifických pro síťový řez

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.791** (Rel-16) — NWDAF Data Collection & Analytics Framework
- **TS 26.531** (Rel-19) — Data Collection & Reporting Architecture for 5G
- **TS 26.532** (Rel-19) — 5G Data Collection and Reporting API Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.812** (Rel-18) — Technical Report
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [NWDAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nwdaf/)
