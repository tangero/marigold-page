---
slug: "owser"
url: "/mobilnisite/slovnik/owser/"
type: "slovnik"
title: "OWSER – OMA Web Services Enabler Release"
date: 2025-01-01
abbr: "OWSER"
fullName: "OMA Web Services Enabler Release"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/owser/"
summary: "OWSER je specifikace 3GPP, která definuje integraci web service enablerů Open Mobile Alliance (OMA) do síťové architektury 3GPP. Poskytuje standardizované mechanismy pro vystavování služeb a interakci"
---

OWSER je specifikace 3GPP, která standardizuje integraci OMA web service enablerů do architektury 3GPP pro vystavování služeb a interakci.

## Popis

OWSER, formálně známý jako [OMA](/mobilnisite/slovnik/oma/) Web Services Enabler Release, je technická specifikace 3GPP (TS 23.222), která vytváří rámec pro začlenění služebních enablerů Open Mobile Alliance do ekosystému 3GPP. Jejím hlavním účelem je definovat architektonické principy, rozhraní a procedury, které umožňují entitám sítě 3GPP standardizovaným způsobem interagovat s webovými služebními schopnostmi definovanými OMA. Tato integrace je klíčová pro umožnění poskytovatelům služeb nabízet pokročilé, konvergované služby, které využívají jak funkce telekomunikační sítě, tak aplikační logiku založenou na internetu.

Architektura specifikovaná OWSER zahrnuje definici referenčních bodů mezi síťovými funkcemi 3GPP, jako je IP Multimedia Subsystem (IMS) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), a OMA Service Enablery. Tyto enablery jsou v podstatě znovupoužitelné softwarové komponenty poskytující běžné funkce, jako je přítomnost (presence), zasílání zpráv nebo správa zařízení. OWSER specifikuje, jak jsou tyto enablery objevovány, jak autentizují a autorizují požadavky od síťových funkcí a jak je skutečná služební logika vyvolána pomocí protokolů webových služeb, primárně SOAP/XML přes [HTTP](/mobilnisite/slovnik/http/). Podrobně popisuje nezbytné adaptace, včetně bezpečnostních mechanismů a mapování dat, pro zajištění bezproblémové interoperability mezi doménami 3GPP a OMA.

Specifikace pokrývá několik klíčových aspektů: celkový architektonický model ukazující vztah mezi doménami 3GPP a OMA; definici OWSER Gateway nebo Adaptation Function, která funguje jako mediátor překládající mezi protokoly specifickými pro 3GPP (jako je Diameter) a rozhraními OMA webových služeb; a detailní procedury pro vyvolání služby, odběr (subscription) a oznámení (notification). Poskytnutím této architektury umožňuje OWSER síťovým operátorům bezpečně vystavovat síťové schopnosti (jako je poloha uživatele nebo stav předplatného) autorizovaným OMA aplikacím, což umožňuje vývoj bohatých, kontextově povědomých služeb bez nutnosti, aby vývojáři aplikací rozuměli složitostem podkladových signalizačních protokolů 3GPP.

## K čemu slouží

OWSER byl vytvořen k řešení rostoucí potřeby konvergence mezi tradičními telekomunikačními sítěmi a internetovými webovými službami. Před jeho specifikací byla integrace [OMA](/mobilnisite/slovnik/oma/) služebních enablerů (které byly navrženy s web-centrickou, RESTful nebo SOAP-based filozofií) se sítěmi 3GPP (které spoléhaly na telekomunikačně specifické protokoly jako [MAP](/mobilnisite/slovnik/map/) a Diameter) pro výrobce a operátory složitým, proprietárním a neinteroperabilním úkolem. Tato fragmentace brzdila rychlé nasazení inovativních kombinovaných služeb, které by mohly spojit síťovou inteligenci s aplikační logikou.

Primární motivací bylo využít bohatý ekosystém OMA služebních enablerů – jako jsou ty pro přítomnost (Presence), Push-to-talk over Cellular (PoC) a správu zařízení (Device Management) – v rámci řízeného a bezpečného prostředí sítě operátora 3GPP. OWSER poskytuje standardizovaný 'tmel', který tento integrační problém řeší. Definuje jasnou, dohodnutou metodu pro vystavování služeb, která umožňuje operátorům monetizovat jejich síťové aktiva tím, že je zpřístupní poskytovatelům aplikací třetích stran kontrolovaným způsobem, a zároveň umožňuje tvorbu operátorem spravovaných služeb, které jsou bohatší a funkčně kompletnější. Jeho zavedení v Release 15 bylo v souladu se širším průmyslovým posunem směrem k otevřenosti sítí, architekturám řízeným [API](/mobilnisite/slovnik/api/) a bezproblémovému propojení telekomunikačních a [IT](/mobilnisite/slovnik/it/) schopností, což jsou základní koncepty pro architektury služeb 5G.

## Klíčové vlastnosti

- Standardizovaná architektura pro integraci OMA web service enablerů se sítěmi 3GPP
- Definice adaptačních funkcí (OWSER Gateway) pro překlad protokolů mezi telekomunikační a webovou služební doménou
- Specifikace bezpečnostních mechanismů pro objevování, autentizaci a autorizaci služebních enablerů
- Podpora procedur pro vyvolání služby, odběr (subscription) a oznámení (notification) využívajících protokoly webových služeb
- Umožňuje vystavení schopností sítě 3GPP (např. stav uživatele, poloha) autorizovaným OMA aplikacím
- Usnadňuje vývoj konvergovaných, kontextově povědomých služeb kombinací síťové a aplikační logiky

## Související pojmy

- [OMA – Open Mobile Alliance](/mobilnisite/slovnik/oma/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs

---

📖 **Anglický originál a plná specifikace:** [OWSER na 3GPP Explorer](https://3gpp-explorer.com/glossary/owser/)
