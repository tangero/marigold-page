---
slug: "efl"
url: "/mobilnisite/slovnik/efl/"
type: "slovnik"
title: "EFL – Effective Frequency Load"
date: 2025-01-01
abbr: "EFL"
fullName: "Effective Frequency Load"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/efl/"
summary: "Effective Frequency Load (EFL) je metrika výkonnosti sítě používaná v sítích GSM a EDGE pro hodnocení zatížení přenosového kanálu na dané rádiové frekvenci. Poskytuje přesnější vyjádření využití kanál"
---

EFL je metrika výkonnosti sítě GSM/EDGE, která vyhodnocuje zatížení přenosového kanálu na rádiové frekvenci s přihlédnutím k rušení a kvalitě služeb, čímž poskytuje přesné vyjádření využití kanálu.

## Popis

Effective Frequency Load (EFL) je sofistikované měření zatížení definované v rámci GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)). Kvantifikuje využití rádiového kmitočtového (RF) kanálu tím, že bere v úvahu nejen objem přenášeného provozu, ale také zhoršení kvality způsobené rušením. Výpočet EFL je založen na konceptu 'efektivního' provozu, který váží přenášený provoz faktorem souvisejícím s poměrem signálu k rušení ([C/I](/mobilnisite/slovnik/c-i/)) na daném kanále. Nižší C/I, značící vyšší rušení, vede k vyšší váze, což znamená, že stejný objem provozu spotřebovává více 'efektivní' kapacity. To poskytuje operátorům sítí věrnější obraz toho, jak blízko je kanál svému praktickému kapacitnímu limitu v reálných podmínkách omezených rušením.

Základní princip zahrnuje měření přenášeného provozu (např. v erlangech) a převládající úrovně rušení. Specifikace jako 3GPP TS 45.903 definují metodiky jeho výpočtu. Hodnota EFL typicky leží v rozsahu od 0 do 1 (nebo 0 % do 100 %), přičemž hodnota blížící se 1 značí, že kanál je efektivně plně vytížen a kvalita služeb se pravděpodobně zhorší při pokusech o další připojení. Tato metrika se počítá pro každý TRX (Transceiver) a používá se systémy pro správu a optimalizaci sítě.

EFL hraje klíčovou roli v několika síťových operacích. Je důležitým vstupem pro algoritmy vyvažování provozu, které pomáhají směrovat nová volání na méně zatížené kmitočty. Pro plánování kapacity pomáhají historické trendy EFL identifikovat buňky nebo sektory, které vyžadují přidání dalších kanálů dříve, než se zhorší kvalita služeb. Také napomáhá analýze rušení; trvale vysoká hodnota EFL na kanále s mírným hrubým provozem naznačuje významný problém s rušením, který je třeba řešit úpravami kmitočtového plánu nebo antén. Tím, že poskytuje tuto metriku zatížení zohledňující kvalitu, umožňuje EFL inteligentnější a efektivnější využití vzácného rádiového spektra.

## K čemu slouží

EFL byl vytvořen, aby řešil omezení tradičních metrik zatížení, jako jsou prostá měření v erlangech, která berou v úvahu pouze objem provozu. V celulárních systémech omezených rušením, jako je GSM, je kmitočtový kanál přenášející určité množství provozu za podmínek silného rušení efektivně 'plnější' než kanál přenášející stejný provoz za čistých podmínek, protože kvalita na uživatele je horší. Spoléhání se pouze na objem provozu by mohlo vést ke špatné kvalitě hovorů, jejich přerušování a neefektivnímu využití spektra, protože síť by se mohla jevit jako mající volnou kapacitu, která je ve skutečnosti nepoužitelná.

Historický kontext představuje fáze zrání sítí GSM, kdy se kmitočtová reutilizace zahušťovala, aby se zvýšila kapacita, což následně zvýšilo ko-kanálové a přilehlé kanálové rušení. Plánovači sítí a optimalizační inženýři potřebovali jednotnou metriku kombinující provoz a rušení, aby mohli přesněji posoudit zdraví sítě a kapacitní limity. EFL tento problém vyřešil tím, že poskytl jediné standardizované číslo odrážející praktické zatížení zdroje, což efektivněji než samostatné ukazatele kvality a provozu vede rozhodnutí týkající se předávání hovorů (handover), řízení zahlcení a rozšiřování kapacity.

Jeho zavedení umožnilo robustnější automatickou optimalizaci sítě a položilo základy pro pokročilé funkce v pozdějších verzích [GERAN](/mobilnisite/slovnik/geran/). Porozuměním efektivnímu zatížení mohli operátoři zlepšit celkovou kvalitu sítě a spektrální účinnost, a oddálit tak nákladná rozšíření infrastruktury tím, že vytěžili více využitelné kapacity z existujících spektrálních zdrojů.

## Klíčové vlastnosti

- Měření zatížení vážené kvalitou s přihlédnutím k rušení (poměr C/I)
- Standardizovaná výpočetní metoda definovaná ve specifikacích 3GPP
- Poskytuje normalizovanou hodnotu typicky mezi 0 a 1 (0 % a 100 %)
- Používá se pro každý transceiver (TRX) na kmitočtovém kanálu GSM/EDGE
- Klíčový vstup pro algoritmy správy provozu a vyvažování zatížení
- Zásadní metrika pro dlouhodobé plánování kapacity a zmírňování rušení

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [EFL na 3GPP Explorer](https://3gpp-explorer.com/glossary/efl/)
