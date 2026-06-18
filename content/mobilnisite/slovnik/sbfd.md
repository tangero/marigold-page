---
slug: "sbfd"
url: "/mobilnisite/slovnik/sbfd/"
type: "slovnik"
title: "SBFD – Sub-Band non-overlapping Full Duplex"
date: 2025-01-01
abbr: "SBFD"
fullName: "Sub-Band non-overlapping Full Duplex"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbfd/"
summary: "Technologie rádiového přístupu umožňující současný přenos a příjem na jediné nosné vlně rozdělením frekvenčního pásma na oddělená, nepřekrývající se podpásma pro uplink a downlink. Zvyšuje spektrální"
---

SBFD je technologie rádiového přístupu, která umožňuje současný přenos a příjem na jediné nosné vlně rozdělením frekvenčního pásma na oddělená, nepřekrývající se podpásma pro uplink a downlink.

## Popis

Sub-Band non-overlapping Full Duplex (SBFD) je pokročilý duplexní režim zavedený ve specifikaci 3GPP Release 18 pro NR (New Radio). Funguje na jediné nosné frekvenci, ale rozděluje dostupnou šířku pásma na odlišná, nepřekrývající se podpásma vyhrazená pro přenosy uplink ([UL](/mobilnisite/slovnik/ul/)) a downlink ([DL](/mobilnisite/slovnik/dl/)). To umožňuje základnové stanici (gNB) nebo uživatelskému zařízení (UE) vysílat a přijímat současně v rámci stejné nosné, na rozdíl od duplexu s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)), který střídá přenosy v čase, nebo duplexu s kmitočtovým dělením ([FDD](/mobilnisite/slovnik/fdd/)), který vyžaduje spárované spektrum s ochranným pásmem. Architektura zahrnuje sofistikovaný návrh [RF](/mobilnisite/slovnik/rf/) front-endu, digitální zpracování signálu a algoritmy potlačení interference pro zvládnutí vlastní interference mezi vysílací a přijímací cestou. Mezi klíčové komponenty patří plánování s ohledem na SBFD ve vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), procedury fyzické vrstvy definované pro hlášení informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a sondovací referenční signály ([SRS](/mobilnisite/slovnik/srs/)) v SBFD slotech a mechanismy přidělování zdrojů, které koordinují UL a DL zdroje v rámci podpásem. Jeho úlohou v síti je významně zvýšit spektrální účinnost, snížit latenci pro aplikace jako XR a průmyslový IoT a poskytnout flexibilnější využití zdrojů ve srovnání s konvenčními duplexními režimy, čímž tvoří základní technologii pro vývoj 5G-Advanced směrem k 6G.

## K čemu slouží

SBFD bylo vytvořeno, aby řešilo rostoucí poptávku po vyšší spektrální účinnosti a nižší latenci v sítích 5G-Advanced a překonalo tak omezení stávajících duplexních metod. Tradiční FDD vyžaduje spárované spektrum, které je nedostatkové a drahé, zatímco TDD zavádí latenci kvůli přepínacím mezerám a vyžaduje přísnou synchronizaci v celé síti. SBFD to řeší tím, že umožňuje plně duplexní provoz na jediné nosné, čímž efektivně zdvojnásobuje využití dostupného spektra a umožňuje okamžitou obousměrnou komunikaci. Historický kontext vychází z výzkumu in-band full-duplexu, který čelil výzvám s potlačením vlastní interference. Přístup SBFD s nepřekrývajícími se podpásmy poskytuje praktičtější implementaci oddělením TX a RX frekvencí, což snižuje složitost interference a umožňuje jeho komerční nasazení. Řeší potřebu zvýšené kapacity pro hustá městská nasazení, ultra-spolehlivou komunikaci s nízkou latencí (URLLC) a efektivní podporu asymetrických provozních vzorů.

## Klíčové vlastnosti

- Současný přenos uplink a downlink na jediné nosné vlně
- Přidělování nepřekrývajících se podpásem v rámci šířky pásma nosné
- Zvýšená spektrální účinnost ve srovnání s TDD a FDD
- Snížená latence díky eliminaci přepínacích mezer TDD
- Flexibilní přidělování zdrojů přizpůsobitelné asymetrii provozu
- Podpora pokročilých technik správy a potlačení interference

## Definující specifikace

- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.922** (Rel-19) — Study on IMT Parameters for NR in Higher Bands

---

📖 **Anglický originál a plná specifikace:** [SBFD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbfd/)
