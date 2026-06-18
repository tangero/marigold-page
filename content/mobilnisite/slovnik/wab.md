---
slug: "wab"
url: "/mobilnisite/slovnik/wab/"
type: "slovnik"
title: "WAB – Wireless Access Backhaul"
date: 2025-01-01
abbr: "WAB"
fullName: "Wireless Access Backhaul"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/wab/"
summary: "Wireless Access Backhaul (WAB) je koncept 3GPP pro využití stejné technologie rádiového přístupu (jako NR) k poskytování jak uživatelského přístupu, tak přenosu v síti. Umožňuje flexibilní a nákladově"
---

WAB (bezdrátový přístupový přenos) je koncept 3GPP pro využití stejné rádiové technologie k poskytování jak uživatelského přístupu, tak přenosu v síti, což umožňuje flexibilní zahušťování sítě eliminací samostatných kabelových připojení.

## Popis

Wireless Access Backhaul (WAB) je základní architektonický koncept v rámci frameworku Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)) od 3GPP. Odkazuje na princip využití stejné technologie rozhraní New Radio (NR) pro dvě odlišné funkce: poskytování přístupových spojů ke koncovým uživatelským zařízením (UE) a vytváření bezdrátových přenosových spojů mezi síťovými uzly. Toto duální využití spektra a rádiových zdrojů je klíčovým prvkem IAB, kde IAB uzel funguje jako přenosový uzel. IAB uzel má funkci Mobile Termination ([MT](/mobilnisite/slovnik/mt/)), která jej připojuje směrem vzhůru k nadřazenému uzlu (dalšímu IAB uzlu nebo IAB donoru) přes bezdrátové přenosové spojení, a funkci Distributed Unit ([DU](/mobilnisite/slovnik/du/)), která poskytuje přístupová spojení směrem dolů k UE nebo případně dalším IAB uzlům. Koncept WAB je realizován prostřednictvím sofistikovaného časového multiplexování ([TDM](/mobilnisite/slovnik/tdm/)) rádiových zdrojů, kdy jsou specifické časové sloty nebo symboly přiděleny pro přenosová vysílání a jiné pro přístupová vysílání, čímž se zabraňuje vlastní interferenci. To vyžaduje těsnou koordinaci a plánování, řízené Central Unit ([CU](/mobilnisite/slovnik/cu/)) IAB donoru, která používá modifikované zprávy aplikačního protokolu F1 (F1-AP) přes kanály [RRC](/mobilnisite/slovnik/rrc/) a [RLC](/mobilnisite/slovnik/rlc/) ke konfiguraci MT a DU IAB uzlu. Architektura je detailně popsána v technických specifikacích jako 38.300 a 38.401, zatímco specifické protokoly řídicí roviny (38.413) a uživatelské roviny (38.423) zajišťují spolehlivé směrování dat a správu topologie v celé více-skokové bezdrátové přenosové síti. WAB je klíčový pro umožnění rychlého a nákladově efektivního nasazení hustých 5G sítí, zejména v oblastech, kde je pokládka optických vláken nepraktická nebo neúměrně drahá.

## K čemu slouží

Hlavním účelem WAB je řešit ekonomický a logistický 'přenosový problém' spojený se zahušťováním sítí pro 5G a další generace. Tradiční nasazení small cell vyžaduje vyhrazené, vysokokapacitní kabelové (obvykle optické) připojení pro přenos, což je často nejnákladnější a nejčasověji náročnější část nasazení, zejména v městských kaňonech, na dočasných akcích nebo ve venkovských oblastech. WAB, jakožto princip umožňující [IAB](/mobilnisite/slovnik/iab/), to řeší tím, že činí přenos bezdrátovým a využívá k němu nasazenou NR infrastrukturu. Tím odstraňuje závislost na dostupnosti optiky v každé lokalitě uzlu. Motivace vychází z potřeby ultra-hustých sítí pro splnění požadavků na kapacitu a pokrytí u enhanced Mobile Broadband (eMBB) a pro podporu vysokofrekvenčních pásem (mmWave) s omezeným dosahem. Historicky se pro bezdrátový přenos používala samostatná mikrovlnná spojení, ale ta fungovala na jiném spektru a vyžadovala odlišné, často proprietární, vybavení. WAB bezproblémově integruje přenos do standardu 3GPP NR, což umožňuje jednotnou správu spektra, zjednodušené plánování sítě a dynamické přidělování zdrojů mezi přístup a přenos na základě reálné poptávky, čímž budoucím způsobem zabezpečuje nasazení sítí.

## Klíčové vlastnosti

- Využívá stejné rozhraní NR jak pro uživatelská přístupová, tak pro síťová přenosová spojení
- Umožňuje funkčnost uzlu Integrated Access and Backhaul (IAB) jako přenosového uzlu
- Používá časový multiplex (TDM) k oddělení přístupových a přenosových přenosů
- Podporováno modifikovanými protokoly F1-AP pro řídicí rovinu (38.413) a uživatelskou rovinu (38.423) přes bezdrátový přenos
- Umožňuje více-skokové, síťové topologie pro rozšířené pokrytí
- Usnadňuje dynamické přidělování zdrojů mezi přístup a přenos na základě zatížení provozem

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.799** (Rel-19) — Study on Additional Topological Enhancements for NR

---

📖 **Anglický originál a plná specifikace:** [WAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/wab/)
