---
slug: "osa"
url: "/mobilnisite/slovnik/osa/"
type: "slovnik"
title: "OSA – Open Services Architecture"
date: 2025-01-01
abbr: "OSA"
fullName: "Open Services Architecture"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/osa/"
summary: "Open Services Architecture (OSA) je standardizovaný rámec pro vytváření a nasazování síťových služeb nezávislý na dodavateli. Umožňuje poskytovatelům aplikací třetích stran přístup k síťovým schopnost"
---

OSA je standardizovaný rámec pro vytváření a nasazování síťových služeb nezávislý na dodavateli, který umožňuje poskytovatelům třetích stran přístup k síťovým schopnostem prostřednictvím otevřených API.

## Popis

Open Services Architecture (OSA) je klíčovým prvkem aplikační vrstvy 3GPP, navrženým tak, aby poskytoval standardizovaný, bezpečný a škálovatelný způsob interakce aplikací se síťovými schopnostmi. Je založena na modelu klient-server, kde Application Server ([AS](/mobilnisite/slovnik/as/)) funguje jako klient a OSA Gateway, často implementovaná jako součást IP Multimedia Subsystem (IMS) Service Capability Interaction Manager ([SCIM](/mobilnisite/slovnik/scim/)), funguje jako server. Architektura definuje sadu Service Capability Features (SCFs), což jsou abstraktní reprezentace síťových funkcionalit, jako je řízení hovorů, lokalizace uživatele, stavová informace (presence) a zasílání zpráv. Tyto SCFs jsou zpřístupněny aplikacím prostřednictvím standardizovaných, na technologii nezávislých aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), která jsou historicky sladěna se specifikacemi Parlay. OSA Gateway mapuje tato volání API na podkladové síťové protokoly, jako jsou [SIP](/mobilnisite/slovnik/sip/), [MAP](/mobilnisite/slovnik/map/) nebo Diameter, a poskytuje tak klíčovou abstraktní vrstvu, která chrání vývojáře aplikací před složitostmi jádrové sítě.

Rámec OSA je postaven na robustní bezpečnostní a správní infrastruktuře. Zahrnuje Framework API, což je povinná sada funkcionalit pro všechny implementace OSA. Tento rámec zajišťuje kritické úlohy, jako je ověřování a autorizace aplikací, zjišťování dostupných SCFs, navazování zabezpečených komunikačních relací a správa integrity. Bezpečnostní model zajišťuje, že pouze autorizované aplikace mohou přistupovat ke konkrétním síťovým schopnostem, často na základě smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). Z provozní perspektivy OSA usnadňuje vytvoření živého ekosystému, kde mohou operátoři bezpečně otevřít své sítě poskytovatelům služeb třetích stran, což umožňuje širokou škálu přidaných služeb bez ohrožení síťové bezpečnosti nebo stability.

V rámci sítě hraje OSA klíčovou roli při umožnění bezproblémové integrace aplikací s IMS a dalšími doménami jádrové sítě. Je klíčovým prvkem pro koncept 'otevřené sítě', který se odklání od vertikálně integrovaných, na dodavateli závislých prostředí pro tvorbu služeb. Architektura podporuje jak stavové, tak bezstavové interakce, což umožňuje složitou servisní logiku zahrnující více síťových schopností. Její návrh podporuje opětovnou použitelnost a interoperabilitu, protože aplikace napsané pro implementaci OSA jednoho operátora mohou být v zásadě s minimálními změnami přeneseny k jinému. To bylo zásadní pro vývoj mobilních sítí směrem k poskytování pokročilých komunikačních služeb, které spojují telekomunikační a [IT](/mobilnisite/slovnik/it/) funkcionality.

## K čemu slouží

OSA byla vytvořena, aby řešila zásadní výzvu pomalé a nákladné inovace služeb v tradičních telekomunikačních sítích. Před jejím zavedením bylo vytváření nových síťových služeb složitý proces těsně svázaný se specifickým zařízením dodavatele a proprietárními rozhraními. Tento přístup 'uzavřené zahrady' dusil inovace, prodlužoval dobu vývoje a uzamykal operátory do ekosystémů jediného dodavatele. Primárním účelem OSA je tyto bariéry odstranit standardizací rozhraní mezi aplikacemi a síťovou funkcionalitou.

Historický kontext vývoje OSA spočívá v přechodu od okruhově přepínaných sítí 2G k paketově přepínaným, IP-based sítím 3G a později 4G/5G. Jak se sítě stávaly schopnějšími a datově orientovanými, poptávka po inovativních službách (mimo hlas a [SMS](/mobilnisite/slovnik/sms/)) exponenciálně rostla. 3GPP ve spolupráci s Parlay Group definovala OSA, aby poskytla budoucím výzvám odolnou, na technologii nezávislou metodu pro zpřístupňování služeb. Řeší problém, jak bezpečně a efektivně umožnit externím aplikacím – jak od operátora, tak od vývojářů třetích stran – využívat vnitřní síťové schopnosti, jako je ověřování uživatele, lokalizace a řízení relace.

Řešením těchto problémů OSA přímo umožňuje obchodní model sítě jako platformy. Umožňuje operátorům monetizovat jejich síťové prostředky nad rámec základní konektivity a podporuje partnerství s vývojáři aplikací a poskytovateli obsahu. Jednalo se o strategický posun od pouhých poskytovatelů konektivity k tvůrcům širšího ekosystému digitálních služeb, což je princip, který zůstává ústřední pro moderní síťové architektury, jako je 5G Service-Based Architecture (SBA).

## Klíčové vlastnosti

- Standardizovaná, na technologii nezávislá API (Parlay/OSA) pro zpřístupnění síťových schopností
- Komplexní Framework API pro ověřování, autorizaci a zjišťování služeb
- Abstrakce síťových schopností do znovupoužitelných Service Capability Features (SCFs)
- Robustní bezpečnostní model řídící přístup aplikací třetích stran k síťovým zdrojům
- Podpora jak stavových (např. řízení hovorů), tak bezstavových servisních interakcí
- Nezávislost na podkladových síťových protokolech (SIP, MAP, Diameter)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SCIM – Service Capability Interaction Manager](/mobilnisite/slovnik/scim/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.240** (Rel-19) — 3GPP Generic User Profile (GUP) Architecture
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [OSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/osa/)
