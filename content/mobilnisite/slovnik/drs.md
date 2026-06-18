---
slug: "drs"
url: "/mobilnisite/slovnik/drs/"
type: "slovnik"
title: "DRS – Discovery Reference Signal"
date: 2025-01-01
abbr: "DRS"
fullName: "Discovery Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/drs/"
summary: "Referenční signál v downlinku v LTE a NR používaný pro objevování zařízení a měření v komunikaci zařízení-zařízení (D2D) a sidelink komunikaci. Umožňuje uživatelskému zařízení (UE) detekovat blízká za"
---

DRS je referenční signál v downlinku používaný v LTE a NR pro objevování zařízení a měření v D2D a sidelink komunikaci, který umožňuje uživatelskému zařízení (UE) detekovat blízká zařízení a navazovat přímé spoje.

## Popis

Discovery Reference Signal (DRS) je signál fyzické vrstvy definovaný ve specifikacích 3GPP pro LTE (od verze Release 13) a následně pro NR. Jeho primární funkcí je usnadňovat objevování mezi blízkými uživatelskými zařízeními (UE) bez nutnosti koordinovaného plánování sítí pro každý pokus o objevení, což umožňuje efektivní komunikaci zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)) a sidelink komunikaci. V kontextu LTE je specifikován pro sidelink objevování, zatímco v NR platí podobné koncepty pro sidelink synchronizaci a objevování.

Z architektonického hlediska je DRS vysílán UE, které chce být objevitelné (tzv. announcing UE), na předem nakonfigurovaných nebo sítí přidělených rádiových zdrojích ve spektru sidelink. Struktura signálu zahrnuje specifické sekvence a zabírá definované zdrojové prvky v časově-frekvenční mřížce. Monitorující UE prohledává tyto nakonfigurované zdroje, detekuje DRS a měří jeho charakteristiky, jako je přijímaný výkon a časování. To umožňuje monitorující UE identifikovat přítomnost, identitu (prostřednictvím zprávy pro objevování, která často signál doprovází) a přibližnou polohu/vzdálenost announcing UE.

DRS funguje ve spojení s protokoly vyšších vrstev pro služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)). Fyzický signál poskytuje robustní mechanismus detekce na nízké úrovni, zatímco zprávy pro objevování přenášejí informace aplikační vrstvy. Mezi klíčové komponenty patří generování sekvence DRS, mechanismy přidělování zdrojů (režim 1: plánováno sítí; režim 2: autonomní výběr UE) a související měřicí reporty. Jeho role je klíčová pro zahájení přímých komunikačních spojů ve scénářích veřejné bezpečnosti, aplikacích vozidlo-vše ([V2X](/mobilnisite/slovnik/v2x/)) a komerčních službách založených na blízkosti, čímž se odlehčuje provoz od jádra sítě a snižuje se latence.

## K čemu slouží

DRS byl vytvořen, aby řešil potřebu efektivního, škálovatelného a sítí řízeného objevování mezi zařízeními v těsné blízkosti. Před standardizovaným [D2D](/mobilnisite/slovnik/d2d/) objevováním taková funkčnost vyžadovala, aby zařízení používala nelicencované spektrum (např. Wi-Fi Direct nebo Bluetooth), kterému chyběla integrace s bezpečností, mobilitou a kontinuitou služeb mobilní sítě. Motivací bylo umožnit nové služby, jako je komunikace pro veřejnou bezpečnost, kde si první respondenti potřebují komunikovat přímo, a [V2X](/mobilnisite/slovnik/v2x/), kde se vozidla musí vzájemně detekovat s vysokou spolehlivostí a nízkou latencí.

Řeší problém, jak může UE efektivně najít jiná UE zájmu bez neustálé, rozsáhlé signalizace přes síťovou infrastrukturu. Předchozí mobilní systémy byly čistě uplink/downlink; DRS zavedl kanál pro objevování na sidelink. To umožňuje síti spravovat zdroje a politiky pro objevování, zatímco samotný proces detekce je prováděn lokálně mezi zařízeními, čímž se šetří síťové zdroje a umožňuje se ultra rychlé navázání spojení, které je klíčové pro bezpečnostní aplikace. Jeho zavedení v Rel-13 pro LTE představovalo významný krok ve vývoji mobilních sítí od čistě infrastrukturních k podpoře přímé komunikace mezi zařízeními.

## Klíčové vlastnosti

- Signál fyzické vrstvy navržený pro robustní detekci ve sidelink spektru
- Podporuje jak síťově plánované (Režim 1), tak autonomní (Režim 2) přidělování zdrojů UE
- Umožňuje objevování UE pro služby ProSe a V2X bez plné síťové cesty
- Nese nebo je spojen se zprávami pro objevování obsahujícími identitu UE na aplikační vrstvě
- Umožňuje měření přijímaného výkonu referenčního signálu (RSRP) pro odhad blízkosti
- Integrován s bezpečnostními mechanismy mobilní sítě a správou předplatného

## Související pojmy

- [D2D – Device-to-Device](/mobilnisite/slovnik/d2d/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [DRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/drs/)
