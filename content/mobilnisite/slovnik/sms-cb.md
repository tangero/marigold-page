---
slug: "sms-cb"
url: "/mobilnisite/slovnik/sms-cb/"
type: "slovnik"
title: "SMS-CB – Short Message Service – Cell Broadcast"
date: 2025-01-01
abbr: "SMS-CB"
fullName: "Short Message Service – Cell Broadcast"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sms-cb/"
summary: "SMS-CB je služba vysílání typu jeden-všem, která doručuje zprávy všem mobilním zařízením v konkrétní geografické oblasti, známé jako buňka. Používá se pro veřejná varování, nouzové výstrahy a lokalitn"
---

SMS-CB je služba vysílání typu jeden-všem, která doručuje zprávy, jako jsou veřejná varování nebo nouzové výstrahy, na všechna mobilní zařízení v rámci konkrétní geografické oblasti buňky.

## Popis

Short Message Service – Cell Broadcast (SMS-CB) je standardizovaný vysílací mechanismus v sítích 3GPP navržený pro současné rozesílání informací všem uživatelským zařízením (UE) v definované geografické oblasti pokrytí, typicky buňce nebo skupině buněk. Na rozdíl od konvenčních bod-bod [SMS](/mobilnisite/slovnik/sms/), které pro každého příjemce vytvářejí vyhrazené signalizační spojení, SMS-CB funguje na jednosměrném, nespojovaném základě. Klíčovým síťovým prvkem pro SMS-CB je Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), který je propojen s jádrem sítě, konkrétně s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo s funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC. CBC formátuje vysílané zprávy, přiřazuje jim identifikátor zprávy a sériové číslo a předává je příslušným základnovým stanicím (eNodeB v LTE, gNB v NR) přes příslušná rozhraní (např. SBC-AP).

Vysílací proces začíná, když aplikace, jako je systém veřejného varování, odešle zprávu do CBC s parametry, jako je geografický rozsah, obsah zprávy a plán opakování. CBC určí sadu buněk, které tvoří cílovou oblast, a zprávu odpovídajícím způsobem distribuuje. Po přijetí vysílaných informací základnová stanice naplánuje zprávu na specifické rádiové zdroje v rámci Cell Broadcast Channel ([CBCH](/mobilnisite/slovnik/cbch/)) v GSM nebo v blocích systémových informací (SIBs) v LTE a NR. Zpráva je opakovaně vysílána po definované období, aby ji mohla přijmout i UE vstupující do oblasti nebo dočasně mimo pokrytí.

Na straně UE zařízení průběžně monitoruje vysílací kanál pro zprávy. Každá vysílaná zpráva obsahuje identifikátor zprávy a sériové číslo, což umožňuje UE filtrovat a zobrazovat zprávy bez duplicit. Uživatelé mohou typicky povolit nebo zakázat příjem určitých kategorií zpráv (např. komerčních vysílání), zatímco nouzová varování jsou často povinná k přijetí a zobrazení. Architektura zajišťuje síťovou efektivitu pro hromadná oznámení, protože využívá stávající vysílací kanály bez vytváření individuální signalizační zátěže pro každé UE, což ji činí vysoce škálovatelnou pro šíření nouzových a veřejných informací.

## K čemu slouží

SMS-CB byl vytvořen pro řešení kritické potřeby efektivní, současné komunikace s velkou populací v konkrétní geografické oblasti, což je schopnost, která chyběla tradičním bod-bod telekomunikačním službám. Jeho hlavní motivací byla veřejná bezpečnost, což umožňuje orgánům vydávat okamžitá varování před přírodními katastrofami, teroristickými hrozbami nebo jinými mimořádnými událostmi přímo na mobilní telefony občanů. Historicky měly předchozí výstražné systémy, jako sirény nebo televizní/rozhlasové vysílání, omezení v dosahu, přesnosti cílení a spolehlivosti.

Mimo nouzové situace SMS-CB řeší problém efektivního doručování lokalitně vázaných informací, jako jsou dopravní aktualizace, varování před počasím nebo komerční reklamy, všem uživatelům v relevantní oblasti bez zahlcování sítě individuálními zprávami. Řeší omezení bod-bod [SMS](/mobilnisite/slovnik/sms/), které se stává neefektivním a síťově náročným, když musí být stejná zpráva odeslána tisícům zařízení v husté městské buňce. Využitím inherentní vysílací povahy rádiového rozhraní poskytuje SMS-CB škálovatelné, nízkolatenční a síťové zdroje šetřící řešení pro komunikaci typu jeden-všem, což je základní požadavek pro moderní celulární systémy veřejného varování a přidané služby.

## Klíčové vlastnosti

- Geograficky cílené vysílání pro všechna UE v určených buňkách
- Nespojovaný provoz nevyžadující vyhrazenou signalizaci na UE
- Filtrování zpráv a detekce duplicit pomocí identifikátoru zprávy a sériového čísla
- Podpora více jazyků zpráv a znakových sad
- Konfigurovatelné plány opakování a doby platnosti
- Povinná schopnost příjmu pro třídy zpráv nouzového varování

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [SMS-CB na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-cb/)
