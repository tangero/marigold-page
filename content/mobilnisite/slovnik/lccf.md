---
slug: "lccf"
url: "/mobilnisite/slovnik/lccf/"
type: "slovnik"
title: "LCCF – Location Client Control Function"
date: 2025-01-01
abbr: "LCCF"
fullName: "Location Client Control Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lccf/"
summary: "LCCF je funkce jádra sítě v rámci architektury polohových služeb (LCS) 3GPP. Slouží jako primární rozhraní a řadič pro externí aplikace založené na polohových službách (LCS Clients) a spravuje jejich"
---

LCCF je funkce jádra sítě, která slouží jako primární rozhraní a řadič pro externí aplikace založené na polohových službách a spravuje jejich žádosti o lokalizaci mobilního zařízení.

## Popis

Location Client Control Function (LCCF) je logická entita definovaná v architektuře polohových služeb ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP. Nachází se v jádru sítě a slouží jako brána a řadič pro všechny polohové žádosti pocházející od externích subjektů, známých jako LCS Clients. Těmito klienty jsou typicky aplikace přidané hodnoty, služby tísňového volání (jako [PSAP](/mobilnisite/slovnik/psap/)) nebo orgány oprávněné k zákonnému odposlechu. Primární rolí LCCF je ověřit, autorizovat a spravovat životní cyklus polohové žádosti ([MT-LR](/mobilnisite/slovnik/mt-lr/), Mobile Terminated Location Request).

Po přijetí polohové žádosti od LCS Clienta přes rozhraní Le provádí LCCF několik klíčových funkcí. Nejprve autentizuje a autorizuje klienta na základě předkonfigurovaných služebních profilů a nastavení ochrany soukromí cílového uživatelského zařízení (UE). Poté interaguje s dalšími funkcemi sítě LCS, především s Location Retrieval Function ([LRF](/mobilnisite/slovnik/lrf/)) v řídicí rovině nebo se staršími architekturami s Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), aby orchestrovala proceduru určení polohy. LCCF je zodpovědná za správné formátování žádosti pro síť, výběr požadované kvality služby (QoS), jako je přesnost a doba odezvy, a za zpracování případných chyb nebo zamítnutí.

Z architektonického hlediska je LCCF klíčovou součástí servisní vrstvy LCS. Skrývá před externím klientem složitosti podkladových mechanismů určování polohy v rádiovém přístupu a jádru sítě (např. Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/), [UTDOA](/mobilnisite/slovnik/utdoa/), [A-GNSS](/mobilnisite/slovnik/a-gnss/)). Také vynucuje předpisy na ochranu soukromí kontrolou nastavení ochrany polohy účastníka a získáním potřebného souhlasu. V pozdějších vydáních 3GPP jsou její funkčnosti často integrovány v rámci nebo úzce spojeny s GMLC. LCCF zajišťuje, že polohové služby jsou poskytovány bezpečně, spolehlivě a v souladu s síťovými politikami i zákonnými požadavky.

## K čemu slouží

LCCF byla vytvořena za účelem poskytnutí standardizovaného, bezpečného a řízeného rozhraní mezi externími poskytovateli služeb a interními schopnostmi určování polohy mobilní sítě. Před její standardizací proprietární rozhraní ztěžovala poskytovatelům aplikací třetích stran přístup k polohovým informacím, což brzdilo inovace v polohových službách (LBS). LCCF tento problém řeší definicí jasného API (rozhraní Le) a řídicí funkce pro správu přístupu.

Řeší kritické problémy autorizace, ochrany soukromí a správy síťových zdrojů. Bez LCCF by externí klienti mohli potenciálně zahlcovat síť polohovými žádostmi nebo přistupovat k polohovým datům bez souhlasu uživatele. LCCF funguje jako bod vynucování politik a zajišťuje, že pouze autorizovaní klienti mohou podávat žádosti a že každá žádost je v souladu s nastavením ochrany soukromí cílového uživatele, jak je definováno v Home Subscriber Server (HSS) nebo v dedikovaném Privacy Profile Register (PPR).

Historicky, zavedena ve 3GPP R99, byla LCCF součástí základní architektury LCS, která umožnila komerční LBS a vylepšené služby tísňového volání (E911/E112). Oddělila servisní logiku od technologie určování polohy, což umožnilo síti vyvíjet své metody určování polohy (od Cell-ID k pokročilým technikám asistovaným GNSS) bez dopadu na externí klientské aplikace. Tato abstrakce byla klíčová pro škálovatelnou a bezpečnou komercializaci polohových služeb v globálních mobilních sítích.

## Klíčové vlastnosti

- Brána pro externí aplikace LCS Client
- Provádí autentizaci a autorizaci polohových žádostí
- Vynucuje politiky ochrany polohy účastníka a souhlas
- Spravuje parametry kvality služby (QoS) pro přesnost polohy/odezvu
- Orchestruje získání polohy interakcí s LRF/GMLC
- Poskytuje standardizované rozhraní (Le) pro servisní žádosti

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LRF – Location Retrieval Function](/mobilnisite/slovnik/lrf/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LCCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lccf/)
