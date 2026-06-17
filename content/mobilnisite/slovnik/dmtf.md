---
slug: "dmtf"
url: "/mobilnisite/slovnik/dmtf/"
type: "slovnik"
title: "DMTF – Distributed Management Task Force"
date: 2025-01-01
abbr: "DMTF"
fullName: "Distributed Management Task Force"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dmtf/"
summary: "DMTF je celosvětová průmyslová organizace pro standardizaci, která vyvíjí, udržuje a podporuje interoperabilní standardy a iniciativy pro správu podnikových a telekomunikačních IT systémů. Její standa"
---

DMTF je Distributed Management Task Force, celosvětová průmyslová organizace pro standardizaci, která vyvíjí interoperabilní standardy pro správu telekomunikačních a podnikových IT systémů.

## Popis

Distributed Management Task Force (DMTF) je klíčové průmyslové konsorcium, nikoli interní protokol 3GPP, avšak jeho standardy jsou v ekosystému 3GPP odkazovány a využívány pro funkce správy sítě. Je to organizace složená z technologických společností zaměřená na vývoj interoperabilních standardů pro správu [IT](/mobilnisite/slovnik/it/) systémů, včetně těch v cloudu, virtualizaci a telekomunikačních sítích. Práce DMTF poskytuje základní rámce a protokoly pro správu heterogenní, více-dodavatelské infrastruktury.

Z architektonického hlediska standardy DMTF definují informační modely, protokoly a profily. Základním kamenem je Common Information Model ([CIM](/mobilnisite/slovnik/cim/)), konceptuální schéma, které popisuje spravované prvky v síti nebo IT prostředí (např. počítače, sítě, aplikace, služby) způsobem nezávislým na dodavateli. CIM je vyjádřen v jednotném modelovacím jazyce a poskytuje konzistentní definici a strukturu pro management data. Nad CIM specifikuje DMTF protokoly jako sadu Web-Based Enterprise Management (WBEM), která zahrnuje standardy pro zjišťování, komunikaci (jako CIM-XML nebo CIM přes [HTTPS](/mobilnisite/slovnik/https/)) a dotazování (CQL). Tyto protokoly umožňují systémům správy komunikovat se spravovanými zařízeními pomocí standardizovaného [API](/mobilnisite/slovnik/api/).

V telekomunikačním kontextu, jako je síť 3GPP, jsou standardy DMTF často používány v management rovině, zejména v Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)) a Network Management Systems ([NMS](/mobilnisite/slovnik/nms/)) pro správu fyzických a virtualizovaných síťových funkcí. Například virtualizační infrastruktura ([NFVI](/mobilnisite/slovnik/nfvi/)), která hostí funkce 5G Core (jako [AMF](/mobilnisite/slovnik/amf/), SMF) v cloudovém prostředí, je často spravována pomocí rozhraní odvozených od DMTF. Standard DMTF Redfish, moderní RESTful API a specifikace datového modelu pro správu hardwaru, je stále více používán pro správu serverů, úložišť a síťových komponent v datových centrech, která hostí telekomunikační úlohy.

Jeho role spočívá v umožnění interoperability a zjednodušené integrace. Poskytnutím společného jazyka a sady operací pro správu umožňují standardy DMTF, aby síťové vybavení od různých dodavatelů, virtualizované síťové funkce (VNF) a cloudové platformy byly spravovány jedním koherentním systémem správy. To snižuje provozní složitost a náklady pro síťové operátory nasazující více-dodavatelské 5G sítě a cloud-nativní infrastrukturu.

## K čemu slouží

DMTF byla zformována k řešení kritického problému interoperability správy v stále složitějších, distribuovaných IT prostředích. Před takovými standardy používal každý dodavatel hardwaru a poskytovatel softwaru proprietární rozhraní, datové modely a protokoly pro správu. To vytvářelo obrovské integrační výzvy pro podniky a poskytovatele služeb, kteří provozovali více-dodavatelská prostředí, což vedlo k vysokým provozním nákladům, fragmentované přehlednosti a omezeným možnostem automatizace.

Vytvoření Common Information Model (CIM) bylo základní motivací. Cílem bylo poskytnout jednotné schéma, které by mohlo reprezentovat jakýkoli spravovaný prostředek, od ventilátoru serveru po přidělení CPU virtuálnímu stroji. To umožnilo management softwaru porozumět a ovládat různé prvky bez nutnosti vlastních adaptérů pro každý z nich. V kontextu telekomunikací, jak se sítě vyvíjely od proprietárních hardwarových zařízení k virtualizovanému, cloud-nativnímu softwaru běžícímu na komerčním hardwaru (COTS), se potřeba standardizovaných postupů IT správy stala prvořadou. Standardy DMTF poskytly most mezi telekomunikačně specifickou správou definovanou 3GPP (např. pro 5G Core) a podkladovou výpočetní, úložnou a síťovou infrastrukturu spravovanou jako generické IT prostředky.

Historicky jeho adopce v rámci 3GPP odráží konvergenci IT a telekomunikací (ICT) v průmyslu. Jak 5G sítě přijímají Network Function Virtualization (NFV) a cloudové principy, správa podkladové infrastruktury se přizpůsobuje IT best practices. Standardy DMTF jako Redfish nabízejí moderní, API-řízený přístup k správě hardwaru, který je zásadní pro automatizaci životního cyklu cloudové infrastruktury, na níž jsou 5G služby budovány, a řeší tak potřebu agility, škálovatelnosti a snížení nákladů v moderních síťových operacích.

## Klíčové vlastnosti

- Vývoj Common Information Model (CIM) pro reprezentaci prostředků nezávislou na dodavateli
- Specifikace protokolů Web-Based Enterprise Management (WBEM) pro výměnu dat
- Vytvoření standardu Redfish, moderního RESTful API pro správu hardwaru
- Definuje profily a implementační příručky pro specifické technologické domény (např. servery, virtualizaci)
- Podporuje interoperabilitu napříč více-dodavatelskou IT a síťovou infrastrukturou
- Poskytuje základní modely pro správu cloudových a virtualizačních platforem

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.198** (Rel-9) — OSA API Overview Specification

---

📖 **Anglický originál a plná specifikace:** [DMTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmtf/)
