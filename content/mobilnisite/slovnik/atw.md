---
slug: "atw"
url: "/mobilnisite/slovnik/atw/"
type: "slovnik"
title: "ATW – Asynchronous Time Warping"
date: 2025-01-01
abbr: "ATW"
fullName: "Asynchronous Time Warping"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/atw/"
summary: "Asynchronous Time Warping (ATW) je technika synchronizace médií 3GPP pro aplikace rozšířené reality (XR). Kompenzuje latenci mezi pohybem a zobrazením (motion-to-photon) deformací vykreslených snímků"
---

ATW je technika synchronizace médií 3GPP pro rozšířenou realitu, která kompenzuje latenci deformací vykreslených snímků pomocí aktualizovaných polohových dat za účelem zlepšení vizuální kvality.

## Popis

Asynchronous Time Warping (ATW) je sofistikovaná softwarová technika standardizovaná v rámci 3GPP pro kompenzaci latence v službách rozšířené reality (XR) doručovaných přes sítě 5G. Funguje v rámci řetězce zpracování médií a cíleně řeší kritickou latenci mezi pohybem a zobrazením (motion-to-photon) – tedy zpoždění mezi pohybem uživatele a odpovídající aktualizací vizuálního displeje. ATW funguje tak, že vezme dříve vykreslený snímek a aplikuje na něj geometrickou transformaci (deformaci) na základě novějších, predikovaných nebo skutečných polohových dat hlavy či zařízení přijatých poté, co byl snímek původně vykreslen. Tento proces vytváří mezisnímek, který přesněji reprezentuje to, co by uživatel měl vidět v daném okamžiku, a účinně tak maskuje zpoždění vykreslování a přenosu sítě, která jsou vlastní scénářům XR vykreslovaným v cloudu/na okraji sítě.

Architektonická implementace ATW zahrnuje několik klíčových komponent v celém řetězci médií XR. Na straně generování obsahu, typicky na okrajovém aplikačním serveru nebo cloudovém rendereru, jsou snímky vykreslovány a kódovány. Systém musí také generovat a přenášet přidružená polohová metadata. Na klientském zařízení (např. XR headsetu) modul ATW přijímá proud zakódovaných snímků spolu s nepřetržitým proudem aktualizovaných polohových informací ze senzorů zařízení (gyroskopů, akcelerometrů). Jádrový algoritmus následně oddělí proces zobrazování snímků od řetězce generování snímků. Když nový snímek ze sítě pro zobrazení ještě není k dispozici, ATW přeprojektuje nejnovější dostupný snímek pomocí nejaktuálnějších polohových dat, aplikuje 2D nebo 3D transformaci pro úpravu perspektivy obrazu. Tím vytváří iluzi nižší latence a plynulejšího pohybu.

Technické fungování ATW vyžaduje přesné časové zarovnání mezi videosnímky a polohovými daty, což je funkce často zajišťovaná synchronizačními protokoly. Samotný algoritmus deformace musí být vysoce efektivní, aby mohl být proveden v rámci těsných časových rozpočtů obnovovací frekvence displeje (např. 11 ms pro 90 Hz). Primárně koriguje rotační změny úhlu pohledu, které jsou nejvíce vnímatelným a dezorientujícím zdrojem latence, ačkoli pokročilejší implementace mohou řešit i omezenou translační deformaci. Účinnost ATW se měří její schopností snížit vnímané trhání obrazu (judder), rozmazání a nevolnost z pohybu (simulator sickness), což přímo zlepšuje kvalitu uživatelského zážitku (QoE) pro uživatele XR. Její role v síti 5G je nedílnou součástí architektury pro streamování médií (Media Streaming Architecture, [MSA](/mobilnisite/slovnik/msa/)) a aplikační vrstvy XR, což umožňuje realizovat architektury s rozděleným vykreslováním (split-rendering), kde je náročné zpracování grafiky přesunuto na okraj sítě, aniž by byla narušena imerze kvůli latenci.

## K čemu slouží

ATW byla zavedena, aby řešila základní problém latence mezi pohybem a zobrazením (motion-to-photon) v síťově doručovaných službách rozšířené reality, což je hlavní překážkou pro imerzi a uživatelský komfort. V tradiční real-time grafice se latence minimalizuje lokálním vykreslováním. Pro náročné XR aplikace plánované pro sítě 5G a 6G – jako cloudové hraní, sociální VR nebo průmyslový metaverse – se však vykreslování často provádí na serveru na okraji sítě, aby bylo možné využít vyšší výpočetní výkon a umožnit tenké klienty. To přináší nevyhnutelná zpoždění z vykreslování, kódování videa, paketizace, přenosu přes rozhraní vzduchem, dekódování a zobrazování. Bez kompenzace tato zpoždění způsobují, že virtuální svět zaostává za pohyby uživatele, což vede k trhání obrazu (judder), konfliktu mezi zrakem a vestibulárním systémem a nevolnosti z pohybu, což výrazně degraduje kvalitu uživatelského zážitku (QoE).

Vytvoření ATW v rámci standardů 3GPP (počínaje Release 16) bylo motivováno snahou průmyslu definovat a optimalizovat podporu XR jako klíčové služby 5G Advanced. Předchozí přístupy byly z velké části proprietární řešení v rámci konkrétních SDK headsetů nebo herních enginů. Standardizace prostřednictvím 3GPP zajišťuje interoperabilitu mezi síťovými mediálními procesory (v edge cloudu) a širokou škálou spotřebitelských XR zařízení. Řeší omezení pouhého snážení o minimalizaci síťové latence, protože fyzická omezení brání snížení doby odezvy na nepostřehnutelnou úroveň pod 10 ms přes bezdrátové spoje pro mnoho uživatelů. ATW poskytuje doplňkovou techniku na aplikační vrstvě, která efektivně „obchází“ problém latence a činí systém tolerantnějším vůči nevyhnutelnému kolísání zpoždění (jitter) a variabilitě přenosového zpoždění v mobilních sítích. Je to klíčový faktor umožňující komerční životaschopnost kvalitních, bezdrátových a neomezených (untethered) zážitků v XR.

## Klíčové vlastnosti

- Kompenzuje latenci mezi pohybem a zobrazením (motion-to-photon) deformací vykreslených snímků
- Funguje asynchronně, odděluje obnovování displeje od řetězce vykreslování/kódování/dekódování snímků
- Primárně koriguje rotační latenci pomocí aktualizovaných polohových dat
- Integruje se s architekturou pro streamování médií 3GPP (Media Streaming Architecture) pro synchronizované doručování snímků a metadat
- Zlepšuje vnímanou plynulost a snižuje trhání obrazu (judder) v XR video proudech
- Zvyšuje toleranci vůči kolísání zpoždění (jitter) a variabilnímu přenosovému zpoždění v systémech 5G

## Definující specifikace

- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [ATW na 3GPP Explorer](https://3gpp-explorer.com/glossary/atw/)
