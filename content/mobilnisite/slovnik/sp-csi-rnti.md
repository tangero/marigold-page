---
slug: "sp-csi-rnti"
url: "/mobilnisite/slovnik/sp-csi-rnti/"
type: "slovnik"
title: "SP-CSI-RNTI – Semi-Persistent Channel State Information Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SP-CSI-RNTI"
fullName: "Semi-Persistent Channel State Information Radio Network Temporary Identifier"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sp-csi-rnti/"
summary: "Specializovaný RNTI používaný v 5G NR k plánování polo-perzistentních přenosů referenčních signálů CSI. Umožňuje efektivní periodické poskytování zpětné vazby o kvalitě kanálu od UE k gNB bez režie sp"
---

SP-CSI-RNTI je specializovaný RNTI používaný v 5G NR k plánování polo-perzistentních přenosů referenčních signálů CSI, což umožňuje efektivní periodické poskytování zpětné vazby o kvalitě kanálu od UE bez režie spojené s průběžným dynamickým plánováním.

## Popis

SP-CSI-RNTI je klíčový identifikátor ve vrstvě [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) 5G New Radio (NR), definovaný ve specifikaci 3GPP 38.321. Funguje jako jedinečná adresa, kterou gNodeB (gNB) používá ke konfiguraci a aktivaci polo-perzistentního plánování ([SPS](/mobilnisite/slovnik/sps/)) pro hlášení informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). Na rozdíl od dynamicky plánovaného hlášení CSI, které je spouštěno samostatnou zprávou [DCI](/mobilnisite/slovnik/dci/) pro každý výskyt, umožňuje SP-CSI-RNTI gNB nastavit periodický vzor pro přenos [CSI-RS](/mobilnisite/slovnik/csi-rs/) (referenčního signálu) a odpovídající hlášení CSI od uživatelského zařízení (UE) pomocí jediného aktivačního příkazu. Tato aktivace se obvykle provádí pomocí formátu DCI zašifrovaného tímto konkrétním [RNTI](/mobilnisite/slovnik/rnti/), který přenáší periodicitu a časový posun pro hlášení.

Po úspěšném dekódování DCI adresovaného na jeho SP-CSI-RNTI nakonfiguruje MAC vrstva UE její fyzickou vrstvu tak, aby periodicky měřila nakonfigurované zdroje CSI-RS a generovala hlášení CSI (např. indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), indikátor předkódovací matice ([PMI](/mobilnisite/slovnik/pmi/)), indikátor řádu (RI)) podle udělených parametrů. Tato hlášení jsou následně přenášena na fyzickém kanálu řídicího signálu v uplinku (PUCCH) nebo fyzickém sdíleném kanálu v uplinku (PUSCH) v definovaných intervalech. Tento mechanismus odděluje proces získávání CSI od smyčky dynamického plánování dat a poskytuje gNB pravidelné, předvídatelné aktualizace stavu kanálu.

Klíčová architektonická role SP-CSI-RNTI spočívá ve snížení režie řídicí signalizace a latence spojené s častým odhadem kvality kanálu. Je součástí sady RNTI, z nichž každé má specifický účel (např. C-RNTI pro dynamické plánování, CS-RNTI pro konfigurovaný grant v uplinku). gNB přiřadí SP-CSI-RNTI UE prostřednictvím signalizace RRC (Radio Resource Control) během nastavování nebo rekonfigurace spojení. Řízení jeho aktivace, deaktivace a případné rekonfigurace je prováděno pomocí MAC řídicích elementů (CE) nebo DCI, což síti poskytuje flexibilitu pro přizpůsobení frekvence hlášení CSI na základě mobility UE, typu provozu a podmínek zatížení sítě.

## K čemu slouží

SP-CSI-RNTI bylo zavedeno v 5G NR (Release 15) jako odpověď na potřebu efektivního získávání informací o stavu kanálu s nízkou režií, což je zásadní pro pokročilé funkce jako beamforming, massive MIMO a dynamické sdílení spektra. V předchozích systémech LTE, ačkoli existovalo polo-perzistentní plánování pro data, mechanismy pro periodické hlášení CSI byly těsněji provázány s konfigurací RRC a postrádaly stejnou úroveň dynamické granularity aktivace/deaktivace řízené MAC vrstvou. Návrh 5G předpokládal případy použití vyžadující velmi spolehlivou a častou znalost kanálu, jako je komunikace s ultra-spolehlivým nízkým zpožděním (URLLC) a rozšířené mobilní širokopásmové připojení (eMBB), kde by čekání na dynamicky plánovaná hlášení mohlo zavést nežádoucí latenci nebo zahlcení řídicího kanálu.

Tato technologie řeší problém režie řídicího kanálu. Dynamické plánování každého hlášení CSI vyžaduje přenos DCI pro každý výskyt, což spotřebovává cenné prostředky PDCCH. Pro scénáře se stabilními podmínkami kanálu nebo předvídatelnými vzory provozu (např. stacionární UE s konstantním datovým tokem videostreamu) je to vysoce neefektivní. SP-CSI-RNTI umožňuje přístup typu 'nastav a zapomeň', kdy je vzor hlášení nastaven jednou a poté pokračuje periodicky, dokud není explicitně zastaven, čímž se uvolní kapacita PDCCH pro jiná UE nebo dynamičtější rozhodnutí o plánování. Tato efektivita je zásadní pro podporu masivních nasazení IoT a scénářů hustých sítí, které jsou v 5G a dalších generacích plánovány.

## Klíčové vlastnosti

- Umožňuje aktivaci/deaktivaci periodického hlášení CSI na vrstvě MAC
- Snižuje režii PDCCH odstraněním plánování DCI pro každé jednotlivé hlášení
- Podporuje flexibilní konfiguraci periody a časového posunu hlášení CSI
- Funguje v součinnosti s polo-perzistentně plánovanými zdroji CSI-RS
- Spravováno pomocí formátů DCI specificky zašifrovaných tímto RNTI
- Integruje se s procedurami MAC 5G NR pro efektivní řízení prostředků

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SP-CSI-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sp-csi-rnti/)
