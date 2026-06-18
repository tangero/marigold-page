---
slug: "nplr"
url: "/mobilnisite/slovnik/nplr/"
type: "slovnik"
title: "NPLR – Number Portability Location Register"
date: 2025-01-01
abbr: "NPLR"
fullName: "Number Portability Location Register"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nplr/"
summary: "Databáze v jádrové síti, která ukládá směrovací informace pro mobilní čísla, jež byla přenesena mezi operátory. Umožňuje směrování hovorů do správné sítě, když účastník změnil poskytovatele služeb, al"
---

NPLR je databáze v jádrové síti, která ukládá směrovací informace pro přenesená mobilní čísla, což umožňuje správné směrování hovorů, když účastník změní poskytovatele služeb, ale ponechá si své telefonní číslo.

## Popis

Number Portability Location Register (NPLR) je klíčová funkční entita v architektuře jádrové sítě 3GPP, specificky definovaná pro podporu přenositelnosti mobilních čísel (Mobile Number Portability, [MNP](/mobilnisite/slovnik/mnp/)). Funguje jako centralizovaná nebo distribuovaná databáze, která uchovává mapování mezi přeneseným mobilním číslem účastníka (Mobile Station International Subscriber Directory Number, [MSISDN](/mobilnisite/slovnik/msisdn/)) a identitou sítě (sítě příjemce), ke které bylo číslo přeneseno. Když účastník změní operátora, ale ponechá si telefonní číslo, jeho MSISDN již není spojeno s domovským registrem (Home Location Register, [HLR](/mobilnisite/slovnik/hlr/)) jeho původní domovské sítě. NPLR poskytuje nezbytnou inteligenci pro správné směrování hovorů a zpráv.

Architektonicky NPLR komunikuje s dalšími prvky jádrové sítě, jako je Gateway Mobile Switching Center ([GMSC](/mobilnisite/slovnik/gmsc/)) nebo jádro IP Multimedia Subsystem (IMS). Když je uskutečněn hovor na přenesené číslo, GMSC volající sítě provede dotaz, typicky pomocí mechanismu založeného na [ENUM](/mobilnisite/slovnik/enum/) nebo Signalizačním systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), aby zjistil, zda je číslo přeneseno. Pokud ano, je dotaz směrován do NPLR (nebo do centralizované databáze přenositelnosti čísel, která může být považována za synonymní). NPLR odpoví směrovacím číslem (např. Mobile Network Code, [MNC](/mobilnisite/slovnik/mnc/) nebo specifickým směrovacím prefixem), které identifikuje síť příjemce. Tyto směrovací informace jsou pak použity k předání hovoru do brány správné sítě pro konečné doručení účastníkovi.

Jeho role je čistě pro řešení směrování; nezpracovává autentizaci účastníka, servisní profily ani správu relací. Provoz NPLR je pro koncového uživatele transparentní, ale je zásadní pro dodržování regulací a plynulou kontinuitu služeb v konkurenčních telekomunikačních trzích. Odděluje identitu účastníka (MSISDN) od identity síťové infrastruktury, což umožňuje skutečnou přenositelnost čísel.

## K čemu slouží

NPLR byl vytvořen, aby vyřešil základní problém zavedený přenositelností mobilních čísel (Mobile Number Portability, [MNP](/mobilnisite/slovnik/mnp/)): jak směrovat hovor k účastníkovi, který změnil síťového operátora, ale ponechal si své telefonní číslo. Před MNP obsahovalo MSISDN vnořené směrovací informace (kódy země a sítě). Hovor byl směrován do sítě identifikované těmito kódy, která pak použila svůj HLR k lokalizaci účastníka. Když je číslo přeneseno, toto inherentní směrování selže, protože původní síťový kód čísla již neukazuje na skutečnou síť, která účastníka obsluhuje.

Primární motivací byly regulační důvody, poháněné vládními politikami na zvýšení tržní konkurence snížením bariér pro účastníky při změně operátora. Bez technického řešení, jako je NPLR, by na přenesená čísla nebylo možné dovolat, což by popřelo výhody přenositelnosti. NPLR poskytuje nezbytnou vyhledávací službu, která přeloží přenesené MSISDN na správný identifikátor cílové sítě, čímž řeší problém směrování hovorů. Řešil omezení architektury z doby před přenositelností, kde bylo směrování staticky určeno rozsahy čísel přiřazenými operátorům, a umožnil dynamický, na dotazech založený směrovací mechanismus, který je nezbytný pro moderní, konkurenční telekomunikační ekosystém.

## Klíčové vlastnosti

- Ukládá mapování mezi přenesenými MSISDN a identifikátory sítě příjemce
- Poskytuje rozhraní dotaz/odpověď pro řešení směrování (např. přes SS7 nebo IP)
- Umožňuje dodržování regulací pro přenositelnost mobilních čísel (Mobile Number Portability, MNP)
- Spolupracuje s GMSC a HLR při směrování hovorů
- Možnosti centralizovaného nebo distribuovaného architektonického nasazení
- Podporuje směrování hlasu i SMS pro přenesená čísla

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [NPLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nplr/)
