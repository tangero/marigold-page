---
slug: "aiur"
url: "/mobilnisite/slovnik/aiur/"
type: "slovnik"
title: "AIUR – Air Interface User Rate"
date: 2025-01-01
abbr: "AIUR"
fullName: "Air Interface User Rate"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aiur/"
summary: "AIUR je maximální přenosová rychlost pro uživatele podporovaná přes radiové (vzdušné) rozhraní v síti 3GPP. Definuje špičkovou propustnost dostupnou pro připojení jednotlivého uživatele, což je klíčov"
---

AIUR je maximální přenosová rychlost pro uživatele podporovaná přes rozhraní radiového přístupu v síti 3GPP, která definuje špičkovou propustnost dostupnou pro připojení jednotlivého uživatele.

## Popis

Air Interface User Rate (AIUR) je základní parametr výkonu definovaný ve specifikacích 3GPP, který kvantifikuje maximální dosažitelnou rychlost přenosu dat pro připojení jednotlivého uživatele přes radiové rozhraní Uu. Představuje teoretickou špičkovou propustnost dostupnou pro uživatelské zařízení (UE) za ideálních rádiových podmínek, bez započtení režie vyšších vrstev protokolů, signalizace nebo soupeření o sdílené médium. Tato rychlost je klíčovým determinantem uživatelského zážitku u datových služeb a je vnitřně spojena s možnostmi fyzické vrstvy a přidělenými rádiovými prostředky.

Technicky se AIUR vypočítává na základě kombinace několika parametrů nižších vrstev definovaných technologií rádiového přístupu. Pro UMTS (3G) to zahrnuje rozprostřovací faktor (SF), počet použitých kanalizačních kódů (v případě High-Speed Downlink Packet Access - [HSDPA](/mobilnisite/slovnik/hsdpa/)) a modulační schéma (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)). Rychlost je v podstatě hrubá přenosová rychlost dodávaná přenosovými kanály fyzické vrstvy (např. Dedicated Channel - [DCH](/mobilnisite/slovnik/dch/), High-Speed Downlink Shared Channel - [HS-DSCH](/mobilnisite/slovnik/hs-dsch/)) do vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Je to statický nebo semi-statický konfigurační parametr pro dané nastavení rádiového přenosového kanálu, který definuje horní hranici pro datovou „trubku“ tohoto připojení.

V architektuře sítě je AIUR klíčovým parametrem během zřizování a správy rádiového přenosového kanálu. Protokol řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) používá AIUR spolu s dalšími parametry QoS, jako je garantovaná přenosová rychlost ([GBR](/mobilnisite/slovnik/gbr/)), k vyjednání a konfiguraci odpovídajících přenosových kanálů a fyzických prostředků mezi Node B (základnovou stanicí) a UE. Jádrová síť přes přístupovou rádiovou síť (RAN) požaduje přenosový kanál s určitými charakteristikami QoS a RAN je namapuje na konkrétní hodnotu AIUR na základě dostupné kapacity buňky a možností UE. AIUR tedy slouží jako přímý překlad mezi požadavky QoS na úrovni služeb a fyzickou implementací rádiového spoje.

Jeho role sahá až k plánování a dimenzování sítě. Operátoři používají cílové hodnoty AIUR k projektování svých sítí, aby zajistili, že stanice buněk a backhaulové spoje mohou podporovat souhrnné AIUR všech očekávaných současných uživatelů pro danou kombinaci služeb. Zatímco skutečná propustnost uživatele je vždy nižší kvůli režii, retransmisím a plánování, AIUR poskytuje základní strop. Je to standardizovaný metrik, který umožňuje konzistentní srovnávání výkonu napříč různými zařízeními dodavatelů a nasazeními sítí, čímž zajišťuje interoperabilitu a jasné definice úrovní služeb.

## K čemu slouží

AIUR byl zaveden, aby poskytl standardizovanou, jednoznačnou definici maximální přenosové rychlosti pro uživatele na rádiovém rozhraní, což byla kritická potřeba, když se sítě 3G vyvíjely z primárně hlasově orientovaných systémů na systémy podporující data s UMTS. Před jeho formální definicí ve verzi 3GPP Release 4 mohly specifikace a implementace dodavatelů používat různé interpretace nebo metriky pro „uživatelskou přenosovou rychlost“, což vedlo k záměně v definicích služeb, plánování sítí a srovnávání výkonu. AIUR vytvořil společný technický jazyk a přesný referenční bod v rámci protokolového zásobníku (bod přístupu ke službám mezi fyzickou a MAC vrstvou) pro měření a garantování datové propustnosti.

Tento koncept řešil základní výzvu mapování požadavků na přenosovou rychlost na aplikační úrovni na proměnné a sdílené rádiové médium. Definováním AIUR jako konfigurovatelného atributu rádiového přenosového kanálu mohl systém 3GPP implementovat sofistikovanou diferenciaci QoS. Například streamovací videu službě mohl být přidělen rádiový přenosový kanál s vysokým AIUR a garantovanými charakteristikami, zatímco synchronizace e-mailů na pozadí mohla používat kanál s nižším nebo negarantovaným AIUR. To umožnilo efektivní správu rádiových prostředků a komerční nabídku datových služeb ve vrstvách.

Dále AIUR sloužil jako klíčový hybatel a metrik pro vývoj technologie rádiového přístupu. Vylepšení jako HSDPA a HSUPA v pozdějších verzích 3GPP byla v zásadě o zvyšování dosažitelného AIUR pro uživatele prostřednictvím technik, jako je adaptivní modulace a kódování, přenos s více kódy a rychlejší plánování. Snaha o vyšší hodnoty AIUR přímo poháněla cestovní mapu od 3G přes 4G LTE až po 5G NR, kde podobné koncepty (jako špičková přenosová rychlost odvozená z šířky pásma a řádu modulace) pokračují v tomto odkazu. Poskytoval jasný technický cíl pro zlepšování spektrální účinnosti a uživatelského zážitku.

## Klíčové vlastnosti

- Definuje maximální teoretickou přenosovou rychlost pro uživatele na rádiovém rozhraní Uu
- Slouží jako klíčový parametr pro řízení rádiových prostředků (RRC) během zřizování přenosového kanálu a vyjednávání QoS
- Vypočítává se z parametrů fyzické vrstvy (rozprostřovací faktor, modulace, počet kódů)
- Poskytuje standardizovaný metrik pro srovnávání výkonu sítě a její plánování
- Umožňuje diferenciaci QoS tím, že je konfigurovatelným atributem rádiového přenosového kanálu
- Ukotvuje definici přenosové rychlosti v bodě přístupu ke službám mezi vrstvou 1 a MAC

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview

---

📖 **Anglický originál a plná specifikace:** [AIUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/aiur/)
