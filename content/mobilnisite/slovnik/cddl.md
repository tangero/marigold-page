---
slug: "cddl"
url: "/mobilnisite/slovnik/cddl/"
type: "slovnik"
title: "CDDL – Concise Data Definition Language"
date: 2025-01-01
abbr: "CDDL"
fullName: "Concise Data Definition Language"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cddl/"
summary: "CDDL je standardizovaný jazyk pro modelování dat používaný v specifikacích 3GPP k definování datových struktur a jejich omezení. Poskytuje čitelný formát pro člověka i strojově zpracovatelný formát pr"
---

CDDL je standardizovaný jazyk pro modelování dat používaný v 3GPP k definování datových struktur a omezení pro formáty JSON a CBOR, což zajišťuje interoperabilitu mezi síťovými funkcemi a aplikacemi.

## Popis

Concise Data Definition Language (CDDL) je formální jazyk pro popis datových struktur, speciálně navržený pro použití s datovými formáty [JSON](/mobilnisite/slovnik/json/) (JavaScript Object Notation) a [CBOR](/mobilnisite/slovnik/cbor/) (Concise Binary Object Representation). V rámci standardů 3GPP slouží CDDL jako primární specifikační jazyk pro definování přesného schématu dat vyměňovaných mezi síťovými funkcemi, mezi sítí a aplikačními servery a v rámci rozhraní pro správu. Funguje tak, že definuje sadu pravidel, která odpovídají datovým typům a strukturám povoleným v daném dokumentu JSON nebo CBOR, přičemž specifikuje povolené hodnoty, povinné versus volitelné položky, vnořování, pole a další omezení.

Gramatika jazyka je založena na [ABNF](/mobilnisite/slovnik/abnf/) (Augmented Backus-Naur Form) a používá kompaktní, výraznou syntaxi. Definice CDDL typicky sestává ze série přiřazení pravidel, kde je název pravidla (identifikátor) přiřazen popisu typu. Popisy typu mohou být základní typy (jako čísla, textové řetězce, logické hodnoty), složené typy (jako pole nebo mapy) nebo odkazy na jiná pravidla pro vytváření vnořených nebo rekurzivních struktur. CDDL také podporuje pokročilé funkce, jako volitelné skupiny, volby (sjednocení) a možnost specifikovat rozsahy, regulární výrazy pro řetězce a omezení velikosti pro pole.

V architektuře 3GPP jsou definice CDDL vloženy do technických specifikací (TS), aby jednoznačně definovaly obsah zpráv [HTTP](/mobilnisite/slovnik/http/)/2 (pro rozhraní založená na službách), zpráv [NAS](/mobilnisite/slovnik/nas/) nebo konfiguračních dat. Například 3GPP TS 29.890 používá CDDL k definování datových struktur pro službu Nnef_EventExposure. Použití CDDL eliminuje nejednoznačnost, která by mohla vzniknout z textových popisů nebo neformálních příkladů, což vede k méně problémům s interoperabilitou během integrace a testování. Nástroje mohou analyzovat definice CDDL za účelem generování kódu, validace datových instancí nebo automatického vytváření dokumentace.

Role CDDL přesahuje pouhou dokumentaci; je základní součástí přístupu 3GPP řízeného modely. Tím, že poskytuje jediný autoritativní zdroj pro strukturu datového modelu, zajišťuje, že všechny implementace – ať už pro funkci vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) jádra 5G sítě, službu multimediální telefonie nebo funkci streamování médií – interpretují datové formáty stejně. To je klíčové pro bezproblémový provoz více-dodavatelských sítí a pro vývoj aplikací třetích stran, které komunikují s možnostmi sítě 3GPP prostřednictvím [API](/mobilnisite/slovnik/api/).

## K čemu slouží

CDDL byl zaveden k vyřešení problému nejednoznačných a nekonzistentních definic datových formátů v telekomunikačních standardech. Před jeho přijetím specifikace 3GPP často popisovaly datové struktury pomocí neformálních tabulek, textových popisů nebo definic [XML](/mobilnisite/slovnik/xml/) schémat (XSD). Tyto metody mohly být rozvláčné, obtížně automaticky analyzovatelné a někdy vedly k rozdílným interpretacím ze strany dodavatelů zařízení a vývojářů softwaru. Tato nejednoznačnost měla za následek selhání interoperability během síťové integrace, což prodlužovalo čas uvedení na trh a zvyšovalo náklady.

Motivace pro CDDL přišla s přechodem odvětví na RESTful API založená na JSONu pro rozhraní založená na službách v rámci jádra 5G sítě (zavedeno v 3GPP Release 15). JSON je lehký a široce používaný ve webovém vývoji, ale postrádá nativní, standardizovaný jazyk schémat. CDDL tuto mezeru zaplňuje tím, že poskytuje stručný, čitelný, ale přitom formální způsob, jak přesně definovat, jak musí vypadat platný objekt JSON pro danou službu 3GPP. Podporuje také CBOR, binární formát odvozený z JSONu, který je efektivnější pro zařízení s omezenými zdroji a spoje citlivé na šířku pásma, což jej činí velmi relevantním pro aplikace IoT.

Standardizací na CDDL umožnilo 3GPP rigoróznější a automatizovanější přístup k dodržování specifikací. Umožňuje vytváření validačních nástrojů a generátorů kódu, které přímo využívají dokumenty standardů, čímž snižuje lidskou chybu. To je v souladu s širším cílem 3GPP vytvářet otevřená, dobře definovaná rozhraní, která podporují inovace a konkurenci v telekomunikačním ekosystému tím, že snižují vstupní bariéru pro nové hráče a zajišťují spolehlivou více-dodavatelskou interoperabilitu.

## Klíčové vlastnosti

- Formální definice schématu pro datové formáty JSON a CBOR
- Čitelná syntaxe pro člověka založená na gramatice ABNF
- Podpora složitých datových typů, vnořování a omezení
- Umožňuje automatické generování kódu a validaci dat
- Poskytuje jednoznačné definice pro obsah zpráv API 3GPP
- Usnadňuje více-dodavatelskou interoperabilitu a testování

## Související pojmy

- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)
- [CBOR – Concise Binary Object Representation](/mobilnisite/slovnik/cbor/)

## Definující specifikace

- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [CDDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cddl/)
