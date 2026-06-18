---
slug: "hsdn"
url: "/mobilnisite/slovnik/hsdn/"
type: "slovnik"
title: "HSDN – High Speed Dedicated Network"
date: 2025-01-01
abbr: "HSDN"
fullName: "High Speed Dedicated Network"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hsdn/"
summary: "Koncept nasazení sítě v 5G NR pro vyhrazené, vysoce výkonné privátní nebo neveřejné sítě. Poskytuje zvýšenou propustnost, spolehlivost a nízkou latenci pro specifické podnikové nebo vertikální případy"
---

HSDN je koncept nasazení sítě 5G NR pro vyhrazené, vysoce výkonné privátní sítě, který poskytuje zvýšenou propustnost, spolehlivost a nízkou latenci pro specifické podnikové nebo průmyslové případy užití.

## Popis

High Speed Dedicated Network (HSDN) je koncept nasazení v rámci architektury 5G New Radio (NR), který označuje vyhrazené sítě budované za účelem poskytování vysokorychlostního, spolehlivého a nízkolatenčního připojení pro specifické podnikové nebo vertikální průmyslové aplikace. Architektura zahrnuje vyhrazenou rádiovou přístupovou síť (RAN) a často i vyhrazenou jádrovou síť (např. 5GC), fungující buď jako plně samostatná neveřejná síť ([NPN](/mobilnisite/slovnik/npn/)), nebo jako virtuální řez (slice) uvnitř veřejné sítě. Mezi klíčové komponenty patří gNB (5G základnové stanice) nasazené lokálně nebo ve vyhrazené oblasti, uživatelská zařízení (UE) přizpůsobená danému případu užití a jádrová síť, která může být hostována lokálně. RAN pracuje v licencovaném, nelicencovaném nebo sdíleném spektru (jako je [CBRS](/mobilnisite/slovnik/cbrs/)) s konfiguracemi optimalizovanými pro pokrytí, kapacitu a izolaci od rušení.

HSDN funguje tak, že vyčleňuje vyhrazené síťové zdroje výhradně pro použití konkrétní organizací nebo službou. gNB jsou konfigurovány s parametry upřednostňujícími vysokou propustnost (např. nosné s širokou šířkou pásma, pokročilé [MIMO](/mobilnisite/slovnik/mimo/)) a funkce pro ultra-spolehlivou nízkolatenční komunikaci ([URLLC](/mobilnisite/slovnik/urllc/)), jako jsou zkrácené přenosové časové intervaly ([TTI](/mobilnisite/slovnik/tti/)) a redundantní přenosové cesty. UE přistupují k síti pomocí standardních procedur 5G NR, ale řízení přístupu je omezeno na autorizované uživatele, často s využitím mechanismů uzavřené přístupové skupiny ([CAG](/mobilnisite/slovnik/cag/)) nebo identifikátoru sítě ([NID](/mobilnisite/slovnik/nid/)) definovaných pro neveřejné sítě. Jádrová síť, pokud je vyhrazená, hostuje aplikační funkce ([AF](/mobilnisite/slovnik/af/)) a funkce uživatelské roviny (UPF) lokálně, aby se minimalizovala latence a citlivá data zůstala v místě.

Její úlohou je poskytnout přizpůsobené řešení konektivity, které veřejné sítě nemohou zaručit kvůli soutěžení o sdílené zdroje. Je dokumentována v RAN specifikacích (např. TS 38.300, TS 36.304), které pokrývají požadavky na UE a procedury v takovém prostředí. HSDN podporuje kritické komunikace pro továrny (Průmysl 4.0), chytré sítě, přístavy a areály, kde jsou klíčové výkon, bezpečnost a kontrola. Koexistuje s nasazeními veřejných sítí, ale je logicky nebo fyzicky oddělena, aby splňovala přísné smlouvy o úrovni služeb (SLA).

## K čemu slouží

HSDN byl zaveden, aby splňoval náročné požadavky vertikálních odvětví a podniků na konektivitu, které nelze uspokojit konvenčními veřejnými mobilními širokopásmovými sítěmi. Tato odvětví, jako je výroba, energetika a logistika, potřebovala sítě se zaručenou vysokou rychlostí, ultra nízkou latencí, vysokou spolehlivostí a silným soukromím dat. Veřejné sítě, navržené pro široké pokrytí spotřebitelů a sdílenou kapacitu, často postrádají deterministický výkon a míru kontroly vyžadovanou pro průmyslovou automatizaci, dálkové ovládání a citlivé operace.

Vznik HSDN ve verzi 15 (Release 15) byl motivován konstrukčními principy 5G podporujícími rozšířené mobilní širokopásmo (eMBB), ultra-spolehlivou nízkolatenční komunikaci (URLLC) a komunikaci s masivním počtem strojových zařízení (mMTC). Řeší omezení předchozích podnikových řešení, jako je Wi-Fi (omezená mobilita, rušení) nebo rané privátní sítě 4G (omezené možnosti přizpůsobení výkonu). HSDN využívá technologické pokroky 5G NR – jako je flexibilní numerologie, síťové řezy (network slicing) a edge computing – k vytváření vyhrazených sítí, které jsou stejně výkonné a řiditelné jako tradiční průmyslové sítě s kabelovým připojením, ale s bezdrátovou flexibilitou. Umožňuje digitální transformaci v odvětvích, kde je konektivita klíčovým provozním nástrojem.

## Klíčové vlastnosti

- Vyhrazené nasazení RAN 5G NR pro exkluzivní použití
- Podpora provozu v licencovaných, nelicencovaných a sdílených kmitočtových pásmech
- Zvýšená propustnost a kapacita prostřednictvím agregace nosných a massive MIMO
- Schopnosti ultra-spolehlivé nízkolatenční komunikace (URLLC)
- Uzavřená přístupová skupina (CAG) a identifikátor sítě (NID) pro řízení přístupu
- Možnost samostatné neveřejné sítě (SNPN) nebo neveřejné sítě integrované s veřejnou sítí

## Související pojmy

- [NPN – Non-Public Network](/mobilnisite/slovnik/npn/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [CAG – Closed Access Group](/mobilnisite/slovnik/cag/)

## Definující specifikace

- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [HSDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsdn/)
