---
slug: "srnc"
url: "/mobilnisite/slovnik/srnc/"
type: "slovnik"
title: "SRNC – Serving Radio Network Controller"
date: 2025-01-01
abbr: "SRNC"
fullName: "Serving Radio Network Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srnc/"
summary: "SRNC je klíčový řídicí uzel v sítích UMTS (3G), který spravuje rádiové prostředky a spojení pro jedno nebo více uživatelských zařízení (UE). Zajišťuje funkce jako řízení přístupu, řízení výkonu, předá"
---

SRNC je klíčový řídicí uzel v síti UMTS (3G), který spravuje rádiové prostředky a spojení pro uživatelské zařízení a zajišťuje funkce jako řízení přístupu, řízení výkonu a předávání spojení.

## Popis

Serving Radio Network Controller (SRNC) je základní síťový prvek v architektuře UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), standardizované od 3GPP Release 99. Působí jako řídicí [RNC](/mobilnisite/slovnik/rnc/) pro konkrétní spojení s uživatelským zařízením (UE). Když si UE naváže spojení se sítí, je jednomu RNC přiřazena role SRNC. Tento SRNC je zodpovědný za kompletní ukončení protokolů vrstvy 2 (linkové vrstvy) a vrstvy 3 (síťové vrstvy) pro rádiové rozhraní (rozhraní Uu) směrem k danému UE. Spravuje s tím spojené rádiové přístupové přenosové cesty ([RAB](/mobilnisite/slovnik/rab/)) a provádí klíčové funkce správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)).

Z architektonického hlediska se SRNC připojuje k jádru sítě (CN) přes rozhraní Iu a k dalším RNC přes rozhraní Iur. Řídí jeden nebo více Node B (základnových stanic) prostřednictvím rozhraní Iub. SRNC obsahuje entitu protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), která komunikuje přímo s UE a zajišťuje navazování spojení, mobilní procedury a vysílání systémových informací. Obsahuje také entity Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), zodpovědné za přenos dat, segmentaci, opětovné sestavení a plánování přes rozhraní vzduchu.

Mezi klíčové provozní role SRNC patří řízení přístupu, kdy rozhoduje o přijetí nových rádiových spojení na základě dostupné kapacity a úrovně rušení; řízení výkonu pro udržení kvality rádiového spojení při minimalizaci rušení; a řízení předávání spojení, spravující jak měkká předání spojení (kdy UE komunikuje současně s více Node B), tak tvrdá předání spojení. SRNC také provádí šifrování a ochranu integrity pro data a signalizaci přenášené přes rádiové rozhraní. Ve scénářích, kdy se UE přesune pod kontrolu jiného RNC (Drift RNC nebo [DRNC](/mobilnisite/slovnik/drnc/)), si původní SRNC ponechává kontrolu nad spojením a rozhraním Iu k jádru sítě, přičemž uživatelská data mohou být směrována přes rozhraní Iur.

## K čemu slouží

SRNC byl zaveden s UMTS (3G), aby poskytl centralizovaný, inteligentní řídicí bod pro rádiovou přístupovou síť, což představuje významný vývoj oproti jednoduššímu Base Station Controller (BSC) v sítích GSM/GPRS. Byl vytvořen pro správu nového rozhraní vzduchu Wideband Code Division Multiple Access (W-CDMA), které přineslo složité výzvy v řízení prostředků, jako je měkké předání spojení a rychlé řízení výkonu. Architektura SRNC oddělila řídicí rovinu (zajišťovanou SRNC) od přeposílání uživatelské roviny (kterou mohl zajišťovat Drift RNC), což umožnilo flexibilnější a efektivnější síťové topologie a správu mobility.

Toto oddělení řešilo omezení staršího GSM BSC, který byl těsněji svázán se svými základnovými stanicemi a méně schopen zvládat sofistikované požadavky na makrodiverzitu a QoS služeb 3G. Model SRNC umožnil zavedení rozhraní Iur mezi RNC, což umožnilo bezproblémové měkké předání spojení mezi RNC a robustní mobilitu bez nutnosti předání spojení na rozhraní jádra sítě při každé změně RNC. To bylo zásadní pro podporu služeb v reálném čase, jako je hlas a video přes IP, se souvislou kvalitou.

Dále role SRNC v šifrování a ochraně integrity centralizovala bezpečnostní funkce na důvěryhodném síťovém uzlu a poskytla robustní koncový bod zabezpečení pro rádiové spojení. Jeho návrh byl klíčový pro umožnění paketově orientované domény a smíšených toků provozu, které definovaly multimediální služby 3G, a položil základy pro čistě IP architektury následujících generací.

## Klíčové vlastnosti

- Ukončuje protokoly RRC, RLC a MAC pro rádiové rozhraní Uu
- Provádí správu rádiových prostředků (RRM) včetně řízení přístupu, plánování paketů a řízení výkonu
- Řídí procedury měkkého a tvrdého předání spojení, včetně správy aktivní sady
- Slouží jako bezpečnostní kotva pro rádiové rozhraní a provádí šifrování a ochranu integrity
- Spravuje spojení Iu k jádru sítě (Core Network) pro svá řízená UE
- Může řídit spojení uživatelské roviny přes rozhraní Iur, když UE využívá Drift RNC (DRNC)

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [DRNC – Drift Radio Network Controller](/mobilnisite/slovnik/drnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [SRNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/srnc/)
