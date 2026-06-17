---
slug: "ldap"
url: "/mobilnisite/slovnik/ldap/"
type: "slovnik"
title: "LDAP – Lightweight Directory Access Protocol"
date: 2025-01-01
abbr: "LDAP"
fullName: "Lightweight Directory Access Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ldap/"
summary: "Otevřený, dodavatele nezávislý aplikační protokol pro přístup a správu distribuovaných informačních služeb adresáře přes IP síť. V systémech 3GPP je široce používán pro zřizování dat účastníků, přístu"
---

LDAP je otevřený, dodavatele nezávislý protokol pro přístup k distribuovaným adresářovým službám přes IP sítě, používaný v 3GPP pro zřizování účastníků, přístup k EIR a správu konfigurace sítě.

## Popis

Lightweight Directory Access Protocol (LDAP) je standardizovaný protokol založený na TCP/IP, definovaný [IETF](/mobilnisite/slovnik/ietf/) (RFC 4511), pro dotazování a modifikaci adresářových služeb. Adresář je v tomto kontextu specializovaná databáze optimalizovaná pro efektivitu čtení, častá vyhledávání a hierarchické uspořádání popisných dat založených na atributech. LDAP poskytuje model klient-server, kde LDAP klient (např. síťová funkce) odesílá požadavky na LDAP adresářový server, aby provedl operace jako vyhledávání, porovnání, přidání, smazání a úpravu záznamů ve stromu adresářových informací (DIT). Každý záznam je jednoznačně identifikován rozlišujícím jménem ([DN](/mobilnisite/slovnik/dn/)) a skládá se z kolekce atributů, z nichž každý má typ a jednu či více hodnot, řízených schématem. V architekturách 3GPP je LDAP využíván jako lehké a efektivní rozhraní k různým datovým úložištím. Typickým příkladem je integrace s registrem identit zařízení ([EIR](/mobilnisite/slovnik/eir/)), kde síťové elementy jako [MME](/mobilnisite/slovnik/mme/) nebo [AMF](/mobilnisite/slovnik/amf/) používají LDAP k dotazování databáze EIR za účelem kontroly [IMEI](/mobilnisite/slovnik/imei/) mobilního zařízení proti černé, šedé nebo bílé listině. Je také hojně používán v managementových doménách pro zřizování dat účastníků v domácím serveru účastníků ([HSS](/mobilnisite/slovnik/hss/)) nebo pro získávání konfiguračních dat sítě. Protokol typicky funguje na portu 389 (nebo 636 pro LDAPS, SSL zabezpečenou verzi). Operace LDAP vyhledávání, která je nejběžnější, umožňuje klientům specifikovat základní DN, rozsah hledání (základ, jedna úroveň, podstrom) a filtr pro přesnou lokalizaci záznamů odpovídajících kritériím jako "uid=user123". Jeho efektivita pro operace náročné na čtení, standardizovaná povaha a podpora komplexních hierarchických datových struktur z něj činí preferovanou volbu pro integraci pomocných databází a manažerských systémů v telekomunikačních sítích bez nutnosti použití těžkých, transakčně orientovaných databázových protokolů.

## K čemu slouží

LDAP byl v systémech 3GPP přijat pro řešení potřeby standardizované, efektivní a široce podporované metody, kterou síťové elementy používají pro přístup k externím databázím typu adresáře. Před jeho použitím mohla být použita proprietární rozhraní nebo těžší databázové protokoly, což vedlo ke složitosti integrace a závislosti na dodavateli. Návrh protokolu jako lehčí alternativy k protokolu X.500 Directory Access Protocol ([DAP](/mobilnisite/slovnik/dap/)) jej učinil ideálním pro požadavky telekomunikačních sítí na dotazy s vysokým objemem a nízkou latencí. Pro funkce jako kontrola IMEI v EIR síť vyžaduje rychlou, jednoduchou operaci typu "zkontroluj tento identifikátor a vrať stav", což dokonale odpovídá vyhledávací schopnosti LDAP. Jeho hierarchický datový model je vhodný pro reprezentaci strukturovaných síťových a účastnických dat. Motivací pro jeho zařazení byla interoperabilita a provozní efektivita: specifikací LDAP jako standardního rozhraní 3GPP zajistilo, že operátoři mohou nasadit nejlepší adresářové servery (jako OpenLDAP nebo komerční nabídky) a mít různé síťové funkce od různých dodavatelů, které se k nim bezproblémově připojují. Vyřešil problém poskytnutí společné přístupové metody pro sdílená datová úložiště (jako seznamy zakázaných zařízení nebo konfigurační adresáře) napříč sítí s více dodavateli, čímž zjednodušil provoz, snížil vývojové náklady pro dodavatele zařízení a zvýšil síťové bezpečnostní a manažerské schopnosti.

## Klíčové vlastnosti

- Protokol pro dotazování a aktualizaci adresáře: Umožňuje vyhledávání, čtení a úpravu záznamů v hierarchické adresářové službě.
- Model klient-server: Lehký protokol, kde klienti odesílají požadavky na adresářové servery přes TCP/IP.
- Standardizovaný IETF protokol: Založený na RFC IETF, zajišťující interoperabilitu mezi více dodavateli.
- Používán pro přístup k EIR: Standardní rozhraní pro MME/AMF k dotazování registru identit zařízení (EIR) pro kontrolu stavu IMEI.
- Zřizování dat účastníků: Běžně používán v managementových rozhraních pro zřizování dat HSS nebo konfigurace sítě.
- Hierarchický datový model: Organizuje data ve stromové struktuře (DIT) se záznamy identifikovanými rozlišujícími jmény (DN).

## Související pojmy

- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TR 29.935** (Rel-19) — HSS Reference Data Model for Ud Interface
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TR 32.901** (Rel-19) — UDC Application Data Models Study

---

📖 **Anglický originál a plná specifikace:** [LDAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldap/)
