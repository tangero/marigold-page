---
slug: "rst"
url: "/mobilnisite/slovnik/rst/"
type: "slovnik"
title: "RST – Running Status Table"
date: 2025-01-01
abbr: "RST"
fullName: "Running Status Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rst/"
summary: "Running Status Table (Tabulka průběžného stavu) je datová struktura definovaná v rámci frameworku Multimedia Broadcast Multicast Service (MBMS) konsorcia 3GPP, konkrétně pro protokol File Delivery ove"
---

RST je datová struktura ve frameworku MBMS konsorcia 3GPP pro protokol FLUTE, která poskytuje příjemcům informace o stavu v reálném čase o probíhajících relacích doručování souborů.

## Popis

Running Status Table (RST) (Tabulka průběžného stavu) je specifická komponenta v architektuře Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) konsorcia 3GPP, standardizovaná primárně v TS 26.347 pro protokol File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)). FLUTE se používá pro spolehlivé doručování souborů přes vysílací/multicastové sítě. RST je signalizační tabulka přenášená v pásmu, která je periodicky vysílána v rámci FLUTE relace spolu se samotnými daty souborů. Jejím hlavním účelem je sdělovat všem přijímajícím klientům stav přenosu souborů v rámci relace v reálném čase. Tabulka obsahuje záznamy pro každý doručovaný soubor, včetně klíčových metadat, jako je Transport Object Identifier ([TOI](/mobilnisite/slovnik/toi/)) souboru, jeho aktuální stav doručení (např. 'aktivní', 'dokončený', 'zrušený') a relevantní časové informace. Z architektonického hlediska RST generuje a spravuje Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťová entita odpovědná za poskytování a doručování služeb MBMS. BM-SC zapouzdřuje RST do FLUTE paketů a plánuje její vysílání v rámci vysílacího karuselu. Na straně přijímače (UE) klient MBMS parsuje příchozí FLUTE data, extrahuje RST a používá ji pro správu procesu příjmu souborů. RST umožňuje přijímači určit, které soubory jsou právě přenášeny, které již byly dokončeny a zda byly nějaké plánované soubory odstraněny. To umožňuje klientovi činit informovaná rozhodnutí, jako je ignorování dokončených souborů, zahájení příjmu nově oznámených souborů nebo uvolnění prostředků pro zrušené soubory. Jde o klíčový mechanismus pro dosažení efektivního a spolehlivého doručování souborů v jednosměrném prostředí, kde explicitní zpětná vazba od příjemců k odesílateli není možná nebo škálovatelná.

## K čemu slouží

RST byla vytvořena k řešení problému dynamického řízení relací v jednosměrných vysílacích/multicastových systémech pro doručování souborů, konkrétně v rámci frameworku [MBMS](/mobilnisite/slovnik/mbms/) konsorcia 3GPP. Při tradičnímu unicastovému stahování souborů stav relace spravuje obousměrný handshake a řídicí protokol (jako TCP). Ve vysílání však, kde jeden vysílač obsluhuje potenciálně miliony pasivních přijímačů, je taková zpětná vazba nemožná. Předchozí přístupy mohly spoléhat pouze na statický popis relace (např. File Delivery Table - [FDT](/mobilnisite/slovnik/fdt/)), který popisuje pouze počáteční plán, nikoli živý průběh. RST řeší omezení statických popisů tím, že poskytuje 'tep' relace doručování v reálném čase přenášený v pásmu. Informuje přijímače o změnách, které nastanou po zahájení relace, jako je přidání, odstranění nebo dokončení přenosu souborů. To je kritické pro služby jako softwarové aktualizace přes vzduch (FOTA), kde se nabídka obsahu může dynamicky měnit, nebo pro efektivní karuselové doručování opakujícího se obsahu. RST zajišťuje, aby všichni příjemci měli synchronizovaný a přesný pohled na stav přenosu, což umožňuje efektivní využití baterie a výpočetních prostředků přijímače a zabraňuje klientům v nekonečném čekání na soubory, které již nejsou plánovány.

## Klíčové vlastnosti

- Signalizace v pásmu periodicky přenášená v datovém toku FLUTE relace
- Poskytuje stav v reálném čase (aktivní, dokončený, zrušený) pro každý doručovaný soubor
- Identifikuje soubory pomocí FLUTE Transport Object Identifier (TOI)
- Generována a spravována Broadcast Multicast Service Center (BM-SC)
- Umožňuje efektivní správu prostředků přijímače v jednosměrných vysílacích scénářích
- Nezbytná pro dynamické řízení MBMS relací, kde se sestava souborů může měnit

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [FDT – FLUTE File Delivery Table](/mobilnisite/slovnik/fdt/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [TOI – Transmission Object Identifier](/mobilnisite/slovnik/toi/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [RST na 3GPP Explorer](https://3gpp-explorer.com/glossary/rst/)
