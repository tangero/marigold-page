---
slug: "nrpik"
url: "/mobilnisite/slovnik/nrpik/"
type: "slovnik"
title: "NRPIK – NR PC5 Integrity Key"
date: 2025-01-01
abbr: "NRPIK"
fullName: "NR PC5 Integrity Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nrpik/"
summary: "Kryptografický klíč používaný k zajištění integrity a ochrany proti opětovnému přehrání pro signalizaci a data na 5G NR PC5 sidelinku. Zajišťuje, že zprávy mezi zařízeními nebyly změněny ani padělány,"
---

NRPIK je kryptografický klíč používaný k zajištění integrity a ochrany proti opětovnému přehrání pro signalizaci a data přenášená přes 5G NR PC5 sidelink rozhraní.

## Popis

NR PC5 Integrity Key (NRPIK) je symetrický kryptografický klíč tvořící složku ochrany integrity v bezpečnostním souboru pro rozhraní PC5 založené na New Radio (NR). Toto rozhraní umožňuje přímou komunikaci mezi zařízeními (sidelink) pro 5G Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). NRPIK je odvozen definovanou klíčovou hierarchií, často vycházející z hlavního klíče vytvořeného během procesu autorizace PC5 spoje, který může zahrnovat síťové funkce jako ProSe Function nebo V2X Control Function. Jeho jediným účelem je umožnit přijímajícímu UE ověřit, že zpráva přijatá přes PC5 rozhraní nebyla během přenosu pozměněna, znovu přehrána nebo vyrobena neoprávněnou stranou.

Provozně se NRPIK používá integritním ochranným algoritmem ve vrstvě [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol) pro NR sidelink. Pro každý datový paket nebo řídicí zprávu vyžadující ochranu je pomocí NRPIK a dalších vstupů (jako data paketu a čítač) vypočítán Message Authentication Code ([MAC-I](/mobilnisite/slovnik/mac-i/)). Tento MAC-I je před přenosem připojen ke zprávě. Příjemce, který disponuje stejným NRPIK, přepočítá MAC-I z přijatých dat a porovná jej s přijatou hodnotou. Neshoda signalizuje potenciální narušení integrity a paket je zahozen. Tento proces chrání jak uživatelská data, tak kritickou řídicí signalizaci, čímž zajišťuje autenticitu příkazů a výměn informací ve scénářích jako je jízda v koloně nebo oznámení vozidel záchranných služeb.

NRPIK je vždy používán společně s NR PC5 Encryption Key ([NRPEK](/mobilnisite/slovnik/nrpek/)) pro kompletní bezpečnostní asociaci, jedná se však o odlišný klíč. Toto oddělení klíčů pro integritu a šifrování je základním bezpečnostním principem, který omezuje rozsah kompromitace při prozrazení jednoho klíče a umožňuje nezávislý vývoj algoritmů. NRPIK je spravován na bázi jednotlivých bezpečnostních asociací, což znamená, že každý zabezpečený PC5 komunikační spoj nebo skupina má svůj vlastní unikátní integritní klíč. Správa životního cyklu klíče, včetně odvození, aktivace a případné obnovy, je řízena protokoly definovanými ve specifikacích 3GPP, což zajišťuje, že klíče zůstávají čerstvé a odolné vůči kryptoanalytickým útokům v čase.

## K čemu slouží

NRPIK byl vytvořen, aby splnil kritické požadavky na integritu a autentizaci původu pro komunikaci přes 5G NR sidelink, které jsou zásadní pro bezpečnostní a spolehlivé komerční aplikace. V LTE [V2X](/mobilnisite/slovnik/v2x/) byla také definována ochrana integrity, ale nástup 5G NR sidelinku s vylepšenými schopnostmi (jako pokročilá alokace zdrojů, vyšší frekvence a nové případy užití, například sdílení senzorů) si vyžádal novou, nativně NR klíčovou hierarchii a integraci. Motivací jsou závažné důsledky přijetí padělaných nebo pozměněných zpráv ve scénářích přímé komunikace; například pozměněná varovná zpráva o brzdění mezi vozidly může vést k nehodám.

Před standardizovanou ochranou integrity byla přímá komunikace zranitelná vůči útokům typu vložení, modifikace a opětovného přehrání zpráv. NRPIK tyto hrozby řeší tím, že poskytuje standardizovaný, kryptograficky robustní mechanismus pro ověření autenticity zprávy. Jeho vývoj byl hnáním požadavky automobilového průmyslu, požadavky na veřejnou bezpečnost a obecnou potřebou důvěryhodné přímé komunikace jako součásti 5G ekosystému. Řeší problém zajištění důvěryhodnosti dat v decentralizovaném komunikačním modelu, kde není vždy přítomný síťový zprostředkovatel, který by zprávy ověřoval, čímž umožňuje bezpečnou a spolehlivou autonomní koordinaci mezi zařízeními na okraji sítě.

## Klíčové vlastnosti

- Poskytuje integritu a ochranu proti opětovnému přehrání pro data a signalizaci na NR PC5 rozhraní.
- Je odvozen společně s NRPEK jako součást NR PC5 klíčové hierarchie po autentizaci.
- Je využíván vrstvou NR PDCP k vytváření a ověřování Message Authentication Codes (MAC-I).
- Je odlišný od klíče NRPEK, čímž vynucuje oddělení funkcí integrity a důvěrnosti.
- Je aplikován na každou PC5 bezpečnostní asociaci, což zajišťuje izolaci mezi různými komunikačními relacemi.
- Je nezbytný pro zaručení autenticity zpráv v bezpečnostně kritických aplikacích V2X a ProSe.

## Definující specifikace

- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.536** (Rel-19) — 5G V2X Security for NR PC5

---

📖 **Anglický originál a plná specifikace:** [NRPIK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrpik/)
