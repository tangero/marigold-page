---
slug: "nsei"
url: "/mobilnisite/slovnik/nsei/"
type: "slovnik"
title: "NSEI – Network Service Entity Identifier"
date: 2025-01-01
abbr: "NSEI"
fullName: "Network Service Entity Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nsei/"
summary: "Jedinečný identifikátor síťové služební entity (NSE) v síti GPRS, konkrétně používaný na rozhraní Gb mezi BSS a SGSN. Je klíčový pro správu a směrování datového provozu v paketově orientované jádrové"
---

NSEI je jedinečný identifikátor síťové služební entity (Network Service Entity) v síti GPRS, používaný na rozhraní Gb, který umožňuje SGSN rozlišovat různé entity BSS pro směrování datového provozu.

## Popis

Identifikátor síťové služební entity (NSEI) je základním identifikátorem v architektuře sítí [GPRS](/mobilnisite/slovnik/gprs/) a raných 3G sítí, definovaným ve specifikacích rozhraní Gb. Jednoznačně identifikuje síťovou služební entitu, což je logická entita reprezentující [BSS](/mobilnisite/slovnik/bss/) (Base Station Subsystem) nebo skupinu BSS z pohledu [SGSN](/mobilnisite/slovnik/sgsn/) (Serving GPRS Support Node). NSEI se používá v protokolech vrstvy síťové služby ([NS](/mobilnisite/slovnik/ns/)), které jsou odpovědné za přenos paketů protokolu [BSSGP](/mobilnisite/slovnik/bssgp/) (Base Station System GPRS Protocol) přes rozhraní Gb založené na frame relay. Tato vrstva spravuje virtuální spojení, známá jako [NS-VC](/mobilnisite/slovnik/ns-vc/) (Network Service Virtual Connections), mezi BSS a SGSN. NSEI spolu s [BVCI](/mobilnisite/slovnik/bvci/) (BSSGP Virtual Connection Identifier) tvoří dvouúrovňový adresovací systém, který umožňuje SGSN směrovat pakety na správnou buňku ve správném BSS. SGSN udržuje mapování NSEI na adresy podkladové transportní sítě (např. Frame Relay [DLCI](/mobilnisite/slovnik/dlci/)) a používá tuto informaci k navazování a správě NS-VC. Tento mechanismus je nezbytný pro SGSN ke správě více BSS, zpracování událostí mobility, jako je převýběr buňky, a zajištění spolehlivého přenosu dat pro paketově přepínané služby. Role NSEI je omezena na architekturu rozhraní Gb a jde o klíčovou součást éry mobilních paketových dat před zavedením rozhraní S1.

## K čemu slouží

NSEI bylo vytvořeno k řešení potřeby škálovatelného a efektivního adresovacího mechanismu pro subsystémy základnových stanic (BSS) v architektuře sítě GPRS zavedené v 2,5G. Před GPRS měly okruhově přepínané hlasové sítě odlišné řídicí mechanismy. Paketově orientovaná povaha GPRS vyžadovala nové rozhraní (Gb) a protokolový zásobník pro zpracování datového provozu. Hlavním problémem bylo umožnit jedinému SGSN komunikovat a spravovat potenciálně velký počet BSS a jejich buněk. NSEI poskytuje logický identifikátor, který abstrahuje fyzické transportní detaily a umožňuje SGSN identifikovat zdrojovou nebo cílovou entitu BSS pro jakýkoli datový paket nebo řídicí zprávu. Tato abstrakce zjednodušuje správu sítě, směrování a procedury mobility. Vyřešilo to omezení spočívající v nutnosti spravovat přímá fyzická spojení ke každému BSS zavedením logické vrstvy (vrstva síťové služby), která může multiplexovat provoz přes sdílené virtuální okruhy, přičemž NSEI je klíčem k demultiplexování a směrování provozu na straně SGSN.

## Klíčové vlastnosti

- Jednoznačně identifikuje síťovou služební entitu (BSS nebo skupinu BSS) na rozhraní Gb.
- Spolu s BVCI tvoří první část dvouúrovňového adresovacího systému pro přesnou identifikaci buňky.
- Používá se SGSN k mapování logických entit BSS na podkladové virtuální okruhy Frame Relay (NS-VC).
- Nezbytný pro směrování datových jednotek protokolu BSSGP mezi BSS a SGSN.
- Podporuje funkce správy sítě, jako je správa kontextu BSS a procedury resetu.
- Základní prvek GPRS Tunnelling Protocol (GTP) a směrování paketových dat v sítích 2,5G/3G.

## Související pojmy

- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [BVCI – BSS GPRS Protocol Virtual Connection Identifier](/mobilnisite/slovnik/bvci/)
- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)
- [NS-VC – Network Service Virtual Connection](/mobilnisite/slovnik/ns-vc/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [NSEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsei/)
