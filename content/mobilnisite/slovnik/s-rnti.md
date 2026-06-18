---
slug: "s-rnti"
url: "/mobilnisite/slovnik/s-rnti/"
type: "slovnik"
title: "S-RNTI – Serving Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "S-RNTI"
fullName: "Serving Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-rnti/"
summary: "Dočasný identifikátor přiřazený RNC stanici UE v UTRAN na dobu trvání spojení. Jednoznačně identifikuje stanici UE v kontextu obsluhující RNC, což umožňuje efektivní řízení rádiových prostředků a sign"
---

S-RNTI je dočasný identifikátor přiřazený RNC stanici UE v UTRAN, který jednoznačně identifikuje stanici UE v kontextu obsluhující RNC za účelem efektivního řízení rádiových prostředků a signalizace.

## Popis

Serving Radio Network Temporary Identifier (S-RNTI) je základní identifikátor používaný v architektuře UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně spravovaný Radio Network Controllerem ([RNC](/mobilnisite/slovnik/rnc/)). Je přiřazen User Equipment (UE) obsluhující RNC ([SRNC](/mobilnisite/slovnik/srnc/)) při navázání Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) spojení a zůstává platný po dobu jeho trvání. S-RNTI slouží jako jedinečný lokální identifikátor pro stanici UE v kontextu její SRNC, čímž ji odlišuje od všech ostatních UE aktuálně připojených ke stejné RNC. Tento identifikátor je hojně používán v signalizačních zprávách mezi RNC a stanicí UE, stejně jako v komunikaci mezi uzly RNC (např. mezi SRNC a Drift RNC). Jeho primární role je poskytnout stručnou a efektivní referenci pro síť, aby odkazovala na kontext spojení konkrétní stanice UE, který zahrnuje informace o rádiových přenosových kanálech, stavu mobility a přidělených prostředcích.

Z procedurálního hlediska je S-RNTI přidělen během procedury RRC Connection Setup. RNC vygeneruje S-RNTI a zahrne jej do zprávy RRC CONNECTION SETUP odeslané stanici UE. Následně stanice UE používá toto S-RNTI v hlavičce svých RRC zpráv při komunikaci se SRNC. Na straně sítě používá SRNC S-RNTI k indexování své interní databáze kontextů UE. Tento kontext obsahuje všechny potřebné informace pro správu relace stanice UE, včetně bezpečnostních klíčů, informací o schopnostech, aktivních rádiových přenosových kanálech a aktuální buňce/[URA](/mobilnisite/slovnik/ura/). Identifikátor je také zásadní během událostí mobility, jako je přemístění Serving Radio Network Subsystem ([SRNS](/mobilnisite/slovnik/srns/)), kde je kontext S-RNTI přenesen ze zdrojové SRNC na cílovou SRNC.

S-RNTI funguje spolu s dalšími identifikátory, jako je [U-RNTI](/mobilnisite/slovnik/u-rnti/) (který zahrnuje S-RNTI a RNC ID) a [C-RNTI](/mobilnisite/slovnik/c-rnti/) používaný na úrovni buňky. Zatímco C-RNTI identifikuje stanici UE v rámci jedné buňky, S-RNTI má širší rozsah a identifikuje stanici UE v celé doméně SRNC. Tento hierarchický identifikační systém je klíčový pro fungování UTRAN, umožňuje efektivní volání, provádění předávání spojení a přenos dat. S-RNTI je přenášen v Radio Network Layer (RNL) protokolů, jako je Radio Access Network Application Part (RANAP) pro komunikaci s Core Network a Radio Network Subsystem Application Part (RNSAP) pro komunikaci mezi RNC. Jeho návrh je nedílnou součástí oddělení řídicí a uživatelské roviny v UTRAN, zajišťuje, že řídicí signalizace může být přesně směrována a asociována se správnými datovými toky uživatele.

## K čemu slouží

S-RNTI byl vytvořen, aby řešil potřebu robustní a efektivní metody identifikace spojení mobilního uživatele v rádiové přístupové síti, konkrétně pro systém UMTS zavedený ve 3GPP Release 99. Předchozí buněčné systémy jako GSM používaly odlišné identifikační mechanismy, ale složitější, spojově orientovaná povaha UMTS a jeho rozdělená architektura RNC/Node B vyžadovala vyhrazený dočasný identifikátor spravovaný na úrovni RNC. Primární problém, který řeší, je jednoznačná identifikace kontextu stanice UE v rámci obsluhující RNC, která je zodpovědná za řízení rádiového spojení stanice UE. Bez takového identifikátoru by RNC zápasila se správou více současných spojení, správným směrováním signalizačních zpráv a udržováním stavových informací během mobility.

Motivace vychází z požadavků paketově přepínaných služeb a pokročilého řízení mobility v 3G. Síť potřebovala způsob, jak rychle odkazovat na všechny parametry spojené s relací stanice UE, aniž by neustále používala trvalé identifikátory jako IMSI, což by bylo neefektivní a představovalo bezpečnostní riziko. S-RNTI poskytuje tuto referenci na úrovni relace. Také umožňuje efektivní komunikaci mezi RNC (např. během soft handoveru s Drift RNC), protože S-RNTI v kombinaci s RNC ID tvoří globálně jedinečný U-RNTI v rámci UTRAN. Tento návrh podporuje základní princip UMTS mít obsluhující kontrolér (SRNC), který si udržuje kontrolu nad spojením, i když se uživatel pohybuje buňkami řízenými jinými RNC.

Dále je S-RNTI nezbytný pro správu stavu spojení. Umožňuje RNC korelovat příchozí zprávy od stanice UE nebo od jiných síťových uzlů s konkrétním aktivním kontextem RRC spojení. To je kritické pro procedury jako zřízení/rekonfigurace rádiového přenosového kanálu, předání spojení a volání ve stavech CELL_PCH nebo URA_PCH. Tím, že poskytuje stabilní referenci po dobu trvání spojení, zjednodušuje interní logiku sítě a zlepšuje spolehlivost stavově závislých operací, čímž tvoří základní kámen architektury řídicí roviny UTRAN.

## Klíčové vlastnosti

- Jednoznačně identifikuje kontext spojení stanice UE v rámci jedné obsluhující RNC (SRNC).
- Přiřazen SRNC během procedury RRC Connection Setup.
- Používán jako klíčové pole v RRC signalizačních zprávách mezi stanicí UE a SRNC.
- Zásadní pro indexování a načítání kontextu UE v interních databázích RNC.
- Jádrová součást U-RNTI (UTRAN Radio Network Temporary Identifier), zajišťující jedinečnost napříč UTRAN.
- Usnadňuje signalizaci mezi RNC a procedury jako SRNS Relocation, když je přenášen v RNSAP zprávách.

## Související pojmy

- [U-RNTI – UTRAN Radio Network Temporary Identifier](/mobilnisite/slovnik/u-rnti/)
- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [SRNC – Serving Radio Network Controller](/mobilnisite/slovnik/srnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [S-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-rnti/)
