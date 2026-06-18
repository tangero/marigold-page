---
slug: "mcm"
url: "/mobilnisite/slovnik/mcm/"
type: "slovnik"
title: "MCM – Multi-Connection Mode"
date: 2025-01-01
abbr: "MCM"
fullName: "Multi-Connection Mode"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mcm/"
summary: "Provozní režim definovaný 3GPP, který umožňuje uživatelskému zařízení (UE) udržovat více současných připojení k různým přístupovým sítím, jako jsou 3GPP a ne-3GPP sítě (např. Wi-Fi). Umožňuje bezprobl"
---

MCM (Multi-Connection Mode) je provozní režim definovaný 3GPP, ve kterém uživatelské zařízení (UE) udržuje více současných připojení k různým přístupovým sítím, což umožňuje bezproblémovou mobilitu a agregaci provozu napříč heterogenními technologiemi.

## Popis

Multi-Connection Mode (MCM) je síťová architektura a provozní režim specifikovaný 3GPP, primárně v kontextu vývoje jádra sítě směrem k bezproblémové integraci více přístupových technologií. Definován v TS 23.402 umožňuje uživatelskému zařízení (UE) navázat a udržovat souběžná připojení k různým přístupovým sítím, jako jsou 3GPP sítě (např. LTE, 5G NR) a ne-3GPP sítě (např. Wi-Fi, pevný broadband). MCM umožňuje síti tato připojení spravovat kolektivně a poskytovat funkce jako směrování provozu, agregaci a podporu mobility bez přerušení služby. Je klíčovým prvkem pro nasazení heterogenních sítí (HetNet) a vylepšený uživatelský zážitek.

Architektonicky MCM zahrnuje funkce jádra sítě, jako je Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) pro výběr přístupu na základě politik, Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC pro ukotvení připojení uživatelské roviny, a Non-3GPP Interworking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) pro bezpečnou integraci ne-3GPP přístupů. Režim funguje tak, že umožňuje UE registrovat se u více přístupových bodů současně, přičemž jádro sítě koordinuje správu relací a tok dat přes tyto cesty. Klíčové komponenty zahrnují schopnosti duálního IP zásobníku, autentizační mechanismy pro ne-3GPP sítě a rozhraní jako S2a/b/c v EPC nebo N3 v 5GC.

V provozu MCM podporuje scénáře, kdy může UE například používat LTE pro hlasové služby a Wi-Fi pro stahování dat vysokou rychlostí současně, přičemž síť dynamicky směruje provoz na základě politik, kvality spoje nebo uživatelských preferencí. Jádro sítě udržuje jednotný kontext pro UE, což umožňuje bezproblémové předávání a kontinuitu relace při pohybu mezi přístupy. Role MCM sahá až k umožnění pokročilých služeb, jako je agregace LTE-WLAN ([LWA](/mobilnisite/slovnik/lwa/)) nebo multi-access edge computing ([MEC](/mobilnisite/slovnik/mec/)) v 5G, kde je nízká latence a vysoká šířka pásma dosaženo využitím více připojení. Je základem pro naplnění vize 3GPP o konvergentním přístupu v architekturách vyvinutého paketového jádra a systému 5G.

## K čemu slouží

MCM byl zaveden, aby řešil rostoucí heterogenitu přístupových sítí a potřebu bezproblémové integrace mezi 3GPP a ne-3GPP technologiemi, jako je Wi-Fi. Před jeho standardizací obvykle UE pracovala v režimech s jedním připojením a přepínala mezi sítěmi s přerušeními, což omezovalo potenciál pro agregaci provozu a zážitek 'vždy nejlépe připojen'. MCM poskytuje standardizovaný rámec pro souběžný provoz s více přístupy a řeší problémy jako neefektivní využití zdrojů a špatný výkon mobility ve smíšených prostředích.

Historicky, s nárůstem poptávky po mobilních datech v důsledku rozšíření chytrých telefonů, operátoři hledali způsoby, jak přesměrovat provoz na Wi-Fi a další doplňkové přístupy, ale postrádali ucelené možnosti správy. MCM, definovaný od 3GPP Release 12 dále, byl motivován snahou vylepšit architektury jádra sítě (např. EPC a později 5GC) pro lepší agnosticismus vůči přístupu. Umožňuje operátorům využít více rádiových rozhraní pro zlepšení kapacity, pokrytí a spokojenosti uživatelů, zejména v hustě obydlených městských oblastech nebo vnitřních prostorech.

Vytvoření MCM také podporuje vývoj směrem k 5G a síťovému řezání, kde je flexibilní výběr přístupu klíčový pro různé požadavky služeb. Tím, že umožňuje současná připojení, usnadňuje inovace jako multi-path TCP a edge computing, čímž řeší omezení předchozích přístupů s jednou cestou. To se stává stále důležitějším s internetem věcí (IoT) a ultra-spolehlivou komunikací s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), kde mohou redundantní připojení zvýšit spolehlivost.

## Klíčové vlastnosti

- Umožňuje současná připojení k 3GPP a ne-3GPP přístupovým sítím
- Podporuje směrování a agregaci provozu přes více spojů
- Poskytuje bezproblémovou mobilitu a kontinuitu relace mezi heterogenními přístupy
- Integruje se s funkcemi jádra sítě, jako jsou ANDSF a N3IWF, pro správu politik
- Usnadňuje pokročilé funkce, jako je agregace LTE-WLAN a multi-access edge computing
- Zvyšuje kapacitu, pokrytí a uživatelský zážitek prostřednictvím optimalizovaného výběru přístupu

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)

## Definující specifikace

- **TS 23.161** (Rel-19) — Network-based IP Flow Mobility (NBIFOM)
- **TS 23.861** (Rel-13) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN

---

📖 **Anglický originál a plná specifikace:** [MCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcm/)
