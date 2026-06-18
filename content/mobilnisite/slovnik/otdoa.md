---
slug: "otdoa"
url: "/mobilnisite/slovnik/otdoa/"
type: "slovnik"
title: "OTDOA – Observed Time Difference Of Arrival"
date: 2025-01-01
abbr: "OTDOA"
fullName: "Observed Time Difference Of Arrival"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/otdoa/"
summary: "Síťová metoda určování polohy, která vypočítává umístění mobilního zařízení měřením časového rozdílu příjmu signálů z více základnových stanic. Poskytuje lokalizační služby pro tísňová volání, zákonný"
---

OTDOA je síťová metoda určování polohy, která vypočítává umístění mobilního zařízení měřením časového rozdílu příjmu signálů z více základnových stanic.

## Popis

Observed Time Difference of Arrival (OTDOA) je downlinková metoda určování polohy standardizovaná organizací 3GPP. Funguje tak, že uživatelské zařízení (UE) měří Referenční signálový časový rozdíl ([RSTD](/mobilnisite/slovnik/rstd/)) mezi signály přijatými z více sousedních eNBs nebo gNBs a referenční buňkou, typicky obslužnou buňkou. Tato měření RSTD jsou hlášena síti, konkrétně lokalizačnímu serveru (např. Evolved Serving Mobile Location Centre - [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, Location Management Function - [LMF](/mobilnisite/slovnik/lmf/) v 5GC). Lokalizační server, který zná přesné zeměpisné souřadnice a časování zapojených základnových stanic, používá multilaterační algoritmy (jako hyperbolické určování polohy) k výpočtu polohy UE na základě časových rozdílů. Přesnost závisí na faktorech, jako je počet měřitelných buněk, jejich geometrické rozložení a kvalita signálu.

V architektuře je UE měřicím zařízením, zatímco lokalizační server je výpočetní entitou. Rozhraní mezi UE a lokalizačním serverem pro zasílání zpráv lokalizačního protokolu je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) v LTE a NR, přenášený přes uživatelskou nebo řídicí rovinu. Aby síť podporovala OTDOA, musí základnové stanice vysílat Positioning Reference Signals ([PRS](/mobilnisite/slovnik/prs/)) – speciálně navržené sekvence s nízkým rušením a vysokou periodicitou pro zlepšení přesnosti měření a slyšitelnosti vzdálených buněk. Síť musí také poskytovat UE asistenční data, včetně konfigurace PRS sousedních buněk, prostřednictvím protokolu LPP, aby naváděla měření UE.

Role OTDOA je nedílnou součástí lokalizačního rámce 3GPP a doplňuje další metody, jako je Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) a Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)). Je to primární řešení pro určování polohy v interiérech nebo scénářích, kde nejsou dostupné signály GNSS. Metoda je řízena sítí, ale asistována UE, což vyvažuje výpočetní zátěž. Průběžná vylepšení napříč releasy se zaměřovala na zlepšení přesnosti, snížení latence a podporu nových scénářů nasazení, jako je určování polohy v interiérech, pro IoT a vehicle-to-everything (V2X), což z ní činí základní kámen pro komerční a regulační služby založené na poloze.

## K čemu slouží

OTDOA byla vytvořena za účelem splnění regulačních požadavků na lokalizaci tísňových volání (např. E911 v USA, E112 v Evropě) a umožnění komerčních služeb založených na poloze (LBS) v rámci buněčných sítí. Před její standardizací byly možnosti síťového určování polohy omezeny na méně přesné metody, jako je Cell ID (zobrazující oblast obslužné buňky) nebo časový posun, které poskytovaly nízkou granularitu. Potřeba přesnějšího, spolehlivějšího a všudypřítomného určování polohy, zejména pro uživatele bez zařízení s podporou GNSS nebo v prostředích bez GNSS, jako jsou hluboké interiéry, poháněla vývoj OTDOA.

Tato technologie řeší problém určení zeměpisné polohy mobilního zařízení pomocí samotné stávající infrastruktury buněčného rádiového přístupu. Řeší omezení metod založených na satelitech, které selhávají v interiérech nebo městských kaňonech, a jednodušších síťových metod, kterým chybí přesnost. Využitím synchronizovaného časování buněčné sítě poskytuje OTDOA standardizovanou, interoperabilní metodu, kterou mohou operátoři nasadit, aby splnili zákonné požadavky pro tísňové služby a vytvořili nové zdroje příjmů prostřednictvím sledování majetku, navigace a reklamy založené na blízkosti.

Historicky její zavedení v 3GPP Release 9 pro LTE (s přípravnými pracemi v dřívějších releasech UMTS) představovalo významný krok k tomu, aby se buněčné sítě staly lokalizačně schopnými. Průběžný vývoj v následujících releasech odráží rostoucí požadavky na vyšší přesnost (až na úroveň metrů), nižší spotřebu energie pro zařízení IoT a podporu nových případů užití v 5G, jako jsou průmyslové senzorové sítě a autonomní systémy vyžadující přesné určování polohy.

## Klíčové vlastnosti

- Downlinkové určování polohy využívající měření signálů sousedních buněk ze strany UE
- Využívá Positioning Reference Signals (PRS) pro přesná měření času příjmu
- Používá LTE Positioning Protocol (LPP) a NR Positioning Protocol (NPP) pro komunikaci mezi UE a lokalizačním serverem
- Podporuje architektury přenosu lokalizačních dat přes řídicí i uživatelskou rovinu
- Poskytuje přesnost na úrovni metrů za příznivých podmínek s dobrou geometrií buněk
- Zlepšuje slyšitelnost vzdálených buněk prostřednictvím konfigurací PRS s nízkým rušením a vysokým výkonem

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [E-CID – Enhanced Cell-ID](/mobilnisite/slovnik/e-cid/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [OTDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/otdoa/)
