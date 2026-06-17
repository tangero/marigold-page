---
slug: "ief"
url: "/mobilnisite/slovnik/ief/"
type: "slovnik"
title: "IEF – Identity Event Function"
date: 2025-01-01
abbr: "IEF"
fullName: "Identity Event Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ief/"
summary: "Síťová funkce zavedená v 5G pro bezpečné služby ověřování identity s ochranou soukromí. Funguje jako důvěryhodný zprostředkovatel mezi stranou spoléhající se na ověření (Relying Party, např. online sl"
---

IEF je síťová funkce 5G sítě, která funguje jako důvěryhodný zprostředkovatel pro bezpečné ověřování identity s ochranou soukromí mezi poskytovatelem identity (Identity Provider) a stranou spoléhající se na ověření (Relying Party).

## Popis

Funkce pro správu identitních událostí (Identity Event Function, IEF) je klíčovou součástí rámce pro správu identity a autentizaci 3GPP, standardizovaného od Release 16. Funguje jako služba v architektuře systému 5G, konkrétně definovaná pro usnadnění bezpečných transakcí ověřování identity se zvýšenou ochranou soukromí. Primární úlohou IEF je zprostředkování mezi stranou spoléhající se na ověření (Relying Party, RP) – entitou, která potřebuje ověřit atributy uživatele (jako věk nebo stav členství) – a poskytovatelem identity (Identity Provider, IdP), který spravuje identifikační údaje uživatele. Činí tak zpracováním identitních událostí (identity events), což jsou žádosti o ověření konkrétních atributů nebo přihlašovacích údajů uživatele.

Architektonicky je IEF definována jako síťová funkce s rozhraním založeným na službách (service-based interface), typicky služba Nidf_IdentityEventManagement. Interaguje s uživatelským zařízením (UE, User Equipment), stranou spoléhající se na ověření (Relying Party) a poskytovatelem identity (Identity Provider). Pracovní postup začíná, když strana spoléhající se na ověření, potřebující ověřit atribut uživatele, odešle žádost o identitní událost (Identity Event Request) k IEF. IEF následně komunikuje s UE (prostřednictvím uživatele), aby získala souhlas a potřebné přihlašovací údaje. Může také komunikovat s IdP za účelem jejich ověření. Klíčové je, že IEF zajišťuje minimální zveřejnění; pouze potvrdí, zda atributy uživatele splňují politiku RP (např. „uživatel je starší 18 let“), aniž by odhalila skutečnou hodnotu atributu nebo jiné osobní údaje. Toho je dosaženo prostřednictvím mechanismů založených na tokenech a kryptografických protokolů.

IEF je klíčovým prvkem pro vizi 3GPP, v níž mobilní síť slouží jako důvěryhodná platforma pro digitální identitu. Využívá inherentní zabezpečení předplatného 3GPP (např. SIM/USIM) a autentizační infrastrukturu sítě. Poskytnutím standardizované síťové funkce pro ověřování identity umožňuje poskytovatelům služeb (RP) outsourcovat složité kontroly identity do sítě operátora, a to způsobem, který je kompatibilní a interoperabilní. To je podrobně popsáno ve specifikacích 33.127 a 33.128, které pokrývají bezpečnostní rámec a protokoly pro správu identitních událostí. IEF podporuje různé formáty přihlašovacích údajů a může pracovat s poskytovateli identity jak 3GPP (např. přihlašovací údaje 3GPP), tak i mimo 3GPP.

## K čemu slouží

IEF byla vytvořena, aby řešila rostoucí potřebu bezpečného, souhlasem uživatele řízeného a soukromí chránícího ověřování digitální identity v online službách. Před jejím zavedením ověřování identity často zahrnovalo přímé sdílení citlivých osobních údajů uživatele (jako naskenované doklady totožnosti) s mnoha online stranami spoléhajícími se na ověření (Relying Parties), což vytvářelo významná rizika pro soukromí a zranitelnosti vůči únikům dat. Nebyla k dispozici standardizovaná funkce na úrovni sítě pro usnadnění minimálního zveřejňování atributů. Motivací byly předpisy jako GDPR, které zdůrazňují minimalizaci dat a souhlas uživatele, a také potřeba průmyslu bojovat proti podvodům a zároveň zlepšovat uživatelský zážitek.

Historicky byla správa identity fragmentovaná, založená na proprietárních řešeních nebo závislá na poskytovatelích přihlášení přes sociální sítě, kteří mohli sledovat aktivitu uživatele napříč službami. IEF od 3GPP poskytuje standardizovanou alternativu úrovně operátora (carrier-grade), která využívá důvěryhodnou roli mobilního operátora a jeho stávající procesy ověřování zákazníka (Know Your Customer). Řeší problém, jak prokázat aspekty své identity bez odhalení celé identity, což je koncept známý jako ověřitelné přihlašovací údaje (verifiable credentials) nebo selektivní zveřejnění (selective disclosure). Vytvořením specializované funkce v architektuře 5G umožňuje 3GPP mobilním sítím nabízet identitu jako službu (identity-as-a-service), čímž se otevírají nové zdroje příjmů pro operátory a zároveň uživatelům poskytuje větší kontrolu a soukromí.

## Klíčové vlastnosti

- Zprostředkovává žádosti o ověření identity mezi stranami spoléhajícími se na ověření (Relying Parties) a poskytovateli identity (Identity Providers)
- Zajišťuje ochranu soukromí prostřednictvím minimálního zveřejňování (ověřuje predikáty, nikoliv surová data)
- Podporuje získání a správu souhlasu uživatele pro sdílení identity
- Využívá zabezpečenou autentizační infrastrukturu 3GPP a přihlašovací údaje k předplatnému
- Poskytuje standardizované rozhraní založené na službách (Service-Based Interface, Nidf_IdentityEventManagement)
- Zpracovává různé typy přihlašovacích údajů a formáty identitních událostí

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [IEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ief/)
