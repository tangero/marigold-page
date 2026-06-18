---
slug: "tos"
url: "/mobilnisite/slovnik/tos/"
type: "slovnik"
title: "TOS – Type of Service"
date: 2025-01-01
abbr: "TOS"
fullName: "Type of Service"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tos/"
summary: "TOS je pole v hlavičce paketu IPv4, které slouží k označení požadovaného zacházení s paketem z hlediska kvality služby (QoS), jako je priorita, zpoždění, propustnost a spolehlivost. Je předchůdcem mod"
---

TOS je pole v hlavičce paketu IPv4, které slouží k označení požadovaného zacházení s paketem z hlediska kvality služby, jako je jeho priorita, zpoždění, propustnost nebo spolehlivost.

## Popis

Ve specifikacích 3GPP označuje Type of Service (TOS) 8bitové pole v hlavičce paketu IPv4 původně definované v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 791. Jeho účelem je poskytnout routerům a síťovým prvkům informaci o požadované kvalitě služby pro daný paket. Pole TOS se dělí na dvě hlavní části: bity precedence (3 bity) a bity TOS (4 bity), přičemž poslední bit byl historicky nevyužitý. Bity precedence udávají prioritu paketu (v rozsahu od běžné po řídicí pro síť). Bity TOS umožňují odesílateli požadovat konkrétní typ služby nastavením příznaků pro minimalizaci zpoždění, maximalizaci propustnosti, maximalizaci spolehlivosti nebo minimalizaci finančních nákladů.

V architektuře paketové sítě 3GPP, jako je jádrová síť [GPRS](/mobilnisite/slovnik/gprs/) nebo Evolved Packet Core (EPC), je uživatelská přenosová data přenášena přes IP. Pole TOS (a jeho vývojová forma, DiffServ Code Point – [DSCP](/mobilnisite/slovnik/dscp/)) hraje klíčovou roli při vynucování QoS. Při vytváření kontextu Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) nebo přenašeče EPS jsou vyjednávány parametry QoS, jako je třída provozu, Allocation/Retention Priority ([ARP](/mobilnisite/slovnik/arp/)) a QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)). U provozu mezi uživatelským zařízením (UE) a paketovou datovou sítí ([PDN](/mobilnisite/slovnik/pdn/)) může Gateway GPRS Support Node (GGSN) nebo Packet Data Network Gateway (P-GW) mapovat tyto specifické parametry QoS 3GPP na pole TOS/DSCP vrstvy IP ve vnějších IP hlavičkách (např. v tunelech GTP nebo na rozhraní Gi/SGi).

Toto mapování umožňuje přenosové IP síti mezi jádrovými uzly (např. mezi SGSN a GGSN nebo uvnitř evolved packet core) poskytovat diferencované přepravní zacházení bez nutnosti rozumět specifickým přenašečům 3GPP. Směrovače v přenosové síti mohou zkoumat hodnotu TOS/DSCP a zařazovat pakety do příslušných front pro přeposílání, aplikovat prioritní plánování nebo podle toho řídit zahlcení. Zatímco původní sémantika pole TOS je převážně historická, koncept se vyvinul v architekturu Differentiated Services (DiffServ), kde jsou stejné bity hlavičky reinterpretovány jako 6bitový DSCP. Systémy 3GPP využívají toto označení na vrstvě IP jako nástroj k realizaci end-to-end QoS slibované službou přenašeče, což zajišťuje, že provoz v reálném čase, jako je VoIP, dostává zacházení s nižší latencí než provoz stahování na pozadí.

## K čemu slouží

Pole TOS bylo vytvořeno, aby řešilo nedostatek vestavěné diferenciace kvality služby v raném internetu, kde se se všemi IP pakety zacházelo jako s 'best-effort'. To bylo nedostatečné pro nově vznikající aplikace se specifickými požadavky, jako je interaktivní hlas (citlivý na zpoždění) nebo hromadný přenos dat (citlivý na propustnost). Pole TOS poskytlo jednoduchý signalizační mechanismus na úrovni paketu k vyjádření těchto potřeb, což umožnilo routerům implementovat základní prioritní fronty a rozhodování o směrování.

V kontextu přijetí IP pro paketové jádro 3GPP poskytlo pole TOS (a později DSCP) zásadní spojení mezi specifickým QoS modelem pro mobilní sítě (postaveným na přenašečích se zaručenými bitovými rychlostmi, ARP atd.) a QoS schopnostmi podkladové IP přenosové infrastruktury. Řešilo problém, jak přenést komplexní QoS profil přenašeče 3GPP přes směrovače, které jsou agnostické vůči protokolům 3GPP. Mapováním hodnot QCI nebo ARP na konkrétní označení TOS/DSCP v bráně mohla mobilní síť využít standardní mechanismy QoS IP v přenosových sítích backhaul a jádra. To bylo klíčové pro nákladově efektivní škálování, protože se tak vyhnulo potřebě routerů s podporou 3GPP všude v přenosové cestě. Vývoj od původní sémantiky TOS k DiffServ poskytl škálovatelnější a flexibilnější rámec, na kterém jsou závislé sítě 3GPP od GPRS (Rel-4) dále pro škálovatelné poskytování QoS.

## Klíčové vlastnosti

- 8bitové pole v hlavičce IPv4 pro signalizaci QoS
- Obsahuje podpole Precedence (priorita) a TOS (typ služby)
- Základ pro moderní DiffServ Code Point (DSCP)
- Používá se v GGSN/P-GW k označování IP paketů na základě QoS přenašeče 3GPP
- Umožňuje diferenciaci QoS v IP přenosových sítích mezi jádrovými uzly
- Podporuje mapování na optimalizace zpoždění, propustnosti, spolehlivosti a nákladů

## Související pojmy

- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [ARP – Allocation and Retention Priority](/mobilnisite/slovnik/arp/)
- [DSCP – Differentiated Services Code Point](/mobilnisite/slovnik/dscp/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems

---

📖 **Anglický originál a plná specifikace:** [TOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tos/)
