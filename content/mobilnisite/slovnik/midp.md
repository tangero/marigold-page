---
slug: "midp"
url: "/mobilnisite/slovnik/midp/"
type: "slovnik"
title: "MIDP – Mobile Information Device Profile"
date: 2025-01-01
abbr: "MIDP"
fullName: "Mobile Information Device Profile"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/midp/"
summary: "Profil J2ME definující API pro mobilní zařízení, jako jsou telefony a PDA, umožňující standardizovaný vývoj aplikací. Poskytuje konzistentní prostředí pro funkce jako uživatelské rozhraní, síťování a"
---

MIDP je profil J2ME, který definuje standardizovaná API pro mobilní zařízení, umožňující konzistentní vývoj aplikací s funkcemi pro uživatelské rozhraní, síťování a trvalé ukládání dat.

## Popis

Mobile Information Device Profile (MIDP) je specifikace pro platformu Java 2 Platform, Micro Edition ([J2ME](/mobilnisite/slovnik/j2me/)). Definuje sadu Java [API](/mobilnisite/slovnik/api/) a běhové prostředí přizpůsobené pro mobilní informační zařízení, především mobilní telefony a osobní digitální asistenty (PDA). MIDP staví na Connected Limited Device Configuration ([CLDC](/mobilnisite/slovnik/cldc/)), která poskytuje jádro Java runtime pro zařízení s omezenými prostředky. Společně CLDC a MIDP tvoří kompletní aplikační platformu, umožňující vývojářům vytvářet přenositelné, síťově orientované aplikace známé jako MIDlety.

Architektonicky MIDP leží nad vrstvou CLDC, která sama běží na nativním operačním systému zařízení. Specifikace MIDP standardizuje několik klíčových oblastí: API uživatelského rozhraní pro vytváření grafických displejů a zpracování vstupních událostí; síťové API založené na Generic Connection Framework ([GCF](/mobilnisite/slovnik/gcf/)) pro [HTTP](/mobilnisite/slovnik/http/) a další protokoly; mechanismus trvalého ukládání dat (Record Management System) pro lokální data; a API pro časovače a správu životního cyklu aplikace (stavy MIDletu). Tento vrstvený přístup abstrahuje hardwarové rozdíly, což umožňuje, aby jeden MIDlet běžel na různorodých zařízeních od různých výrobců.

Při provozu je sada MIDletů (zabalena aplikace) stažena do zařízení a spravována Java Application Managerem ([JAM](/mobilnisite/slovnik/jam/)). Běhové prostředí MIDP zajišťuje vykonávání a poskytuje definovaná API, aby MIDlet mohl komunikovat s displejem zařízení, sítí a úložištěm. Jeho role v raných sítích 3GPP byla významná pro umožnění stahovatelných aplikací a služeb a tvořila předchůdce moderních mobilních obchodů s aplikacemi. Ačkoli byl z velké části nahrazen nativními platformami Android a iOS, MIDP byl zásadní pro vytvoření standardizovaného, bezpečného prostředí pro vývoj mobilních aplikací třetích stran.

## K čemu slouží

MIDP byl vytvořen, aby řešil fragmentaci v raných platformách mobilních zařízení poskytnutím standardizovaného aplikačního prostředí založeného na Javě. Před jeho zavedením byl vývoj softwaru pro mobilní telefony vysoce specifický pro výrobce a vyžadoval hlubokou integraci s proprietárními operačními systémy a hardwarem. To bránilo vývoji aplikací třetích stran a omezovalo dostupnost služeb. Iniciativa [J2ME](/mobilnisite/slovnik/j2me/), s MIDP jako klíčovým profilem, si kladla za cíl vytvořit paradigma „napiš jednou, spusť kdekoli“ pro mobilní zařízení, podobně jako Java uspěla na stolních počítačích.

Hlavním problémem, který MIDP řešil, bylo umožnění bezpečných, stahovatelných aplikací na zařízeních s omezenými prostředky, s malou pamětí, výpočetním výkonem a životností baterie. Definoval minimální, ale funkční sadu [API](/mobilnisite/slovnik/api/), kterou bylo možné implementovat na široké škále hardwaru. To umožnilo síťovým operátorům a poskytovatelům obsahu nasazovat hry, utility a obchodní aplikace pro masový trh. Jeho vytvoření bylo motivováno potřebou průmyslu posunout se za předinstalovaný, statický softwarový vybavení zařízení a odemknout hodnotu mobilních datových služeb vedle hlasové komunikace.

Historický kontext řadí zavedení MIDP do 3GPP Release 5 spolu s ranými nasazeními 3G/UMTS. Řešil omezení proprietárních platforem a dřívějších, omezenějších služeb založených na mikroprohlížečích (jako WAP). Tím, že poskytoval skutečné aplikační běhové prostředí, umožnil interaktivnější a schopnější služby a připravil cestu pro následný ekosystém mobilních dat. Jeho specifikace byly udržovány napříč mnoha vydáními 3GPP, aby byla zajištěna zpětná kompatibilita a postupné vylepšování s rostoucími schopnostmi zařízení.

## Klíčové vlastnosti

- Standardizované API uživatelského rozhraní pro displeje a vstup
- Síťové API podporující HTTP, HTTPS, sokety a datagramy
- Trvalé ukládání dat prostřednictvím Record Management System (RMS)
- Model životního cyklu aplikace definovaný stavy MIDletu (Pozastavený, Aktivní, Zničený)
- Bezpečnostní model pro řízení přístupu k síti a souborovému systému
- Provisioning přes vzdušné rozhraní (OTA) pro stahování a instalaci sad MIDletů

## Související pojmy

- [J2ME – Java 2 Platform, Micro Edition](/mobilnisite/slovnik/j2me/)
- [CLDC – Connected Limited Device Configuration](/mobilnisite/slovnik/cldc/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [MIDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/midp/)
