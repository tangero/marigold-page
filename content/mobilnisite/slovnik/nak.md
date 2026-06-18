---
slug: "nak"
url: "/mobilnisite/slovnik/nak/"
type: "slovnik"
title: "NAK – Negative Acknowledgement"
date: 2025-01-01
abbr: "NAK"
fullName: "Negative Acknowledgement"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nak/"
summary: "Řídicí zpráva v komunikačních protokolech signalizující, že přenesený datový blok (např. paket nebo rámec) nebyl přijat správně nebo byl ztracen. Spouští retransmisi chybějících dat a tvoří základ mec"
---

NAK je řídicí zpráva signalizující, že datový blok nebyl přijat správně, což spouští retransmisi a je základním prvkem mechanismů řízení chyb ARQ a HARQ.

## Popis

Negativní potvrzení (NAK nebo [NACK](/mobilnisite/slovnik/nack/)) je základní zpětnovazební signál v protokolech vrstvy spojení dat a transportní vrstvy, který označuje neúspěšný příjem a dekódování konkrétní datové jednotky. V kontextu systémů 3GPP je nedílnou součástí mechanismů řízení chyb, jako je potvrzovaný režim ([AM](/mobilnisite/slovnik/am/)) řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) a protokol hybridního automatického opakovaného dotazu ([HARQ](/mobilnisite/slovnik/harq/)) používaný ve vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Když přijímač (např. UE nebo základnová stanice) detekuje chybu v přijatém transportním bloku prostřednictvím neúspěšné kontroly cyklickým redundantním kódem ([CRC](/mobilnisite/slovnik/crc/)) nebo identifikuje mezeru v sekvenci přijatých paketů, vygeneruje a odešle NAK pro tento konkrétní blok. Tato zpětná vazba je odeslána zpět vysílači, typicky na vyhrazeném řídicím kanálu, jako je fyzický uplinkový řídicí kanál ([PUCCH](/mobilnisite/slovnik/pucch/)) nebo fyzický downlinkový řídicí kanál ([PDCCH](/mobilnisite/slovnik/pdcch/)) pro HARQ, nebo v rámci stavových hlášení RLC pro ARQ.

Fungování zahrnuje přesnou identifikaci chybějících nebo chybných dat. V HARQ je každý transportní blok asociován s ID HARQ procesu a sekvenčním číslem (New Data Indicator). NAK pro konkrétní HARQ proces instruuje vysílač k retransmisi stejné nebo komplementární verze (inkrementální redundance) neúspěšného bloku. Přijímač následně kombinuje měkké bity z původního přenosu a retransmisí před novým pokusem o dekódování, čímž zvyšuje pravděpodobnost úspěchu. V RLC AM je NAK součástí STATUS PDU, které uvádí sekvenční čísla chybějících RLC servisních datových jednotek (SDU), čímž spouští selektivní retransmisi. Načasování zpětné vazby NAK je kritické; HARQ pracuje s velmi těsnými časovými lhůtami (řádově milisekundy) pro retransmisi s nízkou latencí, zatímco RLC ARQ pracuje v delších časových škálách, aby opravila reziduální chyby po HARQ.

Mechanismy NAK jsou základním kamenem spolehlivé bezdrátové komunikace, kompenzují inherentně náchylný rádiový kanál k chybám. Umožňují adaptivní opravu chyb tím, že reagují na aktuální podmínky kanálu. Efektivita celého systému výrazně závisí na přesnosti a rychlosti zpětné vazby NAK. Falešné NAK (hlášení ztráty, když byla data přijata) nebo nezachycené NAK mohou vést buď k nepotřebným retransmisím, nebo k trvalé ztrátě dat. Proto je samotný návrh zpětnovazebního kanálu robustní, často využívá silné kanálové kódování. Vzájemné působení mezi HARQ (rychlý, zaměřený na fyzickou vrstvu) a RLC ARQ (pomalejší, vyšší vrstva) vytváří vícevrstvou obranu proti chybám, přičemž NAK působí jako klíčový spouštěč v každé vrstvě k zachování integrity dat a doručování ve správném pořadí pro protokoly vyšších vrstev, jako je TCP.

## K čemu slouží

NAK existuje k řešení problému nespolehlivého přenosu dat přes kanály náchylné k chybám, zejména bezdrátového média v mobilních sítích. Bez mechanismu pro detekci a opravu chyb by byla data poškozena nebo ztracena, což by znemožnilo praktické digitální komunikace. Jednoduchá korekce dopředných chyb (FEC) přidává redundanci k opravě omezeného počtu chyb, ale stává se neefektivní při hlubokých útlumech nebo silném rušení. NAK umožňuje zpětnovazební retransmisi (ARQ), která je vysoce efektivní, protože spotřebovává zdroje pouze tehdy, když se chyby skutečně vyskytnou.

Historicky protokoly ARQ jako Stop-and-Wait, Go-Back-N a Selective Repeat používaly kladná potvrzení (ACK) a NAK pro řízení toku a chyb. Systémy 3GPP tento koncept rozvinuly pomocí HARQ, který těsně integruje FEC a ARQ. Motivací pro HARQ a s ním spojené signalizace NAK/ACK bylo dosažení velmi vysoké spolehlivosti a nízké latence pro paketové datové služby ve 3G (HSPA) a novějších systémech. Rychlý HARQ na fyzické/MAC vrstvě se zpětnou vazbou NAK (v řádu milisekund) řeší rychlé změny kanálu a poskytuje první linii obrany. ARQ na vyšší vrstvě RLC s NAK pak řeší reziduální chyby a zajišťuje spolehlivost end-to-end. Tento dvouvrstvý přístup řeší omezení čisté FEC (nadměrná režie v dobrých podmínkách) a čistého ARQ (vysoká latence způsobená dobou odezvy), čímž vytváří adaptivní a robustní systém řízení chyb, který je základním prvkem všech moderních rádiových rozhraní 3GPP.

## Klíčové vlastnosti

- Signalizuje selhání dekódování konkrétního datového bloku nebo sekvenčního čísla
- Spouští retransmisi v protokolech ARQ a HARQ
- Nedílná součást stavových hlášení potvrzovaného režimu (AM) RLC
- Odesílá se prostřednictvím řídicích kanálů fyzické vrstvy (např. PUCCH) pro HARQ
- Umožňuje kombinování inkrementální redundance v HARQ
- Nezbytný pro spolehlivé doručování dat ve správném pořadí

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [ACK – Acknowledgement](/mobilnisite/slovnik/ack/)

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [NAK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nak/)
