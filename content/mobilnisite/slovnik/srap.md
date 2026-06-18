---
slug: "srap"
url: "/mobilnisite/slovnik/srap/"
type: "slovnik"
title: "SRAP – Sidelink Relay Adaptation Protocol"
date: 2025-01-01
abbr: "SRAP"
fullName: "Sidelink Relay Adaptation Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srap/"
summary: "Protokolová vrstva v 5G NR sidelink komunikaci, která umožňuje přenosovou (relay) funkcionalitu mezi terminály (UE). Adaptuje data pro přenos přes sidelink rozhraní přenosového uzlu a podporuje služby"
---

SRAP je protokolová vrstva 3GPP pro 5G NR sidelink, která adaptuje data pro přenos přes přenosový uzel (relay) mezi uživatelskými terminály za účelem rozšíření pokrytí pro služby ProSe, veřejnou bezpečnost a V2X aplikace.

## Popis

Sidelink Relay Adaptation Protocol (SRAP) je klíčová protokolová vrstva v zásobníku protokolů 5G New Radio (NR) sidelink, specificky definovaná pro přenosové (relay) operace mezi uživatelskými terminály (UE). Funguje jako podvrstva vrstvy Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) pro uživatelskou rovinu sidelink přenosového uzlu. SRAP je zodpovědný za adaptaci datových paketů pro přenos přes sidelink rozhraní přenosového uzlu, což je přímé spojení zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)). Provádí funkce jako přidávání a odstraňování SRAP hlaviček, které obsahují nezbytné informace pro směrování a identifikaci v přenosovém řetězci, a může zajišťovat segmentaci a zpětné složení datových jednotek tak, aby odpovídaly charakteristikám sidelink radiového beareru.

Architektonicky se SRAP nachází mezi službami vyšších vrstev (např. IP pakety nebo ne-IP data) a nižšími sidelink radiovými protokoly (jako [RLC](/mobilnisite/slovnik/rlc/) a [MAC](/mobilnisite/slovnik/mac/)). Je využíván ve scénářích, kdy vzdálený terminál (remote UE) komunikuje se sítí prostřednictvím přenosového terminálu (relay UE), který funguje jako zprostředkovatel. Přenosový terminál má přímé spojení s gNB (rozhraní Uu) a také navazuje sidelink spojení (rozhraní PC5) se vzdáleným terminálem. SRAP funguje na obou stranách – na vzdáleném i přenosovém terminálu – aby zajistil správné formátování datových paketů pro sidelink část komunikační cesty. Spolupracuje s dalšími sidelink protokoly, jako je Sidelink Radio Link Control (SL-RLC) a Sidelink Medium Access Control (SL-MAC), a zajišťuje tak spolehlivý přenos dat.

Činnost protokolu zahrnuje zpracování jednotek servisních dat ([SDU](/mobilnisite/slovnik/sdu/)) z vyšších vrstev entitou SRAP. Ta přidá SRAP hlavičku obsahující pole jako cílové Layer-2 ID a případně zdrojové Layer-2 ID pro adresování v rámci sidelink. Tato hlavička umožňuje přenosovému terminálu identifikovat cílový vzdálený terminál nebo přeposlat data směrem k síti. Na přijímací straně entita SRAP hlavičku odstraní a doručí SDU příslušné entitě vyšší vrstvy. SRAP je navržen tak, aby byl transparentní pro core network, což znamená, že síť se ke vzdálenému terminálu chová, jako by byl připojen přímo, a zjednodušuje tak správu sítě. Jeho role je klíčová pro efektivní komunikaci založenou na přenosových uzlech, což je základní schopnost pro služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)), sítě veřejné bezpečnosti a scénáře Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)), kde může být přímé síťové pokrytí omezené.

## K čemu slouží

SRAP byl zaveden za účelem standardizace a vylepšení přenosové (relay) funkcionality v 5G NR sidelink komunikaci, čímž reaguje na potřebu spolehlivého přenosu zařízení-zařízení bez nutnosti trvalého síťového pokrytí. Před 3GPP Release 17 sidelink komunikace v LTE a raném 5G primárně podporovala přímou komunikaci, ale měla omezené standardizované přenosové mechanismy, zejména pro data uživatelské roviny. To představovalo výzvu pro aplikace veřejné bezpečnosti, kde záchranné složky mohou operovat v oblastech s poškozenou nebo neexistující síťovou infrastrukturou, a pro [V2X](/mobilnisite/slovnik/v2x/) scénáře, kde vozidla potřebují rozšířit dosah komunikace. SRAP poskytuje protokolový rámec pro efektivní adaptaci dat pro přenos přes přenosový uzel a řeší tak problém plynulého rozšíření konektivity.

Vznik SRAP byl motivován vývojem služeb založených na blízkosti (ProSe) a rostoucí poptávkou po pokročilých V2X a průmyslových IoT aplikacích. V Release 16 bylo 5G NR sidelink vylepšeno pro V2X, ale podpora přenosových uzlů nebyla v zásobníku protokolů uživatelské roviny plně rozpracována. SRAP tuto mezeru zaplňuje definováním vyhrazené adaptační vrstvy, která řeší složitosti směrování přes přenosový uzel na rozhraní PC5. Řeší omezení předchozích ad-hoc nebo nestandardizovaných přístupů k přenosu tím, že zajišťuje interoperabilitu, efektivní využití hlaviček a integraci se stávající architekturou NR sidelink. To umožňuje terminálům (UE) dynamicky fungovat jako přenosové uzly, rozšiřovat síťové pokrytí a zlepšovat spolehlivost služeb v náročných prostředích.

## Klíčové vlastnosti

- Adaptuje data uživatelské roviny pro přenos přes sidelink přenosový uzel (relay)
- Přidává a odstraňuje SRAP hlavičky pro směrování a identifikaci v přenosovém řetězci
- Funguje jako podvrstva PDCP v zásobníku sidelink protokolů
- Podporuje komunikaci mezi vzdáleným terminálem (remote UE) a přenosovým terminálem (relay UE) přes rozhraní PC5
- Umožňuje rozšíření síťového pokrytí pro veřejnou bezpečnost a V2X
- Funguje transparentně vůči core networku, což zjednodušuje správu

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.351** (Rel-19) — Sidelink Relay Adaptation Protocol (SRAP)
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [SRAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/srap/)
