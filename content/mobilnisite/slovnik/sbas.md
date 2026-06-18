---
slug: "sbas"
url: "/mobilnisite/slovnik/sbas/"
type: "slovnik"
title: "SBAS – Satellite Based Augmentation Systems"
date: 2025-01-01
abbr: "SBAS"
fullName: "Satellite Based Augmentation Systems"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbas/"
summary: "SBAS jsou satelitní systémy, které zlepšují přesnost, integritu a dostupnost signálů globálního navigačního satelitního systému (GNSS), například GPS. Jsou klíčové pro služby založené na poloze v sítí"
---

SBAS (Satellite Based Augmentation Systems, satelitní systémy pro zvýšení přesnosti) je satelitní systém, který zlepšuje přesnost, integritu a dostupnost signálů GNSS, jako je GPS, pro vysoce přesné lokalizační služby v sítích 3GPP.

## Popis

Satellite Based Augmentation Systems (SBAS, satelitní systémy pro zvýšení přesnosti) jsou regionální nebo rozsáhlé systémy, které zlepšují výkonnost základních konstelací globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou [GPS](/mobilnisite/slovnik/gps/), [GLONASS](/mobilnisite/slovnik/glonass/) nebo Galileo. Fungují tak, že nasazují síť přesně lokalizovaných pozemních referenčních stanic, které monitorují signály GNSS satelitů. Tyto stanice shromažďují data o chybách způsobených ionosférickými poruchami, driftem satelitních hodin a nepřesnostmi efemerid. Data jsou zpracována v centrální hlavní stanici za účelem generování diferenčních korekčních zpráv a informací o integritě. Tyto korekční zprávy jsou následně vysílány na geostacionární ([GEO](/mobilnisite/slovnik/geo/)) satelity, které je šíří v široké oblasti pokrytí k uživatelskému zařízení (UE). UE přijímá jak standardní GNSS signály, tak SBAS korekční signály, a aplikuje korekce v reálném čase pro výpočet přesnější a spolehlivější polohy.

V kontextu standardů 3GPP je SBAS integrován jako podporovaná metoda určování polohy, zejména pro Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Síť může poskytnout asistenční data UE, která mohou zahrnovat SBAS-specifické informace, jako jsou identity dostupných SBAS satelitů (např. [WAAS](/mobilnisite/slovnik/waas/), [EGNOS](/mobilnisite/slovnik/egnos/), [MSAS](/mobilnisite/slovnik/msas/)) a jejich charakteristiky signálu. Tato asistence pomáhá UE získat SBAS signály rychleji a s nižší spotřebou energie. Lokalizační měřicí jednotka UE zpracovává kombinované GNSS a SBAS signály za účelem vytvoření polohových měření, která jsou hlášena zpět do sítě prostřednictvím protokolů, jako je LTE Positioning Protocol (LPP) nebo NR Positioning Protocol (NRPPa).

Role SBAS v sítích 3GPP spočívá především v plnění přísných požadavků na polohové služby, zejména pro regulatorní povinnosti, jako je lokalizace tísňového volajícího. SBAS výrazně zlepšuje horizontální a vertikální přesnost, často ji snižuje na úroveň metrů. Poskytuje také klíčové informace o integritě, které uživatele upozorní, pokud systém nemá být z důvodu zjištěných chyb používán pro bezpečnostně kritické aplikace. To činí SBAS klíčovým prvkem pro pokročilé služby založené na poloze, vozidlovou komunikaci a aplikace vyžadující vysokou spolehlivost, které doplňují další metody určování polohy 3GPP, jako je Observed Time Difference of Arrival (OTDOA) a uplink Time Difference of Arrival (UTDOA).

## K čemu slouží

SBAS byl vytvořen, aby řešil inherentní omezení samostatného GNSS, který může trpět významnými chybami způsobenými atmosférickými vlivy, nepřesnostmi satelitních hodin a orbitálními chybami. Tyto chyby mohou snížit přesnost určení polohy na desítky metrů, což je nedostatečné pro bezpečnostně kritické aplikace, jako je letectví, námořní navigace a stále více i pro pozemní aplikace, jako je autonomní řízení a přesné záchranné služby. Před systémy pro zvýšení přesnosti museli uživatelé spoléhat na místní diferenční korekční stanice, které nabízely vysokou přesnost, ale pouze ve velmi omezené geografické oblasti. SBAS tento problém řeší poskytováním korekčních signálů pro rozsáhlé nebo regionální oblasti z geostacionárních satelitů, čímž zpřístupňuje vysoce přesné určování polohy s garantovanou integritou na celých kontinentech.

Integrace SBAS do standardů 3GPP, počínaje Release 8, byla motivována rostoucí regulatorní a komerční poptávkou po vysoce přesném a spolehlivém mobilním určování polohy. Předpisy v regionech, jako jsou Spojené státy (FCC E911) a Evropa (E112), ukládaly stále přesnější požadavky na informace o poloze pro tísňová volání. Zatímco existovaly síťové a asistované GNSS metody, SBAS nabídl způsob, jak tyto požadavky na přesnost splnit a překročit bez nutnosti hustého nasazení infrastruktury. Poskytl standardizovanou metodu pro využití stávající infrastruktury civilního letectví a navigace v telekomunikacích, čímž rozšířil schopnosti mobilních zařízení pro služby založené na poloze, logistiku a aplikace veřejné bezpečnosti.

## Klíčové vlastnosti

- Šíření diferenčních korekcí pro rozsáhlé oblasti prostřednictvím geostacionárních satelitů
- Zlepšuje přesnost GNSS na úroveň metrů nebo lepší
- Poskytuje monitoring integrity a výstrahy pro aplikace kritické z hlediska bezpečnosti života
- Podporován jako asistenční a měřicí metoda v 3GPP A-GNSS
- Zvyšuje dostupnost a kontinuitu polohové služby
- Funguje s více základními konstelacemi (GPS, GLONASS, Galileo)

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [SBAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbas/)
