---
slug: "egnos"
url: "/mobilnisite/slovnik/egnos/"
type: "slovnik"
title: "EGNOS – European Geostationary Navigation Overlay Service"
date: 2025-01-01
abbr: "EGNOS"
fullName: "European Geostationary Navigation Overlay Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/egnos/"
summary: "Satelitní doplňkový systém (SBAS), který zlepšuje přesnost, integritu a dostupnost signálů GPS nad Evropou. Poskytuje korigovaná polohová data pro aplikace kritické z hlediska bezpečnosti, jako je let"
---

EGNOS je evropský satelitní doplňkový systém, který zlepšuje přesnost, integritu a dostupnost signálů GPS pro aplikace kritické z hlediska bezpečnosti.

## Popis

European Geostationary Navigation Overlay Service (EGNOS) je satelitní doplňkový systém ([SBAS](/mobilnisite/slovnik/sbas/)) vyvinutý Evropskou kosmickou agenturou, Evropskou komisí a Eurocontrolem. Ačkoli nejde o technologii vytvořenou 3GPP, jeho podpora a integrace jsou specifikovány ve standardech 3GPP za účelem umožnění služeb založených na poloze v mobilních sítích. EGNOS zlepšuje výkon základních globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)), jako je [GPS](/mobilnisite/slovnik/gps/), tím, že poskytuje korekční data a informace o integritě.

Architektonicky se EGNOS skládá ze sítě přesně zaměřených pozemních referenčních stanic (RIMS - Ranging and Integrity Monitoring Stations) rozmístěných po celé Evropě. Tyto stanice nepřetržitě monitorují signály ze satelitů GPS. Shromážděná data jsou odesílána do hlavních řídicích center (MCCs), kde se vypočítávají chyby (jako jsou ty způsobené ionosférickým zpožděním, driftem satelitních hodin a nepřesnostmi efemerid). Tyto vypočtené korekční a integritní zprávy jsou následně nahrány na geostacionární satelity ([GEO](/mobilnisite/slovnik/geo/) satelity), které je vysílají přes oblast pokrytí služby EGNOS.

Uživatelské zařízení (UE) s přijímačem GNSS podporujícím EGNOS přijímá jak standardní signály GPS, tak doplňkové signály EGNOS z GEO satelitů. Přijímač aplikuje korekční data na surová měření GPS, čímž výrazně zlepšuje polohovou přesnost z přibližně 10 metrů (samostatný GPS) na lepší než 1-2 metry horizontálně. Klíčové je, že EGNOS také poskytuje informace o integritě, které uživatele během sekund upozorní, pokud je signál GPS nespolehlivý nebo obsahuje chyby přesahující bezpečnostní limity pro aplikace jako je letecká navigace. V kontextu 3GPP mohou tato vylepšená polohová data být použita UE nebo poskytnuta síti prostřednictvím řídicí nebo uživatelské roviny polohových protokolů (např. [LPP](/mobilnisite/slovnik/lpp/), [SUPL](/mobilnisite/slovnik/supl/)) pro podporu pokročilých služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)).

## K čemu slouží

EGNOS byl vytvořen, aby řešil omezení samostatného [GPS](/mobilnisite/slovnik/gps/) pro aplikace kritické z hlediska bezpečnosti života a další komerční aplikace vyžadující vysokou přesnost v Evropě. Zatímco GPS poskytuje globální pokrytí, jeho signály jsou náchylné k chybám, které snižují přesnost, a co je důležitější, postrádají garantovaný systém monitorování integrity. To jej činilo nevhodným pro kritické fáze letu v letectví nebo pro jiné aplikace, kde je prvořadá odpovědnost a bezpečnost.

Účelem integrace podpory EGNOS do standardů 3GPP (počínaje Release 8) bylo využít tuto vysoce kvalitní, certifikovanou polohovou službu pro mobilní aplikace. Umožňuje síťovým operátorům a poskytovatelům služeb nabízet přesnější a spolehlivější polohové služby. To řeší problémy, jako je poskytování vylepšené lokalizace volajícího při nouzovém volání (E112) s lepší přesností, umožňuje systémy mýtného, precizní zemědělství a podporuje rostoucí potřeby inteligentních dopravních systémů a aplikací IoT, které závisí na důvěryhodných polohových datech.

Specifikací toho, jak mohou UE a sítě využívat data EGNOS, umožnilo 3GPP mobilnímu ekosystému těžit z veřejně financované infrastruktury, která poskytuje otevřené, bezplatné a certifikované doplňkové signály, což přesahuje omezení základního určování polohy pomocí cell-ID nebo samostatného GPS dostupného v dřívějších releasech.

## Klíčové vlastnosti

- Vysílá diferenciální korekční data pro zlepšení přesnosti GPS na úroveň 1-2 metrů
- Poskytuje monitoring integrity a upozornění na nespolehlivost signálu během sekund
- Používá síť pozemních stanic a geostacionárních satelitů pro pokrytí Evropy
- Poskytuje signály otevřené služby bez poplatků pro komerční a bezpečnostní aplikace
- Podporován v 3GPP pro řešení polohování v řídicí a uživatelské rovině
- Umožňuje aplikace kritické z hlediska bezpečnosti v letectví, námořní a silniční dopravě

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [LBS – Location Based Services](/mobilnisite/slovnik/lbs/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [EGNOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/egnos/)
