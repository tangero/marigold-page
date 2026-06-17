---
slug: "gl"
url: "/mobilnisite/slovnik/gl/"
type: "slovnik"
title: "GL – Group Length"
date: 2025-01-01
abbr: "GL"
fullName: "Group Length"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gl/"
summary: "Pole používané ve specifikacích protokolových vrstev 3GPP, zejména pro protokoly vrstvy 2 (L2), jako jsou PDCP a RLC, k označení celkové délky protokolové datové jednotky (PDU) nebo specifické skupiny"
---

GL je pole ve specifikacích protokolů vrstvy 2 (Layer 2) 3GPP, které udává celkovou délku protokolové datové jednotky nebo specifické skupiny dat pro správnou analýzu (parsování) struktur s proměnnou délkou.

## Popis

Group Length (GL) je základním konceptem v návrhu protokolů 3GPP, konkrétně ve specifikaci protokolů linkové vrstvy (Layer 2) v rádiové přístupové síti. Jeho formální definice je uvedena v technických specifikacích, jako je TS 37.462, která se zabývá aspekty protokolů napříč různými rádiovými přístupovými technologiemi. GL je pole zabudované v hlavičce nebo podhlavičce protokolové datové jednotky (PDU). Jeho hodnota představuje celkovou délku (typicky v bajtech nebo bitech) následující skupiny dat, což může být sada polí, subPDU nebo specifický informační prvek.

Během provozu, když přijímající entita (např. PDCP nebo RLC entita v UE nebo gNB) zpracovává příchozí PDU, přečte pole GL, aby určila, kolik oktetů má vyčíst pro přidruženou skupinu. To umožňuje protokolu efektivně zpracovávat komponenty s proměnnou délkou bez nutnosti pevných, předem definovaných délek pro všechny prvky. Logika analýzy je sekvenční: přečte se typ nebo identifikátor pole, přečte se přidružená hodnota GL a poté se přeskočí dopředu o počet bajtů udaný hodnotou GL, aby se dosáhlo začátku další skupiny. Tento mechanismus je klíčový pro rozšiřitelnost, protože nová pole nebo informační prvky mohou být v pozdějších verzích přidány do formátu PDU bez narušení zpětné kompatibility – starší přijímače mohou jednoduše přeskočit neznámé skupiny pomocí jejich hodnot GL.

Architektura protokolů používajících GL často zahrnuje strukturu typu TLV (Type-Length-Value) nebo LTV (Length-Type-Value), kde 'L' odpovídá Group Length. Například v datové PDU Protokolu konvergence paketových dat (PDCP) pro 5G NR mohou být určité řídicí informace nebo kontejnery protokolu adaptace dat služby (SDAP) přenášeny pomocí takových skupinových formátů. GL zajišťuje, že přijímač může přesně vymezit hranice mezi více řetězcovými skupinami v rámci jedné PDU, čímž zabraňuje nesprávnému zarovnání, které by mohlo vést k protokolovým chybám nebo poškození dat.

Jeho role je základní pro flexibilitu a robustnost vrstvového návrhu protokolů 3GPP. Abstrakcí indikace délky do obecného konceptu 'Group Length' mohou tvůrci specifikací vytvářet složité, složené PDU, které přenášejí různé typy informací (např. uživatelská data, řídicí zpětná vazba, bezpečnostní hlavičky) v jedné přenosové jednotce. Tím se optimalizuje režie a efektivita zpracování na rádiovém rozhraní, což je klíčové pro splnění požadavků moderních mobilních systémů od LTE po 5G NR na vysokou propustnost a nízkou latenci.

## K čemu slouží

Pole Group Length existuje, aby vyřešilo základní problém návrhu protokolů – efektivní kódování datových prvků s proměnnou délkou a volitelných prvků v rámci pevné nebo semi-pevné struktury PDU. Rané komunikační protokoly často používaly pole s pevnou délkou, která byla jednoduchá na analýzu, ale plýtvala přenosovou kapacitou, když informace nebyla přítomna nebo byla kratší než přidělený prostor. Alternativně použití oddělujících znaků bylo nevhodné pro binární protokoly, kde se v datech může vyskytnout jakákoli hodnota bajtu.

Přijetí přístupu s indikací délky, jehož příkladem je GL, bylo motivováno potřebou flexibilnějšího a efektivnějšího kódovacího schématu. Umožňuje návrhářům protokolů definovat PDU, které se mohou přizpůsobit různým požadavkům služeb, přenášet volitelná rozšíření pro budoucí funkce a minimalizovat režii tím, že alokují prostor pouze pro skutečně přítomné informace. To je obzvláště důležité na rádiovém rozhraní, kde je spektrální efektivita prvořadá.

Historicky jsou koncepty jako TLV rozšířené v telekomunikacích a síťování (např. ASN.1 [BER](/mobilnisite/slovnik/ber/)). Formální definice GL v dokumentech 3GPP, jako je TS 37.462, poskytuje standardizovanou interpretaci a zajišťuje konzistentní implementaci napříč všemi protokoly vrstvy 2 (PDCP, RLC, [MAC](/mobilnisite/slovnik/mac/)) a napříč různými RAT ([E-UTRA](/mobilnisite/slovnik/e-utra/), NR). Řeší omezení rigidních formátů PDU, umožňuje vývoj protokolů přes více verzí 3GPP při zachování zpětné kompatibility, protože nové 'skupiny' mohou být přidány a starší zařízení je mohou bezpečně ignorovat pomocí hodnoty GL pro jejich přeskočení.

## Klíčové vlastnosti

- Udává celkovou délku v bajtech následující skupiny polí nebo datových prvků
- Umožňuje analýzu (parsování) protokolových komponent s proměnnou délkou a volitelných komponent
- Základní prvek pro struktury typu TLV používané ve formátech PDU vrstvy 2 3GPP
- Podporuje rozšiřitelnost protokolů a zpětnou kompatibilitu
- Používá se napříč více RAT (LTE, NR) a protokoly vrstvy 2 (PDCP, RLC)
- Snižuje režii protokolu tím, že se vyhýbá výplni (padding) pro pole s pevnou délkou

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [GL na 3GPP Explorer](https://3gpp-explorer.com/glossary/gl/)
