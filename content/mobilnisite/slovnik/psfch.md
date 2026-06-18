---
slug: "psfch"
url: "/mobilnisite/slovnik/psfch/"
type: "slovnik"
title: "PSFCH – Physical Sidelink Feedback Channel"
date: 2025-01-01
abbr: "PSFCH"
fullName: "Physical Sidelink Feedback Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psfch/"
summary: "Fyzický kanál pro zpětnou vazbu na postranním spoji (Physical Sidelink Feedback Channel, PSFCH) je vyhrazený kanál v rozhraní postranního spoje (sidelink) 5G NR pro přenos zpětné vazby hybridního auto"
---

PSFCH je vyhrazený fyzický kanál pro zpětnou vazbu na postranním spoji (Physical Sidelink Feedback Channel) v 5G NR pro přenos signálů HARQ ACK/NACK mezi zařízeními, což umožňuje spolehlivou přímou komunikaci pro služby jako V2X.

## Popis

Fyzický kanál pro zpětnou vazbu na postranním spoji (Physical Sidelink Feedback Channel, PSFCH) je kanál fyzické vrstvy definovaný v rámci protokolového zásobníku postranního spoje (sidelink, [SL](/mobilnisite/slovnik/sl/)) 5G New Radio (NR), specifikovaný primárně v 3GPP TS 38.212 a 38.213. Je mechanismem pro přenos potvrzovací zpětné vazby hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)) pro přenosy přijaté přes fyzický sdílený kanál postranního spoje ([PSSCH](/mobilnisite/slovnik/pssch/)). PSFCH nese informaci [HARQ-ACK](/mobilnisite/slovnik/harq-ack/), která udává, zda byl přenosový blok úspěšně dekódován ([ACK](/mobilnisite/slovnik/ack/)) či nikoliv ([NACK](/mobilnisite/slovnik/nack/)), což je zásadní pro umožnění opakovaných přenosů a dosažení spolehlivé komunikace v režimu přidělování prostředků postranního spoje Režim 1 (naplánovaný) a Režim 2 (autonomní).

Z architektonického hlediska je PSFCH mapován na specifické časově-frekvenční prostředky v rámci konfigurace fondu prostředků postranního spoje. Jeho přenos je úzce spjat s PSSCH, pro který poskytuje zpětnou vazbu. Struktura kanálu zahrnuje přenos založený na sekvencích. Přijímající UE generuje specifickou sekvenci (např. Zadoff-Chuovu sekvenci), jejíž cyklický posun nebo index prostředku implicitně nebo explicitně reprezentuje hodnotu HARQ-ACK (ACK nebo NACK) a může také identifikovat zdroj zpětné vazby. Tato sekvence je následně vysílána ve vyhrazených prostředcích PSFCH. Design je optimalizován pro nízkou režii a odolnost v potenciálně rušivém [D2D](/mobilnisite/slovnik/d2d/) prostředí.

Z provozního hlediska jeho fungování zahrnuje definovaný časový vztah. Poté, co UE přijme přenos PSSCH ve slotu, připraví HARQ-ACK na základě výsledku dekódování. Přenos PSFCH proběhne v následujícím slotu, s mezerou definovanou parametrem vyšší vrstvy sl-PSFCH-Period. Vysílající UE sleduje PSFCH kvůli zpětné vazbě. Po přijetí NACK může spustit opakovaný přenos stejného přenosového bloku podle nakonfigurovaného procesu HARQ. Tento mechanismus zpětné vazby se smyčkou významně zlepšuje spolehlivost komunikace po postranním spoji, což je klíčové pro bezpečnostně kritické zprávy [V2X](/mobilnisite/slovnik/v2x/) nebo datové relace.

PSFCH je klíčovou součástí podpory pokročilé QoS (Quality of Service) v NR postranním spoji. Funguje ve spojení s dalšími kanály postranního spoje, jako je PSCCH (řídicí) a PSSCH (datový). Jeho konfigurace, včetně periodicty, velikosti prostředků a řízení výkonu, je spravována sítí (v Režimu 1) nebo předkonfigurována (v Režimu 2). Role kanálu přesahuje základní HARQ; v pozdějších vydáních vylepšení podpořila zpětnou vazbu pro multicast (např. pouze NACK pro skupinový přenos) a koordinaci s procedurami snímání pro autonomní výběr prostředků, čímž se rozhraní postranního spoje stává robustním a efektivním pro dynamické scénáře přímé komunikace.

## K čemu slouží

PSFCH byl zaveden, aby splnil potřebu spolehlivé, nízkolatenční přímé komunikace v postranním spoji založeném na 5G NR, což je nástupce postranního spoje LTE (PC5). Zatímco postranní spoj LTE poskytoval základní broadcastové schopnosti pro veřejnou bezpečnost a V2X, měl omezenou podporu pro spolehlivý unicast a groupcast se zpětnou vazbou HARQ. Vytvoření PSFCH bylo motivováno přísnějšími požadavky pokročilých případů užití V2X (definovaných 3GPP), průmyslového IoT a aplikací veřejné bezpečnosti, které vyžadují vysokou spolehlivost a garantované doručování paketů pro bezpečnostně kritickou výměnu informací.

Předchozí přístupy v postranním spoji LTE se primárně spoléhaly na slepé opakované přenosy (opakování přenosu pevně daný počet opakování) k dosažení spolehlivosti, což je neefektivní a plýtvavé vůči spektrálním zdrojům. Absence vyhrazeného, nízkolatenčního kanálu pro zpětnou vazbu omezovala schopnost implementovat adaptivní opakované přenosy na základě skutečných podmínek kanálu. PSFCH to řeší zavedením standardizované, efektivní metody pro hlášení HARQ-ACK, což umožňuje adaptaci spojení se smyčkou a opakované přenosy na vyžádání. Tím se přímo řeší omezení mechanismu spolehlivosti s otevřenou smyčkou, což vede k efektivnějšímu využití spektra a spolehlivější komunikaci.

Historický kontext je evoluce z LTE komunikace mezi zařízeními (D2D) k postrannímu spoji 5G NR, který byl navržen od základu pro podporu širší škály služeb, včetně rozšířeného V2X (eV2X). PSFCH, jako součást návrhu fyzické vrstvy NR od vydání 16, byl zásadním prvkem umožňujícím podporu úrovní QoS NR přes rozhraní postranního spoje. Umožňuje postrannímu spoji podporovat služby s požadavky na chybovost paketů až 10^-5, čímž splňuje potřeby koordinace autonomního řízení, dálkového řízení a sdílení senzorů, kde je včasné a potvrzené doručení zpráv nezbytné.

## Klíčové vlastnosti

- Nese zpětnou vazbu HARQ-ACK (ACK/NACK) pro přenosy na postranním spoji přes PSSCH
- Používá modulaci založenou na sekvencích pro robustní přenos s nízkou režií
- Konfigurovatelná periodicita a prostředky v rámci fondu prostředků postranního spoje
- Podporuje zpětnou vazbu pro unicastové, groupcastové a broadcastové přenosy (s konkrétními režimy)
- Umožňuje opakované přenosy se smyčkou, čímž zvyšuje spolehlivost postranního spoje
- Integrální součást provozu NR postranního spoje Režim 1 (naplánovaný sítí) a Režim 2 (autonomní UE)

## Související pojmy

- [PSSCH – Physical Sidelink Shared Channel](/mobilnisite/slovnik/pssch/)
- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution

---

📖 **Anglický originál a plná specifikace:** [PSFCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/psfch/)
