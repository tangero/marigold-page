---
slug: "facch-h"
url: "/mobilnisite/slovnik/facch-h/"
type: "slovnik"
title: "FACCH/H – Fast Associated Control Channel/Half rate"
date: 2025-01-01
abbr: "FACCH/H"
fullName: "Fast Associated Control Channel/Half rate"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/facch-h/"
summary: "Poloviční řídicí kanál v GSM, který přivlastňuje bity z polovičního provozního kanálu (TCH/H) pro přenos naléhavých signalizačních zpráv. Umožňuje kritickou signalizaci, jako jsou příkazy k předání ho"
---

FACCH/H je poloviční řídicí kanál v GSM, který přenáší naléhavou signalizaci přivlastněním bitů z polovičního provozního kanálu, což umožňuje kritické funkce, jako jsou příkazy k předání hovoru během volání bez vyhrazeného plnorychlostního kanálu.

## Popis

Rychlý přidružený řídicí kanál s poloviční rychlostí ([FACCH](/mobilnisite/slovnik/facch/)/H) je signalizační kanál definovaný v rádiovém rozhraní GSM, určený speciálně pro použití s polovičním provozním kanálem (TCH/H). Funguje na principu 'vnitropásmové signalizace' neboli 'přivlastňování', kdy jsou předem definované bity v datovém toku uživatele na TCH/H periodicky přeúčelovány pro přenos signalizačních informací vrstvy 2 a vrstvy 3. Tento mechanismus je klíčový, protože vyhrazený samostatný řídicí kanál by byl pro sporadické, ale naléhavé signalizační potřeby aktivního spojení neefektivní. FACCH/H je 'přidružený', protože je vnitřně propojen s konkrétním TCH/H uživatele, a 'rychlý', protože poskytuje signalizaci s nižší latencí ve srovnání s Pomalým přidruženým řídicím kanálem (SACCH), který pracuje na pevném, vícerámcovém časování.

Z architektonického hlediska je FACCH/H mapován na stejný fyzický zdroj jako TCH/H. Struktura GSM burstu obsahuje v hlavičce bit 'Stealing Flag'. Když je tento příznak nastaven, signalizuje přijímači, že datová část tohoto konkrétního burstu obsahuje data FACCH namísto uživatelského provozu. Kanálové kódování pro FACCH/H je robustní, typicky zahrnuje konvoluční kódování a prokládání přes více burstů, aby byla zajištěna spolehlivá recepce i za špatných rádiových podmínek. To je nezbytné, protože signalizační zprávy, které přenáší, jako jsou příkazy k předání hovoru, jsou kritické pro udržení kontinuity hovoru.

Při provozu rozhoduje řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) sítě o tom, kdy použít FACCH/H. Když potřebuje odeslat signalizační zprávu mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) zapojené do polovičního hlasového hovoru, BSC nařídí základnové přijímací a vysílací stanici ([BTS](/mobilnisite/slovnik/bts/)), aby nahradila příslušné řečové rámce zakódovanými daty FACCH/H. MS po detekci příznaků přivlastnění dekóduje řídicí zprávu a podle ní jedná, například provede předání hovoru na novou buňku. Primární úlohou FACCH/H je podpora řídicích procedur v reálném čase pro již navázané spojení, což vyvažuje potřebu okamžité signalizace s efektivním využitím rádiového spektra přiděleného pro hlas.

## K čemu slouží

[FACCH](/mobilnisite/slovnik/facch/)/H byl vyvinut, aby rozšířil efektivní signalizační schopnosti plnorychlostního FACCH na poloviční provozní kanály zavedené v GSM pro zvýšení kapacity sítě. Před polovičními kodeky všechny hlasové hovory používaly plnorychlostní provozní kanál (TCH/F), který měl přidružený [FACCH/F](/mobilnisite/slovnik/facch-f/). Zavedení TCH/H, který využívá účinnější řečové kódování pro snížení šířky pásma na polovinu na jeden hovor, vytvořilo potřebu odpovídajícího mechanismu řídicího kanálu. Bez FACCH/H by polovičním hovorům chyběl signalizační kanál s nízkou latencí, což by nutilo veškerou signalizaci přenášet na mnohem pomalejší SACCH nebo by vyžadovalo přechod na plnorychlostní kanál pouze pro signalizaci. Obě tyto možnosti by zhoršily uživatelský zážitek a zrušily by kapacitní výhody polovičního kódování.

Jádrem problému, který řeší, je poskytnutí včasného a spolehlivého doručení kritických signalizačních zpráv – nejvýznamněji příkazů k předání hovoru – pro účastníky používající poloviční řečové kanály. Rozhodnutí o předání hovoru jsou časově citlivá; zpoždění mohou vést ke ztrátě hovoru. FACCH/H zajišťuje, že mobilní stanice v polovičním hovoru může přijmout a provést příkaz k předání hovoru s latencí srovnatelnou s plnorychlostním hovorem, čímž udržuje kvalitu služby. Jeho vytvoření bylo motivováno dvojím cílem: optimalizace sítě (podpora většího počtu uživatelů na buňku) a udržení nebo dokonce zlepšení vnímané kvality služby pro všechny účastníky s rostoucím síťovým provozem.

## Klíčové vlastnosti

- Vnitropásmová signalizace prostřednictvím přivlastňování bitů z burstů TCH/H
- Používá příznaky přivlastnění v hlavičkách burstů k označení řídicích dat
- Poskytuje signalizaci s nízkou latencí pro aktivní poloviční spojení
- Přenáší kritické zprávy vrstvy 3, jako jsou příkazy k předání hovoru
- Používá robustní kanálové kódování (konvoluční kódování, prokládání) pro spolehlivost
- Funguje v režimu point-to-point přidruženém ke konkrétnímu spojení MS

## Související pojmy

- [FACCH/F – Fast Associated Control Channel/Full rate](/mobilnisite/slovnik/facch-f/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [FACCH/H na 3GPP Explorer](https://3gpp-explorer.com/glossary/facch-h/)
