---
slug: "pgk"
url: "/mobilnisite/slovnik/pgk/"
type: "slovnik"
title: "PGK – ProSe Group Key"
date: 2025-01-01
abbr: "PGK"
fullName: "ProSe Group Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pgk/"
summary: "ProSe Group Key je bezpečnostní klíč používaný v LTE Proximity Services (ProSe) pro skupinovou komunikaci. Umožňuje zabezpečenou komunikaci typu jeden-vůči-mnoha mezi zařízeními v blízkosti, nezávisle"
---

PGK je ProSe Group Key, bezpečnostní klíč používaný v LTE Proximity Services pro autentizaci a šifrování zabezpečené skupinové komunikace typu jeden-vůči-mnoha mezi blízkými zařízeními, nezávisle na buněčné síti.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Group Key (PGK) je kryptografický klíč definovaný v bezpečnostní architektuře 3GPP pro Proximity Services (ProSe). ProSe umožňuje komunikaci zařízení mezi sebou (Device-to-Device, [D2D](/mobilnisite/slovnik/d2d/)), kde si uživatelská zařízení (UE) mohou vzájemně detekovat a komunikovat přímo přes rozhraní PC5, a to buď s pokrytím sítí, nebo bez něj. PGK se konkrétně používá pro zabezpečení skupinové komunikace v rámci funkcionality ProSe. Jedná se o klíč na úrovni skupiny, což znamená, že jeden PGK je sdílen mezi všemi členy definované ProSe skupiny. Tato skupina může být vytvořena pro scénáře veřejné bezpečnosti (např. jednotka hasičů) nebo pro komerční aplikace (např. skupina na sociální síti na akci).

Životní cyklus PGK spravuje centrální entita. Pro síťově autorizované ProSe je to typicky ProSe Function v jádru sítě. ProSe Function PGK vygeneruje nebo získá a bezpečně jej zřídí autorizovaným členům skupiny. Zřizování může proběhnout přes rozhraní LTE-Uu, když je UE v síťovém pokrytí. Pro ProSe komunikaci bez síťového pokrytí (UE-to-Network Relay nebo přímá komunikace v místech bez pokrytí) musí být PGK předem zřízen nebo zřízen přes relay. Klíč se používá ve spojení s ProSe Group IP Multicast adresou a ProSe Layer 2 Group ID k identifikaci komunikační skupiny.

Při provozu plní PGK dvě hlavní bezpečnostní funkce: autentizaci a důvěrnost. Pro autentizaci se používá k odvození ProSe Group Integrity Key (PGIK). PGIK se používá k výpočtu hodnot integrity pro skupinové zprávy, což přijímajícím UE umožňuje ověřit, že zpráva pochází od legitimního člena skupiny. Pro důvěrnost se PGK používá k odvození ProSe Group Encryption Key (PGEK). PGEK se používá k zašifrování obsahu skupinových zpráv, čímž se zajistí, že pouze členové disponující PGK mohou obsah dešifrovat. Toto dvojí použití poskytuje zabezpečený kanál pro skupinové vysílání, chránící před odposlechem a vkládáním zpráv neautorizovanými zařízeními.

## K čemu slouží

PGK byl vytvořen k řešení bezpečnostních požadavků skupinové komunikace zařízení mezi sebou (Device-to-Device), která je klíčovým prvkem LTE sítí pro veřejnou bezpečnost a komerčních služeb blízkosti. Tradiční bezpečnost v buněčných sítích spoléhá na trvalý, bod-bod bezpečnostní kontext mezi UE a sítí (např. pomocí klíčů jako KASME). Tento model selhává v [D2D](/mobilnisite/slovnik/d2d/) scénářích, zejména při přímé komunikaci bez účasti sítě. Předchozí ad-hoc komunikační metody postrádaly standardizované, robustní zabezpečení, což je činilo nevhodnými pro citlivou komunikaci veřejné bezpečnosti.

Problémy, které řeší, jsou dvojí. Za prvé poskytuje efektivní a škálovatelné zabezpečení pro komunikaci typu jeden-vůči-mnoha. Použití individuálních párových klíčů pro každého člena ve velké skupině by bylo pro broadcastový provoz neefektivní. Jeden skupinový klíč umožňuje vysílajícímu UE zabezpečit zprávu jednou pro příjem celou skupinou. Za druhé umožňuje zabezpečený provoz mimo síťové pokrytí. Předzřízením PGK může skupina záchranářů udržovat zabezpečenou komunikaci v oblastech katastrof, kde je buněčná infrastruktura poškozena. Jeho vytvoření bylo motivováno kritickými potřebami organizací veřejné bezpečnosti, což vedlo k jeho standardizaci v 3GPP Release 12 a novějších, zajišťující interoperabilitu a vysokou úroveň zabezpečení pro komunikace kritické pro život.

## Klíčové vlastnosti

- Sdílený tajný klíč používaný všemi členy konkrétní ProSe komunikační skupiny.
- Generován a spravován síťovou ProSe Function pro autorizované skupiny.
- Používá se k odvození samostatných klíčů pro ochranu integrity (PGIK) a pro šifrování (PGEK).
- Umožňuje zabezpečenou multicast/broadcast komunikaci přes postranní rozhraní PC5 (sidelink).
- Podporuje ProSe komunikaci jak v síťovém pokrytí, tak mimo něj.
- Nedílná součást bezpečnostní architektury pro Mission Critical Push-To-Talk (MCPTT) přes ProSe.

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 36.323** (Rel-19) — PDCP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PGK na 3GPP Explorer](https://3gpp-explorer.com/glossary/pgk/)
