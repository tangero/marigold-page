---
slug: "tsp"
url: "/mobilnisite/slovnik/tsp/"
type: "slovnik"
title: "TSP – Transport Service Provider"
date: 2026-01-01
abbr: "TSP"
fullName: "Transport Service Provider"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tsp/"
summary: "Logická entita v architektuře 3GPP poskytující služby transportní konektivity mezi síťovými funkcemi. Abstrahuje detaily podkladové transportní sítě, což umožňuje flexibilní poskytování služeb a podpo"
---

TSP (Transport Service Provider) je logická entita poskytující služby transportní konektivity mezi síťovými funkcemi a abstrahující detaily podkladové transportní sítě.

## Popis

Transport Service Provider (TSP) je funkční koncept v rámci službami řízené architektury ([SBA](/mobilnisite/slovnik/sba/)) 3GPP, definovaný zejména pro síť 5G Core (5GC). Působí jako logický zprostředkovatel, který nabízí služby transportní konektivity mezi různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), nebo mezi funkcemi uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). TSP není jediným fyzickým uzlem, ale schopností, kterou lze implementovat uvnitř síťových funkcí nebo jako vyhrazenou službu. Jeho primární role spočívá v řízení aspektů transportní vrstvy komunikace, včetně výběru vhodných transportních protokolů, zpracování kvality služeb (QoS) pro transportní síť a potenciálně bezpečnostních aspektů, jako je šifrování pro rozhraní [N2](/mobilnisite/slovnik/n2/) (řídicí rovina) a N3 (uživatelská rovina).

Architektonicky TSP komunikuje s ostatními síťovými funkcemi prostřednictvím službami řízených rozhraní (např. Nnssf, Nnef) nebo referenčních bodů. Využívá transportní profily, což jsou sady parametrů definujících požadované transportní charakteristiky (např. latence, šířka pásma, spolehlivost) pro daný tok služebních dat nebo instanci síťového řezu. TSP konzultuje s Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), aby určil vhodné transportní zdroje odpovídající smlouvě o úrovni služeb (SLA) řezu. Následně komunikuje s podkladovou transportní sítí (např. řízenou Transport Network Controllerem), aby zajistil potřebnou konektivitu, často využívaje technologie jako Segment Routing nebo MPLS.

Při provozu, když síťová funkce vyžaduje transportní služby, vyvolá schopnosti TSP prostřednictvím standardizovaných API. TSP vyhodnotí požadavek na základě dostupných zásad síťových řezů a předplatitele, vybere transportní cestu a odpovídajícím způsobem nakonfiguruje prvky transportní sítě. Tato abstrakce umožňuje, aby funkce jádrové sítě byly agnostické vůči konkrétním transportním technologiím (např. IP, Ethernet, optické), což usnadňuje interoperabilitu mezi různými dodavateli a bezproblémový vývoj transportní vrstvy. TSP je klíčovým prvkem pro end-to-end síťové řezání, neboť zajišťuje, že transportní segment splňuje specifické požadavky na výkon a izolaci každého řezu.

## K čemu slouží

TSP byl zaveden, aby řešil rostoucí složitost správy transportních zdrojů v oddělené, cloud-nativní síti 5G Core. V architekturách před 5G byla transportní konektivita často těsně integrována s uzly jádrové sítě, což ztěžovalo dynamické přidělování zdrojů pro různé služby, jako je enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency Communications (URLLC) a massive Machine-Type Communications (mMTC). Tato nepružnost bránila efektivnímu síťovému řezání, kde každý řez vyžaduje odlišné transportní charakteristiky.

Koncept TSP to řeší poskytováním standardizované abstraktní vrstvy pro transportní služby. Odděluje servisní logiku jádrové sítě od podkladové transportní infrastruktury, což operátorům umožňuje spravovat a optimalizovat transportní síť nezávisle. To umožňuje flexibilní nasazení služeb, automatizované zřizování transportních zdrojů pro každý řez a lepší využití síťových aktiv. Historicky, bez TSP, vyžadovalo dosažení end-to-end QoS a izolace řezů napříč transportní sítí proprietární integrace, což omezovalo škálovatelnost a inovace.

## Klíčové vlastnosti

- Abstrahuje detaily transportní sítě od funkcí jádrové sítě
- Podporuje dynamické přidělování transportních zdrojů pro síťové řezy
- Umožňuje vynucování transportní QoS na základě SLA řezů
- Poskytuje standardizovaná rozhraní pro požadavky na transportní služby
- Usnadňuje interoperabilitu mezi doménami jádra a transportu
- Umožňuje integraci s různými podkladovými transportními technologiemi (IP, MPLS, Ethernet)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios

---

📖 **Anglický originál a plná specifikace:** [TSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsp/)
