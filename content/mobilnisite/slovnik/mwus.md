---
slug: "mwus"
url: "/mobilnisite/slovnik/mwus/"
type: "slovnik"
title: "MWUS – MTC Wake Up Signal"
date: 2025-01-01
abbr: "MWUS"
fullName: "MTC Wake Up Signal"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mwus/"
summary: "Nízkopříkonový signál fyzické vrstvy v NB-IoT a LTE-M navržený k probouzení spících zařízení pro komunikaci typu stroj-stroj (MTC). Prodlužuje životnost baterie tím, že umožňuje zařízením přejít do hl"
---

MWUS je nízkopříkonový signál fyzické vrstvy v NB-IoT a LTE-M, který probouzí spící MTC zařízení za účelem prodloužení životnosti baterie tím, že indikuje čekající downlink data.

## Popis

Signál pro probuzení [MTC](/mobilnisite/slovnik/mtc/) (MWUS) je mechanismus pro úsporu energie zavedený pro technologie buněčného internetu věcí (CIoT) založené na LTE, konkrétně Narrowband IoT (NB-IoT) a LTE pro komunikaci typu stroj-stroj (LTE-M). Jde o signál fyzické vrstvy navržený k umožnění extrémní úspory energie u zařízení, která se převážně nacházejí ve stavu hlubokého spánku, známém jako režim úspory energie ([PSM](/mobilnisite/slovnik/psm/)) nebo rozšířený diskontinuální příjem (eDRX). Základní princip spočívá v oddělení nízkopříkonového monitorování síťového pagingu od vysokopříkonového provozu hlavního přijímače zařízení. Z architektonického hlediska je MWUS vysílán základnovou stanicí ([eNB](/mobilnisite/slovnik/enb/) pro LTE, gNB pro NR v některých kontextech) v downlinku. Je to jednoduchý, robustní a velmi krátký signál, který může být detekován obvodem ultra-nízkopříkonového přijímače (Wake-Up Receiver - WUR) uvnitř MTC zařízení. Tento WUR spotřebovává o několik řádů méně energie než hlavní přijímač LTE/NB-IoT zařízení. Samotný MWUS nenese konkrétní data; je to indikátor zapnutí/vypnutí. Jeho vysílání je koordinováno s pagingovou příležitostí zařízení. Jak to funguje: MTC zařízení nakonfigurované s podporou MWUS přejde do stavu hlubokého spánku, vypne téměř veškerou elektroniku kromě minimálního WUR. Síť, když má pro zařízení downlink data nebo signalizaci (jako mobilně-terminovaný požadavek), nejprve vysílá MWUS na předdefinovaném zdroji, synchronizovaném s vypočítanou MWUS příležitostí zařízení. WUR zařízení se periodicky probouzí na velmi krátkou dobu, aby zkontroloval přítomnost tohoto signálu. Pokud WUR detekuje MWUS, spustí hlavní aplikační procesor zařízení a primární přijímač LTE/NB-IoT, aby se plně zapnul. Zařízení poté pokračuje v monitorování své skutečné pagingové příležitosti ([PO](/mobilnisite/slovnik/po/)) obvyklým způsobem, aby přijalo pagingovou zprávu obsahující podrobnosti downlink transakce. Pokud není detekován žádný MWUS, WUR se vrátí do spánku a hlavní přijímač zůstane vypnutý, čímž se ušetří značné množství energie. Konfigurace MWUS, včetně jeho periodicity a rádiových zdrojů, je signalizována zařízení prostřednictvím zpráv řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) nebo systémových informací. Tento mechanismus je klíčovým prvkem umožňujícím životnost baterie přesahující 10 let pro určité IoT aplikace.

## K čemu slouží

MWUS byl vytvořen k řešení kritické výzvy v hromadné komunikaci typu stroj-stroj (mMTC): dosažení ultra-dlouhé životnosti baterie, často desetileté nebo delší, pro stacionární nebo zřídka komunikující senzory a měřiče. Před MWUS se úspora energie spoléhala na [PSM](/mobilnisite/slovnik/psm/) a eDRX, kde zařízení spí dlouhá období, ale stále musí periodicky probouzet svůj plný, energeticky náročný LTE přijímač, aby zkontrolovala pagingové zprávy. Toto 'slepé' probouzení znamená významné energetické náklady, i když žádná data nečekají. MWUS to řeší zavedením dvoukrokového procesu probuzení. Problém, který řeší, je energie promrhaná během těchto zbytečných aktivací plného přijímače. Motivace byla dána přísnými požadavky odvětví (chytré měřiče), zemědělských senzorů a zařízení pro monitorování infrastruktury, kde je výměna baterií nákladná nebo nemožná. Tím, že umožní zařízení zůstat ve velmi hlubokém spánku a používat drobný specializovaný obvod k naslouchání jednoduchému 'probouzejícímu' signálu, je spotřeba energie během nečinných období drasticky snížena. Tato inovace přímo prodlužuje provozní životnost zařízení, čímž činí buněčný IoT životaschopnou a konkurenceschopnou technologií pro širší škálu nízkopříkonových aplikací široké oblasti ([LPWA](/mobilnisite/slovnik/lpwa/)). Byla to klíčová funkce zavedená ve 3GPP Release 15 jako součást pokračujících vylepšení pro CIoT, konkrétně za účelem posunutí hranic energetické účinnosti za to, co bylo možné pouze s PSM a eDRX.

## Klíčové vlastnosti

- Ultra-nízkopříkonový přijímač pro probuzení (WUR) pro detekci signálu
- Signál fyzické vrstvy (MWUS) vysílaný před pagingovými příležitostmi
- Významně snižuje spotřebu energie během nečinných období
- Aplikovatelný pro technologie NB-IoT i LTE-M (eMTC)
- Konfigurovatelný prostřednictvím RRC signalizace pro flexibilní profily úspory energie
- Umožňuje prodloužení životnosti baterie přes 10 let pro vhodné IoT aplikace

## Související pojmy

- [PSM – Protocol State Machine](/mobilnisite/slovnik/psm/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [MWUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mwus/)
