---
slug: "fec"
url: "/mobilnisite/slovnik/fec/"
type: "slovnik"
title: "FEC – Forward Erasure Correction / Forward Error Correction"
date: 2026-01-01
abbr: "FEC"
fullName: "Forward Erasure Correction / Forward Error Correction"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fec/"
summary: "Technika kódování kanálu, která k přenášeným informacím přidává redundantní data, což umožňuje přijímači detekovat a opravit chyby bez nutnosti žádat o opakovaný přenos. Je zásadní pro spolehlivý přen"
---

FEC (Forward Erasure Correction / Forward Error Correction) je technika kódování kanálu, která k přenášeným informacím přidává redundantní data, což umožňuje přijímači detekovat a opravit chyby bez nutnosti žádat o opakovaný přenos.

## Popis

Forward Error Correction (FEC, dopředná korekce chyb) je základní technika digitálního zpracování signálu používaná k řízení chyb při přenosu dat přes nespolehlivé nebo šumové komunikační kanály. V systémech 3GPP funguje FEC tak, že vysílač zakóduje zprávu redundantním způsobem pomocí kódu pro opravu chyb ([ECC](/mobilnisite/slovnik/ecc/)). Tato redundance umožňuje přijímači detekovat omezený počet chyb, které se mohou vyskytnout kdekoli ve zprávě, a často tyto chyby opravit bez nutnosti žádosti o opakovaný přenos. Proces zahrnuje přidání paritních bitů nebo použití složitějších algebraických struktur k původním datovým bitům před přenosem odesílatelem. Při příjmu dekodér tyto dodatečné bity použije k identifikaci a opravě bitových chyb způsobených rušením kanálu, jako je interference, útlum nebo šum.

Architektura FEC v 3GPP pokrývá více vrstev a technologií rádiového přístupu (GSM, UMTS, LTE, NR). Na fyzické vrstvě jsou specifikovány konvoluční kódy, Turbo kódy (zavedené v UMTS), kódy s nízkou hustotou parity ([LDPC](/mobilnisite/slovnik/ldpc/), pro datové kanály NR) a polární kódy (Polar codes, pro řídicí kanály NR). Tyto kódy se aplikují na transportní kanály po procesech, jako je kódování kanálu, přizpůsobení rychlosti a prokládání. Konkrétní kód a kódovací rychlost se volí na základě podmínek kanálu a požadované spolehlivosti, často jako součást adaptace spojení. Výkon je charakterizován kódovým ziskem, což je snížení potřebného poměru signálu k šumu pro danou míru bitových chyb ve srovnání s nekódovaným přenosem.

Role FEC je klíčová pro dosažení cílů kvality služeb (QoS) pro různé služby. Pro hlas zajišťuje srozumitelnost; pro paketová data udržuje propustnost a snižuje latenci tím, že se vyhýbá opakovaným přenosům na vyšších vrstvách, jako jsou ty z vrstvy řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)). Ve vyvinutých systémech je hybridní automatické opakování dotazu ([HARQ](/mobilnisite/slovnik/harq/)) kombinováno s FEC, kde počáteční přenos používá slabý FEC kód a následné opakované přenosy poskytují přírůstkovou redundanci, kterou dekodér může kombinovat, čímž se zvyšuje účinnost. Specifikace podrobně popisují struktury kódů, kódovací/dekódovací algoritmy a požadavky na výkon pro různé kanály (např. [PDSCH](/mobilnisite/slovnik/pdsch/), [PUSCH](/mobilnisite/slovnik/pusch/), [PBCH](/mobilnisite/slovnik/pbch/)) napříč všemi vydáními 3GPP, což zajišťuje interoperabilitu a robustní komunikaci.

## K čemu slouží

FEC byla vytvořena k řešení inherentní nespolehlivosti bezdrátových komunikačních kanálů. Na rozdíl od drátových médií jsou rádiové kanály náchylné k časově proměnným rušením, jako je vícecestný útlum, interference a aditivní bílý Gaussovský šum, které způsobují bitové chyby. Bez FEC by systémy spoléhaly výhradně na protokoly opakovaného přenosu ([ARQ](/mobilnisite/slovnik/arq/)), které zavádějí významnou latenci a snižují spektrální účinnost, zejména pro služby v reálném čase, jako je hlas nebo video. Primárním účelem FEC je proaktivně bojovat proti těmto chybám na fyzické vrstvě a zlepšit hrubou míru bitových chyb (BER), než jsou data předána vyšším vrstvám.

Historicky se v rané digitální komunikaci používaly jednoduché kontroly parity a blokové kódy. GSM od 3GPP původně používalo konvoluční kódování. Motivace se vyvíjela s UMTS a potřebou vyšších datových rychlostí, což vedlo k přijetí Turbo kódů, které nabízely výkon blízko Shannonova limitu. Kontinuální vývoj přes LTE až k 5G NR je poháněn požadavky na ultra-spolehlivou komunikaci s nízkou latencí (URLLC), rozšířené mobilní širokopásmové připojení (eMBB) a komunikaci s masivním počtem strojů (mMTC). Každá nová třída služeb má odlišné požadavky na spolehlivost a latenci, což vyžaduje pokročilejší schémata FEC, jako jsou LDPC a polární kódy, aby poskytly vyšší kódový zisk, nižší složitost a lepší přizpůsobivost než předchozí generace.

FEC řeší problém udržení cílové míry chyb bloků (BLER) za náročných podmínek signálu bez nadměrného vyzařovacího výkonu. Je klíčovým prvkem pro spektrální účinnost, umožňuje sítím pracovat s vyššími řády modulace (např. 256-QAM, 1024-QAM) tím, že poskytuje nezbytnou odolnost proti chybám. Snížením počtu potřebných opakovaných přenosů FEC přímo přispívá k nižší latenci a vyšší propustnosti, což jsou klíčové ukazatele výkonu moderních mobilních sítí. Je to základní technologie, bez které by spolehlivá digitální mobilní komunikace nebyla možná.

## Klíčové vlastnosti

- Podporuje více kódovacích schémat: Konvoluční, Turbo, LDPC a polární kódy napříč různými generacemi 3GPP
- Umožňuje provoz hybridního ARQ (HARQ) poskytováním paketů s přírůstkovou redundancí
- Integruje se s adaptací spojení pro dynamický výběr kódovacích rychlostí na základě kvality kanálu
- Poskytuje kódový zisk, snižuje potřebný SNR pro cílovou míru chyb
- Specifikováno pro všechny kritické fyzické kanály (např. PDSCH, PUSCH, PBCH, PDCCH)
- Umožňuje spolehlivý přenos pro různé služby od hlasu po ultra-spolehlivou komunikaci s nízkou latencí

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- … a dalších 42 specifikací

---

📖 **Anglický originál a plná specifikace:** [FEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fec/)
