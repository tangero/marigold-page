---
slug: "pft"
url: "/mobilnisite/slovnik/pft/"
type: "slovnik"
title: "PFT – Packet Flow Timer"
date: 2025-01-01
abbr: "PFT"
fullName: "Packet Flow Timer"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pft/"
summary: "Packet Flow Timer (PFT) je síťově řízený časovač používaný v systémech GPRS/EDGE ke správě stavu a prostředků dočasného toku bloků (TBF) nebo kontextu paketového toku. Řídí uvolnění rádiových a síťový"
---

PFT je síťově řízený časovač používaný v systémech GPRS/EDGE pro správu prostředků tím, že řídí uvolnění dočasného toku bloků (Temporary Block Flow) nebo kontextu paketového toku (Packet Flow Context) po období nečinnosti.

## Popis

Packet Flow Timer (PFT) je klíčový parametr správy sítě v architektuře systémů [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/), který je specificky svázán s procedurami správy paketového toku ([PFM](/mobilnisite/slovnik/pfm/)). Jedná se o konfigurovatelnou hodnotu časovače, kterou udržuje síť, primárně [SGSN](/mobilnisite/slovnik/sgsn/) (Serving GPRS Support Node) a [BSS](/mobilnisite/slovnik/bss/) (Base Station System), za účelem řízení setrvání prostředků pro přenos dat. PFT je asociován s dočasným tokem bloků ([TBF](/mobilnisite/slovnik/tbf/)) – což je alokace fyzických rádiových prostředků na kanálu pro paketová data ([PDCH](/mobilnisite/slovnik/pdch/)) pro přenos dat v uplinku nebo downlinku – nebo obecněji s logickým kontextem paketového toku. Jeho hlavní funkcí je určit, jak dlouho by síť měla tyto alokované prostředky udržovat po přenosu posledního datového bloku, než zahájí proceduru uvolnění.

Operačně, když je pro mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) zřízen TBF pro odesílání nebo přijímání datových paketů, je příslušný PFT spuštěn nebo restartován s každým úspěšným přenosem nebo příjmem RLC (Radio Link Control) datového bloku. To udržuje TBF v aktivním stavu. Pokud nejsou před vypršením PFT přeneseny žádné další datové bloky, síť to interpretuje jako období nečinnosti a spustí uvolnění TBF. To zahrnuje uvolnění rádiových prostředků na rozhraní Um a aktualizaci stavu přidruženého kontextu paketového toku v SGSN, ačkoli kontext PDP na vyšší vrstvě může zůstat aktivní ve stavu 'ready'. Mechanismus PFT umožňuje rychlé obnovení přenosu dat (zřízením nového TBF), pokud činnost opět nastane, a zároveň zajišťuje, že vzácné rádiové prostředky nejsou plýtvány na nečinná spojení.

Různé hodnoty PFT mohou být použity pro TBF v uplinku a downlinku a lze je přizpůsobit na základě QoS profilu kontextu PDP (např. kratší časovač pro provoz třídy background, delší pro interaktivní provoz). Hodnoty časovače jsou typicky konfigurovány operátorem sítě a mohou být komunikovány k MS během určitých procedur. PFT je klíčovým prvkem pro dosažení uživatelského zážitku 'vždy připojen' u GPRS, protože umožňuje, aby logická relace (kontext PDP) zůstala aktivní, zatímco jsou efektivně spravovány prostředky fyzické rádiové vrstvy. Vyvažuje efektivitu využití prostředků a odezvu služeb, čímž brání zbytečné signalizaci u častých, krátkých datových záblesků.

## K čemu slouží

Packet Flow Timer byl zaveden, aby vyřešil základní problém optimalizace prostředků u přerušovaného (bursty) charakteru paketového datového provozu v omezeném rádiovém prostředí GSM/GPRS. Na rozdíl od okruhově přepínaných hovorů, které drží vyhrazený kanál, jsou paketová data přerušovaná. Držení TBF (rádiového prostředku) neomezeně dlouho po přenosu dat by plýtvalo cennými časovými sloty a snižovalo síťovou kapacitu pro ostatní uživatele. Naopak, okamžité zrušení TBF po každém jednotlivém datovém bloku by generovalo nadměrnou signalizační režii u běžných interaktivních aplikací, jako je prohlížení webu, které se skládají z mnoha krátkých záblesků typu požadavek-odpověď.

PFT poskytuje inteligentní kompromis. Umožňuje síti krátce udržovat prostředky pro přenos dat během období nečinnosti v očekávání dalších bezprostředních dat. Tím se snižuje latence pro následující pakety v rámci stejného 'toku' nebo 'transakce', protože TBF nemusí být znovu zřizován. Pokud nečinnost přetrvává déle než časovač, jsou prostředky řádně uvolněny. Tento mechanismus byl zásadní pro to, aby byly rané mobilní datové služby zároveň efektivní i responsivní. Přímo podporoval konstrukční cíl GPRS, kterým je statistické multiplexování a sdílení prostředků. Konfigurovatelnost PFT umožnila operátorům ladit výkon sítě na základě vzorců provozu a mixu služeb, čímž se stal PFT nezbytným nástrojem pro diferenciaci Quality of Service a celkové řízení rádiových prostředků v paketových sítích 2G/2.5G.

## Klíčové vlastnosti

- Síťově řízený časovač spravující uvolnění prostředků dočasného toku bloků (TBF)
- Spuštěn/restartován s přenosem každého RLC datového bloku
- Vypršení spouští síťově iniciované uvolnění kontextu rádiového přenosu dat
- Konfigurovatelný podle QoS třídy pro vyvážení efektivity a responsivity
- Umožňuje, aby kontext PDP zůstal aktivní, i když jsou rádiové prostředky uvolněny
- Klíčový mechanismus pro optimalizaci využití rádiových prostředků u přerušovaného (bursty) paketového datového provozu

## Související pojmy

- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [PFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/pft/)
