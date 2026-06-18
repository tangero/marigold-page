---
slug: "vr"
url: "/mobilnisite/slovnik/vr/"
type: "slovnik"
title: "VR – Virtualized Resource"
date: 2026-01-01
abbr: "VR"
fullName: "Virtualized Resource"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vr/"
summary: "Abstraktní reprezentace výpočetních, úložných nebo síťových hardwarových schopností spravovaných virtualizačním softwarem. V 3GPP jsou VR základními stavebními bloky pro nasazování síťových funkcí jak"
---

VR (Virtualized Resource, virtualizovaný prostředek) je abstraktní reprezentace výpočetních, úložných nebo síťových hardwarových schopností, které představují základní stavební bloky pro nasazování síťových funkcí jako softwaru na cloudové infrastruktuře.

## Popis

Virtualized Resource (VR, virtualizovaný prostředek) je klíčový koncept v rámci 3GPP management framework, zejména pro správu virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) v cloud-nativním prostředí. Představuje logickou abstrakci fyzického prostředku, jako je procesorové jádro, blok paměti, úložný svazek nebo virtuální síťová karta (vNIC). Tyto abstrakce vytváří a spravuje virtualizační vrstva (např. hypervizor nebo kontejnerový runtime) nad fyzickým hardwarem. 3GPP management systém, definovaný ve specifikacích jako 28.520 (Management and Orchestration, [MANO](/mobilnisite/slovnik/mano/)), s VR interaguje za účelem jejich alokace, monitorování a orchestrace pro instanciaci a škálování síťových funkcí.

Architektura zahrnuje několik klíčových entit. Virtualized Infrastructure Manager ([VIM](/mobilnisite/slovnik/vim/)) je zodpovědný za řízení a správu výpočetních, úložných a síťových prostředků [NFVI](/mobilnisite/slovnik/nfvi/) (Network Functions Virtualization Infrastructure). VIM tyto prostředky vystavuje jako VR. [NFV](/mobilnisite/slovnik/nfv/) Orchestrator ([NFVO](/mobilnisite/slovnik/nfvo/)) a VNF Manager ([VNFM](/mobilnisite/slovnik/vnfm/)) pak tyto VR, popsané v VNF Descriptor (VNFD), používají k nasazení VNF. VNFD definuje požadavky VNF z hlediska Virtualized Compute, Storage, and Network Resources (Vnfc, VnfStorage, VnfVirtualLink). Během instanciace systém MANO mapuje tyto požadavky na dostupné VR v infrastruktuře, čímž vytváří potřebné virtuální stroje ([VM](/mobilnisite/slovnik/vm/)) nebo kontejnery se specifikovaným CPU, pamětí a síťovou konektivitou.

VR jsou dynamické a elastické. Jejich životní cyklus (vytvoření, změna, ukončení) je spravován prostřednictvím standardizovaných rozhraní, jako je referenční bod Or-Vi mezi NFVO a VIM. Monitorování metrik výkonu VR (např. využití CPU, využití paměti, I/O rychlosti) je také standardizováno, což umožňuje systému MANO provádět automatizované škálovací akce. Například pokud VNF zaznamená vysoké zatížení, může VNFM požádat prostřednictvím NFVO o další virtualizované výpočetní prostředky (více VR) od VIM, což vede k horizontálnímu škálování instance VNF. Tato abstrakce je klíčová pro dosažení cílů NFV: hardwarové nezávislosti, efektivního multi-tenancy a agilního nasazování služeb.

## K čemu slouží

Koncept Virtualized Resource byl zaveden, aby řešil omezení tradičních telekomunikačních sítí postavených na proprietárních fyzických zařízeních. Tato zařízení byla pevně svázána se specifickým hardwarem, což vedlo k dlouhým cyklům pořizování a nasazování, neefektivnímu využití prostředků (často předimenzovaných na špičkovou kapacitu) a vysokým provozním nákladům. Přechod k Network Functions Virtualization (NFV), prosazovaný průmyslovými fóry jako ETSI ISG NFV a přijatý 3GPP, vyžadoval standardizovaný způsob modelování a správy softwarových prostředků, které měly nahradit fyzické síťové funkce.

Vytvoření abstrakce VR ve specifikacích 3GPP, zejména od Rel-13 výše, poskytlo tento standardizovaný model. Vyřešilo problém heterogenity cloudové infrastruktury definováním společné sady typů prostředků (výpočetní, úložné, síťové) a jejich management rozhraní, bez ohledu na podkladový hypervizor (VMware, KVM atd.) nebo dodavatele hardware. To umožňuje síťovým operátorům nasazovat VNF od různých dodavatelů na společném sdíleném fondu fyzických prostředků, což umožňuje skutečnou multi-vendor interoperabilitu a zabraňuje vendor lock-in na vrstvě infrastruktury. Model VR je základem pro automatizaci, elastické škálování a efektivní "cloudifikaci" mobilních sítí, což je nezbytné pro podporu různorodých služeb 5G a dalších generací s různými nároky.

## Klíčové vlastnosti

- Abstrakce fyzického výpočetního, úložného a síťového hardware
- Standardizovaný životní cyklus správy (vytvoření, škálování, ukončení)
- Definované výkonnostní metriky a možnosti monitorování
- Mapování požadavků VNF na dostupné prostředky infrastruktury
- Podpora multi-tenancy a izolace prostředků
- Správa prostřednictvím standardizovaných rozhraní (např. Or-Vi) v rámci MANO framework

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)
- [NFVI – Network Functions Virtualization Infrastructure](/mobilnisite/slovnik/nfvi/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.873** (Rel-18) — Technical Report on IMS Multimedia Telephony Service Enhancements
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TR 26.812** (Rel-18) — Technical Report
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [VR na 3GPP Explorer](https://3gpp-explorer.com/glossary/vr/)
