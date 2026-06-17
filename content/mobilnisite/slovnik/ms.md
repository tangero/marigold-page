---
slug: "ms"
url: "/mobilnisite/slovnik/ms/"
type: "slovnik"
title: "MS – Mobile Station"
date: 2026-01-01
abbr: "MS"
fullName: "Mobile Station"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ms/"
summary: "Uživatelské zařízení (UE) v síti GSM/UMTS, skládající se z mobilního zařízení (ME) a modulu identifikace účastníka (SIM). Je to koncové zařízení, které účastník používá pro přístup k síťovým službám a"
---

MS (mobilní stanice) je uživatelské zařízení v síti GSM nebo UMTS, které se skládá z mobilního zařízení (Mobile Equipment) a SIM karty a představuje koncové zařízení používané účastníkem pro přístup k síťovým službám.

## Popis

Mobilní stanice (MS) je základním síťovým prvkem v systémech 2G (GSM) a 3G (UMTS) a představuje kompletní uživatelský terminál. Skládá se ze dvou samostatných subentit: mobilního zařízení ([ME](/mobilnisite/slovnik/me/)) a modulu identifikace účastníka (SIM). ME je fyzické hardwarové zařízení – telefon, modem nebo datová karta – které obsahuje rádiový transceiver, displej, procesor a další hardware potřebný pro komunikaci. SIM je výměnná čipová karta, která bezpečně ukládá identitu účastníka (International Mobile Subscriber Identity – [IMSI](/mobilnisite/slovnik/imsi/)), autentizační klíče a další data a aplikace specifické pro účastníka.

Z architektonického hlediska je MS koncovým bodem rádiového rozhraní (Um v GSM, Uu v UMTS). Obsahuje všechny potřebné protokolové zásobníky pro komunikaci, včetně fyzické vrstvy (vrstva 1), linkové vrstvy (vrstva 2 s protokoly jako RLC/[MAC](/mobilnisite/slovnik/mac/)) a síťové vrstvy (vrstva 3 s protokoly pro správu mobility, řízení hovorů a správu relací). MS je zodpovědná za kritické funkce, jako je výběr a převýběr buňky, připojení a registrace v síti, zahájení a správa hovorů a datových relací, řízení výkonu, hlášení měření a provádění předávání hovorů na příkaz sítě.

Její role se vyvinula z jednoduchého hlasového terminálu v GSM na sofistikované výpočetní zařízení podporující vysokorychlostní data, multimédia a přístup k internetu v UMTS a novějších systémech. Oddělení ME a SIM je klíčovým architektonickým rysem, který umožňuje osobní mobilitu (uživatel může přenést své předplatné na jiný hardware) a bezpečnou autentizaci. MS komunikuje s podsystémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/) v GSM) nebo s rádiovou přístupovou sítí (RAN v UMTS) a přes ně se připojuje k jádru sítě pro komutaci a poskytování služeb. V pozdějších vydáních 3GPP (LTE, 5G) termín uživatelské zařízení (UE) nahradil MS, ale základní koncept zůstává.

## K čemu slouží

Mobilní stanice byla definována jako koncový bod na straně uživatele v původní architektuře GSM za účelem vytvoření jasného, standardizovaného rozhraní mezi zařízením účastníka a síťovou infrastrukturou. Jejím účelem bylo umožnit hromadný trh a interoperabilní celulární telefonii specifikací funkcí a rozhraní terminálu. Rozdělení na [ME](/mobilnisite/slovnik/me/) a SIM bylo revolučním konceptem, který oddělil hardwarové zařízení od identity účastníka, podpořil konkurenční trh s handsety a zjednodušil logistiku operátorům.

Řešila problém uživatelské mobility a bezpečného přístupu k síti. MS prostřednictvím svých protokolů zvládá složitost provozu v celulární síti – hledání buněk, registraci polohy, bezpečnou autentizaci a udržování spojení při pohybu. Před takovou standardizací byly celulární systémy často proprietární. Specifikace MS zajistila, že jakékoli kompatibilní zařízení může pracovat na jakékoli kompatibilní síti, což byl základní kámen globálního úspěchu GSM. Architektura MS také poskytla platformu pro zavádění nových služeb (SMS, data) definováním rozšiřitelných protokolových zásobníků uvnitř terminálu.

## Klíčové vlastnosti

- Skládá se ze dvou oddělitelných entit: mobilního zařízení (hardware) a SIM (identita účastníka).
- Implementuje kompletní protokolový zásobník rádiového rozhraní (vrstva 1, 2 a 3).
- Provádí procedury výběru buňky, ukotvení a registrace.
- Provádí funkce správy mobility, jako je aktualizace polohy a předávání hovorů.
- Spravuje řízení hovorů (CC), správu relací (SM) a doplňkové služby.
- Poskytuje rozhraní mezi člověkem a strojem (MMI) pro koncového uživatele.

## Související pojmy

- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.146** (Rel-19) — MBMS Stage 1 Description
- **TS 22.246** (Rel-19) — MBMS User Services Specification
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- … a dalších 95 specifikací

---

📖 **Anglický originál a plná specifikace:** [MS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ms/)
