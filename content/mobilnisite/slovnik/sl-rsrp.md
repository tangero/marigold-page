---
slug: "sl-rsrp"
url: "/mobilnisite/slovnik/sl-rsrp/"
type: "slovnik"
title: "SL-RSRP – Sidelink Reference Signal Received Power"
date: 2026-01-01
abbr: "SL-RSRP"
fullName: "Sidelink Reference Signal Received Power"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sl-rsrp/"
summary: "Měření úrovně přijatého výkonu referenčních signálů postranního spoje z jiného uživatelského zařízení (UE). Používá se pro odhad kvality kanálu postranního spoje, správu paprsků a rozhodování o výběru"
---

SL-RSRP je měření úrovně přijatého výkonu referenčních signálů postranního spoje (sidelink) z jiného uživatelského zařízení (UE), používané pro odhad kvality kanálu postranního spoje, správu paprsků a výběr zdrojů v přímé komunikaci mezi zařízeními.

## Popis

SL-RSRP je měření fyzické vrstvy definované pro NR a vyvinutý LTE postranní spoj, analogické měření [RSRP](/mobilnisite/slovnik/rsrp/) pro downlink na rozhraní Uu, ale aplikované na rozhraní PC5. Kvantifikuje průměrný přijatý výkon prvků zdroje, které nesou referenční signály specifické pro postranní spoj, jako je Demodulační referenční signál ([DM-RS](/mobilnisite/slovnik/dm-rs/)) uvnitř Fyzického sdíleného kanálu postranního spoje ([PSSCH](/mobilnisite/slovnik/pssch/)) nebo Referenční signál pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) nakonfigurovaný pro postranní spoj. Měření provádí přijímající UE na signálech vysílaných partnerským UE, typicky přes nakonfigurovanou sadu měřicích zdrojů. UE filtruje měření v čase a frekvenci, aby vytvořila spolehlivý odhad, který je hlášen v dBm. Toto měření je klíčové pro několik procedur postranního spoje. Pro správu paprsků v NR postranním spoji, zejména na vyšších frekvencích, se měření SL-RSRP na různých párech paprsků používají k výběru optimálního vysílacího a přijímacího paprsku, což je proces známý jako zjemnění paprsku. Při přidělování zdrojů, zejména pro autonomní režimy výběru zdrojů (např. Režim 2), UE snímá kanál a měří SL-RSRP z přenosů jiných UE. Pokud je naměřené SL-RSRP pro daný zdroj nad nakonfigurovaným prahem, UE považuje tento zdroj za obsazený nebo rezervovaný sousedem způsobujícím vysoké rušení a vyloučí jej z vlastní sady kandidátních zdrojů, čímž implementuje algoritmus semi-persistentního plánování ([SPS](/mobilnisite/slovnik/sps/)) založený na snímání. Dále SL-RSRP slouží jako vstup pro algoritmy řízení výkonu, pomáhající UE upravit jejich vysílací výkon k udržení cílového přijatého výkonu na přijímači, čímž se optimalizuje rušení a životnost baterie. Přesnost a mechanismy hlášení pro SL-RSRP jsou specifikovány podrobně, aby byla zajištěna interoperabilita a spolehlivý výkon postranního spoje.

## K čemu slouží

SL-RSRP bylo zavedeno, aby poskytlo standardizovanou, kvantifikovatelnou metriku pro hodnocení kvality přímého rádiového spoje mezi uživatelskými zařízeními (UE), což byla schopnost chybějící v raných specifikacích postranního spoje. Počáteční verze [D2D](/mobilnisite/slovnik/d2d/) a [V2X](/mobilnisite/slovnik/v2x/) se zaměřovaly na základní konektivitu bez sofistikované adaptace spoje nebo výběru zdrojů s ohledem na rušení. Jak se případy užití postranního spoje rozšířily o pokročilé V2X vyžadující ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a NR postranní spoj pracující v pásmech mmWave, potřeba přesných informací o stavu kanálu se stala prvořadou. SL-RSRP to řeší tím, že umožňuje UE měřit sílu spoje, což je zásadní pro několik klíčových funkcí: umožňuje efektivní správu paprsků pro směrovou komunikaci ve vysokofrekvenčním NR postranním spoji, nahrazující jednodušší předpoklady všesměrovosti LTE postranního spoje; usnadňuje inteligentní výběr zdrojů s ohledem na rušení v autonomních režimech, což snižuje kolize paketů a zlepšuje spolehlivost v hustých scénářích; a podporuje uzavřenou smyčku řízení výkonu pro minimalizaci rušení a úsporu baterie UE. V podstatě přináší vyspělé paradigma měření a správy kanálu z buněčného spoje Uu do domény komunikace mezi zařízeními, což je nezbytné pro dosažení výkonnostních cílů pokročilého V2X, veřejné bezpečnosti a komerčních D2D aplikací.

## Klíčové vlastnosti

- Měření přijatého výkonu z referenčních signálů postranního spoje (např. DM-RS, CSI-RS)
- Základní pro procedury správy paprsků a výběru paprsku v postranním spoji
- Klíčový vstup pro algoritmy autonomního výběru zdrojů založené na snímání (Režim 2)
- Používá se pro řízení výkonu postranního spoje k optimalizaci rušení a spotřeby energie
- Podporuje rozhraní přenosu jak pro LTE, tak pro NR postranní spoj
- Umožňuje odhad kvality spoje pro rozhodování o mobilitě a předávání v postranním spoji

## Související pojmy

- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)

## Definující specifikace

- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [SL-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-rsrp/)
