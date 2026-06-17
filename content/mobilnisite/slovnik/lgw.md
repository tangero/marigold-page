---
slug: "lgw"
url: "/mobilnisite/slovnik/lgw/"
type: "slovnik"
title: "LGW – Local Gateway"
date: 2025-01-01
abbr: "LGW"
fullName: "Local Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lgw/"
summary: "Síťová funkce, která odkládá přenos uživatelské roviny lokálně na okraji sítě, blíže k uživateli. Snižuje latenci a zatížení páteřní sítě tím, že zpracovává provoz přímo mezi rádiovou přístupovou sítí"
---

LGW je síťová funkce, která odkládá přenos uživatelské roviny lokálně na okraji sítě, aby snížila latenci a zatížení páteřní sítě tím, že zpracovává provoz přímo mezi RAN a internetem.

## Popis

Lokální brána (LGW) je funkce uživatelské roviny definovaná v architektuře 3GPP pro odkládání provozu na okraji mobilní sítě. Jejím hlavním úkolem je ukončit cestu uživatelské roviny z rádiové přístupové sítě (např. eNodeB v LTE) a poskytnout přímý lokální výstup datového provozu do internetu nebo specifických místních služeb. Architektonicky je LGW typicky umístěna společně nebo v těsné blízkosti základnové stanice (např. u multi-RAT základnové stanice nebo brány pro small cell), čímž vytváří lokální kotvící bod pro uživatelská data.

Při provozu, když je datová relace uživatele způsobilá pro lokální odkládání (např. při přístupu na veřejný internet), řídicí rovina páteřní sítě ([MME](/mobilnisite/slovnik/mme/), SGSN) vytvoří přenosový kanál, kde cesta uživatelské roviny vede mezi uživatelským zařízením (UE) a LGW, namísto tradiční centrální brány paketové datové sítě ([P-GW](/mobilnisite/slovnik/p-gw/)). LGW lokálně vykonává klíčové funkce brány: slouží jako bod přidělování IP adres pro UE (s využitím místního fondu IP adres), provádí směrování a přeposílání paketů, vynucuje místní politiky kvality služeb (QoS) a zpracovává generování účtovacích dat pro odkládaný provoz. Udržuje spojení s centrální páteřní sítí pro řídicí signalizaci (např. přes rozhraní SGi), aby přijímala aktualizace politik a hlásila účtovací informace.

LGW je klíčovou součástí architektur, jako je odkládání vybraného IP provozu (SIPTO) v místní síti. Umožňuje aplikace s nízkou latencí a efektivní zpracování objemného provozu internetu s nejlepším úsilím. Odkládáním tohoto provozu snižuje zatížení mobilní přenosové sítě a centrálních prvků páteřní sítě (P-GW), což vede k úsporám nákladů a lepší škálovatelnosti. LGW spolupracuje s entitami řídicí roviny, aby zajistila plynulou mobilitu; například pokud se uživatel přesune mimo oblast pokrytí LGW, může být relace plynule převedena (nebo 'přemístěna') na centrální P-GW.

## K čemu slouží

LGW byla vytvořena jako reakce na explozivní růst mobilního datového provozu, zejména náročného na šířku pásma, ale tolerantního k latenci (jako je streamování videa, prohlížení webu). Tento provoz způsoboval zahlcení a problémy se škálovatelností v mobilní přenosové síti a centralizovaných bránách páteřní sítě (GGSN/[P-GW](/mobilnisite/slovnik/p-gw/)). Směrování všech dat přes centrální bod se stávalo neefektivní a nákladné.

Její vývoj byl motivován potřebou optimalizace síťové architektury a vznikem případů použití s nízkou latencí. Odkládáním provozu lokálně mohli operátoři snížit náklady na přenos, zlepšit výkon sítě pro místní služby a položit základy pro edge computing. Řešila problém neefektivního 'trombónování', kdy místní provoz musel putovat do vzdálené centrální brány a zpět. LGW jako součást paradigmat SIPTO a později edge computingu poskytla standardizovaný způsob decentralizace uživatelské roviny, přibližujíc obsah a aplikace blíže koncovému uživateli, aby umožnila služby jako rozšířená realita, průmyslový IoT a hry v reálném čase.

## Klíčové vlastnosti

- Lokální ukončení uživatelské roviny a IP kotvící bod blízko RAN
- Umožňuje odkládání vybraného IP provozu (SIPTO) v místní síti
- Přiděluje místní IP adresy zařízením UE z vyhrazeného fondu
- Lokálně provádí směrování a přeposílání paketů a vynucování QoS
- Generuje místní záznamy o účtování dat pro odkládaný provoz
- Podporuje mechanismy kontinuity relace pro události mobility

## Definující specifikace

- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System

---

📖 **Anglický originál a plná specifikace:** [LGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/lgw/)
