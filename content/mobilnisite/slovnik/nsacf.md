---
slug: "nsacf"
url: "/mobilnisite/slovnik/nsacf/"
type: "slovnik"
title: "NSACF – Network Slice Admission Control Function"
date: 2026-01-01
abbr: "NSACF"
fullName: "Network Slice Admission Control Function"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nsacf/"
summary: "Vyhrazená síťová funkce implementující politiku řízení přístupu k síťovým řezům (NSAC). Udržuje aktuální počet registrovaných UE na síťový řez a poskytuje rozhodnutí o přístupu AMF, čímž slouží jako c"
---

NSACF je síťová funkce, která vynucuje politiku řízení přístupu k síťovým řezům (Network Slice Admission Control) sledováním registrovaných UE na řez a poskytováním rozhodnutí o přístupu AMF pro vynucení limitů kapacity řezu.

## Popis

Funkce řízení přístupu k síťovým řezům (NSACF) je klíčová síťová funkce řídicí roviny zavedená ve specifikaci 3GPP Release 17 jako centrální entita zodpovědná za provádění politik řízení přístupu k síťovým řezům ([NSAC](/mobilnisite/slovnik/nsac/)). Jedná se o logickou funkci, kterou lze nasadit jako samostatný síťový prvek nebo společně s jinými funkcemi řídicí roviny. Hlavní úlohou NSACF je spravovat a vynucovat maximální povolený počet uživatelských zařízení (UE) registrovaných ke každé instanci síťového řezu ([NSI](/mobilnisite/slovnik/nsi/)). Toho dosahuje udržováním přesných počítadel registrací a odregistrací UE v reálném čase pro každý řez. [AMF](/mobilnisite/slovnik/amf/), který zpracovává žádosti o registraci UE, komunikuje s NSACF, aby zjistil, zda lze UE připustit k požadovanému řezu.

NSACF funguje prostřednictvím sady rozhraní na bázi služeb, přičemž primárně vystavuje služby AMF. Když UE zahájí registrační proceduru obsahující informace pro asistovaný výběr síťového řezu ([NSSAI](/mobilnisite/slovnik/nssai/)), AMF vyvolá služební operaci na NSACF (např. službu Nnsacf_NSAC_Control), aby požádal o kontrolu přístupu. NSACF přijme tuto žádost, která obsahuje identifikátor řezu ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)), a ve své interní databázi nebo úložišti politik zkontroluje nakonfigurovaný maximální limit UE a aktuální počet registrací pro daný řez. Na základě této kontroly vrátí AMF rozhodnutí o řízení přístupu (povolit nebo odmítnout). Pokud je přístup povolen, NSACF zvýší své interní počítadlo. Naopak, když se UE odregistruje nebo je její registrační kontext uvolněn, AMF o tom NSACF notifikuje a ta pak odpovídající počítadlo sníží.

Architektonicky je NSACF stavová funkce, která musí zajišťovat konzistenci a spolehlivost dat. Může komunikovat s jednotným datovým úložištěm ([UDR](/mobilnisite/slovnik/udr/)) pro trvalé ukládání dat politik řízení přístupu k řezům a potenciálně i počtů registrací pro účely obnovy. Návrh NSACF také zohledňuje škálovatelnost a vysokou dostupnost, neboť se stává centrálním bodem pro řízení přístupu k řezům v celé síti. Její funkčnost je těsně integrována s celým systémem správy síťových řezů, včetně funkce pro výběr síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)) a funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), aby byl zajištěn ucelený rámec správy řezů a vynucování politik.

## K čemu slouží

NSACF byla vytvořena, aby poskytla vyhrazený, škálovatelný a centralizovaný bod pro vynucování politik řízení přístupu k síťovým řezům. Před jejím zavedením neexistovala standardizovaná funkce pro správu rozsahu síťových řezů z hlediska připojených zařízení. Spoléhat se na jednotlivé síťové funkce, jako je AMF, aby tyto limity vynucovaly lokálně, by bylo neefektivní, nekonzistentní a obtížně spravovatelné v rámci celé sítě. NSACF tento problém řeší centralizací logiky a stavu pro přístup k řezům, čímž zajišťuje jediný zdroj pravdy o počtech registrací na řez napříč všemi AMF v síti.

Tato centralizace je zásadní z několika důvodů. Za prvé zaručuje konzistentní vynucování politik bez ohledu na to, ke kterému AMF se UE připojí, což je klíčové v cloud-nativní, distribuované síti jádra. Za druhé zjednodušuje operátorům provoz a správu politik, protože mohou konfigurovat a aktualizovat limity kapacity řezů v jedné logické funkci. Za třetí umožňuje pokročilé funkce, jako jsou dynamické úpravy kapacity a integrace se síťovou analytikou. Vytvoření NSACF byla přímá reakce na požadavky operátorů na robustní komerční řezy, kde je zaručení, že řez nebude nadměrně obsazen, stejně důležité jako zaručení jeho výkonu, což z ní činí základní kámen pro obchodní modely typu slice-as-a-service.

## Klíčové vlastnosti

- Centralizované úložiště a vynucovač politik NSAC, včetně maximálních limitů UE na řez.
- Udržuje počítadla registrací a odregistrací UE v reálném čase pro každý řez.
- Poskytuje rozhodnutí o řízení přístupu (Povolit/Odmítnout) AMF prostřednictvím rozhraní na bázi služeb.
- Podporuje stavový provoz s možnou integrací s UDR pro trvalost dat.
- Umožňuje konzistentní vynucování limitů kapacity řezů v celé síti.
- Usnadňuje operátorům správu životního cyklu řezů a monitorování kapacity.

## Související pojmy

- [NSAC – Network Slice Admission Control](/mobilnisite/slovnik/nsac/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)
- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.203** (Rel-18) — Charging management
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.536** (Rel-19) — NSACF Service Based Interface Protocol
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.574** (Rel-19) — 5G Data Collection Coordination Services Stage 3
- **TS 29.575** (Rel-19) — 5G Analytics Data Repository Services Stage 3
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [NSACF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsacf/)
