---
slug: "btfd"
url: "/mobilnisite/slovnik/btfd/"
type: "slovnik"
title: "BTFD – Blind Transport Format Detection"
date: 2025-01-01
abbr: "BTFD"
fullName: "Blind Transport Format Detection"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/btfd/"
summary: "Mechanismus na straně přijímače ve WCDMA, který umožňuje detekci parametrů transportního formátu bez explicitní signalizace od vysímače. Analyzuje charakteristiky přijímaného signálu, aby určil skuteč"
---

BTFD je mechanismus na straně přijímače ve WCDMA, který detekuje parametry transportního formátu analýzou přijímaného signálu, čímž odstraňuje potřebu explicitní signalizace od vysílače.

## Popis

Blind Transport Format Detection (BTFD) je klíčová technologie fyzické vrstvy v systémech 3GPP [WCDMA](/mobilnisite/slovnik/wcdma/), která umožňuje přijímači autonomně určit kombinaci transportního formátu ([TFC](/mobilnisite/slovnik/tfc/)) použitou pro přenos, aniž by se spoléhal na explicitní signalizaci od vysílače. Mechanismus funguje analýzou statistických vlastností přijímaného signálu, kódů pro detekci chyb a struktury protokolu, aby identifikoval, která z několika možných kombinací transportního formátu byla skutečně přenesena. Tento proces zahrnuje sofistikované algoritmy zpracování signálu, které porovnávají přijatá data s více možnými dekódovacími hypotézami odpovídajícími různým transportním formátům.

Na technické úrovni BTFD funguje využitím struktury řetězce zpracování transportního kanálu ve WCDMA. Přijímač zpracovává příchozí signál prostřednictvím více paralelních dekódovacích cest, z nichž každá je nakonfigurována s různými parametry transportního formátu včetně velikosti transportního bloku, počtu transportních bloků a schématu kanálového kódování. Každá hypotéza je vyhodnocována pomocí metrik, jako jsou výsledky ověření [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check), poměry věrohodnosti a statistické vlastnosti dekódovaných dat. Hypotéza, která poskytne platnou kontrolu CRC nebo nejvyšší metriku věrohodnosti, je vybrána jako správná kombinace transportního formátu.

Klíčovými součástmi implementace BTFD jsou modul generování hypotéz, který vytváří všechny možné kombinace transportního formátu na základě sady kombinací transportního formátu ([TFCS](/mobilnisite/slovnik/tfcs/)), paralelní dekódovací jednotky, které zpracovávají signál podle každé hypotézy, a rozhodovací logika, která vyhodnocuje výsledky dekódování. Systém musí také zahrnovat mechanismy pro zpracování nejednoznačných případů, kdy více hypotéz poskytne platné výsledky, typicky prostřednictvím dodatečné statistické analýzy nebo kontrol konzistence na úrovni protokolu. BTFD funguje ve spolupráci s dalšími funkcemi fyzické vrstvy, jako je odhad kanálu, ekvalizace a řízení výkonu, aby zajistil spolehlivou detekci formátu za různých podmínek kanálu.

V architektuře WCDMA je BTFD primárně implementováno v uživatelském zařízení (UE) pro příjem v uplinku na Node B a v Node B pro příjem v downlinku na UE. Mechanismus je obzvláště důležitý pro služby s proměnnou rychlostí, kde se datová rychlost dynamicky mění na základě požadavků obsahu a podmínek kanálu. Odstraněním potřeby explicitních indikátorů transportního formátu v řídicím kanálu fyzické vrstvy BTFD snižuje režii signalizace a zlepšuje spektrální účinnost, což je zvláště cenné pro bezdrátové systémy s omezenou šířkou pásma.

## K čemu slouží

BTFD bylo vyvinuto k řešení základní výzvy efektivní podpory služeb s proměnnou rychlostí ve [WCDMA](/mobilnisite/slovnik/wcdma/) systémech bez spotřeby nadměrné šířky pásma pro řídicí signalizaci. V raných mobilních komunikačních systémech dominovaly služby s pevnou rychlostí a parametry transportního formátu mohly být konfigurovány polostaticky. S nástupem multimediálních služeb vyžadujících dynamickou adaptaci rychlosti však byl potřeba efektivnější mechanismus pro komunikaci informací o transportním formátu mezi vysílačem a přijímačem.

Před implementací BTFD systémy buď používaly pevné transportní formáty (neefektivní pro provoz s proměnnou rychlostí), nebo vyhrazené signalizační kanály k explicitnímu označení transportního formátu pro každý přenos. Explicitní signalizační přístup spotřebovával cenné rádiové zdroje, které by jinak mohly být použity pro přenos dat, čímž snižoval celkovou kapacitu systému. To bylo obzvláště problematické pro služby jako hlas s detekcí aktivity, streamování videa s proměnnou kompresí a interaktivní datové aplikace, kde se optimální datová rychlost často mění na základě charakteristik obsahu a stavu sítě.

BTFD tyto omezení vyřešilo přesunutím určení transportního formátu na stranu přijímače, čímž odstranilo potřebu explicitních indikátorů formátu v řídicím kanálu. Tato inovace byla motivována potřebou maximalizovat spektrální účinnost v systémech 3. generace při současné podpoře různých požadavků QoS nově vznikajících multimediálních služeb. Tím, že umožnilo přijímači 'naslepo' detekovat transportní formát ze samotného přijímaného signálu, umožnilo BTFD WCDMA systémům dosáhnout vyšší datové propustnosti, lepší podpory služeb s proměnnou rychlostí a efektivnějšího využití rádiových zdrojů ve srovnání s předchozími přístupy.

## Klíčové vlastnosti

- Autonomní detekce transportního formátu bez explicitní signalizace
- Paralelní testování hypotéz více možných kombinací transportního formátu
- Ověřování založené na CRC a vyhodnocování metrik věrohodnosti pro výběr hypotézy
- Podpora služeb s proměnnou rychlostí s dynamickými změnami transportního formátu
- Snížená režie řídicího kanálu ve srovnání s metodami explicitní signalizace
- Integrace se zpracováním fyzické vrstvy WCDMA včetně kanálového kódování a prokládání

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [BTFD na 3GPP Explorer](https://3gpp-explorer.com/glossary/btfd/)
