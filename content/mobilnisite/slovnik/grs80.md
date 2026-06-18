---
slug: "grs80"
url: "/mobilnisite/slovnik/grs80/"
type: "slovnik"
title: "GRS80 – Geodetic Reference System 1980"
date: 2025-01-01
abbr: "GRS80"
fullName: "Geodetic Reference System 1980"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/grs80/"
summary: "GRS80 je globální geodetický referenční systém definující tvar Země a její gravitační pole. V 3GPP je standardním modelem elipsoidu používaným pro převod geografických souřadnic (zeměpisná šířka/délka"
---

GRS80 je standardní globální geodetický referenční systém a model elipsoidu používaný v 3GPP pro převod geografických souřadnic na kartézské souřadnice se středem v Zemi a pevně spojené se Zemí (Earth-Centered, Earth-Fixed).

## Popis

Geodetický referenční systém 1980 (GRS80) je globální datum poskytující standardizovaný matematický model tvaru Země a jejího gravitačního pole. Definuje referenční elipsoid – zploštělý sféroid aproximující střední hladinu světového oceánu – se specifickými definičními parametry včetně poloosy hlavní (rovníkový poloměr) a faktoru zploštění. Ve specifikacích 3GPP pro určování polohy (např. TS 36.305 pro LTE, TS 38.305 pro NR) je GRS80 nařízen jako standardní elipsoid, který má být použit pro všechny převody souřadnic mezi geografickými (elipsoidními) souřadnicemi a kartézskými souřadnicemi se středem v Zemi a pevně spojenými se Zemí ([ECEF](/mobilnisite/slovnik/ecef/)).

V rámci služeb lokalizace 3GPP je poloha zařízení často určována a hlášena pomocí geografických souřadnic (zeměpisná šířka, délka a nadmořská výška vztažená k elipsoidu). Pro mnohé geometrické výpočty, jako je výpočet vzdáleností mezi body nebo pro některé metody určování polohy, jako je pozorovaný časový rozdíl příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)), však musí být souřadnice převedeny do trojrozměrného kartézského systému (X, Y, Z), jehož počátek je v těžišti Země. Elipsoid GRS80 poskytuje nezbytné parametry (hlavní poloosa 'a' a zploštění 'f') pro provedení tohoto přesného převodu. Vzorce zahrnují trigonometrické transformace, které zohledňují zploštění Země.

Úlohou GRS80 je zajistit konzistenci a interoperabilitu napříč všemi síťovými prvky a uživatelskými zařízeními zapojenými do určování polohy. Když funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v 5G nebo rozšířené středisko správy polohy mobilních účastníků ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE vypočítává polohu nebo když uživatelské zařízení (UE) hlásí svou polohu, je kritické používat stejný referenční elipsoid. Použití různých dat (jako staršího WGS72 nebo regionálních systémů) by vedlo k chybám a nekonzistencím v polohových datech. Standardizací na GRS80, který je pro většinu praktických účelů totožný s datem WGS84 používaným [GPS](/mobilnisite/slovnik/gps/), zajišťuje 3GPP, že informace o poloze ze sítě bezproblémově korespondují s údaji globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) a geografických informačních systémů (GIS).

## K čemu slouží

GRS80 byl přijat do specifikací 3GPP, aby vyřešil problém nekonzistence dat v mobilních službách lokalizace. Před jeho standardizací mohly různé komponenty v ekosystému určování polohy – přijímače [GNSS](/mobilnisite/slovnik/gnss/), síťové databáze, mapové aplikace – potenciálně používat různé modely Země. To by způsobilo, že stejná fyzická lokalita by měla různé souřadnicové reprezentace, což by vedlo k chybám ve službách založených na poloze, v lokalizaci volajících při nouzových voláních (E911/112) a v síťových optimalizačních funkcích, jako je geofencing.

Konkrétní motivací pro závazné zavedení GRS80, zejména od vydání 15 s vylepšeními určování polohy v 5G NR, bylo poskytnout jediný, autoritativní a globálně přijímaný geodetický referenční rámec. GRS80 je vědecky rigorózní systém přijatý Mezinárodní unií pro geodézii a geofyziku (IUGG). Jeho použití zajišťuje, že vysoká přesnost určování polohy v 5G (v některých scénářích cílená na centimetrovou úroveň) není podkopána základními chybami v modelu Země. Řeší tak omezení spočívající v absenci standardizovaného modelu nebo v použití méně přesného modelu, což by bylo nepřijatelné pro pokročilé případy užití, jako je komunikace vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)) a průmyslová automatizace IoT, které spoléhají na přesnou geolokalizaci.

Historicky tvoří GRS80 základ široce používaného datumu WGS84. Přímým odkazem na GRS80 se 3GPP sladil s moderní geodetickou vědou a zajistil dlouhodobou konzistenci. Jeho zařazení do specifikací určování polohy poskytuje jasný, jednoznačný základ pro všechny transformace souřadnic, což je nezbytné pro interoperabilitu mezi síťovými metodami určování polohy (jako UTDOA), asistovaným GNSS (A-GNSS) a senzorově založeným hybridním určováním polohy v budoucích vydáních.

## Klíčové vlastnosti

- Definuje standardní referenční elipsoid pro výpočty určování polohy v 3GPP
- Poskytuje parametry pro převod mezi geografickými (zeměp. šířka/délka/výška) a ECEF (X,Y,Z) souřadnicemi
- Zajišťuje konzistenci s moderními systémy GNSS, jako je GPS, které používají kompatibilní datum WGS84
- Kritický pro techniky vysoké přesnosti určování polohy v LTE a 5G NR
- Podporuje interoperabilitu polohových dat napříč síťovými prvky a uživatelskými zařízeními
- Tvoří geodetický základ pro lokalizaci v nouzových službách a pokročilé služby založené na poloze

## Související pojmy

- [ECEF – Earth-Centered, Earth-Fixed](/mobilnisite/slovnik/ecef/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [GRS80 na 3GPP Explorer](https://3gpp-explorer.com/glossary/grs80/)
