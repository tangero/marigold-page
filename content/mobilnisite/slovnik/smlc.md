---
slug: "smlc"
url: "/mobilnisite/slovnik/smlc/"
type: "slovnik"
title: "SMLC – Standalone Mobile Location Center"
date: 2025-01-01
abbr: "SMLC"
fullName: "Standalone Mobile Location Center"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/smlc/"
summary: "Prvek základní sítě zodpovědný za výpočet geografické polohy mobilních zařízení (UE) pro služby založené na poloze. Řídí lokalizační metody a komunikuje s RAN a UE za účelem získání měření. Je klíčový"
---

SMLC je prvek základní sítě, který vypočítává geografickou polohu mobilních zařízení řízením lokalizačních metod a komunikací s rádiovou přístupovou sítí a zařízením.

## Popis

Standalone Mobile Location Center (SMLC) je vyhrazený síťový uzel v architektuře 3GPP, speciálně navržený pro určování polohy a lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)). Jeho primární funkcí je vypočítat zeměpisnou polohu uživatelského zařízení (UE) řízením a prováděním lokalizačních procedur. Jde o logickou funkci, která může být implementována jako samostatný fyzický uzel nebo integrována v jiných síťových prvcích, jako je řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) nebo řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS. SMLC funguje jako centrální koordinátor lokalizačních aktivit, který vybírá vhodnou lokalizační metodu na základě faktorů, jako je požadovaná přesnost, schopnosti UE a síťové podmínky.

Z architektonického hlediska má SMLC rozhraní k několika síťovým entitám. V GERAN se připojuje k BSC přes rozhraní Lb. V UMTS se připojuje k RNC přes rozhraní Iupc. Také komunikuje s Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)) přes rozhraní Lg pro koordinaci na úrovni služeb a se Serving Mobile Location Center (dalším typem SMLC integrovaným v [MSC](/mobilnisite/slovnik/msc/)/[SGSN](/mobilnisite/slovnik/sgsn/)) pro řízení. SMLC obsahuje Positioning Calculation Function (PCF), která provádí vlastní výpočet polohy pomocí měření, jako je časový předstih (TA), pozorovaný časový rozdíl příchodu (OTDOA) nebo data asistovaného GNSS (A-GNSS) přijatá od UE a/nebo sítě.

Provoz SMLC zahrnuje několik kroků. Po obdržení požadavku na polohu (např. od GMLC nebo pro vnitrosíťové účely) určí obsluhující buňku UE a použitelnou lokalizační metodu. Poté dá pokyn RAN (BSC/RNC) a případně UE, aby provedla potřebná rádiová měření. Tato měření jsou hlášena zpět SMLC, který zpracovává nezpracovaná data pomocí algoritmů, jako je triangulace nebo trilaterace, aby vypočítal zeměpisnou šířku, délku a odhad nejistoty. Výsledek je následně naformátován a vrácen žadateli. SMLC také řeší chybové stavy související s určováním polohy a může podporovat záložní metody, pokud selže primární metoda.

Jeho role je základní pro sadu funkcí Location Services (LCS) v sítích 2G, 3G a raného 4G. Abstrahuje složitosti různých technologií rádiového přístupu a lokalizačních technik od servisní vrstvy a poskytuje standardizovaný mechanismus pro získání polohy UE. Zatímco jeho význam poklesl s vývojem LTE a 5G, kde jsou lokalizační funkce více integrovány do E-SMLC (Evolved SMLC) a Location Management Function (LMF), SMLC definoval základní principy pro síťové a síťově asistované určování polohy mobilních zařízení.

## K čemu slouží

SMLC byl vytvořen za účelem standardizace a centralizace schopností určování polohy mobilních zařízení v celulárních sítích, což se stalo nezbytnou funkcí s nástupem regulatorních a komerčních požadavků na služby založené na poloze. Před jeho standardizací se používala proprietární řešení nebo omezená lokalizace na základě Cell-ID, která byla nedostatečná pro požadavky tísňových služeb, jako je Enhanced 911 (E911) v USA, které vyžadovaly přesnější a spolehlivější určení polohy. SMLC poskytl vyhrazenou, standardizovanou síťovou funkci pro splnění těchto zákonných povinností.

Vyřešil problém fragmentovaných, technologií specifických implementací určování polohy. Zavedením SMLC vytvořil 3GPP jednotný architektonický rámec pro Location Services (LCS), který mohl fungovat napříč sítěmi GSM a UMTS. Umožnil síťovým operátorům nasadit jedinou platformu pro podporu více lokalizačních metod (např. Cell-ID, TA, OTDOA, A-GNSS) a obsluhovat různé klienty, od tísňových služeb a orgánů pro zákonný odposlech až po komerční poskytovatele služeb nabízejících navigaci nebo reklamu založenou na poloze.

Motivace byla hnána třemi klíčovými faktory: regulatorním tlakem na lokalizaci tísňových volajících, komerčním potenciálem služeb založených na poloze a potřebou optimalizace sítě (např. předávání hovorů asistované polohou). SMLC umožnil operátorům dodržovat zákony, generovat nové zdroje příjmů a zlepšovat výkon sítě, a to vše prostřednictvím řízeného, zabezpečeného a zpoplatnitelného rozhraní (GMLC), které spravovalo přístup k citlivým lokalizačním datům.

## Klíčové vlastnosti

- Centralizovaná koordinace a výpočet geografické polohy UE
- Podpora více lokalizačních metod (např. Cell-ID, TA, OTDOA, A-GNSS)
- Rozhraní k RAN (BSC přes Lb, RNC přes Iupc) a základní síti (GMLC přes Lg)
- Obsahuje Positioning Calculation Function (PCF) pro výpočet polohy
- Řídí lokalizační procedury a sběr měření od UE a sítě
- Poskytuje odhady polohy s přidruženými údaji o přesnosti a nejistotě

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [SMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/smlc/)
