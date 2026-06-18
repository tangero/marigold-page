---
slug: "png"
url: "/mobilnisite/slovnik/png/"
type: "slovnik"
title: "PNG – Portable Networks Graphics"
date: 2025-01-01
abbr: "PNG"
fullName: "Portable Networks Graphics"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/png/"
summary: "PNG je rastrový grafický formát souboru standardizovaný organizací 3GPP pro použití v mobilních službách, zejména pro službu multimediálních zpráv (MMS) a další multimediální aplikace. Poskytuje bezzt"
---

PNG je rastrový grafický formát souboru standardizovaný organizací 3GPP pro mobilní služby jako MMS, který poskytuje bezztrátovou kompresi a podporu průhlednosti pro přenos obrazu vysoké kvality.

## Popis

Portable Network Graphics (PNG) je rastrový grafický formát souboru, který podporuje bezztrátovou kompresi dat. V rámci ekosystému 3GPP je PNG standardizován jako podporovaný obrazový formát pro multimediální služby, primárně definovaný v specifikacích jako 3GPP TS 26.234 (Transparent end-to-end packet-switched streaming service) a 3GPP TS 26.928 (Media codec for streaming services). Jeho zařazení zajišťuje interoperabilitu obrazového obsahu mezi různými zařízeními a síťovými prvky v mobilní komunikaci.

Technicky PNG používá nepatentovaný bezztrátový kompresní algoritmus nazvaný DEFLATE, který kombinuje kódování LZ77 a Huffmanovo. To umožňuje efektivní ukládání a přenos bez ztráty kvality obrazu, což je klíčové pro mobilní sítě s omezenou přenosovou kapacitou. Formát podporuje obrazy s indexovanými barvami, odstíny šedi a plnobarevné obrazy spolu s volitelným alfa kanálem pro průhlednost. Tento alfa kanál umožňuje složité skládání obrazu, což je cenné pro prvky uživatelského rozhraní a bohatý multimediální obsah v mobilních aplikacích.

V architektuře 3GPP je PNG typicky zpracováván aplikační vrstvou a funkcemi pro zpracování médií. Pro služby jako [MMS](/mobilnisite/slovnik/mms/) musí centrum služby multimediálních zpráv (MMSC) a klientské aplikace podporovat dekódování a kódování PNG. Specifikace formátu ve standardech 3GPP zajišťuje, že všechna kompatibilní zařízení mohou správně zobrazit PNG obrázky, což usnadňuje konzistentní uživatelský zážitek. Jeho role je nedílnou součástí multimediálních schopností definovaných od vydání 3GPP Release 8 dále, podporujících vývoj bohatšího mobilního obsahu.

Technický návrh PNG zahrnuje funkce jako korekce gama a data pro korekci barev pro zachování konzistentního vzhledu obrazu na různých zobrazovacích zařízeních. To je obzvláště důležité v heterogenním mobilním prostředí s různými technologiemi obrazovek. Formát také podporuje prokládání, které umožňuje progresivní zobrazování obrazu, což může zlepšit vnímaný výkon při stahování obrazu přes pomalejší mobilní připojení. Ačkoli je PNG statický obrazový formát, jeho robustnost a široké přijetí z něj činí základní kámen pro služby založené na obrazech v sítích 3GPP.

## K čemu slouží

Primárním účelem standardizace PNG v rámci 3GPP bylo poskytnout spolehlivý, vysoce kvalitní a bezlicenčně poplatkový obrazový formát pro mobilní multimediální služby. Před jeho zařazením se mobilní služby často spoléhaly na proprietární nebo méně schopné formáty, což vedlo k problémům s kompatibilitou a nekonzistentním uživatelským zážitkům na různých zařízeních a sítích. PNG řešil potřebu bezztrátového kompresního formátu, který by dokázal zpracovat složité obrazy s průhledností, což se stávalo stále důležitějším pro pokročilé mobilní aplikace a uživatelská rozhraní.

Motivace pro přijetí PNG pramenila z rostoucí poptávky po bohatším multimediálním obsahu v mobilní komunikaci, zejména s nástupem [MMS](/mobilnisite/slovnik/mms/) a mobilního prohlížení internetu. Stávající formáty jako [GIF](/mobilnisite/slovnik/gif/) měly omezení, včetně patentových problémů a omezené palety barev. PNG nabídl technicky nadřazenou alternativu s lepší kompresní účinností pro určité typy obrazů a plnou podporou alfa průhlednosti. Standardizací PNG 3GPP zajistilo, že moderní, otevřený formát je dostupný pro všechna kompatibilní zařízení, což podporuje interoperabilitu a snižuje fragmentaci v mobilním ekosystému.

Historicky zařazení PNG do Release 8 korespondovalo s širším úsilím směrem k IP multimediálním službám v sítích 3G a 4G. Řešilo problém efektivního přenosu grafického obsahu vysoké věrnosti bez právních závazků, podporujíc tak odvětvový posun směrem k vizuálně bohatším aplikacím. Tato standardizace byla klíčovým umožňovatelem konzistentních multimediálních zážitků, jak se mobilní sítě vyvíjely z primárně hlasově orientovaných na datově orientované platformy.

## Klíčové vlastnosti

- Bezztrátová komprese využívající algoritmus DEFLATE
- Podpora plnobarevných obrazů, obrazů v odstínech šedi a obrazů s indexovanými barvami
- Alfa kanál pro proměnnou průhlednost (alfa skládání)
- Korekce gama a metadata pro korekci barev
- Prokládání pro progresivní zobrazování obrazu
- Detekce chyb prostřednictvím kontrolních součtů CRC

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G

---

📖 **Anglický originál a plná specifikace:** [PNG na 3GPP Explorer](https://3gpp-explorer.com/glossary/png/)
