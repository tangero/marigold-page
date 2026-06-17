---
slug: "n-hd"
url: "/mobilnisite/slovnik/n-hd/"
type: "slovnik"
title: "N-HD – Network Header Decompressor"
date: 2025-01-01
abbr: "N-HD"
fullName: "Network Header Decompressor"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/n-hd/"
summary: "Entita v síti, typicky ve vrstvě PDCP řadiče RNC, která provádí dekompresi hlaviček na datových paketech ve směru uplink přijatých od UE. Rekonstruuje původní hlavičky IP/UDP/RTP z komprimovaných form"
---

N-HD je síťová entita, typicky ve vrstvě PDCP řadiče RNC, která dekomprimuje hlavičky paketů ve směru uplink od UE, aby rekonstruovala původní hlavičky IP/UDP/RTP pro směrování v jádru sítě.

## Popis

Network Header Decompressor (N-HD) je funkční entita v rámci UMTS rádiové přístupové sítě, implementovaná ve vrstvě Packet Data Convergence Protocol (PDCP) řadiče Radio Network Controller (RNC). Působí na cestě uplink a zpracovává datové pakety přijaté od uživatelského zařízení (UE). Kompresor hlaviček v UE (U-HC) odesílá přes rádiové rozhraní pakety s komprimovanými hlavičkami za účelem úspory šířky pásma ve směru uplink. N-HD tyto pakety přijímá a provádí inverzní operaci: využívá sdílený kontext robustní komprese hlaviček (ROHC), který udržuje v synchronizaci s kompresorem UE, k rekonstrukci úplných původních hlaviček IP, UDP, RTP nebo [ESP](/mobilnisite/slovnik/esp/). Proces dekomprese zahrnuje interpretaci komprimovaného formátu hlavičky, aplikaci kontextu (který obsahuje statické hodnoty polí a pravidla pro interpretaci měnících se polí) a výstup paketu identického s tím před kompresí na straně UE. N-HD je zodpovědný za správu kontextu na síťové straně pro směr uplink, včetně ověřování kontextu pomocí kontrolních součtů, zvládání poškození kontextu v důsledku ztráty paketů a zahajování opravných procedur prostřednictvím zpětnovazebních mechanismů ROHC. Musí robustně zvládat mimo pořadí doručené pakety a chyby vlastní bezdrátovému spoji. Po úspěšné dekompresi předává vrstva PDCP kompletní IP paket do jádra sítě přes rozhraní Iu-PS. N-HD pracuje v tandemu s [N-HC](/mobilnisite/slovnik/n-hc/) (pro směr downlink), ale funguje nezávisle a spravuje samostatné stavové automaty kontextu pro každý tok uplink od UE.

## K čemu slouží

N-HD byl vytvořen, aby umožnil efektivní přenos ve směru uplink od mobilních zařízení, která mají často omezenější vysílací výkon a přidělenou šířku pásma ve srovnání se směrem downlink. Stejně jako komprese ve směru downlink šetří rádiové prostředky, komprese uplink snižuje množství dat, která musí UE vysílat, čímž šetří její životnost baterie a zlepšuje celkovou kapacitu uplink. Role N-HD je klíčová, protože umožňuje síti těžit z kompresního zisku v obou směrech, čímž jsou úspory rádiových prostředků symetrické. Umístěním složitosti dekomprese do sítě (RNC) namísto do bran jádra sítě systém lokalizuje funkci dekomprese blízko rádiového rozhraní, minimalizuje latenci a zjednodušuje architekturu end-to-end. Tento návrh zajišťuje, že jádro sítě vždy přijímá standardní, nekomprimované IP pakety, čímž zachovává kompatibilitu s existující IP infrastrukturou a zjednodušuje funkce účtování, hluboké kontroly paketů a zabezpečení. N-HD jako součást frameworku ROHC řeší výzvu udržování synchronizace kompresního kontextu přes ztrátový spoj pomocí robustních algoritmů, které brání desynchronizaci kontextu, jež by mohla vést k trvalé ztrátě paketů.

## Klíčové vlastnosti

- Umístěn ve vrstvě PDCP řadiče RNC pro dekompresi provozu ve směru uplink
- Rekonstruuje úplné IP hlavičky z paketů komprimovaných ROHC odeslaných od UE
- Udržuje a synchronizuje dekompresní kontexty pro každý tok uplink od UE
- Implementuje mechanismy detekce chyb a opravy kontextu pomocí zpětné vazby ROHC
- Zvládá přeuspořádání paketů a odolnost vůči ztrátám specifické pro rádiový spoj
- Výstupem jsou standardní IP pakety do jádra sítě, což zajišťuje transparentnost sítě

## Související pojmy

- [N-HC – Network Header Compressor](/mobilnisite/slovnik/n-hc/)

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification

---

📖 **Anglický originál a plná specifikace:** [N-HD na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-hd/)
