---
slug: "randms"
url: "/mobilnisite/slovnik/randms/"
type: "slovnik"
title: "RANDMS – RANDom number for Mobile Station (USIM storage)"
date: 2025-01-01
abbr: "RANDMS"
fullName: "RANDom number for Mobile Station (USIM storage)"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/randms/"
summary: "RANDMS je náhodná výzva uložená v nevolatilní paměti USIM. Používá se jako vstup pro generování sdíleného tajného klíče (K) ve fázi personalizace USIM a pro odvozování klíčů v některých legacy GSM aut"
---

RANDMS je náhodná výzva (challenge) uložená v nevolatilní paměti USIM, která slouží jako vstup pro generování sdíleného tajného klíče při personalizaci USIM a v legacy GSM autentizaci.

## Popis

RANDMS je specifický typ parametru [RAND](/mobilnisite/slovnik/rand/) (náhodné číslo), který je trvale uložen v nevolatilní paměti modulu Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) nebo [SIM](/mobilnisite/slovnik/sim/) karty. Na rozdíl od dynamického RAND používaného ve standardním online postupu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), který se mění s každou autentizací, je RANDMS statická hodnota zapsaná do USIM během fáze jeho personalizace ve výrobě nebo při provizionování operátorem. Jeho primární technická role spočívá v tom, že slouží jako seed nebo vstupní parametr pro kryptografické procesy probíhající lokálně na kartě, konkrétně pro generování nebo odvození dlouhodobého tajného klíče (K) a pro použití v GSM-specifických algoritmech.

Nejkritičtější funkcí RANDMS je generování účastníkově specifického tajného klíče (K). Během personalizace USIM použije operátor RANDMS spolu s dalšími údaji (jako je účastníkovo [IMSI](/mobilnisite/slovnik/imsi/)) jako vstup do funkce generování klíče. Výstupem této funkce je 128bitový tajný klíč (K), který je následně bezpečně uložen na USIM. Stejný RANDMS a proces použije operátorův backend (AuC/[HSS](/mobilnisite/slovnik/hss/)) ke generování identického klíče K pro daného účastníka. Tím je zajištěna synchronizace mezi tajemstvím uloženým na kartě a tajemstvím uloženým v síťové databázi. Dále, při provozním použití pro kompatibilitu s GSM, když se UE připojí k GSM síti (používá USIM v SIM režimu), může USIM použít uloženou hodnotu RANDMS při provádění GSM algoritmů [A3](/mobilnisite/slovnik/a3/)/[A8](/mobilnisite/slovnik/a8/) ke generování GSM-specifické Signed Response (SRES) a šifrovacího klíče (Kc), čímž poskytuje zpětnou bezpečnostní kompatibilitu.

Z architektonického hlediska je RANDMS uložen v chráněném souboru (např. EF_KC) na USIM. Nepřenáší se vzduchem a není součástí standardního autentizačního vektoru vyměňovaného mezi síťovými uzly. Jeho použití je omezeno na interní kryptografické výpočty USIM. Díky tomu je základním prvkem bezpečnostního stavu karty. Utajení dlouhodobého klíče K závisí na náhodnosti a důvěrnosti RANDMS použitém k jeho vytvoření. Pokud je proces generování RANDMS chybný nebo předvídatelný, mohlo by to oslabit bezpečnost odvozeného klíče K pro všechny účastníky z dané šarže USIM.

## K čemu slouží

RANDMS byl zaveden, aby splnil konkrétní potřebu v procesu personalizace USIM a správy klíčů. Rané SIM karty měly tajný klíč (Ki pro GSM) vložen přímo, ale jak se architektura vyvíjela s USIM pro 3G, byl standardizován strukturovanější způsob odvozování klíče K z jiných parametrů. RANDMS poskytuje tento deterministický, avšak operátorem řízený vstup. Řeší problém bezpečného generování jedinečného, silného tajného klíče pro každý USIM reprodukovatelným způsobem jak vydavatelem karty, tak autentizačním centrem síťového operátora.

Jeho vytvoření bylo motivováno snahou o zvýšenou bezpečnost a flexibilitu správy klíčů během výroby karet. Namísto nutnosti přímého zacházení s vysoce citlivým hlavním klíčem K a jeho nahrávání na každou kartu může být výrobci poskytnuta šarže hodnot RANDMS a algoritmus generování klíčů. Skutečný tajný klíč K je pak vypočítán přímo na kartě pomocí RANDMS. To může přidat vrstvu bezpečnosti, protože algoritmus odvozování hlavního klíče může být oddělen od fyzické linky personalizace karet. Také umožňuje, aby byl klíč K kryptograficky svázán s konkrétním RANDMS a dalšími identifikátory karty.

Dále RANDMS podporuje mechanismy zpětné kompatibility. Když je USIM pro 3G/4G použit v 2G GSM síti, může síť použít GSM autentizační výzvu (RAND_GSM). USIM může použít svůj uložený RANDMS jako součást výpočtu pro generování GSM-specifických SRES a Kc, čímž zajišťuje, že jediný tajný klíč K může podporovat jak UMTS/LTE AKA, tak legacy GSM autentizační algoritmy. To poskytuje uživateli bezproblémový zážitek napříč různými generacemi radiové technologie.

## Klíčové vlastnosti

- Statické náhodné číslo trvale uložené v nevolatilní paměti USIM
- Používá se jako seed parametr během personalizace USIM pro generování dlouhodobého tajného klíče (K)
- Umožňuje reprodukovatelné generování klíče K jak USIM, tak operátorovým HSS/AuC
- Může být využito ve výpočtech GSM algoritmů, když USIM pracuje v SIM režimu pro přístup k 2G
- Je uloženo v chráněném souboru (např. EF_KC) na USIM a nikdy se nepřenáší vzduchem
- Poskytuje základ pro bezpečnost správy klíčů v procesu personalizace karty

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [RAND – RANDom number (authentication parameter)](/mobilnisite/slovnik/rand/)

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [RANDMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/randms/)
