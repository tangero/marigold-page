---
slug: "usch"
url: "/mobilnisite/slovnik/usch/"
type: "slovnik"
title: "USCH – Uplink Shared Channel"
date: 2025-01-01
abbr: "USCH"
fullName: "Uplink Shared Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/usch/"
summary: "Transportní kanál v UMTS používaný pro přenos dat v uplinku, kde více uživatelů sdílí stejný fyzický zdroj. Umožňuje efektivní statistické multiplexování trhavého datového provozu, což ve srovnání s v"
---

USCH je transportní kanál v UMTS pro uplink, kde více uživatelů sdílí stejný fyzický zdroj pro efektivní přenos trhavých dat, čímž zvyšuje kapacitu a využití.

## Popis

Uplink Shared Channel (USCH) je transportní kanál definovaný v rádiové přístupové síti UMTS (Universal Mobile Telecommunications System), konkrétně pro systémy Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)). Funguje v rámci vrstev Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a fyzické vrstvy na straně User Equipment (UE) a Node B. Na rozdíl od vyhrazených kanálů ([DCH](/mobilnisite/slovnik/dch/)), které přidělují pevný kód a výkon jednomu uživateli po dobu trvání spojení, USCH umožňuje více UE přenášet paketová data na stejném fyzickém zdroji pro uplink, který je primárně definován konkrétním scrambling kódem a kanalizačním(i) kódem(kódy). Toto sdílení je dynamicky řízeno sítí na základě přenosového časového intervalu ([TTI](/mobilnisite/slovnik/tti/)).

Provoz USCH je úzce řízen pomocí příznaku Uplink State Flag ([USF](/mobilnisite/slovnik/usf/)), který je přenášen na přidružených downlink kanálech. Scheduler sítě, umístěný v Node B pro konfigurace související s [HSDPA](/mobilnisite/slovnik/hsdpa/) nebo v Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) pro starší verze, používá USF k udělení povolení konkrétní UE použít sdílený zdroj v následujícím dostupném uplink TTI. Když má UE data k odeslání, musí naslouchat jí přiřazené hodnotě USF. Po zjištění svého povolení přenáší UE svůj datový paket na USCH během určeného TTI. Tento mechanismus zabraňuje kolizím, protože v jednom TTI smí vysílat pouze jedna UE.

Z architektonického hlediska je USCH mapován na jeden nebo více fyzických kanálů, primárně Uplink Physical Shared Channel (UPSCH). Data z MAC vrstvy jsou segmentována do transportních bloků, které jsou následně kódovány, prokládány a rozprostřeny před přenosem. USCH podporuje proměnné datové rychlosti prostřednictvím výběru kombinace transportních formátů (TFC), což umožňuje přizpůsobení podmínkám na kanálu a datovým požadavkům. Jeho hlavní rolí je poskytnout efektivní transportní mechanismus pro nereálný čas, na zpoždění tolerantní paketové datové služby, jako je prohlížení webu nebo e-mail, kde je provoz ze své podstaty trhavý a přerušovaný. Sdílením zdrojů výrazně zlepšuje celkovou spektrální účinnost a kapacitu uplinku v síti UMTS ve srovnání s modelem založeným pouze na vyhrazených kanálech.

## K čemu slouží

USCH byl zaveden ve 3GPP Release 99, aby řešil neefektivitu používání vyhrazených kanálů pro vznikající paketově přepínané datové služby. Rané mobilní datové služby často spoléhaly na vyhrazená spojení, která rezervovala šířku pásma, kódy a výkon pro jediného uživatele i během období nečinnosti, kdy se žádná data nepřenášela. To bylo plýtvání vzácnými rádiovými zdroji, zejména pro asymetrický a trhavý internetový provoz, kde je uplink často nečinný.

Vytvoření USCH bylo motivováno potřebou zisků ze statistického multiplexování. Tím, že umožnil více uživatelům sdílet stejný fyzický kanál v časové oblasti, mohla síť obsloužit více uživatelů se stejným množstvím spektra, čímž zvýšila celkovou kapacitu a snížila cenu za bit. Vyřešil problém nízkého využití zdrojů pro datové služby typu best-effort, což umožnilo UMTS efektivněji konkurovat jiným širokopásmovým technologiím. USCH spolu se svým downlink protějškem (DSCH) vytvořil základ pro pokročilejší funkce paketového plánování a vysokorychlostních dat, které se později vyvinuly v HSPA.

## Klíčové vlastnosti

- Dynamické multiplexování více UE v časové oblasti na jednom fyzickém zdroji pro uplink
- Přístup založený na povolení řízený pomocí příznaku Uplink State Flag (USF)
- Podpora proměnných datových rychlostí prostřednictvím kombinací transportních formátů
- Efektivní transport pro trhavé, nereálného času paketové datové služby
- Vylepšená spektrální účinnost a kapacita uplinku oproti vyhrazeným kanálům
- Funguje na základě přenosového časového intervalu (TTI) pro plánování

## Související pojmy

- [USF – Uplink State Flag](/mobilnisite/slovnik/usf/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [USCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/usch/)
