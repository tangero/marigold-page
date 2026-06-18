---
slug: "rfcs"
url: "/mobilnisite/slovnik/rfcs/"
type: "slovnik"
title: "RFCS – Resource Facing Communication Service"
date: 2025-01-01
abbr: "RFCS"
fullName: "Resource Facing Communication Service"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rfcs/"
summary: "Resource Facing Communication Service (RFCS) je síťová interní služba, která poskytuje konektivitu a přenosové schopnosti ostatním síťovým funkcím nebo servisním vrstvám. Abstrahuje podkladové síťové"
---

RFCS je síťová interní služba, která poskytuje konektivitu a přenosové schopnosti tím, že abstrahuje podkladové prostředky do spotřebovatelné služby pro ostatní síťové funkce nebo servisní vrstvy.

## Popis

Resource Facing Communication Service (RFCS) je základní koncept v rámci architektury a frameworku správy 3GPP, definovaný zejména ve specifikacích pro správu sítí (např. 28.805) a výkon kodeků (26.102, 26.202). Představuje typ komunikační služby, která není přímo spotřebovávána koncovým uživatelem nebo zákazníkem, ale jinými síťovými funkcemi nebo komponentami vyšších servisních vrstev v doméně operátora. RFCS poskytuje standardizované schopnosti konektivity, přenosu nebo zpracování využívající fyzické a logické prostředky sítě. Příklady zahrnují službu vyhrazeného přenosového kanálu, službu multicastové distribuce nebo službu zpracování médií jako je transkódování.

Architektonicky se RFCS nachází mezi surovými síťovými prostředky (jako routery, přepínače, rádiové přenosové kanály a výpočetní platformy) a Customer Facing Communication Services (CFCS). CFCS je to, k čemu se koncový uživatel přihlašuje, například služba streamování videa ve vysokém rozlišení. Tato CFCS je realizována složením jedné nebo více RFCS. Například CFCS pro streamování videa může využívat RFCS pro přenos s garantovanou vysokou propustností, další RFCS pro ukládání obsahu na okraji sítě a třetí pro správu digitálních práv. Tento vrstvený servisní model umožňuje opakované použití a flexibilní skládání. RFCS je definována servisní smlouvou, která specifikuje její funkční chování, výkonnostní metriky (latence, šířka pásma), spolehlivost a rozhraní pro správu.

Jak to funguje, zahrnuje vystavení služby, její zjišťování a orchestraci. V servisně orientované architektuře ([SBA](/mobilnisite/slovnik/sba/)) 5G mohou producenti služeb síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) nabízet RFCS. Spotřebitelé služeb (jiné NF nebo systémy správy) mohou tyto RFCS zjišťovat a vyvolávat prostřednictvím standardizovaných [API](/mobilnisite/slovnik/api/), často používajících [HTTP](/mobilnisite/slovnik/http/)/2 nebo jiné protokoly. Implementace RFCS pak mapuje požadavek na službu na konkrétní konfigurace síťových prostředků. Například požadavek na 'RFCS pro přenos s ultra-spolehlivou nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/))' může spustit zřízení vyhrazené [PDU](/mobilnisite/slovnik/pdu/) Session s příslušnými QoS toky, výběr síťového řezu a prioritizaci v RAN a jádru sítě. Specifikace správy jako 28.805 používají RFCS v kontextu výkonnostního managementu, definujíce, jak se měří a zajišťuje kvalita těchto interních služeb pro podporu kvality koncové zákaznické služby.

## K čemu slouží

Koncept RFCS byl vyvinut pro řešení rostoucí složitosti správy a orchestrace moderních telekomunikačních sítí, zejména se zavedením 5G, síťových řezů a cloud-nativních principů. Tradiční správa sítě fungovala na bázi jednotlivých prvků nebo technologií, což ztěžovalo zajištění kvality služby od konce ke konci a automatizaci poskytování služeb. Byla potřeba standardizovaná abstraktní vrstva, která skryje heterogenitu podkladových prostředků (multi-dodavatel, multi-technologie, cloud vs. fyzické).

RFCS to řeší tím, že poskytuje prostředky orientovaný servisní model, který umožňuje agilní skládání služeb a správu jejich životního cyklu. Umožňuje operátorům definovat znovupoužitelné, katalogizované stavební bloky (RFCS), které lze dynamicky řetězit pro vytváření zákaznických služeb. Tento přístup podporuje automatizační frameworky jako [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/) MANO a správu síťových řezů 3GPP. Tím, že existuje jasná smlouva pro interní služby, lze sladit správu poruch a zajištění výkonu s dopadem na službu, čímž se zlepšuje provozní efektivita. Jeho specifikace v dokumentech souvisejících s kodeky (26.xxx) jej také spojuje se zajištěním, že služby zpracování médií (RFCS) splňují požadované úrovně výkonu pro zkušenost koncového uživatele.

## Klíčové vlastnosti

- Abstrahuje podkladové síťové prostředky (přenos, výpočetní výkon, úložiště) do spotřebovatelné služby
- Používána interně síťovými funkcemi a systémy správy, nikoli přímo koncovými uživateli
- Umožňuje skládání Customer Facing Communication Services (CFCS)
- Definována servisní smlouvou s funkčními, výkonnostními a správními atributy
- Klíčový prvek pro automatizaci, orchestraci a servisně orientovanou architekturu v 5G
- Usnadňuje správu a zajištění kvality služby od konce ke konci

## Definující specifikace

- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TS 28.805** (Rel-16) — Management of Communication Services in 5G

---

📖 **Anglický originál a plná specifikace:** [RFCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfcs/)
