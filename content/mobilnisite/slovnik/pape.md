---
slug: "pape"
url: "/mobilnisite/slovnik/pape/"
type: "slovnik"
title: "PAPE – Provider Authentication Policy Extension"
date: 2025-01-01
abbr: "PAPE"
fullName: "Provider Authentication Policy Extension"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pape/"
summary: "PAPE je rozšíření ověřovacího protokolu OpenID, které umožňuje závislé straně (Relying Party) vyžádat si od poskytovatele OpenID (OpenID Provider) konkrétní zásady ověřování. V rámci 3GPP je profilová"
---

PAPE (Provider Authentication Policy Extension) je rozšíření protokolu OpenID, profilované v 3GPP TS 33.924, které umožňuje závislé straně (Relying Party) vyžádat si od poskytovatele (Provider) konkrétní zásady ověřování pro zvýšení zabezpečení webových služeb.

## Popis

Provider Authentication Policy Extension (PAPE) je specifikace původně vyvinutá komunitou OpenID a později profilovaná v rámci 3GPP TS 33.924. Rozšiřuje základní ověřovací protokol OpenID, který se používá pro decentralizované jednotné přihlašování ([SSO](/mobilnisite/slovnik/sso/)) napříč webovými stránkami. PAPE umožňuje závislé straně (Relying Party, [RP](/mobilnisite/slovnik/rp/)) – webové stránce nebo službě, ke které se uživatel chce dostat – sdělit její požadavky na zásady ověřování poskytovateli OpenID (OpenID Provider, [OP](/mobilnisite/slovnik/op/)) – subjektu, který uživatele ověřuje. Tyto zásady určují, jak musí být uživatel ověřen, a jdou nad rámec pouhého tvrzení totožnosti tím, že specifikují požadovanou úroveň jistoty (Level of Assurance, LoA).

Technicky PAPE funguje přidáním nových parametrů do požadavku a odpovědi na ověření OpenID. Když RP chce vynutit konkrétní zásady ověřování, zahrne do svého přesměrování na OP parametry `openid.pape.preferred_auth_policies` a volitelně `openid.pape.max_auth_age`. Parametr `preferred_auth_policies` je seznam identifikátorů [URI](/mobilnisite/slovnik/uri/) zásad oddělených mezerami, které definují přijatelné metody ověřování, například `http://schemas.openid.net/pape/policies/2007/06/multi-factor` pro vícefaktorové ověřování nebo `http://schemas.openid.net/pape/policies/2007/06/phishing-resistant` pro mechanismy odolné vůči phishingu. Parametr `max_auth_age` určuje maximální povolenou dobu, která uplynula od posledního ověření uživatele u OP.

Poskytovatel OpenID požadavek zpracuje, pokusí se uživatele ověřit podle požadovaných zásad (nebo podle svých vlastních možností) a poté do ověřovací odpovědi zpět pro RP zahrne odpovídající parametr `openid.pape.auth_policies`. Tato odpověď uvádí zásady ověřování, které byly během relace skutečně použity. RP pak může ověřit, že zásady splňují její bezpečnostní požadavky, než udělí přístup. V rámci ekosystému 3GPP je tento mechanismus integrován do bezpečnostního rámce pro webové služby, což umožňuje síťovým operátorům nebo poskytovatelům služeb vystupujícím jako závislé strany vyžadovat silnější ověřování od poskytovatelů identit, čímž se sladí s regulačními nebo služebně specifickými bezpečnostními potřebami.

## K čemu slouží

PAPE bylo vytvořeno, aby vyřešilo zásadní nedostatek původního protokolu OpenID: ten ověřoval pouze *kdo* uživatel je, ale ne *jak* byl ověřen. [RP](/mobilnisite/slovnik/rp/) neměla způsob, jak zjistit, zda uživatel pouze zadá heslo (zranitelné phishingem), nebo použil silnější metodu, jako je hardwarový token nebo biometrika. To bylo nedostatečné pro služby zpracovávající citlivá data nebo vyžadující soulad s konkrétními úrovněmi jistoty. PAPE poskytuje standardizované rozšíření pro komunikaci požadavků na zásady ověřování, což umožňuje řízení přístupu založené na riziku.

Zavedení a profilace PAPE v TS 33.924 ze strany 3GPP, počínaje Release 9, bylo motivováno rostoucím využíváním webových služeb a služeb IMS (IP Multimedia Subsystem), které mohly využít OpenID pro správu identit. Jak operátoři otevírali své sítě poskytovatelům aplikací třetích stran, vznikla potřeba společného a rozšiřitelného způsobu, jak sdělovat požadavky na sílu ověřování napříč administrativními doménami. PAPE to vyřešilo tím, že umožnilo službě (RP) v jedné doméně trvat na tom, aby poskytovatel ověření ([OP](/mobilnisite/slovnik/op/), potenciálně provozovaný síťovým operátorem) použil metodu s vysokou mírou zabezpečení, než potvrdí totožnost uživatele. To usnadnilo zabezpečené poskytování služeb a pomohlo splnit regulační požadavky na elektronické transakce a přístup k citlivým zdrojům, čímž propojilo standardy webového ověřování s bezpečnostními očekáváními na úrovni telekomunikací.

## Klíčové vlastnosti

- Rozšiřuje protokol OpenID o možnost komunikace požadavků na zásady ověřování
- Umožňuje závislým stranám (Relying Parties) vyžádat si konkrétní metody ověřování prostřednictvím identifikátorů URI zásad
- Podporuje vyžádání maximálního stáří ověření pro vynucení opětovného přihlášení
- Umožňuje poskytovatelům OpenID deklarovat, které zásady byly v odpovědi použity
- Usnadňuje dosažení vyšších úrovní jistoty (LoA) pro citlivé transakce
- Profilováno 3GPP pro zabezpečené ověřování webových a IMS služeb

## Definující specifikace

- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification

---

📖 **Anglický originál a plná specifikace:** [PAPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pape/)
