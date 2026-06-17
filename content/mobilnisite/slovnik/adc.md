---
slug: "adc"
url: "/mobilnisite/slovnik/adc/"
type: "slovnik"
title: "ADC – Application Detection and Control"
date: 2025-01-01
abbr: "ADC"
fullName: "Application Detection and Control"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/adc/"
summary: "ADC je síťová funkce, která identifikuje specifické aplikace nebo typy provozu a uplatňuje na ně kontrolu založenou na politikách. Operátorům umožňuje spravovat síťové zdroje, zavádět účtovací politik"
---

ADC je síťová funkce, která identifikuje specifické aplikace nebo typy provozu a uplatňuje na ně kontrolu založenou na politikách, čímž umožňuje správu zdrojů, implementaci účtování a zajištění kvality služby.

## Popis

Application Detection and Control (ADC) je sofistikovaná síťová schopnost definovaná v architektuře Policy and Charging Control (PCC) standardu 3GPP. Jejím hlavním úkolem je provádět hloubkovou kontrolu paketů (DPI) nebo používat jiné metody detekce k identifikaci konkrétní aplikace nebo typu provozu spojeného s datovou relací uživatele. Jakmile je aplikace detekována, ADC v součinnosti s funkcí Policy and Charging Rules Function (PCRF) prosazuje dynamická pravidla politik. Tato pravidla mohou řídit parametry Quality of Service (QoS), například přidělení garantované přenosové rychlosti pro službu streamování videa nebo aplikování tvarování provozu pro sdílení souborů typu peer-to-peer. ADC také poskytuje klíčový vstup pro účtovací funkce, což umožňuje účtovací modely citlivé na aplikaci, jako je nulování poplatků (zero-rating) pro konkrétní aplikace nebo objemové tarify.

Architektonická implementace ADC je typicky integrována s funkcí Traffic Detection Function (TDF) nebo PCEF (Policy and Charging Enforcement Function) v uživatelské rovině. PCRF, umístěná v řídicí rovině, poskytuje přes referenční body Gx nebo Sd detekční a kontrolní pravidla pro TDF/PCEF. Detekční mechanismy mohou být založené na signaturách (analýza hlaviček a obsahu paketů) nebo využívat behaviorální analýzu, strojové učení a spolupráci s aplikačními servery. Po detekci určené aplikace může vymáhací bod spustit akce, jako je přesměrování provozu, jeho blokování, změna jeho priority nebo generování specifických záznamů o účtovacích datech (CDR) pro offline účtovací systémy.

Mezi klíčové komponenty zapojené do ADC patří TDF, což je vyhrazený uzel pro detekci aplikací, a PCEF, často umístěný společně s Gateway GPRS Support Node (GGSN) nebo Packet Data Network Gateway (PGW). PCRF funguje jako mozek, který rozhoduje o tom, které politiky použít na základě detekované aplikace, profilu účastníka a stavu sítě. Online Charging System (OCS) a Offline Charging System (OFCS) přijímají zprávy o využití specifickém pro aplikace pro řízení kreditu v reálném čase a následné zpracování účtování. Tento integrovaný systém umožňuje detailní kontrolu nad síťovým provozem na aplikační vrstvě v reálném čase.

Role ADC přesahuje rámec pouhé správy provozu. Je zásadní pro implementaci strategií diferenciace služeb, jako je vytváření „service passů“ pro sociální média nebo hry. Podporuje rodičovskou kontrolu blokováním nevhodného obsahu a umožňuje podnikové služby zaručením výkonu pro obchodní aplikace. V moderních sítích je ADC nezbytná pro zvládnutí obrovského nárůstu různorodého provozu z Over-the-Top (OTT) aplikací, což zajišťuje, že kritické služby dostanou potřebné zdroje, a zároveň optimalizuje celkovou efektivitu sítě a vytváří nové zdroje příjmů pro operátory.

## K čemu slouží

ADC byla vytvořena, aby vyřešila zásadní výzvu fenoménu „hloupé trubky“ (dumb pipe), kdy mobilním operátorům hrozilo, že se stanou pouhými poskytovateli konektivity bez možnosti rozlišovat nebo monetizovat širokou škálu aplikací přenášených přes jejich infrastrukturu. Před ADC byla kontrola politik založena převážně na statických profilech účastníků nebo nastaveních Access Point Name (APN), což nabízelo malou až žádnou granularitu na základě skutečně používané aplikace. To znemožňovalo nabízet inovativní služební plány, garantovat výkon pro aplikace citlivé na latenci (jako je VoIP) nebo řídit zahlcení sítě způsobené konkrétními aplikacemi s vysokou přenosovou rychlostí.

Zavedení ADC, počínaje 3GPP Release 5 v rámci širšího rámce PCC, umožnilo operátorům přejít od univerzální datové služby k inteligentní síti citlivé na aplikace. Vyřešilo problém konkurence o síťové zdroje tím, že operátorům umožnilo identifikovat a řídit provoz na aplikační vrstvě. To umožnilo politiky spravedlivého využití, vytváření vrstvených služebních nabídek (např. „balíček pro sociální média“) a vytvořilo technický základ pro sponzorovaná data nebo nulování poplatků, kdy se provoz specifické aplikace nezapočítává do datového limitu uživatele. ADC navíc poskytla nástroje pro dodržování regulatorních požadavků, například implementaci spouštěčů pro zákonné odposlechy na základě použití aplikace.

## Klíčové vlastnosti

- Hloubková kontrola paketů (DPI) pro detekci aplikací podle signatur
- Dynamické prosazování politik na základě identifikace aplikací v reálném čase
- Integrace s architekturou PCC prostřednictvím rozhraní Gx a Sd
- Podpora účtovacích a fakturačních modelů citlivých na aplikace
- Optimalizace provozu pomocí blokování (gating), přesměrování a správy šířky pásma
- Generování záznamů o využití specifických pro aplikace pro účtování (CDR)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [ADC na 3GPP Explorer](https://3gpp-explorer.com/glossary/adc/)
