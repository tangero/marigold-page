---
slug: "cdur"
url: "/mobilnisite/slovnik/cdur/"
type: "slovnik"
title: "CDUR – Chargeable DURation"
date: 2025-01-01
abbr: "CDUR"
fullName: "Chargeable DURation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdur/"
summary: "CDUR je fakturační parametr v sítích 3GPP, který představuje dobu trvání zpoplatnitelné události, například hovoru nebo datové relace. Je základní jednotkou pro výpočty účtování, která umožňuje operát"
---

CDUR je fakturační parametr 3GPP, který představuje dobu trvání zpoplatnitelné události, například hovoru, pro výpočty časově závislého účtování.

## Popis

Chargeable DURation (CDUR, Zpoplatnitelná Doba Trvání) je klíčový fakturační parametr definovaný v rámci fakturační architektury 3GPP, konkrétně v kontextu offline a online fakturačních systémů ([OFCS](/mobilnisite/slovnik/ofcs/) a [OCS](/mobilnisite/slovnik/ocs/)). Kvantifikuje uplynulý čas využití služby, který podléhá účtování. CDUR není samostatnou entitou, ale kritickým datovým prvkem vyplňovaným v záznamech o fakturačních datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo v kreditních řídicích zprávách. Jeho hodnota se měří v příslušných časových jednotkách (např. sekundy, milisekundy), jak je definováno příslušným tarifem.

Z architektonického hlediska CDUR generuje síťová funkce zodpovědná za monitorování události služby, typicky Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro služby IMS, Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Gateway GPRS Support Node (GGSN)/Packet Data Network Gateway (PGW) pro paketová data, nebo Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro okruhově spínané hovory. Tyto Charging Trigger Functions ([CTF](/mobilnisite/slovnik/ctf/)) detekují začátek a konec zpoplatnitelné události. CTF tyto události časově označí a vypočítá rozdíl, což vede k hodnotě CDUR. Tato doba trvání je pak zahrnuta do fakturačních informací odeslaných do Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) pro offline účtování nebo použita pro odečítání kreditu v reálném čase s Online Charging System (OCF).

Technická implementace vyžaduje přesnou časovou synchronizaci napříč síťovými prvky pro zajištění přesnosti. Výpočet CDUR musí zohledňovat konkrétní fakturační model; například může představovat celkovou dobu relace, dobu trvání konkrétní mediální komponenty v rámci IMS relace nebo dobu po uplynutí prvního počátečního časového intervalu ve vícestupňové tarifní struktuře. V online účtování je CDUR klíčové pro účtování na bázi relace, kdy OCS přidělí kvótu časových jednotek. CTF hlásí spotřebovaný CDUR, což umožňuje OCS odečíst kredit a případně znovu autorizovat další službu. Úroveň podrobnosti a hlášení CDUR lze konfigurovat na základě politiky operátora a požadované přesnosti účtování.

Jeho role přesahuje rámec prostého účtování. CDUR je klíčovým vstupem pro systémy zajištění výnosů, analýzy služeb a detekce podvodů. Nesrovnalosti v hlášeném CDUR na různých síťových rozhraních mohou naznačovat poruchy nebo podvodnou činnost. Dále v kontextu QoS-aware účtování mohou být pro různé úrovně kvality přenosu použity různé hodnoty CDUR. Definice tohoto parametru ve specifikacích 3GPP zajišťuje interoperabilitu mezi síťovými zařízeními a fakturačními systémy různých dodavatelů a vytváří standardizovaný základ pro monetizaci služeb založenou na čase.

## K čemu slouží

CDUR existuje proto, aby poskytoval standardizovanou, přesnou a spolehlivou míru času spotřeby služby pro účely účtování v telekomunikačních sítích. Před zavedením standardizovaných fakturačních parametrů se operátoři spoléhali na proprietární metody měření délky hovorů a relací, což vytvářelo problémy s interoperabilitou při integraci více-dodavatelských sítí a fakturačních systémů. Tento nedostatek standardizace mohl vést k chybám v účtování, únikům výnosů a složitým procesům zúčtování mezi operátory. CDUR jako součást fakturačního rámce 3GPP tento problém řeší definicí univerzálního parametru pro vyjádření časového využití.

Vznik CDUR byl motivován přechodem od jednoduchého účtování okruhově spínaných hovorů ke složitějším fakturačním modelům pro datové a multimediální služby zavedeným se sítěmi 2.5G a 3G. Jak se služby vyvíjely, rostla i potřeba přesného měření délky relace pro nové tarifní plány, včetně rozděleného účtování, časově závislých sazeb a dob trvání specifických pro službu (např. doba videohovoru vs. doba hlasového hovoru). CDUR poskytuje základní stavební kámen, na kterém jsou tyto složité tarifní struktury implementovány v rámci fakturačních subsystémů sítě.

Řeší omezení spočívající v tom, že fakturační logika byla pevně zabudována v přepínacích zařízeních. Externalizací doby trvání jako jasného parametru ve standardizovaných fakturačních zprávách (jako jsou Diameter Credit-Control nebo accounting requesty) umožňuje CDUR flexibilním fakturačním systémům aplikovat různé tarifní plány bez nutnosti upgradu síťového hardwaru. Toto oddělení generování fakturačních informací od aplikace fakturační politiky je základním kamenem moderních telekomunikačních operací a podporuje vše od předplacených mobilních tarifů až po účtování podnikových VoIP služeb.

## Klíčové vlastnosti

- Standardizované měření času pro fakturační události napříč všemi doménami sítí 3GPP (CS, PS, IMS)
- Základní datový prvek v záznamech o fakturačních datech (CDR) pro offline účtování
- Kritický parametr v Diameter Credit-Control zprávách pro online účtování v reálném čase
- Podpora složitých tarifních modelů včetně vícestupňového účtování, časově závislých sazeb a dob trvání specifických pro službu
- Umožnění přesného zúčtování mezi operátory za roamingové hovory a relace
- Poskytování vstupů pro systémy zajištění výnosů, správy podvodů a analýzy využití služeb

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CDUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdur/)
