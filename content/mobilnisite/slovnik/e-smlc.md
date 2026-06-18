---
slug: "e-smlc"
url: "/mobilnisite/slovnik/e-smlc/"
type: "slovnik"
title: "E-SMLC – Enhanced Serving Mobile Location Centre"
date: 2025-01-01
abbr: "E-SMLC"
fullName: "Enhanced Serving Mobile Location Centre"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-smlc/"
summary: "Hlavní síťová entita zodpovědná za určení geografické polohy uživatelského zařízení (UE) v sítích LTE a 5G. Řídí polohovací procedury, vypočítává odhady polohy pomocí různých metod (např. OTDOA, A-GNS"
---

E-SMLC je hlavní síťová entita v sítích LTE a 5G, která určuje geografickou polohu uživatelského zařízení (UE) řízením polohovacích procedur a výpočtem odhadů polohy pro služby jako tísňová volání.

## Popis

Enhanced Serving Mobile Location Centre (E-SMLC) je klíčový funkční prvek v architektuře Evolved Packet Core (EPC) a 5G Core (5GC), věnovaný polohování v řídicí rovině. Je to centrální uzel, který řídí proces určování polohy pro cílové uživatelské zařízení (UE). E-SMLC komunikuje s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPC nebo s funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC přes rozhraní SLs (pro LTE) nebo NLs (pro 5G NR). Po přijetí požadavku na polohu vybere E-SMLC vhodnou polohovací metodu na základě faktorů jako požadovaná přesnost, schopnosti UE a stav sítě.

E-SMLC podporuje více polohovacích technik. Pro LTE to zahrnuje Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), která využívá referenční signály z více eNodeB; Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), která poskytuje pomocná data přijímači [GNSS](/mobilnisite/slovnik/gnss/) v UE; Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)), která využívá časový předstih a měření signálu; a Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)). Pro 5G NR podporuje podobné metody jako [DL-TDOA](/mobilnisite/slovnik/dl-tdoa/) (Downlink TDOA) a Multi-RTT (Round Trip Time). E-SMLC komunikuje s UE přes protokol LPP (LTE Positioning Protocol) nebo jeho NR protějšek, NRPPa, za účelem získání měření nebo doručení pomocných dat. Také komunikuje s základnovými stanicemi (eNodeB/gNB) a v případě potřeby se Secure User Plane Location (SUPL) Enabled Location Server (SLP) přes protokol LPPa, aby získal informace o buňce nebo nakonfiguroval polohovací referenční signály.

Z architektonického hlediska obsahuje E-SMLC funkci výpočtu polohy. Zpracovává surová měřicí data (např. časové rozdíly, sílu signálu) přijatá od UE a/nebo sítě, aby vypočítal odhad zeměpisné šířky, délky a nejistoty. Výsledná poloha je pak doručena žadateli, jako je Gateway Mobile Location Centre (GMLC) pro externí aplikace nebo MME/AMF pro zpracování tísňového volání. Její fungování je podrobně definováno v řadě specifikací 3GPP pokrývajících servisní požadavky (23.271), procedury fáze 2 (36.305) a protokoly fáze 3 (36.355, 37.355).

## K čemu slouží

E-SMLC byl představen ve 3GPP Release 9, aby splnil přísné regulatorní požadavky na lokalizaci tísňových volání, jako je mandát E911 ve Spojených státech a směrnice E112 v Evropě. Předchozí metody určování polohy v sítích 2G/3G, často spoléhající na Cell-ID nebo méně standardizované přístupy v řídicí rovině, postrádaly přesnost a spolehlivost potřebnou pro rychlé nalezení osoby v nouzi. E-SMLC poskytl standardizovanou, síťovou architekturu pro polohování v řídicí rovině uvnitř celo-IP sítě LTE, což zajišťuje spolehlivé určení polohy nezávislé na stavu IP konektivity UE.

Kromě záchranných služeb vytvoření E-SMLC umožnilo širokou škálu komerčních a provozních služeb založených na poloze (LBS). Umožňuje operátorům mobilních sítí nabízet přesné určování polohy poskytovatelům aplikací třetích stran, podporovat sledování majetku a umožňovat úlohy optimalizace sítě, jako je analýza pokrytí. E-SMLC řešil omezení řešení v uživatelské rovině, jako je SUPL, která vyžadovala IP připojení a aktivní účast UE, tím, že poskytl síťově řízenou alternativu fungující i během stavů omezené služby. Jeho návrh zajistil škálovatelnost a podporu více vysoce přesných polohovacích metod, aby uspokojil různé požadavky případů užití.

## Klíčové vlastnosti

- Centralizované řízení polohovacích procedur UE v řídicí rovině
- Podpora více vysoce přesných polohovacích metod (OTDOA, A-GNSS, E-CID, UTDOA)
- Podpora protokolů LPP (s UE), LPPa (s eNB/gNB) a SLs/NLs (s MME/AMF)
- Výpočet konečných odhadů polohy ze surových měření ze sítě a od UE
- Předávání výsledků polohy autorizovaným síťovým entitám (např. GMLC)
- Vývoj pro podporu polohovacích technik 5G NR (DL-TDOA, Multi-RTT)

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 36.111** (Rel-19) — LMU Requirements for UTDOA Positioning
- **TS 36.112** (Rel-19) — E-UTRAN LMU Conformance Requirements
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 36.456** (Rel-19) — SLm Interface Introduction
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-SMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-smlc/)
