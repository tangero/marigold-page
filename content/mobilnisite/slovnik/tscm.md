---
slug: "tscm"
url: "/mobilnisite/slovnik/tscm/"
type: "slovnik"
title: "TSCM – Transparent Single-connection mode"
date: 2025-01-01
abbr: "TSCM"
fullName: "Transparent Single-connection mode"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tscm/"
summary: "Režim definovaný v 3GPP pro přístup non-3GPP k EPC, ve kterém si UE udržuje jediné IP připojení přes důvěryhodnou přístupovou síť non-3GPP. Umožňuje bezproblémovou mobilitu IP toků a kontinuitu služeb"
---

TSCM je režim definovaný v 3GPP pro důvěryhodný přístup non-3GPP k EPC, ve kterém si UE udržuje jediné IP připojení přes jediný bod připojení.

## Popis

Transparentní režim s jediným připojením (TSCM) je specifický operační režim definovaný v rámci architektury [SAE](/mobilnisite/slovnik/sae/) (System Architecture Evolution) 3GPP pro integraci přístupu non-3GPP, jak je specifikováno v TS 23.402. Aplikuje se, když se uživatelské zařízení (UE) připojuje k architektuře EPC (Evolved Packet Core) přes důvěryhodnou přístupovou síť non-3GPP, jako je důvěryhodná [WLAN](/mobilnisite/slovnik/wlan/). V tomto režimu UE naváže a udržuje jediné IP připojení (jediný bod připojení) k EPC přes přístup non-3GPP. Toto připojení je ukotveno v bráně [PGW](/mobilnisite/slovnik/pgw/) (Packet Data Network Gateway) v EPC. Klíčovou architektonickou komponentou umožňující TSCM je brána [TNGF](/mobilnisite/slovnik/tngf/) (Trusted Non-3GPP Access Gateway) (nebo ePDG v nedůvěryhodných scénářích, ale pro TSCM se konkrétně jedná o důvěryhodný přístup), která slouží jako koncový bod v přístupové síti a komunikuje se serverem [AAA](/mobilnisite/slovnik/aaa/) 3GPP pro autentizaci a s PGW pro uživatelskou rovinu přes rozhraní S2a založené na PMIPv6 nebo [GTP](/mobilnisite/slovnik/gtp/).

Z procedurálního hlediska, když se UE připojí přes důvěryhodnou přístupovou síť non-3GPP s volbou TSCM, provede přístupovou autentizaci a autorizaci s EPC 3GPP. Po úspěšné autentizaci TNGF naváže tunel PMIPv6 nebo GTP s PGW, čímž vytvoří pro UE jediné IP připojení. Veškerý IP provoz UE je směrován tímto jediným tunelem. UE je přidělena IP adresa z poolu PGW a tato adresa zůstává stabilní, dokud je připojení udržováno. Režim je označován jako 'transparentní', protože přístupová síť non-3GPP neprovádí žádné přidělování IP adres nebo překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)) pro provoz UE směrem k EPC; IP adresa UE je plně viditelná pro PGW.

Hlavní úlohou TSCM v síti je poskytnout zjednodušený a efektivní model pro integraci důvěryhodných přístupů non-3GPP. Podporuje mobilitu IP toků ([IFOM](/mobilnisite/slovnik/ifom/)) a kontinuitu služeb, jak je definováno 3GPP, což umožňuje přesouvat IP toky mezi přístupy 3GPP a non-3GPP bez přerušení aplikační relace. Protože má UE jediné IP připojení ukotvené v PGW, mohou být události mobility (jako přidání cesty přístupu 3GPP) spravovány sítí (PGW) pomocí dual-stack Mobile IPv6 (DSMIPv6) nebo samotným UE, pokud podporuje více přístupů. TSCM stojí v protikladu k režimu s více připojeními (Multiple-connection mode), kde může mít UE více současných nezávislých připojení k EPC. Model s jediným připojením v TSCM snižuje signalizační složitost a je vhodný pro scénáře, kde UE vyžaduje jednoduchý, stabilní bod IP připojení přes alternativní přístupové technologie.

## K čemu slouží

TSCM bylo zavedeno, aby řešilo rostoucí potřebu bezproblémové integrace přístupových technologií non-3GPP, jako je Wi-Fi, do mobilní paketové jádrové sítě 3GPP. Před jeho standardizací byl přístup non-3GPP často považován za zcela samostatnou síť, což vedlo k nespojitosti služeb, složitým roamingovým scénářům a neschopnosti využít řídicí mechanismy politiky a účtování v jádrové síti mobilního operátora. Motivací bylo vytvořit jednotnou jádrovou síť (EPC), která by mohla poskytovat konzistentní služby bez ohledu na podkladovou technologii rádiového přístupu.

Konkrétní problém, který TSCM řeší, je poskytnutí standardizované, efektivní metody pro připojení UE k EPC přes *důvěryhodnou* přístupovou síť non-3GPP s využitím jediného, trvalého IP připojení. Tento model zjednodušuje síťovou architekturu a chování UE ve srovnání s podporou více současných připojení. Umožňuje operátorům přesměrovávat datový provoz na Wi-Fi sítě při zachování kontroly jádrové sítě nad autentizací, vynucováním politik (přes PCRF) a účtováním. Navíc, ukotvením připojení v PGW, je TSCM základním prvkem umožňujícím mobilitu IP toků definovanou 3GPP, což operátorům umožňuje dynamicky směrovat specifické datové toky mezi přístupy 3GPP a non-3GPP na základě síťových podmínek, politik nebo preferencí uživatele, a to vše při zachování kontinuity relace pro koncového uživatele.

## Klíčové vlastnosti

- Jediné IP připojení ukotvené v PGW pro důvěryhodný přístup non-3GPP
- Podpora rozhraní S2a s využitím protokolu PMIPv6 nebo GTPv2
- Transparentní správa IP adres bez NAT v důvěryhodné přístupové cestě
- Podpora mobility IP toků (IFOM) a kontinuity služeb dle 3GPP
- Integrovaná autentizace a autorizace prostřednictvím infrastruktury AAA 3GPP
- Řízení politiky a účtování prostřednictvím interakce s PCRF přes rozhraní Gxa

## Definující specifikace

- **TS 23.161** (Rel-19) — Network-based IP Flow Mobility (NBIFOM)
- **TS 23.861** (Rel-13) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN

---

📖 **Anglický originál a plná specifikace:** [TSCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/tscm/)
