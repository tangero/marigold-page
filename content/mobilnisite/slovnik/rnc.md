---
slug: "rnc"
url: "/mobilnisite/slovnik/rnc/"
type: "slovnik"
title: "RNC – Radio Network Controller"
date: 2026-01-01
abbr: "RNC"
fullName: "Radio Network Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rnc/"
summary: "Řídicí síťový uzel v rádiové přístupové síti (UTRAN) 3G UMTS. Spravuje jednu nebo více stanic Node B, zajišťuje správu rádiových prostředků, funkce mobility a směrování uživatelských dat. Je klíčovým"
---

RNC je řídicí síťový uzel v rádiové přístupové síti (RAN) 3G UMTS, který spravuje Node B pro správu rádiových prostředků, mobility a směrování uživatelských dat a zároveň komunikuje s páteřní sítí.

## Popis

Řadič rádiové sítě (Radio Network Controller, RNC) je kritický síťový prvek v architektuře rádiové přístupové sítě ([UTRAN](/mobilnisite/slovnik/utran/)) 3G UMTS. Funguje jako řídicí uzel pro jednu nebo více základnových stanic známých jako Node B. RNC je zodpovědný za komplexní sadu řídicích a správních funkcí pro rádiové prostředky a mobilitu uživatelů ve své doméně. Z architektonického hlediska se RNC připojuje k Node B přes rozhraní Iub, k jiným RNC přes rozhraní Iur a k páteřní síti (obvody přepojené a paketově přepojené domény) přes rozhraní Iu. Tato pozice z něj činí centrální inteligenci UTRAN, která konsoliduje řízení z více Node B.

Funkční odpovědnosti RNC jsou rozsáhlé. V rámci správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) provádí úkoly, jako je řízení přístupu, řízení zahlcení, řízení předávání spojení a řízení výkonu. Spravuje přidělování a uvolňování rádiových přenosových kanálů (radio bearer), včetně vyhrazených kanálů ([DCH](/mobilnisite/slovnik/dch/)) a společných kanálů, jako je např. náhodný přístupový kanál ([RACH](/mobilnisite/slovnik/rach/)) a kanál s dopředným přístupem ([FACH](/mobilnisite/slovnik/fach/)). V oblasti mobility řídí RNC všechna předání spojení (měkká, měkčí, tvrdá) mezi buňkami pod jeho kontrolou a koordinuje s jinými RNC při předání mezi RNC přes rozhraní Iur. Také zajišťuje makro diverzitní kombinování a rozdělování pro spojení při měkkém předání. Z pohledu uživatelské roviny RNC provádí šifrování a ochranu integrity pro data a signalizaci a směruje pakety uživatelských dat mezi rozhraními Iub a Iu. V řídicí rovině RNC ukončuje protokol [RRC](/mobilnisite/slovnik/rrc/) a spravuje stavy připojení RRC (IDLE, CELL_FACH, CELL_DCH atd.) uživatelského zařízení (UE).

Role RNC se vyvíjela, ale zůstala ústřední ve všech 3GPP vydáních 99 až 14 pro sítě UMTS/[HSPA](/mobilnisite/slovnik/hspa/). V pozdějších vydáních se zavedením HSPA+ a funkcí jako je nepřetržité paketové připojení ([CPC](/mobilnisite/slovnik/cpc/)) a vylepšený CELL_FACH se algoritmy RNC staly složitějšími, aby zvýšily efektivitu a snížily latenci. RNC je centralizovaný prvek, který přinášel výhody silné koordinace, ale také představoval potenciální úzké hrdlo a jediný bod selhání. Tato architektura kontrastovala s plošší, více distribuovanou architekturou 4G LTE, kde byly funkce RNC z velké části integrovány do eNodeB, což vedlo k jeho postupnému vyřazení v 5G NR.

## K čemu slouží

RNC byl vytvořen jako součást původní architektury UMTS (3G), aby poskytl centralizovaný řídicí bod pro rádiovou přístupovou síť. Před 3G využívaly sítě 2G GSM řadič základnových stanic (BSC), který plnil podobný účel – spravoval více vysílacích a přijímacích stanic (BTS). RNC byl navržen tak, aby zvládal větší složitost UMTS založeného na WCDMA, který zavedl funkce jako měkké předání spojení (kdy je UE připojeno k více buňkám současně), rychlé řízení výkonu a dynamičtější správu rádiových prostředků.

Centralizovaný model RNC vyřešil několik problémů. Umožnil efektivní makro diverzitní kombinování pro měkké předání, které vyžadovalo centrální bod pro kombinování signálů z více Node B. Umožnil sofistikované RRM algoritmy, které mohly zohledňovat stav prostředků více buněk pod jeho kontrolou. Také zjednodušil návrh Node B, čímž z něj učinil relativně 'hloupou' rádiovou jednotku, což bylo výhodné z hlediska nákladů a nasazení na počátku roku 2000. RNC fungoval jako jediný kontaktní bod pro páteřní síť, skrývající mobilitu a rádiovou složitost UTRAN. Tato centralizace však také přinesla latenci, zejména pro data v uživatelské rovině, která musela být směrována přes RNC. Vývoj směrem k HSPA, který vyžadoval nižší latenci, začal tlačit některé funkce blíže k Node B, což připravilo půdu pro plně distribuovanou architekturu LTE.

## Klíčové vlastnosti

- Centralizovaný řadič pro jednu nebo více základnových stanic Node B v UTRAN
- Ukončuje protokol řízení rádiových prostředků (RRC) pro uživatelská zařízení (UE)
- Spravuje všechny typy předání spojení (měkká, měkčí, tvrdá) a makro diverzitní kombinování
- Provádí správu rádiových prostředků (RRM) včetně řízení přístupu, výkonu a zahlcení
- Poskytuje šifrování a ochranu integrity pro data v uživatelské a řídicí rovině
- Komunikuje s páteřní sítí přes rozhraní Iu a s jinými RNC přes rozhraní Iur

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- … a dalších 77 specifikací

---

📖 **Anglický originál a plná specifikace:** [RNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnc/)
