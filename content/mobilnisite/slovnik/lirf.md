---
slug: "lirf"
url: "/mobilnisite/slovnik/lirf/"
type: "slovnik"
title: "LIRF – Location Information Relay Function"
date: 2025-01-01
abbr: "LIRF"
fullName: "Location Information Relay Function"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lirf/"
summary: "LIRF je síťová funkce, která přeposílá informace související s polohou mezi uživatelským zařízením (UE) a serverem polohy, jako je Gateway Mobile Location Centre (GMLC). Funguje jako zprostředkovatel"
---

LIRF je síťová funkce, která přeposílá informace o poloze mezi uživatelským zařízením (UE) a serverem polohy za účelem podpory služeb, jako jsou tísňová volání a navigace.

## Popis

Location Information Relay Function (LIRF) je funkční entita definovaná v architektuře 3GPP, konkrétně popsaná v TS 25.305 pro UTRAN (UMTS Terrestrial Radio Access Network). Jejím hlavním úkolem je sloužit jako přenosový bod pro signalizaci a data související s polohou mezi mobilním zařízením a infrastrukturou služeb polohy v jádru sítě. Samotnou polohu nepočítá, ale je klíčová pro přenos nezbytných informací, jako jsou měřicí reporty nebo pomocná data, vyžadovaných metodami určování polohy, jako je Observed Time Difference Of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)).

Z architektonického hlediska je LIRF typicky implementována v rámci Radio Network Controller (RNC) v síti UMTS. Rozhraní k UE zajišťuje přes rádiové rozhraní Uu a k serveru polohy v jádru sítě, často Serving Mobile Location Centre (SMLC) nebo Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), přes rozhraní Iupc. Funkce zajišťuje adaptaci protokolů a směrování zpráv, čímž zaručuje, že požadavky na polohu ze sítě jsou doručeny k UE a že měření polohy nebo schopnosti UE jsou spolehlivě reportovány zpět.

Při provozu, když je spuštěna služba polohy (např. pro tísňové volání), přijme LIRF požadavek na polohu z jádra sítě. Poté iniciuje s UE příslušné procedury určování polohy, které mohou zahrnovat zaslání pomocných dat k UE pro zlepšení rychlosti a přesnosti určení polohy. UE provede požadovaná měření (např. satelitních signálů nebo časování sousedních buněk) a odešle měřicí report zpět přes LIRF. LIRF přepošle tato nezpracovaná data na server polohy, kde proběhne vlastní výpočet polohy. Toto oddělení přenosové a výpočetní funkce umožňuje optimalizovanou síťovou architekturu a podporuje různé technologie určování polohy.

Role LIRF je nedílnou součástí plnění regulatorních požadavků na lokalizaci tísňových volajících a umožňuje komerční služby založené na poloze. Standardizací této přenosové funkce zajistilo 3GPP interoperabilitu mezi síťovými zařízeními různých výrobců a poskytlo konzistentní mechanismus pro podporu vyvíjejících se technik určování polohy napříč více vydáními 3GPP, od počátečních specifikací UMTS až po pozdější vylepšení.

## K čemu slouží

LIRF byla vytvořena, aby řešila potřebu standardizovaného a spolehlivého mechanismu pro podporu služeb polohy ([LCS](/mobilnisite/slovnik/lcs/)) v sítích 3GPP, konkrétně pro UMTS. Před její specifikací byly služby polohy méně standardizované, což mohlo vést k problémům s interoperabilitou mezi síťovými prvky různých výrobců. LIRF poskytuje jasný architektonický bod pro přenos specifické polohové signalizace a odděluje transport polohových dat od jejich výpočtu.

Hlavní problém, který řeší, je umožnění efektivní komunikace mezi UE, které obsahuje rádiová měření, a síťovým serverem polohy, který disponuje výpočetními zdroji a databázovými informacemi (jako jsou souřadnice buněk) pro výpočet polohy. Bez vyhrazené přenosové funkce by tuto komunikaci musely ad-hoc zvládat jiné síťové entity, což by komplikovalo návrh protokolů a správu sítě. LIRF standardizuje rozhraní a procedury a zajišťuje, že požadavky na polohu mohou být obslouženy přesně a v rámci časových omezení vyžadovaných pro služby jako E-911.

K jejímu vytvoření motivovala rostoucí regulatorní a komerční poptávka po mobilních službách polohy na počátku 21. století. Regulátoři začali vyžadovat schopnost lokalizovat tísňové volající, zatímco operátoři chtěli zavádět služby jako navigace, vyhledávání přátel nebo reklamu založenou na poloze. LIRF jako součást širší architektury služeb polohy 3GPP poskytla základní rámec pro splnění těchto požadavků škálovatelným a budoucím vývojem odolným způsobem, podporujícím jak síťové, tak terminálové metody určování polohy.

## Klíčové vlastnosti

- Přeposílá specifickou polohovou signalizaci mezi UE a síťovým serverem polohy
- Podporuje více metod určování polohy (např. OTDOA, A-GNSS) přenosem relevantních měřicích a pomocných dat
- Typicky implementována v rámci Radio Network Controller (RNC) v UTRAN
- Pro komunikaci se serverem polohy v jádru sítě využívá standardizované rozhraní Iupc
- Umožňuje splnění požadavků na lokalizaci pro tísňové služby (např. E-112)
- Usnadňuje interoperabilitu mezi zařízeními různých výrobců tím, že poskytuje standardizovanou funkční entitu

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [LIRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lirf/)
