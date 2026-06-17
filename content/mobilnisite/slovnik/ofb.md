---
slug: "ofb"
url: "/mobilnisite/slovnik/ofb/"
type: "slovnik"
title: "OFB – Output Feedback Mode"
date: 2025-01-01
abbr: "OFB"
fullName: "Output Feedback Mode"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ofb/"
summary: "Režim provozu pro blokovou šifru, standardizovaný organizací 3GPP pro kryptografické algoritmy. V režimu OFB se šifra používá ke generování šifrovacího proudu, který se následně pomocí operace XOR kom"
---

OFB je režim provozu blokové šifry, který generuje šifrovací proud (keystream), jenž se pomocí operace XOR kombinuje s otevřeným textem za vzniku šifrového textu, čímž efektivně vytváří synchronní proudovou šifru zabraňující šíření chyb.

## Popis

Režim výstupní zpětné vazby (Output Feedback, OFB) je kryptografický režim provozu specifikovaný v technických specifikacích 3GPP pro použití s definovanými algoritmy blokových šifer. Je podrobně popsán v řadách bezpečnostních specifikací, jako je 35.205 (pro algoritmy 3GPP) a 35.909 (pro bezpečnostní algoritmy LTE). Režim OFB převádí blokovou šifru (jako např. algoritmy definované 3GPP na bázi Kasumi nebo SNOW 3G) na synchronní proudovou šifru. Jeho klíčová operace spočívá v použití šifrovací funkce blokové šifry nikoli přímo na data, ale na interní stavový registr za účelem generování pseudonáhodného bloku šifrovacího proudu.

Mechanismus funguje následovně: Inicializační vektor ([IV](/mobilnisite/slovnik/iv/)) je načten do posuvného registru. Bloková šifra zašifruje obsah tohoto registru. Výsledný výstupní blok tvoří šifrovací proud pro danou iteraci. Tento blok šifrovacího proudu je následně pomocí operace XOR kombinován s blokem otevřeného textu za vzniku odpovídajícího bloku šifrového textu. Zásadní je, že výstupní blok šifrovacího proudu je také zpětnovazebně přiveden, aby se stal vstupem pro další šifrovací operaci (odtud 'výstupní zpětná vazba'), poté co je registr posunut. Tento proces se opakuje pro každý následující blok dat. Kritickou charakteristikou je, že šifrování zpětnovazebního registru je nezávislé na otevřeném nebo šifrovém textu; závisí pouze na klíči a předchozím výstupu.

V systémech 3GPP byla primární role režimu OFB ve specifikaci návrhu a testování kryptografických algoritmů, nikoli jako přímo používaný šifrovací režim v protokolovém zásobníku rádiového rozhraní. Používá se například při návrhu a hodnocení základních kryptografických primitiv. Jeho vlastnosti jsou analyzovány za účelem zajištění síly algoritmu. Synchronní proudová povaha OFB znamená, že chyba bitu v přenosu způsobí chybu bitu v dešifrovaném otevřeném textu na stejném místě, bez šíření chyby. To může být žádoucí v určitých kontextech komunikace v reálném čase, ačkoli primární režimy šifrování rádiového rozhraní 3GPP (jako UEA1, UEA2 pro UMTS nebo [EEA](/mobilnisite/slovnik/eea/) pro LTE) typicky používají jiné režimy, jako je režim čítače ([CTR](/mobilnisite/slovnik/ctr/)) nebo specifické konstrukce proudových šifer.

## K čemu slouží

Režim OFB byl začleněn do specifikací 3GPP, aby poskytl standardizovaný, dobře pochopený kryptografický konstrukt pro použití v rámci návrhu a analýzy souboru bezpečnostních algoritmů 3GPP. Jeho účelem není nutně primární šifrovací režim pro uživatelská data přes rozhraní, ale jako součást širšího kryptografického nástrojového souboru. Slouží jako referenční režim pro testování a validaci algoritmů a pro konstrukci složitějších kryptografických operací, pokud je to potřeba.

Historická motivace pro zahrnutí různých režimů, jako je OFB, pramení z potřeby důkladného bezpečnostního hodnocení. Když 3GPP vyvíjí novou šifru (např. pro 4G nebo 5G), její základní bloková šifra nebo transformace je testována v uznávaných režimech, jako jsou OFB, [CBC](/mobilnisite/slovnik/cbc/) a [CTR](/mobilnisite/slovnik/ctr/), aby bylo možné posoudit její kryptografické vlastnosti (např. náhodnost, difúzi) v různých scénářích. Tato komplexní analýza zajišťuje robustnost algoritmu před jeho nasazením ve složitějších, přizpůsobených režimech používaných pro skutečné šifrování rádiového rozhraní (jako je [AES](/mobilnisite/slovnik/aes/) v režimu CTR pro 5G).

Režim OFB konkrétně řeší scénář vyžadující synchronní proudovou šifru. Ve srovnání s režimem řetězení šifrových bloků (CBC) režim OFB nezpůsobuje šíření chyb, což může být důležité pro služby v reálném čase, kde není možné retransmise. Jeho požadavek na striktní synchronizaci a riziko opakovaného použití šifrovacího proudu při opakování [IV](/mobilnisite/slovnik/iv/) však vedly 3GPP k upřednostnění jiných režimů, jako je CTR, pro hlavní použití. Role OFB je tedy primárně role kryptografického zajištění návrhu a úplnosti v portfoliu bezpečnostních specifikací 3GPP.

## Klíčové vlastnosti

- Převádí blokovou šifru na synchronní proudovou šifru
- Generuje šifrovací proud nezávislý na datech otevřeného/šifrového textu
- Používá výstup šifrování jako zpětnou vazbu pro další blok šifrovacího proudu
- Dešifrování používá identický generátor šifrovacího proudu, kombinovaný se šifrovým textem pomocí XOR
- Chyby bitů v šifrovém textu způsobují izolované chyby bitů v otevřeném textu (bez šíření)
- Vyžaduje jedinečný inicializační vektor (IV) pro každou relaci, aby se zabránilo opakovanému použití šifrovacího proudu

## Související pojmy

- [AES – Advanced Encryption Standard](/mobilnisite/slovnik/aes/)

## Definující specifikace

- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [OFB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ofb/)
