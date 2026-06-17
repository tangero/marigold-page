---
slug: "eac"
url: "/mobilnisite/slovnik/eac/"
type: "slovnik"
title: "EAC – Ericsson Alpha Compression"
date: 2026-01-01
abbr: "EAC"
fullName: "Ericsson Alpha Compression"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eac/"
summary: "Ericsson Alpha Compression (EAC) je proprietární kompresní algoritmus s nízkou složitostí pro textová data aplikační vrstvy, například zprávy v chatu. Zavedený v 3GPP Rel-16 pro 5G si klade za cíl zme"
---

EAC je proprietární kompresní algoritmus s nízkou složitostí definovaný v 3GPP pro 5G, používaný ke zmenšení velikosti užitečného zatížení textových aplikačních dat, jako jsou zprávy v chatu, za účelem zlepšení efektivity přenosu.

## Popis

Ericsson Alpha Compression (EAC) je textový kompresní algoritmus standardizovaný 3GPP, původně navržený společností Ericsson. Je navržen jako kompresní schéma aplikační vrstvy s nízkou složitostí optimalizované pro krátké textové řetězce, jako jsou ty používané v chatovacích aplikacích, službách zasílání zpráv nebo jiných přenosech alfanumerických dat. Algoritmus funguje na principu statického slovníku a souboru kódovacích pravidel pro reprezentaci běžných znaků, párů znaků (digramů) a slov pomocí kratších bitových sekvencí. Tento statický slovník je předdefinován a znám jak kompresoru (klient/UE), tak dekompresoru (server/aplikační funkce), čímž odpadá potřeba přenosu a synchronizace dynamického slovníku, což snižuje režii a latenci.

Architektonicky EAC funguje nad transportní vrstvou, typicky v rámci samotného aplikačního protokolu. V kontextu 3GPP je jeho použití definováno v rámci Edge Computing a optimalizace aplikačních dat. Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo Application Function ([AF](/mobilnisite/slovnik/af/)) jádra 5G sítě mohou být informovány o službách využívajících EAC, aby umožnily efektivnější zpracování dat. Kompresní proces zahrnuje parsování vstupního textu, porovnávání sekvencí se statickým slovníkem a výstup komprimovaného bitového toku. Dekomprese je přímočarý proces zpětného vyhledávání. Jeho nízká výpočetní složitost jej činí vhodným pro implementaci na zařízeních s omezenými prostředky a pro komunikaci v reálném čase.

Úlohou EAC v síti je zvýšit efektivitu specifických datových služeb snížením objemu dat přenášených přes rozhraní rádiové a jádrové sítě. Toto snížení snižuje latenci, šetří šířku pásma a může zlepšit výdrž baterie uživatelského zařízení zkrácením doby rádiového přenosu. Je součástí souboru technik optimalizace dat zvažovaných v 5G pro podporu různorodých požadavků služeb, zejména pro IoT a efektivní zasílání zpráv. Je důležité poznamenat, že EAC je specifický, proprietární algoritmus, který byl přijat do standardů 3GPP, čímž se odlišuje od jiných obecných kompresních standardů, jako je DEFLATE.

## K čemu slouží

Ericsson Alpha Compression (EAC) byl vytvořen k řešení potřeby efektivního přenosu krátkých textových zpráv v mobilních sítích, což je případ převládající v chatovacích aplikacích, aktualizacích stavu zařízení IoT a signalizačních zprávách. Ačkoli existují univerzální kompresní algoritmy (např. gzip, DEFLATE), ty často zahrnují vyšší výpočetní složitost a paměťové nároky, což je činí méně vhodnými pro časté, malé datové přenosy a pro zařízení s omezenou kapacitou baterie. Navíc jejich přístup s dynamickým slovníkem přináší režii pro malé datové bloky.

Motivací pro standardizaci EAC v rámci 3GPP bylo poskytnout odlehčenou, standardizovanou kompresní metodu, kterou by sítě a zařízení mohly všeobecně podporovat pro specifické typy aplikací. Jeho zavedení ve verzi 16 je v souladu s cíli 5G podporovat masivní IoT a efektivní komunikaci typu stroj-stroj. Použitím statického slovníku EAC odstraňuje potřebu přenosu dat slovníku, čímž je vysoce efektivní pro kompresi velmi krátkých řetězců, kde by režie dynamického slovníku negovala přínosy. Tím se řeší problém neefektivního využití šířky pásma pro opakující se, předvídatelné textové vzory běžné v komunikaci stroj-stroj a osoba-osoba.

## Klíčové vlastnosti

- Kompresní algoritmus s nízkou složitostí založený na statickém slovníku
- Optimalizovaný pro krátké alfanumerické řetězce (např. zprávy v chatu)
- Předdefinovaný slovník známý kompresoru i dekompresoru
- Snižuje velikost zatížení pro data aplikační vrstvy
- Vhodný pro UE s omezenými prostředky a aplikace s nízkou latencí
- Standardizován v 3GPP pro použití v optimalizaci služeb 5G sítě

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 29.536** (Rel-19) — NSACF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [EAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/eac/)
