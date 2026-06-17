---
slug: "ctch-bs"
url: "/mobilnisite/slovnik/ctch-bs/"
type: "slovnik"
title: "CTCH-BS – Common Traffic Channel Block Set"
date: 2025-01-01
abbr: "CTCH-BS"
fullName: "Common Traffic Channel Block Set"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctch-bs/"
summary: "CTCH-BS je datová struktura v protokolu MAC-c/sh/m pro UMTS, používaná k přenosu vysílaných nebo skupinově šířených uživatelských dat přes společný datový kanál (CTCH). Umožňuje efektivní přenos dat t"
---

CTCH-BS je datová struktura protokolu MAC-c/sh/m v UMTS, která přenáší vysílaná nebo skupinově šířená uživatelská data přes společný datový kanál (Common Traffic Channel) pro efektivní přenos typu point-to-multipoint k více uživatelským zařízením (UE).

## Popis

Common Traffic Channel Block Set (CTCH-BS) je základní datová jednotka v architektuře řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro společný datový kanál ([CTCH](/mobilnisite/slovnik/ctch/)) v UMTS, konkrétně zpracovávaná entitou MAC-c/sh/m. CTCH je přenosový kanál pro downlink používaný k vysílání nebo skupinovému šíření uživatelských dat k více uživatelským zařízením (UE) v rámci buňky. CTCH-BS slouží jako strukturovaný kontejner, který vrstva MAC předává fyzické vrstvě pro přenos přes tento kanál. Zapouzdřuje datové jednotky protokolů vyšších vrstev (PDU), například z vrstvy řízení rádiového spoje (RLC), a připravuje je pro zpracování fyzickou vrstvou a rádiový přenos.

Z architektonického hlediska je CTCH-BS generována entitou MAC-c/sh/m v Node B (nebo řízena RNC v dřívějších architekturách). Tato entita je zodpovědná za plánování a multiplexování dat pro společné kanály. Když jsou vysílaná nebo skupinově šířená data přijata z jádra sítě přes RNC, jsou zpracována vrstvou RLC a následně předána vrstvě MAC. Entita MAC-c/sh/m tato data naformátuje do CTCH-BS. Každá CTCH-BS má definovanou strukturu, která zahrnuje uživatelskou datovou část a nezbytné řídicí informace pro fyzickou vrstvu, aby mohla tuto sadu bloků správně zakódovat a vyslat přes rozhraní vzduchu. Fyzická vrstva mapuje CTCH-BS na sekundární společný řídicí fyzický kanál (S-CCPCH) pro přenos.

Operace zahrnuje přijetí RLC PDU vrstvou MAC; tyto PDU mohou být segmentovány nebo konkatenovány, aby odpovídaly velikosti přenosového bloku CTCH. CTCH-BS se skládá z jednoho nebo více těchto přenosových bloků, které jsou vysílány ve stejném přenosovém časovém intervalu (TTI). Fyzická vrstva před vysíláním na CTCH-BS aplikuje kanálové kódování (např. konvoluční nebo turbo kódování), prokládání a modulaci. Na straně uživatelského zařízení (UE) fyzická vrstva dekóduje přijímaný signál, rekonstruuje CTCH-BS a předává ji vrstvě MAC. Entita MAC-c/sh/m v UE následně extrahuje RLC PDU a předává je vrstvě RLC a vyšším vrstvám. Tento mechanismus umožňuje, aby jediný přenos ze sítě byl přijat všemi uživatelskými zařízeními (UE), která sledují CTCH, což umožňuje efektivní vysílací služby.

Mezi klíčové zahrnuté komponenty patří protokolová entita MAC-c/sh/m, přenosový kanál CTCH, fyzický kanál S-CCPCH a související přenosový formát (TF) a kombinace přenosových formátů (TFC), které definují velikost, kódování a načasování přenosu CTCH-BS. CTCH-BS hraje klíčovou roli při umožnění služeb vysílání v buňce ([CBS](/mobilnisite/slovnik/cbs/)), multimediální vysílací/skupinové služby ([MBMS](/mobilnisite/slovnik/mbms/)) v pozdějších vydáních a dalších aplikací typu point-to-multipoint tím, že poskytuje standardizovanou a efektivní metodu pro doručování společných uživatelských dat přes rádiové rozhraní UMTS.

## K čemu slouží

CTCH-BS byla vytvořena, aby poskytla standardizovaný mechanismus pro vysílání uživatelských dat k více uživatelským zařízením (UE) v síti UMTS. Před standardizací 3GPP měly celulární systémy omezené nebo proprietární metody pro doručování vysílaných dat. CTCH-BS, zavedená ve vydání UMTS Release 4, řešila potřebu efektivního, spolehlivého a řízeného datového kanálu typu point-to-multipoint v rámci rádiové přístupové sítě WCDMA (UTRAN). Vyřešila problém neefektivního vysílání identických dat přes více vyhrazených kanálů, které by spotřebovávaly nadměrné síťové prostředky a rádiovou kapacitu.

Motivace pramenila z rostoucí poptávky po vysílacích službách, jako jsou zpravodajské výstrahy, předpověď počasí, dopravní informace a následně i multimediální obsah. CTCH-BS umožňuje síti přenášet takové informace jednou přes společný kanál, což umožňuje všem zainteresovaným uživatelským zařízením (UE) v buňce přijmout je současně. Tím se ve srovnání s individuálními přenosy typu point-to-point šetří rádiové prostředky i šířka pásma jádra sítě. Poskytuje také základ pro pokročilejší vysílací/skupinové služby, jako je [MBMS](/mobilnisite/slovnik/mbms/), které byly zavedeny v pozdějších vydáních 3GPP.

Historicky měl GSM službu vysílání v buňce ([CBS](/mobilnisite/slovnik/cbs/)) využívající kanál Cell Broadcast Channel ([CBCH](/mobilnisite/slovnik/cbch/)), ale UMTS vyžadovalo novou architekturu integrovanou s jeho přenosovými kanály založenými na WCDMA a protokoly vrstvy [MAC](/mobilnisite/slovnik/mac/). Definice CTCH-BS v TS 25.324 tuto integraci poskytla, což zajistilo kompatibilitu s rámcem QoS UMTS, mechanismy řízení výkonu (pro společné kanály) a plánovacími algoritmy. Odstranila omezení dřívějších přístupů tím, že nabídla flexibilní strukturu sady přenosových bloků, která se mohla přizpůsobit různým datovým rychlostem a požadavkům služeb, a podpořila tak vývoj od jednoduchých textových vysílání k bohatšímu multimediálnímu obsahu.

## Klíčové vlastnosti

- Definuje datovou strukturu pro přenos vysílaných/skupinově šířených uživatelských dat na kanálu CTCH
- Zpracovávána protokolovou entitou MAC-c/sh/m v UTRAN
- Mapována na sekundární společný řídicí fyzický kanál (S-CCPCH) pro rádiový přenos
- Podporuje flexibilní kombinace přenosových formátů (TFC) pro proměnné datové rychlosti
- Umožňuje efektivní doručování typu point-to-multipoint k více uživatelským zařízením (UE) současně
- Tvoří základ pro službu vysílání v buňce (CBS) a MBMS v UMTS

## Související pojmy

- [CTCH – Common Traffic Channel](/mobilnisite/slovnik/ctch/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol

---

📖 **Anglický originál a plná specifikace:** [CTCH-BS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctch-bs/)
