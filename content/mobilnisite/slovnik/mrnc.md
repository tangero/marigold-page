---
slug: "mrnc"
url: "/mobilnisite/slovnik/mrnc/"
type: "slovnik"
title: "MRNC – MBMS Master Radio Network Controller"
date: 2025-01-01
abbr: "MRNC"
fullName: "MBMS Master Radio Network Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mrnc/"
summary: "Určený RNC v UTRAN, který koordinuje řízení relací služby Multimedia Broadcast Multicast Service (MBMS) pro konkrétní servisní oblast. Slouží jako centrální bod pro správu přenosových kanálů MBMS a sy"
---

MRNC je určený řadič rádiové sítě (Radio Network Controller) v UTRAN, který koordinuje řízení relací a správu přenosových kanálů pro MBMS v dané servisní oblasti a synchronizuje vysílání s dalšími RNC za účelem umožnění makrodiverzitního kombinování.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Master Radio Network Controller (MRNC) je funkční role definovaná v architektuře UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) pro MBMS. V typickém nasazení MBMS pokrývajícím rozsáhlou oblast se na vysílání stejného obsahu podílí více [RNC](/mobilnisite/slovnik/rnc/) (a jim podřízených Node B). Pro koordinaci tohoto vysílání a umožnění funkcí, jako je selektivní kombinování pro zlepšení příjmu, je jeden RNC určen jako hlavní (Master) pro danou konkrétní službu MBMS a oblast. MRNC je kotvícím bodem pro přenosový kanál Iu od jádra sítě (přes [SGSN](/mobilnisite/slovnik/sgsn/)) pro data MBMS. Přijímá datový proud MBMS z jádra a je zodpovědný za jeho distribuci přes rozhraní Iur k ostatním RNC zapojeným do vysílání, které se označují jako podřízené RNC (Slave RNCs, SRNCs).

Klíčovou technickou funkcí MRNC je zpracování signalizace pro řízení relací MBMS. Ukončuje řídicí rovinu MBMS od jádra sítě (rozhraní Iu) a generuje potřebné zprávy Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)) pro stranu UTRAN. MRNC spravuje aktivaci a deaktivaci rádiových prostředků pro přenosový kanál MBMS v rámci své koordinované sady RNC. Hraje také zásadní roli v synchronizaci vysílání. MRNC zajišťuje, aby datové rámce MBMS byly vysílány ze všech zapojených Node B (pod MRNC i všemi [SRNC](/mobilnisite/slovnik/srnc/)) časově synchronizovaným způsobem. Tato synchronizace umožňuje koncovým zařízením (UE) na hranici buňky, která přijímají signál z více buněk, provádět makrodiverzitní kombinování (také nazývané selektivní kombinování), což výrazně zlepšuje spolehlivost příjmu a pokrytí vysílání.

Role MRNC je dynamická a specifická pro službu. RNC může být MRNC pro jednu servisní oblast MBMS a podřízeným RNC pro jinou. Určení, který RNC funguje jako MRNC, je založeno na provozní konfiguraci a potenciálně na topologii servisní oblasti. MRNC komunikuje s jádrem sítě přes rozhraní Iu a s ostatními RNC přes rozhraní Iur. Jeho zodpovědnosti jsou podrobně popsány ve specifikacích UTRAN, zejména v těch, které se zabývají architekturou MBMS (TS 25.346), signalizací na rozhraní Iur (TS 25.423) a celkovými funkcemi UTRAN (TS 25.401).

## K čemu slouží

Koncept MRNC byl zaveden, aby vyřešil problém koordinace, který je vlastní vysílání v celulární síti určené primárně pro individuální přenos (unicast). Ve standardním unicast provozu [UTRAN](/mobilnisite/slovnik/utran/) má každé UE svůj vyhrazený obsluhující [RNC](/mobilnisite/slovnik/rnc/) (Serving RNC, SRNC). Pro vysílací službu musí být jediný datový proud doručován shodně z mnoha buněk. Bez koordinátoru by každý RNC fungoval nezávisle, což by vedlo k nesynchronizovanému vysílání, které UE nemůže kombinovat, a výsledkem by byl špatný výkon na hranicích buněk a neefektivní využití rádiových prostředků.

MRNC poskytuje tuto nezbytnou koordinační vrstvu. Jeho zavedení bylo motivováno potřebou efektivního doručování MBMS se zisky z makrodiverzity. Centralizací řízení relací a distribuce dat pro servisní oblast MRNC zajišťuje synchronizovaný čas vysílání napříč více RNC. To umožňuje UE používat techniky kombinování v přijímači, které jsou klíčové pro dosažení přijatelného pokrytí a kvality vysílacích služeb bez nadměrně vysokého vysílacího výkonu. Architektura MRNC umožňuje znovupoužití existujících rozhraní Iur mezi RNC pro přeposílání dat MBMS, čímž vytváří v přístupové síti logický distribuční strom typu point-to-multipoint, který odpovídá vysílací povaze služby.

## Klíčové vlastnosti

- Slouží jako koordinační bod UTRAN a bod ukončení přenosového kanálu Iu pro konkrétní servisní oblast MBMS
- Distribuuje uživatelskou rovinu dat MBMS k podřízeným RNC (SRNCs) přes rozhraní Iur
- Ukončuje signalizaci pro řízení relací MBMS (RANAP) od jádra sítě (SGSN)
- Řídí aktivaci/deaktivaci rádiových prostředků pro přenosový kanál MBMS napříč zapojenými RNC
- Poskytuje synchronizační data pro vysílání za účelem umožnění makrodiverzitního kombinování (Selective Combining) na straně UE
- Role je dynamicky přiřazována pro každou službu MBMS a servisní oblast

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [SRNC – Serving Radio Network Controller](/mobilnisite/slovnik/srnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.446** (Rel-19) — MBMS Synchronisation Protocol (SYNC)

---

📖 **Anglický originál a plná specifikace:** [MRNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrnc/)
