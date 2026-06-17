---
slug: "ecm"
url: "/mobilnisite/slovnik/ecm/"
type: "slovnik"
title: "ECM – Error Correction Mode"
date: 2025-01-01
abbr: "ECM"
fullName: "Error Correction Mode"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ecm/"
summary: "Error Correction Mode (ECM) je funkce protokolu pro přenos faksimilí (fax) standardizovaná v 3GPP pro použití v mobilních sítích. Umožňuje detekci chyb a opakovaný přenos poškozených datových bloků bě"
---

ECM je funkce protokolu pro přenos faksimilí v mobilních sítích, která umožňuje detekci chyb a opakovaný přenos za účelem zajištění spolehlivého doručení dokumentu přes rádiové spoje.

## Popis

Error Correction Mode (ECM) je protokolový mechanismus navržený k zajištění přesného přenosu faksimilních (faxových) dat přes digitální mobilní sítě, jak je definováno ve specifikacích 3GPP. Během faxové relace funguje tak, že rozděluje přenášená data stránky na menší bloky, typicky o velikosti 256 nebo 64 oktetů v závislosti na implementaci. Každý datový blok je doprovázen kontrolním součtem rámce (Frame Check Sequence, [FCS](/mobilnisite/slovnik/fcs/)) pro detekci chyb. Příjemní faxový terminál při přijetí FCS zkontroluje; pokud je detekována chyba, signalizuje vysílacímu terminálu, aby daný konkrétní blok přenesl znovu. Tento proces pokračuje, dokud nejsou všechny bloky přijaty správně, nebo není dosaženo maximálního limitu opakování, načež může být relace ukončena. ECM je implementován v rámci protokolu T.30 pro fax přes [ISDN](/mobilnisite/slovnik/isdn/), přizpůsobený pro mobilní sítě prostřednictvím podpory faxových služeb v 3GPP přes okruhově přepínanou a později paketově přepínanou doménu.

Z architektonického hlediska funguje ECM na aplikační vrstvě pro faxové služby a rozhraní s transportními protokoly nižších vrstev poskytovanými mobilní sítí. V raných vydáních 3GPP (např. Rel-5) byly faxové služby primárně podporovány přes okruhově přepínaná spojení, jako v GSM nebo UMTS [CS](/mobilnisite/slovnik/cs/) datových hovorech. Síť poskytuje transparentní datový přenos a ECM funguje koncově mezi faxovými terminály nezávisle na technologii radiového přístupu. Mezi klíčové součásti patří vyjednávání schopnosti ECM faxového terminálu během fáze navázání spojení T.30, logika segmentace a opětovného složení bloků a mechanismus řízení opakovaného přenosu. Úlohou ECM je zmírnit chyby způsobené zhoršením rádiového kanálu, síťovými interferencemi nebo předáváním spojení, které jsou běžné v mobilním prostředí, a tím zabránit zkreslenému výstupu faxu.

Při provozu ECM přidává režii kvůli hlavičkám bloků a opakovaným přenosům, což může zvýšit dobu přenosu, ale zajišťuje věrnost dat. Je obzvláště důležitý pro mobilní fax, protože bezdrátové spoje jsou náchylnější k chybám ve srovnání s pevnými linkami. Specifikace 3GPP odkazují na ECM v kontextu faxové interoperability, což zajišťuje kompatibilitu se standardy [ITU-T](/mobilnisite/slovnik/itu-t/) T.30. Zatímco používání faxu pokleslo, ECM zůstává definovanou funkcí pro podporu starších služeb a regulační požadavky v některých regionech. Jeho zařazení do více vydání 3GPP zdůrazňuje potřebu spolehlivých služeb reálné komunikace přes vyvíjející se síťové technologie.

## K čemu slouží

ECM byl vytvořen, aby řešil výzvu spolehlivého přenosu faksimilních dokumentů přes nespolehlivé mobilní rádiové kanály. V raných mobilních sítích (např. GSM) byl fax kritickou obchodní službou, ale rádiové interference, útlum a předávání spojení mohly poškodit data, což vedlo k nečitelným faxovým stránkám. Bez opravy chyb byly faxové přenosy přes mobilní spoje často nespolehlivé, což omezovalo přijetí mobilních faxových služeb. ECM to řeší implementací robustního schématu detekce chyb a opakovaného přenosu, čímž zajišťuje integritu dokumentu podobně jako fax přes pevnou linku.

Historický kontext vychází ze standardu [ITU-T](/mobilnisite/slovnik/itu-t/) T.30 pro fax přes PSTN/[ISDN](/mobilnisite/slovnik/isdn/), který zahrnoval ECM pro řízení chyb. 3GPP to přijalo a přizpůsobilo pro mobilní sítě, aby zachovalo interoperabilitu s existujícími faxovými přístroji a sítěmi. Předchozí přístupy, jako základní faxové režimy bez ECM, trpěly vysokou mírou chyb v mobilním prostředí, což způsobovalo časté neúspěšné přenosy nebo zkreslené výstupy. ECM poskytlo standardizovanou metodu pro zmírnění těchto problémů, což umožnilo životaschopné mobilní faxové služby jako součást nabídky okruhově přepínaných dat 3GPP.

Motivace ECM také spočívá v podpoře starších služeb během přechodu na digitální mobilní systémy a zajištění zpětné kompatibility. Řešila omezení předchozích mobilních datových služeb, kterým chyběla oprava chyb na aplikační vrstvě pro fax v reálném čase. Začleněním ECM 3GPP umožnilo spolehlivý fax přes 2G, 3G a další generace, čímž splnilo regulační a obchodní potřeby přenosu dokumentů v odvětvích, jako je zdravotnictví a právo, kde fax zůstal zakořeněn.

## Klíčové vlastnosti

- Blokový přenos s kontrolním součtem rámce (Frame Check Sequence, FCS) pro detekci chyb
- Automatický opakovaný přenos poškozených datových bloků na žádost přijímače
- Schopnost vyjednávání během fáze navázání faxového spojení T.30 pro povolení nebo zakázání ECM
- Podpora velikostí bloků 256 oktetů (výchozí) a 64 oktetů (volitelné)
- Koncový provoz nezávislý na podkladovém transportu mobilní sítě
- Kompatibilita se standardem ITU-T T.30 pro faksimile přes ISDN

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.420** (Rel-19) — X2 Interface Introduction for E-UTRAN

---

📖 **Anglický originál a plná specifikace:** [ECM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecm/)
