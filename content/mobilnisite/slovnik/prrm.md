---
slug: "prrm"
url: "/mobilnisite/slovnik/prrm/"
type: "slovnik"
title: "PRRM – Positioning Radio Resource Management"
date: 2025-01-01
abbr: "PRRM"
fullName: "Positioning Radio Resource Management"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/prrm/"
summary: "Soubor procedur v rámci RAN pro správu rádiových prostředků specificky pro služby založené na poloze. Koordinuje přidělování fyzických kanálů, výkonu a časování pro podporu lokalizačních měření, jako"
---

PRRM je soubor procedur RAN pro správu rádiových prostředků, jako jsou kanály a výkon, s cílem podporovat síťově asistované lokalizační služby bez degradace celkového rádiového výkonu.

## Popis

Positioning Radio Resource Management (PRRM) je klíčová funkční entita v architektuře rádiové přístupové sítě (RAN), definovaná pro správu rádiových prostředků potřebných pro lokalizaci uživatelského zařízení (UE). Funguje jako součást vrstvy řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a komunikuje s prvky jádra sítě, jako je Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). Hlavní úlohou PRRM je zajišťovat nastavení, údržbu a uvolňování vyhrazených rádiových prostředků pro účely lokalizace, což zahrnuje konfiguraci měřicích mezer, plánování lokalizačních referenčních signálů ([PRS](/mobilnisite/slovnik/prs/)) a koordinaci hlášení měření z UE. Tento management je zásadní, protože lokalizační činnosti, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), spotřebovávají šířku pásma v uplinku i downlinku a vyžadují přesnou časovou synchronizaci; PRRM zajišťuje efektivní přidělení těchto prostředků bez nadměrného rušení nebo degradace kvality služby pro ostatní komunikační kanály.

Architektonicky jsou funkce PRRM rozděleny mezi síť a UE. Na straně sítě uzel RAN (např. Node B, eNodeB nebo gNB) provádí procedury PRRM na základě požadavků od lokalizačního serveru jádra sítě. Tyto procedury zahrnují rozhodování o tom, které bloky fyzických prostředků ([PRB](/mobilnisite/slovnik/prb/)), časové sloty a kmitočtová pásma přidělit pro lokalizační signály. Pro metody založené na downlinku, jako je OTDOA, PRRM konfiguruje vysílání PRS z více buněk a zajišťuje, aby byly vysílány s dostatečným výkonem a v určitých periodických intervalech, aby je UE mohlo detekovat. Pro metody založené na uplinku, jako je Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)), PRRM plánuje vysílání sondovacích referenčních signálů (SRS) určených pro lokalizaci z UE. Entita PRRM také spravuje související signalizaci, jako jsou zprávy RRC, které přenášejí lokalizační pomocná data (např. informace o konfiguraci PRS) k UE a které příkazují UE provést konkrétní měření.

Klíčové součásti PRRM zahrnují mechanismy řízení měření a hlášení, algoritmy plánování prostředků a rozhraní pro koordinaci lokalizace. Řízení měření zahrnuje odesílání zpráv Measurement Control protokolem RRC k UE, které specifikují typ lokalizačního měření (např. Reference Signal Time Difference (RSTD) pro OTDOA), buňky k měření a kritéria pro hlášení. PRRM spolupracuje s dalšími funkcemi RAN, jako je Admission Control a Packet Scheduling, aby zajistila, že přidělení prostředků pro lokalizaci je povoleno pouze v případě dostupnosti dostatečných rádiových prostředků, čímž se udržuje celková stabilita sítě. Její role je obzvláště důležitá v přeplněných městských prostředích nebo během nouzových scénářů, kde jsou přesné informace o poloze prvořadé; dynamickou správou prostředků PRRM pomáhá vyvažovat přesnost lokalizace s hlavním cílem sítě poskytovat spolehlivé hlasové a datové služby.

## K čemu slouží

PRRM bylo zavedeno, aby řešilo rostoucí potřebu síťově asistovaných lokalizačních služeb v celulárních sítích, vyžadovaných regulačními požadavky jako Enhanced 911 (E911) ve Spojených státech a podobnými službami lokalizace nouzových volajících po celém světě. Před jeho standardizací rané mobilní sítě postrádaly vyhrazené mechanismy pro správu rádiových prostředků pro lokalizaci, což vedlo k ad-hoc implementacím, které mohly vážně ovlivnit kapacitu a výkon sítě. Například bez koordinované správy prostředků mohla lokalizační měření způsobit nadměrné rušení, vybíjet baterii UE kvůli neustálému prohledávání nebo selhávat v hustých městských zástavbách, kde převládají odrazy signálu. Vytvoření PRRM poskytlo standardizovaný, efektivní rámec v rámci 3GPP pro integraci lokalizačních služeb přímo do paradigmatu správy prostředků RAN.

Tato technologie řeší problém, jak provádět přesnou lokalizaci UE bez degradace kvality primárních komunikačních služeb. Umožňuje síti dynamicky přidělovat a uvolňovat potřebné časově-kmitočtové prostředky pro lokalizační signály a měření na požádání. To je klíčové pro techniky jako OTDOA, které vyžadují, aby více základnových stanic vysílalo speciálně navržené referenční signály (PRS) v známých časech. PRRM zajišťuje, že tato vysílání jsou plánována koordinovaně napříč buňkami, čímž minimalizuje intracelulární a intercelulární rušení. Dále spravuje kompromis mezi přesností lokalizace (která těží z více prostředků a častých měření) a efektivitou sítě. Díky vyhrazené řídicí entitě může síť podporovat různé lokalizační metody – včetně těch založených na LTE, NR a hybridních přístupech – škálovatelným a budoucím vývojem odolným způsobem.

Historicky zavedení PRRM v 3GPP Release 99 položilo základy pro všechna následná vylepšení v celulární lokalizaci. Představovalo posun od samostatných GPS řešení, která byla v interiérech nespolehlivá, k síťově asistovaným hybridním metodám. Počáteční architektura definovala základní procedury pro vyjednávání prostředků mezi RAN a lokalizačním serverem jádra sítě. V průběhu releasů, jak se požadavky na přesnost lokalizace zpřísňovaly (např. pro komerční služby založené na poloze a sledování majetku IoT), se PRRM vyvíjelo, aby podporovalo nové signály, vyšší šířky pásma a agregaci nosných, ale jeho základní účel efektivní správy rádiových prostředků pro lokalizaci zůstal nezměněn.

## Klíčové vlastnosti

- Spravuje přidělování bloků fyzických prostředků (PRB) pro vysílání lokalizačních referenčních signálů
- Koordinuje měřicí mezery a plánování, aby umožnila lokalizační měření UE bez narušení datových služeb
- Podporuje více lokalizačních metod včetně OTDOA, A-GNSS a E-CID prostřednictvím standardizovaných procedur RRC
- Komunikuje s lokalizačními servery jádra sítě (např. SMLC, LMF) k provedení lokalizačních požadavků
- Řídí konfigurace a kritéria hlášení měření UE pro lokalizaci
- Vyvažuje požadavky na přesnost lokalizace s celkovou kapacitou sítě a úrovněmi rušení

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [PRRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/prrm/)
