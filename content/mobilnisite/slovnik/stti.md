---
slug: "stti"
url: "/mobilnisite/slovnik/stti/"
type: "slovnik"
title: "STTI – Short Transmission Time Interval"
date: 2025-01-01
abbr: "STTI"
fullName: "Short Transmission Time Interval"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/stti/"
summary: "Zkrácený přenosový časový interval zavedený v LTE pro služby citlivé na latenci. Zkrácením základní plánovací jednotky umožňuje rychlejší adaptaci rádiového spoje, HARQ zpětnou vazbu a přenos dat, což"
---

STTI je zkrácený přenosový časový interval v LTE, který zkracuje základní plánovací jednotku, aby umožnil rychlejší adaptaci spoje a přenos dat pro služby s nízkou latencí, jako je URLLC.

## Popis

Short Transmission Time Interval (sTTI) je funkce zavedená v LTE ke snížení latence v uživatelské rovině definováním přenosových časových intervalů kratších než původní 1ms podrámec. Přenosový časový interval je minimální časová jednotka, po kterou může být uživatel naplánován pro přenos dat, a je svázán s časováním procesů hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)). Původní [TTI](/mobilnisite/slovnik/tti/) v LTE je jeden podrámec (1 ms, skládající se ze dvou 0,5ms slotů). sTTI toto zkracuje na doby trvání jako 2 symboly (přibližně 0,143 ms), 1 slot (0,5 ms) nebo konfiguraci se 7 symboly, v závislosti na rozestupu subnosných a scénáři nasazení.

Z architektonického hlediska sTTI ovlivňuje více vrstev protokolového zásobníku LTE. Na fyzické vrstvě vyžaduje nové struktury kanálů pro data (sPDSCH, sPUSCH) a řídicí informace (sPDCCH). Tyto kanály jsou mapovány na zkrácené časové zdroje uvnitř podrámce. Zkrácená délka TTI vyžaduje rychlejší časování zpracování jak na straně UE, tak eNodeB. To zahrnuje rychlejší kódování/dekódování kanálu, rychlejší generování a příjem řídicích informací v uplinku ([UCI](/mobilnisite/slovnik/uci/)) a downlinku ([DCI](/mobilnisite/slovnik/dci/)) a výrazně zkrácenou dobu odezvy HARQ ([RTT](/mobilnisite/slovnik/rtt/)). Časování procesu HARQ je komprimováno, což umožňuje přijetí potvrzovací zpětné vazby ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) mnohem dříve po přenosu.

Jak to funguje, zahrnuje dynamickou nebo semistatickou konfiguraci ze strany sítě. eNodeB může nakonfigurovat UE pro provoz sTTI na základě jeho požadavků na služby (např. pro [URLLC](/mobilnisite/slovnik/urllc/)). Když je naplánováno pomocí sTTI, UE vysílá nebo přijímá data po zkrácenou dobu. Související řídicí informace, které tento přenos dat plánují, jsou také přenášeny v podobně zkráceném sPDCCH. Toto těsné propojení plánování a přenosu dat v rámci velmi krátkého okna je klíčové pro dosažení nízké latence. Provoz sTTI může být multiplexován s legacy UE používajícími běžné 1ms TTI v rámci stejného nosiče prostřednictvím pečlivé alokace zdrojů v časově-frekvenční mřížce.

## K čemu slouží

sTTI bylo vytvořeno, aby řešilo přísné požadavky na latenci pro nové případy užití, jako je průmyslová automatizace, komunikace vozidlo-se-vším (V2X) a hraní her v reálném čase, které se objevily s cestovní mapou směrem k 5G. Původní 1ms TTI v LTE a s ním spojené časování HARQ mělo za následek minimální teoretickou latenci v uživatelské rovině kolem 10 ms, což bylo nedostatečné pro služby vyžadující latence 1 ms nebo méně. sTTI byla klíčovou evoluční funkcí LTE, která měla tuto výkonnostní mezeru překlenout před plným nasazením 5G NR.

Řešilo základní úzké hrdlo granularity plánování. Kratší TTI umožňuje, aby byly datové pakety přeneseny, potvrzeny a případně retransmitovány v mnohem kratším celkovém čase. To přímo snižuje latenci na rádiovém rozhraní. Dále umožňuje rychlejší adaptaci spoje, protože kvalita kanálu může být měřena a modulační a kódovací schéma (MCS) aktualizováno častěji, což zlepšuje spolehlivost pro přerušované přenosy. sTTI byla kritickou součástí umožňující LTE podporovat třídu služeb Ultra-spolehlivé komunikace s nízkou latencí (URLLC) definovanou 3GPP.

Motivace byla hnána poptávkou průmyslu po před-5G řešeních s nízkou latencí. Umožnila operátorům sítí upgradovat stávající LTE infrastrukturu pro podporu aplikací citlivých na latenci bez čekání na kompletní zavedení 5G NR. Jeho zavedení v Rel-15 (jako součást evoluce LTE pro 5G) pozici LTE jako komplementární technologie rádiového přístupu k NR, schopné podporovat širokou škálu 5G případů užití.

## Klíčové vlastnosti

- Délky TTI kratší než 1 ms (např. 2 OFDM symboly, 1 slot)
- Nové fyzické kanály: sPDSCH, sPUSCH, sPDCCH
- Zkrácená doba odezvy HARQ (RTT) pro rychlejší retransmise
- Rychlejší časování zpracování pro UE a eNodeB
- Dynamická konfigurace na UE podle požadavků QoS
- Frekvenční multiplexování s přenosy legacy 1ms TTI

## Související pojmy

- [TTI – Transmission Timing Interval](/mobilnisite/slovnik/tti/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [STTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/stti/)
