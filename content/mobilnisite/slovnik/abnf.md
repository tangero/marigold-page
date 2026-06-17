---
slug: "abnf"
url: "/mobilnisite/slovnik/abnf/"
type: "slovnik"
title: "ABNF – Augmented Backus-Naur Form"
date: 2025-01-01
abbr: "ABNF"
fullName: "Augmented Backus-Naur Form"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/abnf/"
summary: "ABNF je formální jazyk pro specifikaci syntaxe hojně používaný v technických specifikacích 3GPP k definici formátů protokolových zpráv, datových struktur a kódovacích pravidel. Poskytuje přesný, stroj"
---

ABNF je formální jazyk pro specifikaci syntaxe používaný v 3GPP k jednoznačné definici formátů protokolových zpráv a kódovacích pravidel, což zajišťuje interoperabilitu mezi síťovými elementy.

## Popis

Augmented Backus-Naur Form (ABNF) je metajazyk založený na Backus-Naurově formě (BNF), rozšířený o další operátory a možnosti speciálně navržené pro definování syntaxe komunikačních protokolů. Ve specifikacích 3GPP je ABNF primárním formalismem používaným k určení přesné struktury protokolových datových jednotek (PDU), formátů zpráv pro různá rozhraní (např. Diameter, [HTTP](/mobilnisite/slovnik/http/)) a kódování složitých informačních elementů. Definuje pravidla pro posloupnosti znaků, specifikující, které řetězce symbolů jsou platné podle gramatiky protokolu. Pravidla ABNF se skládají z názvu pravidla definovaného rovnítkem a definice pravidla, která využívá kombinaci terminálních hodnot (literálů nebo číselných hodnot znaků) a dalších názvů pravidel. Operátory jako konkatenace, alternativa (reprezentovaná lomítkem '/'), opakování (pomocí '*', '+' nebo specifických rozsahů jako 'n*m'), volitelné elementy (uzavřené v '[]') a seskupení (uzavřené v '()') umožňují konstrukci sofistikovaných a přesných syntaktických definic. Jazyk také podporuje komentáře a řetězcové literály nerozlišující velikost písmen, což je zvláště užitečné pro textové protokoly.

Jádrem fungování ABNF v 3GPP je jeho role jako definitivního zdroje pro implementaci protokolů. Když specifikace jako 3GPP TS 29.329 (Sh Interface) definuje příkazy Diameter aplikace, používá ABNF k určení přesného pořadí, datových typů a volitelnosti atribut-hodnotových párů ([AVP](/mobilnisite/slovnik/avp/)) uvnitř příkazu. To zahrnuje definici formátu hlavičky, povinných a volitelných AVP a vnoření seskupených AVP. Například pravidlo ABNF může definovat AVP 'User-Name' jako obsahující UTF8String určitého formátu. Tato formální definice je pak používána dodavateli zařízení ke generování parsovacího kódu, validaci příchozích zpráv a správné konstrukci odchozích zpráv, což zajišťuje, že požadavek na správu relace od Policy and Charging Rules Function (PCRF) jednoho dodavatele je správně pochopen Policy and Charging Enforcement Function (PCEF) jiného dodavatele.

Klíčové komponenty specifikace ABNF zahrnují základní pravidla (jako ALPHA, DIGIT, CRLF) definovaná v RFC 5234, která poskytují základní stavební bloky, a protokolově specifická pravidla definovaná v samotné specifikaci 3GPP. Proces parsování začíná nejvyšším pravidlem (např. pravidlem pro kompletní Diameter zprávu) a rekurzivně aplikuje definovaná pravidla, aby porovnal vstupní řetězec s gramatikou. Úspěšné sparsování indikuje syntakticky platnou zprávu. Použití ABNF v 3GPP pokrývá četné technické specifikace, zejména ty definující rozhraní založená na Diameter v jádrové síti (např. Gx, Rx, S6a), služby založené na HTTP/2 (např. N5, N7 v 5GC) a managementová rozhraní. Jeho přesnost je klíčová pro automatizované testování, validaci shody protokolu a vývoj softwarových knihoven, které zpracovávají protokolové zásobníky 3GPP, a tvoří syntaktickou páteř, která zaručuje spolehlivou a jednoznačnou komunikaci v sítích s více dodavateli.

