---
slug: "ns"
url: "/mobilnisite/slovnik/ns/"
type: "slovnik"
title: "NS – No Speech-call capability"
date: 2026-01-01
abbr: "NS"
fullName: "No Speech-call capability"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ns/"
summary: "NS označuje schopnost (capability) uživatelského zařízení (UE), která signalizuje, že zařízení nepodporuje tradiční hlasové hovory v přepojování okruhů (CS). Jedná se o základní charakteristiku zaříze"
---

NS je schopnost (capability) uživatelského zařízení (UE) označující, že zařízení nepodporuje tradiční hlasové hovory v přepojování okruhů (circuit-switched), což ovlivňuje připojení k síti a poskytování služeb.

## Popis

Schopnost No Speech-call (NS) je parametr schopností uživatelského zařízení (UE) definovaný v mnoha specifikacích 3GPP. Jedná se o booleovský indikátor, který síti signalizuje, zda je UE schopno navázat a udržovat tradiční hlasový hovor v přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)). Když se UE registruje v síti a indikuje schopnost NS, výslovně tím informuje jádro sítě – konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPS nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GS – že pro něj nelze provést volání (paging) ani jej obsloužit službami CS domény, jako je Voice over CS (VoCS).

Z architektonického hlediska příznak NS ovlivňuje postupy správy mobility a relace v síti. V síti 4G EPS, která je pouze paketově přepínaná, je běžná přítomnost CS fallbacku ([CSFB](/mobilnisite/slovnik/csfb/)) pro hlasové služby. UE bez schopnosti NS by typicky použilo CSFB pro přechod na síť 2G/3G kvůli hlasovému hovoru. Avšak UE deklarující schopnost NS je považováno za zařízení, které 'nepodporuje CS hlas'. Síť se u něj nepokusí spustit procedury CSFB. Místo toho musí být hlasová služba, pokud je vyžadována, doručena prostřednictvím metod přepojování paketů, jako je Voice over LTE (VoLTE) pomocí IMS, nebo v 5G Voice over NR (VoNR). Pro zařízení pouze pro data nebo IoT je NS trvalou charakteristikou a síť bude poskytovat pouze datové služby v přepojování paketů.

Role NS v síti je klíčová pro efektivní správu zdrojů a doručování služeb. Zabrání síti plýtvat signalizačními zdroji pokusy o doručení CS služeb zařízení, které je nemůže použít. Také usměrňuje rozhodování o politikách; například UE s nastaveným NS může být zakázáno připojit se k určitým technologiím rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)), které jsou primárně orientované na CS, nebo může být nasměrováno k síťovým řezům optimalizovaným pro massive IoT (mIoT), kde je hlas irelevantní. Tato schopnost je vyměněna během počáteční registrace (ATTACH nebo REGISTRATION REQUEST) a je uložena v kontextu účastníka v jádru sítě, což ovlivňuje následné příkazy správy mobility a relace.

## K čemu slouží

Schopnost NS existuje, aby explicitně sdělila síti servisní omezení zařízení, a řeší tak problém neefektivních a neúspěšných pokusů o doručení služeb. V časných mobilních sítích se předpokládalo, že všechna UE podporují hlasové hovory. S příchodem zařízení zaměřených na data, jako jsou dongly, tablety a později široká škála IoT senzorů, se tento předpoklad stal neplatným. Bez explicitního indikátoru by se síť marně pokoušela volat tato zařízení pro hlasové hovory nebo spouštět složité procedury [CS](/mobilnisite/slovnik/cs/) fallbacku, což by vedlo ke kongesci signalizace a neúspěšným pokusům o služby.

Historicky byla tato schopnost formalizována, jak se sítě vyvíjely směrem k plně IP, paketově přepínaným architekturám, jako jsou LTE a 5G NR. Řeší omezení předchozího implicitního modelu tím, že poskytuje jasný binární signál. To umožňuje optimalizované chování sítě: zařízení pouze pro data mohou být spravována efektivněji a síť může bezproblémově nabízet alternativní hlasová řešení (jako VoLTE) zařízením, která je podporují, a zároveň se vyhýbat zastaralým CS cestám pro ta, která je nepodporují. Její vytvoření bylo motivováno potřebou škálovatelné a efektivní komunikace typu stroj-stroj a jasného oddělení mezi profilem zařízení orientovaných na hlas a zařízení orientovaných na data v moderní telekomunikaci.

## Klíčové vlastnosti

- Binární indikátor schopností UE vyměňovaný během registrace v síti
- Zabraňuje síti v iniciování procedur služeb přepojování okruhů (CS) pro dané UE
- Ovlivňuje rozhodnutí správy mobility (např. nespouští CSFB)
- Zásadní pro klasifikaci a obsluhu zařízení pouze pro data a IoT
- Uložen v kontextu účastníka v jádru sítě (MME/AMF) po dobu trvání relace
- Umožňuje optimalizaci sítě tím, že se vyhýbá zbytečné signalizaci za nepodporované služby

## Související pojmy

- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.834** (Rel-18) — Technical Report
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TR 32.847** (Rel-18) — Technical Report
- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TS 37.825** (Rel-16) — High Power UE (PC2) for EN-DC TDD-TDD
- **TR 37.829** (Rel-18) — Technical Report
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [NS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns/)
