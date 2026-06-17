---
slug: "mbms"
url: "/mobilnisite/slovnik/mbms/"
type: "slovnik"
title: "MBMS – Multimedia Broadcast Multicast Service"
date: 2026-01-01
abbr: "MBMS"
fullName: "Multimedia Broadcast Multicast Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mbms/"
summary: "Služba 3GPP umožňující efektivní doručování multimediálního obsahu (např. TV, aktualizace softwaru) od jednoho zdroje k mnoha příjemcům současně. Optimalizuje rádiové a síťové zdroje využitím vysílací"
---

MBMS je služba 3GPP, která efektivně doručuje multimediální obsah více uživatelům současně využitím vysílacích (broadcast) nebo skupinových (multicast) přenosových kanálů, čímž optimalizuje síťové zdroje pro hromadnou distribuci.

## Popis

Multimedia Broadcast Multicast Service (MBMS) je architektura služby typu point-to-multipoint standardizovaná 3GPP pro doručování dat z jedné zdrojové entity více příjemcům v definované servisní oblasti. Funguje přes jádro sítě (Core Network – CN) i přes rádiovou přístupovou síť (Radio Access Network – RAN). Služba je založena na dvou hlavních režimech přenosové služby: vysílacím režimu (Broadcast Mode) a skupinovém režimu (Multicast Mode). Ve vysílacím režimu může jakýkoli uživatel v rámci vysílací servisní oblasti přijímat data bez předplatného, zatímco skupinový režim vyžaduje, aby se uživatelé přihlásili k odběru a byli autorizováni pro připojení ke konkrétní skupině, což umožňuje řízenější poskytování služby a případné účtování.

Z architektonického hlediska MBMS zavádí nové funkční entity a rozhraní. Mezi klíčové síťové prvky patří Broadcast Multicast-Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), které slouží jako vstupní bod pro poskytovatele obsahu a stará se o oznamování služeb, plánování a zabezpečení (správu klíčů). V jádru sítě je MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) zodpovědný za přeposílání paketů, IP skupinovou distribuci a signalizaci řízení relace směrem k RAN. RAN, zahrnující Node B (pro UMTS) nebo [eNB](/mobilnisite/slovnik/enb/) (pro LTE/NR), spravuje přidělování rádiových zdrojů pro MBMS přenosy. Kritickým konceptem je MBMS Service Area, definovaná jako seznam MBMS Service Area IDs, kde každé ID představuje skupinu buněk. To umožňuje flexibilní geografické cílení relací obsahu.

Služba funguje tak, že pro relaci vytvoří kontext MBMS přenosového kanálu. BM-SC zahájí proceduru začátku relace, signalizací přes MBMS-GW k RAN a nakonec k uživatelskému zařízení (UE). RAN rozhodne o způsobu přenosu: buď použije vyhrazený přenosový kanál point-to-point (PTP) pro malý počet uživatelů, nebo sdílený přenosový kanál point-to-multipoint (PTM) (jako Single Frequency Network – [MBSFN](/mobilnisite/slovnik/mbsfn/) v LTE), když je přítomno mnoho uživatelů, čímž optimalizuje využití zdrojů. Na rádiovém rozhraní jsou MBMS data přenášena na společných fyzických kanálech (např. logický kanál [MTCH](/mobilnisite/slovnik/mtch/) mapovaný na PMCH v LTE). UE zájemce o službu monitorují řídicí kanály ([MCCH](/mobilnisite/slovnik/mcch/)) kvůli informacím o plánování a následně přijímají data na odpovídajícím přenosovém kanálu.

MBMS hraje zásadní roli při umožnění efektivních služeb hromadné komunikace. Je základem pro evolved Multimedia Broadcast Multicast Service (eMBMS) v LTE a NR, podporující funkce jako přenos MBSFN pro zlepšenou spektrální účinnost a kvalitu příjmu. Architektura podporuje jak streamovací služby (jako mobilní TV), tak služby doručování souborů pro distribuci. Její integrace s IP multicast v jádru sítě umožňuje škálovatelnou distribuci obsahu z jednoho zdroje k více uzlům v přenosové síti, což snižuje celkové zatížení sítě ve srovnání s replikovanými jednosměrnými (unicast) toky.

## K čemu slouží

MBMS bylo vytvořeno, aby řešilo zásadní neefektivitu používání jednosměrných (unicast) spojení pro doručování identického obsahu velkému počtu mobilních uživatelů současně. Před MBMS by služby jako mobilní TV vyžadovaly samostatný vyhrazený přenosový kanál pro každého diváka, což by rychle spotřebovalo dostupnou kapacitu rádiového a přenosového sítě, což by takové služby ve velkém měřítku činilo ekonomicky a technicky neproveditelnými. Technologie byla motivována rostoucí poptávkou po multimediálních službách a potřebou operátorů efektivněji využívat své frekvenční spektrum a síťovou infrastrukturu pro scénáře komunikace jeden-k-mnoha.

Historicky zavedené v 3GPP Release 6 (se základy v Release 99 pro [CBS](/mobilnisite/slovnik/cbs/)), poskytlo MBMS první standardizovaný rámec pro vysílání/skupinový přenos v celulárních sítích. Vyřešilo problém škálovatelného doručování obsahu zavedením sdílených rádiových a jádrových síťových přenosových kanálů. To umožnilo operátorům nabízet nové služby generující příjmy, jako je vysílání videa, rádia a rozsáhlé aktualizace softwaru pro flotily zařízení. Vytvoření MBMS také zavedlo nezbytný rámec zabezpečení a správy služeb (prostřednictvím [BM-SC](/mobilnisite/slovnik/bm-sc/)) pro podporu komerčních vysílacích a skupinových služeb, včetně správy předplatného pro skupinový přenos a ochrany obsahu.

## Klíčové vlastnosti

- Podporuje jak vysílací (otevřený), tak skupinový (na předplatném založený) režim služby
- Definuje flexibilní MBMS Service Areas pro cílené doručování obsahu
- Zavádí BM-SC pro poskytování služeb, plánování a správu zabezpečení
- Optimalizuje rádiové zdroje prostřednictvím dynamického přepínání mezi přenosem point-to-point a point-to-multipoint
- Využívá IP multicast v jádru sítě pro efektivní distribuci dat
- Poskytuje mechanismy pro oznamování a objevování služeb pro UE

## Související pojmy

- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBMS-GW – MBMS Gateway](/mobilnisite/slovnik/mbms-gw/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.146** (Rel-19) — MBMS Stage 1 Description
- **TS 22.246** (Rel-19) — MBMS User Services Specification
- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.741** (Rel-13) — MBMS/GCSE_LTE Architecture Enhancements Study
- … a dalších 109 specifikací

---

📖 **Anglický originál a plná specifikace:** [MBMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbms/)
