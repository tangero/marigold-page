---
slug: "uhdtv"
url: "/mobilnisite/slovnik/uhdtv/"
type: "slovnik"
title: "UHDTV – Ultra High-Definition TeleVision"
date: 2025-01-01
abbr: "UHDTV"
fullName: "Ultra High-Definition TeleVision"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uhdtv/"
summary: "Ultra High-Definition TeleVision (UHDTV) je konkrétní služba 3GPP pro vysílání a multicastování UHD videoobsahu do mobilních zařízení. Definuje kompletní systém pro efektivní doručování lineární telev"
---

UHDTV je služba 3GPP pro efektivní vysílání a multicast ultra vysokorozlišujícího lineárního televizního signálu do mobilních zařízení s využitím technologií jako eMBMS a 5G Broadcast.

## Popis

Ultra High-Definition TeleVision (UHDTV) je specializovaná vysílací/multicastová služba v rámci architektury 3GPP navržená pro lineární doručování televizního obsahu v ultra vysokém rozlišení ([UHD](/mobilnisite/slovnik/uhd/)) do mobilních a přenosných zařízení. Na rozdíl od unicastového UHD streamování využívá UHDTV point-to-multipoint přenosové technologie, především evolved Multimedia Broadcast Multicast Service (eMBMS) v 4G LTE a jeho nástupce 5G Broadcast (založený na 5G NR). Systémová architektura pro UHDTV zahrnuje Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je vstupní bod pro poskytovatele obsahu. BM-SC zajišťuje oznámení služby, zabezpečení (správu klíčů) a přeposílá IP multicastový provoz do core sítě.

Core síť, konkrétně [MBMS](/mobilnisite/slovnik/mbms/) Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) v LTE nebo funkce 5G Broadcast/Multicast Service v 5GC, spravuje distribuci tohoto provozu do příslušných základnových stanic ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) přes IP multicast bearer. Klíčovou oblastí je [MBSFN](/mobilnisite/slovnik/mbsfn/) area, kde všechny základnové stanice v určené vysílací oblasti synchronizují své přenosy, aby vysílaly identické signály současně. To umožňuje uživatelským zařízením (UE) kombinovat signály z více buněk, což výrazně zlepšuje spolehlivost příjmu a spektrální účinnost. Rozhraní rádiového přístupu využívá vyhrazené fyzické kanály (např. [PMCH](/mobilnisite/slovnik/pmch/) v LTE) pro přenos multicastového provozu. UE používá pro příjem obsahu vysílací bearer vyhrazený pro broadcast, aniž by musela navazovat jednotlivé unicastové relace, což činí službu vysoce škálovatelnou pro neomezený počet diváků v pokryté oblasti.

Technická role UHDTV spočívá v určení, jak jsou obecné UHD videoformáty a kodeky zabaleny, transportovány a doručovány přes tyto vysílací kanály. Specifikace 26.948 podrobně popisuje mediální kodek a transportní formáty pro UHDTV přes eMBMS. To zahrnuje použití [HEVC](/mobilnisite/slovnik/hevc/) pro video kompresi, MPEG-H Audio nebo Dolby AC-4 pro prostorový zvuk a MPEG-2 Transport Stream (TS) nebo RTP/MPEG-TS pro paketizaci. Systém také definuje mechanismy pro objevování služeb, elektronický průvodce programem (ESG) a sledování kvality specifické pro vysílací prostředí. To umožňuje mobilním operátorům nabízet živé televizní služby, včetně významných sportovních událostí nebo zpráv v UHD, aniž by zahlcovali své unicastové sítě.

## K čemu slouží

UHDTV byla standardizována v 3GPP Release 13 spolu s širším rámcem UHD, aby řešila konkrétní výzvu efektivního doručování lineárního, živého UHD televizního obsahu masivnímu publiku. Unicastové doručování živých UHD událostí tisícům či milionům současných diváků by rychle zahltilo kapacitu buněk kvůli vysokému datovému toku každého streamu. Tradiční pozemní vysílání (např. DVB-T2) by mohlo UHD doručovat, ale k pevným přijímačům, nikoli plynule k mobilním zařízením integrovaným s buněčnou konektivitou a interaktivními službami.

Vytvoření služby UHDTV mělo tento problém vyřešit využitím stávající infrastruktury eMBMS v nové, vylepšené podobě. Poskytlo standardizovanou, s mobilní sítí integrovanou metodu, jak mohou vysílatelé oslovit mobilní uživatele prémiovým živým obsahem v nejvyšší kvalitě. Tím se vyřešil problém zahlcení sítě díky spektrální účinnosti vysílání a zároveň se vytvořil nový obchodní model pro operátory a vlastníky obsahu. Řešilo to omezení předchozích služeb mobilní televize (jako MBMS v 3G), kterým chyběla šířka pásma pro HD, natož pro UHD, a které nebyly integrovány s pokročilými službami core sítí 4G/5G.

## Klíčové vlastnosti

- Využívá eMBMS (LTE) a 5G Broadcast (NR) pro point-to-multipoint doručování
- Používá provoz v jedinofrekvenční síti (MBSFN) pro vylepšené pokrytí a účinnost
- Definuje specifické mediální profily využívající HEVC video a pokročilé audiokodeky pro vysílání
- Zahrnuje objevování služeb prostřednictvím elektronického průvodce programem (ESG)
- Poskytuje inherentní škálovatelnost pro podporu neomezeného počtu současných diváků
- Integruje se s core sítí mobilní sítě pro správu služeb a potenciální hybridní unicast/broadcast scénáře použití

## Související pojmy

- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [UHDTV na 3GPP Explorer](https://3gpp-explorer.com/glossary/uhdtv/)
