---
slug: "t-taf"
url: "/mobilnisite/slovnik/t-taf/"
type: "slovnik"
title: "T-TAF – Transmission side Terminal Adaptation Function"
date: 2025-01-01
abbr: "T-TAF"
fullName: "Transmission side Terminal Adaptation Function"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-taf/"
summary: "T-TAF je funkční entita v sítích 3GPP zodpovědná za adaptaci datových toků z terminálu pro přenos po síti. Zajišťuje převod protokolů a formátování dat, čímž zaručuje kompatibilitu mezi terminálem a s"
---

T-TAF je funkční entita v sítích 3GPP, která adaptuje datové toky z terminálu pro přenos sítí tím, že zajišťuje převod protokolů a formátování dat.

## Popis

Funkce adaptace terminálu na straně přenosu (Transmission side Terminal Adaptation Function, T-TAF) je klíčová vrstva pro adaptaci protokolů definovaná v architektuře 3GPP, konkrétně v kontextu terminálového zařízení a datových služeb. Funguje jako součást terminálového zařízení nebo uvnitř sítě, aby usnadnila přenos uživatelských dat. Hlavní rolí T-TAF je provádět nezbytné převody a adaptace protokolů potřebné k tomu, aby data z terminálu byla kompatibilní s podkladovými mechanismy síťového přenosu. To zahrnuje adaptaci datových toků do příslušného formátu, přenosové rychlosti a procedur řízení chyb podle definic síťových protokolů.

Z architektonického hlediska je T-TAF často spojována s funkcí mobilního ukončení (Mobile Termination, [MT](/mobilnisite/slovnik/mt/)) nebo je integrována do protokolového zásobníku terminálu. Rozhraní má k vyšším vrstvám aplikací a nižším vrstvám rádiových přenosových protokolů. Funkce pracuje tak, že přijímá data z aplikační vrstvy terminálu, která mohou být v nativním formátu, a následně je zpracovává, aby vyhovovala požadavkům spojové a fyzické vrstvy sítě. Toto zpracování může zahrnovat segmentaci, opětovné složení, adaptaci rychlosti a kódování pro opravu chyb v závislosti na konkrétní službě a síťových podmínkách.

Klíčové součásti funkčnosti T-TAF zahrnují samotné adaptační protokoly, jako jsou ty definované pro přepojování okruhů nebo přepojování paketů, a řízení toku dat. Její role je zvláště důležitá v raných vydáních 3GPP (jako [R99](/mobilnisite/slovnik/r99/)), kde bylo třeba podporovat více typů datových služeb (např. fax, modemová data) přes vznikající síť UMTS. T-TAF zajišťuje, že data z terminálu mohou být efektivně a spolehlivě přenášena přes rozhraní vzduchem a jádrem sítě, čímž umožňuje širokou škálu telekomunikačních služeb.

## K čemu slouží

T-TAF byla vytvořena, aby řešila potřebu standardizované adaptace dat mezi různorodým terminálovým zařízením a infrastrukturou sítě 3GPP. V počátcích sítí 3G (UMTS) bylo třeba podporovat nejen hlas, ale také různé datové služby zděděné ze systémů 2G, jako je fax a data s přepojováním okruhů. Tyto služby měly specifické požadavky na protokoly, které nebyly nativně kompatibilní s novými rádiovými a jádrovými síťovými protokoly UMTS. T-TAF poskytuje definovanou funkci pro zvládnutí této kompatibility, čímž zajišťuje, že terminály mohly nabízet konzistentní sadu služeb bez ohledu na vývoj podkladové sítě.

Historicky by bez standardizované adaptační funkce výrobci terminálů a síťoví operátoři čelili problémům s interoperabilitou, což by vedlo k fragmentované podpoře služeb. T-TAF, jak je specifikována v 3GPP TS 23.146, stanovila společný přístup k převodu protokolů, což usnadnilo migraci datových služeb do ekosystému 3G. Řešila problém integrace starších datových aplikací s novými možnostmi UMTS orientovanými na pakety i přepojování okruhů, čímž chránila investice do stávajících aplikací terminálů a zároveň umožnila přechod k pokročilejším sítím.

## Klíčové vlastnosti

- Převod protokolů pro datové služby
- Adaptace dat z terminálu do síťových přenosových formátů
- Podpora dat s přepojováním okruhů i paketů
- Adaptace rychlosti a řízení toku
- Řízení chyb a správa integrity dat
- Interoperabilita mezi terminály a síťovou infrastrukturou

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [T-TAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-taf/)
