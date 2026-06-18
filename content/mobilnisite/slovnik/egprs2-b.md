---
slug: "egprs2-b"
url: "/mobilnisite/slovnik/egprs2-b/"
type: "slovnik"
title: "EGPRS2-B – EGPRS2 Level B"
date: 2025-01-01
abbr: "EGPRS2-B"
fullName: "EGPRS2 Level B"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/egprs2-b/"
summary: "EGPRS2-B je vyšší výkonnostní úroveň rozšíření EGPRS2, která kombinuje modulace vyššího řádu s provozem na větší šířce pásma. Agreguje více nosných GSM o šířce 200 kHz, čímž dosahuje výrazně vyšších š"
---

EGPRS2-B je vyšší výkonnostní úroveň rozšíření EGPRS2, která agreguje více nosných GSM pro větší šířku pásma a vyšší špičkové přenosové rychlosti, a představuje maximální propustnost na vývojové cestě GSM.

## Popis

EGPRS2-B je jedna ze dvou definovaných výkonnostních úrovní [EGPRS2](/mobilnisite/slovnik/egprs2/), konkrétně navržená pro dosažení nejvyšších možných přenosových rychlostí v rámci architektury GSM. Navazuje na základ EGPRS2-A, ale přidává klíčovou vlastnost: zvýšenou symbolovou rychlost prostřednictvím rozšíření šířky pásma. Tato architektura vyžaduje mobilní stanice a síťové vybavení schopné vysílat a přijímat v šířce pásma až 1,6 MHz, což odpovídá osmi standardním časovým slotům GSM o šířce 200 kHz agregovaným dohromady. Toho je dosaženo použitím dvoukanálového nebo vícekanálového provozu na downlinku.

Provozně EGPRS2-B funguje tak, že uživatelskému zařízení (UE) jsou přidělovány prostředky na dvou nebo více nesousedních nosných o šířce 200 kHz současně. [BTS](/mobilnisite/slovnik/bts/) plánuje přenos dat přes tyto nosné a UE musí mít [RF](/mobilnisite/slovnik/rf/) schopnosti naladit se na tyto více nosných a zpracovávat je paralelně. Tento paralelní přenos efektivně zdvojnásobuje symbolovou rychlost ve srovnání s jedinou nosnou o šířce 200 kHz. V kombinaci s modulačními schématy vyššího řádu (jako je 32-QAM), která jsou také definována v EGPRS2, je špičková přenosová rychlost výrazně zvýšena. Mechanismus adaptace spojení je rozšířen, aby zvládal složitější podmínky kanálu na větší šířce pásma.

Klíčové komponenty pro EGPRS2-B zahrnují pokročilé RF front-endy v UE i BTS, které zvládnou větší okamžitou šířku pásma nebo rychlé přepínání mezi nosnými, výkonnější základnové procesory pro paralelní zpracování symbolových proudů a vylepšení vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro vícekanálové plánování a přidělování prostředků. Jeho úlohou je sloužit jako motor pro špičkové přenosové rychlosti v sítích GSM, cílený na uživatele v excelentních podmínkách pokrytí, kde rádiové prostředí dokáže podporovat náročnější požadavky na poměr signálu a šumu širokopásmových modulací vyššího řádu. Posouvá teoretické limity technologie GSM, aby konkurovala raným přenosovým rychlostem 3G.

## K čemu slouží

Účelem EGPRS2-B bylo posunout výkonnostní možnosti sítí GSM na jejich absolutní maximum, konkrétně s cílem téměř zdvojnásobit špičkové přenosové rychlosti ve srovnání s EGPRS2-A. Bylo vytvořeno k vyřešení problému omezené spektrální účinnosti jednoho kanálu; i s modulacemi vyššího řádu má kanál o šířce 200 kHz základní kapacitní limit. Agregací nosných EGPRS2-B tento limit překonává a poskytuje cestu k přenosovým rychlostem, které by v ideálních podmínkách mohly konkurovat nebo překonat raná nasazení [HSPA](/mobilnisite/slovnik/hspa/).

Toto bylo motivováno konkurenční potřebou operátorů GSM nabízet špičkové přenosové rychlosti srovnatelné s těmi, které byly inzerovány pro sítě 3G, zejména na trzích, kde bylo spektrum pro 3G vzácné nebo bylo jeho nasazování pomalé. Řešilo to omezení [EGPRS](/mobilnisite/slovnik/egprs/) a dokonce i EGPRS2-A, které byly v konečném důsledku limitovány úzkopásmovou povahou jediné nosné GSM. Přístup s větší šířkou pásma u EGPRS2-B byl přímou reakcí na vývoj směrem k širokopásmovosti, který byl vidět u jiných technologií jako LTE.

Dále poskytovalo případ užití pro operátory s fragmentovaným nebo nesouvislým spektrem GSM, umožňující jim spojit různé části spektra a vytvořit tak datovou přípojku s vyšší rychlostí. To bylo zvláště cenné pro maximalizaci návratnosti stávajících spektrálních aktiv před přechodem na 4G. EGPRS2-B ukázalo, že s dostatečnou inovací mohou i zastaralé systémy založené na [TDMA](/mobilnisite/slovnik/tdma/) stále poskytovat smysluplné širokopásmové uživatelské zkušenosti.

## Klíčové vlastnosti

- Provoz na větší šířce pásma až 1,6 MHz prostřednictvím agregace více nosných
- Dvoukanálový provoz na downlinku jako primární konfigurace
- Využívá modulační schémata vyššího řádu z EGPRS2 (např. 32-QAM)
- Vyžaduje vylepšené RF schopnosti UE a BTS pro větší šířku pásma
- Pokročilé vícekanálové plánování ve vrstvě MAC
- Poskytuje nejvyšší špičkové přenosové rychlosti na vývojové cestě GSM/EDGE

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [EGPRS2-B na 3GPP Explorer](https://3gpp-explorer.com/glossary/egprs2-b/)
