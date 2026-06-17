---
slug: "d-cpich"
url: "/mobilnisite/slovnik/d-cpich/"
type: "slovnik"
title: "D-CPICH – Demodulation Common Pilot Channel"
date: 2025-01-01
abbr: "D-CPICH"
fullName: "Demodulation Common Pilot Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/d-cpich/"
summary: "D-CPICH je referenční signál v sestupné větvi v sítích UMTS/HSPA používaný pro odhad kanálu a demodulaci. Poskytuje stabilní fázový odkaz pro koherentní detekci, což umožňuje přesnou demodulaci vyhraz"
---

D-CPICH je referenční signál v sestupné větvi v sítích UMTS/HSPA, který poskytuje stabilní fázový odkaz pro odhad kanálu a koherentní demodulaci vyhrazených kanálů.

## Popis

Demodulation Common Pilot Channel (D-CPICH) je klíčová komponenta fyzické vrstvy v sítích 3GPP UMTS a [HSPA](/mobilnisite/slovnik/hspa/), která slouží jako fázový odkaz pro koherentní demodulaci vyhrazených fyzických kanálů. Na rozdíl od primárního [CPICH](/mobilnisite/slovnik/cpich/) ([P-CPICH](/mobilnisite/slovnik/p-cpich/)), který poskytuje pokrytí pro celou buňku a používá se pro vyhledávání buněk a měření pro předávání hovoru, je D-CPICH speciálně navržen pro podporu pokročilých přijímacích technik a zlepšení výkonu demodulace v různých rádiových podmínkách.

Architektonicky D-CPICH funguje jako sekundární společný pilotní kanál, který lze konfigurovat nezávisle na primárním pilotním kanálu. Vysílá známé pilotní symboly pomocí specifické kombinace kanalizačního kódu a kódu pro rozprostření spektra, která se liší od P-CPICH. Struktura kanálu spočívá v kontinuálním vysílání předdefinovaných pilotních symbolů na pevné úrovni výkonu, což umožňuje uživatelskému zařízení (UE) provádět přesný odhad kanálu pro vyhrazené fyzické kanály přiřazené danému UE. D-CPICH je vysílán ze stejné antény jako vyhrazené fyzické kanály, které podporuje, čímž zajišťuje fázové sladění mezi referenčním signálem a datovými kanály.

Během provozu D-CPICH umožňuje několik pokročilých schopností přijímače. Pokud je nakonfigurován, UE používá signál D-CPICH k odhadu charakteristik rádiového kanálu, včetně fázové rotace, útlumu amplitudy a časové disperze. Tento odhad kanálu je následně aplikován pro demodulaci přidružených vyhrazených fyzických kanálů prostřednictvím koherentní detekce. D-CPICH je obzvláště cenný ve scénářích zahrnujících diverzitu vysílání, formování svazku nebo operace [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output), kde je třeba přesně odhadnout charakteristiky kanálu pro různé přenosové cesty. Kanál podporuje jak otevřené, tak uzavřené schémata diverzity vysílání tím, že poskytuje potřebný fázový odkaz pro správné kombinování signálů z více antén.

Klíčovými součástmi implementace D-CPICH jsou přiřazení kanalizačního kódu, nastavení výkonu vůči P-CPICH a konfigurační parametry definující jeho použití. Síť konfiguruje parametry D-CPICH prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), včetně toho, zda použít D-CPICH pro specifické transportní kanály, a výkonového posunu vůči primárnímu pilotnímu signálu. Kanál hraje klíčovou roli ve vývoji HSPA tím, že podporuje pokročilé funkce jako modulace [64QAM](/mobilnisite/slovnik/64qam/), MIMO a operace s dvěma buňkami, kde se přesný odhad kanálu stává stále důležitějším pro udržení vysokých přenosových rychlostí a spektrální účinnosti.

## K čemu slouží

D-CPICH byl zaveden, aby řešil specifická omezení v sítích UMTS/[HSPA](/mobilnisite/slovnik/hspa/) související s přesností odhadu kanálu a výkonem demodulace. Před jeho zavedením sítě spoléhaly primárně na primární [CPICH](/mobilnisite/slovnik/cpich/) pro všechny účely odhadu kanálu, což se ukázalo jako nedostatečné pro pokročilé přenosové techniky a náročné rádiové podmínky. P-CPICH, který je celobuněčný a vysílaný s pevnými charakteristikami, nemohl poskytnout optimální fázový odkaz pro vyhrazené kanály zažívající odlišné podmínky šíření nebo používající specializované přenosové schémata.

Primární motivací pro vytvoření D-CPICH byla podpora vývoje funkcí HSPA, které vyžadovaly přesnější odhad kanálu. Když 3GPP zavedlo modulace vyššího řádu (16QAM a později 64QAM), diverzitu vysílání a schopnosti MIMO ve vydáních HSPA 7 a novějších, potřeba přesného fázového odkazu se stala kritickou. Tyto pokročilé funkce jsou citlivější na chyby v odhadu kanálu a použití pouze celobuněčného P-CPICH mohlo vést ke zhoršení výkonu, zejména na okrajích buněk nebo ve scénářích omezených interferencí.

D-CPICH tyto problémy řeší tím, že poskytuje vyhrazený fázový odkaz, který je specificky sladěn s přenosovými charakteristikami uživatelských vyhrazených kanálů. To umožňuje přesnější demodulaci, lepší výkon spoje a lepší využití pokročilých funkcí. Kanál umožňuje sítím udržovat vyšší přenosové rychlosti a lepší kvalitu služeb v různorodých rádiových podmínkách, což v konečném důsledku zvyšuje kapacitu systému a uživatelský zážitek a zároveň podporuje kontinuální vývoj standardů 3GPP směrem k vyšší spektrální účinnosti.

## Klíčové vlastnosti

- Poskytuje vyhrazený fázový odkaz pro koherentní demodulaci vyhrazených fyzických kanálů
- Podporuje pokročilé přenosové techniky včetně diverzity vysílání a formování svazku
- Umožňuje přesný odhad kanálu pro modulační schémata vyššího řádu (16QAM/64QAM)
- Konfigurovatelný výkonový posun vůči primárnímu CPICH pro optimalizaci
- Podporuje operace MIMO tím, že poskytuje anténně-specifické referenční signály
- Zlepšuje výkon v náročných rádiových podmínkách a na okrajích buněk

## Související pojmy

- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [P-CPICH – Primary Common Pilot Channel](/mobilnisite/slovnik/p-cpich/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [D-CPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/d-cpich/)
