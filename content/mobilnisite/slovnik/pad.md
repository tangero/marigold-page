---
slug: "pad"
url: "/mobilnisite/slovnik/pad/"
type: "slovnik"
title: "PAD – Packet Assembler/Disassembler"
date: 2025-01-01
abbr: "PAD"
fullName: "Packet Assembler/Disassembler"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pad/"
summary: "Síťová funkce, historicky přítomná v uzlech podpory GPRS, která formátuje uživatelské datové pakety do vhodných protokolových datových jednotek pro přenos přes rádiovou síť a naopak. Zpracovává adapta"
---

PAD je síťová funkce, která formátuje uživatelské datové pakety do protokolových datových jednotek pro rádiový přenos a naopak, zajišťující adaptaci mezi síťovými protokoly a rámováním rádiového rozhraní.

## Popis

Packet Assembler/Disassembler (PAD) je funkční entita uvnitř paketové jádrové sítě, nejvýznamněji spojovaná s architekturou uzlu podpory [GPRS](/mobilnisite/slovnik/gprs/) ([SGSN](/mobilnisite/slovnik/sgsn/)/GGSN). Jejím hlavním úkolem je provádět protokolovou adaptaci a formátování datových jednotek pro uživatelská data procházející mezi externími paketovými datovými sítěmi (jako je Internet) a mobilní stanicí. PAD funguje na rozhraní síťové vrstvy a transportních mechanismů nižších vrstev specifických pro rádiovou přístupovou síť. 'Skládá' (assembles) pakety tak, že přebírá data vyšších protokolových vrstev (např. IP pakety) z externí sítě a zapouzdřuje je do specifické rámcové struktury vyžadované pro přenos přes rádiové rozhraní GPRS/UMTS, což typicky zahrnuje segmentaci do menších protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)), jako jsou [LLC](/mobilnisite/slovnik/llc/) rámce nebo [RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/) bloky.

Naopak, 'rozkládá' (disassembles) příchozí data z mobilní stanice odstraněním hlaviček specifických pro rádiové rozhraní a opětovným složením původních paketů vyšších vrstev pro směrování do externí sítě. Klíčovým technickým aspektem je její zpracování různých protokolů síťové vrstvy (např. IP, X.25), jak jsou definovány kontextem [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol). Funkce PAD zajišťuje, že datová část je správně namapována mezi formátem externího protokolu a interním protokolovým zásobníkem GPRS/UMTS. V SGSN je funkce PAD úzce spojena s vrstvou LLC (Logical Link Control), kde napomáhá segmentaci a opětovnému složení LLC PDU. V GGSN interaguje s rozhraním Gi a provádí zapouzdření/odzapouzdření pro tunelovací protokoly jako [GTP](/mobilnisite/slovnik/gtp/) (GPRS Tunneling Protocol).

Architektura zahrnuje specifické parametry PAD vyjednané během aktivace kontextu PDP, které definují charakteristiky jako datový tok, velikost okna a maximální velikost paketu. Funkce PAD není samostatným uzlem, ale logickým souborem procedur distribuovaných napříč síťovými elementy. Spravuje vyrovnávací paměti pro skládání a rozkládání, řeší potenciální změnu pořadí paketů a spolupracuje s kompresními funkcemi, pokud jsou použity. Její činnost je pro koncového uživatele transparentní, ale je klíčová pro zachování integrity dat a efektivní využití rádiového rozhraní tím, že zajišťuje balení dat do optimálně velkých jednotek pro podkladové transportní vrstvy, čímž minimalizuje režii a opakované přenosy.

## K čemu slouží

Funkce PAD byla koncipována k vyřešení základního problému propojení sítí mezi standardizovanými externími paketovými datovými sítěmi (PDN) a novým, pro rádiový přenos optimalizovaným paketovým transportním systémem GPRS. Rané systémy mobilních dat před GPRS často používaly proprietární protokoly end-to-end. Aby GPRS získalo široké přijetí, potřebovalo bezproblémově propojit s všudypřítomnými sítěmi jako Internet (používající IP) a staršími sítěmi X.25 pro podnikový přístup.

Základní výzvou byl nesoulad v charakteristikách protokolů a velikostech paketů. Rádiové sítě mají striktní omezení velikosti paketu kvůli náchylnosti kanálů k chybám a sdílenému přístupu k médiu, což favorizuje menší, snadno zvládnutelné bloky. Externí sítě však přenášejí mnohem větší pakety (např. IP MTU o velikosti 1500 bajtů). Přímý přenos velkého IP paketu přes rádio by byl vysoce neefektivní a náchylný k chybám. PAD to řeší provedením nezbytné segmentace (rozložení) pro rádiovou část a opětovného složení (složení) pro pevnou síťovou část. To umožňuje mobilním zařízením komunikovat pomocí standardních protokolů, aniž by si byla vědoma adaptací specifických pro rádio.

Historicky byly PAD běžné také v zastaralých sítích X.25 pro rozhraní s terminály orientovanými na znaky. 3GPP tento koncept adaptovala pro celulární paketové jádro. Jeho vytvoření bylo motivováno potřebou flexibilní adaptační vrstvy s povědomím o protokolu, která by mohla podporovat více typů PDP, což umožnilo, aby se GPRS od svého počátku stalo platformou pro více služeb. Abstrahovala složitosti rádiového spoje od aplikací vyšších vrstev a síťových protokolů, což je konstrukční princip, který pokračuje v pozdějších systémech prostřednictvím různých mechanismů, jako je PDCP v LTE a NR.

## Klíčové vlastnosti

- Provádí protokolovou adaptaci mezi protokoly externí PDN a interními protokoly GPRS/UMTS
- Segmentuje velké externí pakety na menší PDU rádiového rozhraní (skládání)
- Skládá rádiové PDU zpět do původních externích paketů (rozkládání)
- Podporuje více typů Packet Data Protocol (PDP) (např. IP, PPP, X.25)
- Spravuje parametry PAD vyjednané pro každý kontext PDP
- Spolupracuje s vrstvami LLC a GTP při formátování dat

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation

---

📖 **Anglický originál a plná specifikace:** [PAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/pad/)
