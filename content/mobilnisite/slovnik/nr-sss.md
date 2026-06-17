---
slug: "nr-sss"
url: "/mobilnisite/slovnik/nr-sss/"
type: "slovnik"
title: "NR-SSS – New Radio-Secondary Synchronization Signal"
date: 2025-01-01
abbr: "NR-SSS"
fullName: "New Radio-Secondary Synchronization Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nr-sss/"
summary: "NR-SSS je signál fyzické vrstvy detekovaný po PSS během hledání buňky. Poskytuje zbývající část fyzické identifikace buňky (PCI) a umožňuje detekci časování rámce. Společně s PSS jednoznačně identifik"
---

NR-SSS je signál fyzické vrstvy 5G, který je detekován po PSS a poskytuje zbývající část fyzické identifikace buňky (Physical Cell Identity) a umožňuje detekci časování rámce, čímž buňku jednoznačně identifikuje.

## Popis

New Radio-Secondary Synchronization Signal (NR-SSS) je doprovodný signál k [NR-PSS](/mobilnisite/slovnik/nr-pss/) v rámci 5G NR SS/PBCH bloku. Po detekci PSS přesně ví UE, kde v čase má hledat SSS, protože jejich relativní pozice v rámci SSB jsou specifikací pevně stanoveny. Primární úlohou NR-SSS je přenést zbývající část fyzické identifikace buňky (PCI). Zatímco PSS indikuje jednu ze 3 možných hodnot (N_ID^(2)), SSS indikuje jednu z 336 možných hodnot (N_ID^(1)). Jejich kombinací (PCI = 3 * N_ID^(1) + N_ID^(2)) vznikne celý rozsah PCI od 0 do 1007. Detekce SSS navíc umožňuje UE určit hranici 10ms rádiového rámce, čímž se vyřeší 5ms nejednoznačnost zbývající po detekci PSS.

NR-SSS je také založen na M-posloupnosti ve frekvenční doméně, ale ve srovnání s PSS používá delší a složitější metodu generování. Jedná se o posloupnost délky 127 generovanou ze dvou prokládaných M-posloupností, které jsou skramblovány v závislosti na indexu PSS posloupnosti (N_ID^(2)). Tento návrh zajišťuje ortogonalitu a nízkou vzájemnou korelaci mezi různými SSS posloupnostmi, čímž se snižuje pravděpodobnost chybné detekce. Stejně jako PSS je mapován na 127 sousedních subnosných v rámci SSB, zabírá stejnou sadu subnosných, ale v jiném [OFDM](/mobilnisite/slovnik/ofdm/) symbolovém čase. Konkrétní symbolová pozice SSS v rámci SSB závisí na rozestupu subnosných.

Z architektonického hlediska je NR-SSS generován fyzickou vrstvou gNB pro každý přenos SSB. Jeho detekce UE je klíčovým krokem v procesu hledání a výběru buňky. Po nalezení PSS a SSS má UE získáno PCI buňky, symbolové časování a časování rámce. Tyto informace jsou nezbytné pro deskramblování referenčních signálů (jako je [DM-RS](/mobilnisite/slovnik/dm-rs/) pro PBCH) a pro zahájení dekódování NR-PBCH za účelem získání [NR-MIB](/mobilnisite/slovnik/nr-mib/). SSS také pomáhá rozlišit buňky, které mohou sdílet stejnou PSS posloupnost. Kombinovaný návrh PSS/SSS je optimalizován pro hledání buňky s nízkou latencí, což podporuje rychlé objevování sítě pro mobilní zařízení, IoT senzory a další 5G koncové body v různých scénářích nasazení od makro buněk po husté small buňky.

## K čemu slouží

NR-SSS byl vytvořen, aby dokončil proces identifikace buňky zahájený [NR-PSS](/mobilnisite/slovnik/nr-pss/), a řešil tak potřebu robustního a jednoznačného mechanismu identifikace buňky v různorodých prostředích 5G. Problém, který řeší, je poskytnout UE přesné časování rámce a úplnou fyzickou identifikaci buňky (PCI), což je nezbytné pro všechny následné procedury fyzické vrstvy, včetně odhadu kanálu, demodulace vysílacích kanálů a identifikace interference. V LTE také SSS poskytoval časování rámce, ale návrh 5G musel počítat s flexibilnější strukturou rámce a možností velmi hustých sítí s mnoha překrývajícími se buňkami.

Historickým motivem pro jeho návrh byla potřeba většího prostoru pro identifikaci buněk (1008 PCI) pro podporu ultra-hustých síťových nasazení bez konfliktů PCI. Prokládaný návrh M-posloupnosti pro NR-SSS byl zvolen, aby poskytoval dobré autokorelační a vzájemné korelační vlastnosti, což zajišťuje spolehlivou detekci i při vysoké interferenci ze sousedních buněk – což je běžný scénář v městských nasazeních 5G. Jeho závislost na PSS posloupnosti (prostřednictvím skramblování) navíc spojuje oba signály dohromady, čímž zlepšuje celkovou robustnost procedury hledání buňky. Tento návrh zajišťuje, že UE může buňku rychle a přesně identifikovat, což je zásadní pro mobilitu (předávání), výběr sítě a efektivní správu rádiových zdrojů v ekosystému 5G.

## Klíčové vlastnosti

- Založen na posloupnosti délky 127 generované ze dvou prokládaných M-posloupností
- Poskytuje 336 možných posloupností (N_ID^(1) = 0...335) pro dokončení PCI (0-1007)
- Umožňuje detekci hranice 10ms rádiového rámce, čímž řeší 5ms časovou nejednoznačnost
- Skramblování posloupnosti závisí na detekovaném indexu PSS (N_ID^(2))
- Vysílán s pevným symbolovým odstupem od PSS ve stejném SSB
- Nezbytný pro UE k získání úplné identifikace buňky před dekódováním PBCH/MIB

## Související pojmy

- [NR-PSS – New Radio-Primary Synchronization Signal](/mobilnisite/slovnik/nr-pss/)
- [NR-MIB – NR-Master Information Block](/mobilnisite/slovnik/nr-mib/)

## Definující specifikace

- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [NR-SSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nr-sss/)
