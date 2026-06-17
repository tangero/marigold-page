---
slug: "ha"
url: "/mobilnisite/slovnik/ha/"
type: "slovnik"
title: "HA – High-Accuracy GNSS"
date: 2025-01-01
abbr: "HA"
fullName: "High-Accuracy GNSS"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ha/"
summary: "High-Accuracy GNSS (HA) je služba 3GPP poskytující přesné určování polohy pomocí technik jako Real-Time Kinematic (RTK) a Precise Point Positioning (PPP). Dosahuje přesnosti na úrovni centimetrů, což"
---

HA je služba 3GPP poskytující přesné určování polohy pomocí technik jako RTK a PPP, která dosahuje přesnosti na úrovni centimetrů pro aplikace jako autonomní řízení a průmyslový IoT.

## Popis

High-Accuracy [GNSS](/mobilnisite/slovnik/gnss/) (HA) je standardizovaná služba v rámci 3GPP, která využívá pokročilá korekční data globálního navigačního satelitního systému (GNSS) k dosažení přesnosti určování polohy na úrovni centimetrů nebo decimetrů. Na rozdíl od konvenčního GNSS, který spoléhá na samostatné satelitní signály náchylné k chybám z atmosférických zpoždění, nepřesností satelitních hodin a odchylek oběžných drah, HA využívá korekční datové toky přenášené přes mobilní sítě. Tyto korekce kompenzují systematické chyby, což umožňuje přijímačům vypočítat vysoce přesné polohy. Služba je definována tak, aby podporovala více GNSS konstelací včetně [GPS](/mobilnisite/slovnik/gps/), Galileo, [GLONASS](/mobilnisite/slovnik/glonass/) a BeiDou, čímž zajišťuje globální interoperabilitu a robustnost prostřednictvím redundance signálu.

Architektura HA zahrnuje několik klíčových komponent: uživatelské zařízení (UE) se schopným GNSS přijímačem, mobilní síť pro přenos dat a externí nebo síťové poskytovatele korekčních služeb. Korekční data, generovaná sítěmi referenčních stanic monitorujících GNSS signály, jsou doručována do UE prostřednictvím point-to-point nebo broadcast mechanismů. Pro doručování se používají protokoly jako Secure User Plane Location (SUPL) nebo metody řídicí roviny, s formáty standardizovanými organizacemi jako Radio Technical Commission for Maritime Services (RTCM) nebo proprietární řešení. UE aplikuje tyto korekce v reálném čase pomocí algoritmů pro RTK nebo PPP, v závislosti na požadované přesnosti, latenci a dostupnosti infrastruktury.

HA funguje prostřednictvím dvou hlavních technik: Real-Time Kinematic (RTK) a Precise Point Positioning (PPP). RTK spoléhá na hustou síť referenčních stanic, které poskytují korekce založené na fázi, což umožňuje centimetrovou přesnost téměř okamžitě, ale vyžaduje blízkost infrastruktury. PPP využívá přesné korekce satelitních oběžných drah a hodin od globálních nebo regionálních služeb, dosahuje přesnosti od decimetrů po centimetry s delšími časy konvergence, ale širším pokrytím. Standardy 3GPP specifikují požadavky na službu, rozhraní a bezpečnostní mechanismy, aby zajistily spolehlivé a nízkolatenční doručování korekčních dat, a integrují HA do širšího rámce Location Services ([LCS](/mobilnisite/slovnik/lcs/)) pro aplikace jako nouzové služby, logistika a rozšířená realita.

## K čemu slouží

High-Accuracy [GNSS](/mobilnisite/slovnik/gnss/) byl zaveden, aby uspokojil rostoucí poptávku po přesném určování polohy v komerčních a průmyslových aplikacích, kde standardní GNSS (s přesností na úrovni metrů) nestačí. Před HA aplikace jako autonomní vozidla, precizní zemědělství a doručování pomocí dronů spoléhaly na proprietární nebo necílové korekční služby, což vedlo k fragmentaci, vysokým nákladům a omezené škálovatelnosti. Integrace HA do standardů 3GPP umožňuje všudypřítomné, síťově asistované vysoce přesné určování polohy, které využívá stávající mobilní infrastrukturu pro spolehlivé doručování dat.

Zavedení HA řeší omezení jako mnohocestné šíření signálu, ionosférická zpoždění a chyby satelitních hodin, která snižují přesnost GNSS. Standardizací doručování korekcí přes mobilní sítě 3GPP zajišťuje interoperabilitu napříč zařízeními a sítěmi, snižuje složitost nasazení a podporuje masové přijetí. To je zvláště kritické pro aplikace týkající se bezpečnosti života a nově vznikající technologie jako komunikace Vehicle-to-Everything (V2X), kde je přesná poloha klíčová pro zabránění kolizím a navigaci.

Historicky bylo vysoce přesné určování polohy omezeno na specializované sektory jako geodetické práce nebo vojenské využití. HA demokratizuje tuto schopnost tím, že ji vkládá do spotřebitelských a IoT zařízení, což je hnací silou trendů v chytrých městech, průmyslové automatizaci a službách založených na poloze. Řeší problémy s přesností, dostupností a integritou v náročných prostředích, jako jsou městské kaňony nebo vnitřní prostory, a zvyšuje tak celkovou užitečnost GNSS v ekosystémech 5G a dalších generací.

## Klíčové vlastnosti

- Podpora přesnosti určování polohy na úrovni centimetrů až decimetrů
- Integrace technik Real-Time Kinematic (RTK) a Precise Point Positioning (PPP)
- Doručování GNSS korekčních dat přes mobilní sítě prostřednictvím uživatelské nebo řídicí roviny
- Podpora více konstelací (GPS, Galileo, GLONASS, BeiDou) pro robustnost
- Standardizovaná rozhraní a protokoly pro interoperabilitu napříč zařízeními a sítěmi
- Nízkolatenční doručování korekcí pro umožnění aplikací v reálném čase, jako je autonomní řízení

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 23.261** (Rel-19) — IP Flow Mobility between 3GPP and WLAN
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.303** (Rel-19) — Dual-Stack MIPv6 Mobility Management
- **TS 24.304** (Rel-19) — MIPv4 FA Mode Mobility Management in EPC
- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.279** (Rel-19) — MIPv4 Mobility Protocol over S2a
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [HA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ha/)
