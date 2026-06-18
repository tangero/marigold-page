---
slug: "radl"
url: "/mobilnisite/slovnik/radl/"
type: "slovnik"
title: "RADL – Random Access Decodable Leading"
date: 2025-01-01
abbr: "RADL"
fullName: "Random Access Decodable Leading"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/radl/"
summary: "Fyzická vrstva konceptu v LTE a NR pro detekci preambule náhodného přístupu. Definuje úvodní sekvenci, kterou může základnová stanice dekódovat, aby identifikovala pokus uživatele o náhodný přístup, c"
---

RADL je fyzická vrstva sekvence v LTE a NR, kterou základnová stanice dekóduje, aby identifikovala pokus uživatele o náhodný přístup pro počáteční přístup k síti a synchronizaci v uplinku.

## Popis

Random Access Decodable Leading (RADL) je technický koncept definovaný ve specifikacích fyzické vrstvy 3GPP, konkrétně se týkající procedury kanálu náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)). Odkazuje na úvodní část preambule náhodného přístupu, signál vysílaný uživatelským zařízením (UE) k zahájení kontaktu se sítí. Tato úvodní sekvence je navržena se specifickými vlastnostmi – jako jsou dobré autokorelační a zkřížené korelační charakteristiky – které umožňují základnové stanici ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) robustně detekovat a dekódovat preambuli i v náročných rádiových podmínkách. Proces detekce zahrnuje korelaci přijímaného signálu základnovou stanicí proti sadě známých sekvencí preambule. Úspěšná shoda indikuje pokus o náhodný přístup, poskytuje síti hrubý odhad časového předstihu (timing advance) pro UE a identifikuje specifický index preambule, který může nést omezené informace (např. pro přístup s kolizemi vs. bez kolizí).

Architektura pro RADL je zabudována do návrhu fyzického kanálu náhodného přístupu ([PRACH](/mobilnisite/slovnik/prach/)). Samotná preambule je konstruována ze sekvence, jako je Zadoff-Chu ([ZC](/mobilnisite/slovnik/zc/)) sekvence v LTE nebo sekvence založená na Goldových kódech nebo ZC sekvencích v NR. Vlastnost 'decodable leading' zajišťuje, že počáteční část tohoto vysílaného průběhu je obzvláště odolná vůči šumu, interferenci a nejistotě časování. To je klíčové, protože procedura náhodného přístupu probíhá před navázáním jakéhokoli vyhrazeného spojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)); přesné časování a úrovně výkonu UE jsou neznámé. Zpracování fyzické vrstvy základnové stanice proto musí být schopno tuto úvodní sekvenci izolovat od pozadí, aby spustilo následné kroky odpovědi na náhodný přístup ([RAR](/mobilnisite/slovnik/rar/)).

Role RADL je základní pro vstup do sítě, předávání spojení (handover) a opětovnou synchronizaci v uplinku. Když se UE zapne, vrátí se z režimu nečinnosti (idle mode) nebo provádí předání spojení, použije RACH. Koncept RADL zajišťuje, že první krok – vysílání a detekce preambule – je spolehlivý. Jeho specifikace řídí parametry jako délka sekvence, kořenový index, cyklický posun a mapování časově-frekvenčních prostředků, které jsou podrobně popsány v 3GPP TS 36.211 (LTE) a 38.211 (NR). Výkonnost této dekódovatelné úvodní sekvence přímo ovlivňuje přístupovou latenci, míru úspěšnosti a celkovou kapacitu systému, protože určuje, kolik současných přístupových pokusů buňka dokáže rozlišit a správně zpracovat.

## K čemu slouží

Účelem RADL je poskytnout standardizovaný, robustní mechanismus pro počáteční detekci pokusů o náhodný přístup v celulárních sítích. Před navázáním vyhrazeného spojení musí UE signalizovat svou přítomnost síti, ale jeho vysílací časování není zarovnáno a jeho signál je slabý a potenciálně koliduje s ostatními. Preambule náhodného přístupu se svou dekódovatelnou úvodní částí řeší tento 'problém studeného startu' použitím známé, detekovatelné struktury signálu.

Historicky metody náhodného přístupu potřebovaly zvládnout rostoucí hustotu uživatelů a rozmanité scénáře nasazení (např. vysokorychlostní buňky, massive [MIMO](/mobilnisite/slovnik/mimo/)). Koncept RADL, formalizovaný ve specifikacích, zajišťuje, že návrh preambule splňuje přísné požadavky na pravděpodobnost detekce a míru falešných poplachů. Řeší omezení jednodušších přístupových signálů, které by mohly být náchylnější k interferenci nebo nebyly schopny podporovat velkou sadu rozlišitelných preambulí, což je nezbytné pro efektivní přístup s kolizemi v přeplněných buňkách. Definováním vlastností této úvodní sekvence 3GPP zaručuje interoperabilitu a předvídatelný výkon napříč zařízeními různých výrobců, což je pro ekosystém zásadní.

## Klíčové vlastnosti

- Definuje strukturu úvodní sekvence pro detekci preambule náhodného přístupu
- Umožňuje robustní detekci v přítomnosti šumu a časového posunu
- Podporuje procedury náhodného přístupu s kolizemi i bez kolizí
- Umožňuje počáteční odhad časování v uplinku pro UE
- Založeno na sekvencích s dobrými autokorelačními a zkříženými korelačními vlastnostmi (např. Zadoff-Chu)
- Specifikováno v technických specifikacích fyzické vrstvy (např. TS 36.211, 38.211)

## Související pojmy

- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)

## Definující specifikace

- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [RADL na 3GPP Explorer](https://3gpp-explorer.com/glossary/radl/)
