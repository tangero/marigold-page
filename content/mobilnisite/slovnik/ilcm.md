---
slug: "ilcm"
url: "/mobilnisite/slovnik/ilcm/"
type: "slovnik"
title: "ILCM – Incoming Leg Control Model"
date: 2025-01-01
abbr: "ILCM"
fullName: "Incoming Leg Control Model"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ilcm/"
summary: "Model řízení příchozí větve (Incoming Leg Control Model, ILCM) je model řízení hovoru definovaný v 3GPP pro správu signalizace a zpracování médií příchozí větve hovoru nebo relace v IP Multimedia Subs"
---

ILCM je 3GPP model řízení hovoru pro správu signalizace a médií příchozí větve (leg) hovoru nebo relace v IP Multimedia Subsystem (IMS).

## Popis

Model řízení příchozí větve (Incoming Leg Control Model, ILCM) je klíčový architektonický koncept v rámci 3GPP IP Multimedia Subsystem (IMS), definovaný primárně v TS 23.218. Popisuje funkční model a procedury pro řízení 'příchozí větve' (incoming leg) relace – signalizační cesty ze sítě směrem k volanému účastníkovi. V IMS je relace (například hlasový nebo video hovor) koncepčně rozdělena na dvě větve: vycházející (originating/outgoing leg) od volajícího do sítě a koncovou (terminating/incoming leg) od sítě k volanému. ILCM řídí tu druhou.

Model je soustředěn kolem funkce Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), která funguje jako centrální uzel pro řízení relace. Když relace cílí na uživatele, [I-CSCF](/mobilnisite/slovnik/i-cscf/) (Interrogating-CSCF) lokalizuje uživateli přiřazenou S-CSCF. Tato S-CSCF pak pro danou relaci vytvoří instanci ILCM. ILCM zahrnuje logiku S-CSCF pro zpracování příchozích [SIP](/mobilnisite/slovnik/sip/) požadavků (jako je INVITE), interakci s aplikačními servery ([AS](/mobilnisite/slovnik/as/)) pro provádění servisní logiky, uplatňování profilů účastníka a konečně směrování relace směrem k uživatelskému zařízení (UE) volaného prostřednictvím [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-CSCF). Zpracovává klíčové funkce jako autentizaci, autorizaci, vyhodnocování počátečních filtračních kritérií (iFC) a spouštění účtování.

Klíčové komponenty v rámci fungování ILCM zahrnují počáteční filtrační kritéria (Initial Filter Criteria, iFC), což je sada pravidel stažená jako součást servisního profilu uživatele z Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). S-CSCF používá tato iFC k rozhodování o tom, kdy a které aplikační servery (AS) zapojit do nastavení relace. Model také definuje interakce s Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)) pro relace směřující do [PSTN](/mobilnisite/slovnik/pstn/) a s Media Resource Function (MRF) pro zpracování médií. ILCM zajišťuje standardizovanou, na službě nezávislou řídicí rovinu pro poskytování multimediálních služeb, což umožňuje funkce jako přesměrování hovoru, hlasová schránka a překlad čísel konzistentním způsobem.

## K čemu slouží

ILCM byl vytvořen, aby poskytl standardizovaný, robustní a škálovatelný model pro řízení koncové strany multimediálních relací v rámci architektury IMS. Před IMS měla tradiční telefonie s přepojováním okruhů dobře definované, ale rigidní modely hovorů. Přechod na plně IP sítě vyžadoval nový, flexibilní řídicí model, který by mohl podporovat širokou škálu služeb nad rámec jednoduchých hlasových hovorů. ILCM spolu se svým protějškem OLCM (Originating Leg Control Model) toto poskytuje oddělením logiky řízení hovoru od podkladového přenosu, což umožňuje rychlou inovaci služeb.

Jeho zavedení v 3GPP Release 5 (první verze IMS) řešilo potřebu společné platformy pro poskytování služeb. ILCM řeší problém, jak jednotně aplikovat služby specifické pro účastníka (jako filtrování hovorů, větvení nebo předplacené účtování) na příchozí požadavky na relaci bez ohledu na polohu volajícího nebo síť. Centralizací řízení v S-CSCF a použitím mechanismu filtrů řízených profilem (iFC) umožňuje operátorům nasazovat nové služby na aplikačních serverech bez nutnosti pokaždé upravovat jádrovou logiku řízení relace.

ILCM navíc umožňuje síťovou interoperabilitu a roaming. Definuje jasný demarkační bod (S-CSCF v domovské síti), kde je uplatňována servisní politika domovského operátora, a to i když je uživatel v roamingu. Tento model byl zásadní pro globální nasazení VoLTE, VoNR a Rich Communication Services (RCS), protože zajišťuje konzistentní chování a poskytování funkcí napříč různými sítěmi a implementacemi zařízení.

## Klíčové vlastnosti

- Definuje řídicí procedury pro koncovou (volaného) stranu IMS relace
- Centrálně implementován ve funkci Serving-Call Session Control Function (S-CSCF)
- Využívá počáteční filtrační kritéria (Initial Filter Criteria, iFC) pro spouštění služeb na základě triggerů
- Spravuje interakce s aplikačními servery (Application Servers, AS) pro servisní logiku
- Řídí rozhodnutí o směrování směrem k uživatelskému zařízení (UE) volaného nebo k průniku do PSTN
- Podporuje základní funkce jako autorizace, účtování a řízení mediální politiky

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [OLCM – Outgoing Leg Control Model](/mobilnisite/slovnik/olcm/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [ILCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ilcm/)
