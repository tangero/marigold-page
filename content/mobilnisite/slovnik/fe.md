---
slug: "fe"
url: "/mobilnisite/slovnik/fe/"
type: "slovnik"
title: "FE – Functional Entity"
date: 2025-01-01
abbr: "FE"
fullName: "Functional Entity"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fe/"
summary: "Funkční entita (FE) je konceptuální stavební blok v architektuře sítí 3GPP představující diskrétní soubor funkcí. Jde o logickou abstrakci používanou k definování schopností a rozhraní bez vynucení ko"
---

FE je konceptuální stavební blok v architektuře sítě 3GPP představující diskrétní soubor funkcí; používá se jako logická abstrakce k definování schopností a rozhraní bez předepisování konkrétní fyzické implementace.

## Popis

Funkční entita je základním návrhovým konceptem ve standardech 3GPP a představuje logické seskupení příbuzných síťových funkcí. Není to fyzický uzel ani hardwarová součástka, ale spíše specifikační nástroj popisující, co musí síť dělat. Každá FE zapouzdřuje konkrétní soubor schopností, jako je řízení hovoru, správa mobility, správa relací nebo přepojování uživatelské roviny. Chování FE je definováno jejími funkčními procedurami, informacemi, které zpracovává, a jejími interakcemi s ostatními FEs přes přesně definované referenční body. Například v klasické jádrové síti s přepojováním okruhů je [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) popsána jako soubor FEs, jako jsou entity řízení hovoru ([CC](/mobilnisite/slovnik/cc/)), správy mobility ([MM](/mobilnisite/slovnik/mm/)) a propojování ([IWU](/mobilnisite/slovnik/iwu/)).

Specifikace FEs umožňuje 3GPP vytvářet modulární a flexibilní architekturu. Síťové prvky nebo síťové funkce (jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) nebo [UPF](/mobilnisite/slovnik/upf/) v 5GC) jsou definovány agregací konkrétních FEs. Tato abstrakce odděluje 'co' od 'jak', což umožňuje různým dodavatelům implementovat požadované funkce různými způsoby – ať už na dedikovaném hardwaru, virtualizovaném softwaru nebo cloud-nativních mikroslužbách – při zachování end-to-end interoperability. Interakce mezi FEs jsou standardizovány jako protokoly přes referenční body (např. N1, [N2](/mobilnisite/slovnik/n2/), N4 v 5G). Tyto protokoly, jako NGAP nebo PFCP, efektivně definují komunikaci mezi logickými funkcemi, které FEs představují.

Z architektonického hlediska je definice FEs jedním z prvních kroků při návrhu nového systému nebo služby v 3GPP. Zahrnuje identifikaci nezbytných funkcí, jejich seskupení do soudržných entit a specifikaci toků informací mezi nimi. Tento model je všudypřítomný napříč všemi doménami 3GPP: jádrovou sítí (CN), rádiovou přístupovou sítí (RAN) a uživatelským zařízením (UE). Poskytuje stabilní rámec, který se může v čase vyvíjet; nové FEs mohou být zavedeny a stávající mohou být upraveny nebo rozděleny bez nutnosti změny fyzického nasazení sítě. Tato konceptuální jasnost je zásadní pro inženýry navrhující, testující a integrující komplexní telekomunikační systémy.

## K čemu slouží

Koncept funkční entity byl zaveden pro zvládnutí komplexity specifikace rozsáhlých, více-dodavatelských telekomunikačních systémů. Rané standardy mobilních sítí riskovaly být příliš direktivní ohledně fyzických implementací, což by mohlo potlačovat inovace a svazovat operátory ke konkrétním dodavatelům. Model FE zavedl jasné oddělení zájmů tím, že definoval systém z hlediska logických funkcí namísto fyzických zařízení. Tím bylo vyřešeno zajištění interoperability při současném poskytnutí svobody dodavatelům a operátorům ve volbě implementace a nasazení, jako je konsolidace více FEs do jednoho fyzického uzlu nebo jejich distribuce v cloudové infrastruktuře.

Historicky byl tento přístup upevněn ve verzi 3GPP Release 99 formalizací architektury UMTS, která stavěla na principech z ITU-T a dřívějších specifikací GSM. Odstranil omezení monolitických specifikací síťových prvků tím, že poskytl modulární plán. Tato modularita se stala čím dál kritičtější s vývojem směrem k čistě IP sítím (IMS), EPC v LTE a zejména cloud-nativního 5G jádra (5GC). Koncept FE přímo umožnil přechod k virtualizaci síťových funkcí (NFV) a servisně orientovaným architekturám (SBA), kde jsou tradiční síťové prvky rozloženy na softwarové síťové funkce (NFs), z nichž každá často odpovídá jedné nebo více dobře definovaným funkčním entitám. FE je tedy základní abstrakcí, která umožnila sítím 3GPP vyvinout se z hardwarově orientovaných přepínačů na agilní, softwarově definované servisní platformy.

## Klíčové vlastnosti

- Logická abstrakce diskrétního souboru síťových funkcí
- Definuje schopnosti a chování nezávisle na implementaci
- Slouží jako stavební blok pro skládání fyzických síťových prvků nebo softwarových síťových funkcí
- Interaguje s ostatními FEs přes standardizované referenční body a protokoly
- Umožňuje modulární, flexibilní a do budoucna připravený návrh síťové architektury
- Základní pro zajištění více-dodavatelské interoperability v celém systému

## Definující specifikace

- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.335** (Rel-19) — User Data Convergence (UDC) Procedures
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 29.335** (Rel-19) — Ud Interface Protocol for UDC (Stage 3)
- **TS 32.182** (Rel-19) — UDC Common Baseline Information Model (CBIM)
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TR 32.901** (Rel-19) — UDC Application Data Models Study

---

📖 **Anglický originál a plná specifikace:** [FE na 3GPP Explorer](https://3gpp-explorer.com/glossary/fe/)
