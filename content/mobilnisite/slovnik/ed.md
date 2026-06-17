---
slug: "ed"
url: "/mobilnisite/slovnik/ed/"
type: "slovnik"
title: "ED – Envelope Detector"
date: 2026-01-01
abbr: "ED"
fullName: "Envelope Detector"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ed/"
summary: "Signálově zpracovávající komponenta používaná v 3GPP rádiových přijímačích k demodulaci amplitudově modulovaných signálů extrakcí obálky přijímaného průběhu. Je klíčová pro energeticky efektivní příje"
---

ED je signálově zpracovávající komponenta v 3GPP rádiovém přijímači, která demoduluje amplitudově modulované signály extrakcí obálky přijímaného průběhu.

## Popis

Detektor obálky (ED) je základní nekoherentní demodulační obvod používaný na fyzické vrstvě 3GPP rádiových přístupových sítí, zejména specifikovaný pro technologie jako LTE-M a NB-IoT. Jeho primární funkcí je obnovení základopásmového informačního signálu z amplitudově modulované nosné vlny bez nutnosti fázově synchronizovaného lokálního oscilátoru pro synchronizaci nosné. Z architektonického hlediska je typicky implementován jako jednoduchá diodová usměrňovačka následovaná dolní propustí. Přijímaný vysokofrekvenční signál je nejprve usměrněn, což umožňuje průchod proudu primárně v jednom směru, čímž se zachytávají vrcholy průběhu. Následná dolní propust pak tento usměrněný signál vyhladí, odstraní vysokofrekvenční složky nosné a na výstup poskytne časově proměnnou obálku odpovídající původním modulujícím datům.

V kontextu 3GPP specifikací, jako jsou 36.789 a 38.191, je ED analyzován a definován z hlediska svého výkonu v přijímačích uživatelského zařízení (UE). Funguje na principu využití amplitudových změn signálu. U modulačních schémat jako klíčování zapnuto/vypnuto ([OOK](/mobilnisite/slovnik/ook/)) nebo amplitudová fázová manipulace (ASK) používaných v některých IoT scénářích výstupní napětí detektoru přímo sleduje amplitudu vstupního signálu. Tento proces je inherentně odolný vůči fázovému šumu a frekvenčním odchylkám, protože nezávisí na přesné obnově fáze nosné. To však probíhá na úkor výkonu v šumovém prostředí ve srovnání s koherentními detektory, protože je náchylnější k amplitudovému šumu a zkreslení.

Role ED v síti je primárně na straně UE, zejména u zařízení s omezeným příkonem. Umožňuje návrh přijímače s nízkou složitostí a nízkou spotřebou, což je klíčový požadavek pro zařízení hromadné komunikace strojového typu (mMTC), která upřednostňují životnost baterie před špičkovou přenosovou rychlostí. V 3GPP testovacích specifikacích jsou definovány charakteristiky ED, aby byla zajištěna interoperabilita a minimální požadavky na výkon přijímačů využívajících tuto detekční metodu. Jeho integrace umožňuje cenově efektivní křemíkovou implementaci, což přispívá k rozšíření IoT zařízení v celulárních sítích snížením spotřeby energie i nákladů na komponenty.

## K čemu slouží

Detektor obálky existuje, aby poskytoval nízkonákladové a energeticky efektivní demodulační řešení pro amplitudově modulované signály v celulárním IoT a dalších aplikacích s nízkou spotřebou. Byl zaveden, aby řešil přísná omezení spotřeby energie a nákladů u zařízení hromadného IoT, jako jsou senzory a měřiče, které vyžadují roky životnosti baterie. Před jeho explicitním zohledněním ve standardech 3GPP pro IoT přijímače často spoléhaly na složitější koherentní nebo synchronní detekci, která vyžaduje přesné obvodové obnovení nosné, vyšší stabilitu lokálního oscilátoru a náročnější digitální zpracování signálu – to vše zvyšuje spotřebu energie a plochu čipu.

Historická motivace vychází z potřeby podpory sítí ultra-nízkopříkonových širokopásmových sítí (LPWAN) v rámci ekosystému 3GPP, zejména se standardizací LTE-M a NB-IoT od vydání 13. Tyto technologie vyžadovaly architektury přijímačů, které mohou pracovat s minimální aktivní spotřebou. Detektor obálky, jakožto klasický analogový obvod, nabízí osvědčenou jednoduchou metodu demodulace signálů bez nutnosti energeticky náročných smyček fázového závěsu (PLL) nebo vysokorychlostních analogově-digitálních převodníků ([ADC](/mobilnisite/slovnik/adc/)) pro plné digitální zpracování. Řeší problém umožnění funkční bezdrátové komunikace pro zařízení, kde jsou přenosové rychlosti nízké a tolerance k latenci vysoká, ale energetická účinnost je prvořadá.

Standardizací jeho výkonnostních parametrů 3GPP zajišťuje, že i při použití této jednodušší techniky zařízení splňují základní úroveň citlivosti a potlačení rušení, což umožňuje předvídatelné plánování pokrytí sítě a kapacity. Představuje záměrný kompromis v návrhu, přijetí mírné penalizace rozpočtu spoje za významné zlepšení životnosti baterie zařízení a snížení nákladů, což je nezbytné pro ekonomickou životaschopnost rozsáhlých nasazení IoT.

## Klíčové vlastnosti

- Nekoherentní demodulace bez obnovy fáze nosné
- Jednoduchá implementace s diodovým usměrňovačem a dolní propustí
- Nízká spotřeba energie vhodná pro IoT zařízení napájená bateriemi
- Odolnost vůči fázovému šumu a frekvenčním odchylkám
- Použitelnost pro amplitudové modulace jako OOK a ASK
- Definované výkonnostní metriky v 3GPP specifikacích pro zkoušky shody

## Definující specifikace

- **TS 36.789** (Rel-13) — LAA Multi-Node Coexistence Test Methodology
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [ED na 3GPP Explorer](https://3gpp-explorer.com/glossary/ed/)
