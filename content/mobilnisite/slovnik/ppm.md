---
slug: "ppm"
url: "/mobilnisite/slovnik/ppm/"
type: "slovnik"
title: "PPM – Packed Picture Mapping"
date: 2025-01-01
abbr: "PPM"
fullName: "Packed Picture Mapping"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ppm/"
summary: "PPM je technika komprese a mapování dat používaná v rádiových přístupových sítích 3GPP pro efektivní přenos obrazových dat přes rozhraní vzdušného rozhraní. Optimalizuje využití šířky pásma zabalování"
---

PPM je technika komprese a mapování dat používaná v rádiových přístupových sítích 3GPP pro efektivní zabalení obrazových informací do transportních bloků pro přenos přes rozhraní vzdušného rozhraní, čímž optimalizuje využití šířky pásma.

## Popis

Packed Picture Mapping (PPM) je specifický mechanismus zpracování dat definovaný ve specifikacích 3GPP pro rádiový přenos a příjem v uživatelském zařízení (UE). Funguje na fyzické vrstvě a zabývá se efektivním formátováním a mapováním obrazových dat na transportní kanály poskytované fyzickou vrstvou. Proces spočívá v převzetí obrazových informací, které mohou pocházet z aplikací vyšších vrstev, a jejich 'zabalení' do užitečného zatížení transportních bloků způsobem, který minimalizuje režii protokolu a maximalizuje využití přidělených rádiových zdrojů. Toto mapování se řídí přísnými pravidly popsanými v technických specifikacích 3GPP (TS), zejména těmi, které detailně popisují rádiové přístupové schopnosti a požadavky na výkon UE.

Architektura PPM je integrována v protokolovém zásobníku UE, konkrétně v rámci zpracovatelského řetězce vrstvy 1 ([L1](/mobilnisite/slovnik/l1/)). Když jsou obrazová data naplánována k přenosu, vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) doručí transportní bloky fyzické vrstvě. Funkce PPM poté na tyto bloky aplikuje svá specifická pravidla mapování před dalším zpracováním na fyzické vrstvě, jako je kanálové kódování, prokládání a modulace. Přesná implementace zajišťuje, že přijímač (Node B nebo gNB) může správně demapovat a rekonstruovat původní obrazová data. Její role je klíčová ve scénářích, kde je třeba přenášet obrazová nebo obrazová data s nízkou latencí a vysokou spolehlivostí, jako u raných multimediálních zpráv nebo základních služeb sdílení obrázků, protože přímo ovlivňuje spektrální účinnost a uživatelský zážitek.

Klíčové komponenty zapojené do PPM zahrnují mechanismus výběru kombinace transportního formátu ([TFC](/mobilnisite/slovnik/tfc/)), který spolupracuje s PPM při určování, jak jsou data zabalena, a samotné fyzické kanály, jako je vyhrazený fyzický datový kanál ([DPDCH](/mobilnisite/slovnik/dpdch/)) v UMTS. Specifikace jako TS 25.101, 25.102 a 25.103 detailně popisují požadavky na rádiový přenos a příjem UE, včetně aspektů výkonu souvisejících s PPM. Testovací specifikace jako TS 37.571 definují shodové testy pro zajištění správné implementace PPM v UE. Zatímco jeho význam poklesl s příchodem pokročilejších multimediálních kodeků a paketově přepínaných přenosů, PPM představovala důležitou optimalizaci pro okruhově přepínané a rané paketově přepínané obrazové služby v sítích 3G.

## K čemu slouží

PPM byla vytvořena k řešení výzvy efektivního přenosu obrazových dat přes rádiová rozhraní s omezenou šířkou pásma raných sítí 3G (UMTS). Na konci 90. a začátkem 2000 let bylo umožnění multimediálních služeb, jako je zasílání obrázků (vývoj z [SMS](/mobilnisite/slovnik/sms/)), klíčovým hybatelem pro 3G. Nezpracovaná obrazová data jsou však relativně velká a jejich přenos bez optimalizace by spotřeboval nadměrné rádiové zdroje, což by vedlo k nízké kapacitě sítě a vysoké uživatelské latenci. PPM byla vyvinuta jako standardizovaná metoda pro kompresi a mapování těchto dat přímo na fyzické vrstvě, čímž se snížila režie protokolu spojená s paketizací na vyšších vrstvách.

Historický kontext je zakořeněn ve vývoji UMTS Release 99, který zavedl vyhrazené kanály schopné přenášet uživatelská data. Předchozí systémy 2G jako GSM měly omezené datové schopnosti (přes okruhově přepínaná data nebo [GPRS](/mobilnisite/slovnik/gprs/)) a postrádaly standardizované, efektivní mechanismy pro přenos obrázků. PPM poskytovala definovaný, interoperabilní způsob pro UE a sítě, jak zacházet s tímto specifickým typem dat. Vyřešila problém neefektivního využití rádiového přenosu těsným zabalením obrazových informací do transportních bloků, čímž zlepšila efektivní datovou rychlost pro obrazové služby a vylepšila uživatelský zážitek pro rané uživatele mobilní multimédií.

## Klíčové vlastnosti

- Standardizovaná komprese a mapování obrazových dat na vrstvě 1
- Snižuje režii protokolu pro přenos obrazu
- Zlepšuje spektrální účinnost na vyhrazených transportních kanálech
- Definované shodové testy pro implementaci v UE
- Integrováno s mechanismem výběru kombinace transportního formátu (TFC)
- Použitelné pro oba režimy UMTS: FDD i TDD

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- **TS 37.571** (Rel-19) — UE Conformance for Positioning

---

📖 **Anglický originál a plná specifikace:** [PPM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppm/)
