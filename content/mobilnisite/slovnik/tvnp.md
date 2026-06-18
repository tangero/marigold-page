---
slug: "tvnp"
url: "/mobilnisite/slovnik/tvnp/"
type: "slovnik"
title: "TVNP – TV Network Protocol"
date: 2025-01-01
abbr: "TVNP"
fullName: "TV Network Protocol"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tvnp/"
summary: "TVNP je protokol definovaný v 3GPP pro poskytování televizních služeb přes mobilní sítě. Umožňuje efektivní vysílání a multicast televizního obsahu a podporuje funkce jako vyhledávání služeb a ochrana"
---

TVNP je protokol 3GPP pro poskytování televizních služeb přes mobilní sítě, který umožňuje efektivní vysílání a multicast televizního obsahu s funkcemi jako vyhledávání služeb a ochrana obsahu.

## Popis

[TV](/mobilnisite/slovnik/tv/) Network Protocol (TVNP) je standardizovaný protokol v rámci architektury 3GPP, specifikovaný v TS 22.281, navržený k usnadnění poskytování televizních služeb přes mobilní sítě. Funguje jako součást širších architektur Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a evolved Multimedia Broadcast Multicast Service (eMBMS), což umožňuje efektivní distribuci obsahu typu jeden k mnoha. TVNP definuje postupy a rozhraní nezbytné pro zřizování služeb, doručování obsahu a interakci s uživatelem, čímž zajišťuje interoperabilitu mezi síťovými prvky a uživatelským zařízením (UE). Podporuje jak vysílací (broadcast), tak skupinový (multicast) režim, což operátorům umožňuje optimalizovat síťové zdroje na základě popularity obsahu a rozložení uživatelů.

Architektonicky se TVNP integruje s prvky jádra sítě, jako je Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), který slouží jako vstupní bod pro poskytovatele obsahu, a MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)), který zajišťuje přeposílání dat. Na straně rádiového přístupu se rozhraní připojuje k eNodeB v LTE nebo k gNB v 5G NR a koordinuje přenos televizních streamů přes rozhraní vzduchu. Mezi klíčové komponenty patří mechanismy oznámení služeb, které informují uživatele o dostupných televizních kanálech a programech, a protokoly pro doručování souborů pro přenos videa a přidružených metadat. TVNP také zahrnuje bezpečnostní funkce, jako je správa klíčů pro šifrování obsahu, aby se zabránilo neoprávněnému přístupu a zajistila integrita služby.

Během provozu TVNP spravuje celý životní cyklus televizní služby, od počátečního nastavení a zahájení relace přes dynamickou adaptaci až po ukončení. Podporuje adaptivní streamování s proměnným datovým tokem, což umožňuje úpravu kvality videa na základě síťových podmínek a možností zařízení. Protokol umožňuje plynulé předávání a správu mobility, čímž zajišťuje nepřetržitý sledovací zážitek při pohybu uživatelů mezi buňkami. Standardizací těchto postupů TVNP snižuje složitost pro operátory a výrobce zařízení a podporuje konkurenceschopný ekosystém pro mobilní televizní služby. Jeho role přesahuje tradiční vysílání, neboť podporuje interaktivní funkce a integraci s jednosměrnými (unicast) službami pro hybridní televizní zážitek.

## K čemu slouží

TVNP byl vytvořen, aby reagoval na rostoucí poptávku po televizních službách na mobilních zařízeních a využil možností sítí 3GPP pro efektivní doručování obsahu. Před jeho zavedením se mobilní televizní služby často spoléhaly na proprietární řešení nebo technologie mimo 3GPP, jako je DVB-H, což vedlo k fragmentaci a omezené interoperabilitě. TVNP standardizuje doručování televizního obsahu přes sítě 3GPP a umožňuje operátorům nabízet vysílací a skupinové služby bez nutnosti samostatné infrastruktury. To snižuje náklady a zjednodušuje nasazení, zároveň zlepšuje uživatelský zážitek funkcemi jako elektronický průvodce programem a ochrana obsahu.

Motivace pro TVNP vychází z potřeby optimalizovat síťové zdroje pro oblíbené živé události, jako jsou sportovní přenosy nebo zpravodajství, kde by jednosměrné (unicast) doručování zatěžovalo kapacitu. Díky umožnění multicastu umožňuje TVNP více uživatelům přijímat stejný obsah současně, čímž šetří šířku pásma a zlepšuje škálovatelnost. Podporuje také vývoj směrem k 5G, kde jsou vysílací služby integrovány do architektury jádra sítě, a poskytuje základ pro budoucí vylepšení, jako je síťové segmentování (network slicing) pro doručování médií. TVNP řeší omezení dřívějších přístupů tím, že poskytuje komplexní, standardy založený protokol, který zajišťuje spolehlivost, bezpečnost a plynulou integraci se stávajícími systémy 3GPP.

## Klíčové vlastnosti

- Podporuje vysílací (broadcast) a skupinový (multicast) režim pro efektivní distribuci obsahu
- Integruje se s architekturami MBMS/eMBMS pro poskytování služeb
- Poskytuje mechanismy pro oznámení a vyhledávání služeb
- Zahrnuje bezpečnostní funkce pro šifrování obsahu a správu klíčů
- Umožňuje adaptivní streamování s proměnným datovým tokem pro úpravu kvality
- Podporuje správu mobility a předávání pro nepřetržité sledování

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TS 22.281** (Rel-19) — Mission Critical Video (MCVideo) Service Requirements

---

📖 **Anglický originál a plná specifikace:** [TVNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tvnp/)
