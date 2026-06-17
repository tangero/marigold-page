---
slug: "altc"
url: "/mobilnisite/slovnik/altc/"
type: "slovnik"
title: "ALTC – Alternate Connectivity"
date: 2025-01-01
abbr: "ALTC"
fullName: "Alternate Connectivity"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/altc/"
summary: "Alternate Connectivity (ALTC) je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) udržovat více současných připojení k různým přístupovým sítím. Umožňuje směrovat provoz alternativními cestami,"
---

ALTC je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) udržovat více současných připojení k různým přístupovým sítím pro zvýšenou spolehlivost a kontinuitu služeb.

## Popis

Alternate Connectivity (ALTC) je sofistikovaný mechanismus správy mobility definovaný ve specifikacích 3GPP, především v TS 23.334 (Proximity-services (ProSe) architecture) a TS 29.162 (Interworking between the IMS and non-IMS networks). Funguje na síťové vrstvě a umožňuje uživatelskému zařízení (UE) navázat a udržovat více aktivních připojení k různým přístupovým sítím současně. Tyto sítě mohou zahrnovat 3GPP přístup (jako LTE nebo 5G NR) i ne-3GPP přístup (například Wi-Fi nebo pevný broadband), které jsou spravovány prostřednictvím funkcí jádra sítě, jako je Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Architektura zahrnuje koordinaci mezi UE, obsluhující sítí a potenciálně funkcí ProSe nebo Application Function pro objevování, autentizaci a správu alternativních připojovacích cest.

V jádru ALTC funguje tak, že umožňuje UE registrovat více připojení k paketové datové síti (PDN) nebo PDU session přes různé typy přístupu. Síť poskytuje UE politiky, které ji instruují, kdy a jak tyto alternativní cesty používat. Například síť může určit, že určité IP toky nebo služby mají být směrovány přes primární 3GPP přístup, ale pokud kvalita tohoto přístupu klesne pod prahovou hodnotu (např. síla signálu nebo latence), má UE plynule přepnout tyto toky na navázané alternativní ne-3GPP připojení bez přerušení session. To je řízeno prostřednictvím mechanismů IP flow mobility ([IFOM](/mobilnisite/slovnik/ifom/)) nebo multi-access PDU session ([MA](/mobilnisite/slovnik/ma/) PDU), kde může být stejná IP adresa zachována při předání spojení, aby byla zachována kontinuita aplikace.

Klíčové komponenty v rámci ALTC zahrnují UE, která musí podporovat více rozhraní a schopnost provádět síťové politiky; funkce politiky v jádru sítě (ANDSF/PCF), které generují a poskytují tyto připojovací politiky; a uzly brány (např. PGW v EPC nebo [UPF](/mobilnisite/slovnik/upf/) v 5GC), které kotví uživatelskou rovinu a usnadňují směrování provozu přes různé přístupy. Ve scénářích zahrnujících služby na blízkost (proximity services) může funkce ProSe pomáhat při objevování blízkých UE nebo sítí, které mohou sloužit jako alternativní připojovací body, což umožňuje cesty typu zařízení-zařízení nebo UE-síťový přenos. Role ALTC spočívá ve vytvoření robustního, multi-homed připojovacího prostředí, které maximalizuje využití zdrojů, zlepšuje uživatelský zážitek prostřednictvím plynulé mobility a poskytuje redundanci pro kritickou komunikaci.

Z protokolového hlediska se ALTC opírá o rozšíření stávajících protokolů pro správu mobility a session. Například v 5G umožňuje Non-3GPP Interworking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) bezpečnou integraci nedůvěryhodného ne-3GPP přístupu do 5G Core. Politiky jsou komunikovány pomocí protokolů jako S14 pro ANDSF nebo RESTful [API](/mobilnisite/slovnik/api/) pro PCF. UE průběžně monitoruje výkonnost svých aktivních přístupů a uplatňuje pravidla politik pro rozhodování o směrování, což může spouštět předání spojení na úrovni toku. Tato detailní kontrola umožňuje optimalizované vyvažování zátěže a správu kvality služeb (QoS), což zajišťuje, že provoz s vysokou prioritou vždy využívá nejlepší dostupnou cestu.

## K čemu slouží

ALTC bylo vytvořeno, aby řešilo rostoucí poptávku po službách typu 'vždy nejlépe připojen' a odolnosti sítě v mobilních komunikacích. Před jeho zavedením se UE typicky spoléhala na jedno aktivní připojení v daném čase, přičemž předání spojení mezi přístupy způsobovalo přerušení služeb nebo ztrátu paketů. To bylo nedostatečné pro nově vznikající aplikace, jako je video v reálném čase, VoIP a komunikace pro veřejnou bezpečnost, které vyžadují nepřerušené připojení i v náročných rádiových podmínkách. Omezení jednocestného připojení se stalo zvláště zřejmým s rozšířením heterogenních sítí, kde se 3GPP buněčné pokrytí překrývá s hustými Wi-Fi hotspoty, přičemž uživatelé nemohli obě současně využívat pro redundanci nebo agregaci.

Historicky řešení jako Mobile IP poskytovala určitou úroveň multi-homing, ale často byla neefektivní, zahrnovala trojúhelníkové směrování a významnou latenci. Motivací pro ALTC v rámci 3GPP bylo vyvinout standardizovaný, síťově řízený přístup, který umožňuje plynulou mobilitu toků napříč různými přístupovými technologiemi. Zavedením ALTC ve verzi 12 cílilo 3GPP na zvýšení kontinuity služeb, zlepšení využití zdrojů napříč více rádiovými přístupy a podporu aplikací s kritickými požadavky, které vyžadují vysokou dostupnost. To byla součást širšího trendu směrem k zahušťování sítí a integraci ne-3GPP přístupů, což připravilo cestu pro konvergované 5G systémy.

Dále ALTC řeší problémy související s mezerami v pokrytí a přetížením. V oblastech se slabým buněčným signálem může alternativní Wi-Fi připojení udržet službu. Pro operátory sítí umožňuje odlehčení provozu z přetížených buněčných sítí na jiné dostupné přístupy, čímž optimalizuje celkový výkon sítě. Technologie také podporuje scénáře, kdy přímé síťové připojení není k dispozici, například v situacích veřejné bezpečnosti, tím, že umožňuje UE používat jiná blízká UE jako přenosové stanice pro dosažení sítě, čímž rozšiřuje pokrytí. ALTC je tedy základním prvkem pro spolehlivé a efektivní vícepřístupové připojení v moderních mobilních sítích.

## Klíčové vlastnosti

- Umožňuje současné vícepřístupové připojení (3GPP i ne-3GPP)
- Podporuje síťově řízenou IP flow mobility (IFOM) pro plynulé předání spojení
- Umožňuje kontinuitu služeb napříč různými typy přístupu bez přerušení session
- Poskytuje rozhodování o směrování provozu založené na politikách
- Usnadňuje objevování a využívání alternativních připojovacích cest, včetně přenosů UE-síť
- Zvyšuje spolehlivost a dostupnost pro aplikace s kritickými požadavky

## Definující specifikace

- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking

---

📖 **Anglický originál a plná specifikace:** [ALTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/altc/)
