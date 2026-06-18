---
slug: "cbgti"
url: "/mobilnisite/slovnik/cbgti/"
type: "slovnik"
title: "CBGTI – Code Block Group Transmission Information"
date: 2025-01-01
abbr: "CBGTI"
fullName: "Code Block Group Transmission Information"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbgti/"
summary: "CBGTI je řídicí mechanismus fyzické vrstvy v 5G NR, který poskytuje podrobnou zpětnou vazbu o stavu příjmu jednotlivých skupin kódových bloků (CBG) v rámci transportního bloku. Umožňuje efektivnější H"
---

CBGTI je řídicí mechanismus fyzické vrstvy v 5G NR, který poskytuje podrobnou zpětnou vazbu o stavu příjmu jednotlivých skupin kódových bloků v rámci transportního bloku, aby umožnil efektivní HARQ retransmise.

## Popis

Code Block Group Transmission Information (CBGTI, informace o přenosu skupin kódových bloků) je klíčovou součástí fyzické vrstvy 5G New Radio (NR), konkrétně v rámci rámce downlink control information ([DCI](/mobilnisite/slovnik/dci/)). Funguje jako součást mechanismu zpětné vazby Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) a poskytuje podrobné informace o tom, které skupiny kódových bloků ([CBG](/mobilnisite/slovnik/cbg/)) v rámci transportního bloku byly přijaty úspěšně a které nikoli. Transportní blok je rozdělen na více kódových bloků pro kanálové kódování a tyto kódové bloky jsou dále seskupeny do CBG pro účely přenosu a zpětné vazby. Pole CBGTI v DCI přesně indikuje, které CBG jsou retransmitovány, což příjemci umožňuje kombinovat dříve přijaté CBG s nově přenášenými.

Architektura CBGTI je úzce integrována s 5G NR physical downlink shared channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) a physical uplink control channel ([PUCCH](/mobilnisite/slovnik/pucch/)) nebo physical uplink shared channel ([PUSCH](/mobilnisite/slovnik/pusch/)) pro zpětnou vazbu. Když uživatelské zařízení (UE) přijme transportní blok, provede dekódování každého CBG a vygeneruje [HARQ-ACK](/mobilnisite/slovnik/harq-ack/) zpětnou vazbu. Pokud některé CBG selžou, gNodeB použije CBGTI v plánovacím DCI pro retransmisi, aby specifikoval, které CBG jsou zahrnuty. Pole CBGTI je bitmapa, kde každý bit odpovídá jednomu CBG, přičemž '1' indikuje, že daný CBG je retransmitován, a '0' indikuje, že není. Délka této bitmapy je konfigurovatelná na základě maximálního počtu CBG na transportní blok, což je nastaveno přes [RRC](/mobilnisite/slovnik/rrc/).

Klíčové komponenty zahrnují konfigurační parametry CBG (maxCodeBlockGroupsPerTransportBlock), pole CBGTI v DCI formátech 1_0, 1_1 a 1_2 a návrh HARQ-ACK kodexu, který podporuje zpětnou vazbu založenou na CBG. Síť konfiguruje, zda je přenos založený na CBG povolen, prostřednictvím RRC signalizace, a pokud je povolen, musí jak vysílač, tak přijímač udržovat soft buffer na CBG místo na transportní blok. To vyžaduje sofistikovanější správu bufferu, ale umožňuje výrazné zisky v účinnosti. Příjemce používá informaci CBGTI k identifikaci, které CBG kombinovat z předchozích přenosů a které nahradit novými přenosy.

Úloha CBGTI v síti spočívá ve zvýšení účinnosti retransmisí, zejména u velkých transportních bloků, kde by retransmise celého bloku byla plýtvání. Umožněním částečných retransmisí snižuje latenci a zlepšuje propustnost, zvláště v náročných rádiových podmínkách. Funguje ve spojení s dalšími vylepšeními HARQ v 5G NR, jako je enhanced dynamic codebook pro HARQ-ACK zpětnou vazbu, aby poskytl robustní a účinný systém adaptace spojení. Implementace vyžaduje pečlivou koordinaci mezi plánováním, HARQ procesy a správou bufferu, aby byla zajištěna správná funkce napříč více přenosy.

## K čemu slouží

CBGTI bylo zavedeno v 5G NR, aby řešilo neefektivitu tradičních HARQ retransmisí založených na transportním bloku, zejména u velkých velikostí paketů. V předchozích buněčných systémech (včetně LTE), když jakákoli část transportního bloku selhala při dekódování, musel být retransmitován celý transportní blok, což plýtvalo šířkou pásma a zvyšovalo latenci. To se stávalo stále problematičtějším s podporou velmi vysokých datových rychlostí a velkých transportních bloků v 5G, kde retransmise celého bloku mohla spotřebovat významné zdroje a oddálit doručení dat.

Primární motivací pro CBGTI bylo zlepšit spektrální účinnost a snížit latenci umožněním podrobnějších retransmisí. Tím, že síti dovoluje retransmitovat pouze neúspěšné skupiny kódových bloků místo celého transportního bloku, CBGTI minimalizuje režii a lépe využívá dostupné rádiové zdroje. To je obzvláště důležité pro aplikace vyžadující vysokou spolehlivost a nízkou latenci, jako je ultra-reliable low-latency communications (URLLC), kde je efektivní oprava chyb kritická.

Historicky LTE zavedlo některé koncepty částečných retransmisí s omezeným úspěchem, ale CBGTI v 5G NR představuje systematický a flexibilnější přístup. Řeší omezení předchozích přístupů tím, že poskytuje standardizovaný, konfigurovatelný mechanismus, který bezproblémově spolupracuje s flexibilní numerologií 5G a širokým spektrem případů užití. Vytvoření CBGTI bylo hnací silou potřeby podporovat rozmanité požadavky 5G, od enhanced mobile broadband (eMBB) s velkými transportními bloky po URLLC s přísnými požadavky na spolehlivost, což činí efektivní retransmise nezbytnými pro celkový výkon systému.

## Klíčové vlastnosti

- Umožňuje retransmisi jednotlivých skupin kódových bloků místo celých transportních bloků
- Snižuje režii a zlepšuje spektrální účinnost pro velké transportní bloky
- Konfigurovatelný maximální počet CBG na transportní blok prostřednictvím RRC signalizace
- Používá indikaci založenou na bitmapě v DCI pro přesnou kontrolu retransmise
- Vyžaduje správu soft bufferu na CBG jak na straně vysílače, tak přijímače
- Spolupracuje s vylepšenými návrhy HARQ-ACK kodexu pro efektivní zpětnou vazbu

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [CBGTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbgti/)
