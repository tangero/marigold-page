---
slug: "jvet"
url: "/mobilnisite/slovnik/jvet/"
type: "slovnik"
title: "JVET – Joint Video Exploratory Group"
date: 2025-01-01
abbr: "JVET"
fullName: "Joint Video Exploratory Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jvet/"
summary: "Společná pracovní skupina 3GPP a ITU-T, která zkoumala a vyvinula standard Všestranného kódování videa (VVC/H.266). Měla klíčovou úlohu při definování kodeku videa nové generace pro služby ultra-high-"
---

JVET je společná pracovní skupina 3GPP a ITU-T, která zkoumala a vyvinula standard Všestranného kódování videa (Versatile Video Coding, VVC/H.266) pro služby videa nové generace.

## Popis

Skupina Joint Video Exploratory Group (JVET) byla společný technický orgán zřízený ve spolupráci [ITU-T](/mobilnisite/slovnik/itu-t/) Study Group 16 (VCEG) a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) JTC 1/SC 29 ([MPEG](/mobilnisite/slovnik/mpeg/)). V kontextu 3GPP se na práci JVET odkazuje a je přijímána za účelem standardizace pokročilého kódování videa pro multimediální služby. Hlavním výsledkem práce skupiny je standard Všestranného kódování videa (VVC), známý také jako H.266. Architektura VVC navazuje na hybridní rámec blokového kódování svých předchůdců (jako je [HEVC](/mobilnisite/slovnik/hevc/)/H.265), ale zavádí četná technická vylepšení. Funguje tak, že rozděluje snímek videa na bloky a využívá sofistikované techniky predikce (intra-frame a inter-frame), transformace, kvantizace a entropického kódování k odstranění prostorové a časové redundance. Mezi klíčové inovace patří flexibilnější struktura dělení bloků využívající QuadTree plus Multi-Type Tree (QTMT), pokročilá predikce pohybových vektorů a adaptivní smyčkové filtry.

Kódovací proces začíná rozdělením snímku na jednotky kódovacího stromu (Coding Tree Units, [CTU](/mobilnisite/slovnik/ctu/)), které lze rekurzivně dělit kombinací čtyřstromového a binárního/ternárního dělení, což umožňuje mnohem přesnější přizpůsobení detailům obsahu než rigidní čtyřstrom HEVC. Pro predikci používá intra-predikce široké spektrální směrových režimů, zatímco inter-predikce zahrnuje pokročilé techniky jako afinní pohybová predikce pro komplexní pohyby a zpřesňování pohybových vektorů na straně dekodéru. Fáze transformace může adaptivně aplikovat více transformačních voleb (DCT-II, DST-VII). Po kvantizaci se pro entropické kódování používá kontextově adaptivní binární aritmetické kódování ([CABAC](/mobilnisite/slovnik/cabac/)) s několika vylepšeními pro vyšší propustnost. Tyto komponenty společně pracují na dosažení hlavního cíle: výrazného snížení datového toku – přibližně o 50 % oproti HEVC při stejné subjektivní kvalitě videa.

V ekosystému 3GPP specifikace (např. TS 26.855, TS 26.928) definují, jak je VVC zabaleno a transportováno pro multimediální služby, zejména pro 5G. Jeho úlohou je umožnit efektivní doručování aplikací videa náročných na šířku pásma, jako je streamování 4K/8K, 360stupňové video a imerzní média v mobilních sítích. Díky radikálnímu zlepšení kompresní účinnosti VVC snižuje zatížení sítě a nároky na úložný prostor, což je klíčové pro uskutečnění a ekonomickou udržitelnost pokročilých video služeb ve scénářích rádiového přístupu s omezenou kapacitou. Standardy 3GPP zajišťují interoperabilitu specifikací profilů kodeku, úrovní a zapouzdření VVC bitstreamů v multimediálních kontejnerech pro navázání a doručení relace.

## K čemu slouží

JVET byla zřízena, aby řešila rostoucí poptávku po vyšších rozlišeních videa (4K, 8K, [HDR](/mobilnisite/slovnik/hdr/)), imerzních formátech (VR/360°) a efektivnější kompresi videa pro streamování a ukládání. Předchozí standard, Vysokoúčinné kódování videa (High Efficiency Video Coding, HEVC/H.265), přestože představoval významný pokrok oproti H.264/AVC, čelil výzvám včetně složitého licencování patentů a jeho kompresní zisky již přestávaly stačit pro novou vlnu ultra-high-definition obsahu. Exponenciální růst video provozu, u kterého se předpokládá, že bude dominovat mobilním datům, vytvořil naléhavou potřebu nového kodeku, který by mohl dramaticky snížit datové toky bez ztráty kvality, aby byly budoucí video služby udržitelné pro provozovatele sítí.

Vznik JVET a standardu VVC byl motivován snahou dosáhnout generačního skoku v účinnosti kódování. Společným využitím odborných znalostí ITU-T i ISO/IEC chtěla skupina vytvořit technicky nadřazený a široce přijímaný standard. Pro 3GPP a mobilní průmysl byl účel jasný: definovat video kodek, který bude základem multimediálního zážitku 5G. Efektivní kódování videa je pilířem případů užití 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB) a hromadný internet věcí (IoT) s video senzory. VVC řeší problém přenosu extrémně kvalitního videa přes bezdrátové spoje, kde je spektrum vzácným a drahým zdrojem, což umožňuje nové obchodní modely a uživatelské zážitky při současném zvládání zahlcení sítě.

## Klíčové vlastnosti

- ~50% snížení datového toku ve srovnání s HEVC při stejné vizuální kvalitě
- Flexibilní dělení bloků pomocí struktury QuadTree plus Multi-Type Tree (QTMT)
- Pokročilá pohybová kompenzace s afinním pohybem a zpřesňováním pohybových vektorů na straně dekodéru
- Rozšířená intra-predikce se 67 směrovými režimy
- Adaptivní výběr z více transformací (DCT-II, DST-VII)
- Vylepšené entropické kódování využívající CABAC s vyšší propustností

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.855** (Rel-19) — Study on Film Grain Synthesis
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [JVET na 3GPP Explorer](https://3gpp-explorer.com/glossary/jvet/)