## K čemu slouží

ABNF bylo přijato 3GPP k řešení kritického problému nejednoznačnosti v specifikaci protokolů. Před rozšířeným používáním formálních syntaktických definic byly protokolové specifikace často popisovány prostým textem a neformálními diagramy, což vedlo k rozdílným interpretacím implementátorů. To mělo za následek problémy s interoperabilitou, kdy síťové elementy od různých dodavatelů nemohly správně komunikovat, přestože oba tvrdily, že dodržují stejný standard. Tyto selhání interoperability způsobovala výpadky služeb, chyby v účtování a zvýšený čas a náklady na integraci pro operátory. Potřeba rigorózního, jednoznačného a strojově zpracovatelného jazyka se stala prvořadou, jak sítě 3GPP rostly v komplexitě a s každou verzí zaváděly četná nová rozhraní a protokoly.

Vytvoření a standardizace ABNF, primárně dokumentovaná v [IETF](/mobilnisite/slovnik/ietf/) RFC 5234, poskytla řešení, které je jak čitelné pro člověka, tak vhodné pro automatizované zpracování. 3GPP využilo této existující, dobře pochopené normy, aby přineslo formální přísnost do vlastních definic protokolů. Motivací bylo zajistit, aby protokolová datová jednotka definovaná ve specifikaci 3GPP měla jedinou a pouze jednu platnou interpretaci. To umožňuje generování kódu parseru, vytváření testovacích sad pro shodu, které mohou mechanicky ověřit výstup implementace vůči gramatice, a jasnou identifikaci povinných, volitelných a podmíněných elementů uvnitř zprávy. Použitím ABNF 3GPP přešlo od deskriptivních specifikací k preskriptivním, kde je povolená syntax explicitně vyjmenována.

Historicky tento přístup řešil omezení dřívějších ad-hoc metod. Poskytl společný jazyk pro autory norem, implementátory a testery. Pro 3GPP, počínaje zejména Release 8 se System Architecture Evolution (SAE) a zavedením mnoha nových rozhraní založených na Diameter, se ABNF stalo de facto nástrojem pro definování syntaxe těchto protokolů. Jeho použití pokračovalo a rozšířilo se do éry 5G pro definování služebních rozhraní založených na [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/), což dokazuje jeho přizpůsobivost jak binárnímu, tak textovému kódování protokolů. Účel zůstává nezměněn: odstranit odhady při implementaci a sloužit jako jediný zdroj pravdy pro to, co představuje syntakticky platnou protokolovou zprávu, což je základním požadavkem pro globálně interoperabilní telekomunikační ekosystém.

## Klíčové vlastnosti

- Definice formální gramatiky pomocí názvů pravidel, terminálů a operátorů jako alternativa (/) a opakování (*)
- Strojově čitelná syntax umožňující automatizované generování parserů a testování shody
- Podpora definování složitých, vnořených struktur a volitelných elementů uvnitř protokolových datových jednotek
- Integrace základních pravidel (ALPHA, DIGIT atd.) pro definování základních znakových sad
- Schopnost specifikovat přesné rozsahy hodnot znaků a porovnávání řetězců nerozlišující velikost písmen
- Používá se k definování syntaxe jak pro binární/TLV protokoly (např. Diameter AVP), tak pro textové protokoly (např. HTTP hlavičky)

## Definující specifikace

- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.329** (Rel-19) — Diameter Protocol for Sh Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 29.336** (Rel-19) — HSS Diameter Interfaces for PDN Interworking
- **TS 29.337** (Rel-19) — Diameter T4 Interface for MTC Device Triggering
- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TR 33.978** (Rel-8) — Interim Security for Early IMS

---

📖 **Anglický originál a plná specifikace:** [ABNF na 3GPP Explorer](https://3gpp-explorer.com/glossary/abnf/)
