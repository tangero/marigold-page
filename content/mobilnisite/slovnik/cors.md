---
slug: "cors"
url: "/mobilnisite/slovnik/cors/"
type: "slovnik"
title: "CORS – Cross-Origin Resource Sharing"
date: 2025-01-01
abbr: "CORS"
fullName: "Cross-Origin Resource Sharing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cors/"
summary: "CORS je bezpečnostní mechanismus, který umožňuje webovým aplikacím běžícím v jednom zdroji přistupovat k prostředkům z jiného zdroje. V 3GPP umožňuje bezpečné meziodkazové volání API pro funkce zveřej"
---

CORS je bezpečnostní mechanismus, který umožňuje webovým aplikacím z jednoho zdroje (origin) přistupovat k prostředkům z jiného zdroje, což umožňuje bezpečné meziodkazové (cross-origin) volání API pro funkce zveřejnění sítě (network exposure functions) 3GPP.

## Popis

Cross-Origin Resource Sharing (CORS) v 3GPP je bezpečnostní mechanismus implementovaný v architekturách Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Service Capability Exposure Function (SCEF) pro umožnění bezpečných meziodkazových [HTTP](/mobilnisite/slovnik/http/) požadavků. Mechanismus funguje prostřednictvím standardizované sady HTTP hlaviček, které serverům umožňují deklarovat, které zdroje mají povolen přístup k jejich prostředkům. Když se webová aplikace z jednoho zdroje pokusí přistoupit k prostředkům z jiného zdroje, prohlížeč odešle předletový (preflight) požadavek pomocí metody OPTIONS, který obsahuje hlavičky Origin, Access-Control-Request-Method a Access-Control-Request-Headers. Server odpoví hlavičkami Access-Control-Allow-Origin, Access-Control-Allow-Methods, Access-Control-Allow-Headers a Access-Control-Allow-Credentials, aby specifikoval, co je povoleno.

Architektura se integruje s rámcem pro zveřejnění sítě 3GPP, kde NEF/SCEF funguje jako server s podporou CORS, který zveřejňuje síťové schopnosti autorizovaným aplikačním funkcím (AFs). Mechanismus funguje tak, že zachycuje HTTP požadavky od externích aplikací a ověřuje je vůči nakonfigurovaným CORS politikám před povolením přístupu k síťovým [API](/mobilnisite/slovnik/api/). Mezi klíčové komponenty patří databáze konfigurace CORS politik, modul pro validaci zdroje, engine pro vkládání hlaviček a obsluha předletových požadavků. Tyto komponenty spolupracují na ověření požadavků, vložení příslušných CORS hlaviček do odpovědí a vynucení bezpečnostních politik definovaných síťovými operátory.

CORS funguje prostřednictvím vícekrokového procesu handshake. Nejprve klientská aplikace odešle HTTP požadavek s hlavičkou Origin označující její zdroj. Server tento zdroj zkontroluje vůči své povolené listině (whitelist) a rozhodne, zda požadavek povolí. Pro složité požadavky (ty, které používají jiné metody než GET, HEAD nebo POST, nebo které obsahují vlastní hlavičky), prohlížeč automaticky odešle předletový OPTIONS požadavek před skutečným požadavkem. Server na tento předletový požadavek odpoví hlavičkami, které označují, které metody, hlavičky a zdroje jsou povoleny. Teprve pokud předletový požadavek uspěje, pokračuje prohlížeč se skutečným požadavkem.

Role tohoto mechanismu v sítích 3GPP je klíčová pro umožnění bezpečného přístupu třetích stran k síťovým schopnostem při zachování bezpečnostního modelu politiky stejného zdroje (same-origin policy). Umožňuje síťovým operátorům zveřejňovat API pro služby jako řízení kvality služby (QoS), lokalizační služby a monitorování stavu sítě autorizovaným externím aplikacím bez kompromitování bezpečnosti. Implementace následuje principy RESTful a integruje se s OAuth 2.0 pro autentizaci a autorizaci, čímž vytváří komplexní bezpečnostní rámec pro zveřejnění sítě.

## K čemu slouží

CORS byl v 3GPP zaveden, aby řešil bezpečnostní výzvy spojené se zveřejňováním síťových schopností třetím stranám prostřednictvím webových [API](/mobilnisite/slovnik/api/). Před implementací CORS čelily funkce zveřejnění sítě omezením politiky stejného zdroje, která bránila webovým aplikacím v provádění meziodkazových požadavků, což nutilo vývojáře používat méně bezpečná řešení jako JSONP nebo proxy servery. Tato řešení zaváděla bezpečnostní zranitelnosti a složitost při správě přístupu třetích stran k síťovým prostředkům.

Historický kontext pro CORS v 3GPP vychází z rostoucí poptávky po síťových API v éře 5G a síťového řezání (network slicing), kde třetí strany potřebují bezpečný přístup k síťovým schopnostem. Tradiční přístupy vyžadovaly složité proxy architektury nebo uvolněné bezpečnostní politiky, které vystavovaly sítě potenciálním útokům. CORS poskytuje standardizovaný, bezpečný mechanismus, který zachovává bezpečnost prohlížeče a zároveň umožňuje legitimní meziodkazové požadavky, čímž řeší základní napětí mezi bezpečností a funkcionalitou ve scénářích zveřejnění sítě.

CORS řeší konkrétní problém umožnění bezpečné komunikace mezi webovými aplikacemi hostovanými na různých doménách a funkcemi zveřejnění sítě 3GPP. Umožňuje síťovým operátorům udržovat přísné bezpečnostní hranice a zároveň poskytovat řízený přístup k síťovým API, čímž podporuje obchodní model zveřejňování síťových schopností jako služeb. Mechanismus řeší omezení předchozích přístupů tím, že poskytuje řešení založené na standardech, které se integruje s existujícími webovými bezpečnostními modely a implementacemi prohlížečů.

## Klíčové vlastnosti

- Řízení přístupu na základě zdroje (origin) prostřednictvím HTTP hlaviček
- Mechanismus předletového (preflight) požadavku pro složité meziodkazové požadavky
- Integrace s autentizačními a autorizačními rámci 3GPP
- Konfigurovatelné CORS politiky pro různé koncové body API
- Podpora pro přihlašované (credentialed) požadavky s cookies a HTTP autentizací
- Validace a vkládání hlaviček pro bezpečné odpovědi

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TR 26.957** (Rel-19) — Evaluation of MPEG DASH SAND for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CORS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cors/)
