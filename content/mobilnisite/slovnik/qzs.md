---
slug: "qzs"
url: "/mobilnisite/slovnik/qzs/"
type: "slovnik"
title: "QZS – Quasi-Zenith Satellite"
date: 2025-01-01
abbr: "QZS"
fullName: "Quasi-Zenith Satellite"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/qzs/"
summary: "Satelit v japonské konstelaci systému Quasi-Zenith Satellite System (QZSS). Následuje vysoce eliptickou dráhu navrženou tak, aby zůstával po delší dobu poblíž zenitu (přímo v nadhlavníku) nad Japonske"
---

QZS je satelit v japonském systému Quasi-Zenith Satellite System, který využívá vysoce eliptickou dráhu, aby zůstal téměř v nadhlavníku, čímž zlepšuje dostupnost a přesnost GNSS pro mobilní sítě v náročném terénu.

## Popis

Quasi-Zenith Satellite (QZS) je klíčovou součástí japonského regionálního systému pro augmentaci satelitní navigace. Na rozdíl od tradičních geostacionárních satelitů operují satelity QZS na vysoce skloněných eliptických drahách známých jako Quasi-Zenith Orbits (QZO). Tato specifická orbitální geometrie zajišťuje, že alespoň jeden satelit je po přibližně 8 hodin denně umístěn téměř v nadhlavníku (pod vysokým elevančním úhlem) nad Japonskem a regionem Asie a Oceánie. Tento vysoký elevanční úhel je klíčový, protože výrazně snižuje blokování signálu budovami, horami a dalšími překážkami ve srovnání se satelity níže na horizontu, což je častý problém v městských kaňonech.

Z pohledu 3GPP jsou satelity QZS integrovány do mobilních sítí primárně za účelem poskytování vylepšených polohovacích dat. Vysílají standardní signály kompatibilní s globálním polohovacím systémem ([GPS](/mobilnisite/slovnik/gps/)) (L1C/A, L1C, L2C, L5) a také jedinečné japonské augmentační signály (L1S, L5S, L6). Tyto augmentační signály nesou korekční data a informace o integritě za účelem zlepšení přesnosti, dostupnosti a spolehlivosti polohovacích služeb pro uživatelské zařízení (UE). Systém je navržen tak, aby bezproblémově spolupracoval s dalšími globálními navigačními satelitními systémy ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou GPS, Galileo a BeiDou.

V architektuře 3GPP je podpora QZS definována v rámci protokolů pro Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Síť může poskytnout asistenční data pro UE, která zahrnují přesné orbitální informace (efemeridy) a korekční data hodin pro satelity QZS, čímž se zkracuje doba do prvního určení polohy a zlepšuje se citlivost polohování. Specifikace podrobně popisují formáty zpráv a procedury pro příjem a využití signálů QZS ze strany UE, a to samostatně nebo v kombinaci s jinými konstelacemi GNSS. Tato integrace umožňuje mobilním operátorům nabízet vysoce přesné služby založené na poloze, určení polohy volajícího v nouzových případech a další aplikace závislé na přesném polohování.

## K čemu slouží

Systém Quasi-Zenith Satellite byl vytvořen, aby řešil významná omezení tradičních [GNSS](/mobilnisite/slovnik/gnss/), zejména [GPS](/mobilnisite/slovnik/gps/), ve specifickém geografickém a městském prostředí Japonska. Topografie Japonska zahrnuje hustá městská centra s mrakodrapy vytvářejícími hluboké 'městské kaňony' a hornaté oblasti, které často blokují signály od satelitů poblíž horizontu. Standardní konstelace GNSS v těchto podmínkách často neposkytují dostatečnou viditelnost satelitů, což vede ke snížené přesnosti, dlouhým časům určení polohy nebo k úplnému výpadku služby.

Historicky představovala závislost pouze na GPS výzvy pro kritické aplikace v Japonsku, včetně vozidlové navigace, řízení katastrof a precizního zemědělství. Koncept QZS byl vyvinut, aby poskytl regionální augmentaci a doplněk ke globálním systémům. Tím, že zajišťuje téměř stálou přítomnost satelitu poblíž zenitu nad Japonskem, systém garantuje silný, neblokovaný zdroj signálu. To přímo řeší problém dostupnosti signálu. Dále [QZSS](/mobilnisite/slovnik/qzss/) vysílá augmentační signály, které poskytují korekční data, čímž zlepšují přesnost polohy z úrovně metrů na úroveň centimetrů pro autorizované služby, a informace o integritě, které uživatele upozorní, pokud by systém neměl být používán pro aplikace související s bezpečností života. Jeho vývoj byl motivován národními požadavky na odolnou infrastrukturu pro vysokopřesné polohování nezávislou na výhradní závislosti na zahraničních systémech GNSS.

## Klíčové vlastnosti

- Operuje na Quasi-Zenith Orbit (QZO), což zajišťuje vysoké elevanční úhly nad Japonskem
- Vysílá signály kompatibilní s GPS (L1C/A, L2C, L5) pro interoperabilitu
- Vysílá jedinečné augmentační signály (L1S, L5S, L6) pro korekční data a data o integritě
- Zvyšuje dostupnost GNSS v městských kaňonech a náročném prostředí
- Poskytuje funkci Satellite-Based Augmentation System (SBAS) pro region Asie a Oceánie
- Integrován do standardů 3GPP pro Assisted GNSS (A-GNSS) polohování

## Související pojmy

- [QZSS – Quasi-Zenith Satellite System](/mobilnisite/slovnik/qzss/)
- [QZST – Quasi-Zenith System Time](/mobilnisite/slovnik/qzst/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [QZS na 3GPP Explorer](https://3gpp-explorer.com/glossary/qzs/)
