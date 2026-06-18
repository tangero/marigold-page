---
slug: "tef"
url: "/mobilnisite/slovnik/tef/"
type: "slovnik"
title: "TEF – Transport Element Function"
date: 2025-01-01
abbr: "TEF"
fullName: "Transport Element Function"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tef/"
summary: "Transport Element Function (TEF) je logická entita v systému správy 3GPP (3GPP MS) odpovědná za správu zdrojů transportní sítě. Poskytuje standardizované rozhraní pro konfiguraci, správu poruch, výkon"
---

TEF (Transport Element Function) je logická entita v systému správy 3GPP odpovědná za správu zdrojů transportní sítě prostřednictvím standardizovaného rozhraní pro konfiguraci, správu poruch, výkonu a inventáře.

## Popis

Transport Element Function (TEF) je klíčová komponenta architektury systému správy 3GPP, definovaná primárně v TS 32.102. Funguje jako mediační funkce, která poskytuje rozhraní pro správu služeb pro transportní síťové elementy (TNE), což jsou fyzické nebo logické uzly tvořící transportní síť (např. směrovače, přepínače, optické transportní zařízení). TEF abstrahuje výrobci specifická rozhraní pro správu těchto TNE a předkládá sjednocené, standardizované rozhraní – typicky založené na referenčním bodu integrace ([IRP](/mobilnisite/slovnik/irp/)) – vyšším systémům správy, jako je systém správy elementů ([EMS](/mobilnisite/slovnik/ems/)) nebo systém správy sítě ([NMS](/mobilnisite/slovnik/nms/)). To umožňuje centralizovanou správu transportních zdrojů jako součásti celé telekomunikační sítě.

Architektonicky se TEF nachází ve vrstvě správy a komunikuje směrem k TNE pomocí protokolových adaptérů (které mohou podporovat protokoly jako [SNMP](/mobilnisite/slovnik/snmp/), NETCONF nebo TL1) a směrem k EMS/NMS prostřednictvím specifikovaných 3GPP IRP, jako je IRP pro obecný model síťových zdrojů ([NRM](/mobilnisite/slovnik/nrm/)). Její vnitřní funkcionalita zahrnuje transformaci datového modelu, kde jsou výrobci specifické modely řídicích informací mapovány na standardizovaný 3GPP NRM pro transportní zdroje. TEF provádí klíčové operace správy: správu konfigurace (např. zřizování transportních spojů a parametrů QoS), správu poruch (sbírání a korelace alarmů z TNE), správu výkonu (sběr metrik jako využití šířky pásma a míra chyb) a správu inventáře (vedení záznamů o transportním zařízení a jeho schopnostech).

Princip fungování spočívá v tom, že TEF slouží jako integrační bod. Když NMS potřebuje nakonfigurovat transportní cestu pro nové backhaulové připojení základnové stanice, odešle standardizovaný požadavek do TEF. TEF tento požadavek přeloží na specifické příkazy pro zapojené směrovače nebo přepínače, provede je a vrátí konsolidovaný stav. Podobně pro správu poruch jsou alarmy z různých TNE shromažďovány, filtrovány, korelovány za účelem identifikace hlavních příčin (např. přerušení vlákna ovlivňující více spojů) a předávány dál jako standardizovaná oznámení. Tato mediační role je klíčová pro automatizaci síťových operací, zajištění konzistence a umožnění vícevýrobcových prostředí transportních sítí bez nutnosti, aby NMS zpracovávalo proprietární rozhraní každého výrobce.

## K čemu slouží

TEF byla zavedena ve 3GPP Release 8 jako součást širšího úsilí o definici standardizovaného, sjednoceného rámce správy pro telekomunikační sítě, zahrnujícího jak rádiovou přístupovou síť (RAN), tak transportní síť. Před její standardizací byly transportní sítě často spravovány izolovanými, výrobci specifickými systémy, které byly špatně integrovány se správou mobilního jádra a RAN. Tento izolovaný přístup vedl k provozní neefektivitě, delší době nasazování služeb a obtížím při provádění korelace poruch a zajištění služeb od konce ke konci, zejména s tím, jak se sítě vyvíjely směrem k plně IP a paketovému transportu.

Vytvoření TEF bylo motivováno potřebou integrované správy sítě v kontextu standardizace modelu síťových zdrojů ([NRM](/mobilnisite/slovnik/nrm/)). Řeší problém fragmentace správy tím, že poskytuje společnou abstraktní vrstvu pro transportní zdroje. To umožňuje operátorům mobilních sítí spravovat celou svou infrastrukturu – od rádiové buňky po směrovač jádra – prostřednictvím souvislé sady nástrojů a rozhraní. TEF řeší klíčové problémy, jako je automatizované zřizování backhaulu pro nové základnové stanice, sjednocené monitorování výkonu pro dodržování smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) a zjednodušená správa poruch, která dokáže korelovat selhání transportního spoje s ovlivněnými rádiovými službami. Její vývoj v následujících releasech odráží pokračující potřebu spravovat stále složitější transportní technologie, včetně mikrovlnných, optických a IP/[MPLS](/mobilnisite/slovnik/mpls/) sítí, v rámci sjednoceného paradigmatu správy 3GPP.

## Klíčové vlastnosti

- Standardizovaná mediační funkce mezi TNE a vyššími systémy správy (EMS/NMS)
- Poskytuje správu konfigurace, poruch, výkonu a inventáře pro transportní zdroje
- Využívá referenční body integrace 3GPP (IRP) pro standardizaci severního rozhraní
- Podporuje vícevýrobcové transportní sítě prostřednictvím adaptace protokolů a transformace modelu
- Umožňuje správu služeb od konce ke konci integrací správy transportní a mobilní sítě
- Usnadňuje automatizované zřizování a zajištění transportu pro připojení RAN a jádra sítě

## Související pojmy

- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [TEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tef/)
