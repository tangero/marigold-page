---
slug: "i-rnti"
url: "/mobilnisite/slovnik/i-rnti/"
type: "slovnik"
title: "I-RNTI – Inactive RNTI"
date: 2025-01-01
abbr: "I-RNTI"
fullName: "Inactive RNTI"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/i-rnti/"
summary: "I-RNTI je dočasný rádiový síťový identifikátor používaný v 5G NR k jednoznačné identifikaci uživatelského zařízení (UE) ve stavu RRC_INACTIVE. Umožňuje efektivní paging a rychlé obnovení spojení bez n"
---

I-RNTI je dočasný identifikátor používaný v 5G NR k jednoznačné identifikaci uživatelského zařízení (UE) v neaktivním stavu, který umožňuje efektivní paging a rychlé obnovení spojení.

## Popis

Inactive Radio Network Temporary Identifier (I-RNTI) je klíčový identifikátor v protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro 5G New Radio (NR), zavedený jako součást stavu RRC_INACTIVE ve specifikaci 3GPP Release 15. Slouží jako jedinečný, kontextově specifický identifikátor pro uživatelské zařízení (UE), když se nachází ve stavu RRC_INACTIVE, což je stav s nízkou spotřebou energie určený pro přenos dat s nízkou četností. I-RNTI přiděluje obsluhující gNB (Next Generation NodeB) při přechodu UE ze stavu RRC_CONNECTED do RRC_INACTIVE. Tento identifikátor je uložen jako součást kontextu přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) UE, který je také uchován v gNB a v případě architektury s oddělením CU-DU může být spravován centrální jednotkou ([CU](/mobilnisite/slovnik/cu/)). Hlavní technickou operací zahrnující I-RNTI je procedura RRC Resume. Když dorazí datový provoz směrem k neaktivnímu UE, RAN zahájí pagingovou zprávu na bázi RAN v rámci nakonfigurované oblasti RAN Notification Area (RNA). Tato pagingová zpráva obsahuje I-RNTI daného UE. UE, které monitoruje pagingové příležitosti, rozpozná své I-RNTI a zahájí žádost o obnovení spojení směrem k gNB, přičemž poskytne své I-RNTI. gNB použije toto I-RNTI k načtení uloženého kontextu UE, což umožní rychlé obnovení spojení bez nutnosti úplného nastavení RRC a procedury Service Request zahrnující síť jádra. Struktura I-RNTI může být dvou typů: plné I-RNTI, které zahrnuje identitu gNB a příponu specifickou pro UE, nebo krátké I-RNTI, což je kompaktnější forma. Jeho specifikace a použití jsou podrobně popsány v 3GPP TS 38.300 (celkový popis NR) a specifikacích protokolu RRC (TS 38.331).

## K čemu slouží

I-RNTI bylo vytvořeno, aby řešilo klíčové požadavky 5G NR pro hromadnou komunikaci strojového typu (mMTC) a vylepšené mobilní širokopásmové připojení (eMBB): ultra nízkou spotřebu energie a sníženou signalizační latenci pro sporadické přenosy dat. Předchozí stavy v LTE, [RRC](/mobilnisite/slovnik/rrc/)_IDLE a RRC_CONNECTED, představovaly kompromis. Režim IDLE šetřil energii, ale vyžadoval k obnovení přenosu dat zdlouhavou proceduru zahrnující síť jádra. Režim CONNECTED udržoval prostředky připravené, ale spotřebovával významnou část výdrže baterie UE. Stav RRC_INACTIVE, umožněný právě I-RNTI, zavádí třetí stav, který kombinuje výhody obou předchozích. I-RNTI řeší problém efektivní a jednoznačné identifikace uloženého kontextu konkrétního UE v rámci RAN během nečinnosti. Bez něj by síť musela pro paging používat identifikátor ze sítě jádra (jako je S-TMSI), který by přímo neodkazoval na kontext v RAN, což by vynutilo pomalejší proces obnovení nebo úplné znovupřipojení. Poskytnutím lokálního ukazatele v RAN umožňuje I-RNTI paging a načítání kontextu na bázi RAN, což drasticky snižuje zpoždění v řídicí rovině a signalizační zátěž při přechodech stavů. To je zásadní pro zařízení IoT vysílající malé, nepravidelné datové pakety i pro smartphony udržující aplikace v režimu "always-on" s minimálním dopadem na baterii.

## Klíčové vlastnosti

- Jednoznačně identifikuje UE ve stavu RRC_INACTIVE v rámci RAN.
- Používá se v pagingových zprávách na bázi RAN k vyvolání obnovení spojení.
- Poskytuje jej UE v zprávě RRC Resume Request k načtení svého kontextu.
- Umožňuje obnovení spojení bez signalizace se sítí jádra (pro UE v CM-CONNECTED).
- Podporuje dva formáty: plné I-RNTI a krátké I-RNTI pro vyšší efektivitu.
- Je nedílnou součástí kontextu AS UE uloženého v gNB/CU.

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [I-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-rnti/)
