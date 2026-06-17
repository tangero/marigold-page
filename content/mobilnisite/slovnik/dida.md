---
slug: "dida"
url: "/mobilnisite/slovnik/dida/"
type: "slovnik"
title: "DIDA – Data IDentification in ANDSF"
date: 2025-01-01
abbr: "DIDA"
fullName: "Data IDentification in ANDSF"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dida/"
summary: "Mechanismus v rámci ANDSF pro identifikaci konkrétních datových toků nebo aplikací. Umožňuje síťovým operátorům poskytovat pokyny pro směrování a směrování provozu založené na politikách a přizpůsoben"
---

DIDA je mechanismus ANDSF pro identifikaci konkrétních datových toků nebo aplikací, který umožňuje poskytovat pokyny pro směrování a směrování provozu založené na politikách a přizpůsobené jednotlivým typům dat.

## Popis

DIDA (Data IDentification in [ANDSF](/mobilnisite/slovnik/andsf/)) je funkční komponenta integrovaná do rámce Access Network Discovery and Selection Function (ANDSF) definovaného ve 3GPP Release 11 a následujících verzích. Jejím hlavním úkolem je poskytovat detailní identifikační mechanismus pro datové toky nebo konkrétní aplikace procházející uživatelským zařízením (UE). DIDA funguje definováním pravidel pro identifikaci dat a kontejnerů v rámci objektů správy ([MO](/mobilnisite/slovnik/mo/)) ANDSF. Tato pravidla mohou být založena na různých deskriptorech toku paketů, jako jsou cílové IP adresy, čísla portů, typy protokolů nebo identifikátory aplikací (např. z hloubkové inspekce paketů nebo signálů poskytovaných operačním systémem). Server ANDSF, typicky provozovaný poskytovatelem sítě, může tyto politiky DIDA zřídit pro UE přes rozhraní S14.

Když UE přijme politiky DIDA, jeho klient ANDSF je uloží a interpretuje. Jak aplikace generují datové pakety, bod vynucení politik v UE porovnává tyto pakety s aktivními pravidly DIDA. Úspěšná shoda spojí datový tok s konkrétním identifikátorem DIDA. Tento identifikátor se nepoužívá přímo pro směrování, ale slouží jako klíč. Hlavní funkcí DIDA je působit jako selektor pro další politiky ANDSF, konkrétně [ISRP](/mobilnisite/slovnik/isrp/) (Inter-System Routing Policy) a [IARP](/mobilnisite/slovnik/iarp/) (Inter-APN Routing Policy). Tyto směrovací politiky lze nakonfigurovat tak, aby se vztahovaly pouze na datové toky označené konkrétním identifikátorem DIDA.

Z architektonického hlediska DIDA zavádí nové uzly ve stromu objektů správy ANDSF, konkrétně prvky `<DIDARule>` a `<DIDAContainer>`. `<DIDARule>` obsahuje skutečná kritéria pro shodu (jako šablona toku provozu), zatímco `<DIDAContainer>` seskupuje více pravidel a přiřazuje jedinečné ID DIDA. Tato hierarchická struktura umožňuje složitou identifikaci s více kritérii. Proces je nedílnou součástí směrování provozu založeného na politikách a umožňuje scénáře, kde je například veškerý provoz pro streamování videa (identifikovaný pomocí DIDA) směrován na Wi-Fi síť, zatímco provoz citlivý na latenci (např. hraní her) zůstává na buněčném spojení, i když oba pocházejí ze stejného bloku IP adres.

Úloha DIDA v síti spočívá v umožnění inteligentního výběru přístupu a správy provozu. Tím, že přesahuje směrování na úrovni sítě nebo [APN](/mobilnisite/slovnik/apn/), umožňuje operátorům implementovat politiky s ohledem na služby. Tato podrobnost pomáhá optimalizovat využití síťových zdrojů, řídit přetížení a implementovat služebně specifické účtování nebo zacházení z hlediska kvality služeb. Tvoří základní kámen pro pozdější vylepšení v oblasti vícepřístupové konektivity a bezproblémového odlehčování, neboť poskytuje nezbytnou 'datovou informovanost' pro sofistikovaná rozhodnutí řízená ANDSF.

