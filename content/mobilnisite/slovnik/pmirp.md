---
slug: "pmirp"
url: "/mobilnisite/slovnik/pmirp/"
type: "slovnik"
title: "PMIRP – Performance Management Integration Reference Point"
date: 2025-01-01
abbr: "PMIRP"
fullName: "Performance Management Integration Reference Point"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pmirp/"
summary: "Performance Management Integration Reference Point (PMIRP) je standardizované rozhraní v rámci architektury správy sítě 3GPP. Definuje výměnu informací mezi síťovým prvkem (NE) nebo doménovým manažere"
---

PMIRP je standardizované rozhraní 3GPP pro výměnu dat správy výkonnosti a řídicích informací mezi síťovým prvkem nebo doménovým manažerem a manažerem referenčního bodu integrace.

## Popis

Performance Management Integration Reference Point (PMIRP) je klíčovou součástí architektury Telekomunikační manažerské sítě ([TMN](/mobilnisite/slovnik/tmn/)) a správy sítě ([NM](/mobilnisite/slovnik/nm/)) organizace 3GPP, definovanou v řadě specifikací 32.4xx. Standardizuje rozhraní a informační model pro výměnu dat správy výkonnosti ([PM](/mobilnisite/slovnik/pm/)) mezi spravovaným systémem (agentem) a řídicím systémem (manažerem). Spravovaným systémem může být síťový prvek ([NE](/mobilnisite/slovnik/ne/)), manažer prvků ([EM](/mobilnisite/slovnik/em/)) nebo doménový manažer ([DM](/mobilnisite/slovnik/dm/)). Řídicím systémem je typicky manažer referenčního bodu integrace ([IRP](/mobilnisite/slovnik/irp/) Manager), který může být součástí síťového manažera (NM) nebo systému vyšší úrovně pro podporu provozu ([OSS](/mobilnisite/slovnik/oss/)). PMIRP definuje sadu řešitelských množin (SS), z nichž každá obsahuje řadu tříd informačních objektů (IOC) a tříd notifikačních objektů (NOC), které modelují data o výkonnosti. Klíčové IOC zahrnují úlohy měření výkonnosti (PM-Jobs), což jsou naplánované úkony definující, co se má měřit (např. čítač nebo ukazatel), na kterých prostředcích a s jakou granularitou (např. 15minutovou, 24hodinovou). Výsledky těchto úloh jsou uloženy jako výsledky měření výkonnosti (PM-Results), které obsahují nasbírané hodnoty čítačů nebo odečty ukazatelů. Rozhraní PMIRP umožňuje IRP Managerovi vytvářet, pozastavovat, obnovovat, upravovat a mazat PM-Jobs ve spravovaném systému. Poskytuje také operace pro získání PM-Results a pro přihlášení k odběru notifikací o událostech, jako jsou změny stavu úlohy nebo překročení prahových hodnot. Komunikace je typicky založena na CORBA (Common Object Request Broker Architecture) nebo později na webových službách (SOAP/XML), jak je specifikováno v protokolu-neutrálním informačním modelu a jeho vazbách na protokoly. PMIRP umožňuje automatizovaný, standardizovaný sběr klíčových ukazatelů výkonnosti (KPI), jako je úspěšnost sestavení hovoru, úspěšnost předání hovoru, propustnost, latence a vytížení zdrojů, ze všech síťových prvků bez ohledu na výrobce. Tato získaná data jsou základním předpokladem pro monitorování výkonu sítě, odstraňování problémů, plánování kapacity a optimalizaci.

## K čemu slouží

PMIRP byl vytvořen, aby řešil problém výrobci specifických a různorodých rozhraní pro správu výkonnosti ve vícevýrobcových telekomunikačních sítích. Před standardizací poskytoval každý výrobce síťového zařízení své vlastní unikátní rozhraní a datový model pro získávání měření výkonnosti, což nutilo operátory vyvíjet pro jejich OSS vlastní, nákladné a křehké integrace. Primárním účelem PMIRP je poskytnout jednotné, standardizované rozhraní pro sběr dat a řízení výkonnosti, které umožní interoperabilitu více výrobců a sníží náklady na integraci. Tvoří součást širšího rámce IRP organizace 3GPP, jehož cílem je standardizovat všechny hlavní oblasti správy (poruchy, konfigurace, účtování, výkonnost a zabezpečení - FCAPS). Definováním společného objektového modelu a sady operací pro správu výkonnosti umožňuje PMIRP operátorům nasadit jediný manažerský systém, který může sbírat konzistentní data o výkonnosti ze všech síťových prvků, což usnadňuje přesnou analýzu a korelaci KPI v celé síti. Jeho zavedení, zejména od Release 8 společně se zavedením LTE/EPC, bylo klíčové pro automatizovaný provoz moderních, komplexních a softwarově řízených mobilních sítí. Reaguje na potřebu efektivního, škálovatelného a spolehlivého monitorování výkonnosti pro zajištění kvality služeb a proaktivní údržby sítě.

## Klíčové vlastnosti

- Standardizovaný informační model pro úlohy měření výkonnosti (PM-Jobs) a výsledky (PM-Results)
- Definuje operace pro správu životního cyklu PM-Jobs (vytvořit, upravit, smazat, pozastavit, obnovit)
- Podporuje získávání historických a aktuálních dat měření výkonnosti
- Poskytuje notifikační mechanismy pro změny stavu úlohy a poplachy překročení prahových hodnot
- Umožňuje definici granularity měření (např. 15minutová, 1hodinová, 24hodinová)
- Protokol-neutrální návrh s vazbami na technologie jako CORBA a Webové služby

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TS 32.411** (Rel-19) — PM IRP Requirements
- **TS 32.412** (Rel-19) — PM IRP Information Service Specification
- **TS 32.415** (Rel-9) — PM IRP XML Definitions for Performance Management
- **TS 32.416** (Rel-19) — PM IRP Solution Set Definitions

---

📖 **Anglický originál a plná specifikace:** [PMIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmirp/)
