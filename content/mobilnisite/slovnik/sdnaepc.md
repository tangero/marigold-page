---
slug: "sdnaepc"
url: "/mobilnisite/slovnik/sdnaepc/"
type: "slovnik"
title: "SDNAEPC – Secondary DN Authentication and Authorization over EPC"
date: 2025-01-01
abbr: "SDNAEPC"
fullName: "Secondary DN Authentication and Authorization over EPC"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sdnaepc/"
summary: "Mechanismus umožňující sekundární datové síti (DN) provést vlastní autentizaci a autorizaci uživatelského zařízení (UE) připojeného přes Evolved Packet Core (EPC). Umožňuje poskytovatelům služeb uplat"
---

SDNAEPC je mechanismus, který umožňuje sekundární datové síti (Data Network) provést vlastní autentizaci a autorizaci uživatelského zařízení (UE) připojeného přes Evolved Packet Core, což umožňuje nezávislé bezpečnostní politiky nad rámec přístupu 3GPP.

## Popis

SDNAEPC je funkce definovaná ve 3GPP Release 18, která rozšiřuje rámec autentizace a autorizace pro uživatelské zařízení (UE) přistupující ke službám přes Evolved Packet Core. Konkrétně řeší scénáře, kdy uživatelské zařízení (UE), které již prošlo primární přístupovou autentizací sítě 3GPP (např. přes EPS [AKA](/mobilnisite/slovnik/aka/)), potřebuje být samostatně autentizováno a autorizováno sekundární datovou sítí ([DN](/mobilnisite/slovnik/dn/)), jako je podniková síť nebo platforma konkrétního poskytovatele služeb. Architektura zahrnuje UE, obsluhující síť (EPC s [MME](/mobilnisite/slovnik/mme/), [S-GW](/mobilnisite/slovnik/s-gw/), [P-GW](/mobilnisite/slovnik/p-gw/)) a [AAA](/mobilnisite/slovnik/aaa/) server sekundární DN. Proces je typicky integrován do procedur navázání nebo modifikace připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)). Když UE požaduje přístup k sekundární DN, která vyžaduje SDNAEPC, P-GW (fungující jako brána k této DN) komunikuje s AAA serverem DN. P-GW přeposílá zprávy Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) mezi UE a AAA serverem sekundární DN, čímž usnadňuje autentizační dialog založený na EAP. To umožňuje sekundární DN ověřit přihlašovací údaje UE (které jsou oddělené od přihlašovacích údajů USIM) a uplatnit vlastní autorizační politiky, jako je udělení přístupu ke konkrétním službám nebo aplikování filtrů provozu. Úspěšné dokončení této sekundární autentizace vede k navázání PDN připojení s autorizovaným kontextem. Tento mechanismus je klíčový pro scénáře s více nájemci (multi-tenancy), zajišťuje, že sekundární DN si udržuje kontrolu nad tím, která UE mohou přistupovat k jejím zdrojům, a poskytuje další bezpečnostní vrstvu nezávislou na doméně důvěry jádrové sítě mobilního operátora.

## K čemu slouží

SDNAEPC byl vytvořen, aby řešil rostoucí potřebu zabezpečeného a odděleného síťového přístupu v stále více propojeném ekosystému. Tradiční přístupová autentizace EPC (např. pomocí EPS AKA) ověřuje pouze předplatné UE u mobilního operátora (MNO). Mnoho podnikových, průmyslových IoT a specializovaných poskytovatelů služeb však vyžaduje vlastní nezávislou autentizaci před udělením přístupu ke svým citlivým zdrojům. Před SDNAEPC byla taková sekundární autentizace často řešena ad-hoc způsobem na aplikační vrstvě nebo vyžadovala složitá nastavení VPN, což mohlo být neefektivní a postrádat standardizaci. SDNAEPC standardizuje tuto sekundární autentizaci na síťové vrstvě během nastavování PDN připojení. Řeší problém umožnění poskytovateli DN uplatňovat vlastní bezpečnostní politiky bez spoléhání se pouze na autentizaci MNO. To je zvláště důležité pro scénáře, jako je podniková mobilita, kdy společnost potřebuje ověřit přihlašovací údaje zaměstnaneckých zařízení, nebo pro IoT vertikály, kde servisní platforma musí nezávisle autentizovat senzor. Integrací tohoto mechanismu do procedur 3GPP EPC poskytuje zjednodušenou, bezpečnou a standardizovanou metodu pro více doménovou důvěru, což umožňuje nové obchodní modely a předchůdce zabezpečeného síťového řezání (network slicing) v sítích 4G.

## Klíčové vlastnosti

- Umožňuje sekundární, na DN specifickou autentizaci nezávislou na autentizaci přístupu 3GPP
- Využívá EAP (Extensible Authentication Protocol) pro podporu flexibilních autentizačních metod
- Integrováno do procedur navázání a modifikace PDN připojení v EPC
- Umožňuje AAA serveru sekundární DN uplatňovat vlastní autorizační politiky a filtry provozu
- Udržuje oddělení bezpečnostních domén mezi MNO a poskytovatelem DN
- Poskytuje standardizovaný mechanismus pro zabezpečený přístup k podnikovým a IoT sítím přes 4G EPC

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [EAP – Extensible Authentication Protocol](/mobilnisite/slovnik/eap/)

## Definující specifikace

- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [SDNAEPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdnaepc/)