## K čemu slouží

DIDA byla zavedena, aby řešila rostoucí potřebu detailního, na aplikace zaměřeného směrování provozu v heterogenních sítích (HetNets). Před Release 11 politiky [ANDSF](/mobilnisite/slovnik/andsf/) fungovaly primárně na široké úrovni, směrujíce veškerý provoz z UE nebo veškerý provoz spojený s konkrétním Access Point Name ([APN](/mobilnisite/slovnik/apn/)) k určité přístupové síti (např. Wi-Fi nebo 3GPP). Tato hrubá granularita byla nedostatečná s rozšířením chytrých telefonů a tím, že se uživatelský provoz stal směsí různorodých aplikací s velmi odlišnými požadavky (např. streamování videa, VoIP, prohlížení webu, aktualizace softwaru). Operátoři neměli nástroj k rozlišení těchto toků a aplikaci odlišných směrovacích politik.

Vytvoření DIDA bylo motivováno snahou implementovat výběr sítě a odlehčování založené na službách. Bez DIDA neměl operátor, který chtěl odlehčit pouze video provoz na doplňkovou Wi-Fi síť, zatímco hlasové hovory ponechat v buněčné síti, standardizovaný způsob, jak identifikovat tok 'video provozu' v rámci ANDSF. DIDA toto vyřešila poskytnutím standardizovaného kontejneru pro kritéria identifikace toku, který může být dynamicky zřizován. Řešila omezení předchozích, nestandardizovaných nebo proprietárních řešení hloubkové inspekce paketů (DPI) zabudovaných v síti, která byla složitá, nákladná a často vyvolávala obavy o soukromí. DIDA přesunula inteligenci a logiku porovnávání na stranu UE na základě pravidel poskytovaných operátorem, čímž vytvořila škálovatelnější a soukromí respektující model.

Historicky se vývoj DIDA shodoval s posunem průmyslu směrem k inteligentní správě provozu a raným konceptům síťového dělení a architektur s ohledem na služby. Poskytla základní 'filtrovací' mechanismus, který umožnil ANDSF vyvinout se z jednoduchého nástroje pro objevování přístupu ve sofistikovaný motor politik pro Multi-Access PDN Connectivity ([MAPCON](/mobilnisite/slovnik/mapcon/)) a později IP Flow Mobility (IFOM). Tím, že vyřešila problém identifikace dat, DIDA odemkla potenciál pro skutečně dynamické, politikami řízené vícepřístupové sítě a připravila cestu pro bezproblémovou integraci nepřístupů 3GPP, jak je koncipováno v 5G.

## Klíčové vlastnosti

- Definuje standardizovaná pravidla pro identifikaci konkrétních datových toků nebo aplikací na straně UE.
- Používá šablony toku provozu (podobné TFT) s kritérii shody, jako jsou IP adresa, port a protokol.
- Poskytuje hierarchickou strukturu s DIDARules a DIDAContainers pro organizovanou správu politik.
- Slouží jako selektorový klíč pro Inter-System Routing Policy (ISRP) a Inter-APN Routing Policy (IARP).
- Umožňuje směrování provozu s ohledem na aplikaci nebo službu napříč 3GPP a nepřístupy 3GPP.
- Podporuje dynamické zřizování a aktualizaci ze serveru ANDSF na UE přes referenční bod S14.

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [ISRP – Inter-System Routing Policies](/mobilnisite/slovnik/isrp/)
- [IARP – Inter-APN Routing Policy](/mobilnisite/slovnik/iarp/)

## Definující specifikace

- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification

---

📖 **Anglický originál a plná specifikace:** [DIDA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dida/)
