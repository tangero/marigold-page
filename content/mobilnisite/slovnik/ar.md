---
slug: "ar"
url: "/mobilnisite/slovnik/ar/"
type: "slovnik"
title: "AR – Application Relation"
date: 2026-01-01
abbr: "AR"
fullName: "Application Relation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ar/"
summary: "Application Relation (AR) je standardizované rozhraní mezi sítí 3GPP a externími aplikačními servery, které umožňuje vystavení služeb a přístup k síťovým schopnostem. Poskytuje bezpečný a standardizov"
---

AR je standardizované rozhraní mezi sítí 3GPP a externími aplikačními servery, které umožňuje bezpečné vystavení služeb a přístup k síťovým schopnostem.

## Popis

Application Relation je základní architektonický koncept ve standardech 3GPP, který definuje vztah a interakci mezi doménou sítě 3GPP a externími poskytovateli aplikací. Vytváří standardizovaný rámec pro vystavení služeb, který umožňuje autorizovaným aplikacím třetích stran bezpečně přistupovat k síťovým schopnostem a informacím. AR zahrnuje protokoly, rozhraní, bezpečnostní mechanismy a obchodní dohody nezbytné pro tuto interakci a slouží jako hranice, na které jsou síťové služby zpřístupněny aplikační vrstvě.

Z architektonického hlediska je AR implementována prostřednictvím specifických referenčních bodů a síťových funkcí navržených pro vystavení služeb. V dřívějších vydáních 3GPP bylo toho primárně dosaženo prostřednictvím rámce Open Service Access ([OSA](/mobilnisite/slovnik/osa/)), který se později vyvinul ve složitější architektury, jako je IP Multimedia Subsystem (IMS) Service Capability Interaction Manager ([SCIM](/mobilnisite/slovnik/scim/)) a Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) v 4G, což nakonec vedlo k Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) v 5G. Tyto funkce fungují jako brány, které řídí a zprostředkovávají přístup k síťovým službám, jako je poloha uživatele, informace o přítomnosti, řízení kvality služeb (QoS) a spouštění zařízení.

Provoz AR zahrnuje několik klíčových komponent: expoziční funkci (např. NEF, SCEF), která ověřuje žádosti aplikací a překládá je do příkazů vnitřní sítě; aplikační server, který se nachází v externí doméně a využívá vystavené schopnosti; a standardizovaná [API](/mobilnisite/slovnik/api/) (Application Programming Interfaces), která definují komunikační protokol. Bezpečnost je prvořadá a je vynucována prostřednictvím mechanismů autentizace, autorizace a účtování ([AAA](/mobilnisite/slovnik/aaa/)), často zahrnujících OAuth 2.0 a správu API klíčů. AR také definuje modely účtování a smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) mezi síťovým operátorem a poskytovatelem aplikací.

V síťovém ekosystému hraje AR klíčovou roli při umožňování nových obchodních modelů a inovací služeb. Umožňuje operátorům zpeněžit jejich síťová aktiva nad rámec základní konektivity tím, že zpřístupňuje cenné schopnosti vertikálním odvětvím (např. automobilový průmysl, zdravotnictví, IoT). Pro vývojáře aplikací poskytuje konzistentní rozhraní na úrovni operátora, které umožňuje obohatit jejich služby o síťovou inteligenci, jako je zajištění nízké latence pro aplikace v reálném čase nebo probouzení zařízení pro příjem dat, což je zásadní pro zařízení IoT s omezenou kapacitou baterie.

## K čemu slouží

Application Relation byla vytvořena, aby řešila rostoucí potřebu bezpečné a standardizované metody pro interakci aplikací třetích stran s možnostmi telekomunikační sítě. Před její standardizací byla integrace aplikací často dosahována prostřednictvím proprietárních, na dodavateli závislých rozhraní, která byla nákladná, složitá a bránila inovacím služeb a interoperabilitě. AR poskytuje společný rámec, který odděluje vývoj aplikací od podkladové síťové technologie, a podporuje tak otevřený ekosystém.

Historicky byl tento koncept představen ve vydání 3GPP Release 6 jako součást snahy o všeprotokolové IP sítě a vývoj IMS. Vyřešil problém 'zahrad s pevnou zdí' tím, že umožnil důvěryhodným externím partnerům přistupovat k síťovým službám kontrolovaným způsobem. To operátorům otevřelo nové zdroje příjmů prostřednictvím vystavení služeb a umožnilo vytváření bohatších, kontextově povědomých aplikací, které mohly využívat síťová data, jako je poloha uživatele nebo stav relace.

Vývoj AR odráží měnící se prostředí telekomunikací, od služeb zaměřených na hlas k datově řízeným aplikacím a internetu věcí. Řeší omezení předchozích ad-hoc integrací tím, že poskytuje škálovatelné, bezpečné a účtovatelné rozhraní. To je zásadní pro podporu různorodých požadavků vertikálních odvětví v 4G a 5G, kde aplikace v automobilovém průmyslu, průmyslové automatizaci a zdravotnictví vyžadují spolehlivý přístup k parametrům řízeným sítí, jako je latence, šířka pásma a správa zařízení.

## Klíčové vlastnosti

- Standardizovaná API rozhraní pro vystavení síťových schopností
- Bezpečné mechanismy autentizace a autorizace pro přístup aplikací
- Zprostředkování a vynucování politik mezi externími aplikacemi a síťovými funkcemi
- Podpora různorodých schopností služeb (QoS, poloha, spouštění zařízení)
- Rozhraní pro účtování a fakturaci pro zpeněžení vystavených služeb
- Škálovatelná architektura podporující četné poskytovatele aplikací

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 22.823** (Rel-16) — IMS enhancements for new real-time communication services
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TR 22.873** (Rel-18) — Technical Report on IMS Multimedia Telephony Service Enhancements
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.812** (Rel-18) — Technical Report
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [AR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ar/)
