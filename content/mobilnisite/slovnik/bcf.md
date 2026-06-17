---
slug: "bcf"
url: "/mobilnisite/slovnik/bcf/"
type: "slovnik"
title: "BCF – Base station Control Function"
date: 2025-01-01
abbr: "BCF"
fullName: "Base station Control Function"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bcf/"
summary: "Base station Control Function (BCF) je logická řídicí entita v řadiči základnových stanic (BSC) v GSM/EDGE rádiové přístupové síti (GERAN). Spravuje rádiové zdroje, řídí hovorové spojení pro služby s"
---

BCF je logická řídicí entita v řadiči základnových stanic (BSC) systému GSM, která spravuje rádiové zdroje, řídí přepojování okruhů (circuit-switched) a koordinuje více základnových přijímačů/vysílačů (BTS) pro navázání, udržení a ukončení rádiových spojení.

## Popis

Base station Control Function (BCF) je klíčová logická komponenta v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)), konkrétně umístěná v řadiči základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). Působí jako centrální řídicí a procesní jednotka pro skupinu základnových přijímačů/vysílačů ([BTS](/mobilnisite/slovnik/bts/)). BCF je zodpovědná za správu všech rádiových zdrojů ve svěřeném geografickém území, známém jako lokalizační oblast ([LA](/mobilnisite/slovnik/la/)) nebo směrovací oblast (RA). Provádí kritické úlohy v reálném čase, jako je přidělování rádiových kanálů, řízení předávání hovorů mezi buňkami (handover), řízení výkonu a koordinace přeskakování kmitočtů napříč připojenými BTS. Centralizací této kontroly BCF zajišťuje efektivní využití rádiového spektra a udržuje kontinuitu služeb pro mobilní uživatele.

Z architektonického hlediska se BCF propojuje s BTS přes rozhraní Abis, přes které vysílá řídicí příkazy a přijímá měřicí reporty. Také se připojuje k jádru sítě (CN) přes rozhraní A pro služby s přepojováním okruhů, kde komunikuje s ústřednou mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)). Vnitřně se BCF skládá z několika podfunkcí: funkce správy rádiových zdrojů (RRM) obstarává přidělování a uvolňování kanálů; funkce řízení předávání hovorů (Handover Control) spravuje proces přechodu hovoru mezi buňkami; a funkce provozu a údržby (O&M) podporuje konfiguraci, správu poruch a monitorování výkonu BTS pod její kontrolou.

Během provozu BCF zpracovává měřicí reporty od mobilních stanic ([MS](/mobilnisite/slovnik/ms/)) a BTS, aby mohla činit inteligentní rozhodnutí o přidělování rádiových zdrojů. Například při sestavování hovoru BCF vybere vhodný hovorový kanál (TCH) na základě aktuálního zatížení a úrovní interference. Průběžně monitoruje kvalitu a sílu signálu a v případě potřeby iniciuje předání hovoru do buňky s lepším pokrytím. BCF také implementuje algoritmy pro řízení výkonu, kdy udílí pokyny MS a BTS k úpravě vysílacího výkonu za účelem minimalizace interference a šetření životnosti baterie při zachování kvality hovoru. Dále spravuje přidělování signalizačních kanálů (jako SDCCH a [BCCH](/mobilnisite/slovnik/bcch/)) pro komunikaci řídicí roviny.

Její role sahá až k podpoře různých služeb GSM, včetně hlasových hovorů (Full Rate a Enhanced Full Rate), dat s přepojováním okruhů (přes CSD a HSCSD) a doručování SMS přes rádiové rozhraní. Centralizovaný řídicí model BCF byl charakteristickým rysem architektury sítí 2G GERAN, což kontrastuje s distribuovanějším řízením v pozdějších sítích 3G UMTS a 4G LTE. Zatímco její funkční odpovědnosti byly v následujících generacích z velké části absorbovány nebo přerozděleny (např. na RNC v UMTS a eNodeB v LTE), porozumění BCF je nezbytné pro pochopení vývoje paradigmat řízení rádiových přístupových sítí.

## K čemu slouží

BCF byla vytvořena, aby řešila potřebu centralizované a efektivní kontroly rádiových zdrojů v průkopnickém buněčném systému GSM. Před GSM měly systémy první generace (1G) omezené a často decentralizované řídicí mechanismy, což vedlo k neefektivnímu využití spektra, nespolehlivému předávání hovorů a obtížím se škálováním sítí. BCF jako součást BSC byla zavedena, aby tyto problémy vyřešila poskytnutím vyhrazeného, inteligentního řadiče, který dokáže řídit více rádiových lokalit (BTS) současně.

Jejím primárním účelem je optimalizace využití vzácného rádiového spektra – kritického zdroje v buněčných sítích. Centralizací kontroly může BCF provádět dynamické přidělování kanálů v široké oblasti, vyvažovat zatížení mezi buňkami a provádět složité algoritmy předávání hovorů, aby udržela kvalitu hovoru, když se uživatelé pohybují. Tato centralizovaná inteligence umožňuje pokročilé funkce, jako je přeskakování kmitočtů (pro potlačení interference a útlumu), řízení výkonu (ke snížení interference a spotřeby energie) a nespojitý přenos (DTX) pro detekci hlasové aktivity. Tyto schopnosti byly nezbytné pro dosažení vysoké kapacity, spolehlivosti a kvality hovoru, které definovaly komerční úspěch GSM.

Historicky BCF představovala významnou architektonickou inovaci oddělující řídicí rovinu (řešenou BCF/BSC) od přenosu uživatelských dat (který prochází BTS). Toto oddělení umožnilo sofistikovanější správu sítě, snazší zavádění nových služeb a škálovatelné rozšiřování. Řešilo to omezení dřívějších systémů, kde bylo rádiové řízení buď příliš jednoduché, nebo příliš těsně svázané s rádiovým hardwarem. Model BCF se ukázal jako velmi úspěšný pro hlas a data s přepojováním okruhů a vytvořil základ, na kterém byly později vybudovány vylepšení jako GPRS a EDGE, a to i když se architektura vyvíjela směrem k paketově orientovaným, IP-based sítím v 3GPP a dále.

## Klíčové vlastnosti

- Centralizovaná správa rádiových zdrojů (RRM) pro skupinu BTS
- Dynamické přidělování hovorových (TCH) a signalizačních kanálů
- Řízení a provedení předání hovoru mezi buňkami (handover)
- Algoritmy řízení výkonu pro uplink a downlink
- Správa a koordinace přeskakování kmitočtů
- Správa rozhraní Abis (k BTS) a A (k MSC)

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [BCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcf/)
