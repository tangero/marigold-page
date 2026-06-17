---
slug: "jcr"
url: "/mobilnisite/slovnik/jcr/"
type: "slovnik"
title: "JCR – JSON Content Rules"
date: 2025-01-01
abbr: "JCR"
fullName: "JSON Content Rules"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/jcr/"
summary: "JSON Content Rules (JCR) je formální jazyk definovaný v 3GPP pro specifikaci struktury, omezení a validačních pravidel pro JSON data používaná v síťových API a servisních rozhraních. Poskytuje standar"
---

JCR je formální jazyk pro specifikaci struktury, omezení a validačních pravidel pro JSON data v 3GPP síťových API a servisních rozhraních za účelem zajištění konzistence a interoperability.

## Popis

[JSON](/mobilnisite/slovnik/json/) Content Rules (JCR) je specifikační jazyk standardizovaný 3GPP, primárně dokumentovaný v TS 29.155. Definuje syntaxi a sémantiku pro vytváření pravidel, která popisují očekávanou strukturu a obsah JSON dokumentů. Tato pravidla fungují jako schéma, specifikující povolené datové typy (např. řetězce, čísla, logické hodnoty, pole, objekty), povinná a volitelná pole, omezení hodnot (např. rozsahy, vzory, výčty) a vnořené vztahy. V praxi jsou JCR pravidla textové definice, které mohou být zpracovány validačními enginy. Síťová funkce nebo [API](/mobilnisite/slovnik/api/) brána může použít JCR validátor ke kontrole příchozích nebo odchozích JSON zpráv vůči předdefinovaným pravidlům, čímž zajistí jejich soulad s očekávaným formátem před dalším zpracováním. Tato validace je klíčová pro prevenci chyb způsobených nesprávně formátovanými daty v servisní logice nebo problémů s interoperabilitou mezi systémy. Jazyk podporuje komplexní konstrukty jako podmíněná pravidla (např. pokud pole 'serviceType' má hodnotu 'VoLTE', pak další pole 'codec' musí být přítomno), reference pro opakované použití běžných definic pravidel a anotace pro dokumentaci. Jeho role v ekosystému 3GPP spočívá v poskytování strojově čitelné smlouvy pro výměnu dat, zejména v servisně orientovaných rozhraních (SBI) uvnitř 5G jádra sítě, kde API hojně využívají JSON. Formalizací datových očekávání JCR snižuje úsilí při integraci, napomáhá automatizovanému testování a zvyšuje spolehlivost interakcí síťových služeb.

## K čemu slouží

JCR byl vytvořen jako odpověď na rostoucí používání [JSON](/mobilnisite/slovnik/json/) jako primárního formátu pro výměnu dat v moderních, webově orientovaných síťových architekturách, konkrétně v 5G servisně orientované architektuře (SBA). Předchozí přístupy často spoléhaly na neformální dokumentaci nebo proprietární definice schémat, což vedlo k nekonzistentnostem, integračním chybám a prodloužení doby vývoje u výrobců síťových funkcí a vývojářů aplikací. Motivace vycházela z potřeby standardizovaného, dodavatele neutrálního způsobu definice přesné struktury JSON zátěží používaných v [API](/mobilnisite/slovnik/api/) definovaných 3GPP, jako jsou například rozhraní mezi funkcemi síťového repozitáře ([NRF](/mobilnisite/slovnik/nrf/)), funkcemi síťové expozice ([NEF](/mobilnisite/slovnik/nef/)) a dalšími prvky jádra sítě. Poskytnutím formálního jazyka pravidel cílilo 3GPP na zajištění, aby všechny implementace interpretovaly datové smlouvy API shodně, čímž se řeší problémy interoperability, které mohly vzniknout z nejednoznačných specifikací. Také usnadňuje automatizované nástroje pro generování kódu, dokumentaci a validaci, čímž zefektivňuje vývojový a testovací životní cyklus pro 5G síťový software. Historicky byly podobné potřeby u jiných protokolů naplněny jazyky jako ASN.1 nebo XML Schema, ale JCR je přizpůsoben jednoduchosti formátu JSON a jeho rozšířenosti v RESTful API, což odpovídá posunu průmyslu směrem k webovým technologiím v telekomunikacích.

## Klíčové vlastnosti

- Formální definice schématu pro struktury JSON dat
- Podpora validace datových typů (řetězce, čísla, logické hodnoty, null, pole, objekty)
- Specifikace omezení pro hodnoty (rozsahy, regulární výrazy, výčtové seznamy)
- Skládání pravidel pomocí operátorů (AND, OR, NOT) a referencí pro opakované použití
- Podmíněná logika pravidel založená na hodnotách polí
- Možnost anotací pro vkládání čitelné dokumentace pro člověka přímo do pravidel

## Související pojmy

- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)

## Definující specifikace

- **TS 29.155** (Rel-19) — REST-based St Reference Point Protocol

---

📖 **Anglický originál a plná specifikace:** [JCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/jcr/)
