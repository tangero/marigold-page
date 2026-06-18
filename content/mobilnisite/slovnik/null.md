---
slug: "null"
url: "/mobilnisite/slovnik/null/"
type: "slovnik"
title: "NULL – Null Information Frame"
date: 2025-01-01
abbr: "NULL"
fullName: "Null Information Frame"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/null/"
summary: "Specifický typ rámce v protokolu LAPDm používaný na rádiovém rozhraní v sítích GSM/UMTS. Nepřenáší uživatelská data, ale je klíčový pro udržení spojení na vrstvě datového spoje a plnění dohledových fu"
---

NULL je specifický typ rámce LAPDm na rádiovém rozhraní GSM/UMTS, který nepřenáší žádná uživatelská data, ale je klíčový pro udržení spojení linky a plnění dohledových funkcí, jako jsou potvrzení.

## Popis

Rámec NULL (rámec bez informačního pole) je základním prvkem protokolu Link Access Procedure on the Dm channel (LAPDm), který pracuje na vrstvě 2 (vrstvě datového spoje) na rádiovém rozhraní (rozhraní Um) v sítích GSM a UMTS. LAPDm je odvozen od protokolu [ISDN](/mobilnisite/slovnik/isdn/) [LAPD](/mobilnisite/slovnik/lapd/), přizpůsobeného specifickým omezením a požadavkům mobilního rádiového prostředí, jako je efektivita šířky pásma a náchylnost přenosu k chybám. Protokol zajišťuje spolehlivý přenos informací mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a systémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) vytvářením, udržováním a uvolňováním datových spojů. Používá různé typy rámců, včetně informačních (I) rámců pro uživatelská data, dohledových (S) rámců pro řízení toku a opravu chyb (jako [RR](/mobilnisite/slovnik/rr/), [RNR](/mobilnisite/slovnik/rnr/), [REJ](/mobilnisite/slovnik/rej/)) a nečíslovaných (U) rámců pro správu spojení. Rámec NULL je specifickým typem nečíslovaného rámce.

Technicky je rámec NULL identifikován specifickými bitovými vzory v jeho řídicím poli. Obsahuje adresní pole a řídicí pole, ale výrazně postrádá informační pole – tedy nepřenáší žádné datové jednotky protokolu ([PDU](/mobilnisite/slovnik/pdu/)) vyšších vrstev. Jeho primární funkcí je dohledová. Když stanice nemá k odeslání žádná uživatelská data (I-rámce), ale potřebuje udržet spojení v aktivním stavu, může odeslat rámec NULL. To umožňuje stanici sdělit stav připravenosti přijímače (RR) nebo nepřipravenosti přijímače (RNR), potvrdit dříve přijaté I-rámce pomocí sekvenčního čísla N(R) v řídicím poli a udržet spojení aktivní, aby nedošlo k vypršení časového limitu. Přenos rámců NULL přispívá k efektivnímu využití šířky pásma; namísto odesílání prázdných dat se minimálním rámcem udržuje stav protokolu.

V rámci síťové architektury rámec NULL funguje mezi MS a BTS. Je klíčový pro vrstvu správy rádiových prostředků (RR). Například během období ticha v hovoru nebo během fází pouze signalizace musí datové spojení zůstat navázáno, aby bylo možné rychle obnovit přenos dat. Rámec NULL tuto roli plní. Jeho specifikace zajišťuje, že oba konce spojení udržují synchronizovaná sekvenční čísla (N(R) a N(S)) pro detekci a opravu chyb, což je zásadní pro integritu signalizačních zpráv a uživatelských dat přes nespolehlivou rádiovou cestu. Konzistentní definice a zpracování rámce NULL napříč vydáními, jak je udržováno v 3GPP TS 24.022, zajišťuje zpětnou kompatibilitu a stabilní provoz pro starší sítě GSM/EDGE a jejich integraci se systémy UMTS a pozdějšími.

## K čemu slouží

Rámec NULL byl zaveden, aby řešil základní požadavek v protokolech linkové vrstvy na spojově orientovaných kanálech: udržení integrity spojení během nečinných období. V telekomunikačních systémech, jako je GSM, je rádiové rozhraní vzácný a sdílený zdroj. Protokol LAPDm potřeboval mechanismus, jak udržet datové spojení aktivní, aniž by spotřebovával nepotřebnou šířku pásma pro užitečné zatížení, když nebyla k odeslání žádná skutečná uživatelská nebo signalizační data. Před standardizovanými postupy linkové vrstvy systémy mohly vyžadovat nepřetržitý přenos výplňových dat nebo složité mechanismy obnovy spojení založené na časovačích, které mohly být neefektivní nebo pomalé.

Jeho vytvoření bylo motivováno potřebou efektivní dohledové komunikace. Rámec NULL umožňuje přijímači odesílat potvrzení (pomocí pole N(R)) pro dříve přijaté I-rámce, i když nemá k odeslání žádná nová data. To je klíčové pro včasné řízení toku a opravu chyb. Dále poskytuje jasný, standardizovaný způsob, jak indikovat stav přijímače (připraven nebo nepřipraven) bez režie informačního pole. Tím se řeší problém vypršení časového limitu spojení; bez pravidelné výměny rámců by mohlo být spojení považováno za mrtvé a zbytečně uvolněné, což by při obnovení komunikace způsobilo zpoždění a signalizační režii.

Historicky koncept vychází z robustních protokolů datového spoje, jako jsou HDLC a LAPD. Adaptace pro mobilní rádiové prostředí v LAPDm vyžadovala odlehčenou, spolehlivou metodu pro dohled nad spojením, což vedlo k zahrnutí rámce NULL již od počátečních specifikací GSM. Jeho pokračující přítomnost napříč vydáními 3GPP podtrhuje jeho základní roli při zajišťování stabilního provozu s nízkou režií na kritické linkové vrstvě rádiového rozhraní, která podporuje jak okruhově přepínané hlasové služby, tak služby paketových dat.

## Klíčové vlastnosti

- Definován jako typ nečíslovaného (U) rámce v rámci struktury protokolu LAPDm.
- Neobsahuje informační pole, čímž minimalizuje režii přenosu.
- V řídicím poli nese stav přijímače (RR/RNR) a potvrzovací sekvenční čísla (N(R)).
- Používá se k udržení aktivního datového spojení během období bez přenosu uživatelských dat.
- Zabraňuje vypršení časového limitu spojení tím, že zajišťuje pravidelnou výměnu rámců.
- Klíčový pro postupy řízení toku a opravy chyb na rádiovém rozhraní.

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [NULL na 3GPP Explorer](https://3gpp-explorer.com/glossary/null/)
