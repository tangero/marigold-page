---
slug: "cs1"
url: "/mobilnisite/slovnik/cs1/"
type: "slovnik"
title: "CS1 – Capability Set 1"
date: 2025-01-01
abbr: "CS1"
fullName: "Capability Set 1"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cs1/"
summary: "Capability Set 1 (CS1) je počáteční standardizovaná sada schopností pro IP Multimedia Subsystem (IMS) definovaná ve 3GPP Release 8. Stanovuje základní servisní architekturu pro poskytování multimediál"
---

CS1 je počáteční standardizovaná sada schopností pro IP Multimedia Subsystem (IMS), která stanovuje základní servisní architekturu pro poskytování multimediálních služeb přes paketově přepínané sítě.

## Popis

Capability Set 1 (CS1) představuje komplexní základní specifikaci pro architekturu IP Multimedia Subsystem (IMS) standardizovanou ve 3GPP Release 8. Definuje kompletní sadu funkčních prvků, protokolů, rozhraní a procedur potřebných k navázání, správě a ukončení multimediálních relací přes IP sítě. Architektura je postavena kolem protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) jako primárního signalizačního protokolu, s detailními specifikacemi pro registraci, navázání relace, spouštění služeb a propojení s existujícími okruhově přepínanými sítěmi.

Architektura CS1 se skládá z několika klíčových funkčních komponent včetně Call Session Control Functions (CSCFs), které zajišťují směrování signalizace a řízení relací, Home Subscriber Servers ([HSS](/mobilnisite/slovnik/hss/)) pro správu profilů účastníků a autentizaci, Application Servers ([AS](/mobilnisite/slovnik/as/)) hostující servisní logiku a Media Resource Functions ([MRF](/mobilnisite/slovnik/mrf/)) poskytující schopnosti zpracování médií. Tyto prvky spolupracují prostřednictvím standardizovaných rozhraní (jako Cx, Sh a [ISC](/mobilnisite/slovnik/isc/)) k poskytování end-to-end multimediálních služeb. Architektura podporuje jak mobilní, tak pevné přístupové sítě, což umožňuje konvergenci různých přístupových technologií.

CS1 specifikuje detailní procedury pro poskytování služeb, včetně počáteční registrace, autentizace pomocí IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), navazování relací s vyjednáváním kvality služeb (QoS) a spouštění služeb na základě initial Filter Criteria (iFC). Definuje komplexní propojení s legacy sítěmi prostřednictvím specifických funkcí jako Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a IMS Media Gateway ([IM-MGW](/mobilnisite/slovnik/im-mgw/)) pro připojení k okruhově přepínaným sítím. Specifikace také zahrnuje detailní architektury účtování, bezpečnostní mechanismy a rámce pro řízení politik, které tvoří základ pro komerční nasazení IMS.

Technická implementace CS1 vyžaduje striktní dodržování standardizovaných protokolů včetně SIP (RFC 3261), Session Description Protocol (SDP), Diameter pro autentizaci a autorizaci a Real-time Transport Protocol (RTP) pro přenos médií. Architektura používá vrstvený přístup oddělující transportní, řídicí a servisní rovinu, což umožňuje nezávislý vývoj každé vrstvy. Komplexní povaha CS1 zajišťuje, že implementace od různých dodavatelů mohou bezproblémově interoperovat, čímž vytváří globální ekosystém pro multimediální služby.

## K čemu slouží

CS1 byl vytvořen za účelem zavedení standardizovaného, interoperabilního rámce pro poskytování multimediálních služeb přes IP sítě, který řešil fragmentaci proprietárních VoIP a multimediálních řešení existujících před standardizací 3GPP. Před CS1 různí dodavatelé a operátoři implementovali nekompatibilní IP hlasová a video řešení s použitím různých protokolů, architektur a sad funkcí, což činilo interoperabilitu mezi sítěmi téměř nemožnou a brzdilo růst multimediálních služeb. Telekomunikační průmysl potřeboval společný základ, který by umožnil globální roaming, interoperabilitu služeb a úspory z rozsahu pro výrobce zařízení a poskytovatele služeb.

Primární motivací pro vývoj CS1 bylo vytvořit architekturu připravenou na budoucnost, která by podporovala přechod od okruhově přepínaných hlasových služeb k paketově přepínaným multimediálním službám při zachování úrovně spolehlivosti, bezpečnosti a kvality na úrovni operátora. Existující internetová VoIP řešení postrádala potřebné mechanismy pro zákonné odposlechy, tísňové služby, záruky kvality služeb a sofistikované modely účtování požadované telekomunikačními operátory. CS1 tato omezení řešil začleněním funkcí na úrovni telekomunikací do IP architektury, což operátorům umožnilo nabízet diferencované služby při zachování regulatorní shody.

CS1 také sloužil jako základ pro konvergenci sítí, což umožnilo pevným a mobilním operátorům nasadit společnou platformu pro poskytování služeb. Standardizací kompletní sady schopností potřebných pro komerční nasazení IMS umožnilo 3GPP průmyslu posunout se za proprietární implementace a vytvořit živý ekosystém interoperabilních síťových prvků, zařízení a aplikací. Tato standardizace byla klíčová pro snížení nákladů na nasazení, zkrácení doby uvedení nových služeb na trh a zajištění konzistentního používání multimediálních služeb účastníky napříč různými sítěmi a zařízeními.

## Klíčové vlastnosti

- Kompletní specifikace architektury IMS včetně všech funkčních prvků a referenčních bodů
- Standardizovaná signalizace založená na SIP pro navázání, modifikaci a ukončení relace
- Komplexní rámec pro autentizaci a zabezpečení využívající IMS AKA
- Detailní specifikace propojení pro připojení k legacy okruhově přepínaným sítím
- Podpora více přístupových technologií včetně UMTS, LTE a pevného širokopásmového připojení
- Integrovaná architektura řízení politik a účtování pro komerční poskytování služeb

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [CS1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/cs1/)
