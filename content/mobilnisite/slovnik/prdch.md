---
slug: "prdch"
url: "/mobilnisite/slovnik/prdch/"
type: "slovnik"
title: "PRDCH – Physical reader-to-device channel"
date: 2026-01-01
abbr: "PRDCH"
fullName: "Physical reader-to-device channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prdch/"
summary: "Fyzický kanál zavedený v NR pro komunikaci mezi zařízeními (D2D) a postranní spoj, konkrétně pro čtecí zařízení, které přenáší data k cílovému zařízení. Působí na rozhraní sidelink a umožňuje přímé zj"
---

PRDCH (fyzický kanál čtečka-zařízení) je fyzický kanál v postranním spoji (sidelink) komunikaci 5G NR používaný čtecím zařízením k přímému přenosu dat k cílovému zařízení pro zjišťování a přímou komunikaci mezi zařízeními.

## Popis

Physical Reader-to-Device Channel (PRDCH) je downlink fyzický kanál definovaný na rozhraní postranního spoje (sidelink) 5G New Radio (NR), standardizovaný od 3GPP Release 19. Je klíčovou součástí rámce NR sidelink komunikace, který podporuje přímé propojení mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)). PRDCH je konkrétně používán zařízením fungujícím jako 'čtečka' nebo iniciující stranou k přenosu dat a řídicích informací k cílovému 'zařízení' v rámci sidelink komunikační relace. Tento kanál funguje na rozhraní PC5, což je referenční bod pro přímou komunikaci mezi uživatelskými zařízeními (UE), a je navržen pro práci v situacích s pokrytím i mimo pokrytí, s podporou plánování ze sítě i bez ní.

Pokud jde o strukturu fyzické vrstvy, PRDCH je mapován na specifické fyzické zdroje v rámci mřížky zdrojů NR sidelink. Využívá flexibilní NR numerologii, podporuje různé rozestupy podnosných a délky cyklické prefixy, aby se přizpůsobil různým kmitočtovým pásmům (včetně FR1 a FR2) a požadavkům služeb (např. vysoká spolehlivost, nízká latence). Kanál přenáší přepravní blok, který zahrnuje uživatelská data pro sidelink komunikaci. Jeho přenos zahrnuje typické postupy NR fyzické vrstvy: kanálové kódování (pravděpodobně s použitím [LDPC](/mobilnisite/slovnik/ldpc/) kódů pro data), modulaci ([QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM), mapování vrstev a prekódování. Zdroje pro PRDCH mohou být autonomně vybrány vysílajícím UE (Režim 2) nebo naplánovány prostřednictvím sidelink řídicí informace ([SCI](/mobilnisite/slovnik/sci/)) přijaté ze sítě nebo jiného UE.

Role PRDCH je klíčová pro umožnění efektivních sidelink služeb, jako jsou komunikace pro veřejnou bezpečnost, zprávy vehicle-to-everything ([V2X](/mobilnisite/slovnik/v2x/)) a komerční služby založené na blízkosti. Funguje ve spojení s dalšími sidelink kanály: Physical Sidelink Control Channel ([PSCCH](/mobilnisite/slovnik/pscch/)) přenáší přidruženou SCI, která plánuje a popisuje přenos PRDCH (např. přidělení zdrojů, schéma modulace a kódování), a Physical Sidelink Feedback Channel (PSFCH) může přenášet hybridní zpětnou vazbu automatického opakování požadavku (HARQ). PRDCH podporuje pokročilé funkce nedílné pro NR, včetně beamformingu a MIMO pro zvýšené pokrytí a kapacitu na vyšších kmitočtech, a je navržen tak, aby splňoval přísné požadavky pro ultra spolehlivou nízkolatenční komunikaci (URLLC) a rozšířené mobilní širokopásmové připojení (eMBB) přes sidelink. Jeho návrh zajišťuje spektrální účinnost a spolehlivou přímou komunikaci a tvoří základní datové potrubí pro NR D2D.

## K čemu slouží

PRDCH byl vytvořen, aby naplnil potřebu výkonného, nativního NR fyzického datového kanálu pro sidelink komunikaci, protože předchozí standardy D2D v LTE (založené na PSSCH) nebyly optimalizovány pro plné možnosti 5G. Motivace vychází z rozšiřujících se případů užití pro přímou komunikaci zařízení mimo tradiční veřejnou bezpečnost, včetně pokročilých V2X aplikací (jako je kooperativní snímání a autonomní řízení), průmyslového IoT a imerzivních zkušeností rozšířené reality (XR), které vyžadují vysoké přenosové rychlosti, velmi nízkou latenci a vysokou spolehlivost mezi zařízeními.

Řeší omezení LTE sidelink, který byl primárně navržen pro nižší přenosové rychlosti a méně dynamické přidělování zdrojů. NR sidelink, s kanály jako je PRDCH, využívá všech pokroků fyzické vrstvy 5G NR, jako je flexibilní numerologie, pokročilé kanálové kódování a beam-based provoz, aby podporoval širší spektrum kmitočtů (včetně mmWave), zlepšil spektrální účinnost a snížil latenci. Vytvoření vyhrazené nomenklatury kanálu 'reader-to-device' také pomáhá objasnit směrový charakter komunikace ve složitějších sidelink scénářích zahrnujících zjišťování, skupinové vysílání a unicast, a poskytuje standardizovaný a efektivní mechanismus pro přenos dat v rozvíjejícím se prostředí služeb založených na blízkosti.

## Klíčové vlastnosti

- Datový fyzický kanál na bázi NR pro sidelink (PC5) komunikaci
- Podporuje flexibilní numerologii pro různorodé potřeby pásem a služeb
- Využívá pokročilé techniky NR, jako je LDPC kódování a MIMO/beamforming
- Může fungovat s plánováním zdrojů ze sítě (Režim 1) nebo autonomně (Režim 2)
- Navržen pro vysokou spolehlivost a nízkou latenci požadovanou V2X a URLLC
- Funguje ve spojení s PSCCH pro řízení a s PSFCH pro zpětnou vazbu

## Související pojmy

- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [PSFCH – Physical Sidelink Feedback Channel](/mobilnisite/slovnik/psfch/)

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.291** (Rel-19) — Ambient IoT Physical Layer Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.391** (Rel-19) — NR; Ambient IoT MAC Protocol Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [PRDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/prdch/)
