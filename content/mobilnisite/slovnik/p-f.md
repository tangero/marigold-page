---
slug: "p-f"
url: "/mobilnisite/slovnik/p-f/"
type: "slovnik"
title: "P/F – Poll/Final Bit"
date: 2025-01-01
abbr: "P/F"
fullName: "Poll/Final Bit"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/p-f/"
summary: "Jednobitové řídicí pole v hlavičkách protokolů vrstvy 2 (L2) systémů 3GPP, jako je RLC a LAPDm. Reguluje přenos rámců v potvrzovaném režimu a řídí, kdy má přijímač odeslat potvrzení nebo kdy může vysí"
---

P/F je jednobitové řídicí pole v hlavičkách protokolů vrstvy 2, které reguluje přenos rámců v potvrzovaném režimu řízením odpovědí přijímače a oprávnění vysílače pro nové rámce.

## Popis

Bit Poll/Final (P/F) je základní řídicí mechanismus používaný v protokolech linkové vrstvy v systémech 3GPP, zejména v Radio Link Control (RLC) Acknowledged Mode ([AM](/mobilnisite/slovnik/am/)) a v protokolu vrstvy 2 pro rozhraní Um (LAPDm). Jedná se o jeden bit v hlavičce protokolové datové jednotky (PDU). Přestože jde o jeden bit, plní dvojí funkci: když je odeslán vysílající stranou, označuje se jako bit Poll (P); když je odeslán přijímající stranou v odpovědi, označuje se jako bit Final (F). Jeho primární funkcí je řídit tok potvrzení a řídit přenos rámců při spolehlivém, spojovaném přenosu dat.

V RLC AM funguje bit P/F v obousměrném kontextu mezi UE a sítí (eNodeB/gNB). Když vysílač (např. RLC entita UE) nastaví bit P na '1' v datové nebo řídicí PDU, provádí "polling" přijímače. Tento dotaz je žádostí, aby přijímač okamžitě odeslal zpět STATUS PDU, které obsahuje informace o potvrzení ([ACK](/mobilnisite/slovnik/ack/) nebo [NACK](/mobilnisite/slovnik/nack/)) pro přijaté RLC PDU. To zajišťuje, že vysílač může zjistit chybějící segmenty a pokračovat v retransmisích nebo nových přenosech. Přijímač po detekci bitu P nastaveného na '1' musí odpovědět odesláním STATUS PDU s bitem F nastaveným na '1' při své další přenosové příležitosti na daném logickém kanálu.

Provoz je přísně řízen pravidlem: v libovolném okamžiku je povolen pouze jeden nevyřízený bit P (tj. dotaz čekající na odpověď s bitem F) na RLC entitu a směr. Tím se zabrání nejednoznačnosti potvrzení. Vysílač nesmí znovu nastavit bit P na '1', dokud neobdrží odpověď s bitem F nastaveným na '1'. Tím vzniká mechanismus podobný stop-and-wait pro řídicí signalizaci, který zajišťuje uspořádanou synchronizaci procesu potvrzování. Bit P/F je klíčový pro správu vysílacího okna RLC; pomocí dotazu může vysílač zjistit, které rámce byly úspěšně přijaty, a tím posunout své vysílací okno.

Mimo RLC koncept bitu P/F pochází ze starších protokolů linkové vrstvy, jako je [LAPD](/mobilnisite/slovnik/lapd/), a používá se v LAPDm pro signalizaci na GSM radiovém rozhraní. Jeho role je podobná: řídit dialog mezi mobilní stanicí a subsystémem základnové stanice pro spolehlivé doručování signalizačních zpráv vrstvy 3. Jednoduchost a účinnost jednobitového mechanismu P/F z něj učinily trvalou vlastnost napříč generacemi telekomunikačních protokolů, poskytující odlehčenou, ale robustní metodu pro synchronizaci a spolehlivost na často nespolehlivých bezdrátových spojích.

## K čemu slouží

Bit P/F existuje k řešení problému efektivní a spolehlivé výměny potvrzení ve spojovaném protokolu s posuvným oknem přes potenciálně ztrátový spoj. V bezdrátové komunikaci mohou být rámce ztraceny kvůli interferenci, útlumu nebo handoveru. Jednoduchý mechanismus automatického opakovaného dotazu ([ARQ](/mobilnisite/slovnik/arq/)) potřebuje způsob, jak přijímač informuje odesílatele o tom, které rámce byly přijaty správně. Zatímco periodická potvrzení jsou možná, zavádějí latenci. Bit P/F poskytuje mechanismus na vyžádání s nízkou režií, který umožňuje vysílači vyžádat si od přijímače okamžitý, aktuální stav potvrzení.

Historicky byl tento mechanismus převzat z protokolu [LAPD](/mobilnisite/slovnik/lapd/) [ISDN](/mobilnisite/slovnik/isdn/) do GSM LAPDm a následně do RLC UMTS a LTE/5G. Předchozí nebo alternativní přístupy bez takového dotazovacího mechanismu by se mohly spoléhat pouze na časovače, což by mohlo být neefektivní – buď by způsobovaly zbytečné hlášení stavu (plýtvání kapacitou), nebo by oddalovaly obnovu z chyb (zvýšení latence). Bit P umožňuje vysílači proaktivně spravovat svůj retransmisní buffer a vysílací okno na základě aktuálních síťových podmínek. Je zvláště důležitý pro udržování Quality of Service (QoS) pro služby citlivé na zpoždění, protože umožňuje rychlou retransmisi ztracených datových jednotek.

Motivací pro jeho pokračující používání napříč releasy je jeho minimální režie (jeden bit) a jeho účinnost v koordinaci dvou protějškových entit bez nutnosti složitých signalizačních kanálů mimo pásmo. Řeší omezení spočívající v tom, že je k dispozici pouze obousměrný logický link pro data a řízení, elegantně multiplexuje řídicí požadavky a odpovědi do stejného datového toku. V systémech 3GPP je základním kamenem pro dosažení spolehlivého doručování dat vyžadovaného pro signalizaci ([RRC](/mobilnisite/slovnik/rrc/), NAS) a pro některé služby přenosu v RLC AM.

## Klíčové vlastnosti

- Jednobit s dvojí funkcí: Poll (P) při odeslání vysílačem, Final (F) při odeslání přijímačem
- Spouští okamžitý přenos hlášení STATUS (např. RLC STATUS PDU)
- Vynucuje pouze jeden nevyřízený dotaz na RLC entitu a směr, aby se zabránilo nejednoznačnosti
- Řídí tok potvrzení v protokolech s potvrzovaným režimem (Acknowledged Mode - AM)
- Umožňuje efektivní retransmisi a posun okna v ARQ s posuvným oknem
- Poskytuje synchronizaci mezi stavovými automaty vysílače a přijímače

## Související pojmy

- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [P/F na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-f/)
