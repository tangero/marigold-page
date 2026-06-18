---
slug: "kss"
url: "/mobilnisite/slovnik/kss/"
type: "slovnik"
title: "KSS – Key Stream Segment"
date: 2025-01-01
abbr: "KSS"
fullName: "Key Stream Segment"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/kss/"
summary: "Key Stream Segment (KSS) je část šifrovacího klíčového proudu generovaného algoritmem proudové šifry (jako SNOW 3G nebo ZUC) používaným v systémech 3GPP. Je vytvářen šifrovacím algoritmem z tajného kl"
---

KSS je část šifrovacího klíčového proudu generovaného proudovou šifrou z tajného klíče a inicializačního vektoru, která je kombinována s otevřeným textem za účelem vytvoření šifrovaného textu pro zajištění důvěrnosti v systémech 3GPP.

## Popis

Key Stream Segment (KSS) je klíčový operační koncept v algoritmech důvěrnosti založených na proudových šifrách specifikovaných 3GPP, konkrétně algoritmech 128-EEA1 (SNOW 3G), 128-EEA2 ([AES](/mobilnisite/slovnik/aes/) v [CTR](/mobilnisite/slovnik/ctr/) režimu) a 128-EEA3 (ZUC). Na rozdíl od blokových šifer, které šifrují data v blocích pevné velikosti, proudová šifra generuje pseudonáhodnou posloupnost bitů nazývanou šifrovací klíčový proud. KSS označuje konkrétní segment tohoto klíčového proudu, který je zarovnán a použit k zašifrování konkrétní jednotky dat, jako je Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) nebo specifický segment datového toku.

Generování KSS začíná inicializací proudové šifry. Algoritmus je naplněn tajným šifrovacím klíčem ([CK](/mobilnisite/slovnik/ck/)) a inicializačním vektorem ([IV](/mobilnisite/slovnik/iv/)). IV je klíčový a je konstruován z parametrů, jako je identita rádiového beareru, směr přenosu (uplink/downlink) a nová hodnota COUNT (kryptografické pořadové číslo). To zajišťuje, že stejný CK nikdy nevygeneruje stejný šifrovací klíčový proud dvakrát pro různé datové jednotky. Po inicializaci je vnitřní stav šifry aktualizován a produkuje výstupní šifrovací klíčový proud. Pro danou datovou jednotku délky L bitů algoritmus vygeneruje L-bitový segment tohoto klíčového proudu – to je KSS pro tuto datovou jednotku.

Proces šifrování je pak přímočarý: bity dat otevřeného textu jsou kombinovány bit po bitu (nebo slovo po slově) s odpovídajícími bity KSS pomocí operace exkluzivního [OR](/mobilnisite/slovnik/or/) (XOR) za účelem vytvoření šifrovaného textu. Dešifrování na přijímací straně je identické: přijímač, který disponuje stejným CK a synchronizovaným IV/COUNT, vygeneruje totožný KSS a pomocí operace XOR jej zkombinuje s přijatým šifrovaným textem, čímž obnoví původní otevřený text. Bezpečnost je zcela závislá na nepředvídatelnosti a náhodnosti KSS. Pokud by byl KSS předvídatelný nebo znovupoužitý, byla by důvěrnost narušena. Proto je pečlivá konstrukce IV a kryptografická síla podkladového algoritmu proudové šifry (SNOW 3G, AES-CTR, ZUC) klíčová pro zajištění, že každý KSS je jedinečný a kryptograficky silný.

## K čemu slouží

Účelem Key Stream Segment je poskytnout efektivní a bezpečnou ochranu důvěrnosti pro uživatelská data a signalizaci přes rozhraní vzduchu v systémech 3GPP. Proudové šifry, a tím i KSS, byly pro tuto roli vybrány kvůli svým specifickým výhodám v kontextu bezdrátové komunikace.

Řeší problém šifrování datových proudů, které jsou inherentně proměnlivé délky a mohou obsahovat chyby bitů. Proudové šifry pracují na bázi bit po bitu (nebo byte po bytu), což je přirozeně vhodné pro spojité datové toky, jako je hlas nebo video. Operace XOR je výpočetně nenáročná a, což je klíčové, způsobuje šíření chyb příznivým způsobem: jediná chyba bitu v šifrovaném textu způsobí pouze jedinou chybu bitu v dešifrovaném otevřeném textu. To je významná výhoda oproti režimům blokových šifer, jako je [CBC](/mobilnisite/slovnik/cbc/), kde jediná chyba bitu může poškodit celý blok dešifrovaných dat, což je nežádoucí v náchylném rádiovém prostředí.

Historická motivace vychází z potřeby silnějšího šifrování v 3G (UMTS) ve srovnání se slabšími algoritmy A5 v GSM. Bezpečnostní skupina 3GPP vybrala a později standardizovala konkrétní proudové šifry (SNOW 3G, později ZUC), které nabízely vysokou úroveň bezpečnosti při splnění výkonnostních omezení mobilních zařízení. Koncept KSS je neoddělitelnou součástí fungování těchto algoritmů. Řeší omezení starších, slabších šifer tím, že poskytuje robustní mechanismus, kde je každý segment dat chráněn jedinečnou, kryptograficky silnou maskou (KSS), odvozenou ze silného klíče a pečlivě synchronizovaného stavu, což zajišťuje dlouhodobou důvěrnost proti odposlechu na rádiovém spoji.

## Klíčové vlastnosti

- Zarovnání šifrovacího klíčového proudu: Představuje konkrétní segment výstupního šifrovacího klíčového proudu šifry zarovnaný na konkrétní datovou jednotku (PDU) pro šifrování/dešifrování.
- Synchronní provoz: Vyžaduje dokonalou synchronizaci vnitřního stavu šifry (pomocí COUNT/IV) mezi odesílatelem a přijímačem pro generování totožného KSS.
- Bitové šifrování XOR: Důvěrnost je dosažena kombinací otevřeného textu a KSS pomocí logické operace exkluzivního OR (XOR).
- Průhlednost vůči chybám: Chyba bitu v přenášeném šifrovaném textu má za následek pouze jedinou chybu bitu v dešifrovaném otevřeném textu, což je vhodné pro rádiové kanály.
- Nezávislost na algoritmu: Koncept KSS platí pro všechny proudové šifry 3GPP (SNOW 3G, AES-CTR, ZUC), i když se jejich vnitřní generovací mechanismus liší.
- Závislost na IV: Jedinečnost a bezpečnost každého KSS kriticky závisí na správné a neopakující se konstrukci inicializačního vektoru (IV).

## Definující specifikace

- **TS 33.102** (Rel-19) — 3G Security Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [KSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/kss/)
