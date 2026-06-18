---
slug: "mt"
url: "/mobilnisite/slovnik/mt/"
type: "slovnik"
title: "MT – Mobile Terminated Short Message Service"
date: 2026-01-01
abbr: "MT"
fullName: "Mobile Terminated Short Message Service"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mt/"
summary: "Mobile Terminated (MT) označuje síťově iniciované doručení služby krátkých textových zpráv (SMS) do mobilního zařízení. Jedná se o klíčovou součást ekosystému SMS, která umožňuje přijímání textových z"
---

MT je síťově iniciované doručení služby krátkých textových zpráv (SMS) do mobilního zařízení, které umožňuje přijímání textových zpráv.

## Popis

Mobile Terminated Short Message Service ([MT-SMS](/mobilnisite/slovnik/mt-sms/)) je proces, při kterém centrum služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) doručí textovou zprávu uživatelskému zařízení (UE). Architektura zahrnuje několik síťových entit: původní entitu (což může být jiné UE nebo aplikace), SMSC, Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro směrovací informace, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro sítě s přepojováním okruhů, nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) pro sítě s přepojováním paketů v pozdějších vydáních. Proces začíná, když SMSC obdrží zprávu určenou pro účastníka. Dotazuje se HLR/HSS, aby získalo aktuální směrovací informace (např. adresu obsluhujícího MSC nebo SGSN/MME). SMSC poté přepošle zprávu tomuto obsluhujícímu uzlu pomocí protokolu MAP (Mobile Application Part) v GSM/UMTS nebo Diameter v LTE/5G. Obsluhující uzel vyvolá UE a po jeho odpovědi naváže potřebné signalizační spojení k doručení obsahu SMS. V LTE a 5G lze SMS doručovat jak přes Circuit-Switched Fallback (CSFB), tak přes IP Multimedia Subsystem (IMS) prostřednictvím rozhraní SGs a SGd, nebo přímo přes Non-Access Stratum (NAS) jako SMS over NAS. Procedura MT je úzce integrována se správou mobility, což zajišťuje doručení zprávy i při roamingu uživatele. Podporuje jak režim point-to-point, tak režim cell broadcast. Mechanismy spolehlivosti zahrnují potvrzení o doručení a opakované pokusy při selhání. Služba je definována v široké škále specifikací 3GPP, pokrývajících servisní požadavky, architekturu, protokoly a účtování.

## K čemu slouží

Účelem MT-SMS je poskytnout spolehlivý mechanismus typu store-and-forward pro doručování textových zpráv mobilním účastníkům. Vyřešil problém asynchronní, nereálné komunikace, kdy příjemce může být dočasně nedostupný (např. vypnutý telefon nebo mimo pokrytí). Před SMS byla mobilní komunikace primárně zaměřená na hlas. SMS zavedla datovou službu s nízkou šířkou pásma a vysokou účinností, která využívala stávající signalizační kanály a minimalizovala dopad na síť. Její vznik byl motivován potřebou jednoduché, všudypřítomné zprávové služby, která by mohla fungovat ve všech GSM (a později 3GPP) sítích po celém světě. Odstranila omezení, které vyžadovalo současnou dostupnost obou stran, jako je tomu u hlasových hovorů. Komponenta MT konkrétně zajišťuje, že síť může iniciovat doručení do mobilního zařízení, což je nezbytné pro jakoukoli službu, kde původce není samotné UE, jako jsou výstrahy, oznámení a zprávy od aplikací k osobám (application-to-person). Její standardizace zajistila interoperabilitu mezi různými síťovými operátory a výrobci zařízení, což bylo klíčové pro její celosvětový úspěch.

## Klíčové vlastnosti

- Mechanismus doručení typu store-and-forward
- Využívá signalizační kanály (např. SDCCH v GSM, NAS v LTE/5G)
- Spolupracuje s HLR/HSS pro určení polohy účastníka a směrování
- Podporuje potvrzení o doručení a oznámení o selhání
- Může být doručeno přes CSFB, SMS over NAS nebo IMS v pokročilejších architekturách
- Globální interoperabilita díky standardizovaným procedurám MAP a Diameter

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MO-SMS – Mobile Originated Short Message Service](/mobilnisite/slovnik/mo-sms/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.031** (Rel-19) — Fraud Information Gathering System (FIGS) Stage 1
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.101** (Rel-19) — UMTS Architecture and Functional Separation
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [MT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mt/)
