---
slug: "h-arq"
url: "/mobilnisite/slovnik/h-arq/"
type: "slovnik"
title: "H-ARQ – Hybrid Automatic Repeat Request"
date: 2025-01-01
abbr: "H-ARQ"
fullName: "Hybrid Automatic Repeat Request"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/h-arq/"
summary: "Klíčový retransmisní protokol linkové vrstvy kombinující korekci chyb vpřed (FEC) a ARQ. Zlepšuje spolehlivost a spektrální účinnost na bezdrátových kanálech tím, že vyžaduje retransmise chybně přijat"
---

H-ARQ je retransmisní protokol linkové vrstvy, který kombinuje korekci chyb vpřed s automatickými žádostmi o opakování, aby zlepšil spolehlivost a spektrální účinnost prostřednictvím retransmise a měkkého kombinování chybně přijatých datových paketů.

## Popis

Hybrid Automatic Repeat Request (H-ARQ) je základní mechanismus řízení chyb používaný v datové linkové vrstvě (vrstva 2) 3GPP rádiových přístupových technologií, včetně LTE a NR. Označení 'hybridní' pochází z toho, že spojuje dvě klasické techniky: korekci chyb vpřed ([FEC](/mobilnisite/slovnik/fec/)) a automatickou žádost o opakování ([ARQ](/mobilnisite/slovnik/arq/)). Primárním cílem je dosáhnout vysoce spolehlivého přenosu dat přes inherentně nespolehlivý a časově proměnlivý bezdrátový kanál při zachování dobré spektrální účinnosti.

H-ARQ funguje na bázi transportního bloku. Když vysílač (např. gNB v downlinku nebo UE v uplinku) odešle datový paket, zahrne redundantní FEC bity (kanálové kódování, jako Turbo kódy v LTE nebo [LDPC](/mobilnisite/slovnik/ldpc/)/Polar kódy v NR). Příjemce se pokusí paket dekódovat. Pokud dekódování selže (detekováno pomocí cyklického redundantního součtu - [CRC](/mobilnisite/slovnik/crc/)), příjemce nezahodí poškozené informace v podobě měkkých bitů (analogové hodnoty reprezentující přijímaný signál). Místo toho uloží tuto 'měkkou' informaci do vyrovnávací paměti zvané H-ARQ buffer a odešle zpět vysílači záporné potvrzení ([NACK](/mobilnisite/slovnik/nack/)) přes zpětnovazební kanál (např. na Physical Uplink Control Channel - PUCCH).

Po přijetí NACK vysílač provede retransmisi. Klíčové je, že H-ARQ využívá různé 'redundantní verze' (RV). Retransmise nemusí být identickou kopií původního paketu. Může obsahovat jinou sadu paritních bitů (FEC redundance) ze stejného mateřského kódu. Příjemce pak provede 'měkké kombinování', při kterém kombinuje novou sadu měkkých bitů z retransmise s uloženými měkkými bity z předchozího neúspěšného pokusu. Tento kombinovaný signál má vyšší efektivní poměr signálu k šumu (SNR), čímž se zvyšuje pravděpodobnost úspěšného dekódování. Tento proces retransmise a měkkého kombinování pokračuje, dokud není paket úspěšně dekódován (což vede k [ACK](/mobilnisite/slovnik/ack/)), nebo dokud není dosaženo maximálního počtu retransmisí, načež může převzít kontrolu ARQ vyšší vrstvy (RLC vrstva).

Systémy 3GPP implementují více paralelních H-ARQ procesů (např. až 8 v LTE, 16 v NR), aby udržely kontinuální tok dat. Zatímco jeden proces čeká na zpětnou vazbu/retransmisi, ostatní mohou být použity k odesílání nových dat, čímž se skryje latence doby odezvy. Správu těchto procesů, včetně plánování retransmisí a přiřazování indikátorů nových dat ([NDI](/mobilnisite/slovnik/ndi/)), zajišťuje vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). H-ARQ je hlavním důvodem vysoké spolehlivosti a účinnosti moderních celulárních systémů, protože umožňuje systému zpočátku pracovat s vyššími mírami chybovosti bloků s vědomím, že většinu chyb lze efektivně opravit rychlými retransmisemi.

## K čemu slouží

H-ARQ byl vyvinut, aby překonal závažná omezení použití samotného čistého ARQ nebo samotné čisté FEC na bezdrátových kanálech. Čisté ARQ, které při chybě jednoduše retransmituje pakety, se za špatných podmínek kanálu stává velmi neefektivním kvůli častým retransmisím a s nimi spojeným zpožděním. Čistá FEC, která přidává každému přenosu značnou redundanci pro opravu chyb, plýtvá šířkou pásma, když je kanál dobrý, a stále může selhat, když je kanál velmi špatný.

Hybridní přístup byl motivován potřebou adaptivnějšího a účinnějšího schématu řízení chyb. Kombinací přiměřené úrovně FEC s rychlým retransmisním mechanismem umožňuje H-ARQ systému pracovat blíže kapacitě kanálu. Počáteční přenos používá právě tolik FEC, aby opravil nejčastější chyby. Pro méně časté, hlubší útlumy nebo interferenční události, které způsobí selhání dekódování, dodatečná redundance poskytovaná retransmisemi (s měkkým kombinováním) funguje jako dodatečná FEC na vyžádání. Tato strategie 'chase combining' nebo 'incremental redundancy' dramaticky zlepšuje výkon.

Jeho vytvoření bylo zásadní pro podporu služeb s vysokou přenosovou rychlostí ve 3G (HSDPA zavedlo H-ARQ) a stalo se základním kamenem pro 4G LTE a 5G NR. Řeší kritický problém nespolehlivých rádiových spojení tím, že poskytuje rychlý mechanismus obnovy soustředěný na fyzickou vrstvu, který minimalizuje latenci a maximalizuje propustnost. To je obzvláště důležité pro aplikace s nízkou latencí a pro udržení vysoké spektrální účinnosti, což je klíčový ekonomický faktor pro mobilní síťové operátory. H-ARQ efektivně způsobuje, že bezdrátové spojení se vyšším protokolovým vrstvám jeví jako spolehlivější a účinnější.

## Klíčové vlastnosti

- Kombinuje korekci chyb vpřed (FEC) a ARQ retransmise
- Používá měkké kombinování více přenosových pokusů v přijímači
- Využívá více paralelních procesů pro udržení kontinuálního toku dat
- Funguje s nízkou latencí na MAC/fyzické vrstvě
- Podporuje různé redundantní verze (RV) pro přírůstkovou redundanci
- Spoléhá se na zpětnou vazbu ACK/NACK odesílanou přes řídicí kanály (např. PUCCH/PUSCH)

## Související pojmy

- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.914** (Rel-19) — Multimedia Telephony over IP Optimization
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [H-ARQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-arq/)
