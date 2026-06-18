---
slug: "duik"
url: "/mobilnisite/slovnik/duik/"
type: "slovnik"
title: "DUIK – Discovery User Integrity Key"
date: 2025-01-01
abbr: "DUIK"
fullName: "Discovery User Integrity Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/duik/"
summary: "Kryptografický klíč používaný ve službách bezprostřední blízkosti (ProSe) k zajištění integrity a autentizace původu zpráv vyměňovaných během objevování mezi zařízeními. Chrání signalizaci objevování"
---

DUIK je kryptografický klíč používaný v ProSe k zajištění integrity a autentizace původu zpráv během zařízení-zařízení objevování, který je chrání před neoprávněnou manipulací a paděláním.

## Popis

Discovery User Integrity Key (DUIK) je bezpečnostní klíč definovaný v rámci architektury služeb bezprostřední blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) 3GPP. Je odvozen spolu s klíčem Discovery User Confidentiality Key ([DUCK](/mobilnisite/slovnik/duck/)) a tvoří druhou polovinu bezpečnostního páru pro ochranu signalizace přímého objevování mezi uživatelskými zařízeními (UE). Specifickou rolí DUIK je poskytovat ochranu integrity a autentizaci původu dat pro zprávy objevování. To znamená, že umožňuje přijímajícímu UE ověřit, že přijaté oznámení nebo žádost o objevení nebylo během přenosu změněno a že skutečně pochází z deklarovaného odesílatele.

Technicky je DUIK odvozen pomocí funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)), jak je specifikováno v 3GPP TS 33.220. Vstupy pro odvození zahrnují kořenový ProSe klíč (např. K_ProSe) a specifické parametry vázané na relaci objevování. Když UE generuje zprávu objevování, použije DUIK k výpočtu kódu autentizace zprávy ([MAC](/mobilnisite/slovnik/mac/)), často s využitím algoritmu jako HMAC-SHA-256. Tento MAC je připojen ke zprávě objevování (která sama může být zašifrována pomocí DUCK). Přijímající UE, která disponuje stejným DUIK, přepočítá MAC z přijaté zprávy a porovná jej s přenášeným MAC. Shoda potvrdí integritu a autentizuje zdroj.

Architektonicky je DUIK zřizován a spravován společně s DUCK. ProSe funkce v síti je zodpovědná za autorizaci objevování a za to, aby se účastnící se UE mohly odvodit správné klíče. DUIK funguje na ProSe protokolové vrstvě a rozhraní s protokolem objevování specifikovaným v TS 24.334. Jeho použití je klíčové pro prevenci útoků založených na objevování, jako je vkládání zpráv, kdy by škodlivé zařízení mohlo posílat falešné informace o objevení za účelem narušení služeb nebo vytvoření zmatku. Ve scénářích veřejné bezpečnosti je integrita zprávy objevování typu "záchranář v blízkosti" stejně důležitá jako její důvěrnost. DUIK zajišťuje, že architektura objevování je odolná vůči takovým útokům, a vytváří tak důvěryhodný základ pro následné nastavení komunikace mezi zařízeními.

## K čemu slouží

DUIK byl zaveden v 3GPP Release 13 spolu s [DUCK](/mobilnisite/slovnik/duck/), aby splnil komplexní bezpečnostní požadavky služeb bezprostřední blízkosti ([ProSe](/mobilnisite/slovnik/prose/)). Zatímco důvěrnost (zajištěná DUCK) chrání obsah zpráv objevování, ochrana integrity byla identifikována jako stejně kritický požadavek. Bez ní by útočník mohl upravovat zprávy objevování nebo je zcela padělat, což by vedlo ke zfalšování identit, narušení služeb nebo škodlivému přesměrování komunikace – což je obzvláště nebezpečné ve scénářích veřejné bezpečnosti a kritické komunikace.

Účelem DUIK je poskytnout tento zásadní garance autenticity a integrity zpráv pro proces objevování. Motivace vychází z nepřátelského prostředí otevřené rádiové komunikace; jakékoli zařízení v dosahu rádiového signálu může potenciálně vysílat nebo rušit signály. Předchozí modely bezpečnosti v celulárních sítích předpokládaly důvěryhodnou základnovou stanici jako protistranu. V přímém [D2D](/mobilnisite/slovnik/d2d/) objevování komunikují zařízení bez tohoto prostředníka, což vyžaduje peer-to-peer bezpečnostní mechanismus. DUIK řeší problém, jak může UE věřit, že vysílání objevování je pravé a nezměněné. Umožněním autentizace zdroje zabraňuje zneužití identity a zajišťuje, že proces objevování, který je prvním krokem k navázání přímého spojení, je bezpečný a spolehlivý. Jednalo se o zásadní inovaci, která umožnila využití ProSe pro bezpečnostně citlivé aplikace nad rámec jednoduchých komerčních služeb typu najdi-a-připoj-se.

## Klíčové vlastnosti

- Poskytuje ochranu integrity a autentizaci původu dat pro zprávy přímého objevování ProSe
- Odvozen z hierarchie ProSe klíčů pomocí standardizované funkce pro odvozování klíčů
- Používá se k vytváření a ověřování kódů autentizace zpráv (MAC) na signalizaci objevování
- Chrání před manipulací s objevovacími zprávami, paděláním a útoky opakováním
- Spolupracuje s DUCK, aby vytvořil kompletní bezpečnostní sadu pro důvěrnost a integritu
- Nezbytný pro důvěryhodné objevování v síťově asistovaných i autonomních režimech ProSe

## Definující specifikace

- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.555** (Rel-19) — 5G ProSe UE Policies Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay

---

📖 **Anglický originál a plná specifikace:** [DUIK na 3GPP Explorer](https://3gpp-explorer.com/glossary/duik/)
