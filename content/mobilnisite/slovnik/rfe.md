---
slug: "rfe"
url: "/mobilnisite/slovnik/rfe/"
type: "slovnik"
title: "RFE – Routing Functional Entity"
date: 2025-01-01
abbr: "RFE"
fullName: "Routing Functional Entity"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rfe/"
summary: "Routing Functional Entity (RFE, směrovací funkční entita) je logická funkce v jádrové síti 3GPP, primárně v GSM a UMTS, odpovědná za určení dalšího směrovacího uzlu pro signalizační zprávy. Nachází se"
---

RFE je logická funkce v jádrové síti 3GPP, která určuje další směrovací uzel pro signalizační zprávy v uzlech jako MSC nebo SGSN, aby umožnila spolehlivé doručování zpráv.

## Popis

Routing Functional Entity (RFE, směrovací funkční entita) je základní logická komponenta definovaná v raných specifikacích 3GPP pro přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) a paketů ([PS](/mobilnisite/slovnik/ps/)) v jádrových sítích. Není to samostatný fyzický uzel, ale funkční schopnost vestavěná do prvků jádrové sítě, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Gateway GPRS Support Node (GGSN). Jejím hlavním úkolem je provádět směrovací rozhodnutí pro signalizační zprávy vyměňované mezi síťovými entitami přes rozhraní jako B, C, D, E, F, G a Gn/Gp. RFE zkoumá obsah příchozích signalizačních zpráv – zejména adresní informace jako Global Titles ([GT](/mobilnisite/slovnik/gt/)), [SS7](/mobilnisite/slovnik/ss7/) Point Codes nebo IP adresy – a určuje vhodný další síťový uzel nebo aplikaci, kam má být zpráva přeposlána.

Architektonicky RFE spolupracuje s dalšími funkčními entitami, jako jsou Mobility Management ([MM](/mobilnisite/slovnik/mm/)) a Call/Session Control (CSC). Například když MSC přijme požadavek na aktualizaci polohy z Visitor Location Register (VLR), může být vyvolána RFE uvnitř MSC, aby nasměrovala následnou autentizační zprávu na správný Home Location Register (HLR). Využívá směrovací tabulky a konfigurační data, která mohou být naplněna staticky nebo dynamicky pomocí protokolů jako SCCP ze sady SS7 nebo IP-based DNS. V jádrové síti GPRS RFE v SGSN směruje signalizační zprávy GTP-C ke správnému GGSN na základě Access Point Name (APN) rozlišeného během aktivace PDP kontextu.

Fungování RFE je klíčové pro škálovatelnost a spolehlivost jádrové sítě. Umožňuje nepřímou komunikaci, kde uzly nepotřebují trvalé přímé spojení se všemi ostatními uzly. Tím, že činí směrovací rozhodnutí na základě standardizovaných adresních schémat, usnadňuje funkce jako roamování, předávání hovorů mezi MSC (inter-MSC handover) a načítání dat účastníka z HLR. Její funkčnost je specifikována v technických specifikacích jako 23.002 (síťová architektura), 29.002 (MAP) a podrobně popsána v 25.331 (RRC) pro určité scénáře a 25.931 (koncepty IMS). Zatímco tento termín je méně běžný v čistých specifikacích 4G/5G – kde je směrování více integrováno do architektury založené na službách s Diameter nebo HTTP/2 – základní směrovací funkce zůstává nezbytná.

## K čemu slouží

RFE byla konceptualizována, aby řešila základní potřebu škálovatelného a flexibilního směrování signalizace v digitálních celulárních sítích (GSM), které se vyvinuly do UMTS. Rané mobilní sítě vyžadovaly mechanismus pro doručování zpráv řídicí roviny (pro registraci, zřizování hovorů, SMS) mezi četnými distribuovanými síťovými uzly (MSC, HLR, VLR) bez nutnosti plné propojenosti přímými spoji. Vyhrazená směrovací funkce uvnitř každého uzlu abstrahuje topologii sítě a zjednodušuje návrh dalších funkčních entit, které mohou jednoduše předat zprávy místní RFE k doručení.

Řešila problémy spojené s růstem sítě, roamováním a interoperabilitou více dodavatelů. Standardizací chování RFE mohly MSC od různých dodavatelů předvídatelně vyměňovat signalizaci. Také umožnila pokročilé funkce mobility; například během předání mezi MSC může RFE v kotvícím MSC směrovat následnou signalizaci na nové obsluhující MSC. Vytvoření RFE bylo motivováno principy Intelligent Network (IN) a Signalizačního systému č. 7 (SS7), kde jasné oddělení přepojovacích a směrovacích funkcí zlepšuje robustnost sítě a zavádění služeb. V paketovém jádru poskytovala podobné výhody pro signalizaci GTP, umožňujíc SGSN směrovat relace na příslušný GGSN na základě služby zvolené účastníkem (APN).

## Klíčové vlastnosti

- Logická funkce vestavěná v uzlech jádrové sítě (MSC, SGSN, GGSN) pro směrování signalizačních zpráv
- Činí směrovací rozhodnutí na základě adresních informací (Global Title, IP adresa, APN)
- Umožňuje nepřímou komunikaci a snižuje potřebu plné propojenosti mezi uzly
- Kritická pro podporu mobility účastníků a roamování přes hranice sítí
- Využívá směrovací tabulky a může komunikovat s externími směrovacími databázemi (např. DNS pro GPRS)
- Základní pro signalizační architektury založené na SS7/MAP a GTP v sítích 2G/3G

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [RFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfe/)
