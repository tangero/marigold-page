---
slug: "mux"
url: "/mobilnisite/slovnik/mux/"
type: "slovnik"
title: "MUX – H.223 Multiplex layer"
date: 2025-01-01
abbr: "MUX"
fullName: "H.223 Multiplex layer"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mux/"
summary: "Vrstva multiplexování definovaná v normě ITU-T H.223, kterou 3GPP přijala pro okruhově spínanou videotelefonii přes UMTS. Multiplexuje audio, video, data a řídicí toky do jediného bitového toku pro př"
---

MUX je vrstva multiplexování H.223, která kombinuje audio, video, data a řídicí toky do jediného bitového toku pro okruhově spínanou videotelefonii přes sítě UMTS.

## Popis

Vrstva MUX, formálně vrstva multiplexování H.223, je protokolová vrstva specifikovaná [ITU-T](/mobilnisite/slovnik/itu-t/) pro nízkorychlostní multimediální komunikaci a přijatá 3GPP pro okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) multimediální služby, zejména pro 3G-324M videotelefonii přes UMTS. Jejím hlavním úkolem je kombinovat více logických kanálů, z nichž každý nese různé typy médií (např. audio, video, uživatelská data) a řídicí informace, do jediného serializovaného bitového toku pro přenos přes jeden fyzický kanál. Tato vrstva se nachází nad adaptačními vrstvami (H.223 přílohy A, B, C, D pro různé úrovně odolnosti proti chybám) a pod řízením hovoru a mediálními kodeky.

Architektonicky vrstva MUX na straně odesílatele přijímá protokolové datové jednotky (PDU) z různých zdrojů přes více logických kanálů identifikovaných číslem logického kanálu ([LCN](/mobilnisite/slovnik/lcn/)). Vytváří MUX-PDU, z nichž každá se skládá z hlavičky a užitečného zatížení. Hlavička obsahuje řídicí informace multiplexování, nejdůležitější je multiplexní kód ([MC](/mobilnisite/slovnik/mc/)), který definuje mapování logických kanálů na části užitečného zatížení MUX-PDU. Užitečné zatížení může obsahovat data z jednoho nebo více logických kanálů, prokládaná v segmentech. Vrstva MUX na straně přijímače používá MC k demultiplexování příchozího bitového toku, extrahuje segmenty a doručuje je na správný logický kanál vyšší vrstvy ke zpracování.

Jak to funguje, zahrnuje dynamickou tabulku, tabulku multiplexních záznamů (MET), která je vyjednána mezi komunikujícími koncovými zařízeními při sestavování hovoru. MET definuje sadu platných hodnot MC a jim odpovídající konfigurace logických kanálů. Během přenosu odesílatel vybere MC z aktivní MET, která popisuje aktuální kombinaci odesílaných logických kanálů. U médií s proměnnou přenosovou rychlostí, jako je video, musí vrstva MUX efektivně balit data, aby minimalizovala výplň a režii, a přizpůsobovat se přerušovanému charakteru zdrojů. Klíčové součásti zahrnují protokolový stroj MUX, správce MET a procedury pro komunikaci a přepínání MET, které umožňují adaptaci multiplexního schématu na měnící se typy médií nebo chybové stavy. Její role je klíčová pro zajištění synchronizovaného, efektivního a spolehlivého doručování více mediálních komponent přes omezenou šířku pásma jediného okruhově spínaného přenosového kanálu 64 kbps v sítích 3G.

## K čemu slouží

Vrstva multiplexování H.223 MUX byla vytvořena, aby umožnila synchronní, reálnou multimediální komunikaci přes okruhově spínané digitální sítě, které byly základem hlasových služeb 2G a 3G. Před jejím přijetím vyžadovalo odesílání kombinovaného audia a videa samostatné kanály nebo proprietární multiplexování, což bylo neefektivní a neinteroperabilní. Soubor norem [ITU-T](/mobilnisite/slovnik/itu-t/) H.324, který zahrnuje H.223, byl vyvinut pro videokonference přes pevné analogové telefonní linky (PSTN). 3GPP tento soubor přijala a upravila (jako 3G-324M), aby poskytla standardizovanou, spolehlivou službu videotelefonie přes okruhově spínané přenosové kanály UMTS, a zajistila tak globální interoperabilitu mezi terminály a sítěmi.

Jádro problému, který řeší, je efektivní integrace a synchronizace více asynchronních mediálních toků (každý s jiným časováním, přenosovou rychlostí a kritičností) na jediný kanál s konstantní přenosovou rychlostí. Okruhově spínané spojení poskytuje garantovanou šířku pásma, ale je to rigidní kanál. Vrstva MUX umožňuje dynamické sdílení tohoto kanálu mezi audio, video a datovými kanály, přizpůsobuje se okamžitým požadavkům každého z nich. Například při změně scény může video tok vyžadovat více bitů, což MUX může akomodovat přidělením více místa v užitečném zatížení jeho logickému kanálu, případně na úkor výplně v jiných kanálech. Toto dynamické přidělování je efektivnější než statické multiplexování s časovým dělením.

Dále, její návrh s adaptabilními přílohami (A-D) řeší výzvu chybovým rádiovým kanálům. Základní MUX nabízí minimální odolnost proti chybám pro čisté kanály, zatímco přílohy B, C a D přidávají stále robustnější ochranu hlavičky, indikaci délky užitečného zatížení a číslování sekvencí pro boj s bitovými chybami a ztrátou paketů na rádiových spojích. Tento vývoj v rámci samotné normy H.223 byl klíčový pro její mobilní přijetí. Vytvoření tohoto standardizovaného multiplexního protokolu bylo motivováno potřebou jednotné metody pro sdružování médií pro nízkorychlostní aplikace, což byl požadavek, který se stal prvořadým se spuštěním služeb 3G slibujících videohovory, což učinilo z MUX základní protokol pro ranou mobilní multimédii.

## Klíčové vlastnosti

- Multiplexuje více logických kanálů (audio, video, data, řízení) do jediného bitového toku
- Používá multiplexní kód (MC) v hlavičce MUX-PDU k definici složení užitečného zatížení
- Dynamická tabulka multiplexních záznamů (MET) vyjednávaná mezi koncovými zařízeními
- Podporuje více adaptačních vrstev (přílohy A-D) pro různé úrovně odolnosti proti chybám
- Umožňuje efektivní, na šířku pásma adaptivní balení mediálních toků s proměnnou přenosovou rychlostí
- Poskytuje synchronizaci mediálních komponent pro přehrávání v reálném čase

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [MUX na 3GPP Explorer](https://3gpp-explorer.com/glossary/mux/)
