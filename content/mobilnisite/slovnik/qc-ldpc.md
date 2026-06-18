---
slug: "qc-ldpc"
url: "/mobilnisite/slovnik/qc-ldpc/"
type: "slovnik"
title: "QC-LDPC – Quasi-Cyclic Low Density Parity Check"
date: 2025-01-01
abbr: "QC-LDPC"
fullName: "Quasi-Cyclic Low Density Parity Check"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qc-ldpc/"
summary: "Třída LDPC kódů pro opravu chyb, u nichž je paritní matice konstruována z cyklicky posunutých jednotkových matic nebo nulových matic. Jako schéma kódování kanálu vybrané pro datové kanály 5G NR nabízí"
---

QC-LDPC je třída kódu pro opravu chyb s názvem Low Density Parity Check, vybraná pro datové kanály 5G NR, u níž je paritní matice sestavena z cyklicky posunutých jednotkových nebo nulových matic, což umožňuje vynikající výkon a efektivní hardwarovou implementaci.

## Popis

Quasi-Cyclic Low Density Parity Check (QC-LDPC) kódy jsou klíčovou technologií kódování kanálu přijatou pro datové kanály 5G New Radio (NR) pro rozšířené mobilní širokopásmové připojení (eMBB). Patří do rodiny [LDPC](/mobilnisite/slovnik/ldpc/) kódů, což jsou lineární blokové kódy definované řídkou paritní maticí (maticí H), což znamená, že většina prvků je '0' a pouze malý zlomek je '1'. Vlastnost 'Quasi-Cyclic' (kvazicyklická) ukládá této matici H specifickou, vysoce pravidelnou strukturu: je složena z menších čtvercových podmatic, z nichž každá je buď nulová matice, nebo cyklicky posunutá jednotková matice (cirkulant). Tato struktura je klíčem k jejím praktickým výhodám.

Architektura NR QC-LDPC kódu je podrobně popsána ve specifikaci 38.212. Základní graf je základním konceptem. 5G NR definuje dva primární základní grafy (BG1 a BG2). BG1 je větší a je navržen pro větší transportní bloky a vyšší kódové rychlosti, nabízí nejlepší špičkovou propustnost. BG2 je menší, optimalizovaný pro menší transportní bloky a nižší kódové rychlosti, poskytuje lepší výkon pro podmínky na okraji buňky a malé datové pakety. Proces kódování zahrnuje rozšíření těchto základních grafů pomocí faktoru 'zvednutí' (lifting factor) 'Z', který určuje velikost cirkulantních podmatic. Tím se vytvoří konečná paritní matice pro konkrétní velikost bloku a kódovou rychlost. Dekodér, typicky iterativní algoritmus šíření přesvědčení (belief propagation), si vyměňuje pravděpodobnostní zprávy (měkké informace) mezi uzly proměnných a kontrolními uzly reprezentovanými v Tannerově grafu kódu, který je přímo odvozen z matice H.

Úloha QC-LDPC ve fyzické vrstvě 5G NR spočívá v ochraně uživatelských a řídicích dat před chybami vzniklými během přenosu přes rádiový kanál. Používá se pro fyzický sdílený kanál pro downlink ([PDSCH](/mobilnisite/slovnik/pdsch/)) a fyzický sdílený kanál pro uplink ([PUSCH](/mobilnisite/slovnik/pusch/)). Její strukturovaná kvazicyklická povaha umožňuje vysoce efektivní paralelní zpracování v hardwarových implementacích kodéru i dekodéru. Tento paralelismus je zásadní pro splnění extrémních požadavků 5G na propustnost (rychlosti v řádu gigabitů za sekundu) a cíle nízké latence, protože umožňuje současné zpracování více bitů. Výkon QC-LDPC je charakterizován velmi strmou 'vodopádovou' oblastí v její křivce chybovosti bitů, což znamená, že jakmile poměr signálu k šumu překročí určitou prahovou hodnotu, chybovost dramaticky klesá, což umožňuje spolehlivou komunikaci při rychlostech velmi blízkých kapacitě kanálu.

## K čemu slouží

QC-LDPC bylo zavedeno, aby překonalo omezení Turbo kódů používaných v 4G LTE pro datové kanály. Zatímco Turbo kódy byly zásadním pokrokem pro 3G a 4G, v kontextu 5G čelily výzvám. Při velmi vysokých datových rychlostech (řádově Gbps) implementace dekodéru Turbo kódů trpěly vysokou implementační složitostí, delší latencí kvůli své iterativní sériové povaze a vnímaným výkonnostním stropem. Dále Turbo kódy vykazovaly 'error floor' (podlahu chybovosti) při velmi nízkých chybovostech, což bylo problematické pro ultra-spolehlivou komunikaci.

Hlavní problémy, které QC-LDPC řeší, jsou potřeba vyšší propustnosti, nižší latence a flexibilnějšího kódování kanálu pro různorodé případy užití 5G. Jeho strukturovaný návrh umožňuje masivní paralelizaci v architekturách dekodéru, což přímo řeší problém s propustností. Paralelizovatelný dekódovací algoritmus také snižuje zpracovatelskou latenci ve srovnání s více serializovaným Turbo dekódováním. Použití dvou základních grafů poskytuje vnitřní flexibilitu, což systému umožňuje efektivně kódovat transportní bloky v rozsahu od velmi malých (např. pro IoT) po extrémně velké (např. pro eMBB) bez významné režie způsobené doplňováním (padding), kterou vyžadoval Turbo kód LTE. Výběr QC-LDPC byl výsledkem rozsáhlého hodnocení a byl motivován jeho vynikajícím výkonem při vysokých kódových rychlostech převládajících v 5G, vhodností pro hardwarovou implementaci a absencí vysoké podlahy chybovosti.

## Klíčové vlastnosti

- Paritní matice sestavená z cirkulantních permutačních matic, umožňující efektivní paralelní zpracování
- Dva základní grafy (BG1 a BG2) pro optimální pokrytí širokého rozsahu velikostí bloků a kódových rychlostí
- Podpora hybridního ARQ (HARQ) s přírůstkovou redundancí prostřednictvím flexibilního přizpůsobení rychlosti (rate matching)
- Vykazuje strmou vodopádovou výkonnostní křivku a velmi nízkou podlahu chybovosti
- Umožňuje implementace dekodérů s vysokou propustností a nízkou latencí, nezbytné pro špičkové datové rychlosti 5G
- Přijato jako povinný kód kanálu pro datové kanály 5G NR eMBB (PDSCH/PUSCH)

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [QC-LDPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/qc-ldpc/)
