---
slug: "pur"
url: "/mobilnisite/slovnik/pur/"
type: "slovnik"
title: "PUR – Preconfigured Uplink Resource"
date: 2026-01-01
abbr: "PUR"
fullName: "Preconfigured Uplink Resource"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pur/"
summary: "PUR (Preconfigured Uplink Resource) je funkcionalita 3GPP umožňující IoT zařízením vysílat uplink data bez provedení procedury náhodného přístupu, což snižuje latenci a spotřebu energie. Umožňuje síti"
---

PUR je funkcionalita 3GPP, která umožňuje IoT zařízením vysílat uplink data pomocí předem přidělených periodických prostředků bez náhodného přístupu, čímž snižuje latenci a spotřebu energie pro aplikace mMTC a energeticky efektivní IoT.

## Popis

Preconfigured Uplink Resource (PUR) je mechanismus definovaný v 3GPP Release 16 a novějších, primárně pro technologie LTE-M a NB-IoT, který umožňuje UE vysílat uplink data na předem přidělených prostředcích bez zahájení procedury kanálu náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)). Toho je dosaženo tak, že síť nakonfiguruje UE specifickými časově-frekvenčními prostředky (např. periodické subrámečky nebo resource bloky) během stavu [RRC](/mobilnisite/slovnik/rrc/) Connected, které přetrvávají, i když UE přejde do stavů RRC Idle nebo Inactive. UE může tyto prostředky použít k přímému odeslání dat, čímž obchází typické kroky vysílání preambule náhodného přístupu, příjmu [RAR](/mobilnisite/slovnik/rar/) a žádosti o plánování, a tím zjednodušuje proces přenosu.

Z architektonického hlediska PUR zahrnuje koordinaci mezi UE a eNodeB (pro LTE-M/NB-IoT) nebo gNodeB (pro NR-IoT). Konfigurace je stanovena prostřednictvím RRC signalizace, například pomocí zprávy RRCConnectionSetup nebo RRCConnectionReconfiguration, která obsahuje parametry jako periodicita PUR, časový offset, frekvenční umístění, schéma modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) a nastavení řízení výkonu. Tyto prostředky jsou přidělovány typicky bez soutěžení, což znamená, že jsou vyhrazeny pro konkrétní UE, ačkoli mohou být podporovány i varianty se soutěžením. Síť si udržuje přehled o přidělených PUR prostředcích a naslouchá na vyhrazených prostředcích, což umožňuje okamžité dekódování příchozích přenosů bez předchozích povolení k plánování.

Jak PUR funguje operačně: Když má UE data k odeslání, zkontroluje, zda je aktivní platná konfigurace PUR a zda aktuální čas odpovídá předkonfigurované příležitosti prostředku. Pokud ano, přenese data přímo pomocí přiřazených prostředků s využitím nakonfigurovaných parametrů pro výkon a modulaci. Síť při úspěšném příjmu může odpovědět potvrzením nebo downlink daty, aniž by vyžadovala, aby UE plně přešlo zpět do stavu RRC Connected. Tím se snižuje signalizační režie a latence, což je zvláště výhodné pro sporadické malé datové pakety typické pro IoT senzory. Konfigurace PUR mohou být pravidelně validovány prostřednictvím vyhrazených procedur, aby byla zajištěna synchronizace, a mohou být uvolněny nebo aktualizovány na základě mobility UE nebo síťových podmínek.

## K čemu slouží

PUR byl vytvořen, aby řešil neefektivnosti tradičních procedur náhodného přístupu a žádosti o plánování pro IoT zařízení, která často přenášejí malé, nepravidelné datové pakety. V LTE-M a NB-IoT před Release 16 vyžadoval každý uplink přenos proceduru [RACH](/mobilnisite/slovnik/rach/), zahrnující výměnu více zpráv, která spotřebovala značnou energii a přidávala latenci. To bylo neoptimální pro use case hromadné komunikace strojového typu (mMTC), jako jsou chytré měřiče nebo environmentální senzory, kde jsou zařízení omezena výdrží baterie a potřebují fungovat roky bez dobíjení.

Motivace pro PUR vychází z potřeby zlepšit úsporu energie a snížit signalizační režii v IoT sítích. Eliminací procesu RACH pro předkonfigurované přenosy PUR minimalizuje dobu, po kterou je rádio UE aktivní, a tím prodlužuje životnost baterie. Také snižuje zahlcení sítě způsobené častými pokusy o náhodný přístup od milionů zařízení, čímž zlepšuje škálovatelnost pro masivní IoT nasazení. To je v souladu s cíli 3GPP pro vývoj 5G, podporující ultra-lean design a efektivní podporu různorodých IoT aplikací.

Historicky dřívější řešení jako Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)) a rozšířené nespojité přijímání (eDRX) pomáhala s energetickou účinností, ale neoptimalizovala samotnou fázi přenosu. PUR je doplňuje tím, že zjednodušuje uplink komunikaci. Řeší omezení předchozích přístupů, kde latence a spotřeba energie byly v kompromisu; PUR umožňuje přenosy s nízkou latencí bez obětování energetické účinnosti, což z něj činí klíčový prvek pro kritické IoT služby a průmyslovou automatizaci v rámci architektury 5G.

## Klíčové vlastnosti

- Umožňuje uplink přenos bez procedury náhodného přístupu
- Snižuje latenci pro malé datové pakety
- Snižuje spotřebu energie UE minimalizací signalizace
- Podporuje prostředky bez soutěžení i se soutěžením
- Konfigurovatelné pomocí RRC signalizace ve stavech idle/inactive
- Zvyšuje škálovatelnost pro masivní IoT nasazení

## Související pojmy

- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks

---

📖 **Anglický originál a plná specifikace:** [PUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pur/)
