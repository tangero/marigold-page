---
slug: "msas"
url: "/mobilnisite/slovnik/msas/"
type: "slovnik"
title: "MSAS – Multi-functional Satellite Augmentation System"
date: 2025-01-01
abbr: "MSAS"
fullName: "Multi-functional Satellite Augmentation System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/msas/"
summary: "Satelitní systém, který zvyšuje přesnost, integritu a dostupnost globálních navigačních satelitních systémů (GNSS), jako je GPS, pro uživatelská zařízení 3GPP. Poskytuje korekční data a monitorování i"
---

MSAS je satelitní augmentační systém, který zvyšuje přesnost, integritu a dostupnost signálů GNSS, jako je GPS, pro uživatelská zařízení 3GPP tím, že poskytuje korekční data a monitorování integrity.

## Popis

Multi-functional Satellite Augmentation System (MSAS) je satelitní augmentační systém ([SBAS](/mobilnisite/slovnik/sbas/)) standardizovaný v rámci 3GPP za účelem zlepšení výkonu globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) pro uživatelská zařízení (UE) v celulárních sítích. Provozně se MSAS vztahuje k systémům jako je augmentace založená na japonském systému [QZSS](/mobilnisite/slovnik/qzss/) nebo podobným regionálním SBAS (např. [WAAS](/mobilnisite/slovnik/waas/), [EGNOS](/mobilnisite/slovnik/egnos/)). Vysílá korekční data (pro satelitní dráhu, hodiny a ionosférická zpoždění) a informace o integritě prostřednictvím geostacionárních satelitů na frekvenci [L1](/mobilnisite/slovnik/l1/) (1575,42 MHz). Tato data přijímají přímo UE s podporou GNSS nebo mohou být doručena k UE prostřednictvím sítě 3GPP jako součást protokolů asistovaného GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), což výrazně zvyšuje přesnost a spolehlivost určování polohy.

Architektonicky je MSAS integrován do architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) 3GPP. Klíčové síťové prvky zahrnují SUPL Enabled Terminal (SET), což je UE, a SUPL Location Platform (SLP). Pro řešení v řídicí rovině komunikuje s UE Serving Mobile Location Center (SMLC) nebo Evolved SMLC (E-SMLC) v LTE/NR. Augmentační data MSAS mohou být těmto síťovým prvkům poskytována z referenčních sítí nebo přímo od poskytovatelů služeb SBAS. GNSS přijímač v UE používá korekce MSAS k výpočtu přesnější polohy, čímž snižuje chyby způsobené atmosférickými vlivy a nepřesnostmi efemerid satelitů na úroveň pod metr v podmínkách přímé viditelnosti satelitů.

Fungování spočívá v tom, že UE přijímá signály GNSS (např. GPS) a současně dekóduje augmentační signály MSAS z geostacionárních satelitů. Korekční parametry jsou aplikovány v algoritmu výpočtu polohy. V režimech A-GNSS může síť poskytovat UE korekční nebo integritní data MSAS přes LTE nebo NR rádiové přenosy pomocí protokolů jako Radio Resource Control (RRC) nebo LTE Positioning Protocol (LPP). To pomáhá UE se slabým přímým příjmem satelitních signálů. MSAS také poskytuje příznaky integrity, které varují UE, pokud je signál konkrétního satelitu GNSS nespolehlivý, což je zásadní pro aplikace týkající se bezpečnosti života. Jeho úlohou je umožnit služby určování polohy s vysokou přesností a vysokou integritou, které jsou vyžadovány pro nouzové volání (E911/E112), navigaci a vznikající služby jako V2X, jež závisí na důvěryhodných polohových údajích.

## K čemu slouží

MSAS byl začleněn do standardů 3GPP, aby řešil inherentní omezení samostatného GNSS v mobilním prostředí, zejména pro nouzové služby a komerční aplikace založené na poloze. Samostatný GPS/GNSS může mít přesnost sníženou na více než 10 metrů kvůli ionosférickým zpožděním, chybám satelitních hodin a nepřesnostem efemerid a postrádá certifikovaný mechanismus monitorování integrity. Pro lokalizaci nouzových volání (např. E112 v Evropě) regulační požadavky vyžadují lepší přesnost a spolehlivost, kterou augmentační systémy jako MSAS poskytují.

Historická motivace vychází z bezpečnostních systémů v letectví, kde byly vyvíjeny SBAS jako WAAS a MSAS pro umožnění přesných přiblížení. 3GPP rozpoznalo hodnotu této stávající infrastruktury pro pozemní mobilní uživatele. Integrací podpory MSAS standardy umožnily mobilním sítím splnit přísnější požadavky na určování polohy bez výhradní závislosti na síťových metodách, jako je Observed Time Difference of Arrival (OTDOA), které mají omezení v nasazení. Vyřešil problém poskytování všudypřítomného určování polohy s vysokou integritou jak v městských kaňonech (prostřednictvím asistenčních dat), tak v otevřených oblastech, čímž vylepšil služby jako navigace s pokyny, geofencing a účtování založené na poloze.

Podpora MSAS navíc připravila systémy 3GPP na budoucí aplikace v IoT a autonomních systémech, kde je přesné a spolehlivé určování polohy nezbytné. Představuje konvergenci technologií satelitní navigace a celulární komunikace, která umožňuje operátorům nabízet vylepšené lokalizační služby využitím veřejně dostupných augmentačních signálů, čímž se snižuje závislost na proprietárních asistenčních datech a zlepšuje se interoperabilita napříč globálními regiony s různými poskytovateli SBAS.

## Klíčové vlastnosti

- Vysílá diferenciální korekční data prostřednictvím geostacionárních satelitů za účelem zlepšení přesnosti GNSS
- Poskytuje monitorování integrity a alarmy pro spolehlivost signálů GNSS
- Podporuje jak samostatný příjem UE, tak síťově asistované doručení (A-GNSS)
- Umožňuje přesnost určování polohy na úrovni pod metr za příznivých podmínek
- Funguje na standardní GNSS frekvenci L1 (1575,42 MHz) pro přímou kompatibilitu
- Integruje se s architekturou LCS 3GPP prostřednictvím protokolů řídicí roviny (LPP) a uživatelské roviny (SUPL)

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [MSAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/msas/)
