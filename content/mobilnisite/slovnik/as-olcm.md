---
slug: "as-olcm"
url: "/mobilnisite/slovnik/as-olcm/"
type: "slovnik"
title: "AS-OLCM – Application Server Outgoing Leg Control Model"
date: 2025-01-01
abbr: "AS-OLCM"
fullName: "Application Server Outgoing Leg Control Model"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/as-olcm/"
summary: "Model řízení služeb v IP Multimedia Subsystem (IMS), ve kterém Application Server (AS) řídí odchozí větev relace. Umožňuje pokročilé služby jako přesměrování hovoru, překlad čísel a filtrování hovorů"
---

AS-OLCM je model řízení služeb v IMS, ve kterém Application Server řídí odchozí větev relace, aby umožnil služby jako přesměrování hovoru prostřednictvím modifikace nebo změny směrování požadavku.

## Popis

Application Server Outgoing Leg Control Model (AS-OLCM) je základní architektonický model v rámci IP Multimedia Subsystem (IMS) dle 3GPP pro provádění služeb. Definuje interakci mezi Application Server ([AS](/mobilnisite/slovnik/as/)) a Serving-Call Session Control Function (S-CSCF) během navazování relace. V tomto modelu AS funguje jako Back-to-Back User Agent ([B2BUA](/mobilnisite/slovnik/b2bua/)) pro odchozí větev relace, což znamená, že ukončí příchozí SIP dialog od S-CSCF a vytvoří nový, odchozí SIP dialog směrem ke konečnému cíli. To umožňuje AS uplatňovat plnou kontrolu nad parametry relace, směrováním a charakteristikami médií na odchozí větvi.

Operační tok začíná, když S-CSCF, vykonávající initial Filter Criteria (iFC) z profilu služeb uživatele, přepošle SIP požadavek (např. INVITE) k určenému AS. AS, fungující v režimu [OLCM](/mobilnisite/slovnik/olcm/), tento požadavek přijme a ukončí příchozí větev. Následně požadavek zpracuje na základě své servisní logiky – což může zahrnovat překlad čísla, aplikaci obchodních pravidel nebo interakci s externími databázemi. Po tomto zpracování AS vytvoří nový SIP požadavek směrem k cílové adrese, kterou může být původně zamýšlený cíl nebo jiný cíl určený servisní logikou. Tento nový požadavek tvoří odchozí větev a AS zůstává v signalizační cestě po dobu trvání relace, což umožňuje řízení služeb během hovoru.

Klíčovými komponentami jsou samotný AS, který hostí servisní logiku a funguje jako B2BUA, a S-CSCF, který provádí počáteční spouštění služeb na základě iFC. Model se opírá o protokol SIP pro všechny signalizační interakce. AS-OLCM je zásadní pro implementaci širokého spektra telefonních a multimediálních služeb, které vyžadují, aby servisní platforma modifikovala cíl nebo charakteristiky relace. Poskytuje standardizovaný a výkonný mechanismus pro poskytovatele služeb, jak vložit služby s přidanou hodnotou do IMS cesty hovoru, a zajišťuje interoperabilitu a konzistentní chování napříč různými síťovými implementacemi.

## K čemu slouží

AS-OLCM byl vytvořen, aby poskytl standardizovaný a výkonný mechanismus pro implementaci pokročilých, v síti hostovaných služeb v rámci architektury IMS. Před IMS a jeho definovanými modely řízení služeb byly služby inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) často těsně provázány s jádrem s okruhovým přepojováním, což komplikovalo jejich nasazení a omezovalo inovace. AS-OLCM, představený ve 3GPP Release 99, byl součástí základního IMS rámce navrženého k oddělení servisní logiky od transportního jádra sítě, což umožnilo rychlejší tvorbu a nasazení služeb v prostředí s paketovým přepojováním založeném na SIP.

Řeší problém, jak umožnit externímu Application Server aktivně řídit a modifikovat relaci poté, co ji uživatel zahájil. Bez takového modelu by [AS](/mobilnisite/slovnik/as/) mohl relaci pouze sledovat nebo na ni pasivně působit. [OLCM](/mobilnisite/slovnik/olcm/) konkrétně řeší případy užití, kdy servisní logika musí změnit cíl nebo základní parametry relace, jako je například bezpodmínečné přesměrování hovoru, řešení přenositelnosti čísel nebo překlad firemního číselníku. Poskytuje nezbytné architektonické prostředky pro AS k přerušení SIP dialogu a jeho znovuvytvoření, což je schopnost klíčová pro mnoho tradičních telefonních služeb přenesených do IP domény.

Motivací bylo zajistit, aby IMS dokázalo podporovat bohatý servisní portfolium dědičných sítí a zároveň umožňovalo nové multimediální služby. Definováním jasných modelů, jako je OLCM, zajistilo 3GPP předvídatelné chování služeb a to, že AS od různých výrobců mohou interoperovat s jakýmkoli IMS jádrem odpovídajícím standardům. To podpořilo konkurenční ekosystém pro vývoj aplikací a bylo klíčové pro komerční úspěch IMS jako platformy pro poskytování služeb.

## Klíčové vlastnosti

- Umožňuje Application Server fungovat jako Back-to-Back User Agent (B2BUA) pro odchozí větev relace
- Poskytuje plnou kontrolu nad SIP signalizací a parametry relace pro odchozí větev
- Podporuje změnu směrování relace na jiný cíl spuštěnou službou
- Umožňuje implementaci služeb jako přesměrování hovoru, překlad čísel a filtrování hovorů
- Integruje se s S-CSCF prostřednictvím initial Filter Criteria (iFC) pro standardizované spouštění služeb
- Udržuje AS v signalizační cestě pro případné řízení služeb během hovoru

## Související pojmy

- [B2BUA – Back-to-Back User Agent](/mobilnisite/slovnik/b2bua/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [AS-OLCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/as-olcm/)
