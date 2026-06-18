---
slug: "sds"
url: "/mobilnisite/slovnik/sds/"
type: "slovnik"
title: "SDS – Short Data Services"
date: 2026-01-01
abbr: "SDS"
fullName: "Short Data Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sds/"
summary: "SDS umožňuje efektivní přenos malých, nepravidelných datových paketů, jako jsou údaje ze senzorů nebo stavové aktualizace, pro zařízení IoT a MTC. Optimalizuje signalizaci sítě a spotřebu energie, což"
---

SDS je služba, která umožňuje efektivní přenos malých, nepravidelných datových paketů pro zařízení IoT, optimalizuje signalizaci sítě a spotřebu energie pro dlouhou životnost baterie.

## Popis

Short Data Services (SDS) je schopnost služby podle 3GPP navržená pro efektivní přenos malých, sporadických datových zátěží, typicky spojených s aplikacemi Internetu věcí (IoT) a komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)). Poskytuje mechanismy pro odesílání a přijímání datových paketů, které jsou malé (často několik desítek až stovek bajtů) a přenášené nepravidelně. Architektura podporuje SDS jak přes řídicí rovinu, tak přes uživatelskou rovinu, se silným důrazem na minimalizaci signalizační režie a spotřeby energie zařízení.

Jak SDS funguje, zahrnuje optimalizované procedury pro přenos dat. V řešeních řídicí roviny mohou být malé datové pakety přenášeny prostřednictvím signalizačních zpráv Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), což umožňuje přenos dat bez nutnosti zřídit plnohodnotný datový rádiový bearer, což snižuje signalizační latenci a režii. Pro uživatelskou rovinu řešení jako early data transmission ([EDT](/mobilnisite/slovnik/edt/)) v LTE-M a NB-IoT umožňují odeslání dat během procedury náhodného přístupu. Mezi klíčové síťové komponenty patří [MTC-IWF](/mobilnisite/slovnik/mtc-iwf/) (pro SDS v řídicí rovině) a funkce jádra sítě ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)), které zajišťují směrování a politiky pro tyto malé datové pakety. Služba je úzce integrována s funkcemi jako Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)) a extended Discontinuous Reception (eDRX) pro maximalizaci životnosti baterie zařízení.

Její role spočívá v tom, že slouží jako základní přenosový prostředek pro širokou škálu případů užití IoT, jako jsou chytré měřiče, sledovače majetku a environmentální senzory. Tím, že poskytuje nativní, optimalizovanou síťovou cestu pro malá data, SDS zabraňuje přetížení sítě nadměrnou signalizací, která by nastala, pokud by tato zařízení používala standardní procedury datové relace navržené pro smartphony. Umožňuje síti efektivně podporovat obrovský počet zařízení, čímž činí rozsáhlá nasazení IoT ekonomicky a technicky proveditelnými.

## K čemu slouží

SDS bylo vytvořeno, aby vyřešilo zásadní nesoulad mezi tradičními protokoly pro mobilní širokopásmový přístup a požadavky zařízení IoT/MTC. Standardní procedury přenosu dat v celulárních sítích zahrnují významnou signalizaci (např. service request, zřizování beareru) v poměru k malým datovým zátěžím IoT, což vede k neefektivnímu využití síťových zdrojů a vysoké spotřebě energie zařízení. To činilo tradiční celulární technologii nepraktickou pro senzory napájené bateriemi, které potřebují životnost v řádu desetiletí.

Primární problém, který SDS řeší, je umožnění efektivní, síťově šetrné komunikace pro zařízení, která odesílají malá, nárazová data. Motivací byl explozivní růst trhu IoT a potřeba připojit miliardy nízkonákladových a nízkoenergetických zařízení k celulárním sítím. Historický kontext zahrnuje jeho zavedení spolu s dalšími funkcemi Cellular IoT (CIoT), jako jsou NB-IoT a LTE-M, ve specifikacích 3GPP Release 13 a 14, které společně měly za cíl připravit sítě LTE pro IoT.

Řeší omezení použití SMS nebo plných IP datových relací pro provoz IoT. SMS mohou být nákladné a postrádají záruky doručení s potvrzením vhodné pro některé aplikace, zatímco plné IP relace jsou příliš zatížené signalizací. SDS poskytuje standardizovanou, optimalizovanou a nákladově efektivní střední cestu, která umožňuje operátorům nabízet šité na míru služby konektivity IoT. Jeho vývoj je hnán potřebou podporovat složitější scénáře IoT, integrovat se s 5G Core a dále zvyšovat efektivitu pro hromadnou komunikaci typu stroj-stroj (mMTC).

## Klíčové vlastnosti

- Optimalizováno pro malé, nepravidelné datové pakety (typicky <1000 bajtů)
- Podporuje přenos dat jak přes řídicí rovinu (NAS), tak přes uživatelskou rovinu
- Minimalizuje signalizační režii ve srovnání s běžným zřizováním datové relace
- Umožňuje efektivní provoz s Power Saving Mode (PSM) a eDRX
- Integruje se s technologiemi Cellular IoT, jako jsou NB-IoT a LTE-M
- Poskytuje spolehlivé mechanismy doručení vhodné pro kritická data IoT

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 22.282** (Rel-19) — Mission Critical Data Service Requirements
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 23.784** (Rel-16) — Discreet Listening for Mission Critical Services
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [SDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sds/)
