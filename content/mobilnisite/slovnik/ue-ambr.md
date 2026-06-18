---
slug: "ue-ambr"
url: "/mobilnisite/slovnik/ue-ambr/"
type: "slovnik"
title: "UE-AMBR – UE Aggregate Maximum Bit Rate"
date: 2025-01-01
abbr: "UE-AMBR"
fullName: "UE Aggregate Maximum Bit Rate"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ue-ambr/"
summary: "UE-AMBR je parametr QoS, který omezuje celkovou maximální přenosovou rychlost, kterou může uživatelské zařízení (UE) spotřebovat na všech svých přenosech typu Non-GBR. Vynucuje jej základnová stanice"
---

UE-AMBR je parametr QoS, který omezuje celkovou maximální přenosovou rychlost, kterou může uživatelské zařízení (UE) spotřebovat na všech svých přenosech typu Non-GBR. Toto omezení vynucuje základnová stanice pro uplink i downlink.

## Popis

UE Aggregate Maximum Bit Rate (UE-AMBR) je parametr kvality služeb (QoS) definovaný v architekturách EPS a 5GS pro řízení celkové spotřeby šířky pásma uživatelského zařízení (UE). Konkrétně se vztahuje na součet datových rychlostí všech přenosů typu Non-Guaranteed Bit Rate (Non-GBR) nebo toků QoS asociovaných s daným UE. Přenosy Non-GBR se používají pro best-effort provoz, jako je prohlížení webu nebo streamování videa, kde síť negarantuje minimální přenosovou rychlost. UE-AMBR představuje pro tento agregovaný provoz strop, čímž zajišťuje spravedlivé sdílení rádiových prostředků mezi více UE v buňce.

UE-AMBR je předplacen v profilu uživatele v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a je stažen do Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) během připojování UE. MME/AMF následně signalizuje předplacenou hodnotu UE-AMBR základnové stanici – eNodeB ([eNB](/mobilnisite/slovnik/enb/)) v LTE nebo gNodeB (gNB) v 5G NR. Vynucování UE-AMBR provádí výhradně základnová stanice v obou směrech – uplink i downlink. Základnová stanice využívá plánovací algoritmy, aby zajistila, že agregovaná datová rychlost pro přenosy Non-GBR daného UE nepřekročí limit UE-AMBR, a zároveň se snaží splnit požadavky QoS jednotlivých přenosů.

Je klíčové rozlišovat UE-AMBR od parametrů QoS na úrovni přenosu, jako je Aggregate Maximum Bit Rate ([APN-AMBR](/mobilnisite/slovnik/apn-ambr/)) a Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)). APN-AMBR omezuje provoz na přístupový bod ([APN](/mobilnisite/slovnik/apn/)) a vynucuje jej paketová brána (PGW/UPF), zatímco GBR je zaručená rychlost pro vyhrazené přenosy. UE-AMBR je naopak vynucován na rádiové úrovni. Nevztahuje se na přenosy GBR, které mají vlastní vyhrazené rezervace prostředků. Tato hierarchická kontrola QoS umožňuje operátorům efektivně spravovat kapacitu sítě: APN-AMBR řídí využití prostředků v jádře sítě na připojení PDN a UE-AMBR řídí využití rozhraní vzduchu na uživatelské zařízení.

## K čemu slouží

UE-AMBR byl zaveden ve 3GPP Release 8 s Evolved Packet System (EPS), aby řešil potřebu řízení rádiových prostředků na úrovni účastníka v sítích typu all-IP. Předchozí mechanismy QoS ve 2G/3G se často zaměřovaly na garance na úrovni přenosu nebo PDP kontextu, ale postrádaly efektivní způsob, jak omezit celkovou spotřebu rádiových prostředků jediného zařízení, zejména s nástupem tarifů s neomezenými daty a aplikací náročných na šířku pásma. Bez UE-AMBR by jediné UE s více aktivními best-effort relacemi (např. simultánní stahování a video streamy) mohlo potenciálně spotřebovat nepřiměřený podíl kapacity buňky, což by degradovalo služby pro ostatní uživatele.

Primární problém, který UE-AMBR řeší, je zajištění spravedlivosti při přidělování rádiových prostředků a prevence zahlcení na rozhraní vzduchu. Umožňuje mobilním operátorům nabízet stupňované datové tarify přiřazením různých hodnot UE-AMBR různým úrovním předplatného (např. prémiové vs. základní). Poskytuje také nástroj pro správu provozu, který zajišťuje respektování sdílené povahy rádiového média. Jeho vynucování na základnové stanici je klíčové, protože rádiový plánovač má nejpřesnější a reálný přehled o dostupnosti prostředků a podmínkách kanálu UE, což umožňuje dynamické a efektivní uplatnění tohoto limitu.

## Klíčové vlastnosti

- Omezuje agregovanou přenosovou rychlost pro všechny přenosy/toky QoS typu Non-GBR daného UE
- Vynucováno uzlem RAN (eNB/gNB) v obou směrech – uplink i downlink
- Předplaceno v HSS/UDM a poskytnuto MME/AMF a následně do RAN
- Nevztahuje se na přenosy GBR, které mají vyhrazené garance prostředků
- Funguje nezávisle na APN-AMBR, který je vynucován v bráně jádra sítě
- Klíčový parametr pro implementaci stupňovaných datových tarifů a politik spravedlivého přístupu k rádiovým prostředkům

## Související pojmy

- [APN-AMBR – Access Point Name Aggregate Maximum Bit Rate](/mobilnisite/slovnik/apn-ambr/)
- [GBR – Generic Binaural Renderer](/mobilnisite/slovnik/gbr/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)

---

📖 **Anglický originál a plná specifikace:** [UE-AMBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ue-ambr/)
