---
slug: "cdch"
url: "/mobilnisite/slovnik/cdch/"
type: "slovnik"
title: "CDCH – Control-plane Dedicated CHannel"
date: 2025-01-01
abbr: "CDCH"
fullName: "Control-plane Dedicated CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdch/"
summary: "Vyhrazený rádiový kanál v sítích GSM/EDGE používaný výhradně pro signalizaci na řídicí rovině mezi mobilními zařízeními a sítí. Přenáší kritické signalizační zprávy pro sestavení hovoru, správu mobili"
---

CDCH je vyhrazený rádiový kanál v sítích GSM/EDGE používaný výhradně pro signalizaci na řídicí rovině, který přenáší zprávy pro sestavení hovoru, správu mobility a přidělování prostředků odděleně od uživatelských dat.

## Popis

Control-plane Dedicated CHannel (CDCH) je základní součástí rádiových přístupových sítí GSM a [EDGE](/mobilnisite/slovnik/edge/), která poskytuje vyhrazený fyzický prostředek pro signalizaci na řídicí rovině mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a systémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)). Na rozdíl od kanálů pro přenos hovoru nebo uživatelských dat je CDCH přidělován výhradně pro signalizační účely během aktivních spojení, což zajišťuje, že kritické řídicí zprávy mají garantovanou šířku pásma a prioritu. Kanál funguje v rámci architektury rádiového rozhraní GSM a využívá specifické časové sloty a frekvenční alokace definované konfigurací kanálů sítě.

Z architektonického hlediska existuje CDCH v rámci rozhraní Um mezi MS a [BTS](/mobilnisite/slovnik/bts/) (Base Transceiver Station) a tvoří část vrstvy správy rádiových prostředků ([RR](/mobilnisite/slovnik/rr/)). Když mobilní zařízení naváže spojení vyžadující průběžnou signalizaci (například během hlasového hovoru nebo paketové datové relace), může síť přidělit CDCH spolu s kanálem pro přenos dat. Tento vyhrazený kanál zpracovává signalizační zprávy včetně hlášení o měření, příkazů k předání hovoru (handover), řízení šifrovacího režimu a přeřazení kanálů. Oddělení od uživatelského provozu zabraňuje zpoždění nebo ztrátě signalizace řídicí roviny v důsledku zahlcení sdílených kanálů.

CDCH funguje pomocí stejné struktury fyzické vrstvy jako ostatní kanály GSM, ale s odlišným mapováním logických kanálů. Typicky využívá konfiguraci s vyhrazeným časovým slotem, kde signalizace řídicí roviny zabírá specifické blesky v rámci struktury [TDMA](/mobilnisite/slovnik/tdma/) rámce. Kanál podporuje signalizaci jak v uplinku (z MS do sítě), tak v downlinku (ze sítě do MS) s odpovídajícími mechanismy ochrany proti chybám. Mezi klíčové protokoly fungující nad CDCH patří protokol správy rádiových prostředků (RR) a aspekty protokolu správy mobility ([MM](/mobilnisite/slovnik/mm/)), které vyžadují výměnu v reálném čase během aktivních spojení.

Přidělování a správa kanálu jsou řízeny řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) na základě konfigurace sítě a požadavků služeb. Když je přidělen, CDCH poskytuje spolehlivou cestu s nízkou latencí pro signalizaci řídicí roviny, která je nezbytná pro udržení kvality spojení, podporu událostí mobility, jako je předání hovoru, a umožnění pokročilých funkcí, jako je dvojitý přenosový režim, kdy hlasové a datové služby fungují současně. Vyhrazená povaha CDCH zajišťuje, že kritické funkce řízení sítě pracují s předvídatelným výkonem nezávisle na zatížení uživatelským provozem.

## K čemu slouží

CDCH byl zaveden, aby řešil omezení sdílených řídicích kanálů v raných sítích GSM, kde signalizace řídicí roviny soupeřila s uživatelským provozem o rádiové prostředky. Před vyhrazenými řídicími kanály sítě spoléhaly na společné řídicí kanály (jako CCCH) pro většinu signalizace, které se mohly během období vysokého provozu zahlcovat, což vedlo ke zpožděným nebo neúspěšným signalizačním zprávám. To bylo obzvláště problematické během aktivních hovorů, kde je včasné doručení příkazů k předání hovoru a hlášení o měření klíčové pro udržení kvality spojení.

Zavedení CDCH poskytlo řešení pro scénáře náročné na signalizaci, kde se sdílené kanály ukázaly jako nedostatečné. Během hlasových hovorů, paketových datových relací nebo kombinovaných služeb se objem a časové požadavky signalizace řídicí roviny výrazně zvyšují. CDCH zajišťuje, že tyto signalizační zprávy mají garantovanou šířku pásma a prioritu, což jim zabraňuje být zařazeny do fronty za uživatelskými daty. Toto oddělení je obzvláště důležité pro služby v reálném čase, kde by zpožděné příkazy k předání hovoru mohly vést ke ztrátě hovoru.

Historicky se CDCH objevil jako součást vylepšení GSM Phase 2+ pro podporu sofistikovanějších služeb a lepší správy mobility. Řešil rostoucí potřebu spolehlivé signalizace řídicí roviny, jak se sítě vyvíjely, aby podporovaly vyšší hustoty uživatelů, pokročilé funkce, jako jsou kodeky Enhanced Full Rate, a rané datové služby. Tím, že poskytoval vyhrazené prostředky pro komunikaci řídicí roviny, umožnil CDCH sítím udržet spolehlivost signalizace i při vysokém provozním zatížení, čímž položil základ pro pozdější vylepšení v evoluci GSM/EDGE.

## Klíčové vlastnosti

- Vyhrazené přidělení pro signalizaci řídicí roviny oddělené od uživatelského provozu
- Garantovaná šířka pásma a priorita pro kritické signalizační zprávy
- Podpora pro výměnu řídicích informací v uplinku i downlinku
- Integrace s TDMA rámcovou strukturou a alokací časových slotů GSM/EDGE
- Mechanismy ochrany proti chybám optimalizované pro spolehlivost řídicích zpráv
- Dynamické přidělování a uvolňování na základě požadavků spojení

## Související pojmy

- [DCCH – Dedicated Control Channel](/mobilnisite/slovnik/dcch/)
- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [CDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdch/)
