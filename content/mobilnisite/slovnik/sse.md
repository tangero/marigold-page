---
slug: "sse"
url: "/mobilnisite/slovnik/sse/"
type: "slovnik"
title: "SSE – Service Specific Entities"
date: 2025-01-01
abbr: "SSE"
fullName: "Service Specific Entities"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sse/"
summary: "Funkční komponenty v rámci IP multimediálního subsystému (IMS), které poskytují logiku přidaných služeb a interakci pro multimediální aplikace. Umožňují pokročilé služby, jako je Push-to-talk over Cel"
---

SSE je funkční komponenta v rámci IP multimediální subsystému (IMS), která poskytuje logiku přidaných služeb pro multimediální aplikace, jako je zasílání zpráv a konferenční hovory, prostřednictvím rozhraní s jádrovými prvky IMS.

## Popis

Service Specific Entities (SSE) jsou standardizovaný architektonický koncept v rámci 3GPP IP multimediálního subsystému (IMS). Představují vyhrazené aplikační servery nebo funkční entity, které hostují a provádějí logiku pro konkrétní, přidané multimediální služby nad rámec základního řízení [SIP](/mobilnisite/slovnik/sip/) relací. SSE není jediný síťový uzel, ale logická role, která může být implementována na různých fyzických platformách, jako je vyhrazený aplikační server ([AS](/mobilnisite/slovnik/as/)), součást telefonního aplikačního serveru ([TAS](/mobilnisite/slovnik/tas/)) nebo specializovaný server pro konkrétní službu. Hlavní funkcí SSE je poskytovat zpracování specifické pro službu, manipulaci s daty a interakci vyžadovanou pro pokročilé služby založené na IMS, jako je Push-to-talk over Cellular (PoC), multimediální konference, instant messaging, presence nebo správa skupin.

SSE fungují tak, že komunikují s jádrovou infrastrukturou IMS prostřednictvím standardizovaných referenčních bodů, primárně rozhraní [ISC](/mobilnisite/slovnik/isc/) (IMS Service Control) pomocí protokolu SIP. Když do [S-CSCF](/mobilnisite/slovnik/s-cscf/) dorazí SIP požadavek na službu (např. pozvánka do relace PoC), S-CSCF použije počáteční filtrační kritéria (iFC) v profilu uživatele, aby rozhodl, zda má být požadavek přeposlán konkrétnímu SSE. Požadavek je poté směrován na příslušný SSE. SSE provede svou servisní logiku, což může zahrnovat interakci s jinými SSE, dotazování databází (jako je Group List Management Server), úpravy SIP zpráv, správu mediálních prostředků nebo rozhraní s externími sítěmi. Po zpracování SSE typicky vrátí řízení zpět S-CSCF pro další směrování. Například PoC SSE by řešilo řízení práva mluvit, identifikaci mluvčího a distribuci médií členům skupiny.

Z architektonického hlediska SSE podporují modulární a škálovatelnou servisní vrstvu. Klíčové komponenty v rámci SSE zahrnují prostředí pro vykonávání servisní logiky, rozhraní k jádru IMS (ISC), rozhraní k dalším službám (např. k serveru presence přes rozhraní Ut pro konfiguraci) a potenciálně rozhraní k mediálním prostředkům (Mr, Mp). Specifikace 3GPP, zejména v řadě TS 26 pro kodeky a zpracování médií a řadě TS 24 pro komunikační procedury, definují přesné chování, protokoly a informační toky pro standardizované SSE. To zajišťuje interoperabilitu mezi zařízeními od různých výrobců a napříč sítěmi operátorů. Role SSE spočívá v oddělení inovací služeb od vývoje jádrové sítě, což umožňuje zavádět nové služby přidáním nebo aktualizací SSE bez zásadních úprav [CSCF](/mobilnisite/slovnik/cscf/) nebo jiných jádrových prvků IMS.

## K čemu slouží

Koncept SSE byl zaveden, aby řešil výzvu tvorby a standardizace služeb v nově vznikající plně IP architektuře IMS. Před IMS byly pokročilé telefonní služby často těsně svázány s přepojováním okruhů nebo implementovány jako proprietární, izolovaná řešení, což vedlo k problémům s interoperabilitou a pomalým inovacím. Vize IMS byla vytvořit společné, opakovaně použitelné IP jádro pro poskytování široké škály multimediálních služeb. Samotné jádro sítě však nemůže poskytovat koncovým uživatelům služby; potřebuje standardizovaný způsob připojení servisní logiky.

SSE byla vytvořena, aby tuto potřebu naplnila. Poskytují 'servisní vrstvu' nad jádrem IMS a řeší problém, jak definovat, standardizovat a nasazovat interoperabilní multimediální aplikace. Specifikací SSE pro klíčové služby (jako je PoC nebo instant messaging) zajistilo 3GPP, že základní stavební kameny pro složité služby jsou jednotně dostupné. To umožnilo operátorům nabízet konzistentní služby a výrobcům zařízení implementovat kompatibilní klienty. Motivací bylo zabránit fragmentaci a urychlit přijetí služeb založených na IMS poskytnutím jasných plánů pro implementaci služeb.

Dále SSE usnadňují integraci a skládání služeb. Různé SSE mohou spolupracovat; například konferenční služba (jeden SSE) může využívat službu správy skupin (další SSE) a službu presence (třetí SSE). Tento modulární přístup řeší problém redundance a složitosti služeb. Namísto toho, aby každá služba implementovala vlastní správu skupin, může více aplikací využívat standardizovaný Group Management SSE. To podporuje efektivitu sítě, snižuje dobu vývoje nových služeb a vytváří soudržnější uživatelský zážitek napříč různými aplikacemi IMS.

## Klíčové vlastnosti

- Hostí servisní logiku specifickou pro multimediální aplikace založené na IMS (např. PoC, konference)
- Komunikuje s jádrem IMS prostřednictvím standardizovaného referenčního bodu ISC za použití SIP
- Umožňuje modulární a oddělenou servisní architekturu v rámci IMS
- Podporuje interoperabilitu prostřednictvím standardizovaného chování a procedur 3GPP
- Umožňuje skládání služeb interakcí s jinými SSE a službami
- Usnadňuje rychlé nasazení nových přidaných služeb bez změn jádrové sítě

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [SSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/sse/)
