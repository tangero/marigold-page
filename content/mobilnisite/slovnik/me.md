---
slug: "me"
url: "/mobilnisite/slovnik/me/"
type: "slovnik"
title: "ME – Mobile Equipment"
date: 2026-01-01
abbr: "ME"
fullName: "Mobile Equipment"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/me/"
summary: "Fyzické zařízení používané účastníkem pro mobilní komunikaci, zahrnující koncové zařízení (TE), koncový adaptér (TA) a mobilní ukončení (MT). Jedná se o účastnický telefonní přístroj nebo zařízení, kt"
---

ME (Mobilní zařízení) je fyzické zařízení, například telefonní přístroj, používané účastníkem pro mobilní komunikaci, které zahrnuje koncové zařízení (Terminal Equipment), koncový adaptér (Terminal Adapter) a mobilní ukončení (Mobile Termination) pro připojení k síti.

## Popis

Mobile Equipment (ME) je základní koncept ve standardech 3GPP představující kompletní fyzické zařízení používané koncovým uživatelem pro přístup k mobilním telekomunikačním službám. Formálně je definováno jako kombinace tří funkčních komponent: koncového zařízení (Terminal Equipment – TE), koncového adaptéru (Terminal Adapter – TA) a mobilního ukončení (Mobile Termination – [MT](/mobilnisite/slovnik/mt/)). TE je část obsahující aplikace a uživatelské rozhraní, například notebook nebo PDA. TA zajišťuje potřebnou adaptaci mezi TE a MT, často zahrnující převod protokolů. MT je základní rádiový modem a funkce síťového ukončení zodpovědná za fyzickou vrstvu, správu rádiových zdrojů, správu mobility a řízení hovorů pro připojení k mobilní síti. ME obsahuje univerzální integrovaný obvodovou kartu (UICC), na které je aplikace modulu SIM, ale ME a UICC jsou samostatné entity; ME poskytuje prostředí pro fungování UICC.

Z architektonického hlediska ME komunikuje s uživatelským zařízením (UE), což je širší termén zahrnující jak ME, tak UICC. ME provádí protokoly definované ve specifikacích 3GPP pro komunikaci přes rádiové rozhraní Uu se základnovou stanicí (např. NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB). Implementuje vrstvy od fyzické vrstvy až po protokoly ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) pro signalizaci v jádru sítě. Schopnosti ME, jako podporovaná kmitočtová pásma, technologie rádiového přístupu (GSM, UMTS, LTE, NR), výkonová třída a sady funkcí, jsou podrobně popsány v jeho technických specifikacích a ověřovány prostřednictvím testů shody.

Jeho úlohou v síti je být koncovým bodem pro veškerou rádiovou komunikaci. Funkce MT v ME spravuje rádiové spojení, včetně modulace, kódování, řízení výkonu, provádění předávání hovoru a podávání hlášení o měřeních. Funkce TE/TA zpracovávají uživatelské datové aplikace a služby. Oddělení funkcí umožňuje flexibilitu, například připojení externích TE (jako notebook) k MT (jako mobilní modem) přes TA. ME je také klíčovou entitou pro správu zařízení, bezpečnostní procedury (jako autentizace a šifrování iniciované sítí, ale prováděné v ME) a rozhraní pro zákonné odposlechy. Výkon a spolehlivost ME přímo ovlivňují uživatelský zážitek a efektivitu sítě.

## K čemu slouží

Koncept Mobile Equipment byl zaveden, aby poskytl jasnou, standardizovanou definici uživatelského zařízení v rámci architektury mobilní sítě. Řeší problém nejednoznačnosti mezi hardwarovým zařízením a identitou účastníka oddělením ME od UICC/SIM. Toto oddělení je zásadní pro umožnění funkcí, jako je výměna SIM karet mezi zařízeními, a pro definování jasných odpovědností při certifikaci zařízení a schvalování typu.

Historicky, jak se mobilní technologie vyvíjela od jednoduchých hlasových telefonů ke složitým multimediálním zařízením, vznikla potřeba modularizovat funkce zařízení. Model TE-MT, převzatý z [ISDN](/mobilnisite/slovnik/isdn/) a adaptovaný pro GSM, umožnil integraci datových aplikací. Koncept ME toto zapouzdřuje a zajišťuje, aby měli síťoví operátoři a normalizační orgány konzistentní referenční bod pro specifikaci požadavků na rádiové rozhraní, testovací protokoly a bezpečnostní mechanismy. Odstraňuje omezení plynoucí z pohledu na telefonní přístroj jako na monolitický blok definováním interoperabilních funkčních bloků, což usnadnilo růst rozmanitého ekosystému zařízení a oddělení výroby zařízení od správy identity účastníka.

## Klíčové vlastnosti

- Integruje funkce koncového zařízení (TE), koncového adaptéru (TA) a mobilního ukončení (MT)
- Obsahuje UICC, ale je logicky odděleno od identity účastníka
- Implementuje celý zásobník protokolů pro rádiový přístup (rozhraní Uu)
- Podléhá testům shody a schvalování typu dle specifikací 3GPP
- Spravuje řízení rádiových zdrojů, správu mobility a řízení hovorů
- Poskytuje fyzickou platformu pro uživatelské aplikace a služby

## Související pojmy

- [MT – Mobile Terminated Short Message Service](/mobilnisite/slovnik/mt/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.101** (Rel-19) — UMTS Architecture and Functional Separation
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- … a dalších 64 specifikací

---

📖 **Anglický originál a plná specifikace:** [ME na 3GPP Explorer](https://3gpp-explorer.com/glossary/me/)
