---
slug: "rsi"
url: "/mobilnisite/slovnik/rsi/"
type: "slovnik"
title: "RSI – Ratio of Self-Interference"
date: 2026-01-01
abbr: "RSI"
fullName: "Ratio of Self-Interference"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsi/"
summary: "Klíčový metrický ukazatel výkonu pro vnitropásmový plný duplex (IBFD) a pokročilé transceiverové systémy, který kvantifikuje úroveň vlastního rušení vzhledem k požadovanému signálu. Měří účinnost tech"
---

RSI je poměr vlastního rušení k požadovanému signálu, který měří účinnost potlačovacích technik klíčových pro umožnění simultánního vysílání a příjmu na stejné frekvenci v plně duplexních systémech.

## Popis

Poměr vlastního rušení (RSI) je bezrozměrná metrika definovaná jako poměr výkonu zbytkového vlastního rušení po potlačení k výkonu požadovaného přijímaného signálu. Matematicky RSI = P_zbytkové_[SI](/mobilnisite/slovnik/si/) / P_požadovaný, často vyjádřeno v decibelech (dB). Jde o ústřední hodnotu pro hodnocení systémů využívajících vnitropásmový plně duplexní (IBFD) rádiový provoz, kde zařízení vysílá a přijímá současně na stejném kmitočtu. Hlavní výzvou u IBFD je ohromný výkon vlastního vysílaného signálu zařízení, který proniká do jeho vlastního přijímacího řetězce a může přehlušit slabý požadovaný signál od vzdáleného vysílače. Tento průnik se označuje jako vlastní rušení (SI).

Proces zmírňování SI zahrnuje sofistikované techniky potlačení vlastního rušení ([SIC](/mobilnisite/slovnik/sic/)), které fungují napříč více doménami: anténní doménou (využitím izolace antén a směrového oddělení), analogovou/[RF](/mobilnisite/slovnik/rf/) doménou (využitím vyvažovacích obvodů, laditelných filtrů a RF potlačení) a digitální doménou (využitím adaptivního digitálního zpracování signálu pro modelování a odečtení odhadovaného rušení). Metrika RSI zachycuje celkovou účinnost tohoto celého SIC řetězce. Po všech stupních potlačení je zbývající výkon rušení (P_zbytkové_SI) tím, co narušuje požadovaný signál. Nižší hodnota RSI indikuje úspěšnější potlačení, což znamená, že zbytkové SI je mnohem slabší než požadovaný signál, což umožňuje úspěšnou demodulaci a dekódování.

Ve specifikacích 3GPP, zejména v kontextu NR a studiích o pokročilých transceiverech (např. pro Integrated Access and Backhaul - [IAB](/mobilnisite/slovnik/iab/)), se RSI používá k charakterizaci požadavků na výkon transceiveru a k modelování výkonu na systémové úrovni. Dosahovaná hodnota RSI určuje praktickou proveditelnost IBFD. Například, pokud je vysílaný výkon +20 dBm a šumové dno přijímače je -90 dBm, musí systém SIC dosáhnout zhruba 110 dB potlačení, aby snížil zbytkové SI na úroveň šumového dna. RSI by v tomto případě bylo poměrem tohoto zbytkového výkonu na úrovni šumového dna k výkonu příchozího požadovaného signálu. Konstruktéři systémů používají RSI k výpočtu efektivního poměru signálu k rušení a šumu ([SINR](/mobilnisite/slovnik/sinr/)), který přímo určuje dosažitelné datové rychlosti a spolehlivost plně duplexního spoje.

## K čemu slouží

Metrika RSI byla zavedena, aby řešila zásadní výzvu vnitropásmové plně duplexní komunikace, technologie slibující zdvojnásobení spektrální účinnosti tím, že umožňuje simultánní vysílání a příjem na stejném frekvenčním zdroji. Tradiční bezdrátové systémy pracují v poloduplexních režimech (časově nebo frekvenčně dělených) právě proto, aby se vyhnuly vážnému problému vlastního rušení. Snaha o IBFD jako prostředek k dramatickému zvýšení kapacity pro 5G a další generace si vyžádala standardizovaný způsob, jak kvantifikovat klíčovou technickou překážku: jak dobře dokáže transceiver potlačit své vlastní vysílání.

Před formální definicí RSI používal výzkum plně duplexních systémů různé ad-hoc metriky, jako je 'hloubka potlačení' nebo se uváděl pouze absolutní zbytkový výkon. RSI poskytuje metriku relevantnější pro systém, protože dává rušení do vztahu k síle požadovaného signálu. To je zásadní, protože dopad zbytkového rušení není absolutní; je relativní vůči tomu, co se přijímač snaží dekódovat. Určitá úroveň zbytkového výkonu může být zanedbatelná při příjmu silného signálu z blízké základnové stanice, ale katastrofální při příjmu slabého signálu na okraji buňky. RSI přímo vstupuje do výpočtu [SINR](/mobilnisite/slovnik/sinr/), což z něj činí nezbytný parametr pro analýzu výkonnosti spoje a simulaci na systémové úrovni.

Jeho vytvoření bylo motivováno prací 3GPP na pokročilých anténních systémech a nových scénářích nasazení v Release 15 a novějších, jako je [IAB](/mobilnisite/slovnik/iab/). V IAB uzel přenáší backhaulový i přístupový provoz a plně duplexní provoz by mohl výrazně zvýšit jeho účinnost. Definice RSI umožnila 3GPP specifikovat požadavky na výkon pro transceivery schopné podporovat takové funkce. Poskytuje společný jazyk pro výrobce zařízení a operátory sítí, aby specifikovali, testovali a ověřovali schopnosti hardwaru v potlačení vlastního rušení, což zajišťuje interoperabilitu a předvídatelné výkonnostní zisky z plně duplexních technologií při jejich nasazení.

## Klíčové vlastnosti

- Kvantifikuje účinnost potlačení vlastního rušení (SIC) v plně duplexních systémech
- Definován jako poměr výkonu zbytkového vlastního rušení k výkonu požadovaného signálu
- Kritický vstup pro výpočet efektivního SINR v plně duplexních spojích
- Používá se k specifikaci požadavků na výkon transceiveru ve standardech 3GPP
- Aplikovatelný napříč více doménami potlačení: anténní, analogovou/RF a digitální
- Umožňuje modelování na systémové úrovni a analýzu kapacity pro vnitropásmový plně duplexní provoz

## Související pojmy

- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)

## Definující specifikace

- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation

---

📖 **Anglický originál a plná specifikace:** [RSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsi/)
