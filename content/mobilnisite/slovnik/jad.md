---
slug: "jad"
url: "/mobilnisite/slovnik/jad/"
type: "slovnik"
title: "JAD – Java Application Descriptor"
date: 2025-01-01
abbr: "JAD"
fullName: "Java Application Descriptor"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/jad/"
summary: "Standardizovaný deskriptor pro Java aplikace v mobilních sítích, zavedený ve specifikaci 3GPP Release 5. Definuje strukturu a metadata pro aplikace založené na Javě (MIDlety) za účelem umožnění jejich"
---

JAD je standardizovaný deskriptor zavedený ve specifikaci 3GPP Release 5, který definuje strukturu a metadata pro Java aplikace (MIDlety) za účelem umožnění jejich bezpečného nasazení a provádění na mobilních zařízeních.

## Popis

Java Application Descriptor (JAD) je klíčovou součástí specifikací 3GPP pro nasazování mobilních aplikací, konkrétně v rámci platformy Java 2 Micro Edition ([J2ME](/mobilnisite/slovnik/j2me/)) a Mobile Information Device Profile ([MIDP](/mobilnisite/slovnik/midp/)). Jedná se o textový soubor obsahující metadata a konfigurační informace pro sadu Java MIDletů (kolekci MIDletů). Soubor JAD obsahuje atributy jako název MIDletu, verze, dodavatel, požadované Java profily a konfigurace, velikost aplikace a oprávnění. Funguje jako externí deskriptor oddělený od souboru Java Archive (JAR), což umožňuje zařízení nebo síti prověřit požadavky aplikace před stažením nebo spuštěním JAR souboru. Toto umožňuje správu životního cyklu aplikace, bezpečnostních politik a kontrol kompatibility zdrojů.

Z architektonického hlediska JAD spolupracuje s Java Application Managerem ([JAM](/mobilnisite/slovnik/jam/)) na mobilním zařízení. JAM čte soubor JAD, aby ověřil, zda zařízení splňuje požadavky aplikace (např. paměť, podpora [API](/mobilnisite/slovnik/api/)), a vynutil bezpečnostní oprávnění před instalací. Deskriptor podporuje dynamické aktualizace a over-the-air ([OTA](/mobilnisite/slovnik/ota/)) provizionování. Mezi klíčové komponenty odkazované v JAD patří hlavní třída sady MIDletů, ikona, popis a závislosti. Jeho role v síti je součástí frameworku pro umožnění služeb, což operátorům a třetím stranám umožňuje bezpečně a efektivně distribuovat a spravovat služby založené na Javě na široké škále mobilních zařízení.

Specifikace JAD zajišťuje interoperabilitu napříč různými implementacemi zařízení standardizací atributů a jejich formátů. Podrobně popisuje, jak jsou atributy parsovány a jak se řeší konflikty mezi JAD a interním manifestem JAR. Specifikace také pokrývá, jak se deskriptor používá v provizionovacích protokolech a v rozhraních pro správu aplikací. Poskytnutím jasného externího souboru metadat zjednodušuje objevování aplikací, jejich instalaci a ověřování důvěryhodnosti jak pro koncové uživatele, tak pro systémy správy sítě.

## K čemu slouží

JAD byl vytvořen, aby řešil potřebu standardizované, bezpečné a efektivní metody pro nasazování Java aplikací na mobilních zařízeních. Před jeho zavedením bylo nasazování aplikací často ad-hoc, s omezenými mechanismy pro ověření kompatibility nebo bezpečnosti před instalací. To vedlo k potenciální nestabilitě zařízení, bezpečnostním rizikům a nespokojenosti uživatelů. Java platforma na mobilních zařízeních ([MIDP](/mobilnisite/slovnik/midp/)) vyžadovala způsob, jak externě popsat vlastnosti aplikace, aby zařízení a sítě mohla činit informovaná rozhodnutí o stahování a instalaci softwaru.

Jeho zavedení v Release 5 bylo motivováno růstem mobilních služeb a snahou vytvořit živé ekosystémy stahovatelných aplikací. Poskytnutím standardizovaného deskriptoru umožnil over-the-air provizionování, což uživatelům umožnilo objevovat a instalovat aplikace přímo ze sítí nebo od poskytovatelů obsahu. Řešil problémy integrity aplikací (umožněním předinstalačních kontrol), správy zdrojů (deklarováním požadavků) a bezpečnosti (specifikací nezbytných oprávnění). To usnadnilo vývoj spravovaného kanálu distribuce aplikací, který byl klíčový pro rané platformy mobilních služeb, jako byl i-mode, a následné služby 3G.

## Klíčové vlastnosti

- Standardizovaný formát metadat pro Java MIDlety
- Umožňuje předinstalační kontroly kompatibility a bezpečnosti
- Podporuje over-the-air (OTA) provizionování a dynamické aktualizace
- Oddělen od JAR souboru pro externí kontrolu
- Definuje atributy pro název, verzi, dodavatele, velikost a oprávnění
- Integruje se s Java Application Managerem (JAM) pro správu životního cyklu

## Související pojmy

- [JAM – Java Application Manager](/mobilnisite/slovnik/jam/)
- [J2ME – Java 2 Platform, Micro Edition](/mobilnisite/slovnik/j2me/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [JAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/jad/)
