---
slug: "hip"
url: "/mobilnisite/slovnik/hip/"
type: "slovnik"
title: "HIP – Host Identity Protocol"
date: 2025-01-01
abbr: "HIP"
fullName: "Host Identity Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hip/"
summary: "HIP je protokol pro identifikaci hostitele a správu mobility, který odděluje identitu hostitele od jeho síťové polohy. Zavádí kryptografickou identitu hostitele (HI), čímž odděluje transportní vrstvu"
---

HIP je protokol pro identifikaci hostitele a správu mobility, který odděluje identitu hostitele od jeho síťové polohy pomocí kryptografické identity hostitele (Host Identity) za účelem umožnění bezpečné mobility a multihoming.

## Popis

Protokol Host Identity Protocol (HIP), zkoumaný 3GPP ve specifikaci 22.980, je protokol Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)), který zásadně mění architekturu tradiční IP zásobníku zavedením nového jmenného prostoru: identity hostitele (Host Identity). V konvenčním IP plní IP adresa dvojí roli: lokátoru (kde se hostitel v síti nachází) a identifikátoru (kdo hostitel je). HIP tyto role odděluje. Hostiteli přiděluje trvalou kryptografickou identitu hostitele ([HI](/mobilnisite/slovnik/hi/)), typicky veřejný klíč, která slouží jako stabilní identifikátor hostitele. IP adresa je pak používána čistě jako lokátor, který se může měnit při pohybu hostitele. K tomuto oddělení dochází mezi síťovou vrstvou (vrstva 3, IP) a transportní vrstvou (vrstva 4, např. TCP, [UDP](/mobilnisite/slovnik/udp/)). Mezi tyto vrstvy je vložena HIP vrstva, která mapuje stabilní identity hostitelů na měnící se IP adresy.

Protokol funguje prostřednictvím čtyřfázového handshake známého jako HIP Base Exchange. Když spolu chtějí komunikovat dva hostitelé s podporou HIP (iniciátor a odpovídač), nejprve provedou tento kryptografický handshake. Během této výměny se vzájemně autentizují pomocí svých identit hostitele (veřejných klíčů) a vytvoří pár bezpečnostních asociací ([SA](/mobilnisite/slovnik/sa/)) [IPsec](/mobilnisite/slovnik/ipsec/) Encapsulating Security Payload ([ESP](/mobilnisite/slovnik/esp/)) pro zabezpečení následných datových přenosů. Handshake také vede k vytvoření 128bitového tagu identity hostitele (HIT), což je hash veřejného klíče, který se používá v hlavičkách paketů jako kompaktní identifikátor. Jakmile je HIP asociace navázána, sokety transportní vrstvy jsou vázány na HITy, nikoli na IP adresy. Pokud se IP adresa hostitele změní kvůli mobilitě, může jednoduše odeslat svému protějšku paket UPDATE s informací o novém lokátoru a komunikace může plynule pokračovat bez přerušení spojení na transportní vrstvě, protože identifikátor koncového bodu soketu (HIT) zůstává konstantní.

Architektura HIP poskytuje několik silných schopností. Pro mobilitu umožňuje hostiteli změnit všechny své IP adresy při zachování probíhajících relací, což je koncept známý jako mobilita koncového hostitele (end-host mobility). Pro multihoming může mít hostitel více IP adres (např. přes Wi-Fi a mobilní síť) a může o všech dostupných lokátorech informovat svůj protějšek, což umožňuje převzetí služeb při selhání (failover) a vyrovnávání zatížení. Bezpečnost je vnitřní, protože identita hostitele je kryptografická; Base Exchange poskytuje vzájemnou autentizaci a umožňuje snadné vytvoření klíčů pro IPsec. V kontextu 3GPP byl HIP zkoumán jako potenciální řešení mobility mobilního uzlu, zejména pro scénáře, kde nebyly žádoucí síťové protokoly mobility jako [GTP](/mobilnisite/slovnik/gtp/) nebo [PMIP](/mobilnisite/slovnik/pmip/), nebo pro umožnění nových modelů důvěry a bezproblémové mobility napříč heterogenními přístupovými sítěmi.

## K čemu slouží

HIP byl vytvořen k řešení základních architektonických omezení původní sady protokolů Internetu, kde IP adresa přetěžuje sémantiku jak lokátoru, tak identity. Toto přetížení způsobuje známé problémy s mobilitou hostitele, multihomingem a bezpečností. Když se hostitel přesune a změní svou IP adresu, všechna existující spojení na transportní vrstvě (relace TCP) vázaná na starou adresu se přeruší. Řešení jako Mobile IP to obcházejí na síťové vrstvě, ale často zavádějí trojúhelníkové směrování a složitost. Účelem HIP je poskytnout čisté architektonické řešení zavedením samostatné, trvalé vrstvy identity, čímž umožní bezproblémovou mobilitu a multihoming na úrovni koncového hostitele.

Zájem 3GPP o HIP, zdokumentovaný v TR 22.980, pramenil z jeho potenciálu poskytnout alternativní mechanismy správy mobility pro uživatelské zařízení (UE) v mobilních sítích. Zatímco sítě 3GPP tradičně spoléhají na síťově řízenou mobilitu (např. předávání řízené RAN a jádrem sítě), HIP nabízel hostitelsky orientovaný přístup. To by mohlo být přínosné pro scénáře zahrnující mobilitu napříč nepřístupovými sítěmi 3GPP (jako Wi-Fi) nebo pro umožnění nových servisních modelů, kde si UE spravuje své vlastní lokátory. Vestavěná kryptografická identita HIP také slibovala zjednodušení vytváření bezpečnostních asociací, což by mohlo zefektivnit procedury pro autentizaci přístupu k síti a zabezpečení komunikace end-to-end. Studie si kladla za cíl pochopit, jak by HIP mohl doplňovat nebo integrovat se stávajícími architekturami mobility a bezpečnosti 3GPP, a prozkoumat jeho potenciální přínosy pro budoucí vývoj sítí.

## Klíčové vlastnosti

- Odděluje identitu hostitele od síťové polohy pomocí kryptografických identit hostitele
- Umožňuje bezproblémovou mobilitu koncového hostitele a multihoming
- Používá čtyřfázový Base Exchange pro vzájemnou autentizaci a vytvoření klíčů
- Váže spojení transportní vrstvy na stabilní tagy identity hostitele (HIT)
- Využívá IPsec ESP pro zabezpečený přenos datových přenosů
- Poskytuje základ pro zvýšenou bezpečnost a důvěru v internetové komunikaci

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [IETF – Internet Engineering Task Force Standard](/mobilnisite/slovnik/ietf/)

## Definující specifikace

- **TR 22.980** (Rel-19) — Network Composition Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [HIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hip/)
