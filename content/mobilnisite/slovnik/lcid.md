---
slug: "lcid"
url: "/mobilnisite/slovnik/lcid/"
type: "slovnik"
title: "LCID – Logical Channel Identifier"
date: 2025-01-01
abbr: "LCID"
fullName: "Logical Channel Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcid/"
summary: "LCID je jedinečný identifikátor používaný v protokolech 3GPP k rozlišení různých logických kanálů v rámci rádiového držitele. Umožňuje multiplexování a demultiplexování datových proudů, čímž zajišťuje"
---

LCID je jedinečný identifikátor používaný v protokolech 3GPP k rozlišení logických kanálů pro multiplexování a směrování datových proudů mezi uživatelským zařízením a sítí.

## Popis

Identifikátor logického kanálu (LCID) je základní identifikátor v rádiových přístupových sítích 3GPP, používaný v protokolech, jako je vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), k rozlišení více logických kanálů, které sdílejí společný transportní kanál. Každý logický kanál odpovídá specifickému typu dat nebo řídicích informací, jako jsou data uživatelské roviny, signalizace řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) nebo bloky systémových informací ([SIB](/mobilnisite/slovnik/sib/)). LCID je obsažen v podhlavičce MAC protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)), což příjemci umožňuje správně demultiplexovat příchozí data a směrovat je k příslušné entitě vyšší vrstvy. V praxi jsou hodnoty LCID předdefinovány v technických specifikacích, s rozsahy vyhrazenými pro různé účely – například hodnoty 0–10 mohou být rezervovány pro řídicí kanály, zatímco vyšší hodnoty jsou používány pro datové rádiové držitele.

Z architektonického hlediska LCID funguje v rámci protokolového zásobníku MAC, který se nachází nad fyzickou vrstvou a pod vrstvou řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)). Při přenosu dat přidá vrstva MAC k jednotce služebních dat MAC ([SDU](/mobilnisite/slovnik/sdu/)) podhlavičku obsahující LCID, čímž vytvoří jednotku protokolových dat MAC (PDU). Tato PDU je následně odeslána přes transportní kanál, například downlinkový sdílený kanál ([DL-SCH](/mobilnisite/slovnik/dl-sch/)) nebo uplinkový sdílený kanál ([UL-SCH](/mobilnisite/slovnik/ul-sch/)). Na přijímací straně vrstva MAC extrahuje LCID z podhlavičky, aby určila, ke kterému logickému kanálu data patří, a odpovídajícím způsobem je předá. Tento mechanismus podporuje multiplexování více logických kanálů na jeden transportní kanál, optimalizuje využití rádiových zdrojů a umožňuje současné zpracování různých typů provozu.

Role LCID je klíčová pro efektivní správu rádiových zdrojů a vynucování kvality služeb (QoS). Identifikací logických kanálů umožňuje síti aplikovat specifické strategie plánování, zacházení s prioritami a mechanismy opravy chyb přizpůsobené požadavkům každého kanálu. Například vysoce prioritním signalizačním kanálům mohou být přiděleny zdroje před kanály pro datový provoz typu best-effort. V 5G NR je LCID rozšířen pro podporu nových logických kanálů pro funkce jako sidelinková komunikace a služby s ultra-spolehlivou nízkou latencí, přičemž specifikace jsou podrobně popsány v dokumentech jako 26.512 pro aspekty kodeků a 33.303 pro bezpečnostní procedury. Jeho konzistentní použití napříč releasy zajišťuje zpětnou kompatibilitu a hladkou vzájemnou spolupráci mezi systémy LTE a NR.

## K čemu slouží

LCID byl vytvořen k řešení potřeby efektivního multiplexování a identifikace více datových proudů v rámci jednoho rádiového držitele, což byla výzva, která vznikla s růstem různorodých mobilních služeb. Před jeho standardizací měly rané celulární systémy omezené mechanismy k rozlišení různých typů provozu, což vedlo k neefektivní alokaci zdrojů a obtížím při upřednostňování kritické signalizace před uživatelskými daty. Zavedení LCID v Release 12 poskytlo standardizovaný způsob označování logických kanálů, což umožnilo podrobnější řízení a optimalizaci výkonu rádiového rozhraní.

Historicky, jak se 3GPP vyvíjelo od HSPA přes LTE až k 5G, nárůst objemů dat a různorodosti služeb – od hlasových hovorů po data ze senzorů IoT – si vyžádal flexibilní systém identifikátorů. LCID tento problém řeší tím, že umožňuje vrstvě MAC současně zpracovávat více logických kanálů, čímž podporuje funkce jako agregace nosných, duální konektivita a síťové slicing. Řeší omezení předchozích přístupů, které se často spoléhaly na statická mapování nebo dodatečnou režii, integrací lehké identifikace přímo do podhlavičky MAC.

Pokračující význam LCID spočívá v jeho základní roli pro pokročilé funkce RAN. Umožňuje dynamické plánování, zlepšuje správu QoS a usnadňuje zavedení nových logických kanálů pro vznikající případy užití, jako je komunikace vozidlo se vším (V2X) nebo masová komunikace mezi stroji (mMTC). Tím, že poskytuje jednoduché, ale účinné identifikační schéma, přispívá LCID ke škálovatelnosti a efektivitě moderních mobilních sítí.

## Klíčové vlastnosti

- Jednoznačně identifikuje logické kanály v jednotkách PDU vrstvy MAC pro účely multiplexování
- Podporuje předdefinované rozsahy hodnot pro řídicí a datové kanály
- Umožňuje efektivní demultiplexování a směrování provozu na straně přijímače
- Usnadňuje zacházení s prioritami a diferenciaci QoS na základě logického kanálu
- Integruje se s algoritmy plánování pro dynamickou alokaci rádiových zdrojů
- Je rozšiřitelný pro nové logické kanály pro pokročilé služby, jako je sidelink nebo URLLC

## Související pojmy

- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [LCID na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcid/)
