---
slug: "sack"
url: "/mobilnisite/slovnik/sack/"
type: "slovnik"
title: "SACK – Selective ACKnowledgement"
date: 2025-01-01
abbr: "SACK"
fullName: "Selective ACKnowledgement"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sack/"
summary: "Mechanismus protokolu TCP/IP, který umožňuje přijímači potvrdit nesouvislé bloky dat přijaté správně. Zvyšuje efektivitu v sítích s vysokými ztrátami tím, že odesílateli umožňuje znovuvyslat pouze kon"
---

SACK je mechanismus protokolu TCP/IP, který zvyšuje efektivitu v sítích s vysokými ztrátami tím, že umožňuje přijímači potvrdit nesouvislé datové bloky, což odesílateli umožňuje znovuvyslat pouze konkrétní chybějící segmenty.

## Popis

Selective ACKnowledgement (SACK, selektivní potvrzení) je volitelná funkce protokolu Transmission Control Protocol (TCP), definovaná v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) a odkazovaná ve specifikacích 3GPP pro transportní protokoly používané v mobilních sítích (např. v kontextu [GTP](/mobilnisite/slovnik/gtp/) nebo jiných IP přenašečů). Vylepšuje tradiční kumulativní mechanismus potvrzování TCP tím, že přijímači poskytuje schopnost informovat odesílatele o všech segmentech, které byly úspěšně přijaty, i když jsou mimo pořadí.

Ve standardním TCP bez SACK jsou potvrzení kumulativní. Přijímač odešle číslo [ACK](/mobilnisite/slovnik/ack/) představující nejvyšší souvislý bajt dat přijatý v pořádku. Pokud je segment 2 ztracen, ale segmenty 1, 3 a 4 dorazí, přijímač může potvrdit pouze bajt 1. To vede k nejednoznačnosti pro odesílatele, který může znovuvyslat segment 2 a podle některých algoritmů i segmenty 3 a 4 zbytečně (jev známý jako 'go-back-N'). SACK funguje tak, že do záhlaví TCP zahrnuje volbu SACK. Tato volba obsahuje seznam 'SACK bloků', z nichž každý popisuje souvislý rozsah dat, který přijímač úspěšně zařadil do fronty.

Architektonická implementace zahrnuje podporu volby SACK na obou koncových bodech TCP. Když přijímač obdrží nesouvislá data, zahrne do svých paketů ACK zpět odesílateli jeden nebo více SACK bloků. Například po přijetí segmentů s čísly sekvence 1000-1999 a 3000-3999, ale s chybějícím rozsahem 2000-2999, by ACK přijímače mělo číslo ACK 2000 (další očekávaný bajt) a SACK bloky pro 1000-1999 a 3000-3999. TCP zásobník odesílatele, používající algoritmy jako Selective Repeat, udržuje mapu potvrzených dat na základě těchto SACK bloků. Může pak znovuvyslat pouze konkrétní chybějící segment (2000-2999), přičemž ví, že pozdější data již přijímač má.

V sítích 3GPP je SACK relevantní pro optimalizaci přenosu dat přes bezdrátové spoje, které jsou ve srovnání s pevnými sítěmi náchylnější k vyšším ztrátám paketů a variabilitě. Je odkazován ve specifikacích týkajících se výkonu protokolů a správy přenašečů. Snižováním zbytečných retransmisí SACK šetří rádiové zdroje, snižuje latenci (zejména pro aplikace citlivé na kolísání zpoždění, jako je video) a zlepšuje celkovou propustnost. Jde o základní vylepšení TCP využívané ve vrstvě IP transportu, která podporuje datové služby 3GPP.

## K čemu slouží

SACK byl vyvinut k řešení zásadní neefektivity v původním mechanismu potvrzování TCP, který si vedl špatně v prostředích se ztrátami segmentů. Kumulativní model [ACK](/mobilnisite/slovnik/ack/) fungoval dostatečně pro rané sítě s nízkou mírou ztrát, ale na ztrátových trasách nebo trasách s vysokou latencí (jako rané bezdrátové sítě) způsoboval nadměrné retransmise a sníženou propustnost. Tento problém se stal známým jako 'problém nejednoznačnosti retransmise TCP'.

Vytvoření SACK bylo motivováno potřebou přesnějšího mechanismu zpětné vazby od přijímače k odesílateli. Předchozí přístupy, jako algoritmus TCP 'Fast Retransmit' založený na duplicitních ACK, pomáhaly, ale stále postrádaly úplné informace o tom, které konkrétní segmenty chybějí. SACK poskytuje explicitní zpětnou vazbu, což odesílateli umožňuje udržovat přesný obraz o stavu vyrovnávací paměti přijímače. Tím se řeší problém znovuvysílání dat, která přijímač již má, což plýtvá šířkou pásma a zvyšuje zpoždění.

V kontextu 3GPP přijetí a doporučení SACK (a souvisejících optimalizací TCP) ve specifikacích jako TS 44.064 pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) odráží historický vývoj mobilních datových služeb. Jak se objevily paketově přepínané služby ([GPRS](/mobilnisite/slovnik/gprs/), EDGE), charakteristiky bezdrátového spoje učinily výkon TCP kritickým problémem. Implementace SACK v koncových zařízeních a síťových serverech zlepšila uživatelský zážitek z prohlížení, stahování a streamování přes mobilní sítě, efektivně využívala vzácné rádiové zdroje a zmírňovala dopad chyb na rádiovém rozhraní na koncový transport.

## Klíčové vlastnosti

- Volba záhlaví TCP obsahující bloky potvrzených nesouvislých rozsahů dat
- Umožňuje odesílateli provádět selektivní retransmisi pouze chybějících segmentů
- Snižuje zbytečné retransmise a zlepšuje efektivitu využití šířky pásma
- Spolupracuje s TCP algoritmy, jako je Selective Repeat, pro správu okna odesílatele
- Zmírňuje degradaci výkonu v sítích s vysokými ztrátami (např. bezdrátových)
- Podporována většinou moderních implementací TCP a doporučena pro mobilní transport

## Související pojmy

- [ACK – Acknowledgement](/mobilnisite/slovnik/ack/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [SACK na 3GPP Explorer](https://3gpp-explorer.com/glossary/sack/)
