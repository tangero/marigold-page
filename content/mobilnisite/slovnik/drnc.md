---
slug: "drnc"
url: "/mobilnisite/slovnik/drnc/"
type: "slovnik"
title: "DRNC – Drift Radio Network Controller"
date: 2025-01-01
abbr: "DRNC"
fullName: "Drift Radio Network Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/drnc/"
summary: "Řídicí jednotka rádiové sítě (RNC), která řídí skupinu Node B, ale není obsluhující RNC (SRNC) pro konkrétní UE. Při měkkém předání působí jako přenosový bod pro uživatelská data a řídicí signalizaci"
---

DRNC (Drift Radio Network Controller, doslova „řídicí jednotka driftové rádiové sítě“) je řídicí jednotka rádiové sítě (RNC), která během měkkého předání v UMTS zprostředkovává uživatelská data a řídicí signalizaci mezi obsluhující RNC (SRNC) a uživatelským zařízením (UE), přičemž řídí Node B, které UE používá, ale není jeho SRNC.

## Popis

Drift Radio Network Controller (DRNC) je základním konceptem v architektuře UMTS Radio Access Network (UTRAN), konkrétně v rámci řídicí roviny pro správu mobility. Jedná se o RNC, která aktuálně řídí buňky (prostřednictvím Node B), které uživatelské zařízení (UE) používá, ale není to RNC, která drží spojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) pro dané UE. RNC, která toto RRC spojení drží, se označuje jako Serving RNC (SRNC). Hlavní role DRNC vystupuje do popředí při mezibuněčném měkkém předání mezi různými RNC, kdy je UE současně připojeno k buňkám patřícím pod různá RNC. V tomto scénáři zůstává SRNC jediným řídicím bodem pro RRC spojení UE, ale DRNC spravuje rádiové prostředky svých vlastních buněk a funguje jako směrovací agent.

Architektonicky se DRNC nachází mezi SRNC a Node B pod její kontrolou. Rozhraní Iur propojuje SRNC a DRNC. Uživatelská data a řídicí signalizace pro UE jsou přenášena přes toto rozhraní Iur. DRNC neprovádí šifrování ani ochranu integrity pro UE; tyto funkce zůstávají u SRNC. Místo toho je DRNC zodpovědná za alokaci a správu rádiových prostředků (jako jsou kanalizační kódy a kódy pro rozprostřené spektrum) ve svých vlastních buňkách a provádí příkazy přijaté od SRNC prostřednictvím protokolu Radio Network Subsystem Application Part (RNSAP) přes Iur.

Z pohledu toku dat v downlinku posílá SRNC uživatelská data k DRNC přes rozhraní Iur. DRNC pak tato data přeposílá příslušným Node B pod její kontrolou přes rozhraní Iub. V uplinku je proces obrácený: DRNC přijímá data od svých Node B, v případě měkčího předání uvnitř buněk DRNC je kombinuje, a pak je přeposílá SRNC. Tato přeposílací funkce je pro UE transparentní. Role DRNC je klíčová pro zajištění plynulé mobility a udržení kvality hovoru během předání mezi RNC bez nutnosti přenosu role SRNC, což je složitější procedura známá jako SRNC relocation.

## K čemu slouží

Koncept DRNC byl zaveden ve 3GPP Release 99, aby vyřešil základní problém plynulé mobility a správy rádiových prostředků v distribuované UMTS síti s více RNC. Před UMTS používaly sítě GSM řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), které typicky spravovaly souvislá geografická území, a předání mezi BSC byla tvrdá předání s charakteristikou „přeruš a pak připoj“. UMTS se svým WCDMA rozhraním umožnilo měkké předání, při kterém může být UE současně připojeno k více buňkám pro zisk makrodiverzity. Tato schopnost potřebovala přesahovat administrativní hranice řízené různými RNC.

Mechanismus DRNC umožňuje síti využít výhod měkkého předání (lepší pokrytí, snížené přerušení hovoru, nižší potřebný vysílací výkon) i tehdy, když se UE přesune do oblasti řízené jinou RNC než je jeho SRNC. Bez role DRNC a standardizovaného rozhraní Iur by takové měkké předání mezi RNC bylo nemožné, což by vynutilo buď tvrdé předání (zhoršení výkonu), nebo okamžité a potenciálně zbytečné přemístění SRNC (zvýšení signalizační zátěže a složitosti). DRNC tedy umožňuje flexibilnější a efektivnější síťovou architekturu, kde může být SRNC ukotvena, zatímco rádiové spojení UE využívá nejlepší dostupné prostředky z více domén RNC, čímž optimalizuje jak výkon mobility, tak využití síťových prostředků.

## Klíčové vlastnosti

- Umožňuje měkké předání mezi RNC pro plynulou mobilitu UE
- Funguje jako směrovací a přeposílací uzel pro uživatelská data mezi SRNC a Node B pod její kontrolou
- Spravuje alokaci a řízení rádiových prostředků (kódy, výkon) pro své vlastní buňky
- Využívá rozhraní Iur pro komunikaci s obsluhující RNC (SRNC)
- Provádí příkazy pro rádiové prostředky od SRNC prostřednictvím protokolu RNSAP
- Podporuje kombinování pro makrodiverzitu pro uplink signály ze svých řízených buněk

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [DRNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/drnc/)
