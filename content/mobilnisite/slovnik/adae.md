---
slug: "adae"
url: "/mobilnisite/slovnik/adae/"
type: "slovnik"
title: "ADAE – Application Data Analytics Enablement"
date: 2026-01-01
abbr: "ADAE"
fullName: "Application Data Analytics Enablement"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adae/"
summary: "ADAE je služební schopnost 3GPP umožňující analýzu dat na aplikační vrstvě tím, že zpřístupňuje síťová data a události autorizovaným aplikačním funkcím (AF). Standardizuje způsob, jakým aplikace mohou"
---

ADAE je služební schopnost 3GPP, která umožňuje analýzu dat na aplikační vrstvě tím, že zpřístupňuje síťová data a události autorizovaným aplikačním funkcím.

## Popis

Application Data Analytics Enablement (ADAE) je rámec standardizovaný 3GPP pro usnadnění využívání analytických údajů generovaných sítí externími aplikacemi. Funguje jako služební schopnost v rámci 5G Core Network, konkrétně definovaná jako služba Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)). Hlavním architektonickým principem je aplikační funkce ([AF](/mobilnisite/slovnik/af/)) v roli klienta, která zasílá požadavky na odběr analytických údajů službě ADAE hostované v NEF. Služba ADAE následně komunikuje s různými zdroji dat v síti, jako je Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)), Unified Data Repository ([UDR](/mobilnisite/slovnik/udr/)) nebo jiné síťové funkce ([NF](/mobilnisite/slovnik/nf/)), aby shromáždila, zpracovala a doručila požadované analytické reporty zpět k AF.

Pracovní postup začíná tím, že AF odešle do NEF požadavek Nnef_AnalyticsExposure_Subscribe, který specifikuje typ požadované analýzy (např. vzorce mobility na úrovni uživatele, analýza uživatelského zážitku ze služby, trendy výkonnosti sítě), cílovou skupinu uživatelských zařízení (UE) a kritéria pro reportování (periodické nebo spouštěné událostí). NEF, vystupující jako poskytovatel služby ADAE, žádost AF autentizuje a autorizuje na základě politik operátora. Následně přeloží aplikační analytický požadavek do interních síťových procedur, přičemž může například dotazovat NWDAF na výpočet analytických údajů nebo získávat uložená data z UDR.

Klíčovými komponentami v architektuře ADAE jsou NEF (který hostuje službu ADAE), konzument AF a producent analytických dat (jako je NWDAF). Rozhraní mezi AF a NEF pro ADAE je definováno jako Nnef_AnalyticsExposure. Datový model pro analytické údaje je standardizován a pokrývá kategorie jako mobilita UE, komunikační vzorce a uživatelský zážitek ze služby, což zajišťuje interoperabilitu. Dodávaný analytický report obsahuje poznatky jako předpokládaný pohyb UE, očekávaná udržitelnost QoS nebo indikátory abnormálního zážitku ze služby, naformátované podle datových struktur definovaných 3GPP.

Úlohou ADAE je poskytnout zabezpečený, politikami řízený a standardizovaný kanál, který aplikacím umožní využívat síťovou inteligenci bez nutnosti přímé, proprietární integrace s jednotlivými síťovými funkcemi. Umožňuje případy užití jako řízení davu, optimalizace rozšířené reality nebo prediktivní zajištění služeb tím, že aplikacím umožňuje činit rozhodnutí založená na datech na základě analytických údajů ze sítě v reálném čase nebo historických. Služba podporuje jak pull (request-response), tak push (subscription-notification) modely pro doručování dat, což nabízí flexibilitu vývojářům aplikací.

## K čemu slouží

ADAE bylo vytvořeno, aby reagovalo na rostoucí poptávku vertikálních odvětví a poskytovatelů aplikací po přístupu k hodnotným analytickým údajům odvozeným z dat 5G sítě. Před jeho standardizací měly aplikace pouze omezené, nestandardizované způsoby získávání síťových poznatků, často spoléhající na bilaterální dohody nebo proprietární [API](/mobilnisite/slovnik/api/), které nebyly škálovatelné, bezpečné ani interoperabilní napříč různými sítěmi operátorů. To bránilo vývoji inovativních služeb, které by se mohly dynamicky přizpůsobovat na základě síťových podmínek nebo chování uživatelů.

Motivace vychází z vize 5G o zpřístupňování a programovatelnosti sítě. Zatímco [NEF](/mobilnisite/slovnik/nef/) již zpřístupňovalo různé síťové schopnosti (jako je řízení QoS), existovala konkrétní mezera v zpřístupňování zpracovaných analytických údajů, nikoli pouze surových událostí nebo stavů. [NWDAF](/mobilnisite/slovnik/nwdaf/) byla definována interně pro automatizaci sítě, ale chybělo standardizované externí rozhraní pro aplikace, aby tyto analytické údaje mohly konzumovat. ADAE tuto mezeru zaplňuje definováním konzistentního služebního rozhraní, datových modelů a autorizačního rámce, což umožňuje operátorům bezpečně monetizovat síťová data a vývojářům vytvářet chytřejší aplikace.

Řeší problém izolované síťové inteligence tím, že poskytuje řízený kanál, přes který mohou být bohaté analytické údaje – jako předpovědi mobility uživatelů, trendy agregované šířky pásma relací nebo detekce anomálií – bezpečně sdíleny s důvěryhodnými třetími stranami. To umožňuje nové obchodní modely a zlepšuje výkon aplikací, čímž přispívá k celkovému ekosystému 5G konceptu sítě jako služby a podpory vertikálních odvětví.

## Klíčové vlastnosti

- Standardizované služební rozhraní (SBI) pro zpřístupňování analytických údajů (Nnef_AnalyticsExposure)
- Podpora odběrového (subscription-based) a request-response modelu doručování analytických údajů
- Autorizace a řízení přístupu k požadavkům AF na základě politik
- Zpřístupnění kategorií analytických údajů jako mobilita UE, komunikace a uživatelský zážitek ze služby
- Integrace s NWDAF a dalšími síťovými zdroji dat pro generování analytických údajů
- Standardizované datové modely pro analytické reporty zajišťující interoperabilitu

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.559** (Rel-19) — Application Data Analytics Enablement Services
- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications

---

📖 **Anglický originál a plná specifikace:** [ADAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/adae/)
