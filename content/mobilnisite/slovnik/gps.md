---
slug: "gps"
url: "/mobilnisite/slovnik/gps/"
type: "slovnik"
title: "GPS – Global Positioning System"
date: 2025-01-01
abbr: "GPS"
fullName: "Global Positioning System"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gps/"
summary: "Satelitní radionavigační systém provozovaný vládou Spojených států, který poskytuje informace o geografické poloze a čase přijímačům GPS kdekoli na Zemi. V 3GPP je uváděn jako metoda pro určování polo"
---

GPS je satelitní radionavigační systém provozovaný vládou Spojených států, který poskytuje informace o geografické poloze a času a je v 3GPP uváděn jako metoda pro určování polohy uživatelského zařízení.

## Popis

Ve specifikacích 3GPP je GPS uváděn jako externí polohovací systém, který může být využíván uživatelským zařízením (UE) a sítí ke stanovení geografické polohy mobilního zařízení. Architektura 3GPP integruje GPS jako jednu z několika polohovacích metod, často kategorizovaných jako režimy založené na UE nebo asistované UE. Při polohování založeném na UE obsahuje UE přijímač GPS, vypočítá svou vlastní polohu pomocí signálů z družic GPS a může ji nahlásit síti. Při polohování asistovaném UE měří UE parametry GPS signálu (např. pseudovzdálenosti) a odesílá tato nezpracovaná měření do polohovacího uzlu sítě (např. [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, [LMF](/mobilnisite/slovnik/lmf/) v 5GC), který následně polohu vypočítá. 3GPP definuje protokoly signalizační roviny a uživatelské roviny (např. [LPP](/mobilnisite/slovnik/lpp/), [SUPL](/mobilnisite/slovnik/supl/)) pro usnadnění výměny asistenčních dat GPS (jako efemeridy, almanach) ze sítě do UE, což výrazně zlepšuje čas do prvního určení polohy ([TTFF](/mobilnisite/slovnik/ttff/)) a přesnost. Síť může požadovat odhad polohy pomocí GPS samostatně nebo v kombinaci s jinými metodami ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Specifikace podrobně popisují požadavky na výkon (např. v TS 25.171, 36.171), testovací postupy a způsob začlenění měření GPS do širších polohovacích architektur, jako je Control Plane [LCS](/mobilnisite/slovnik/lcs/) nebo [OMA](/mobilnisite/slovnik/oma/) SUPL.

## K čemu slouží

GPS je začleněn do norem 3GPP, aby poskytoval vysoce přesnou a široce dostupnou metodu pro určování polohy mobilních zařízení, což je základním požadavkem pro regulatorní služby (jako je lokalizace nouzových volání), komerční služby založené na poloze (LBS) a funkce optimalizace sítě. Před integrací GPS se polohování v celulárních sítích spoléhalo především na metody založené na síti, jako je Cell-ID, časový předstih nebo OTDOA, které nabízely omezenou přesnost, zejména ve venkovských nebo příměstských oblastech. Začlenění GPS (a později dalších konstelací GNSS) řešilo potřebu přesnosti na úrovni metrů, kterou vyžadují aplikace jako navigace s pokyny od zatáčky k zatáčce, sledování majetku a nařízení pro vylepšené služby 911 (E911). Práce 3GPP standardizovala způsob, jakým může celulární síť asistovat přijímači GPS v UE (čímž vzniká A-GPS), aby se překonala omezení jako pomalé startovní časy samostatného GPS a špatná citlivost v interiérech, čímž se spolehlivé, rychlé a přesné určování polohy stalo životaschopnou službou pro masově rozšířená zařízení. Tuto integraci poháněly jak regulatorní tlaky na zlepšení služeb pro nouzové volání, tak komerční potenciál služeb LBS.

## Klíčové vlastnosti

- Poskytuje vysoce přesné geografické určení polohy (typicky <10m na otevřeném prostranství)
- Podporován jako metoda určování polohy v režimech založených na UE a asistovaných UE
- Integrován s protokoly signalizační roviny (např. LPP) a uživatelské roviny (např. SUPL) 3GPP
- Síť může doručovat asistenční data GPS (efemeridy, almanach, čas) do UE
- Podléhá specifikacím výkonu a testům shody 3GPP
- Často používán v hybridní/kombinaci s jinými polohovacími metodami (A-GNSS)

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.032** (Rel-19) — Universal Geographical Area Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [GPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gps/)
