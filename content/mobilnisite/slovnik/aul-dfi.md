---
slug: "aul-dfi"
url: "/mobilnisite/slovnik/aul-dfi/"
type: "slovnik"
title: "AUL-DFI – Autonomous Uplink Downlink Feedback Indication"
date: 2025-01-01
abbr: "AUL-DFI"
fullName: "Autonomous Uplink Downlink Feedback Indication"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aul-dfi/"
summary: "AUL-DFI je zpětnovazební mechanismus v 5G NR, který umožňuje UE autonomně vysílat uplinková data bez čekání na dynamické uplinkové povolení (UL grant). gNB pro tato autonomní vysílání poskytuje downli"
---

AUL-DFI je zpětnovazební mechanismus 5G NR, při kterém UE autonomně vysílá uplinková data bez dynamického povolení (grantu) a gNB pro tato vysílání poskytuje downlinková potvrzení ACK/NACK, čímž se snižuje latence a signalizační režie.

## Popis

Autonomous Uplink Downlink Feedback Indication (AUL-DFI) je klíčová funkce schémat pro vysílání v uplinku v 5G New Radio (NR), definovaná v kontextu provozu s nakonfigurovaným povolením (Configured Grant, Typ 1). Funguje v rámci fyzické vrstvy specifikované v 3GPP TS 36.212 (multiplexování a kódování kanálu) a TS 37.213 (procedury fyzické vrstvy). Architektura zahrnuje uživatelské zařízení (UE), gNodeB (gNB) a specifické signalizační kanály fyzické vrstvy. AUL-DFI umožňuje posun od čistě grantového přístupu k uplinku k hybridnímu modelu, kde může UE vysílat autonomně na předem nakonfigurovaných prostředcích.

V jádru AUL-DFI funguje tak, že odděluje spouštěč vysílání dat v uplinku od downlinkové zpětné vazby pro toto vysílání. Síť předem nakonfiguruje UE sadou periodických časově-frekvenčních prostředků (Configured Grant) pro potenciální uplinkové vysílání. UE na základě příchodu dat a vlastní interní logiky se autonomně rozhoduje, kdy tyto prostředky použije k odeslání přenosového bloku ([TB](/mobilnisite/slovnik/tb/)). Klíčové je, že UE pro tuto konkrétní instanci vysílání neposílá Scheduling Request ([SR](/mobilnisite/slovnik/sr/)) ani nečeká na dynamické Uplinkové povolení ([UL](/mobilnisite/slovnik/ul/) Grant) od gNB. Tím se eliminuje latence výměny žádosti o plánování a povolení.

Komponenta 'Downlink Feedback Indication' je odpovědí gNB na toto autonomní vysílání. Po dekódování vysílání UE na nakonfigurovaných prostředcích musí gNB informovat UE, zda bylo vysílání úspěšné ([ACK](/mobilnisite/slovnik/ack/)), nebo vyžaduje opakování ([NACK](/mobilnisite/slovnik/nack/)). Tato zpětná vazba není posílána přes konvenční Physical [HARQ](/mobilnisite/slovnik/harq/) Indicator Channel ([PHICH](/mobilnisite/slovnik/phich/)) jako v LTE, ale je přenášena na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) pomocí specifického formátu DCI, konkrétně formátu DCI 0_1 nebo 0_2 s nastaveným příznakem DFI. Tento DCI obsahuje identifikátor procesu Hybrid Automatic Repeat Request (HARQ) a New Data Indicator (NDI) odpovídající autonomnímu vysílání, což umožňuje UE jednoznačně spojit zpětnou vazbu se svým konkrétním TB.

Klíčové komponenty v proceduře AUL-DFI zahrnují předem nakonfigurované prostředky grantu (periodicita, časové/frekvenční přidělení, MCS), identifikátor HARQ procesu asociovaný s nakonfigurovaným grantem, rozhodovací logiku UE pro autonomní vysílání a přenos DFI od gNB na PDCCH. Jeho úlohou v síti je poskytovat ultra-spolehlivou komunikaci s nízkou latencí (URLLC) pro provoz orientovaný na uplink, podporovat průmyslové IoT aplikace s deterministickým charakterem provozu a zlepšovat spektrální účinnost snížením režie řídicí signalizace pro předvídatelné uplinkové toky. Mechanismus vyžaduje těsné časové zarovnání; gNB musí být připraven přijímat a dekódovat na nakonfigurovaných prostředcích a UE musí monitorovat DFI v konkrétním časovém okně po svém autonomním vysílání.

## K čemu slouží

AUL-DFI byl vytvořen, aby řešil základní omezení latence a účinnosti dynamického plánování založeného na grantech pro určité případy užití 5G. V tradičním dynamickém plánování musí UE s daty k odeslání nejprve vyslat Scheduling Request (SR), počkat, až gNB odpoví Uplink Grantem, a teprve poté data vyslat. Tento vícestupňový proces zavádí významnou latenci (často několik milisekund), což je nepřijatelné pro klíčové URLLC aplikace, jako je tovární automatizace, dálkové ovládání a rozšířená realita, kde je latence v uplinku klíčovým ukazatelem výkonnosti.

Technologie byla motivována potřebou efektivněji podporovat uplinkový provoz s nepravidelnými, periodickými nebo předvídatelnými charakteristikami. Před AUL-DFI nabízely LTE a rané NR pro downlink semi-persistent scheduling (SPS) a pro uplink nakonfigurované granty, ale mechanismus zpětné vazby pro uplinkové nakonfigurované granty byl méně flexibilní. AUL-DFI konkrétně řeší problém poskytování efektivní zpětné vazby HARQ s nízkou latencí pro autonomní vysílání bez nutnosti používat vždy aktivní, vyhrazený kanál zpětné vazby jako PHICH, který je pro nepravidelný provoz neefektivní. Umožňuje síti zachovat kontrolu nad procesem HARQ (prostřednictvím zpětné vazby), zároveň poskytuje autonomii UE pro počáteční vysílání, čímž dosahuje rovnováhy mezi autonomií UE a správou sítě.

Historicky omezení předchozích přístupů zahrnovala pevné časování PHICH (omezující flexibilitu), latenci cyklu SR/Grant a neefektivitu neustálého přidělování prostředků pro potenciální zpětnou vazbu. AUL-DFI, zavedený v Rel-15 jako součást základní sady nástrojů NR URLLC, poskytl dynamičtější a efektivnější kanál zpětné vazby (založený na PDCCH), který může být sdílen mezi více UE a konfigurován s různou periodicitou, což přímo řeší tyto nedostatky a umožňuje nové služby s nízkou latencí v uplinku.

## Klíčové vlastnosti

- Umožňuje UE autonomní vysílání v uplinku na předem nakonfigurovaných grantech bez dynamické žádosti o plánování
- Poskytuje downlinkovou zpětnou vazbu HARQ (ACK/NACK) prostřednictvím PDCCH pomocí formátu DCI 0_1 nebo 0_2 s příznakem DFI
- Snižuje latenci v uplinku eliminací zpoždění výměny SR a UL Grant
- Snižuje režii řídicí signalizace pro předvídatelné nebo periodické vzorce uplinkového provozu
- Podporuje více HARQ procesů pro provoz s nakonfigurovaným grantem
- Usnadňuje spolehlivou komunikaci pro služby URLLC tím, že zachovává schopnost retransmise HARQ

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 37.213** (Rel-19) — Shared Spectrum Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [AUL-DFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/aul-dfi/)
