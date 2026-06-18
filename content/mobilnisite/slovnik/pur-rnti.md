---
slug: "pur-rnti"
url: "/mobilnisite/slovnik/pur-rnti/"
type: "slovnik"
title: "PUR-RNTI – Preconfigured Uplink Resource Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "PUR-RNTI"
fullName: "Preconfigured Uplink Resource Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pur-rnti/"
summary: "PUR-RNTI je jedinečný identifikátor používaný v sítích 3GPP k adresování UE nakonfigurovaných s přednastavenými uplinkovými prostředky (PUR). Umožňuje efektivní downlinkovou signalizaci, jako jsou pot"
---

PUR-RNTI je jedinečný identifikátor používaný k adresování uživatelského zařízení nakonfigurovaného s přednastavenými uplinkovými prostředky (Preconfigured Uplink Resources), který umožňuje efektivní signalizaci v downlinku jako odpověď na tyto přenosy za účelem snížení režie.

## Popis

PUR-RNTI (Preconfigured Uplink Resource Radio Network Temporary Identifier) je specifický typ [RNTI](/mobilnisite/slovnik/rnti/) zavedený ve specifikaci 3GPP Release 16 pro použití s UE podporujícími [PUR](/mobilnisite/slovnik/pur/) v systémech LTE-M a NB-IoT. RNTI je dočasný identifikátor přidělený sítí pro jedinečné adresování UE přes rádiové rozhraní a PUR-RNTI tuto funkci plní pro operace související s přednastavenými uplinkovými prostředky (PUR). Když je UE nakonfigurováno s PUR, může mu síť přidělit PUR-RNTI, které se používá ke skramblování a adresování řídicích informací v downlinku ([DCI](/mobilnisite/slovnik/dci/)) na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) nebo zpráv na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) určených speciálně pro komunikaci související s PUR.

Z architektonického hlediska PUR-RNTI funguje v rámci [MAC](/mobilnisite/slovnik/mac/) a fyzické vrstvy rádiového protokolového zásobníku. Při konfiguraci PUR prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) může síť přidělit hodnotu PUR-RNTI, která je UE sdělena jako součást konfiguračních parametrů. Tento identifikátor se typicky používá ve scénářích, kdy UE vysílá uplinková data pomocí svých přednastavených prostředků a síť potřebuje odeslat odpověď, například potvrzení ([ACK](/mobilnisite/slovnik/ack/)/NACK) o přijetí dat nebo downlinkový přenos dat. UE monitoruje PDCCH pro formáty DCI skramblované pomocí jeho PUR-RNTI, což mu umožňuje efektivně přijímat downlinkové signály bez nutnosti dalších identifikačních procedur.

Jak to funguje v praxi: Když UE provede uplinkový přenos založený na PUR, síť data dekóduje a může vygenerovat odpověď. Pro doručení této odpovědi síť použije PUR-RNTI k přímému adresování UE. Například pokud síť odešle ACK pomocí formátu DCI na PDCCH, skrambluje cyklický redundantní součet (CRC) tohoto DCI pomocí PUR-RNTI. UE, které zná své přidělené PUR-RNTI, tento CRC deskrambluje a pokud se shoduje, zpracuje DCI, aby získalo potvrzení nebo informace o plánování. Tím se vyhne nutnosti používat širší identifikátory, jako je C-RNTI v připojeném stavu nebo P-RNTI pro paging, což proces zjednodušuje a snižuje režii na řídicím kanálu. PUR-RNTI je navrženo tak, aby bylo specifické pro dané UE, ale může být znovu použito nebo aktualizováno na základě síťových politik, a hraje klíčovou roli při udržování nízkolatenční a energeticky efektivní komunikace pro IoT zařízení.

## K čemu slouží

PUR-RNTI bylo vytvořeno pro podporu efektivní downlinkové signalizace vyžadované funkcí přednastavených uplinkových prostředků (Preconfigured Uplink Resource - PUR) v IoT sítích. Bez vyhrazeného identifikátoru by síť musela pro odpovědi na PUR přenosy spoléhat na stávající RNTI, jako je C-RNTI nebo P-RNTI, což by mohlo vést k dodatečné signalizační režii nebo režii správy stavů. PUR-RNTI poskytuje cílený mechanismus pro adresování UE v idle nebo inactive stavech, která používají PUR, a umožňuje tak rychlá a prostředkově efektivní potvrzení nebo doručení dat.

Motivace pro zavedení PUR-RNTI vychází z potřeby minimalizovat využití řídicího kanálu a spotřebu energie UE v masivních IoT nasazeních. V tradičním LTE downlinkové odpovědi na uplinkové přenosy často vyžadují, aby bylo UE ve stavu RRC Connected s C-RNTI, což si žádá přechody mezi stavy spotřebovávající energii a čas. Použitím PUR-RNTI může síť odesílat downlinkové signály přímo UE nakonfigurované s PUR, a to i když je UE ve stavu RRC Idle nebo Inactive, čímž se snižuje potřeba častých změn stavu a s nimi spojených signalizačních procedur.

Tím se řeší omezení předchozích přístupů, kdy musela IoT zařízení pro obousměrnou komunikaci procházet plným procesem náhodného přístupu a nastavením spojení, což negovalo některé výhody PUR. PUR-RNTI vylepšuje celkovou architekturu PUR tím, že umožňuje odlehčenou downlinkovou cestu, podporuje funkce jako early data transmission a efektivní komunikaci malých objemů dat. Je v souladu s evolucí 3GPP směrem k odlehčeným a škálovatelným IoT řešením a zajišťuje, že jak uplinkové, tak downlinkové aspekty jsou optimalizovány pro nízkopříkonové a nízkolatenční aplikace v 5G a dalších generacích.

## Klíčové vlastnosti

- Jedinečný identifikátor pro UE podporující PUR
- Používá se ke skramblování řídicích informací v downlinku (DCI)
- Umožňuje efektivní potvrzení pro PUR přenosy
- Snižuje režii na řídicím kanálu
- Podporuje adresování UE ve stavech idle/inactive
- Integruje se s procedurami PUR pro LTE-M a NB-IoT

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [P-RNTI – Paging Radio Network Temporary Identifier](/mobilnisite/slovnik/p-rnti/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [PUR – Preconfigured Uplink Resource](/mobilnisite/slovnik/pur/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [PUR-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pur-rnti/)
