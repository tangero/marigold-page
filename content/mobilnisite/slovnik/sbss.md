---
slug: "sbss"
url: "/mobilnisite/slovnik/sbss/"
type: "slovnik"
title: "SBSS – Serving Base Station Subsystem"
date: 2025-01-01
abbr: "SBSS"
fullName: "Serving Base Station Subsystem"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sbss/"
summary: "Serving Base Station Subsystem (SBSS) je kompletní sada zařízení rádiové přístupové sítě obsluhujících mobilního účastníka v daném okamžiku v síti GSM/UMTS. Zahrnuje Serving Base Station Controller (S"
---

SBSS je kompletní sada zařízení rádiové přístupové sítě, včetně řídicí jednotky a jí připojených základnových stanic, která obsluhuje aktivní spojení mobilního účastníka v síti GSM nebo UMTS.

## Popis

Serving Base Station Subsystem (SBSS) je funkční a architektonický koncept ve specifikacích 3GPP, který označuje souhrn entit rádiové přístupové sítě zodpovědných za poskytování služby konkrétní mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelskému zařízení (UE) během spojení. V kontextu GSM a jeho evoluce ([GERAN](/mobilnisite/slovnik/geran/)) se SBSS skládá z Serving Base Station Controller ([SBSC](/mobilnisite/slovnik/sbsc/)) a jedné či více základnových stanic ([BTS](/mobilnisite/slovnik/bts/)). V kontextu UMTS a jeho architektury [UTRAN](/mobilnisite/slovnik/utran/) zahrnuje analogický koncept Serving Radio Network Controller ([SRNC](/mobilnisite/slovnik/srnc/)) a jím řízené Node B, ačkoli termín SBSS je historicky více spjat s terminologií GSM.

SBSS není jediné fyzické zařízení, ale logické seskupení definované pro každou účastnickou relaci. Jeho složení je dynamické; pro mobilní zařízení ve volání nebo datové relaci SBSS zahrnuje [BSC](/mobilnisite/slovnik/bsc/), který aktuálně řídí spojení (obsluhující BSC), a konkrétní BTS (nebo více BTS v případě měkkého předávání v pozdějších technologiích), která aktivně komunikuje s mobilním zařízením. SBSC funguje jako řídicí jednotka, provádí správu rádiových prostředků, rozhoduje o předávání spojení a zajišťuje připojení k jádru sítě. BTS poskytuje fyzické rádiové rozhraní, zajišťuje modulaci, demodulaci a vysílání/příjem rádiových signálů.

Z pohledu signalizace sítě a správy mobility je identita SBSS klíčová. Uzly jádra sítě, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Serving GPRS Support Node (SGSN), komunikují se SBSS (prostřednictvím SBSC) za účelem správy účastnické relace. Během událostí mobility, jako je předávání spojení, se SBSS může změnit. Například při předávání mezi BSC je spojení mobilního zařízení převedeno z jednoho SBSS (zdrojové SBSS) na jiné (cílové SBSS). SBSS je také ústřední pro služby založené na poloze a účtování, protože identifikuje geografickou oblast, kde je účastník obsluhován. Ve specifikacích jsou parametry jako Cell Global Identity (CGI) a identifikátor BSC součástí definice kontextu SBSS pro uživatele.

## K čemu slouží

Koncept Serving Base Station Subsystem byl vyvinut, aby poskytl jasný a standardizovaný způsob, jakým může jádro sítě identifikovat a komunikovat s konkrétní sadou rádiového zařízení obsluhujícího mobilního uživatele. V raných celulárních systémech bylo nutné abstrahovat složitost rádiové přístupové sítě pro ústředny jádra sítě. MSC potřebovalo vědět, 'kde' je účastník připojen v rádiové síti, aby mohlo směrovat hovory a spravovat mobilitu, ale nemuselo spravovat jednotlivé rádiové buňky.

SBSS slouží jako tato abstraktní vrstva. Řeší problém korelace účastnické relace s řídicím prvkem rádiové sítě (BSC) a jeho prostředky. To je nezbytné pro funkce jako sestavení hovoru (MSC kontaktuje správný BSC pro přidělení rádiového kanálu), koordinace předávání spojení (signalizace mezi MSC a BSC) a zákonné odposlechy. Poskytuje také rámec pro provozní a údržbové funkce, což operátorům sítí umožňuje sledovat, který subsystém obsluhuje které uživatele.

Jeho definice byla motivována modulární architekturou GSM, která čistě oddělila Base Station Subsystem (BSS) od Network Switching Subsystem (NSS). Aspekt 'Serving' zdůrazňuje dynamickou, na uživatele zaměřenou povahu asociace, což byl klíčový pokrok oproti pevným telefonním sítím. Tento konceptuální model se osvědčil jako robustní a byl přenesen do 3G UMTS s konceptem Serving RNC (SRNC), čímž byla zajištěna konzistentní pravidla pro mobilitu a správu relací napříč generacemi.

## Klíčové vlastnosti

- Logické seskupení obsluhujících prvků rádiové sítě (BSC a BTS) na uživatele
- Dynamická entita, která se mění během mobility účastníka a předávání spojení
- Slouží jako řídicí bod a rozhraní mezi rádiovým přístupem a jádrem sítě
- Identifikována parametry jako BSC ID a Cell Global Identity (CGI)
- Ústřední pro procedury správy mobility (aktualizace polohy, předávání spojení)
- Poskytuje kontext pro účtování a zákonné odposlechy v rádiové doméně

## Související pojmy

- [SBSC – Serving Base Station Controller](/mobilnisite/slovnik/sbsc/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [SBSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbss/)
