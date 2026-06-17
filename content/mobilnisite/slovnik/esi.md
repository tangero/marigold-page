---
slug: "esi"
url: "/mobilnisite/slovnik/esi/"
type: "slovnik"
title: "ESI – Encoding Symbol Identifier"
date: 2025-01-01
abbr: "ESI"
fullName: "Encoding Symbol Identifier"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esi/"
summary: "Identifikátor kódového symbolu (ESI) je klíčové pole v rámci schématu korekce chyb dopředu (FEC), konkrétně v kódech Raptor a RaptorQ. Jednoznačně identifikuje každý kódový symbol (zdrojový nebo oprav"
---

ESI je pole ve FEC kódech, jako je Raptor, které jednoznačně identifikuje každý kódový symbol v rámci zdrojového bloku a umožňuje správnou rekonstrukci dat po přenosu.

## Popis

Identifikátor kódového symbolu (ESI) je základní součástí specifikovaných schémat korekce chyb dopředu ([FEC](/mobilnisite/slovnik/fec/)) na aplikační vrstvě podle 3GPP, konkrétně kódů Raptor a RaptorQ, definovaných pro spolehlivé doručování dat přes vysílací a skupinové kanály. Tyto FEC kódy fungují tak, že vezmou původní datový objekt (např. soubor nebo segment proudu), rozdělí jej na zdrojové bloky a poté z každého bloku generují potenciálně neomezený počet kódových symbolů. Kódové symboly mohou být buď původní zdrojové symboly, nebo opravné symboly generované matematicky ze zdrojových symbolů. ESI je celočíselná hodnota, která jednoznačně identifikuje každý jednotlivý kódový symbol v kontextu konkrétního zdrojového bloku.

Technicky během procesu kódování přiřadí FEC enkodér ESI každému vygenerovanému symbolu. Pro původní zdrojové symboly jsou hodnoty ESI typicky po sobě jdoucí celá čísla začínající od 0. Pro opravné symboly hodnoty ESI pokračují sekvenčně nebo jsou přiřazeny z odděleného rozsahu v závislosti na konfiguraci FEC schématu. Toto ESI je pak zahrnuto jako část datové části symbolu při jeho přenosu, často zapouzdřené v protokolu jako [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/). Na straně přijímače FEC dekodér shromažďuje přijaté symboly, z nichž každý je označen svým ESI. Dekodér použije ESI k umístění každého symbolu na správnou pozici v rámci matematického systému rovnic, který modeluje FEC kód. Jakmile je přijato dostatek symbolů (s různými ESI) – dosáhne nebo překročí počet původních zdrojových symbolů – může dekodér tyto rovnice vyřešit a dokonale rekonstruovat celý zdrojový blok.

Role ESI je klíčová pro efektivitu a odolnost procesu FEC. Umožňuje přenášet a přijímat symboly mimo pořadí, což je běžné v IP sítích a zejména ve vysílacích scénářích, kde různí přijímači mohou zaznamenat různé ztrátové vzorce. Přijímač nemusí znát pořadí přenosu; potřebuje pouze sadu symbolů s různými ESI. Díky tomu je FEC schéma ideální pro distribuci jeden-všem. ESI spolu s identifikátorem datové části FEC (FEC Payload ID, který také obsahuje číslo zdrojového bloku a další parametry) tvoří minimální nezbytné informace pro funkci dekodéru, což zajišťuje, že režie pro řídicí informace FEC je velmi nízká a maximalizuje se tak efektivita vysílacího přenosového média.

## K čemu slouží

ESI byl vytvořen k řešení výzvy spolehlivého doručování souborů a proudů přes inherentně nespolehlivé kanály jeden-všem, jako jsou ty používané v [MBMS](/mobilnisite/slovnik/mbms/)/eMBMS. Tradiční opakování založené na TCP je pro vysílání neefektivní a neškálovatelné, protože vede k implozi zpětné vazby (miliony přijímačů posílají [NACK](/mobilnisite/slovnik/nack/)). Korekce chyb dopředu ([FEC](/mobilnisite/slovnik/fec/)) poskytuje řešení přidáním redundantních dat, ale praktické FEC schéma pro vysílání vyžaduje způsob, jak mohou přijímače identifikovat, které konkrétní kusy redundantních dat obdržely, aniž by se spoléhaly na pořadová čísla, která implikují striktní lineární pořadí.

ESI to řeší tím, že poskytuje identifikátor zaměřený na obsah spíše než na posloupnost. Jeho účelem je umožnit FEC dekodéru jednoznačně identifikovat matematickou roli každého přijatého symbolu nezávisle na pořadí přenosu nebo ztrátě. Tento design přímo řeší omezení předchozích jednodušších FEC schémat nebo čistého opakování. Umožňuje použití pokročilých fontánových kódů, jako je RaptorQ, kde může přijímač obnovit původní data z *jakékoli* sady kódových symbolů, pokud je celkový počet dostatečný. ESI je klíčem, který umožňuje toto obnovení z 'libovolných symbolů', protože říká dekodéru přesně, kterou lineární rovnici každý symbol reprezentuje. Tato inovace byla klíčová pro zajištění odolnosti vysílacích služeb 3GPP proti ztrátě paketů při zachování vysoké spektrální účinnosti.

## Klíčové vlastnosti

- Jednoznačně identifikuje každý kódový symbol (zdrojový nebo opravný) v rámci zdrojového bloku
- Umožňuje FEC dekódování nezávislé na pořadí přenosu nebo příjmu symbolů
- Integrální součást specifikací FEC schémat Raptor a RaptorQ
- Přenášen v rámci identifikátoru datové části FEC (FEC Payload ID) vysílaných paketů
- Umožňuje přijímačům rekonstruovat data z jakékoli dostatečné sady různých symbolů
- Minimalizuje režii protokolu pro spolehlivé doručování vysíláním/skupinovým přenosem

## Související pojmy

- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.947** (Rel-19) — FEC Evaluation for MBMS Enhancement
- **TS 28.318** (Rel-19) — Management and Orchestration for Energy Utilities

---

📖 **Anglický originál a plná specifikace:** [ESI na 3GPP Explorer](https://3gpp-explorer.com/glossary/esi/)
