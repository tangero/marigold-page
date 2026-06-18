---
slug: "s-cpac"
url: "/mobilnisite/slovnik/s-cpac/"
type: "slovnik"
title: "S-CPAC – Subsequent Conditional PSCell Addition or Change"
date: 2025-01-01
abbr: "S-CPAC"
fullName: "Subsequent Conditional PSCell Addition or Change"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-cpac/"
summary: "S-CPAC je vylepšení 5G NR duální konektivity (EN-DC, NR-DC), které umožňuje UE provést podmíněné přidání nebo změnu PSCell poté, co byla připravena počáteční podmíněná předání spojení (handover) nebo"
---

S-CPAC je vylepšení 5G duální konektivity, které umožňuje UE provést následné podmíněné přidání nebo změnu PSCell poté, co byla připravena počáteční podmíněná mobilní procedura, čímž zvyšuje robustnost a snižuje přerušení.

## Popis

Subsequent Conditional PSCell Addition or Change (S-CPAC) je mobilní procedura definovaná pro 5G New Radio (NR), konkrétně v kontextu Multi-Radio Dual Connectivity ([MR-DC](/mobilnisite/slovnik/mr-dc/)), jako je [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR Dual Connectivity) a [NR-DC](/mobilnisite/slovnik/nr-dc/) (NR-NR Dual Connectivity). Funguje jako rozšíření mechanismů Conditional Handover ([CHO](/mobilnisite/slovnik/cho/)) a Conditional PSCell Change ([CPC](/mobilnisite/slovnik/cpc/)). Primary [SCG](/mobilnisite/slovnik/scg/) Cell (PSCell) je primární buňka sekundárního uzlu v nastavení duální konektivity. Ve standardních podmíněných procedurách síť připraví jednu nebo více kandidátských cílových buněk a UE změnu na jednu z nich provede, když její rádiové podmínky splní předdefinovaná kritéria (např. prahové hodnoty síly signálu).

S-CPAC řeší specifický scénář: co se stane poté, co již bylo pro UE nakonfigurováno příkazem podmíněné předání spojení nebo změna PSCell, ale ještě ho neprovedlo? S-CPAC umožňuje síti následně připravit *další* podmíněné přidání nebo změnu PSCell *navíc* k již připravenému. To znamená, že UE může udržovat více vrstev podmíněných mobilních příkazů. Síť může například nejprve nakonfigurovat podmíněnou změnu PSCell z buňky A na buňku B. Později, předtím než UE tuto změnu provede, může síť pomocí S-CPAC nakonfigurovat další podmíněnou změnu z potenciální buňky B na buňku C. UE tyto podmínky spravuje jako následné.

Procedura zahrnuje specifické [RRC](/mobilnisite/slovnik/rrc/) signalizaci mezi UE a hlavním uzlem (např. gNB v NR-DC). Síť odešle zprávu RRCReconfiguration obsahující následnou podmíněnou konfiguraci (např. 'CondReconfigToAddMod' pro nového kandidáta). UE tuto konfiguraci uloží navíc k jakýmkoli dříve uloženým podmíněným konfiguracím. Logika provedení zůstává řízena událostmi na základě hlášení měření. Toto zvyšuje robustnost mobility v hustých nebo rychle se měnících rádiových prostředích, protože UE může plynule přecházet přes řetězec předem schválených kandidátských buněk bez nutnosti se po každém provedení vracet k síti pro nový příkaz, čímž se minimalizuje doba přerušení služby a signalizační režie.

## K čemu slouží

S-CPAC bylo zavedeno ve vydání 18 ke zvýšení robustnosti a efektivity podmíněných mobilních procedur v pokročilých nasazeních 5G, zejména pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a ve vysokofrekvenčních pásmech (např. mmWave), kde mohou být rádiové spoje nestálé. Základní Conditional Handover (CHO) a Conditional PSCell Change (CPC), zavedené v dřívějších vydáních, významně snížily míru neúspěšných předání spojení ve srovnání s klasickými předáními tím, že připravily záložní cesty předem. Byly však primárně navrženy pro jediný podmíněný přechod.

Omezení, které S-CPAC řeší, je potenciální 'ping-pong' efekt nebo selhání spojení po provedení jediné podmíněné změny. V dynamickém prostředí se může cílové buňce, zvolené podmíněným provedením, sama rychle zhoršit kvalita. Bez S-CPAC by UE musela dokončit předání spojení, znovu se připojit a poté aktivovat nové hlášení měření a přijmout nový příkaz k předání spojení – proces, který zabere čas a může vést k selhání rádiového spoje. S-CPAC na to reaguje proaktivně tím, že umožňuje síti 'předvídat' a nastavit řetězec podmíněných přesunů. To je obzvláště kritické pro případy použití, jako je průmyslový IoT a vozidlové komunikace, kde je nepřerušená konektivita prvořadá. Řeší problém sekvenční mobility v podmíněných scénářích, čímž činí celou proceduru více prediktivní a odolnou.

## Klíčové vlastnosti

- Umožňuje konfiguraci podmíněné změny/přidání PSCell následně po již připravené podmíněné konfiguraci
- Snižuje dobu přerušení služby a signalizační režii pro sekvenční změny buněk
- Zvyšuje robustnost mobility v nestálých rádiových podmínkách (např. mmWave)
- Podporuje scénáře MR-DC (EN-DC) i NR-DC
- Spravováno pomocí RRC rekonfiguračních zpráv mezi UE a hlavním uzlem
- UE udržuje a vyhodnocuje více vrstev podmínek provedení

## Související pojmy

- [MR-DC – Multi-Radio Dual Connectivity](/mobilnisite/slovnik/mr-dc/)
- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)
- [NR-DC – NR-NR Dual Connectivity](/mobilnisite/slovnik/nr-dc/)

## Definující specifikace

- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [S-CPAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-cpac/)
