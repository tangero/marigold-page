---
slug: "stp"
url: "/mobilnisite/slovnik/stp/"
type: "slovnik"
title: "STP – Service Platform Trigger Points"
date: 2025-01-01
abbr: "STP"
fullName: "Service Platform Trigger Points"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/stp/"
summary: "Service Platform Trigger Points (STP, spouštěcí body servisní platformy) jsou standardizované referenční body v architektuře 3GPP, které umožňují integraci externích servisních platforem, jako je IMS"
---

STP je standardizovaný referenční bod v architektuře 3GPP, který definuje, kde a jak se externí servisní platformy integrují s jádrem sítě, aby mohly vyvolat servisní logiku pro služby s přidanou hodnotou.

## Popis

Service Platform Trigger Points (STP, spouštěcí body servisní platformy) jsou základním architektonickým konceptem ve standardech 3GPP, který specifikuje rozhraní a podmínky pro vyvolání služby. Nejde o fyzické uzly, ale o logické body v signalizačním toku jádra sítě, konkrétně v rámci Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IP Multimedia Subsystem (IMS) nebo v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v okruhově přepínaných doménách. STP definuje konkrétní stav nebo událost v rámci relace nebo hovoru (např. zahájení relace, událost během hovoru, ukončení), kdy lze předat řízení externímu aplikačnímu serveru nebo servisní platformě. Toho je dosaženo pomocí standardizovaných protokolů, především Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro služby IMS nebo protokolu Customized Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) pro starší služby.

Fungování STP řídí initial Filter Criteria (iFC), což jsou sady pravidel uložené v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a stažené do Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)). Když do S-CSCF dorazí SIP požadavek (jako INVITE), vyhodnotí jej vůči iFC pro daného uživatele. Každé iFC obsahuje spouštěcí bod, což je logická podmínka (např. konkrétní SIP metoda, hodnota hlavičky nebo požadovaný [URI](/mobilnisite/slovnik/uri/)). Pokud požadavek odpovídá spouštěcímu bodu, S-CSCF jej přepošle na určený Application Server ([AS](/mobilnisite/slovnik/as/)) specifikovaný v iFC. AS pak provede svou servisní logiku, která může upravit relaci, přehrát oznámení, komunikovat s účtovacími systémy nebo vyvolat další služby, než vrátí řízení zpět S-CSCF.

Tato architektura odděluje funkce řízení relace v jádru sítě od servisní logiky, což umožňuje operátorům sítí a poskytovatelům služeb třetích stran nasazovat inovativní služby bez nutnosti úprav samotných prvků jádra sítě. STP jsou klíčové pro umožnění širokého ekosystému multimediálních služeb, včetně Voice over LTE (VoLTE), Rich Communication Services (RCS) a multimediální konferenční hovory. Poskytují standardizovaný, bezpečný a škálovatelný mechanismus pro interakci služeb, což zajišťuje interoperabilitu mezi zařízeními různých výrobců a napříč sítěmi různých operátorů.

## K čemu slouží

Vytvoření Service Platform Trigger Points bylo motivováno potřebou překonat monolitické, pevně naprogramované síťové služby a přejít k otevřené, flexibilní servisní architektuře. Před jejich standardizací často zavedení nových telefonních funkcí vyžadovalo nákladné a časově náročné aktualizace centrálních ústředen (MSC), což brzdilo inovace a prodlužovalo dobu uvedení na trh. STP, jako součást širších architektur IMS a CAMEL, byly navrženy tak, aby tento problém vyřešily poskytnutím standardizovaného 'háčku' nebo rozhraní.

Tento přístup umožňuje, aby servisní logika sídlila na samostatných, vyhrazených aplikačních serverech. Role jádra sítě je redukována na základní řízení relace a směrování, zatímco komplexní servisní inteligence je delegována na tyto externí platformy. Toto oddělení zájmů umožňuje operátorům sítí rychle nasazovat, testovat a škálovat nové služby nezávisle na podkladové přenosové síti. Také usnadňuje vytvoření živého trhu poskytovatelů služeb třetích stran, protože standardizované STP a protokoly (jako SIP) poskytují jasné rozhraní pro integraci služeb.

Historicky se STP vyvinuly z konceptů Intelligent Network (IN) a byly poprvé formalizovány ve 3GPP Release 99 pro podporu vznikající architektury IMS. Řešily omezení předchozích proprietárních prostředí pro tvorbu služeb tím, že poskytly jednotný, na protokolu nezávislý model pro spouštění služeb na základě profilů účastníků a charakteristik relace. To bylo nezbytné pro přechod od okruhově přepínaných hlasových služeb k plně IP multimediálním službám, aby bylo zajištěno, že starší služby (jako přesměrování hovoru) a nové multimediální služby mohou koexistovat a být spravovány podle jednotného architektonického principu.

## Klíčové vlastnosti

- Definuje logické body v toku řízení hovoru/relace pro vyvolání služby
- Pro zřizování spouštěcích pravidel využívá Initial Filter Criteria (iFC) uložená v HSS
- Umožňuje interakci mezi S-CSCF a externími Application Servery prostřednictvím SIP
- Podporuje spouštění služeb na základě SIP metod, hlaviček a identifikátorů relace
- Umožňuje nasazení služeb s přidanou hodnotou, jako je zákaz hovorů, předplacené účtování a multimediální konferenční hovory
- Poskytuje standardizovaný mechanismus zajišťující interoperabilitu mezi více výrobci a více operátory

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management

---

📖 **Anglický originál a plná specifikace:** [STP na 3GPP Explorer](https://3gpp-explorer.com/glossary/stp/)
