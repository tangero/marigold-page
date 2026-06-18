---
slug: "mbms-gw"
url: "/mobilnisite/slovnik/mbms-gw/"
type: "slovnik"
title: "MBMS-GW – MBMS Gateway"
date: 2025-01-01
abbr: "MBMS-GW"
fullName: "MBMS Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mbms-gw/"
summary: "Funkce brány jádrové sítě pro služby MBMS. Slouží jako distribuční bod IP multicastu, přeposílá uživatelská data MBMS z BM-SC k příslušným základnovým stanicím (eNBs/Node Bs) a zpracovává signalizaci"
---

MBMS-GW je brána jádrové sítě, která distribuuje IP multicastová data pro služby MBMS z BM-SC k základnovým stanicím a zpracovává související signalizaci řízení relace směrem k rádiové přístupové síti.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Gateway (MBMS-GW) je logická entita jádrové sítě zavedená jako součást architektury evolved Multimedia Broadcast Multicast Service (eMBMS), primárně pro LTE a později 5G systémy. Jejím hlavním úkolem je sloužit jako distribuční a řídicí bod pro provoz MBMS mezi Broadcast Multicast-Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a rádiovou přístupovou sítí (RAN), která zahrnuje eNodeBs (eNBs) v LTE a gNBs v NR. Funkčně se nachází na uživatelské i řídicí rovině pro procedury specifické pro MBMS.

Na uživatelské rovině MBMS-GW funguje jako IP multicastový směrovač. Přijímá IP pakety obsahující obsah MBMS (např. videoproudy nebo soubory) z BM-SC přes rozhraní SG-mb (založené na Diameter/[GTP](/mobilnisite/slovnik/gtp/)). MBMS-GW pak využívá IP multicastové protokoly k efektivní distribuci těchto paketů ke všem základnovým stanicím (eNBs), které jsou součástí cílové oblasti služby MBMS. Tato IP multicastová distribuce eliminuje potřebu, aby BM-SC vytvářela individuální unicastové tunely ke každému [eNB](/mobilnisite/slovnik/enb/), což výrazně snižuje zatížení transportní části jádrové sítě. MBMS-GW provádí duplikaci paketů pouze tam, kde je to v topologii sítě nezbytné, a tím optimalizuje využití přenosové kapacity.

Na řídicí rovině je MBMS-GW klíčovým uzlem v signalizační cestě řízení relace MBMS. Přijímá příkazy k zahájení/zastavení/aktualizaci relace z BM-SC přes referenční body SG-mb/SG-i. MBMS-GW pak přeposílá tyto zprávy správy relací příslušným uzlům RAN pomocí rozhraní M3 (založeného na [SCTP](/mobilnisite/slovnik/sctp/)) směrem k Multi-cell/multicast Coordination Entity ([MCE](/mobilnisite/slovnik/mce/)) v LTE nebo přímo k RAN v jiných konfiguracích. Je odpovědná za přidělení jedinečné IP multicastové adresy pro každou relaci přenosového kanálu MBMS a za informování RAN o této adrese spolu s dalšími parametry relace, jako je QoS. MBMS-GW také zajišťuje zahájení a ukončení GTP tunelů (pomocí uživatelského rovinnového rozhraní M1) pro distribuci dat k RAN.

Architektonicky může být MBMS-GW implementována jako samostatný síťový prvek nebo může být kolokována s jinými funkcemi jádrové sítě, jako je [SGW](/mobilnisite/slovnik/sgw/) nebo [PGW](/mobilnisite/slovnik/pgw/). V jádrové síti 5G (5GC) pro multicastové/broadcastové služby NR je podobná funkce brány definována v rámci Multicast/Broadcast User Plane Function (MB-UPF). Role MBMS-GW je klíčová pro oddělení servisní logiky (v BM-SC) od transportu a správy rádiových prostředků, což poskytuje škálovatelný a efektivní mechanismus pro doručování broadcastového a multicastového obsahu v rozsáhlé buněčné síti.

## K čemu slouží

MBMS-GW byla zavedena k řešení problémů škálovatelnosti a efektivity v původní architektuře MBMS pro UMTS, kde byla distribuce multicastového provozu k RAN méně definovaná. Její vytvoření bylo motivováno potřebou specializované, optimalizované brány pro zpracování IP multicastové distribuce a správy relací pro eMBMS v LTE. Bez takové brány by BM-SC musela spravovat individuální spojení k potenciálně tisícům základnových stanic, což by vytvářelo významnou signalizační a procesní zátěž a činilo transport jádrové sítě neefektivním.

MBMS-GW řeší problém efektivního point-to-multipoint přeposílání dat v jádrové síti. Využitím IP multicastu zajišťuje, že jediný paket z BM-SC je replikován síťovými směrovači pouze v rozbočovacích bodech nezbytných k dosažení všech cílových eNBs, namísto aby byl odesílán jako více unicastových kopií přes celou síťovou cestu. To dramaticky snižuje potřebnou přenosovou kapacitu v transportní síti operátora (backhaul). Navíc centralizací signalizace řízení relace směrem k RAN poskytuje MBMS-GW jediný kontaktní bod pro BM-SC, což zjednodušuje celkovou správu relací a umožňuje dynamičtější kontrolu nad oblastmi služby a aktivací přenosových kanálů.

## Klíčové vlastnosti

- Slouží jako distribuční bod IP multicastu pro uživatelský provoz MBMS
- Ukončuje rozhraní M1 (GTP-U) pro doručování uživatelských dat k RAN
- Zpracovává signalizaci řízení relace MBMS (zahájení/zastavení/aktualizace) přes rozhraní M3
- Přiděluje a spravuje IP multicastové adresy pro relace přenosových kanálů MBMS
- Může být implementována jako samostatný uzel nebo integrována s jinými funkcemi CN
- Podporuje efektivní přeposílání dat ke všem základnovým stanicím v oblasti služby MBMS

## Související pojmy

- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MCE – Multi-cell/multicast Coordination Entity](/mobilnisite/slovnik/mce/)
- [MB-UPF – Multicast/Broadcast User Plane Function](/mobilnisite/slovnik/mb-upf/)

## Definující specifikace

- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 29.468** (Rel-19) — MB2 Reference Point Protocol Definition
- **TS 36.868** (Rel-12) — Study on Group Communication for E-UTRA

---

📖 **Anglický originál a plná specifikace:** [MBMS-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbms-gw/)
