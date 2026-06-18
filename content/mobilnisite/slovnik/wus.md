---
slug: "wus"
url: "/mobilnisite/slovnik/wus/"
type: "slovnik"
title: "WUS – Wake Up Signal"
date: 2025-01-01
abbr: "WUS"
fullName: "Wake Up Signal"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/wus/"
summary: "Signál s nízkou spotřebou energie vysílaný sítí, který oznamuje uživatelskému zařízení (UE) v úsporném režimu (např. eDRX nebo PSM), že je připravena downlink přenosová zpráva. Umožňuje UE probudit hl"
---

WUS je signál s nízkou spotřebou energie, který informuje uživatelské zařízení (UE) v úsporném režimu o čekajících downlink datech, což mu umožňuje aktivovat hlavní přijímač pouze v případě potřeby, a tím šetřit životnost baterie.

## Popis

Wake Up Signal (WUS) je mechanismus na fyzické vrstvě navržený pro minimalizaci spotřeby energie uživatelského zařízení (UE), zejména pro zařízení hromadné komunikace typu stroj-stroj (mMTC) a vylepšeného mobilního širokopásmového přístupu (eMBB). Funguje na principu oddělení monitorovací činnosti pro paging nebo jiné downlink řídicí informace od aktivních period hlavního rádiového přijímače. Když je UE nakonfigurováno s WUS, přechází do hlubokého spánkového režimu a vypíná komponenty primárního přijímače. Síť před vlastní paging příležitostí nebo cyklem nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)) v připojeném režimu vysílá specifickou, jednoduchou a energeticky úspornou WUS sekvenci na vyhrazeném zdroji v časově-frekvenční mřížce. UE periodicky aktivuje obvod zjednodušeného přijímače s nízkou spotřebou výhradně pro detekci tohoto předdefinovaného signálu. Pokud je WUS detekován, UE plně zapne hlavní přijímač, aby monitorovalo kanál Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) pro případnou paging zprávu nebo downlink přiřazení v následujícím časovém okně. Pokud není WUS detekován, UE přeskočí celé monitorovací okno, vrátí se do hlubokého spánku a vyhne se tak energetické náročnosti dekódování složitějšího PDCCH.

Z architektonického hlediska je WUS integrován do protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a specifikací fyzické vrstvy. Konfigurace, včetně WUS sekvence, časového posunu, frekvenčních zdrojů a přidružených monitorovacích příležitostí, je signalizována UE prostřednictvím RRC signalizace, a to buď v režimu idle/inactive, nebo v připojeném režimu. Na fyzické vrstvě je WUS typicky implementován jako signál založený na sekvenci, například sekvence podobná Primary Synchronization Signal ([PSS](/mobilnisite/slovnik/pss/)) nebo specifický vzor referenčního signálu, navržený pro spolehlivou detekci s minimálním zpracováním. Signál je vysílán s dostatečným výkonem pro zajištění pokrytí, ale je krátký, aby se omezila režie sítě.

Jeho role je klíčová v rámci úsporného režimu sítě Radio Access Network, doplňuje funkce jako rozšířený nespojitý příjem (eDRX) a Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)). Tím, že radikálně snižuje počet případů, kdy musí UE provádět plné blind dekódování PDCCH – což je výpočetně náročná a energeticky nákladná operace – WUS přímo přispívá k delší životnosti baterie, což je klíčový požadavek pro IoT senzory a nositelná zařízení, která mohou potřebovat fungovat roky na jedné baterii. Představuje zásadní posun od přístupu 'vždy naslouchat' k 'naslouchat pouze při volání' pro zařízení s nepravidelnou komunikací.

## K čemu slouží

WUS byl vytvořen, aby řešil kritickou výzvu životnosti baterie UE, zejména pro miliardy zařízení předpokládaných pro Internet věcí (IoT) v ekosystémech 5G a novějších. Před jeho zavedením se úspora energie spoléhala na prodlužování cyklů [DRX](/mobilnisite/slovnik/drx/) (eDRX) nebo použití Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)), ale tyto přístupy měly své kompromisy. eDRX zvyšoval latenci a v obou režimech muselo UE stále periodicky probouzet a dekódovat [PDCCH](/mobilnisite/slovnik/pdcch/) během své paging příležitosti, což spotřebovávalo značnou energii, i když pro něj nebyly určeny žádné data. Toto 'blind dekódování' bylo hlavním zdrojem odběru energie u zařízení s velmi nízkou mírou aktivity.

Motivace pro WUS vycházela z pozorování, že pro mnoho IoT aplikací jsou paging události vzácné. Plýtvání energií na tisíce zbytečných dekódování PDCCH bylo neefektivní. WUS to řeší zavedením dvoustupňového procesu probuzení: levná kontrola signálu s nízkou spotřebou energie předchází nákladné aktivaci plného přijímače. To umožňuje extrémně dlouhé cykly eDRX (i hodiny nebo dny) bez úměrného snížení životnosti baterie v důsledku častého monitorování. Přímo tak naplňuje cílový návrh 3GPP, kterým je životnost baterie přes 10 let pro zařízení mMTC. Historicky byl standardizován počínaje Release 15 jako součást širších vylepšení 5G NR a LTE-M/NB-IoT a vyvíjel se v následujících releasech pro optimalizaci své účinnosti a použitelnosti pro různé kategorie zařízení a stavy sítě.

## Klíčové vlastnosti

- Předkonfigurovaná detekce signálu s nízkou složitostí předcházející paging/DRX příležitostem
- Významně snižuje spotřebu energie UE tím, že se vyhne zbytečnému dekódování PDCCH
- Konfigurovatelné prostřednictvím RRC signalizace pro režimy idle/inactive i připojený režim
- Používá vyhrazené sekvence fyzické vrstvy (např. založené na PSS) pro spolehlivé probuzení
- Podporuje jak LTE (eMTC, NB-IoT), tak NR rádiové přístupové technologie
- Umožňuje ultradlouhé cykly eDRX bez úměrného vybíjení baterie

## Související pojmy

- [PSM – Protocol State Machine](/mobilnisite/slovnik/psm/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [WUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wus/)
