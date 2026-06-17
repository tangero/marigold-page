---
slug: "dvd"
url: "/mobilnisite/slovnik/dvd/"
type: "slovnik"
title: "DVD – Digital Versatile Disc"
date: 2026-01-01
abbr: "DVD"
fullName: "Digital Versatile Disc"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dvd/"
summary: "V 3GPP se termín DVD vztahuje k formátu fyzického média Digital Versatile Disc, který je specifikován pro použití při testování a jako referenční úložné médium. Je relevantní pro testování shody multi"
---

DVD je standardizovaný formát fyzického média používaný v 3GPP pro testování shody a jako stabilní referenční úložné médium pro validaci multimediálních kodeků a formátů souborů.

## Popis

Ve specifikacích 3GPP je Digital Versatile Disc (DVD) definován nikoli jako služba, ale jako konkrétní formát fyzického úložného média používaný pro referenční účely, především v testovacích scénářích. Architektura zahrnuje fyzické specifikace DVD (např. rozměry disku, strukturu datové vrstvy, odrazivost) a logický souborový systém (UDF a [ISO](/mobilnisite/slovnik/iso/) 9660). Slouží jako kontejner pro testovací sekvence a referenční multimediální obsah. Klíčové komponenty zahrnují polykarbonátový substrát, reflexní datovou vrstvu (jednovrstvou nebo dvouvrstvou), rozteč stop a schéma korekce chyb. Data jsou kódována pomocí modulace Eight-to-Fourteen Modulation Plus (EFM+) a uložena ve spirálové stopě z prohlubní (pits) a plošin (lands).

Při provozu by testovaná entita 3GPP (např. UE nebo testovaný síťový simulátor) četla předdefinované audiovizuální soubory uložené na kompatibilním DVD médiu. Specifikace podrobně popisují požadované vlastnosti DVD-ROM (Read-Only Memory) používaného pro ukládání materiálu pro testování shody. Tím je zajištěno, že všechny laboratoře a výrobci používají identický, stabilní zdroj testovacího obsahu, což eliminuje variabilitu způsobenou úložnými médii. Příslušné specifikace 3GPP definují přesný typ DVD (např. DVD-ROM, DVD-R), kapacitu a rozložení souborového systému, které mají být použity pro ukládání testovacích sekvencí pro kodeky jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo [HEVC](/mobilnisite/slovnik/hevc/).

Jeho role v síťovém ekosystému je nepřímá, ale pro zajištění kvality klíčová. Poskytuje standardizovaný fyzický zdroj testovacích vektorů používaných při validaci implementací multimediální telefonie, paketově přepínané streamovací služby (PSS) a multimediální vysílací/multicastové služby ([MBMS](/mobilnisite/slovnik/mbms/)). Tím, že 3GPP nařizuje použití konkrétního, široce dostupného fyzického formátu, zajišťuje reprodukovatelnost a přesnost testů shody pro dekódování médií, synchronizaci a parsování formátů souborů napříč různými zařízeními a síťovými elementy.

## K čemu slouží

Účelem specifikace DVD ve standardech 3GPP bylo vytvořit spolehlivé, standardizované fyzické médium pro distribuci sad testů shody. Tím bylo vyřešeno problému nekonzistence testovacího materiálu, kdy použití různých úložných zařízení nebo přenos digitálních souborů mohlo zavést nezamýšlené odchylky. Standardizované DVD zajišťuje, že každý tester používá bitově identickou kopii referenčních audio a video sekvencí, což je klíčové pro reprodukovatelné testování složitých multimediálních kodeků a protokolů.

Historicky, jak se služby 3GPP rozvíjely a zahrnovaly bohatá multimédia, se stalo nezbytným rigorózní testování pro interoperabilitu. Před touto specifikací mohly zkušebny a výrobci používat různá CD-R, pevné disky nebo síťová úložiště, což vedlo k možným nesrovnalostem. Zavedení formátu DVD-ROM, představeného v Rel-12, poskytlo médium s velkou kapacitou, odolné a univerzálně čitelné. Vyřešilo omezení [CD](/mobilnisite/slovnik/cd/) s nižší kapacitou a méně formalizovaných metod digitální distribuce a vytvořilo řízený fyzický artefakt pro testovací materiál, který podporuje velké velikosti souborů testovacích sekvencí vysokého rozlišení vyžadovaných pro pokročilou validaci kodeků.

## Klíčové vlastnosti

- Standardizovaný fyzický formát (typ DVD-ROM) pro distribuci testovacího materiálu
- Vysoká úložná kapacita (4,7 GB pro jednovrstvé, 8,5 GB pro dvouvrstvé) pro testovací sekvence HD videa
- Specifikované použití souborového systému UDF/ISO 9660 pro univerzální čitelnost
- Definován jako referenční zdroj pro testování shody multimediálních kodeků a formátů souborů
- Zajišťuje bitově přesnou reprodukovatelnost testovacích vektorů v různých testovacích laboratořích
- Odolné fyzické médium vhodné pro archivaci a distribuci sad testů

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements

---

📖 **Anglický originál a plná specifikace:** [DVD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dvd/)
