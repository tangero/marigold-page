---
slug: "bssgp"
url: "/mobilnisite/slovnik/bssgp/"
type: "slovnik"
title: "BSSGP – Base Station System GPRS Protocol"
date: 2025-01-01
abbr: "BSSGP"
fullName: "Base Station System GPRS Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bssgp/"
summary: "BSSGP je protokol vrstvy 3 fungující mezi SGSN a BSS přes rozhraní Gb v sítích 2G/3G GPRS a EDGE. Poskytuje nespojovaný přenos LLC PDU a podporuje funkce správy mobility, vyhledávání a správy rádiovýc"
---

BSSGP je protokol vrstvy 3 mezi SGSN a BSS přes rozhraní Gb, který poskytuje nespojovaný přenos LLC PDU a podporuje správu mobility, vyhledávání (paging) a správu rádiových prostředků.

## Popis

Base Station System [GPRS](/mobilnisite/slovnik/gprs/) Protocol (BSSGP) je klíčový síťový protokol definovaný ve specifikacích 3GPP pro sítě General Packet Radio Service (GPRS) a Enhanced Data rates for GSM Evolution ([EDGE](/mobilnisite/slovnik/edge/)). Funguje mezi Serving GPRS Support Node (SGSN) v jádru sítě a Base Station System ([BSS](/mobilnisite/slovnik/bss/)), který zahrnuje Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) a Base Transceiver Stations ([BTS](/mobilnisite/slovnik/bts/)), přes rozhraní Gb. BSSGP funguje jako nespojovaný protokol, který přenáší Logical Link Control ([LLC](/mobilnisite/slovnik/llc/)) Protocol Data Units (PDU) mezi SGSN a BSS, a zároveň nese zásadní signalizační informace pro správu mobility, vyhledávání a řízení rádiových prostředků.

Z architektonického hlediska se BSSGP nachází nad vrstvou Network Service (NS) a pod vrstvou LLC v zásobníku protokolů. Funguje v kontextu BSSGP Virtual Connections ([BVC](/mobilnisite/slovnik/bvc/)), které představují logická spojení mezi SGSN a konkrétními buňkami nebo skupinami buněk v BSS. Každý BVC je identifikován [BVCI](/mobilnisite/slovnik/bvci/) (BSSGP Virtual Connection Identifier), který má koncový význam přes rozhraní Gb. Protokol používá BSSGP PDU, které obsahují informační prvky jako Quality of Service (QoS) profily, úrovně rádiové priority a identifikátory směrovacích oblastí, aby usnadňovaly správné doručování dat a alokaci prostředků.

Klíčové komponenty BSSGP zahrnují BSSGP kontext, který udržuje stavové informace pro každou mobilní stanici, a různé typy zpráv pro různé funkce. Zprávy pro přenos dat uplink a downlink nesou uživatelská data, zatímco řídicí zprávy zvládají funkce jako vyhledávání, hlášení stavu rádiového rozhraní a řízení toku. BSSGP implementuje mechanismy řízení toku, aby zabránil zahlcení mezi SGSN a BSS, přičemž k regulaci přenosu LLC PDU používá okna založená na kreditech. Protokol také podporuje službu cell broadcast a služby založené na poloze prostřednictvím specifických typů zpráv a procedur.

BSSGP hraje zásadní roli v oddělení funkcí rádiové sítě a jádra sítě, což umožňuje SGSN zůstat nezávislé na konkrétních detailech technologie rádiového přístupu. Umožňuje SGSN spravovat mobilitu na úrovni směrovací oblasti, zatímco BSS zvládá mobilitu na úrovni buňky. Protokol podporuje jak potvrzovaný, tak nepotvrzovaný režim provozu, což poskytuje flexibilitu pro různé požadavky služeb. Návrh BSSGP umožňuje efektivní využití prostředků rozhraní Gb při zachování nezbytné kvality služeb pro paketové datové služby v sítích 2G a 3G.

## K čemu slouží

BSSGP byl vytvořen, aby řešil potřebu standardizovaného protokolu pro podporu paketově orientovaných datových služeb v sítích GSM, které byly původně navrženy primárně pro spojově orientovaný hlas. Před GPRS sítě GSM postrádaly efektivní mechanismy pro přenos paketových dat, což vyžadovalo neustálé navazování a ukončování spojení pro datové přenosy. BSSGP tento problém vyřešil tím, že poskytl nespojovaný transportní mechanismus, který mohl efektivně zvládat přerušovaný datový provoz a zároveň podporovat základní funkce správy mobility.

Protokol byl navržen tak, aby oddělil funkce jádra sítě (zajišťované SGSN) od funkcí rádiové přístupové sítě (zajišťovaných BSS), což umožnilo každé doméně vyvíjet se nezávisle. Toto oddělení umožnilo operátorům sítí modernizovat své rádiové přístupové sítě bez nutnosti měnit infrastrukturu jádra sítě, a naopak. BSSGP také řešil potřebu efektivního využívání prostředků implementací mechanismů řízení toku, které zabraňovaly zahlcení na rozhraní Gb mezi SGSN a BSS.

Historicky se BSSGP objevil jako součást standardizačního úsilí GPRS v 3GPP Release 97/98, s pokračujícími vylepšeními v následujících vydáních. Vyřešil omezení předchozích přístupů tím, že poskytl standardizovaná rozhraní a protokoly specificky optimalizované pro paketové datové služby, na rozdíl od spojově orientovaných protokolů používaných v tradičním GSM. BSSGP umožnil přechod od hlasově orientovaných sítí k sítím podporujícím data, čímž připravil cestu pro mobilní internetové služby a položil základy pro pozdější architektury paketových dat v 3G a 4G.

## Klíčové vlastnosti

- Nespojovaný přenos LLC PDU mezi SGSN a BSS
- Podpora BSSGP Virtual Connections (BVC) identifikovaných pomocí BVCI
- Mechanismy řízení toku využívající okna založená na kreditech
- Podpora správy mobility včetně vyhledávání a aktualizace polohy
- Oddělení funkcí rádiové sítě a jádra sítě
- Přenos a správa profilů Quality of Service (QoS)

## Související pojmy

- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [BVC – BSS GPRS Protocol Virtual Connection](/mobilnisite/slovnik/bvc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [BSSGP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bssgp/)
