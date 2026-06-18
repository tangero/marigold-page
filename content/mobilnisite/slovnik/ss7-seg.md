---
slug: "ss7-seg"
url: "/mobilnisite/slovnik/ss7-seg/"
type: "slovnik"
title: "SS7-SEG – SS7 Security Gateway"
date: 2025-01-01
abbr: "SS7-SEG"
fullName: "SS7 Security Gateway"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ss7-seg/"
summary: "SS7 Security Gateway (SS7-SEG) je síťová funkce, která zabezpečuje propojení mezi sítěmi založenými na SS7 a IP sítěmi nebo mezi různými doménami operátorů. Poskytuje funkce firewallu, filtrování a de"
---

SS7-SEG je síťová funkce, která zabezpečuje propojení mezi sítěmi SS7 a IP sítěmi tím, že poskytuje funkce firewallu, filtrování a detekce narušení pro ochranu starší signalizační infrastruktury SS7.

## Popis

[SS7](/mobilnisite/slovnik/ss7/) Security Gateway (SS7-SEG) je bezpečnostní funkce definovaná 3GPP pro ochranu signalizační sítě číslo 7 (SS7) před hrozbami zavlečenými prostřednictvím IP propojení. S vývojem jádrových sítí byly tradiční SS7 spoje založené na [TDM](/mobilnisite/slovnik/tdm/) stále častěji nahrazovány nebo doplňovány IP přenosem využívajícím protokoly jako SIGTRAN (např. [M3UA](/mobilnisite/slovnik/m3ua/), [SCTP](/mobilnisite/slovnik/sctp/)). Toto IP propojení, ačkoli je nákladově efektivní a flexibilní, prolomilo tradiční 'uzavřený síťový' bezpečnostní model SS7 a vystavilo jej širšímu spektru útoků z IP sítí. SS7-SEG funguje jako demarkační bod a uzel pro vynucování bezpečnosti.

Z architektonického hlediska je SS7-SEG nasazován na hranici signalizační sítě SS7 operátora. Nachází se mezi vnitřní sítí SS7 (s jejími signalizačními přenosovými body – [STP](/mobilnisite/slovnik/stp/), [MSC](/mobilnisite/slovnik/msc/), [HLR](/mobilnisite/slovnik/hlr/)) a externími IP signalizačními spoji nebo sítěmi jiných operátorů. Obvykle funguje v párech pro redundanci. Gateway provádí hloubkovou kontrolu paketů (DPI) na příchozích a odchozích signalizačních zprávách. Zkoumá parametry uvnitř vrstev protokolu SS7 ([MTP](/mobilnisite/slovnik/mtp/), SCCP, TCAP, MAP), aby ověřila jejich správnost a legitimitu podle nastavených bezpečnostních politik.

Jak funguje, zahrnuje několik bezpečnostních mechanismů. Působí jako signalizační firewall, který filtruje zprávy na základě bílých/černých listin zdrojových/cílových point kódů, globálních titulů (GT) a konkrétních typů zpráv. Může provádět omezení přenosové rychlosti (rate limiting), aby zabránila signalizačním záplavám a přetížením. SS7-SEG také poskytuje skrytí topologie tím, že maskuje vnitřní strukturu sítě před externími subjekty, často funguje jako signalizační proxy. Může ověřovat posloupnost zpráv pro detekci anomálií a zaznamenávat veškerý signalizační provoz pro audit a forenzní analýzu. Implementací těchto kontrol má SS7-SEG za cíl zabránit útokům, jako je sledování polohy, odposlech hovorů, podvody a odmítnutí služby (DoS) zaměřené na HLR nebo jiné kritické uzly SS7.

## K čemu slouží

SS7-SEG byl vytvořen jako reakce na rostoucí povědomí o závažných bezpečnostních zranitelnostech v globální síti SS7. Původní návrh SS7 předpokládal uzavřenou, důvěryhodnou síť fyzicky zabezpečených spojů mezi omezeným počtem známých operátorů. Nicméně rozšíření IP propojení, outsourcing sítí a globální roaming zavedly nedůvěryhodné cesty do signalizačního jádra. Účelem SS7-SEG je znovu zavést silnou bezpečnostní hranici, která řeší omezení původního modelu důvěry.

Řeší kritické problémy, jako je neoprávněný přístup k datům účastníka (např. dotazování HLR na polohu účastníka), odposlech hovorů a SMS, zneužití identity účastníka a narušení sítě prostřednictvím signalizačních bouří. Motivací pro jeho standardizaci ve 3GPP Release 8 byla rostoucí závislost na IP pro úsporu nákladů a odpovídající nárůst zdokumentovaných případů zneužití SS7. Poskytuje operátorům standardizovanou metodu pro zabezpečení jejich starší investice do infrastruktury SS7 během přechodu na plně IP sítě, což zajišťuje bezpečný provoz nezbytných hlasových a SMS služeb během období vývoje sítě.

## Klíčové vlastnosti

- Filtrování signalizačních zpráv a funkce firewallu na základě point kódů, globálních titulů (GT) a typu zprávy
- Skrytí topologie pro utajení vnitřní struktury sítě před externími partnery
- Omezení přenosové rychlosti (rate limiting) a řízení přetížení pro prevenci útoků typu odmítnutí služby (DoS) založených na signalizaci
- Hloubková kontrola paketů (DPI) vrstev protokolu SS7 (MTP, SCCP, TCAP, MAP)
- Zaznamenávání (logging), auditování a detekce narušení pro signalizační provoz
- Zabezpečené propojení mezi sítěmi SS7 přes IP přenos (SIGTRAN)

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SS7-SEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss7-seg/)
