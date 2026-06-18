---
slug: "nssf"
url: "/mobilnisite/slovnik/nssf/"
type: "slovnik"
title: "NSSF – Network Slice Selection Function"
date: 2026-01-01
abbr: "NSSF"
fullName: "Network Slice Selection Function"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nssf/"
summary: "NSSF je síťová funkce jádra 5G, která vybírá vhodnou instanci síťového řezu pro uživatelské zařízení (UE) na základě předplatného, požadované služby a stavu sítě. Je klíčová pro umožnění přizpůsobenýc"
---

NSSF je síťová funkce jádra 5G, která vybírá vhodnou instanci síťového řezu pro uživatele na základě předplatného, požadované služby a stavu sítě.

## Popis

Funkce pro výběr síťového řezu (NSSF) je kritická součást architektury jádra 5G (5GC), konkrétně části řídicí roviny. Jejím hlavním úkolem je pomáhat při výběru vhodné instance síťového řezu ([NSI](/mobilnisite/slovnik/nsi/)) pro uživatelské zařízení (UE) během procedur registrace a vytváření relace. NSSF funguje tak, že vyhodnocuje informace pro výběr řezu, které zahrnují požadované pomocné informace pro výběr předplaceného síťového řezu ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)) od UE, povolené [NSSAI](/mobilnisite/slovnik/nssai/) poskytované sítí a profil předplatného UE uložený ve funkci jednotné správy dat ([UDM](/mobilnisite/slovnik/udm/)). Na základě těchto informací, místních provozovatelských politik a dostupnosti instancí síťových řezů NSSF určuje konkrétní NSI, která bude obsluhovat relaci UE.

Architektonicky NSSF komunikuje s ostatními funkcemi jádra sítě prostřednictvím rozhraní založených na službách ([SBI](/mobilnisite/slovnik/sbi/)), primárně využívá službu Nnssf. Klíčové interakce zahrnují komunikaci s funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) během procedury registrace UE. Když AMF přijme registrační požadavek obsahující požadované NSSAI, může se dotázat NSSF, aby určilo povolené NSSAI pro UE a identifikovalo sadu síťových řezů a sad AMF (AMF Set) nebo konkrétní AMF, který může obsluhovat požadované řezy. Proces rozhodování NSSF bere v úvahu mapování mezi S-NSSAI a skutečně nasazenými NSI, které jsou složeny z řízených instancí podsítí síťových řezů ([NSSI](/mobilnisite/slovnik/nssi/)).

Funkcionalita NSSF je zásadní pro praktickou realizaci síťového řezování, což je základní koncept 5G. Zajišťuje, že je UE připojeno k síťovému řezu, který odpovídá jejím požadavkům na službu, ať už jde o vylepšenou mobilní širokopásmovou komunikaci (eMBB), ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) nebo hromadnou komunikaci mezi stroji (mMTC). Tímto výběrem NSSF umožňuje efektivní využití prostředků, izolaci mezi řezy a poskytování přizpůsobené kvality služby (QoS). Její operace jsou definovány ve specifikacích 3GPP, jako je TS 23.501 pro celkovou systémovou architekturu a TS 29.520 pro definici jejího rozhraní založeného na službách.

## K čemu slouží

NSSF byla zavedena s 5G ve verzi 3GPP Release 15, aby řešila základní výzvu efektivního mapování různorodých uživatelských požadavků na služby na logicky izolované síťové řezy. Před5G sítě nabízely převážně monolitickou architekturu, kde byly všechny služby poskytovány přes jedinou, jednotnou síťovou infrastrukturu. Tento přístup byl nedostačující pro podporu širokého spektra případů užití 5G, které mají radikálně odlišné technické požadavky – od gigabitových rychlostí pro streamování videa po milisekundovou latenci pro průmyslovou automatizaci a vysokou hustotu připojení pro senzory IoT.

Vytvoření NSSF bylo motivováno potřebou specializované, inteligentní funkce pro správu výběru řezu jako plnohodnotné procedury v jádru sítě. Bez ní by AMF nebo jiné funkce potřebovaly vestavěnou, komplexní logiku pro pochopení topologií nasazení řezů a nároků předplatitelů, což by vedlo k problémům se škálovatelností a správou. NSSF tuto inteligenci centralizuje a umožňuje dynamický výběr řezu řízený politikami, který se může přizpůsobit zatížení sítě, dostupnosti řezů a komerčním dohodám. Řeší problém, jak automaticky a přesně připojit zařízení ke správnému virtualizovanému síťovému segmentu z mnoha možných variant, což je předpoklad pro poskytování síťového řezování jako služby.

## Klíčové vlastnosti

- Vyhodnocuje data předplatného UE a požadované S-NSSAI, aby určila povolené NSSAI
- Vybírá vhodnou instanci síťového řezu (NSI) pro UE na základě provozovatelských politik
- Určuje příslušnou sadu AMF (AMF Set) nebo konkrétní AMF pro obsluhu vybraného síťového řezu
- Poskytuje mapování mezi S-NSSAI a nasazenými instancemi síťových řezů/podsítí
- Podporuje procedury autentizace a autorizace specifické pro síťový řez
- Komunikuje s AMF prostřednictvím rozhraní založeného na službách (Nnssf) během registrace a správy relace

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.524** (Rel-19) — 5G Cause Code Mapping Specification
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.574** (Rel-19) — 5G Data Collection Coordination Services Stage 3
- **TS 29.576** (Rel-19) — 5G Messaging Framework Adaptor Services Stage 3
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [NSSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssf/)
