---
slug: "sdcch"
url: "/mobilnisite/slovnik/sdcch/"
type: "slovnik"
title: "SDCCH – Stand-Alone Dedicated Control Channel"
date: 2025-01-01
abbr: "SDCCH"
fullName: "Stand-Alone Dedicated Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdcch/"
summary: "SDCCH je logický kanál GSM vyhrazený výhradně pro přenos signalizačních informací mezi mobilní stanicí a sítí. Používá se pro klíčové procedury, jako je sestavení hovoru, aktualizace polohy a přenos S"
---

SDCCH je logický kanál GSM vyhrazený výhradně pro přenos signalizačních informací pro procedury, jako je sestavování hovorů a přenos SMS, a funguje nezávisle na kanálech pro přenos uživatelských dat.

## Popis

Stand-Alone Dedicated Control Channel (SDCCH) je základní logický signalizační kanál v systému GSM (a později [GERAN](/mobilnisite/slovnik/geran/)). Funguje jako vyhrazený obousměrný bod-bod kanál mezi jednou mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BSS](/mobilnisite/slovnik/bss/)). Na rozdíl od kanálu pro přenos uživatelských dat ([TCH](/mobilnisite/slovnik/tch/)), který přenáší hlas nebo data, nebo společných řídicích kanálů ([CCCH](/mobilnisite/slovnik/ccch/)) používaných pro počáteční přístup, je SDCCH přidělen výhradně jedné MS po dobu trvání signalizační transakce. Jedná se o "samostatný" (stand-alone) kanál, protože může být přidělen a používán nezávisle na TCH.

Z architektonického hlediska je SDCCH namapován na fyzické zdroje. V časové doméně zabírá konkrétní časové sloty v rámcích [TDMA](/mobilnisite/slovnik/tdma/). Více SDCCH kanálů může být multiplexováno na jeden fyzický rádiový kmitočtový kanál (nosnou) přiřazením různých časových slotů a podkanálů. Běžná konfigurace je kombinovaná nosná [BCCH](/mobilnisite/slovnik/bcch/)/CCCH/SDCCH, kde časový slot 0 nese vysílací a společné kanály, zatímco jiné časové sloty mohou být nakonfigurovány pro přenos SDCCH (často v konfiguraci "SDCCH/8", která poskytuje 8 podkanálů). Kanál používá vyhrazenou strukturu fyzické vrstvy s vlastními tréninkovými sekvencemi pro ekvalizaci a podporuje jak plnorychlostní, tak poloviční verze.

SDCCH přenáší všechny klíčové signalizační zprávy vrstvy 3 po počátečním náhodném přístupu na [RACH](/mobilnisite/slovnik/rach/). Jeho klíčová operační role začíná poté, co síť přiřadí MS SDCCH prostřednictvím zprávy Immediate Assignment na AGCH. Jakmile je přidělen, MS používá SDCCH pro celý signalizační dialog. To zahrnuje autentizaci a nastavení šifrovacího režimu, aktualizaci polohy (s Visitor Location Register - VLR), kontrolu identity zařízení, signalizaci sestavení hovoru (jako odeslání volaného čísla a přijetí směrovacích informací) a přenos zpráv služby SMS (Short Message Service). Teprve po dokončení signalizace na SDCCH – například po úplném sestavení hovoru – síť přiřadí MS kanál pro přenos uživatelských dat (TCH) a SDCCH se uvolní. Pro SMS nebo aktualizace polohy, které nevyžadují TCH, transakce proběhne celá na SDCCH.

## K čemu slouží

SDCCH byl vytvořen k vyřešení kritického problému efektivního a spolehlivého řízení signalizace pro velký počet mobilních stanic bez blokování kapacity pro hlas. V raných mobilních systémech se řídicí signalizace často dělila o zdroje s přenosem uživatelských dat, což vedlo k zahlcení a selhání při sestavování hovorů. Koncepce GSM oddělila řídicí a uživatelskou rovinu. SDCCH poskytuje vyhrazený, garantovaný zdroj pro signalizaci, což zajišťuje, že se k základním síťovým přístupovým a řídicím procedurám nedostane méně prostředků kvůli zatížení přenosem dat a že jsou chráněny před interferencí.

Řeší omezení použití společných kanálů (jako RACH a AGCH) pro veškerou signalizaci, což by bylo neefektivní a pomalé pro transakce s více zprávami, jako je sestavení hovoru. Vyčleněním vyhrazeného kanálu může síť vést rozsáhlý, zabezpečený dialog (včetně nastavení šifrování) s mobilní stanicí. Jeho samostatná povaha je obzvláště důležitá, protože umožňuje signalizaci bez přidělení plnohodnotného kanálu pro přenos uživatelských dat, což je vzácný zdroj. To je zásadní pro služby mimo hovor, jako jsou SMS a periodické aktualizace polohy, které jsou časté, ale krátké. Koncepce SDCCH je základním kamenem robustnosti a kapacity GSM a umožňuje mu efektivně obsloužit miliony současných účastníků provádějících mix hlasových hovorů a služeb podobných datové signalizaci.

## Klíčové vlastnosti

- Vyhrazený signalizační kanál typu bod-bod
- Fungování nezávislé na kanálu pro přenos uživatelských dat (TCH)
- Podpora procedur autentizace a šifrování
- Používá se pro sestavení hovoru, aktualizaci polohy a SMS
- Multiplexován na fyzickou nosnou (např. SDCCH/8)
- Plnorychlostní a poloviční konfigurace

## Související pojmy

- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [AGCH – Access Grant Channel](/mobilnisite/slovnik/agch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [SDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdcch/)
